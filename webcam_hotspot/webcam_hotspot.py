#!/usr/bin/env python3

import argparse

import cv2
import numpy as np
import matplotlib.pyplot as plt
import math as math
from scipy.optimize import curve_fit, OptimizeWarning
import warnings
from matplotlib.widgets import Slider, Button, CheckButtons
from matplotlib.gridspec import GridSpec
import time
import pickle
from pprint import pprint
from pixelink import PixeLINK
from matplotlib.ticker import FormatStrFormatter

import matplotlib.style as mplstyle
# matplotlib.use('Qt5Agg')
mplstyle.use('fast')

# plt.rc('text', usetex=True)

b_quit = False

warnings.simplefilter("error", OptimizeWarning)

crosshair_x = 0
crosshair_y = 0

CAM_PROP_DICT = {
    'brightness': cv2.CAP_PROP_BRIGHTNESS,
    'contrast': cv2.CAP_PROP_CONTRAST,
    'gain': cv2.CAP_PROP_GAIN,              # is dynamic
    'gamma': cv2.CAP_PROP_GAMMA,
    'exposure': cv2.CAP_PROP_EXPOSURE
}


def get_cam_property(cam_cap, prop_name: str):
    global CAM_PROP_DICT
    return cam_cap.get(CAM_PROP_DICT[prop_name])


def set_cam_property(cam_cap, prop_name: str, value):
    global CAM_PROP_DICT
    print(f'Setting {prop_name} {value}')
    cam_cap.set(CAM_PROP_DICT[prop_name], value)


def gaussian_saturated(x, a, x0, sigma, offset):
    return np.clip(a * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2)) + offset, 0, 1)


def gaussian(x, a, x0, sigma, offset):
    return a * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2)) + offset


def poly4_saturated(x, x0, offset, a, b, c, d, e, f):
    x_ = x - x0
    return np.clip(a + b*x_ + c*x_**2 + d*x_**3 + e*x_**4 + f*x_**5 + offset, 0, 1)


def poly4(x, x0, offset, a, b, c, d, e, f):
    x_ = x - x0
    return a + b*x_ + c*x_**2 + d*x_**3 + e*x_**4 + f*x_**5 + offset


def poly_fit(line_x, line_y):
    offset0 = np.min(line_y)
    x0 = np.average(np.where(line_y == np.max(line_y)))

    try:
        popt, pcov = curve_fit(poly4_saturated, line_x, line_y,
                               p0=[x0, offset0, 0, 0, 0, 0, 0, 0],
                               maxfev=2000)
        line_fit_y = poly4(line_x, *popt)

        x0, offset, a, b, c, d, e, f = popt

        fit_formula = f"${a:.2f} + " \
            f"{b:.2f}*(x-{x0:.2f}) + " \
            f"{c:.2f}*(x-{x0:.2f})^2 + " \
            f"{d:.2f}*(x-{x0:.2f})^3 + " \
            f"{e:.2f}*(x-{x0:.2f})^4 + " \
            f"{f:.2f}*(x-{x0:.2f})^5 + " \
            f"{offset:.2f}$"

        return line_fit_y, fit_formula
    except (ValueError, RuntimeError, OptimizeWarning) as e:
        return None, None


def multi_gaussian_saturated(x, a_0, x0_0, sigma_0,
                   a_1, x0_1, sigma_1,
                   a_2, x0_2, sigma_2,
                   offset):
    return np.clip(a_0 * np.exp(-(x - x0_0) ** 2 / (2 * sigma_0 ** 2)) +
                   a_1 * np.exp(-(x - x0_1) ** 2 / (2 * sigma_1 ** 2)) +
                   a_2 * np.exp(-(x - x0_2) ** 2 / (2 * sigma_2 ** 2)) +
                   offset, 0, 1)


def multi_gaussian(x, a_0, x0_0, sigma_0,
                   a_1, x0_1, sigma_1,
                   a_2, x0_2, sigma_2,
                   offset):
    return a_0 * np.exp(-(x - x0_0) ** 2 / (2 * sigma_0 ** 2)) + \
           a_1 * np.exp(-(x - x0_1) ** 2 / (2 * sigma_1 ** 2)) + \
           a_2 * np.exp(-(x - x0_2) ** 2 / (2 * sigma_2 ** 2)) + \
           offset


def multi_gaussian_fit(line_x, line_y):
    a0 = np.max(line_y) - np.min(line_y)
    offset0 = np.min(line_y)
    n = sum(line_y)
    mean0 = sum(line_y * line_x) / n
    sigma0 = math.sqrt(np.sum(line_y * (line_x - mean0) ** 2) / n)

    try:
        popt, pcov = curve_fit(multi_gaussian_saturated, line_x, line_y,
                               p0=[a0, mean0, sigma0,
                                   0, mean0-10, 0.1,
                                   0, mean0+10, 0.1,
                                   offset0],
                               maxfev=2000)
        line_fit_y = multi_gaussian(line_x, *popt)

        # FIXME:
        fit_formula = "N/A"

        return line_fit_y, fit_formula
    except (ValueError, RuntimeError, OptimizeWarning) as e:
        return None, None


def lorentzian_saturated(x,
                         amp1, cen1, wid1,
                         amp2, cen2, wid2,
                         amp3, cen3, wid3,
                         offset):
    return np.clip((amp1*wid1**2/((x-cen1)**2+wid1**2)) +
                   (amp2*wid2**2/((x-cen2)**2+wid2**2)) +
                   (amp3*wid3**2/((x-cen3)**2+wid3**2)) + offset, 0, 1)


def lorentzian(x,
                 amp1, cen1, wid1,
                 amp2, cen2, wid2,
                 amp3, cen3, wid3,
                 offset):
    return (amp1*wid1**2/((x-cen1)**2+wid1**2)) + \
                   (amp2*wid2**2/((x-cen2)**2+wid2**2)) + \
                   (amp3*wid3**2/((x-cen3)**2+wid3**2)) + offset


def lorentzian_fit(line_x, line_y):
    try:
        popt, pcov = curve_fit(lorentzian_saturated, line_x, line_y,
                               maxfev=20000)
        line_fit_y = lorentzian(line_x, *popt)

        fit_formula = "N/A"
        return line_fit_y, fit_formula
    except (ValueError, RuntimeError, OptimizeWarning) as e:
        return None, None


