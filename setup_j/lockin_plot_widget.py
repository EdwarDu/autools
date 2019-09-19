#!/usr/bin/env python3

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np


class LockInPlotWidget(pg.GraphicsLayoutWidget):
    def __init__(self, parent=None, **kargs):
        pg.GraphicsLayoutWidget.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle("SR830 Data Plot")
        self.p_ch1 = self.addPlot(labels={'left': 'Lock-In X', 'bottom': 'Wave Length'})
        self.nextRow()
        self.p_ch2 = self.addPlot(labels={'left': 'Lock-In Y', 'bottom': 'Wave Length'})

        self.p_ch1.showGrid(x=True, y=True, alpha=0.5)
        self.p_ch1.enableAutoRange(self.p_ch1.getViewBox().XYAxes, enable=True)
        self.p_ch2.showGrid(x=True, y=True, alpha=0.5)
        self.p_ch2.enableAutoRange(self.p_ch1.getViewBox().XYAxes, enable=True)

        self.ch1_xdata = np.array([])
        self.ch1_ydata = np.array([])
        self.ch2_xdata = np.array([])
        self.ch2_ydata = np.array([])

        self.ch1_curve = self.p_ch1.plot(self.ch1_xdata, self.ch1_ydata, symbol='x')
        self.ch2_curve = self.p_ch2.plot(self.ch2_xdata, self.ch2_ydata, symbol='x')

        self.ch1_curve_point = None  # pg.CurvePoint(self.ch1_curve, pos=1)
        self.ch1_curve_note = pg.TextItem(text="", anchor=(1, 1), color=(0, 255, 0))
        self.p_ch1.addItem(self.ch1_curve_note, ignoreBounds=True)
        # self.ch1_curve_note.setParentItem(self.ch1_curve_point)

        self.ch2_curve_point = None  # pg.CurvePoint(self.ch2_curve, pos=1)
        self.ch2_curve_note = pg.TextItem(text="", anchor=(1, 1), color=(0, 255, 0))
        self.p_ch2.addItem(self.ch2_curve_note, ignoreBounds=True)
        # self.ch2_curve_note.setParentItem(self.ch2_curve_point)

        self.ch1_mouse_sig_porxy = pg.SignalProxy(self.p_ch1.scene().sigMouseMoved,
                                                  rateLimit=60, slot=self.ch1_mouse_moved)
        self.ch2_mouse_sig_porxy = pg.SignalProxy(self.p_ch2.scene().sigMouseMoved,
                                                  rateLimit=60, slot=self.ch2_mouse_moved)

    def set_title(self, new_title: str):
        self.setWindowTitle(new_title)

    def add_data(self, new_data_wl, new_data_x, new_data_y):
        self.ch1_xdata = np.append(self.ch1_xdata, new_data_wl)
        self.ch1_ydata = np.append(self.ch1_ydata, new_data_x)
        self.ch2_xdata = np.append(self.ch2_xdata, new_data_wl)
        self.ch2_ydata = np.append(self.ch2_ydata, new_data_y)

        self.update()

    def clear_data(self, ):
        self.ch1_xdata = np.array([])
        self.ch1_ydata = np.array([])
        self.ch2_xdata = np.array([])
        self.ch2_ydata = np.array([])
        self.update()

    def update(self):
        self.ch1_curve.setData(self.ch1_xdata, self.ch1_ydata)
        self.ch2_curve.setData(self.ch2_xdata, self.ch2_ydata)

        if len(self.ch1_xdata) > 0:
            self.ch1_curve_point = pg.CurvePoint(self.ch1_curve, pos=1)
            self.ch1_curve_note.setParentItem(self.ch1_curve_point)
            self.ch1_curve_note.setText(f"{self.ch1_xdata[-1]}: {self.ch1_ydata[-1]:.4f}")

            self.ch2_curve_point = pg.CurvePoint(self.ch2_curve, pos=1)
            self.ch2_curve_note.setParentItem(self.ch2_curve_point)
            self.ch2_curve_note.setText(f"{self.ch2_xdata[-1]}: {self.ch2_ydata[-1]:.4f}")

    def ch1_mouse_moved(self, evt):
        pos = evt[0]
        if self.p_ch1.sceneBoundingRect().contains(pos) and len(self.ch1_xdata) > 0:
            mouse_point = self.p_ch1.vb.mapSceneToView(pos)
            which = (np.abs(self.ch1_xdata - mouse_point.x())).argmin()
            self.ch1_curve_point = pg.CurvePoint(self.ch1_curve, pos=which/(len(self.ch1_xdata)-1))
            self.ch1_curve_note.setParentItem(self.ch1_curve_point)
            self.ch1_curve_note.setText(f"{self.ch1_xdata[which]}: {self.ch1_ydata[which]:.4f}")

    def ch2_mouse_moved(self, evt):
        pos = evt[0]
        if self.p_ch2.sceneBoundingRect().contains(pos) and len(self.ch2_xdata) > 0:
            mouse_point = self.p_ch2.vb.mapSceneToView(pos)
            which = (np.abs(self.ch2_xdata - mouse_point.x())).argmin()
            self.ch2_curve_point = pg.CurvePoint(self.ch2_curve, pos=which/(len(self.ch2_xdata)-1))
            self.ch2_curve_note.setParentItem(self.ch2_curve_point)
            self.ch2_curve_note.setText(f"{self.ch2_xdata[which]}: {self.ch2_ydata[which]:.4f}")
