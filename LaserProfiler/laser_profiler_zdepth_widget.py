#!/usr/bin/env python3

import pyqtgraph as pg
import pyqtgraph.exporters
from matplotlib import cm
import numpy as np
import re
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from scipy.optimize import curve_fit, OptimizeWarning
import math
from .laser_profiler_widget import get_middle_distance


class LaserProfilerZDepthWidget(pg.GraphicsLayoutWidget):
    def __init__(self, parent=None, **kargs):
        pg.GraphicsLayoutWidget.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle("Laser Profiler Plot")
        self.p_vertical = self.addPlot()
        self.z_axis = pg.AxisItem(orientation='bottom')
        self.z_axis.setTicks([{x: str(x) for x in range(0, 100)}.items()])
        self.p_map = self.addPlot(axisItems={'bottom': self.z_axis})

        self.p_vertical.invertY()
        self.image_data = np.random.rand(100, 100)
        self.z_list = np.linspace(0, 100, 100)
        self.map_img = pg.ImageItem()
        self.map_img.setOpts(axisOrder="row-major")
        self.map_img.setLevels([0, 1])
        self.map_img.setImage(image=self.image_data)

        self.p_map.addItem(self.map_img)
        self.p_map.setYLink(self.p_vertical)
        # self.p_map.setAspectLocked(lock=True, ratio=1)
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

        self.image_width = self.image_data.shape[1]
        self.image_height = self.image_data.shape[0]
        self.map_v_line = pg.InfiniteLine(angle=90, movable=True,
                                          label="{value:.1f}",
                                          labelOpts={"position": 0.2,
                                                     "color": (255, 0, 255),
                                                     # "rotateAxis": (1, 0),
                                                     # "angle": -180
                                                     },
                                          bounds=[0, self.image_width-0.001],
                                          pen=pg.mkPen('g', width=1, style=QtCore.Qt.SolidLine))
        self.map_h_line = pg.InfiniteLine(angle=0, movable=True,
                                          label="{value:.1f}",
                                          labelOpts={"position": 0.2, "color": (255, 0, 255)},
                                          bounds=[0, self.image_height - 0.001],
                                          pen=pg.mkPen('g', width=1, style=QtCore.Qt.SolidLine))
        self.p_map.addItem(self.map_v_line)
        self.p_map.addItem(self.map_h_line)
        self.map_v_line.setPos(0)
        self.map_h_line.setPos(0)

        self.p_v_hline = pg.InfiniteLine(angle=0, movable=False,
                                         pen=pg.mkPen('g', width=1, style=QtCore.Qt.SolidLine))
        self.p_vertical.addItem(self.p_v_hline)
        self.p_v_hline.setPos(0)

        self.v_profile_line = self.p_vertical.plot(self.image_data[:, int(self.map_v_line.getPos()[0])],
                                                   range(0, self.image_height))

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

        self.v_profile_fitline = self.p_vertical.plot(np.zeros(self.image_height), range(0, self.image_height),
                                                      pen=pg.mkPen('y', width=1, style=QtCore.Qt.SolidLine))

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
                                                                   "angle": -180 },
                                                        pen=pg.mkPen('y', width=1, style=QtCore.Qt.DashLine))

        self.v_profile_mid_line = self.p_vertical.plot([0, 0, 0], [0, 1, 2],
                                                       pen=pg.mkPen((255, 0, 255), width=1),
                                                       symbolBrush=(255, 0, 0), symbolPen='w', symbol='o')
        self.v_profile_mid_line_point = pg.CurvePoint(self.v_profile_mid_line)
        self.v_profile_mid_note = pg.TextItem("", angle=90, anchor=(1, 1), color=(0, 255, 0))
        self.v_profile_mid_note.setParentItem(self.v_profile_mid_line_point)
        self.p_vertical.addItem(self.v_profile_mid_note, ignoreBounds=True)

        self.__gaussian_fit_force_peak = True
        self.__gaussian_fit_manual_mean = False

        self.p_vertical.addItem(self.v_profile_peakline_fit)
        self.p_vertical.addItem(self.v_profile_bottomline_fit)

        self._flush_image_data()

        self.v_dist = None

    def set_title(self, t: str):
        self.p_map.setTitle(t)

    def map_crosshair_v_moved(self, l: pg.InfiniteLine):
        l.label.setText(f"{self.z_list[int(l.getXPos())]:.6f}")
        self.update_v_profile()

    def map_crosshair_h_moved(self, l: pg.InfiniteLine):
        self.p_v_hline.setPos((l.getPos()))
        if self.__gaussian_fit_manual_mean:
            self.update_v_profile()

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

    def set_z_list(self, z0, z1, zs):
        self.z_list = []
        z = z0
        while z <= z1:
            self.z_list.append(z)
            z += zs

        self.set_zticks()

    def set_zticks(self):
        if len(self.z_list) > 5:
            tick_list = [{i: f"{self.z_list[i]:.4f}"
                          for i in range(0, len(self.z_list), int(len(self.z_list)/5))}.items()]
        else:
            tick_list = [{i: f"{self.z_list[i]:.4f}"
                          for i in range(0, len(self.z_list))}.items()]
        self.z_axis.setTicks(tick_list)
        self.image_width = len(self.z_list)
        self.map_v_line.setBounds([0, self.image_width-0.001])
        self._flush_image_data()
        self.map_crosshair_v_moved(self.map_v_line)

    def set_height(self, height):
        self.image_height = height
        self.map_h_line.setBounds([0, self.image_height-0.001])
        self._flush_image_data()

    def _flush_image_data(self):
        self.image_data = np.zeros((self.image_height, self.image_width))
        self.map_img.setImage(self.image_data)
        self.update_v_profile()

    def set_frame_line(self, z, frame_line, line_index: int = None):
        index = self.z_list.index(z)
        self.image_data[:, index] = frame_line
        self.map_img.setImage(self.image_data)
        if line_index is not None:
            self.map_h_line.setPos(line_index)
        self.update_v_profile()

    @staticmethod
    def get_color_map(cmap_name: str):
        colormap = cm.get_cmap(cmap_name)
        colormap._init()
        lut = (colormap._lut * 255).view(np.ndarray)
        return lut

    @property
    def gaussian_fit_force_peak(self):
        return self.__gaussian_fit_force_peak

    @gaussian_fit_force_peak.setter
    def gaussian_fit_force_peak(self, b_force):
        self.__gaussian_fit_force_peak = b_force

    def set_gaussian_fit_force_peak(self, b_force: bool):
        self.__gaussian_fit_force_peak = b_force
        self.update_v_profile()

    @property
    def gaussian_fit_manual_mean(self):
        return self.__gaussian_fit_manual_mean

    @gaussian_fit_manual_mean.setter
    def gaussian_fit_manual_mean(self, b_force):
        self.__gaussian_fit_manual_mean = b_force

    def set_gaussian_fit_manual_mean(self, b_force: bool):
        self.__gaussian_fit_manual_mean = b_force
        self.update_v_profile()

    def export_image(self, prefix: str):
        map_exporter = pg.exporters.SVGExporter(self.scene())
        map_exporter.export(prefix+"_profile.svg")
        cv2.imwrite(prefix+"_image.png", self.image_data)
        np.savetxt(prefix+'_img.npraw', self.image_data, header=f'Z List: {",".join([str(x) for x in self.z_list])}')

    def load_raw(self, npraw_file: str):
        with open(npraw_file, 'r') as f_raw:
            header_line = f_raw.readline()
            zlist_str = header_line.strip().replace("# Z List: ", "")
            self.z_list = [float(x) for x in re.split("[, ]", zlist_str) if x != ""]
            self.set_zticks()

        image_data = np.loadtxt(npraw_file)
        img_height, img_width = image_data.shape
        self.set_height(img_height)

        self.image_data = image_data
        self.map_img.setImage(self.image_data)
        self.update_v_profile()


z0 = 80
z1 = 100
zs = 0.1
z = z0

def update_image(window, timer):
    global z, z1, zs, z0
    import time
    frame_line = np.random.rand(100)
    window.set_frame_line(z, frame_line)
    z += zs
    if z > z1:
        z = z0
    timer.singleShot(3000, lambda w=window, t=timer: update_image(w, t))
    QtWidgets.qApp.processEvents()


if __name__ == "__main__":
    app = QtGui.QApplication([])
    win = LaserProfilerZDepthWidget()
    win.show()
    win.set_z_list(z0, z1, zs)
    win.set_height(100)

    update_timer = QtCore.QTimer(win)
    update_timer.singleShot(3000, lambda w=win, t=update_timer: update_image(w, t))

    QtGui.QApplication.instance().exec_()