def get_middle_distance(frame_line_x, frame_line, forced=False, manual_mean=None):
    a0 = np.max(frame_line) - np.min(frame_line)
    offset0 = np.min(frame_line)
    n = sum(frame_line)

    try:

        if forced:
            if manual_mean is None:
                mean0 = np.average(np.where(frame_line == np.max(frame_line))) + 0.5
            else:
                mean0 = manual_mean
                a0 = frame_line[mean0] - np.min(frame_line)

            sigma_left = 0
            for i in range(int(mean0)-4, 2, -1):
                if frame_line[i - 2] > frame_line[i - 1] > frame_line[i] : #and \
                    # frame_line[i + 2] > frame_line[i + 1] > frame_line[i]:
                    sigma_left = i
                    break

            sigma_right = len(frame_line)
            for i in range(int(mean0)+4, len(frame_line)-2):
                if frame_line[i + 2] > frame_line[i + 1] > frame_line[i]: # and
                    # frame_line[i - 2] > frame_line[i - 1] > frame_line[i]:
                    sigma_right = i
                    break

            sigma0 = math.sqrt(np.sum(frame_line[sigma_left:sigma_right] / a0 *
                                      (frame_line_x[sigma_left:sigma_right] - mean0) ** 2) /
                               (sigma_right-sigma_left))

            frame_line_x_s = frame_line_x[sigma_left:sigma_right]
            frame_line_s = frame_line[sigma_left:sigma_right]

            popt, pcov = curve_fit(gaussian_saturated, frame_line_x_s, frame_line_s,
                                   p0=[a0, mean0, sigma0, offset0],
                                   bounds=([a0 - 0.00001, mean0 - 0.5, -np.inf, offset0 - 0.00001],
                                           [a0 + 0.00001, mean0 + 0.5, +np.inf, offset0 + 0.00001]),
                                   maxfev=2000)
        else:
            mean0 = sum(frame_line * frame_line_x) / n
            sigma0 = math.sqrt(np.sum(frame_line / a0 * (frame_line_x - mean0) ** 2) / n)

            popt, pcov = curve_fit(gaussian_saturated, frame_line_x, frame_line,
                                   p0=[a0, mean0, sigma0, offset0],
                                   maxfev=2000)

        a, mean, sigma, offset = popt

        fit_value = gaussian(frame_line_x, *popt)
        mid_left = mean - 2.355 * sigma / 2
        mid_right = mean + 2.355 * sigma / 2

        return mid_left, mid_right, a, offset, mean, fit_value
    except (ValueError, RuntimeError, OptimizeWarning) as e:
        print(e)
        return None, None, None, None, None, None


def update_frame_figure_profiles(fig_frame_data: dict, fig_cross_data: dict,
                                 x: int, y: int,
                                 curve_type: str = 'gaussian'):
    frame = fig_frame_data['hm'].get_array()
    frame_width = frame.shape[1]
    frame_height = frame.shape[0]

    h_profile_x = np.array([i for i in range(0, frame_width)])
    h_profile_y = frame[y, :]

    v_profile_y = np.array([i for i in range(0, frame_height)])
    v_profile_x = frame[:, x]

    # Update frame h/v lines
    fig_cross_data['frame_hline'].set_ydata(y)
    fig_cross_data['frame_vline'].set_xdata(x)
    fig_cross_data['h_profile_vline'].set_xdata(x)
    fig_cross_data['v_profile_hline'].set_ydata(y)
    # Update profile lines
    fig_cross_data['h_profile_line'].set_ydata(h_profile_y)
    fig_cross_data['v_profile_line'].set_xdata(v_profile_x)

    if curve_type in ('gaussian', 'gaussian_forced', 'gaussian_manual'):
        # H Profile fit
        if curve_type == 'gaussian':
            mid_left, mid_right, a, offset, mean, fit_value = get_middle_distance(h_profile_x, h_profile_y,
                                                                                  forced=False)
        elif curve_type == 'gaussian_forced':
            mid_left, mid_right, a, offset, mean, fit_value = get_middle_distance(h_profile_x, h_profile_y,
                                                                                  forced=True)
        else:  # gaussian_manual
            mid_left, mid_right, a, offset, mean, fit_value = get_middle_distance(h_profile_x, h_profile_y,
                                                                                  forced=True, manual_mean=x)

        if mid_left is not None:
            # Fit okay
            # Update the patch lines
            fig_cross_data['frame_patch_vline_0'].set_xdata(mid_left)
            fig_cross_data['frame_patch_vline_1'].set_xdata(mid_right)

            # Update the h Profile fig lines
            fig_cross_data['h_profile_fit_line'].set_xdata(h_profile_x)
            fig_cross_data['h_profile_fit_line'].set_ydata(fit_value)
            # Update the h Profile mid line and v lines
            fig_cross_data['h_profile_mid_hline'].set_ydata(a / 2 + offset)
            fig_cross_data['h_profile_patch_vline_0'].set_xdata(mid_left)
            fig_cross_data['h_profile_patch_vline_1'].set_xdata(mid_right)
            # fit_min_value = np.min((0, np.min(fit_value)))
            # fig_frame_data['ax_h_profile'].set_ylim(fit_min_value, np.max(fit_value) + 10)

            fig_cross_data['h_profile_mid_note'].set_text(f'M:{a / 2 + offset:.2f}')
            fig_cross_data['h_profile_mid_note'].set_y(a / 2 + offset)

            fig_cross_data['h_profile_offset_note'].set_text(f'O:{offset:.2f}')
            fig_cross_data['h_profile_offset_note'].set_y(offset)

            fig_cross_data['h_profile_peak_note'].set_text(f'P:{mean:.2f} {a + offset:.2f}')
            fig_cross_data['h_profile_peak_note'].set_position((mean, a + offset))

            fig_cross_data['h_profile_dist_note'].set_text(f'L:{mid_left:.2f} R:{mid_right:.2f}\n'
                                                           f'D:{mid_right - mid_left:.2f}')
            fig_cross_data['h_profile_dist_note'].set_position((mean, a/2+offset))
            # fig_cross_data['h_profile_dist_note'].set_x(mean)

        # V Profile fit
        if curve_type == "gaussian":
            mid_top, mid_bottom, a, offset, mean, fit_value = get_middle_distance(v_profile_y, v_profile_x,
                                                                                  forced=False)
        elif curve_type == 'gaussian_forced':
            mid_top, mid_bottom, a, offset, mean, fit_value = get_middle_distance(v_profile_y, v_profile_x,
                                                                                  forced=True)
        else:
            mid_top, mid_bottom, a, offset, mean, fit_value = get_middle_distance(v_profile_y, v_profile_x,
                                                                                  forced=True, manual_mean=y)
        if mid_top is not None:
            # Update the patch lines
            fig_cross_data['frame_patch_hline_0'].set_ydata(mid_top)
            fig_cross_data['frame_patch_hline_1'].set_ydata(mid_bottom)

            # Update the V profile fig lines
            fig_cross_data['v_profile_fit_line'].set_xdata(fit_value)
            fig_cross_data['v_profile_fit_line'].set_ydata(v_profile_y)
            # Update the v Profile mide line and h lines
            fig_cross_data['v_profile_mid_vline'].set_xdata(a / 2 + offset)
            fig_cross_data['v_profile_patch_hline_0'].set_ydata(mid_top)
            fig_cross_data['v_profile_patch_hline_1'].set_ydata(mid_bottom)
            # fit_min_value = np.min((0, np.min(fit_value)))
            # fig_frame_data['ax_v_profile'].set_xlim(fit_min_value, np.max(fit_value) + 10)

            fig_cross_data['v_profile_mid_note'].set_text(f'M:{a / 2 + offset:.2f}')
            fig_cross_data['v_profile_mid_note'].set_x(a / 2 + offset)

            fig_cross_data['v_profile_offset_note'].set_text(f'O:{offset:.2f}')
            fig_cross_data['v_profile_offset_note'].set_x(offset)

            fig_cross_data['v_profile_peak_note'].set_text(f'P:{a + offset:.2f} {mean:.2f}')
            fig_cross_data['v_profile_peak_note'].set_position((a + offset, mean))
            fig_cross_data['v_profile_dist_note'].set_text(f'T:{mid_top:.2f} B:{mid_bottom:.2f}\n'
                                                           f'D:{mid_bottom - mid_top:.2f}')
            fig_cross_data['v_profile_dist_note'].set_position((a/2+offset, mean))
            # fig_cross_data['v_profile_dist_note'].set_y(mean)
    elif curve_type in ('poly', 'multi_gaussian', 'lorentzian'):
        # TODO
        # H Profile fit
        if curve_type == "poly":
            h_profile_fit_y, fit_formula = poly_fit(h_profile_x, h_profile_y)
        elif curve_type == "multi_gaussian":
            h_profile_fit_y, fit_formula = multi_gaussian_fit(h_profile_x, h_profile_y)
        elif curve_type == "lorentzian":
            h_profile_fit_y, fit_formula = lorentzian_fit(h_profile_x, h_profile_y)
        else:
            raise ValueError(f"Unsupported curve type {curve_type}")

        if h_profile_fit_y is not None:
            fig_cross_data['h_profile_fit_line'].set_xdata(h_profile_x)
            fig_cross_data['h_profile_fit_line'].set_ydata(h_profile_fit_y)
            fig_cross_data['h_profile_poly_note'].set_text(fit_formula)
            fig_cross_data['h_profile_poly_note'].set_y(np.max(h_profile_fit_y))
        else:
            fig_cross_data['h_profile_poly_note'].set_text(f"N/A")

        # V Profile fit
        if curve_type == "poly":
            v_profile_fit_x, fit_formula = poly_fit(v_profile_y, v_profile_x)
        elif curve_type == "multi_gaussian":
            v_profile_fit_x, fit_formula = multi_gaussian_fit(v_profile_y, v_profile_x)
        elif curve_type == "lorentzian":
            v_profile_fit_x, fit_formula = lorentzian_fit(v_profile_y, v_profile_x)
        else:
            raise ValueError(f"Unsupported curve type {curve_type}")

        if v_profile_fit_x is not None:
            fig_cross_data['v_profile_fit_line'].set_xdata(v_profile_fit_x)
            fig_cross_data['v_profile_fit_line'].set_ydata(v_profile_y)
            fig_cross_data['v_profile_poly_note'].set_text(fit_formula)
            fig_cross_data['v_profile_poly_note'].set_x(np.max(v_profile_fit_x))
        else:
            fig_cross_data['v_profile_poly_note'].set_text(f"N/A")        
    else:
        raise ValueError(f'Unsupported curve type {curve_type}')

    fig_frame_data['ax_h_profile'].relim(visible_only=True)
    fig_frame_data['ax_h_profile'].autoscale_view(scaley=True, scalex=False)
    fig_frame_data['ax_v_profile'].relim(visible_only=True)
    fig_frame_data['ax_v_profile'].autoscale_view(scalex=True, scaley=False)


