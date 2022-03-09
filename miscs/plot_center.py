import sys
import os
import cv2
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from scipy.optimize import curve_fit, OptimizeWarning
import math
import warnings

from matplotlib.ticker import FormatStrFormatter
import matplotlib.style as mplstyle

# To fit with Gaussian distribution
def gaussian(x, a, x0, sigma, offset):
    return a * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2)) + offset

# Curve fitting
def get_middle_distance(frame_line_x, frame_line, forced=False, manual_mean=None):
    a0 = np.max(frame_line) - np.min(frame_line)
    offset0 = np.min(frame_line)
    n = sum(frame_line)

    with warnings.catch_warnings():
        warnings.filterwarnings('error')
        try:
            scale_factor = a0
            if forced:
                if manual_mean is None:
                    mean0_idx = np.average(np.where(frame_line == np.max(frame_line))) + 0.5
                    mean0 = frame_line_x[int(mean0_idx)]
                else:
                    mean0 = manual_mean
                    a0 = frame_line[mean0] - np.min(frame_line)

                sigma_left_idx = 0
                sigma_left = 0
                for i in range(int(mean0_idx)-4, 2, -1):
                    if frame_line[i - 2] > frame_line[i - 1] > frame_line[i]:  # and \
                        # frame_line[i + 2] > frame_line[i + 1] > frame_line[i]:
                        sigma_left = frame_line_x[i]
                        sigma_left_idx = i
                        break

                sigma_right_idx = len(frame_line_x)-1
                sigma_right = frame_line_x[-1]
                for i in range(int(mean0_idx)+4, len(frame_line_x)-2):
                    if frame_line[i + 2] > frame_line[i + 1] > frame_line[i]:  # and
                        # frame_line[i - 2] > frame_line[i - 1] > frame_line[i]:
                        sigma_right = frame_line_x[i] 
                        sigma_right_idx = i
                        break

                sigma0 = math.sqrt(np.sum(frame_line[sigma_left_idx:sigma_right_idx] / scale_factor *
                                          (frame_line_x[sigma_left_idx:sigma_right_idx] - mean0) ** 2) /
                                   (sigma_right-sigma_left))

                frame_line_x_s = frame_line_x[sigma_left_idx:sigma_right_idx]
                frame_line_s = frame_line[sigma_left_idx:sigma_right_idx]

                popt, pcov = curve_fit(gaussian, frame_line_x_s, frame_line_s,
                                       p0=[a0, mean0, sigma0, offset0],
                                       bounds=([a0 - 0.00001, mean0 - 0.2*np.max(frame_line_x), -np.inf, offset0 - 0.00001],
                                               [a0 + 0.00001, mean0 + 0.2*np.max(frame_line_x), +np.inf, offset0 + 0.00001]),
                                       maxfev=2000)
            else:
                if manual_mean is None:
                    mean0 = sum(frame_line * frame_line_x) / n
                else:
                    mean0 = manual_mean
                    a0 = frame_line[mean0] - np.min(frame_line)

                sigma0 = math.sqrt(np.sum(frame_line / scale_factor * (frame_line_x - mean0) ** 2) / len(frame_line))

                popt, pcov = curve_fit(gaussian, frame_line_x, frame_line,
                                       p0=[a0, mean0, sigma0, offset0],
                                       bounds=([a0 - 0.00001, mean0 - 0.2*np.max(frame_line_x), -np.inf, offset0 - 0.00001],
                                               [a0 + 0.00001, mean0 + 0.2*np.max(frame_line_x), +np.inf, offset0 + 0.00001]),
                                       maxfev=2000)

            a, mean, sigma, offset = popt

            mid_left = mean - np.sqrt(2*np.log(2)) * sigma
            mid_right = mean + np.sqrt(2*np.log(2)) * sigma

            return mid_left, mid_right, popt
        except (ValueError, RuntimeError, OptimizeWarning, RuntimeWarning, RuntimeError) as e:
            # print(e)
            return None, None, None


plt.rcParams.update({
    "text.usetex": True,
    "font.size": 12,
    "font.weight": "bold",
    "axes.labelweight": "bold",
    #"font.family": "sans-serif",
    #"font.sans-serif": ["Helvetica"]
})

img_data = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
img_height, img_width = img_data.shape[:2]

pixel_size=0.03333 #um

max_temp = np.max(img_data)
max_temp_locs = np.where(img_data == max_temp)
max_temp_center_y, max_temp_center_x = (int(np.average(max_temp_locs[0])+0.5), int(np.average(max_temp_locs[1])+0.5))

