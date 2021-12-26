#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot
import pyqtgraph as pg
import pyqtgraph.exporters
from matplotlib import cm
import numpy as np
import cv2
from scipy.optimize import curve_fit, OptimizeWarning
import math
import warnings

# pg.setConfigOption('background', 'w')
# pg.setConfigOption('foreground', 'k')


def gaussian_saturated(x, a, x0, sigma, offset):
    return np.clip(a * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2)) + offset, 0, 1)


def gaussian(x, a, x0, sigma, offset):
    return a * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2)) + offset


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

            fit_value = gaussian(frame_line_x, *popt)
            mid_left = mean - 2.355 * sigma / 2
            mid_right = mean + 2.355 * sigma / 2

            return mid_left, mid_right, a, offset, mean, fit_value
        except (ValueError, RuntimeError, OptimizeWarning, RuntimeWarning, RuntimeError) as e:
            # print(e)
            return None, None, None, None, None, None


# FIT_LINE_COLOR=pg.mkColor(0, 0, 255)
# FRAME_LINE_COLOR=pg.mkColor(0, 0, 0)
# NOTE_COLOR=pg.mkColor(0, 0, 255)
# LINE_LABEL_COLOR=pg.mkColor(0, 0, 255)
# CH_LINE_COLOR=pg.mkColor(0, 255, 0)
# MID_LINE_COLOR=pg.mkColor(255, 0, 255)

FIT_LINE_COLOR=pg.mkColor('y')
FRAME_LINE_COLOR=pg.mkColor('w')
NOTE_COLOR=pg.mkColor(0, 255, 0)
LINE_LABEL_COLOR=pg.mkColor(255, 0, 255)
CH_LINE_COLOR=pg.mkColor(0, 255, 0)
MID_LINE_COLOR=pg.mkColor(255, 0, 255)