def onclick_cross_hair(event, fig_frame_data, curve_type):
    if event.inaxes == fig_frame_data['ax_frame']:
        update_frame_figure_profiles(fig_frame_data, fig_frame_data['crosshair_data'],
                                     int(event.xdata), int(event.ydata), curve_type=curve_type)


def dump_frame_lines(event, fig_data):
    ch_x = fig_data['crosshair_data']['frame_vline'].get_xdata()
    ch_y = fig_data['crosshair_data']['frame_hline'].get_ydata()
    ch_x = ch_x[0] if type(ch_x) is list else ch_x
    ch_y = ch_y[0] if type(ch_y) is list else ch_y

    ch_h_profile_xdata = fig_data['crosshair_data']['h_profile_line'].get_xdata()
    ch_h_profile_ydata = fig_data['crosshair_data']['h_profile_line'].get_ydata()
    ch_v_profile_xdata = fig_data['crosshair_data']['v_profile_line'].get_xdata()
    ch_v_profile_ydata = fig_data['crosshair_data']['v_profile_line'].get_ydata()

    ac_x = fig_data['autocenter_data']['frame_vline'].get_xdata()
    ac_y = fig_data['autocenter_data']['frame_hline'].get_ydata()
    ac_x = ac_x[0] if type(ac_x) is list else ac_x
    ac_y = ac_y[0] if type(ac_y) is list else ac_y

    ac_h_profile_xdata = fig_data['autocenter_data']['h_profile_line'].get_xdata()
    ac_h_profile_ydata = fig_data['autocenter_data']['h_profile_line'].get_ydata()
    ac_v_profile_xdata = fig_data['autocenter_data']['v_profile_line'].get_xdata()
    ac_v_profile_ydata = fig_data['autocenter_data']['v_profile_line'].get_ydata()

    data_dict = {
        'ch_x': ch_x,
        'ch_y': ch_y,
        'ch_h_profile_xdata': ch_h_profile_xdata,
        'ch_h_profile_ydata': ch_h_profile_ydata,
        'ch_v_profile_xdata': ch_v_profile_xdata,
        'ch_v_profile_ydata': ch_v_profile_ydata,
        'ac_x': ac_x,
        'ac_y': ac_y,
        'ac_h_profile_xdata': ac_h_profile_xdata,
        'ac_h_profile_ydata': ac_h_profile_ydata,
        'ac_v_profile_xdata': ac_v_profile_xdata,
        'ac_v_profile_ydata': ac_v_profile_ydata,
    }

    with open("profile.pickle", "wb") as f_d:
        pickle.dump(data_dict, file=f_d)

    with open("profile.dat", "w") as f_d:
        pprint(data_dict, stream=f_d)


