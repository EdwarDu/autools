#!/usr/bin/env python3

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np


class SR830PlotWidget(pg.GraphicsLayoutWidget):
    def __init__(self, parent=None, **kargs):
        pg.GraphicsLayoutWidget.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle("SR830 Data Plot")
        self.p_ch1 = self.addPlot()
        self.nextRow()
        self.p_ch2 = self.addPlot()

        self.p_ch1.setXRange(0, 110, padding=0)
        self.p_ch2.setXRange(0, 110, padding=0)
        self.p_ch1.setYRange(0, 1)
        self.p_ch2.setYRange(0, 1)

        self.ch1_data = np.array([])
        self.ch2_data = np.array([])
        self.ch1_left = 0
        self.ch1_right = 0
        self.ch2_left = 0
        self.ch2_right = 0
        self.ch1_curve = self.p_ch1.plot(range(self.ch1_left, self.ch1_right), self.ch1_data, symbol='x')
        self.ch2_curve = self.p_ch2.plot(range(self.ch2_left, self.ch2_right), self.ch2_data, symbol='x')

        self.ch1_curve_point = None  # pg.CurvePoint(self.ch1_curve, pos=1)
        self.ch1_curve_note = pg.TextItem(text="")
        self.p_ch1.addItem(self.ch1_curve_note)
        # self.ch1_curve_note.setParentItem(self.ch1_curve_point)

        self.ch2_curve_point = None  # pg.CurvePoint(self.ch2_curve, pos=1)
        self.ch2_curve_note = pg.TextItem(text="")
        self.p_ch2.addItem(self.ch2_curve_note)
        # self.ch2_curve_note.setParentItem(self.ch2_curve_point)

        self.n_records2keep = 100

    def set_title(self, new_title: str):
        self.setWindowTitle(new_title)

    def add_data(self, new_data1, new_data2):
        self.ch1_right += 1
        self.ch2_right += 1
        self.ch1_data = np.append(self.ch1_data, new_data1)
        self.ch2_data = np.append(self.ch2_data, new_data2)
        # Trim the data
        self.ch1_data = self.ch1_data[-self.n_records2keep:]
        self.ch2_data = self.ch2_data[-self.n_records2keep:]

        if self.ch1_right - self.ch1_left > self.n_records2keep:
            self.ch1_left = self.ch1_right - self.n_records2keep
        if self.ch2_right - self.ch2_left > self.n_records2keep:
            self.ch2_left = self.ch2_right - self.n_records2keep

        self.update()

    def clear_data(self, ):
        self.ch1_data = np.array([])
        self.ch2_data = np.array([])
        self.update()

    def update(self):
        self.ch1_curve.setData(range(self.ch1_left, self.ch1_right), self.ch1_data)
        self.ch2_curve.setData(range(self.ch2_left, self.ch2_right), self.ch2_data)

        if len(self.ch1_data) > 0:
            self.ch1_curve_point = pg.CurvePoint(self.ch1_curve, pos=1)
            self.ch1_curve_note.setParentItem(self.ch1_curve_point)
            self.ch1_curve_note.setText(f"{self.ch1_right}: {self.ch1_data[-1]:.4f}")

        if len(self.ch2_data) > 0:
            self.ch2_curve_point = pg.CurvePoint(self.ch2_curve, pos=1)
            self.ch2_curve_note.setParentItem(self.ch2_curve_point)
            self.ch2_curve_note.setText(f"{self.ch2_right}: {self.ch2_data[-1]:.4f}")

        self.p_ch1.setXRange(self.ch1_left, self.ch1_right + 10)
        self.p_ch1.setYRange(np.min(self.ch1_data) * 0.9, np.max(self.ch1_data) * 1.1)
        self.p_ch2.setXRange(self.ch2_left, self.ch2_right + 10)
        self.p_ch2.setYRange(np.min(self.ch2_data) * 0.9, np.max(self.ch2_data) * 1.1)



