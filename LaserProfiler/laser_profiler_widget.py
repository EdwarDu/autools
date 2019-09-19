#!/usr/bin/env python3

import pyqtgraph as pg
import pyqtgraph.exporters
from matplotlib import cm
import numpy as np
import cv2
from PyQt5 import QtCore, QtGui
from scipy.optimize import curve_fit, OptimizeWarning
import math
import warnings


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
                    mean0 = np.average(np.where(frame_line == np.max(frame_line))) + 0.5
                else:
                    mean0 = manual_mean
                    a0 = frame_line[mean0] - np.min(frame_line)

                sigma_left = 0
                for i in range(int(mean0)-4, 2, -1):
                    if frame_line[i - 2] > frame_line[i - 1] > frame_line[i]:  # and \
                        # frame_line[i + 2] > frame_line[i + 1] > frame_line[i]:
                        sigma_left = i
                        break

                sigma_right = len(frame_line)
                for i in range(int(mean0)+4, len(frame_line)-2):
                    if frame_line[i + 2] > frame_line[i + 1] > frame_line[i]:  # and
                        # frame_line[i - 2] > frame_line[i - 1] > frame_line[i]:
                        sigma_right = i
                        break

                sigma0 = math.sqrt(np.sum(frame_line[sigma_left:sigma_right] / scale_factor *
                                          (frame_line_x[sigma_left:sigma_right] - mean0) ** 2) /
                                   (sigma_right-sigma_left))

                frame_line_x_s = frame_line_x[sigma_left:sigma_right]
                frame_line_s = frame_line[sigma_left:sigma_right]

                popt, pcov = curve_fit(gaussian, frame_line_x_s, frame_line_s,
                                       p0=[a0, mean0, sigma0, offset0],
                                       bounds=([a0 - 0.00001, mean0 - 4, -np.inf, offset0 - 0.00001],
                                               [a0 + 0.00001, mean0 + 4, +np.inf, offset0 + 0.00001]),
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
                                       bounds=([a0 - 0.00001, mean0 - 4, -np.inf, offset0 - 0.00001],
                                               [a0 + 0.00001, mean0 + 4, +np.inf, offset0 + 0.00001]),
                                       maxfev=2000)

            a, mean, sigma, offset = popt

            fit_value = gaussian(frame_line_x, *popt)
            mid_left = mean - 2.355 * sigma / 2
            mid_right = mean + 2.355 * sigma / 2

            return mid_left, mid_right, a, offset, mean, fit_value
        except (ValueError, RuntimeError, OptimizeWarning, RuntimeWarning, RuntimeError) as e:
            # print(e)
            return None, None, None, None, None, None