def setup_frame_figure(fig_name: str,
                       frame_width: int, frame_height: int,
                       curve_type: str = 'gaussian'):
    fig_height = 7.2
    fig_n_cols = 5
    fig_n_rows = 3
    fig_col_space_ratio = 0.04
    fig_row_space_ratio = 0.04
    fig_col_width_ratio = [0.2, fig_col_space_ratio, 1, fig_col_space_ratio, 0.05]
    fig_row_height_ratio = [1, fig_row_space_ratio, 0.2]
    fig_wspace = 0.
    fig_hspace = 0.
    top_margin = 0.05
    bottom_margin = 0.05
    left_margin = 0.05
    right_margin = 0.05

    fig_width = fig_height / np.sum(fig_row_height_ratio) / frame_height * \
                 frame_width * np.sum(fig_col_width_ratio)

    fig = plt.figure(fig_name, figsize=(fig_width, fig_height))
    fig_gs = GridSpec(fig_n_rows, fig_n_cols, figure=fig,
                      wspace=fig_wspace,
                      hspace=fig_hspace,
                      width_ratios=fig_col_width_ratio,
                      height_ratios=fig_row_height_ratio,
                      top=(1-top_margin),
                      bottom=bottom_margin,
                      left=left_margin,
                      right=(1-right_margin))

    ax_cbar = fig.add_subplot(fig_gs[0, 4])

    ax_frame = fig.add_subplot(fig_gs[0, 2], aspect='equal',)
    ax_v_profile = fig.add_subplot(fig_gs[0, 0], sharey=ax_frame)
    ax_h_profile = fig.add_subplot(fig_gs[2, 2], sharex=ax_frame)

    ax_frame.set_axis_off()
    ax_frame.set_xlim(0, frame_width)
    ax_frame.set_ylim(0, frame_height)

    ax_frame.invert_yaxis()

    ax_save_button = fig.add_subplot(fig_gs[2, 0])
    btn_save = Button(ax_save_button, 'Save')

    dummy_data = np.zeros((frame_height, frame_width))
    hm = ax_frame.imshow(dummy_data, cmap=plt.cm.rainbow)
    hm.autoscale()

    dummy_data_h_x = np.array([i for i in range(0, frame_width)], dtype='int')
    dummy_data_h_y = np.zeros(frame_width)

    dummy_data_v_x = np.zeros(frame_height)
    dummy_data_v_y = np.array([i for i in range(0, frame_height)], dtype='int')

    fig.colorbar(hm, cax=ax_cbar)

    # ax_frame.grid(True, which='both')
    # ax_v_profile.set_ylabel(f'V Dist: n/a')
    # ax_h_profile.set_xlabel(f'H Dist: n/a')

    if curve_type in ('gaussian', 'gaussian_forced', 'gaussian_manual'):
        # set up cross hair lines in ax_frame
        frame_ch_hline = ax_frame.axhline(0, linestyle='-', color='green')
        frame_ch_vline = ax_frame.axvline(0, linestyle='-', color='green')

        # extend the cross hair line in ax_v_profile and ax_h_profile
        v_profile_ch_hline = ax_v_profile.axhline(0, linestyle='-', color='green')
        h_profile_ch_vline = ax_h_profile.axvline(0, linestyle='-', color='green')

        # set up patch lines in the ax_frame
        frame_ch_patch_hline_0 = ax_frame.axhline(0, linestyle='-.', color='green')
        frame_ch_patch_hline_1 = ax_frame.axhline(0, linestyle='-.', color='green')

        frame_ch_patch_vline_0 = ax_frame.axvline(0, linestyle='-.', color='green')
        frame_ch_patch_vline_1 = ax_frame.axvline(0, linestyle='-.', color='green')

        # extend the patch lines to ax_v_profile and ax_h_profile, should be middle value line
        v_profile_ch_patch_hline_0 = ax_v_profile.axhline(0, linestyle='-.', color='blue')
        v_profile_ch_patch_hline_1 = ax_v_profile.axhline(0, linestyle='-.', color='blue')

        h_profile_ch_patch_vline_0 = ax_h_profile.axvline(0, linestyle='-.', color='blue')
        h_profile_ch_patch_vline_1 = ax_h_profile.axvline(0, linestyle='-.', color='blue')

        h_profile_ch_line, = ax_h_profile.plot(dummy_data_h_x, dummy_data_h_y, 'g-')
        v_profile_ch_line, = ax_v_profile.plot(dummy_data_v_x, dummy_data_v_y, 'g-')

        h_profile_ch_fit_line, = ax_h_profile.plot(dummy_data_h_x, dummy_data_h_y, 'b--')
        v_profile_ch_fit_line, = ax_v_profile.plot(dummy_data_v_x, dummy_data_v_y, 'b--')

        h_profile_ch_mid_hline = ax_h_profile.axhline(0, linestyle='--', color='blue')
        v_profile_ch_mid_vline = ax_v_profile.axvline(0, linestyle='--', color='blue')

        h_profile_ch_mid_note = ax_h_profile.text(frame_width, 0, f'M: n/a',
                                                  color='blue', horizontalalignment='left')
        h_profile_ch_offset_note = ax_h_profile.text(frame_width, 0, f'O: n/a',
                                                     color='blue', horizontalalignment='left')
        h_profile_ch_peak_note = ax_h_profile.text(frame_width / 2, 0, f'P: n/a',
                                                   color='blue', horizontalalignment='left')
        h_profile_ch_dist_note = ax_h_profile.text(frame_width / 2, 0, f'L:n/a R:n/a\nD:n/a',
                                                   color='blue', horizontalalignment='left',
                                                   verticalalignment='bottom')

        v_profile_ch_mid_note = ax_v_profile.text(0, frame_height, f'M: n/a', rotation=-90,
                                                  color='blue', verticalalignment='top')
        v_profile_ch_offset_note = ax_v_profile.text(0, frame_height, f'O: n/a', rotation=-90,
                                                     color='blue', verticalalignment='top')
        v_profile_ch_peak_note = ax_v_profile.text(0, 1, f'P: n/a', rotation=-90,
                                                   color='blue', verticalalignment='top')
        v_profile_ch_dist_note = ax_v_profile.text(0, frame_height / 2, f'L:n/a R:n/a\nD:n/a', color='blue',
                                                   rotation=-90, verticalalignment='top',
                                                   horizontalalignment='left')

        frame_crosshair_data = {
            "frame_hline": frame_ch_hline,
            "frame_vline": frame_ch_vline,
            "v_profile_hline": v_profile_ch_hline,
            "h_profile_vline": h_profile_ch_vline,
            "frame_patch_hline_0": frame_ch_patch_hline_0,
            "frame_patch_hline_1": frame_ch_patch_hline_1,
            "frame_patch_vline_0": frame_ch_patch_vline_0,
            "frame_patch_vline_1": frame_ch_patch_vline_1,
            "v_profile_patch_hline_0": v_profile_ch_patch_hline_0,
            "v_profile_patch_hline_1": v_profile_ch_patch_hline_1,
            "h_profile_patch_vline_0": h_profile_ch_patch_vline_0,
            "h_profile_patch_vline_1": h_profile_ch_patch_vline_1,
            "h_profile_line": h_profile_ch_line,
            "v_profile_line": v_profile_ch_line,
            "h_profile_fit_line": h_profile_ch_fit_line,
            "v_profile_fit_line": v_profile_ch_fit_line,
            "h_profile_mid_hline": h_profile_ch_mid_hline,
            "v_profile_mid_vline": v_profile_ch_mid_vline,
            "h_profile_mid_note": h_profile_ch_mid_note,
            "h_profile_offset_note": h_profile_ch_offset_note,
            "h_profile_peak_note": h_profile_ch_peak_note,
            "h_profile_dist_note": h_profile_ch_dist_note,
            "v_profile_mid_note": v_profile_ch_mid_note,
            "v_profile_offset_note": v_profile_ch_offset_note,
            "v_profile_peak_note": v_profile_ch_peak_note,
            "v_profile_dist_note": v_profile_ch_dist_note
        }
    elif curve_type in ('poly', 'multi_gaussian', 'lorentzian'):
        # set up cross hair lines in ax_frame
        frame_ch_hline = ax_frame.axhline(0, linestyle='-', color='green')
        frame_ch_vline = ax_frame.axvline(0, linestyle='-', color='green')

        # extend the cross hair line in ax_v_profile and ax_h_profile
        v_profile_ch_hline = ax_v_profile.axhline(0, linestyle='-', color='green')
        h_profile_ch_vline = ax_h_profile.axvline(0, linestyle='-', color='green')

        h_profile_ch_line, = ax_h_profile.plot(dummy_data_h_x, dummy_data_h_y, 'g-')
        v_profile_ch_line, = ax_v_profile.plot(dummy_data_v_x, dummy_data_v_y, 'g-')

        h_profile_ch_fit_line, = ax_h_profile.plot(dummy_data_h_x, dummy_data_h_y, 'b--')
        v_profile_ch_fit_line, = ax_v_profile.plot(dummy_data_v_x, dummy_data_v_y, 'b--')

        h_profile_ch_poly_note = ax_h_profile.text(0, 0, f'n/a', color='b',
                                                   horizontalalignment='left',
                                                   verticalalignment='bottom')
        v_profile_ch_poly_note = ax_v_profile.text(0, 0, f'n/a', color='b', rotation=-90,
                                                   horizontalalignment='left',
                                                   verticalalignment='top')

        frame_crosshair_data = {
            "frame_hline": frame_ch_hline,
            "frame_vline": frame_ch_vline,
            "v_profile_hline": v_profile_ch_hline,
            "h_profile_vline": h_profile_ch_vline,
            "h_profile_line": h_profile_ch_line,
            "v_profile_line": v_profile_ch_line,
            "h_profile_fit_line": h_profile_ch_fit_line,
            "v_profile_fit_line": v_profile_ch_fit_line,
            "h_profile_poly_note": h_profile_ch_poly_note,
            "v_profile_poly_note": v_profile_ch_poly_note
        }
    else:
        raise ValueError(f'Unsupported curve type {curve_type}')

    if curve_type in ('gaussian', 'gaussian_forced', 'gaussian_manual'):
        # setup auto center lines
        frame_ac_hline = ax_frame.axhline(0, linestyle='-', color='black')
        frame_ac_vline = ax_frame.axvline(0, linestyle='-', color='black')

        v_profile_ac_hline = ax_v_profile.axhline(0, linestyle='--', color='black')
        h_profile_ac_vline = ax_h_profile.axvline(0, linestyle='--', color='black')

        # set up patch lines in the ax_frame
        frame_ac_patch_hline_0 = ax_frame.axhline(0, linestyle='-.', color='black')
        frame_ac_patch_hline_1 = ax_frame.axhline(0, linestyle='-.', color='black')

        frame_ac_patch_vline_0 = ax_frame.axvline(0, linestyle='-.', color='black')
        frame_ac_patch_vline_1 = ax_frame.axvline(0, linestyle='-.', color='black')

        # extend the patch lines to ax_v_profile and ax_h_profile, should be middle value line
        v_profile_ac_patch_hline_0 = ax_v_profile.axhline(0, linestyle='-.', color='red')
        v_profile_ac_patch_hline_1 = ax_v_profile.axhline(0, linestyle='-.', color='red')

        h_profile_ac_patch_vline_0 = ax_h_profile.axvline(0, linestyle='-.', color='red')
        h_profile_ac_patch_vline_1 = ax_h_profile.axvline(0, linestyle='-.', color='red')

        # setup ax_v_profile
        h_profile_ac_line, = ax_h_profile.plot(dummy_data_h_x, dummy_data_h_y, 'k-')
        v_profile_ac_line, = ax_v_profile.plot(dummy_data_v_x, dummy_data_v_y, 'k-')

        h_profile_ac_fit_line, = ax_h_profile.plot(dummy_data_h_x, dummy_data_h_y, 'r--')
        v_profile_ac_fit_line, = ax_v_profile.plot(dummy_data_v_x, dummy_data_v_y, 'r--')

        h_profile_ac_mid_hline = ax_h_profile.axhline(0, linestyle='--', color='red')
        v_profile_ac_mid_vline = ax_v_profile.axvline(0, linestyle='--', color='red')

        h_profile_ac_mid_note = ax_h_profile.text(0, 0, f'M: n/a',
                                                  color='red', horizontalalignment='right')
        h_profile_ac_offset_note = ax_h_profile.text(0, 0, f'O: n/a',
                                                     color='red', horizontalalignment='right')
        h_profile_ac_peak_note = ax_h_profile.text(frame_width / 2, 0, f'P: n/a',
                                                   color='red', horizontalalignment='right')
        h_profile_ac_dist_note = ax_h_profile.text(frame_width / 2, 0, f'L:n/a R:n/a\nD:n/a',
                                                   color='red', horizontalalignment='right',
                                                   verticalalignment='bottom')

        v_profile_ac_mid_note = ax_v_profile.text(0, 0, f'M: n/a', rotation=-90,
                                                  color='red', verticalalignment='top')
        v_profile_ac_offset_note = ax_v_profile.text(0, 0, f'O: n/a', rotation=-90,
                                                     color='red', verticalalignment='top')
        v_profile_ac_peak_note = ax_v_profile.text(0, 1, f'P: n/a', rotation=-90,
                                                   color='red', verticalalignment='top')
        v_profile_ac_dist_note = ax_v_profile.text(0, frame_height / 2, f'L:n/a R:n/a\nD:n/a', color='red',
                                                   rotation=-90, verticalalignment='top',
                                                   horizontalalignment='left')

        frame_autocenter_data = {
            "frame_hline": frame_ac_hline,
            "frame_vline": frame_ac_vline,
            "v_profile_hline": v_profile_ac_hline,
            "h_profile_vline": h_profile_ac_vline,
            "frame_patch_hline_0": frame_ac_patch_hline_0,
            "frame_patch_hline_1": frame_ac_patch_hline_1,
            "frame_patch_vline_0": frame_ac_patch_vline_0,
            "frame_patch_vline_1": frame_ac_patch_vline_1,
            "v_profile_patch_hline_0": v_profile_ac_patch_hline_0,
            "v_profile_patch_hline_1": v_profile_ac_patch_hline_1,
            "h_profile_patch_vline_0": h_profile_ac_patch_vline_0,
            "h_profile_patch_vline_1": h_profile_ac_patch_vline_1,
            "h_profile_line": h_profile_ac_line,
            "v_profile_line": v_profile_ac_line,
            "h_profile_fit_line": h_profile_ac_fit_line,
            "v_profile_fit_line": v_profile_ac_fit_line,
            "h_profile_mid_hline": h_profile_ac_mid_hline,
            "v_profile_mid_vline": v_profile_ac_mid_vline,
            "h_profile_mid_note": h_profile_ac_mid_note,
            "h_profile_offset_note": h_profile_ac_offset_note,
            "h_profile_peak_note": h_profile_ac_peak_note,
            "h_profile_dist_note": h_profile_ac_dist_note,
            "v_profile_mid_note": v_profile_ac_mid_note,
            "v_profile_offset_note": v_profile_ac_offset_note,
            "v_profile_peak_note": v_profile_ac_peak_note,
            "v_profile_dist_note": v_profile_ac_dist_note,
        }
    elif curve_type in ('poly', 'multi_gaussian', 'lorentzian'):
        # setup auto center lines
        frame_ac_hline = ax_frame.axhline(0, linestyle='-', color='black')
        frame_ac_vline = ax_frame.axvline(0, linestyle='-', color='black')

        v_profile_ac_hline = ax_v_profile.axhline(0, linestyle='--', color='black')
        h_profile_ac_vline = ax_h_profile.axvline(0, linestyle='--', color='black')

        # setup ax_v_profile
        h_profile_ac_line, = ax_h_profile.plot(dummy_data_h_x, dummy_data_h_y, 'k-')
        v_profile_ac_line, = ax_v_profile.plot(dummy_data_v_x, dummy_data_v_y, 'k-')

        h_profile_ac_fit_line, = ax_h_profile.plot(dummy_data_h_x, dummy_data_h_y, 'r--')
        v_profile_ac_fit_line, = ax_v_profile.plot(dummy_data_v_x, dummy_data_v_y, 'r--')

        h_profile_ac_poly_note = ax_h_profile.text(frame_width, 0, f'n/a', color='r',
                                                   horizontalalignment='right',
                                                   verticalalignment='bottom')
        v_profile_ac_poly_note = ax_v_profile.text(0, frame_height, f'n/a', color='r', rotation=-90,
                                                   horizontalalignment='right',
                                                   verticalalignment='bottom')

        frame_autocenter_data = {
            "frame_hline": frame_ac_hline,
            "frame_vline": frame_ac_vline,
            "v_profile_hline": v_profile_ac_hline,
            "h_profile_vline": h_profile_ac_vline,
            "h_profile_line": h_profile_ac_line,
            "v_profile_line": v_profile_ac_line,
            "h_profile_fit_line": h_profile_ac_fit_line,
            "v_profile_fit_line": v_profile_ac_fit_line,
            "h_profile_poly_note": h_profile_ac_poly_note,
            "v_profile_poly_note": v_profile_ac_poly_note
        }
    else:
        raise ValueError(f'Unsupported curve type {curve_type}')

    fig_frame_data = {
        "fig": fig,
        "ax_cbar": ax_cbar,
        "ax_frame": ax_frame,
        "ax_v_profile": ax_v_profile,
        "ax_h_profile": ax_h_profile,
        "hm": hm,
        "crosshair_data": frame_crosshair_data,
        "autocenter_data": frame_autocenter_data,
        'btn_save': btn_save
    }

    # ax_h_profile.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    # ax_v_profile.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    fig.canvas.mpl_connect('button_press_event', lambda x: onclick_cross_hair(x, fig_frame_data, curve_type))
    btn_save.on_clicked(lambda event: dump_frame_lines(event, fig_frame_data))

    return fig_frame_data