class LaserProfilerWidget(pg.GraphicsLayoutWidget):
    image_size_changed = pyqtSignal(int, int, name='image_size_changed')
    hprof_dsize_changed = pyqtSignal(float, name='hprof_dsize_changed')
    vprof_dsize_changed = pyqtSignal(float, name='vprof_dsize_changed')

    def __init__(self, parent=None, **kargs):
        pg.GraphicsLayoutWidget.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle("Laser Profiler Plot")
        self.profile_lbl = pg.LabelItem(f"", justify='left')
        self.addItem(self.profile_lbl)
        self.__h_profile_info=""
        self.__v_profile_info=""
        #self.nextCol()
        self.p_horizontal = self.addPlot()
        self.nextRow()
        self.p_vertical = self.addPlot()
        self.p_map = self.addPlot()

        self.__calc_pixelsize = 1.0

        self.p_vertical.invertY()
        self.image_data = np.random.rand(100, 100)
        self.map_img = pg.ImageItem()
        self.map_img.setOpts(axisOrder="row-major")
        self.map_img.setLevels([0, 1])
        self.map_img.setImage(image=self.image_data)
        self.__orig_image_data = self.image_data
        self.__img_rotate_angle = 0
        self.__img_hotspot_x = 0
        self.__img_hotspot_y = 0

        self.p_map.addItem(self.map_img)
        self.p_map.setXLink(self.p_horizontal)
        self.p_map.setYLink(self.p_vertical)
        self.p_map.setAspectLocked(lock=True, ratio=1)
        self.p_map.invertY()
        self.p_map.showGrid(x=True, y=True, alpha=0.5)
        self.p_map.enableAutoRange(self.p_map.getViewBox().XYAxes, enable=True)

        self.img_gradient_item = pg.GradientEditorItem()
        self.img_gradient_item.loadPreset('thermal')
        self.img_gradient_item.setOrientation('right')
        self.img_gradient_item.setTickValue(0, 0)
        self.img_gradient_item.setTickValue(-1, 1)
        self.map_img.setLookupTable(self.img_gradient_item.colorMap().getLookupTable(0, 1, 256), update=True)
        self.img_gradient_item.sigGradientChangeFinished.connect(
            lambda: self.map_img.setLookupTable(self.img_gradient_item.colorMap().getLookupTable(0, 1, 256),
                                                update=True))
        self.addItem(self.img_gradient_item)

        q_layout = self.ci.layout
        q_layout.setColumnStretchFactor(0, 3)
        q_layout.setColumnStretchFactor(1, 7)
        q_layout.setRowStretchFactor(0, 3)
        q_layout.setRowStretchFactor(1, 7)

        self.image_width = self.image_data.shape[1]
        self.image_height = self.image_data.shape[0]
        self.map_v_line = pg.InfiniteLine(angle=90, movable=True,
                                          label="{value:.3f}",
                                          labelOpts={"position": 0.05,
                                                     "color": LINE_LABEL_COLOR,
                                                     "rotateAxis": (1, 0),
                                                     "angle": -180},
                                          bounds=[0, self.image_width-0.001],
                                          pen=pg.mkPen(CH_LINE_COLOR, width=1, style=QtCore.Qt.SolidLine))
        self.map_h_line = pg.InfiniteLine(angle=0, movable=True,
                                          label="{value:.3f}",
                                          labelOpts={"position": 0.05, "color": LINE_LABEL_COLOR},
                                          bounds=[0, self.image_height-0.001],
                                          pen=pg.mkPen(CH_LINE_COLOR, width=1, style=QtCore.Qt.SolidLine))
        self.p_map.addItem(self.map_v_line)
        self.p_map.addItem(self.map_h_line)
        self.map_v_line.setPos(0)
        self.map_h_line.setPos(0)

        self.p_h_vline = pg.InfiniteLine(angle=90, movable=False,
                                         pen=pg.mkPen(CH_LINE_COLOR, width=1, style=QtCore.Qt.SolidLine))
        self.p_v_hline = pg.InfiniteLine(angle=0, movable=False,
                                         pen=pg.mkPen(CH_LINE_COLOR, width=1, style=QtCore.Qt.SolidLine))
        self.p_horizontal.addItem(self.p_h_vline)
        self.p_vertical.addItem(self.p_v_hline)
        self.p_v_hline.setPos(0)
        self.p_h_vline.setPos(0)

        self.h_profile_line = self.p_horizontal.plot(range(0, self.image_width),
                                                     self.image_data[int(self.map_h_line.getPos()[1]), :],
                                                     pen=pg.mkPen(FRAME_LINE_COLOR, width=2, style=QtCore.Qt.SolidLine))
        self.v_profile_line = self.p_vertical.plot(self.image_data[:, int(self.map_v_line.getPos()[0])],
                                                   range(0, self.image_height),
                                                   pen=pg.mkPen(FRAME_LINE_COLOR, width=2, style=QtCore.Qt.SolidLine))

        self.h_profile_peakline = pg.InfiniteLine(angle=0, pos=1, movable=False,
                                                  label="{value:.3f}",
                                                  labelOpts={"position": 0.2, 'color': FRAME_LINE_COLOR},
                                                  pen=pg.mkPen(FRAME_LINE_COLOR, width=2, style=QtCore.Qt.DashLine))
        self.h_profile_bottomline = pg.InfiniteLine(angle=0, pos=0, movable=False,
                                                    label="{value:.3f}",
                                                    labelOpts={"position": 0.2, 'color': FRAME_LINE_COLOR},
                                                    pen=pg.mkPen(FRAME_LINE_COLOR, width=2, style=QtCore.Qt.DashLine))

        self.p_horizontal.addItem(self.h_profile_peakline)
        self.p_horizontal.addItem(self.h_profile_bottomline)

        self.v_profile_peakline = pg.InfiniteLine(angle=90, pos=1, movable=False,
                                                  label="{value:.3f}",
                                                  labelOpts={"position": 0.2,
                                                             "rotateAxis": (1, 0),
                                                             "angle": -180,
                                                             'color': FRAME_LINE_COLOR
                                                             },
                                                  pen=pg.mkPen(FRAME_LINE_COLOR, width=2, style=QtCore.Qt.DashLine))
        self.v_profile_bottomline = pg.InfiniteLine(angle=90, pos=0, movable=False,
                                                    label="{value:.3f}",
                                                    labelOpts={"position": 0.2,
                                                               "rotateAxis": (1, 0),
                                                               "angle": -180,
                                                               'color': FRAME_LINE_COLOR
                                                               },
                                                    pen=pg.mkPen(FRAME_LINE_COLOR, width=2, style=QtCore.Qt.DashLine))

        self.p_vertical.addItem(self.v_profile_peakline)
        self.p_vertical.addItem(self.v_profile_bottomline)

        self.map_v_line.sigPositionChanged.connect(lambda l: self.map_crosshair_v_moved(l))
        self.map_h_line.sigPositionChanged.connect(lambda l: self.map_crosshair_h_moved(l))

        self.h_profile_fitline = self.p_horizontal.plot(range(0, self.image_width), np.zeros(self.image_width),
                                                        pen=pg.mkPen(FIT_LINE_COLOR, width=2, style=QtCore.Qt.SolidLine))
        self.v_profile_fitline = self.p_vertical.plot(np.zeros(self.image_height), range(0, self.image_height),
                                                      pen=pg.mkPen(FIT_LINE_COLOR, width=2, style=QtCore.Qt.SolidLine))

        self.h_profile_peakline_fit = pg.InfiniteLine(angle=0, pos=1, movable=False,
                                                      label="{value:.3f}",
                                                      labelOpts={"position": 0.8, "color": FIT_LINE_COLOR},
                                                      pen=pg.mkPen(FIT_LINE_COLOR, width=2, style=QtCore.Qt.DashLine))
        self.h_profile_bottomline_fit = pg.InfiniteLine(angle=0, pos=0, movable=False,
                                                        label="{value:.3f}",
                                                        labelOpts={"position": 0.8, "color": FIT_LINE_COLOR},
                                                        pen=pg.mkPen(FIT_LINE_COLOR, width=2, style=QtCore.Qt.DashLine))
        self.h_profile_mid_line = self.p_horizontal.plot([0, 1, 2], [0, 0, 0],
                                                         pen=pg.mkPen(MID_LINE_COLOR, width=2),
                                                         symbolBrush=(255, 0, 0), symbolPen='w', symbol='o')
        self.h_profile_mid_line_point = pg.CurvePoint(self.h_profile_mid_line)
        self.h_profile_mid_note = pg.TextItem("", anchor=(1, 1), color=NOTE_COLOR)
        self.h_profile_mid_note.setParentItem(self.h_profile_mid_line_point)
        self.p_horizontal.addItem(self.h_profile_mid_note, ignoreBounds=True)

        self.p_horizontal.addItem(self.h_profile_peakline_fit)
        self.p_horizontal.addItem(self.h_profile_bottomline_fit)

        self.v_profile_peakline_fit = pg.InfiniteLine(angle=90, pos=1, movable=False,
                                                      label="{value:.3f}",
                                                      labelOpts={"position": 0.8, "color": FIT_LINE_COLOR,
                                                                 "rotateAxis": (1, 0),
                                                                 "angle": -180},
                                                      pen=pg.mkPen(FIT_LINE_COLOR, width=2, style=QtCore.Qt.DashLine))
        self.v_profile_bottomline_fit = pg.InfiniteLine(angle=90, pos=0, movable=False,
                                                        label="{value:.3f}",
                                                        labelOpts={"position": 0.8,
                                                                   "color": FIT_LINE_COLOR,
                                                                   "rotateAxis": (1, 0),
                                                                   "angle": -180},
                                                        pen=pg.mkPen(FIT_LINE_COLOR, width=2, style=QtCore.Qt.DashLine))

        self.v_profile_mid_line = self.p_vertical.plot([0, 0, 0], [0, 1, 2],
                                                       pen=pg.mkPen(MID_LINE_COLOR, width=2),
                                                       symbolBrush=(255, 0, 0), symbolPen='w', symbol='o')
        self.v_profile_mid_line_point = pg.CurvePoint(self.v_profile_mid_line)
        self.v_profile_mid_note = pg.TextItem("", angle=90, anchor=(1, 1), color=NOTE_COLOR)
        self.v_profile_mid_note.setParentItem(self.v_profile_mid_line_point)
        self.p_vertical.addItem(self.v_profile_mid_note, ignoreBounds=True)

        self.p_vertical.addItem(self.v_profile_peakline_fit)
        self.p_vertical.addItem(self.v_profile_bottomline_fit)

        self.__gaussian_fit_force_peak = True
        self.__cross_hair_auto_hotspot = True
        self.__gaussian_fit_manual_mean = False
        self.__rotate_around_hotspot = False

        self.p_horizontal.setMouseEnabled(x=True, y=False)
        self.p_vertical.setMouseEnabled(x=False, y=True)
        self.refresh()

        self.h_dist = None
        self.v_dist = None
        self.cross_markers = []
        self.cross_marker_lines = []

    def update_profile_info(self, h_profile_info, v_profile_info):
        if h_profile_info is not None:
            self.__h_profile_info = h_profile_info
        if v_profile_info is not None:
            self.__v_profile_info = v_profile_info
        info_text = f"H Profile:<br/>{self.__h_profile_info}<br/>V Profile:<br/>{self.__v_profile_info}"
        self.profile_lbl.setText(info_text, color="#00FF00")

    def draw_cross_markers(self):
        self.remove_all_cross_markers()

        i = 0
        for i in range(0, len(self.cross_markers)):
            # if i != len(self.cross_markers) - 1:
            #     line_color = (0, 255, 0, 0.5)
            #     line_style = QtCore.Qt.DashDotLine
            # else:
            row, col = self.cross_markers[i]
            self.add_cross_marker(row, col)

    def add_cross_marker(self, row=None, col=None):
        if row is None:
            row = self.map_h_line.value()
        if col is None:
            col = self.map_v_line.value()

        line_color = (0, 255, 0, 200)
        line_style = QtCore.Qt.DashDotLine

        v_line = pg.InfiniteLine(angle=90, pos=col, movable=False,
                                 label="{value:.3f}",
                                 labelOpts={"position": 0.2,
                                            "color": (0, 255, 0),
                                            "rotateAxis": (1, 0),
                                            "angle": -180},
                                 pen=pg.mkPen(line_color, width=1, style=line_style))
        self.p_map.addItem(v_line)
        self.cross_marker_lines.append(v_line)

        h_line = pg.InfiniteLine(angle=0, pos=row, movable=False,
                                 label="{value:.3f}",
                                 labelOpts={"position": 0.2,
                                            "color": (0, 255, 0)},
                                 pen=pg.mkPen(line_color, width=1, style=line_style))
        self.p_map.addItem(h_line)
        self.cross_marker_lines.append(h_line)

    def remove_all_cross_markers(self):
        for line in self.cross_marker_lines:
            self.p_map.removeItem(line)

        self.cross_marker_lines = []

    def map_crosshair_v_moved(self, l: pg.InfiniteLine):
        self.p_h_vline.setPos(l.getPos())
        self.update_v_profile()
        if self.__gaussian_fit_manual_mean:
            self.update_h_profile()

    def update_v_profile(self):
        try:
            v_index = int(self.map_v_line.getPos()[0])
            line_x = self.image_data[:, v_index]
            line_y = np.linspace(0, (self.image_height-1), num=self.image_height)
            self.v_profile_line.setData(x=line_x, y=line_y)
            mid_top, mid_bottom, a, offset, mean, fit_value = get_middle_distance(
                line_y, line_x,
                forced=self.__gaussian_fit_force_peak,
                manual_mean=int(self.map_h_line.value()) if self.__gaussian_fit_manual_mean else None)
            self.v_profile_fitline.setData(x=fit_value, y=line_y)
            self.v_profile_peakline.setPos(np.max(line_x))
            self.v_profile_bottomline.setPos(np.min(line_x))
            self.v_profile_peakline_fit.setPos(np.max(fit_value))
            self.v_profile_bottomline_fit.setPos(np.min(fit_value))
            self.v_profile_mid_line.setData([a / 2 + offset, a / 2 + offset, a / 2 + offset],
                                            [0, mid_top, mid_bottom],)
            self.v_profile_mid_line_point = pg.CurvePoint(self.v_profile_mid_line, pos=0)
            self.v_profile_mid_note.setParentItem(self.v_profile_mid_line_point)
            self.v_profile_mid_note.setText(f"T:{mid_top:.3f}, B:{mid_bottom:.3f}\n"
                                            f"D:{mid_bottom - mid_top:.3f}")
            self.update_profile_info(None, f"&nbsp;&nbsp;T:{mid_top:8.3f}, B:{mid_bottom:8.3f}<br/>&nbsp;&nbsp;D:{mid_bottom - mid_top:8.3f}")
            self.vprof_dsize_changed.emit(mid_bottom-mid_top)
            self.v_dist = mid_bottom - mid_top
        except:
            pass

    def map_crosshair_h_moved(self, l: pg.InfiniteLine):
        self.p_v_hline.setPos((l.getPos()))
        self.update_h_profile()
        if self.__gaussian_fit_manual_mean:
            self.update_v_profile()

    def update_h_profile(self):
        try:
            h_index = int(self.map_h_line.getPos()[1])
            line_x = np.linspace(0, (self.image_width-1), num=self.image_width)
            line_y = self.image_data[h_index, :]
            self.h_profile_line.setData(x=line_x, y=line_y)
            mid_left, mid_right, a, offset, mean, fit_value = get_middle_distance(
                line_x, line_y,
                forced=self.__gaussian_fit_force_peak,
                manual_mean=int(self.map_v_line.value()) if self.__gaussian_fit_manual_mean else None)
            self.h_profile_fitline.setData(x=line_x, y=fit_value)
            self.h_profile_peakline.setPos(np.max(line_y))
            self.h_profile_bottomline.setPos(np.min(line_y))
            self.h_profile_peakline_fit.setPos(np.max(fit_value))
            self.h_profile_bottomline_fit.setPos(np.min(fit_value))
            self.h_profile_mid_line.setData([mid_left, mid_right, self.image_width], [a/2+offset, a/2+offset, a/2+offset])
            self.h_profile_mid_line_point = pg.CurvePoint(self.h_profile_mid_line, pos=1)
            self.h_profile_mid_note.setParentItem(self.h_profile_mid_line_point)
            self.h_profile_mid_note.setText(f"L:{mid_left:.3f}, R:{mid_right:.3f}\n"
                                            f"D:{mid_right-mid_left:.3f}")
            self.update_profile_info(f"&nbsp;&nbsp;L:{mid_left:8.3f}, R:{mid_right:8.3f}<br/>&nbsp;&nbsp;D:{mid_right-mid_left:8.3f}", None)
            self.hprof_dsize_changed.emit(mid_right-mid_left)
            self.h_dist = mid_right - mid_left
        except:
            pass

    @staticmethod
    def get_img_data_hotspot(image_data):
        max_temp = np.max(image_data)
        max_temp_locs = np.where(image_data == max_temp)
        max_temp_center_y, max_temp_center_x = (np.average(max_temp_locs[0]),
                                                np.average(max_temp_locs[1]))
        return max_temp_center_x, max_temp_center_y

    # NOT USED, the moving and clipping operations in this method is useless
    @staticmethod
    def rotate_image(img, around, angle, scale, cords = None):
        # create another image to move to center
        # Works, but not necessary
        height, width = img.shape[:2]
        cx, cy = around
        pad_t = max(height-2*cy, 0)
        pad_b = max(2*cy -height, 0)
        pad_l = max(width-2*cx, 0)
        pad_r = max(2*cy-width, 0)
        img2 = cv2.copyMakeBorder(img, pad_t, pad_b, pad_l, pad_r, cv2.BORDER_CONSTANT,
                                  value=0)
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
        return img_bound, new_cords

    def update_image_data(self, image_data):
        img_height, img_width = image_data.shape[:2]
        self.__orig_image_data = image_data.copy()
        if img_height != self.image_height or img_width != self.image_width:
            # if origin image size changed then emit
            self.image_size_changed.emit(img_width, img_height)

        if self.__img_rotate_angle != 0:
            rx, ry = img_width/2, img_height/2
            rotate_matrix = cv2.getRotationMatrix2D(center=(rx, ry),angle=self.__img_rotate_angle, scale=1)
            abs_cos = abs(rotate_matrix[0,0])
            abs_sin = abs(rotate_matrix[0,1])
            bound_w = int(img_height*abs_sin + img_width * abs_cos)
            bound_h = int(img_height*abs_cos + img_width * abs_sin)
            rotate_matrix[0, 2] += bound_w/2 - rx
            rotate_matrix[1, 2] += bound_h/2 - ry
            image_data = cv2.warpAffine(src=image_data, M=rotate_matrix, dsize=(bound_w, bound_h))
            
            # Can'g rotate the mpa_h_line and map_v_line's cords every time, auto hotspot will set them below
            # otherwise leave them be
            #cord=[self.map_v_line.value(), self.map_h_line.value(), 1]
            #new_cord=np.dot(rotate_matrix, cord)
            #self.map_v_line.setValue(new_cord[0])
            #self.map_h_line.setValue(new_cord[1])

        self.image_data = image_data
        self.map_img.setImage(image=self.image_data)
        self.image_height, self.image_width = self.image_data.shape[:2]
        self.map_h_line.setBounds([0, self.image_height-0.001])
        self.map_v_line.setBounds([0, self.image_width-0.001])
        if self.__cross_hair_auto_hotspot:
            hs_x, hs_y = LaserProfilerWidget.get_img_data_hotspot(self.image_data)
            self.__img_hotspot_x = hs_x
            self.__img_hotspot_y = hs_y
            self.map_v_line.setValue(hs_x)
            self.map_h_line.setValue(hs_y)
        self.update_h_profile()
        self.update_v_profile()

    def refresh(self):
        self.update_image_data(self.__orig_image_data)

    def get_h_frame_line(self, h_index: int = None):
        if h_index is None:
            h_index = int(self.map_h_line.value())

        return self.image_data[h_index, :], h_index

    def get_v_frame_line(self, v_index: int = None):
        if v_index is None:
            v_index = int(self.map_v_line.value())

        return self.image_data[:, v_index], v_index

    def get_profile_distances(self):
        return self.h_dist, self.v_dist

    @staticmethod
    def get_color_map(cmap_name: str):
        colormap = cm.get_cmap(cmap_name)
        colormap._init()
        lut = (colormap._lut * 255).view(np.ndarray)
        return lut

    @property
    def cross_hair_auto_hotspot(self):
        return self.__cross_hair_auto_hotspot

    @cross_hair_auto_hotspot.setter
    def cross_hair_auto_hotspot(self, b_auto_loc: bool):
        if b_auto_loc != self.__cross_hair_auto_hotspot:
            self.__cross_hair_auto_hotspot = b_auto_loc
            self.refresh()

    # specific function to allow lambda expression
    def set_cross_hair_auto_hotspot(self, b_auto_loc: bool):
        if b_auto_loc != self.__cross_hair_auto_hotspot:
            self.__cross_hair_auto_hotspot = b_auto_loc
            self.refresh()

    @property
    def gaussian_fit_force_peak(self):
        return self.__gaussian_fit_force_peak

    @gaussian_fit_force_peak.setter
    def gaussian_fit_force_peak(self, b_force):
        self.__gaussian_fit_force_peak = b_force
        self.update_h_profile()
        self.update_v_profile()

    def set_gaussian_fit_force_peak(self, b_force: bool):
        self.__gaussian_fit_force_peak = b_force
        self.update_h_profile()
        self.update_v_profile()

    @property
    def gaussian_fit_manual_mean(self):
        return self.__gaussian_fit_manual_mean

    @gaussian_fit_manual_mean.setter
    def gaussian_fit_manual_mean(self, b_force):
        self.__gaussian_fit_manual_mean = b_force

    @property
    def img_rotate_angle(self):
        return self.__img_rotate_angle

    @img_rotate_angle.setter
    def img_rotate_angle(self, a: float):
        if 0 <= a <= 360:
            self.__img_rotate_angle = a
            self.refresh()

    @property
    def rotate_around_hotspot(self):
        return self.__rotate_around_hotspot
    
    @rotate_around_hotspot.setter
    def rotate_around_hotspot(self, b_hotspot: bool):
        self.__rotate_around_hotspot = b_hotspot
        self.refresh()

    @property
    def hotspot_location(self):
        return self.__img_hotspot_x, self.__img_hotspot_y

    def grab_hotspot(self):
        self.__img_hotspot_x, self.__img_hotspot_y = LaserProfilerWidget.get_img_data_hotspot(self.image_data)
        return self.__img_hotspot_x, self.__img_hotspot_y

    def grab_crosshair(self):
        return int(self.map_v_line.value()), int(self.map_h_line.value())

    def set_gaussian_fit_manual_mean(self, b_force: bool):
        self.__gaussian_fit_manual_mean = b_force
        self.update_h_profile()
        self.update_v_profile()

    def export_image(self, prefix: str):
        map_exporter = pg.exporters.SVGExporter(self.scene())
        map_exporter.export(prefix+"_profile.svg")
        cv2.imwrite(prefix+"_image.png", self.image_data)
        np.savetxt(prefix+'_img.npraw', self.image_data)

    def load_raw(self, npraw_file: str):
        if npraw_file.endswith(".npraw"):
            image_data = np.loadtxt(npraw_file)
        else:
            # FIXME: add to try .. catch
            image_data = cv2.imread(npraw_file, cv2.IMREAD_GRAYSCALE)
        self.update_image_data(image_data)


def update_image(window, timer):
    import time
    # image = np.random.rand(2160, 2560)
    # t0 = time.time() * 1000
    # window.update_image_data(image)
    # t1 = time.time() * 1000
    # print(f"Update image cost {t1-t0}ms")
    # timer.singleShot(10000, lambda w=window, t=timer: update_image(w, t))
    #window.add_cross_marker()
    win.img_rotate_angle = (win.img_rotate_angle + 10) % 360
    timer.singleShot(2000, lambda w=window, t=timer: update_image(w, t))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = LaserProfilerWidget()
    win.show()
    #file_path=input("Enter test image path: ")
    file_path="../tests/test.jpg"
    win.img_rotate_angle = 5
    win.update_image_data(cv2.imread(file_path, cv2.IMREAD_GRAYSCALE))
    update_timer = QtCore.QTimer(win)
    update_timer.singleShot(10000, lambda w=win, t=update_timer: update_image(w, t))

    app.exec_()