class LaserProfilerWidget(pg.GraphicsLayoutWidget):
    def __init__(self, parent=None, **kargs):
        pg.GraphicsLayoutWidget.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle("Laser Profiler Plot")
        # self.point_label = pg.LabelItem("r:, c:, p:", justify='left')
        # self.addItem(self.point_label)
        self.nextCol()
        self.p_horizontal = self.addPlot()
        self.nextRow()
        self.p_vertical = self.addPlot()
        self.p_map = self.addPlot()

        self.p_vertical.invertY()
        self.image_data = np.random.rand(100, 100)
        self.map_img = pg.ImageItem()
        self.map_img.setOpts(axisOrder="row-major")
        self.map_img.setLevels([0, 1])
        self.map_img.setImage(image=self.image_data)

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
                                          label="{value:.1f}",
                                          labelOpts={"position": 0.05,
                                                     "color": (255, 0, 255),
                                                     "rotateAxis": (1, 0),
                                                     "angle": -180},
                                          bounds=[0, self.image_width-0.001],
                                          pen=pg.mkPen('g', width=1, style=QtCore.Qt.SolidLine))
        self.map_h_line = pg.InfiniteLine(angle=0, movable=True,
                                          label="{value:.1f}",
                                          labelOpts={"position": 0.05, "color": (255, 0, 255)},
                                          bounds=[0, self.image_height-0.001],
                                          pen=pg.mkPen('g', width=1, style=QtCore.Qt.SolidLine))
        self.p_map.addItem(self.map_v_line)
        self.p_map.addItem(self.map_h_line)
        self.map_v_line.setPos(0)
        self.map_h_line.setPos(0)

        self.p_h_vline = pg.InfiniteLine(angle=90, movable=False,
                                         pen=pg.mkPen('g', width=1, style=QtCore.Qt.SolidLine))
        self.p_v_hline = pg.InfiniteLine(angle=0, movable=False,
                                         pen=pg.mkPen('g', width=1, style=QtCore.Qt.SolidLine))
        self.p_horizontal.addItem(self.p_h_vline)
        self.p_vertical.addItem(self.p_v_hline)
        self.p_v_hline.setPos(0)
        self.p_h_vline.setPos(0)

        self.h_profile_line = self.p_horizontal.plot(range(0, self.image_width),
                                                     self.image_data[int(self.map_h_line.getPos()[1]), :])
        self.v_profile_line = self.p_vertical.plot(self.image_data[:, int(self.map_v_line.getPos()[0])],
                                                   range(0, self.image_height))

        self.h_profile_peakline = pg.InfiniteLine(angle=0, pos=1, movable=False,
                                                  label="{value:.4f}",
                                                  labelOpts={"position": 0.2},
                                                  pen=pg.mkPen('w', width=1, style=QtCore.Qt.DashLine))
        self.h_profile_bottomline = pg.InfiniteLine(angle=0, pos=0, movable=False,
                                                    label="{value:.4f}",
                                                    labelOpts={"position": 0.2},
                                                    pen=pg.mkPen('w', width=1, style=QtCore.Qt.DashLine))

        self.p_horizontal.addItem(self.h_profile_peakline)
        self.p_horizontal.addItem(self.h_profile_bottomline)

        self.v_profile_peakline = pg.InfiniteLine(angle=90, pos=1, movable=False,
                                                  label="{value:.4f}",
                                                  labelOpts={"position": 0.2,
                                                             "rotateAxis": (1, 0),
                                                             "angle": -180
                                                             },
                                                  pen=pg.mkPen('w', width=1, style=QtCore.Qt.DashLine))
        self.v_profile_bottomline = pg.InfiniteLine(angle=90, pos=0, movable=False,
                                                    label="{value:.4f}",
                                                    labelOpts={"position": 0.2,
                                                               "rotateAxis": (1, 0),
                                                               "angle": -180},
                                                    pen=pg.mkPen('w', width=1, style=QtCore.Qt.DashLine))

        self.p_vertical.addItem(self.v_profile_peakline)
        self.p_vertical.addItem(self.v_profile_bottomline)

        self.map_v_line.sigPositionChanged.connect(lambda l: self.map_crosshair_v_moved(l))
        self.map_h_line.sigPositionChanged.connect(lambda l: self.map_crosshair_h_moved(l))

        self.h_profile_fitline = self.p_horizontal.plot(range(0, self.image_width), np.zeros(self.image_width),
                                                        pen=pg.mkPen('y', width=1, style=QtCore.Qt.SolidLine))
        self.v_profile_fitline = self.p_vertical.plot(np.zeros(self.image_height), range(0, self.image_height),
                                                      pen=pg.mkPen('y', width=1, style=QtCore.Qt.SolidLine))

        self.h_profile_peakline_fit = pg.InfiniteLine(angle=0, pos=1, movable=False,
                                                      label="{value:.4f}",
                                                      labelOpts={"position": 0.8, "color": (255, 255, 0)},
                                                      pen=pg.mkPen('y', width=1, style=QtCore.Qt.DashLine))
        self.h_profile_bottomline_fit = pg.InfiniteLine(angle=0, pos=0, movable=False,
                                                        label="{value:.4f}",
                                                        labelOpts={"position": 0.8, "color": (255, 255, 0)},
                                                        pen=pg.mkPen('y', width=1, style=QtCore.Qt.DashLine))
        self.h_profile_mid_line = self.p_horizontal.plot([0, 1, 2], [0, 0, 0],
                                                         pen=pg.mkPen((255, 0, 255), width=1),
                                                         symbolBrush=(255, 0, 0), symbolPen='w', symbol='o')
        self.h_profile_mid_line_point = pg.CurvePoint(self.h_profile_mid_line)
        self.h_profile_mid_note = pg.TextItem("", anchor=(1, 1), color=(0, 255, 0))
        self.h_profile_mid_note.setParentItem(self.h_profile_mid_line_point)
        self.p_horizontal.addItem(self.h_profile_mid_note, ignoreBounds=True)

        self.p_horizontal.addItem(self.h_profile_peakline_fit)
        self.p_horizontal.addItem(self.h_profile_bottomline_fit)

        self.v_profile_peakline_fit = pg.InfiniteLine(angle=90, pos=1, movable=False,
                                                      label="{value:.4f}",
                                                      labelOpts={"position": 0.8, "color": (255, 255, 0),
                                                                 "rotateAxis": (1, 0),
                                                                 "angle": -180},
                                                      pen=pg.mkPen('y', width=1, style=QtCore.Qt.DashLine))
        self.v_profile_bottomline_fit = pg.InfiniteLine(angle=90, pos=0, movable=False,
                                                        label="{value:.4f}",
                                                        labelOpts={"position": 0.8,
                                                                   "color": (255, 255, 0),
                                                                   "rotateAxis": (1, 0),
                                                                    "angle": -180
                                                                   },
                                                        pen=pg.mkPen('y', width=1, style=QtCore.Qt.DashLine))

        self.v_profile_mid_line = self.p_vertical.plot([0, 0, 0], [0, 1, 2],
                                                       pen=pg.mkPen((255, 0, 255), width=1),
                                                       symbolBrush=(255, 0, 0), symbolPen='w', symbol='o')
        self.v_profile_mid_line_point = pg.CurvePoint(self.v_profile_mid_line)
        self.v_profile_mid_note = pg.TextItem("", angle=90, anchor=(1, 1), color=(0, 255, 0))
        self.v_profile_mid_note.setParentItem(self.v_profile_mid_line_point)
        self.p_vertical.addItem(self.v_profile_mid_note, ignoreBounds=True)

        self.p_vertical.addItem(self.v_profile_peakline_fit)
        self.p_vertical.addItem(self.v_profile_bottomline_fit)

        self.__gaussian_fit_force_peak = True
        self.__cross_hair_auto_hotspot = True
        self.__gaussian_fit_manual_mean = False

        self.update_image_data(self.image_data)

        self.h_dist = None
        self.v_dist = None

    def map_crosshair_v_moved(self, l: pg.InfiniteLine):
        self.p_h_vline.setPos(l.getPos())
        self.update_v_profile()
        if self.__gaussian_fit_manual_mean:
            self.update_h_profile()

    def update_v_profile(self):
        try:
            v_index = int(self.map_v_line.getPos()[0])
            line_x = self.image_data[:, v_index]
            line_y = np.linspace(0, self.image_height, num=self.image_height)
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
            self.v_profile_mid_note.setText(f"T:{mid_top:.2f}, B:{mid_bottom:.2f}\n"
                                            f"D:{mid_bottom - mid_top:.2f}, Sigma:{(mid_bottom - mid_top) / 2.355:.2f}")
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
            line_x = np.linspace(0, self.image_width, num=self.image_width)
            line_y = self.image_data[h_index, :]
            self.h_profile_line.setData(y=self.image_data[h_index, :])
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
            self.h_profile_mid_note.setText(f"L:{mid_left:.2f}, R:{mid_right:.2f}\n"
                                            f"D:{mid_right-mid_left:.2f}, Sigma:{(mid_right-mid_left)/2.355:.2f}")
            self.h_dist = mid_right - mid_left
        except:
            pass

    def update_image_data(self, image_data):
        self.image_data = image_data
        self.map_img.setImage(image=self.image_data)
        self.image_width = self.image_data.shape[1]
        self.image_height = self.image_data.shape[0]
        self.map_h_line.setBounds([0, self.image_height-0.001])
        self.map_v_line.setBounds([0, self.image_width-0.001])
        if self.__cross_hair_auto_hotspot:
            max_temp = np.max(self.image_data)
            max_temp_locs = np.where(self.image_data == max_temp)
            max_temp_center_y, max_temp_center_x = (np.average(max_temp_locs[0]),
                                                    np.average(max_temp_locs[1]))
            self.map_h_line.setPos(max_temp_center_y)
            self.map_v_line.setPos(max_temp_center_x)
            self.update_h_profile()
            self.update_v_profile()
        else:
            self.update_h_profile()
            self.update_v_profile()

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
        self.__cross_hair_auto_hotspot = b_auto_loc

    # specific function to allow lambda expression
    def set_cross_hair_auto_hotspot(self, b_auto_loc: bool):
        self.__cross_hair_auto_hotspot = b_auto_loc

    @property
    def gaussian_fit_force_peak(self):
        return self.__gaussian_fit_force_peak

    @gaussian_fit_force_peak.setter
    def gaussian_fit_force_peak(self, b_force):
        self.__gaussian_fit_force_peak = b_force

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
        image_data = np.loadtxt(npraw_file)
        self.update_image_data(image_data)


def update_image(window, timer):
    import time
    image = np.random.rand(2160, 2560)
    t0 = time.time() * 1000
    window.update_image_data(image)
    t1 = time.time() * 1000
    print(f"Update image cost {t1-t0}ms")
    timer.singleShot(10000, lambda w=window, t=timer: update_image(w, t))


if __name__ == "__main__":
    app = QtGui.QApplication([])
    win = LaserProfilerWidget()
    win.show()
    win.update_image_data(cv2.imread('/home/elio/ws/autools/tests/test.jpg', cv2.IMREAD_GRAYSCALE))
    # update_timer = QtCore.QTimer(win)
    # update_timer.singleShot(1000, lambda w=win, t=update_timer: update_image(w, t))

    QtGui.QApplication.instance().exec_()