def update_frame_figure(fig_frame_data: dict,
                        frame: np.ndarray,
                        cross_hair_man: tuple = None,
                        autocenter_enabled: bool = True,
                        crosshair_enabled: bool = True,
                        curve_type: str = 'gaussian'
                        ):
    frame_width = frame.shape[1]
    frame_height = frame.shape[0]

    fig = fig_frame_data['fig']

    # Update the frame
    fig_frame_data['hm'].set_data(frame)
    fig_frame_data['hm'].autoscale()

    if autocenter_enabled:
        # Auto center
        # Find hot center
        max_temp = np.max(frame)
        max_temp_locs = np.where(frame == max_temp)
        max_temp_center_y, max_temp_center_x = (int(np.average(max_temp_locs[0])),
                                                int(np.average(max_temp_locs[1])))

        update_frame_figure_profiles(fig_frame_data, fig_cross_data=fig_frame_data['autocenter_data'],
                                     x=max_temp_center_x, y=max_temp_center_y, curve_type=curve_type)

    if crosshair_enabled:
        if cross_hair_man is not None:
            ch_x = cross_hair_man[0]
            ch_y = cross_hair_man[1]
        else:
            ch_x = fig_frame_data['crosshair_data']['frame_vline'].get_xdata()
            ch_y = fig_frame_data['crosshair_data']['frame_hline'].get_ydata()
            ch_x = ch_x[0] if type(ch_x) is list else ch_x
            ch_y = ch_y[0] if type(ch_y) is list else ch_y

        update_frame_figure_profiles(fig_frame_data, fig_cross_data=fig_frame_data['crosshair_data'],
                                     x=ch_x, y=ch_y, curve_type=curve_type)

    fig.canvas.draw_idle()
    fig.canvas.flush_events()


