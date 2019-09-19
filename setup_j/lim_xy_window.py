from .lim_xy_ui import Ui_LIM_XYTable
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5 import QtCore, QtGui


class LIM_XYWindow(Ui_LIM_XYTable):
    def __init__(self):
        self.window = QWidget()
        Ui_LIM_XYTable.__init__(self)
        self.setupUi(self.window)

        self.tableWidget_XY.setColumnCount(4)
        self.tableWidget_XY.setRowCount(0)
        self.tableWidget_XY.setHorizontalHeaderLabels(("Wave Length", "Power %", "X", "Y"))
        self.pushButton_Clear.clicked.connect(self.clear)
        self.tableWidget_XY.horizontalHeader().sortIndicatorOrder()

        self.pushButton_Copy.clicked.connect(self.copy_all)

        self.clip = QtGui.QGuiApplication.clipboard()

    def add_record(self, wlen, power, x, y):
        row_count = self.tableWidget_XY.rowCount()
        self.tableWidget_XY.setRowCount(row_count + 1)
        self.tableWidget_XY.setItem(row_count, 0, QTableWidgetItem(f"{wlen:d}"))
        self.tableWidget_XY.setItem(row_count, 1, QTableWidgetItem(f"{power:.2f}"))
        self.tableWidget_XY.setItem(row_count, 2, QTableWidgetItem(f"{x:.4f}"))
        self.tableWidget_XY.setItem(row_count, 3, QTableWidgetItem(f"{y:.4f}"))

    def add_records(self, wlen_power: list):
        for wlen, power in wlen_power:
            self.add_record(wlen, power)

    def copy_all(self, e):
        self.tableWidget_XY.selectAll()
        selected = self.tableWidget_XY.selectedRanges()
        s = ""

        for r in range(selected[0].topRow(), selected[0].bottomRow() + 1):
            for c in range(selected[0].leftColumn(), selected[0].rightColumn() + 1):
                try:
                    s += str(self.tableWidget_XY.item(r, c).text()) + "\t"
                except AttributeError:
                    s += "\t"
            s = s[:-1] + "\n"  # eliminate last '\t'
        self.clip.setText(s)

    def show(self):
        self.window.show()

    def close(self):
        self.window.hide()

    def clear(self):
        self.tableWidget_XY.setRowCount(0)
        self.tableWidget_XY.setHorizontalHeaderLabels(("Wave Length", "Power %", "X", "Y"))

