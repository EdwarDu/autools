from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QMessageBox
from PyQt5.QtCore import QTimer, QDir, pyqtSignal, pyqtSlot

import numpy as np
import cv2

def rotate_image(img, around, angle, scale, cords = None):
    # create another image to move to center
    height, width = img.shape[:2]
    cx, cy = around
    pad_t = max(height-2*cy, 0)
    pad_b = max(2*cy -height, 0)
    pad_l = max(width-2*cx, 0)
    pad_r = max(2*cy-width, 0)
    img2 = cv2.copyMakeBorder(img, pad_t, pad_b, pad_l, pad_r, cv2.BORDER_CONSTANT,
                              value=0)
    cv2.imshow("Padded", img2)
    corners = [[pad_l, pad_t, 1], [width+pad_l, pad_t, 1], [pad_l, height+pad_t, 1], [width+pad_l, height+pad_t, 1]]
    h2, w2 = img2.shape[:2]
    rx, ry = w2/2, h2/2
    rotate_matrix = cv2.getRotationMatrix2D(center=(rx, ry),angle=angle, scale=scale)
    abs_cos = abs(rotate_matrix[0,0])
    abs_sin = abs(rotate_matrix[0,1])
    bound_w = int(h2*abs_sin + w2 * abs_cos)
    bound_h = int(h2*abs_cos + w2 * abs_sin)
    rotate_matrix[0, 2] += bound_w/2 - rx
    rotate_matrix[1, 2] += bound_h/2 - ry
    img_rotated = cv2.warpAffine(src=img2, M=rotate_matrix, dsize=(bound_w, bound_h))
    cv2.imshow("Rotated", img_rotated)
    b_xs = []
    b_ys = []
    for corner in corners:
        corner_n = np.dot(rotate_matrix, corner)
        b_xs.append(corner_n[0])
        b_ys.append(corner_n[1])

    b_t = int(min(b_ys))
    b_b = int(max(b_ys))
    b_l = int(min(b_xs))
    b_r = int(max(b_xs))

    new_cords = []
    if cords is not None:
        for cord in cords:
            cord2 = [cord[0]+pad_l, cord[1]+pad_t, 1]
            cord_n = np.dot(rotate_matrix, cord2)
            new_cords.append([cord_n[0]-b_l, cord_n[0]-b_t])
    img_bound = img_rotated[b_t:b_b, b_l:b_r]
    cv2.imshow("Rebound", img_bound)
    return img_bound, new_cords

img_orig = cv2.imread('../tests/test.jpg', cv2.IMREAD_GRAYSCALE)

while True:
  print(img_orig.shape[:2])
  around_x = int(input("Around X:"))
  around_y = int(input("Around Y:"))
  angle = float(input("Angle: "))
  rotate_image(img_orig, (around_x, around_y), angle, 1, None)
  cv2.waitKey(0)