def quit_btn_clicked(event):
    global b_quit
    b_quit = True


def normal_frame(frame, b_autorange=False):
    if not b_autorange:
        iinfo_orig = np.iinfo(frame.dtype)
        min_orig = iinfo_orig.min
        max_orig = iinfo_orig.max
    else:
        min_orig = np.min(frame)
        max_orig = np.max(frame)
        
    return (frame.astype('float') - min_orig) / (max_orig-min_orig) if max_orig != min_orig else \
            np.zeros(frame.shape, dtype='float')


def setup_orig_fig(cam_cap, b_plk=False):
    global b_quit, image_height, image_width

    fig = plt.figure('Original', figsize=(12, 7))

    supported_features = {}

    if cam_cap is not None and b_plk is False:
        for prop_name in CAM_PROP_DICT.keys():
            prop_value = get_cam_property(cam_cap, prop_name)
            if 0 <= prop_value <= 1.0:
                supported_features[prop_name] = prop_value
    else:
        supported_features = {}

    n_rows = len(supported_features) + 1
    n_cols = 3  # Orig frame + Quit Button + checkbox

    fig_row_height_ratio = [1 if i < 1 else 0.1 for i in range(0, n_rows)]

    fig_gs = GridSpec(n_rows, n_cols, figure=fig,
                      wspace=0.2,
                      hspace=0.2,
                      width_ratios=[1, 0.2, 0.2],
                      height_ratios=fig_row_height_ratio,
                      )

    sliders = []
    ax_orig = fig.add_subplot(fig_gs[0, 0])

    i = 1
    for prop_name in supported_features.keys():
        ax = fig.add_subplot(fig_gs[i, :])

        s = Slider(ax, prop_name, 0, 1, supported_features[prop_name], valstep=0.01)
        s.on_changed(lambda x: set_cam_property(cam_cap, prop_name, x))
        sliders.append(s)
        i += 1

    ax_quit_button = fig.add_subplot(fig_gs[0, 1])
    btn_quit = Button(ax_quit_button, 'Quit')
    btn_quit.on_clicked(quit_btn_clicked)

    ax_options_chbox = fig.add_subplot(fig_gs[0, 2])
    chbox_options = CheckButtons(ax_options_chbox, ['Pause', 'AutoCenter', 'CrossHair'],  [False, True, True])

    if cam_cap is not None and not b_plk:
        ret, frame = cam_cap.read()
        frame_norm = normal_frame(frame)
        img = ax_orig.imshow(cv2.cvtColor(frame_norm, cv2.COLOR_BGR2RGB),
                             cmap='gray',
                             vmin=0, vmax=1, interpolation="None")
    elif cam_cap is not None and b_plk:
        frame = cam_cap.grab()
        frame_norm = normal_frame(frame)
        img = ax_orig.imshow(frame_norm,
                             cmap='gray',
                             vmin=0, vmax=1, interpolation="None")
    else:
        dummy_data = np.zeros((image_height, image_width), dtype='float')
        img = ax_orig.imshow(dummy_data,
                             cmap='gray',
                             vmin=0, vmax=1, interpolation="None")

    fig.tight_layout()

    return {
        'fig': fig,
        'axis': ax_orig,
        'img': img,
        'sliders': sliders,  # WARNING: can't remove this: needs to maintain sliders in memory
        'quit_btn': btn_quit,
        'options_chbox': chbox_options,
        'supported_features': supported_features
    }


