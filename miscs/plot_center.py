import sys
import os
import cv2
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

from matplotlib.ticker import FormatStrFormatter
import matplotlib.style as mplstyle


image_data = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)

max_temp = np.max(image_data)
        max_temp_locs = np.where(image_data == max_temp)
        max_temp_center_y, max_temp_center_x = (np.average(max_temp_locs[0]),
                                                np.average(max_temp_locs[1]))

print(f"Image data loaded, center in {max_temp_center_x},{max_temp_center_y}")

fig = plt.figure("To Center")
ax_main = fig.add_subplot(111)

ax_main.imshow(image_data, )

plt.show()