img_top = -max_temp_center_y * pixel_size
img_bottom = (img_height-1 - max_temp_center_y) * pixel_size

img_left = -max_temp_center_x * pixel_size
img_right = (img_width-1 - max_temp_center_x) * pixel_size

print(f"Image data loaded, center in {max_temp_center_x},{max_temp_center_y}")

fig_main = plt.figure("To Center")

fig_x_prof = plt.figure("X profile")
fig_y_prof = plt.figure("Y profile")

ax_main = fig_main.add_subplot(111)
ax_x_prof = fig_x_prof.add_subplot(111) 
ax_y_prof = fig_y_prof.add_subplot(111)

ax_main.imshow(img_data, cmap='hot', extent=[img_left, img_right, img_bottom, img_top])
# Change main figure x/y label, can use latex
ax_main.set_xlabel('x ($\mu m$)')
ax_main.set_ylabel('y ($\mu m$)')

x_prof_line = np.linspace(img_left, img_right, num=img_width)
x_prof_values = img_data[max_temp_center_y, :]
x_prof_values_unit = (x_prof_values - np.min(x_prof_values))/(np.max(x_prof_values) - np.min(x_prof_values))

x_mid_l, x_mid_r, x_popt = get_middle_distance(x_prof_line, x_prof_values_unit)
print(f"X profile fitting: a, mean, sigma, offset={x_popt}, x_mid_l={x_mid_l}, x_mid_r={x_mid_r}")
# recalculate
x_prof_rec = gaussian((x_mid_l, x_mid_r), *x_popt)
print(f"X profile gaussian recalculate: {x_prof_rec}")

y_prof_line = np.linspace(img_top, img_bottom, num=img_height)
y_prof_values = img_data[:, max_temp_center_x]
y_prof_values_unit = (y_prof_values - np.min(y_prof_values))/(np.max(y_prof_values) - np.min(y_prof_values))

y_mid_l, y_mid_r, y_popt = get_middle_distance(y_prof_line, y_prof_values_unit)
print(f"Y profile fitting: a, mean, sigma, offset={y_popt}, y_mid_l={y_mid_l}, y_mid_r={y_mid_r}")
# recalculate
y_prof_rec = gaussian((y_mid_l, y_mid_r), *y_popt)
print(f"Y profile gaussian recalculate: {y_prof_rec}")

# plot use uniformed values
ax_x_prof.plot(x_prof_line, x_prof_values_unit)

# Add fitted plot for x profile
x_fit_line = np.linspace(img_left, img_right, num=1000)
x_fit_values = gaussian(x_fit_line, *x_popt)

# Plot also the fitted line in dash
#ax_x_prof.plot(x_fit_line, x_fit_values, '--')

ax_x_prof.annotate("", xy=(x_mid_l, 0.5), xycoords='data', xytext=(x_mid_r, 0.5), textcoords='data', 
                  arrowprops=dict(arrowstyle="<->", color="red", shrinkA=0.05, shrinkB=0.05),)
ax_x_prof.text(x_mid_r*1.2, 0.5, f"$FWHM_{{x}}={x_mid_r-x_mid_l:.2f}\lambda_{{0}}$", color='red')

ax_x_prof.set_xlim(img_left, img_right)
ax_x_prof.set_ylim(0, 1)
ax_x_prof.set_xlabel('$x/\lambda_{0}$')



ax_y_prof.plot(y_prof_line, y_prof_values_unit)

# Add fitted plot for y profile
y_fit_line = np.linspace(img_bottom, img_top, num=1000)
y_fit_values = gaussian(y_fit_line, *y_popt)

# Plot also the fitted line in dash
#ax_y_prof.plot(y_fit_line, y_fit_values, '--')

ax_y_prof.annotate("", xy=(y_mid_l, 0.5), xycoords='data', xytext=(y_mid_r, 0.5), textcoords='data', 
                  arrowprops=dict(arrowstyle="<->", color="red", shrinkA=0.05, shrinkB=0.05),)
ax_y_prof.text(y_mid_r*1.2, 0.5, f"$FWHM_{{x,y}}={y_mid_r-y_mid_l:.2f}\lambda_{{0}}$", color='red')

ax_y_prof.set_xlim(img_top, img_bottom)
ax_y_prof.set_ylim(0, 1)
ax_y_prof.set_xlabel('$x,y/\lambda_{0}$')

plt.show()