def select_cam():
    window_title = "Select Camera (N->Next, K->Accept)"
    cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE)
    index = 0
    while index < 8:
        print(f'Current cam index is {index}')
        cam_cap = cv2.VideoCapture(index)
        if cam_cap.isOpened():
            while True:
                ret, frame = cam_cap.read()
                if ret:
                    cv2.imshow(window_title, frame)
                    c = cv2.waitKey(1)
                    if c == ord('N') or c == ord('n'):
                        cam_cap.release()
                        index += 1
                        break
                    elif c == ord('K') or c == ord('k'):
                        print(f'Current cam resolution: W{frame.shape[1]} x H{frame.shape[0]}')
                        cam_cap.release()
                        cv2.destroyWindow(window_title)
                        return index
                else:
                    index += 1
        else:
            index += 1

    raise ValueError('No more cam')


def cam_grab(cap = None, file_source = None):
    if cap is None and file_source is None:
        return False, None
    elif not cap is None:
        return cap.read()
    elif not file_source  is None:
        return True, cv2.imread(file_source, cv2.IMREAD_UNCHANGED)

    return False, None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', choices=('cam', 'file', 'pixelink'), help='input source')
    parser.add_argument('source', nargs='?', help='camera index (optional) or filename')
    parser.add_argument('-r', '--resolution', choices=('input', 'max', 'default'),
                        default='default', help='input: ask for resolution;'
                                                'max:use 4000x4000 to set the max resolution;'
                                                'default: use default resolution. =')
    parser.add_argument('-c', '--channels', nargs='+', help='red, blue, green, grey or all for enabling channels')
    parser.add_argument('-f', '--fit_type', choices=('gaussian', 'gaussian_forced',
                                                     'gaussian_manual',
                                                     'poly',
                                                     'multi_gaussian',
                                                     'lorentzian'),
                        default='gaussian',
                        help='gaussian: gaussian fit; '
                             'gaussian_forced: single gaussian forced a, x0 and offset;'
                             'gaussian_manual: forced single gaussian, with manual center (mean)'
                             'poly: (4) degree polynomial fit, no middle value etc.; '
                             'multi_gaussian: (3) overlapped'
                             'lorentzian: (3) overlapped')

    args = parser.parse_args()

    if args.input == 'cam':
        if args.source is None:
            cam_index = select_cam()
        else:
            cam_index = int(args.source)

        cap = cv2.VideoCapture(cam_index)

        if not cap.isOpened():
            raise ValueError(f"Can't open cam {cam_index}")

        ret, frame_orig = cap.read()
        if not ret:
            raise ValueError(f"Failed to read frame")

        if args.resolution == 'input':
            image_height = int(input('Image height: '))
            image_width = int(input('Image width: '))
        elif args.resolution == 'max':
            image_height = 4000
            image_width = 4000
        else:  # if args.resolution == 'default':
            image_height = frame_orig.shape[0]
            image_width = frame_orig.shape[1]

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, image_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, image_height)

        ret, frame_orig = cap.read()
        if not ret:
            raise ValueError(f"Failed to read frame")

        image_height = frame_orig.shape[0]
        image_width = frame_orig.shape[1]
        print(f'WARNING: new frame size W{image_width} x H{image_height}')
        # raise ValueError(f"Unable to set resolution to W{image_width} x H{image_height}")

    elif args.input == 'file':
        cap = None
        frame_orig = cv2.imread(args.source, cv2.IMREAD_UNCHANGED)
        image_height = frame_orig.shape[0]
        image_width = frame_orig.shape[1]
        if len(frame_orig.shape) < 3:
            args.channels = ['grey', ]
    elif args.input == 'pixelink':
        cap = PixeLINK()
        frame_orig = cap.grab()
    else:
        raise ValueError(f"Invalid input source {args.input}")

    if args.input != 'pixelink':
        if 'red' in args.channels or 'all' in args.channels:
            fig_red_data = setup_frame_figure('Red',
                                            frame_orig.shape[1], frame_orig.shape[0],
                                            curve_type=args.fit_type)
            fig_red_data['fig'].show()

        if 'blue' in args.channels or 'all' in args.channels:
            fig_blue_data = setup_frame_figure('Blue',
                                            frame_orig.shape[1], frame_orig.shape[0],
                                            curve_type=args.fit_type)
            fig_blue_data['fig'].show()

        if 'green' in args.channels or 'all' in args.channels:
            fig_green_data = setup_frame_figure('Green',
                                                frame_orig.shape[1], frame_orig.shape[0],
                                                curve_type=args.fit_type)
            fig_green_data['fig'].show()

    if 'grey' in args.channels or 'all' in args.channels or args.input == 'pixelink':
        fig_grey_data = setup_frame_figure('Grey',
                                           frame_orig.shape[1], frame_orig.shape[0],
                                           curve_type=args.fit_type)
        fig_grey_data['fig'].show()

    fig_orig_data = setup_orig_fig(cap, b_plk= (args.input == 'pixelink'))
    fig_orig = fig_orig_data['fig']
    axis_orig = fig_orig_data['axis']
    img_orig = fig_orig_data['img']
    fig_orig.show()

    options_chbox = fig_orig_data['options_chbox']

    previous_frame_time = time.process_time()

    while True:
        opt_paused, opt_autocenter_enabled, opt_crosshair_enabled = options_chbox.get_status()

        if args.input != 'pixelink':
            if 'red' in args.channels or 'all' in args.channels:
                for art in fig_red_data['autocenter_data'].values():
                    art.set_visible(opt_autocenter_enabled)

                for art in fig_red_data['crosshair_data'].values():
                    art.set_visible(opt_crosshair_enabled)

            if 'blue' in args.channels or 'all' in args.channels:
                for art in fig_blue_data['autocenter_data'].values():
                    art.set_visible(opt_autocenter_enabled)

                for art in fig_blue_data['crosshair_data'].values():
                    art.set_visible(opt_crosshair_enabled)

            if 'green' in args.channels or 'all' in args.channels:
                for art in fig_green_data['autocenter_data'].values():
                    art.set_visible(opt_autocenter_enabled)

                for art in fig_green_data['crosshair_data'].values():
                    art.set_visible(opt_crosshair_enabled)

        if 'grey' in args.channels or 'all' in args.channels or args.input == 'pixelink':
            for art in fig_grey_data['autocenter_data'].values():
                art.set_visible(opt_autocenter_enabled)

            for art in fig_grey_data['crosshair_data'].values():
                art.set_visible(opt_crosshair_enabled)

        if args.input == 'cam':
            if not opt_paused:
                ret, frame_orig = cap.read()
            else:
                ret = True
        elif args.input == 'pixelink':
            ret = True
            frame_orig = cap.grab()
        else:
            ret = True

        current_frame_time = time.process_time()

        if current_frame_time != previous_frame_time:
            fps = 1/(time.process_time() - previous_frame_time)
            previous_frame_time = time.process_time()
            print(f'FPS: {fps:>10.2f}\r', end='')
        else:
            print(f'FPS: N/A\r', end='')

        if len(frame_orig.shape) == 3:
            frame_norm = normal_frame(cv2.cvtColor(frame_orig, cv2.COLOR_BGR2RGB))
        else:
            frame_norm = normal_frame(frame_orig)

        img_orig.set_data(frame_norm)

        fig_orig.canvas.draw_idle()
        fig_orig.canvas.flush_events()

        if args.input != 'pixelink' and len(frame_norm.shape) == 3:
            frame_blue = frame_norm[:, :, 0]
            frame_green = frame_norm[:, :, 1]
            frame_red = frame_norm[:, :, 2]
            frame_gray = 0.3 * frame_red + 0.59 * frame_green + 0.11 * frame_blue
        else:
            frame_red, frame_blue, frame_green = None, None, None
            frame_gray = frame_norm

        frames = (frame_red, frame_green, frame_blue, frame_gray)

        if ret:
            if args.input != 'pixelink':
                if 'red' in args.channels or 'all' in args.channels:
                    update_frame_figure(fig_red_data, frame_red,
                                        cross_hair_man=None,
                                        autocenter_enabled=opt_autocenter_enabled,
                                        crosshair_enabled=opt_crosshair_enabled,
                                        curve_type=args.fit_type)

                if 'blue' in args.channels or 'all' in args.channels:
                    update_frame_figure(fig_blue_data, frame_blue,
                                        cross_hair_man=None,
                                        autocenter_enabled=opt_autocenter_enabled,
                                        crosshair_enabled=opt_crosshair_enabled,
                                        curve_type=args.fit_type)

                if 'green' in args.channels or 'all' in args.channels:
                    update_frame_figure(fig_green_data, frame_green,
                                        cross_hair_man=None,
                                        autocenter_enabled=opt_autocenter_enabled,
                                        crosshair_enabled=opt_crosshair_enabled,
                                        curve_type=args.fit_type)

            if 'grey' in args.channels or 'all' in args.channels or args.input == 'pixelink':
                update_frame_figure(fig_grey_data, frame_gray,
                                    cross_hair_man=None,
                                    autocenter_enabled=opt_autocenter_enabled,
                                    crosshair_enabled=opt_crosshair_enabled,
                                    curve_type=args.fit_type)

        if b_quit:
            break

    if cap is not None:
        if args.input != 'pixelink':
            cap.release()
        else:
            cap.close()