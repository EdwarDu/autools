#!/usr/bin/env python3

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np


class PCaliPlotWidget(pg.GraphicsLayoutWidget):
    def __init__(self, parent=None, **kargs):
        pg.GraphicsLayoutWidget.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle("Data Plot")
        self.p_ch1 = self.addPlot(labels={'left': 'Power %', 'bottom': 'Wave Length'})
        self.nextRow()
        self.p_ch2 = self.addPlot(labels={'left': 'NIDAQ Vol', 'bottom': 'Power %'})

        self.p_ch1.showGrid(x=True, y=True, alpha=0.5)
        self.p_ch1.enableAutoRange(self.p_ch1.getViewBox().XYAxes, enable=True)
        self.p_ch2.showGrid(x=True, y=True, alpha=0.5)
        self.p_ch2.enableAutoRange(self.p_ch1.getViewBox().XYAxes, enable=True)

        self.ch1_xdata = np.array([])
        self.ch1_ydata = np.array([])

        self.ch1_curve = self.p_ch1.plot(self.ch1_xdata, self.ch1_ydata, symbol='o')

        self.ch1_curve_point = None  # pg.CurvePoint(self.ch1_curve, pos=1)
        self.ch1_curve_note = pg.TextItem(text="", anchor=(1, 1), color=(0, 255, 0))
        self.p_ch1.addItem(self.ch1_curve_note, ignoreBounds=True)
        # self.ch1_curve_note.setParentItem(self.ch1_curve_point)

        self.ch2_lines = {}
        self.ch2_cur_wl = -1
        self.ch2_hline = pg.InfiniteLine(angle=0, movable=False,
                                         label="{value:.4f}",
                                         labelOpts={"position": 1, "color": (255, 0, 255)},
                                         pen=pg.mkPen('g', width=1, style=QtCore.Qt.SolidLine))
        self.p_ch2.addItem(self.ch2_hline)
        self.p_ch2.addLegend(size=(100, 20))

        self.ch1_mouse_sig_porxy = pg.SignalProxy(self.p_ch1.scene().sigMouseMoved,
                                                  rateLimit=60, slot=self.ch1_mouse_moved)

    def set_title(self, new_title: str):
        self.setWindowTitle(new_title)

    def add_ch2_line(self, wlen: int, color_step: int = 10):
        line_xdata = np.array([])
        line_ydata = np.array([])
        line_color = (int((wlen - 400) / color_step), 17)
        line = self.p_ch2.plot(line_xdata, line_ydata,
                               pen=pg.mkPen(line_color),
                               symbol='x', symbolSize=4,
                               symbolBrush=line_color,
                               symbolPen=line_color,
                               name=f'{wlen}')
        self.ch2_lines[wlen] = [line, line_xdata, line_ydata]
        self.ch2_cur_wl = wlen

    def select_ch2_line(self, wlen: int):
        if wlen in self.ch2_lines.keys():
            self.ch2_cur_wl = wlen
            return True
        else:
            return False

    def get_ch2_line(self, wlen: int):
        if wlen in self.ch2_lines.keys():
            return self.ch2_lines[wlen]
        else:
            return None

    def remove_ch2_line(self, wlen: int):
        if wlen in self.ch2_lines.keys():
            line, line_xdata, line_ydata = self.ch2_lines[wlen]
            self.p_ch2.removeItem(line)
            del self.ch2_lines[wlen]

    def clear_ch2_lines(self):
        for line, line_xdata, line_ydata in self.ch2_lines.values():
            self.p_ch2.removeItem(line)
        self.ch2_lines.clear()

    def add_data_ch2(self, new_data_power_perc, new_data_vol):
        h2_cur_line = self.get_ch2_line(self.ch2_cur_wl)
        if h2_cur_line is None:
            return
        else:
            h2_cur_line[1] = np.append(h2_cur_line[1], new_data_power_perc)
            h2_cur_line[2] = np.append(h2_cur_line[2], new_data_vol)
            h2_cur_line[0].setData(h2_cur_line[1], h2_cur_line[2])

    def move_ch2_hline(self, y: float):
        self.ch2_hline.setPos(y)

    def add_data(self, new_data_wl, new_data_power):
        self.ch1_xdata = np.append(self.ch1_xdata, new_data_wl)
        self.ch1_ydata = np.append(self.ch1_ydata, new_data_power)

        self.update()

    def clear_data(self, ):
        self.ch1_xdata = np.array([])
        self.ch1_ydata = np.array([])
        self.clear_ch2_lines()
        self.update()

    def update(self):
        self.ch1_curve.setData(self.ch1_xdata, self.ch1_ydata)

        if len(self.ch1_xdata) > 0:
            self.ch1_curve_point = pg.CurvePoint(self.ch1_curve, pos=1)
            self.ch1_curve_note.setParentItem(self.ch1_curve_point)
            self.ch1_curve_note.setText(f"{self.ch1_xdata[-1]}: {self.ch1_ydata[-1]:.4f}")

    def ch1_mouse_moved(self, evt):
        pos = evt[0]
        if self.p_ch1.sceneBoundingRect().contains(pos) and len(self.ch1_xdata) > 0:
            mouse_point = self.p_ch1.vb.mapSceneToView(pos)
            which = (np.abs(self.ch1_xdata - mouse_point.x())).argmin()
            self.ch1_curve_point = pg.CurvePoint(self.ch1_curve, pos=which/(len(self.ch1_xdata)-1))
            self.ch1_curve_note.setParentItem(self.ch1_curve_point)
            self.ch1_curve_note.setText(f"{self.ch1_xdata[which]}: {self.ch1_ydata[which]:.4f}")

if __name__ == "__main__":
    app = QtGui.QApplication([])
    win = PCaliPlotWidget()
    win.show()
    update_timer = QtCore.QTimer(win)
    #update_timer.singleShot(1000, lambda w=win, t=update_timer: update_image(w, t))

    QtGui.QApplication.instance().exec_()