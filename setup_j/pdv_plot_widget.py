#!/usr/bin/env python3

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np


class PDVPlotWidget(pg.GraphicsLayoutWidget):
    def __init__(self, parent=None, **kargs):
        pg.GraphicsLayoutWidget.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle("Photo Diode Voltage Plot")
        self.p_ch1 = self.addPlot()

        # self.p_ch1.setXRange(0, 1000)
        self.p_ch1.setYRange(-1, 11)
        self.p_ch1.showGrid(x=True, y=True, alpha=0.5)
        self.p_ch1.enableAutoRange(self.p_ch1.getViewBox().XAxis, enable=True)
        self.p_ch1.enableAutoRange(self.p_ch1.getViewBox().YAxis, enable=False)

        self.ch1_ts_data = np.array([0, ])
        self.ch1_vol_data = np.array([0, ])
        self.ch1_curve = self.p_ch1.plot(self.ch1_ts_data, self.ch1_vol_data, symbol='x')

        self.ch1_curve_point = pg.CurvePoint(self.ch1_curve, pos=1)
        self.ch1_curve_note = pg.TextItem(text="", anchor=(1, 1), color=(0, 255, 0))
        self.p_ch1.addItem(self.ch1_curve_note, ignoreBounds=True)
        
        # self.ch1_curve_note.setParentItem(self.ch1_curve_point)

        self.n_records2keep = 100

    def add_data(self, time_diff: float, voltage: float):
        self.ch1_ts_data = np.append(self.ch1_ts_data, time_diff)[-self.n_records2keep:]
        self.ch1_vol_data = np.append(self.ch1_vol_data, voltage)[-self.n_records2keep:]

        self.update()

    def update(self):
        self.ch1_curve.setData(self.ch1_ts_data, self.ch1_vol_data)
        if len(self.ch1_ts_data) > 0:
            self.ch1_curve_point = pg.CurvePoint(self.ch1_curve, pos=1)
            self.ch1_curve_note.setParentItem(self.ch1_curve_point)
            self.ch1_curve_note.setText(f"{self.ch1_ts_data[-1]:.2f}: {self.ch1_vol_data[-1]:.4f}")

