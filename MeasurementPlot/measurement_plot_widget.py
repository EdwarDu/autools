#!/usr/bin/env python3

import pyqtgraph as pg
import pyqtgraph.exporters
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QTimer
import numpy as np
import math
import cv2
import re


class MeasurementPlotWidget(pg.GraphicsLayoutWidget):
    def __init__(self, parent=None, **kargs):
        pg.GraphicsLayoutWidget.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle("Measurement Plot")
        self.p_horizontal: pg.PlotItem = self.addPlot()
        self.nextRow()
        self.p_map = self.addPlot()

        self.xlist = np.linspace(0, 100, 20)
        self.ylist = np.linspace(0, 100, 20)
        self.image_data = np.random.rand(len(self.ylist), len(self.xlist)) * 100 + 100
        # self.image_data = np.zeros((100, 100))
        self.map_img = pg.ImageItem()
        self.map_img.setOpts(axisOrder="row-major")
        self.map_img.setLevels([0, 1])
        self.map_img.setImage(image=self.image_data)

        self.p_map.addItem(self.map_img)
        self.p_map.setAspectLocked(lock=True, ratio=1)
        # self.p_map.setXLink(self.p_horizontal)
        self.p_map.invertY()
        self.p_map.showGrid(x=True, y=True, alpha=0.5)
        # self.p_map.enableAutoRange(self.p_map.getViewBox().XYAxes, enable=True)

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
        q_layout.setRowStretchFactor(0, 4)
        q_layout.setRowStretchFactor(1, 6)

        self.image_width = self.image_data.shape[1]
        self.image_height = self.image_data.shape[0]
        self.map_h_line = pg.InfiniteLine(angle=0, movable=True,
                                          label="{value:.2f}",
                                          labelOpts={"position": 0.2, "color": (0, 255, 0)},
                                          bounds=[0, self.image_height-0.01],
                                          pen=pg.mkPen('g', width=1, style=QtCore.Qt.SolidLine))
        self.p_map.addItem(self.map_h_line)
        self.map_h_line.setPos(0)

        self.p_h_xdata = np.array(range(0, self.image_width))
        self.p_h_ydata = self.image_data[int(self.map_h_line.getPos()[1]), :]
        self.h_profile_line = self.p_horizontal.plot(self.p_h_xdata,
                                                     self.p_h_ydata,
                                                     symbol='x')
        self.p_horizontal.enableAutoRange('y', enable=True)
        self.p_horizontal.disableAutoRange(axis='x')
        self.p_horizontal.setAutoVisible(x=True, y=True)
        # self.p_horizontal.setMouseEnabled(x=True, y=False)
        self.p_horizontal.showGrid(x=True, y=True, alpha=0.5)

        self.map_h_line.sigPositionChanged.connect(lambda l: self.map_crosshair_h_moved(l))
        self.h_profile_curve_point = pg.CurvePoint(self.h_profile_line, pos=0)
        self.h_profile_data_note = pg.TextItem("", anchor=(1, 0), color=(255, 0, 255))
        self.p_horizontal.addItem(self.h_profile_data_note, ignoreBounds=True)

        self.__auto_move_h_line = True

        self.p_h_mouse_sig_porxy = pg.SignalProxy(self.p_horizontal.scene().sigMouseMoved,
                                                  rateLimit=60, slot=self.p_h_mouse_moved)

    def map_crosshair_h_moved(self, l: pg.InfiniteLine):
        l.label.setText(f"{self.ylist[int(l.value())]:.6f}")
        self.update_h_profile(0)

    def update_h_profile(self, c: int):
        h_index = int(self.map_h_line.getPos()[1])
        self.p_h_ydata = self.image_data[h_index, :]
        self.h_profile_line.setData(y=self.p_h_ydata)
        self.move_h_note(c)

    def move_h_note(self, which: int):
        self.h_profile_curve_point = pg.CurvePoint(self.h_profile_line, pos=which/(len(self.p_h_xdata) - 1))
        y_mid = sum(self.p_horizontal.getAxis("left").range) / 2
        if which < len(self.p_h_xdata) / 2:
            if self.p_h_ydata[which] < y_mid:
                self.h_profile_data_note.setAnchor((0, 1))
            else:
                self.h_profile_data_note.setAnchor((0, 0))
        else:
            if self.p_h_ydata[which] > y_mid:
                self.h_profile_data_note.setAnchor((1, 0))
            else:
                self.h_profile_data_note.setAnchor((1, 1))

        self.h_profile_data_note.setParentItem(self.h_profile_curve_point)
        self.h_profile_data_note.setText(f"X:{self.xlist[which]:.6f}\n"
                                         f"{self.p_h_ydata[which]:.6f}")

    def set_map_size(self, width: int, height: int):
        self.image_data = np.zeros((height, width))
        self.image_width = width
        self.image_height = height
        self.map_img.setImage(self.image_data)
        self.map_h_line.setBounds([0, self.image_height-0.01])

    def set_xy_list(self, xlist, ylist):
        self.xlist = np.sort(xlist)
        self.ylist = np.sort(ylist)
        self.image_width = len(self.xlist)
        self.image_height = len(self.ylist)
        self.image_data = np.zeros((self.image_height, self.image_width))
        self.map_img.setImage(self.image_data)
        self.map_h_line.setBounds([0, self.image_height-0.01])
        self.p_h_xdata = np.array(range(0, self.image_width))
        self.p_h_ydata = np.zeros(self.p_h_xdata.shape)
        self.h_profile_line.setData(x=self.p_h_xdata, y=self.p_h_ydata)
        self.map_crosshair_h_moved(self.map_h_line)

    def set_point_value(self, r: int, c: int, value: float):
        if r >= self.image_height or c >= self.image_width:
            return False
        else:
            self.image_data[r][c] = value
            self.map_img.setImage(self.image_data)
            if self.__auto_move_h_line:
                self.map_h_line.setPos(r)
            self.update_h_profile(c)

    def set_xy_value(self, x, y, value: float):
        r = np.where(self.ylist == y)[0][0]
        c = np.where(self.xlist == x)[0][0]
        self.set_point_value(r, c, value)

    def p_h_mouse_moved(self, evt):
        pos = evt[0]
        if self.p_horizontal.sceneBoundingRect().contains(pos):
            mouse_point = self.p_horizontal.vb.mapSceneToView(pos)
            which = (np.abs(self.p_h_xdata - mouse_point.x())).argmin()
            self.move_h_note(which)

    def export_image(self, prefix: str):
        map_exporter = pg.exporters.SVGExporter(self.scene())
        map_exporter.export(prefix + "_map.svg")
        cv2.imwrite(prefix + "_map_image.png", self.image_data)
        np.savetxt(prefix + '_map_img.npraw',
                   self.image_data,
                   header=f'{",".join([str(x) for x in self.xlist])};'
                          f'{",".join([str(y) for y in self.ylist])}')

    def load_raw(self, npraw_file: str):
        with open(npraw_file, 'r') as f_raw:
            header_line = f_raw.readline()
            xylist_str = header_line.strip().replace("#", "")
            x_str, y_str = re.split(";", xylist_str)
            xlist = [float(x) for x in re.split("[, ]", x_str) if x != ""]
            ylist = [float(y) for y in re.split("[, ]", y_str) if y != ""]
            self.set_xy_list(xlist, ylist)

        self.image_data = np.loadtxt(npraw_file)
        self.map_img.setImage(self.image_data)
        self.update_h_profile(self.image_width-1)
        self.map_crosshair_h_moved(self.map_h_line)


if __name__ == "__main__":
    import time

    mpw: MeasurementPlotWidget = None
    test_r = 0
    test_c = 0

    def test():
        global mpw, test_r, test_c

        mpw.set_point_value(test_r, test_c,
                            math.sin(test_c / mpw.image_width * math.pi * 2 + test_r/mpw.image_height*math.pi*2)*1000 + 1000)
        if test_c == mpw.image_width - 1:
            test_c = 0
            test_r = test_r + 1
        else:
            test_c = test_c + 1

        if test_r != mpw.image_height:
            QTimer.singleShot(0, test)

    app = QApplication([])
    win = MeasurementPlotWidget()
    win.show()
    mpw = win
    QTimer.singleShot(3000, test)
    QApplication.instance().exec_()
