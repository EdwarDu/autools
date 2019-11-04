#!/usr/bin/env python3

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np


class FocusCaliPlotWidget(pg.GraphicsLayoutWidget):
    def __init__(self, parent=None, **kargs):
        pg.GraphicsLayoutWidget.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle("Data Plot")
        self.p_ch = self.addPlot(labels={'left': 'NIDAQ Vol', 'bottom': 'PZT Y'})

        self.p_ch.showGrid(x=True, y=True, alpha=0.5)
        self.p_ch.enableAutoRange(self.p_ch.getViewBox().XYAxes, enable=True)

        self.ch_lines = {}
        self.ch_cur_z = -1

        self.p_ch.addLegend(size=(100, 20))

    def set_title(self, new_title: str):
        self.setWindowTitle(new_title)

    def add_ch_line(self, z: float):
        if z not in self.ch_lines.keys():
            line_xdata = np.array([])
            line_ydata = np.array([])
            line_color = (len(self.ch_lines), 9)
            line = self.p_ch.plot(line_xdata, line_ydata,
                                  pen=pg.mkPen(line_color, width=1, style=QtCore.Qt.DotLine),
                                  symbol='x', symbolSize=4,
                                  symbolBrush=line_color,
                                  symbolPen=line_color,
                                  name=f'PZT-Z@{z:.6f}')
            self.ch_lines[z] = [line, line_xdata, line_ydata, line_color]
        else:
            self.reset_ch_line(z)

        self.ch_cur_z = z

    def reset_ch_line(self, z: float):
        cur_line = self.get_ch_line(z)
        if cur_line is None:
            return
        else:
            cur_line[1] = np.array([])
            cur_line[2] = np.array([])
            cur_line[0].setData(cur_line[1], cur_line[2])

    def select_ch_line(self, z: float):
        if z in self.ch_lines.keys():
            self.ch_cur_z = z
            return True
        else:
            return False

    def get_ch_line(self, z: float):
        if z in self.ch_lines.keys():
            return self.ch_lines[z]
        else:
            return None

    def remove_ch_line(self, z: float):
        if z in self.ch_lines.keys():
            line, line_xdata, line_ydata, line_color = self.ch_lines[z]
            self.p_ch.removeItem(line)
            del self.ch_lines[z]
            if self.ch_cur_z == z:
                self.ch_cur_z = None

    def clear_ch_lines(self):
        for line, line_xdata, line_ydata, line_color in self.ch_lines.values():
            self.p_ch.removeItem(line)
        self.ch_lines.clear()

    def add_data(self, y: float, intensity: float):
        cur_line = self.get_ch_line(self.ch_cur_z)
        if cur_line is None:
            return
        else:
            cur_line[1] = np.append(cur_line[1], y)
            cur_line[2] = np.append(cur_line[2], intensity)
            cur_line[0].setData(cur_line[1], cur_line[2])

    def clear_data(self, ):
        self.clear_ch2_lines()
        self.update()

    def highlight_ch_line(self, z: float):
        for line, line_xdata, line_ydata, line_color in self.ch_lines.values():
            line.setPen(pg.mkPen(line_color, width=1, style=QtCore.Qt.DotLine))

        if z in self.ch_lines.keys():
            line, line_xdata, line_ydata, line_color = self.ch_lines[z]
            line.setPen(pg.mkPen(line_color, width=2, style=QtCore.Qt.SolidLine))

if __name__ == "__main__":
    app = QtGui.QApplication([])
    win = FocusCaliPlotWidget()
    win.show()
    update_timer = QtCore.QTimer(win)
    #update_timer.singleShot(1000, lambda w=win, t=update_timer: update_image(w, t))

    QtGui.QApplication.instance().exec_()