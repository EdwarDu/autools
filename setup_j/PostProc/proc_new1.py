import sys
import os
import argparse
import re
import numpy as np
from scipy.optimize import curve_fit, OptimizeWarning
import concurrent.futures
import matplotlib.pyplot as plt
import matplotlib as mpl
import traceback
import pickle
import warnings
import matplotlib.style as mplstyle
mplstyle.use('fast')


# noinspection DuplicatedCode
def display_image(data: np.ndarray, title: str = "Image", with_arrow: bool = False, cbar_norm = None):
    fig: plt.Figure = plt.figure(title)
    axes: plt.Axes = fig.add_subplot(111, aspect='equal')
    hm_v = axes.imshow(data, cmap=plt.cm.jet, norm=cbar_norm)
    axes.set_title(title)
    if not 0.001 <= np.max(np.abs(data)) <= 1000:
        fig.colorbar(hm_v, ax=axes, format='%.0e')
    else:
        fig.colorbar(hm_v, ax=axes)

    if with_arrow:
        height, width = data.shape
        x, y = np.meshgrid(np.arange(0, width, 1), np.arange(0, height, 1))
        unit = np.ones(data.shape)
        data_deg = np.deg2rad(data)
        # TODO: angle function needs to be fixed
        u = unit * np.cos(data_deg)
        v = unit * np.sin(data_deg)
        axes.quiver(x, y, u, v, angles='xy', scale_units='xy', scale=1.,
                    headwidth=0, headlength=0, headaxislength=0, pivot='mid',
                    units='dots', width=2)

    fig.tight_layout()
    fig.show()
    return fig, axes


npraw_file = sys.argv[1]

with open(npraw_file, 'r') as f_raw:
    header_line = f_raw.readline()
    xylist_str = header_line.strip().replace("#", "")
    x_str, y_str = re.split(";", xylist_str)
    xlist = [float(x) for x in re.split("[, ]", x_str) if x != ""]
    ylist = [float(y) for y in re.split("[, ]", y_str) if y != ""]

image_data = np.loadtxt(npraw_file)

fig, axes = display_image(image_data, title=npraw_file)

xtick_pos = np.arange(0, stop=len(xlist), step=5)
ytick_pos = np.arange(0, stop=len(ylist), step=5)
axes.set_xticks(xtick_pos)
axes.set_yticks(ytick_pos)

axes.set_xticklabels([str(xlist[i]) for i in xtick_pos])
axes.set_yticklabels([str(ylist[i]) for i in ytick_pos])

axes.set_autoscale_on(True)
axes.set_xlim(auto=True)
axes.set_ylim(auto=True)
axes.autoscale(tight=True)

plt.pause(1)
input('Enter to close')
plt.close()

