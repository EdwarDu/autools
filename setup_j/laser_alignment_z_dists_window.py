from .laser_alignment_z_dists_ui import Ui_LaserAlignment_Z_DistTable
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5 import QtCore, QtGui


class QCustomTableWidgetItem(QTableWidgetItem):
    def __init__(self, value):
        super().__init__(value)

    def __lt__(self, other):
        if isinstance(other, QCustomTableWidgetItem):
            self_data_value = float(self.data(QtCore.Qt.EditRole))
            other_data_value = float(other.data(QtCore.Qt.EditRole))
            return self_data_value < other_data_value
        else:
            return QTableWidgetItem.__lt__(self, other)


class LaserAlignmentZDistsWindow(Ui_LaserAlignment_Z_DistTable):
    def __init__(self):
        self.window = QWidget()
        Ui_LaserAlignment_Z_DistTable.__init__(self)
        self.setupUi(self.window)

        self.tableWidget_Z_Dists.setColumnCount(3)
        self.tableWidget_Z_Dists.setRowCount(0)
        self.tableWidget_Z_Dists.setHorizontalHeaderLabels(("Z", "H Dist", "V Dist"))
        self.pushButton_Clear.clicked.connect(self.clear)
        self.tableWidget_Z_Dists.horizontalHeader().sortIndicatorOrder()

        self.pushButton_Copy.clicked.connect(self.copy_all)

        self.clip = QtGui.QGuiApplication.clipboard()

    def add_record(self, z, h_dist, v_dist):
        row_count = self.tableWidget_Z_Dists.rowCount()
        self.tableWidget_Z_Dists.setRowCount(row_count+1)
        self.tableWidget_Z_Dists.setItem(row_count, 0, QCustomTableWidgetItem(f"{z:.6f}"))
        self.tableWidget_Z_Dists.setItem(row_count, 1, QCustomTableWidgetItem(f"{h_dist:.6f}"))
        self.tableWidget_Z_Dists.setItem(row_count, 2, QCustomTableWidgetItem(f"{v_dist:.6f}"))

    def add_records(self, z_dists: list):
        for z, h_dist, v_dist in z_dists:
            self.add_record(z, h_dist, v_dist)

    def copy_all(self, e):
        self.tableWidget_Z_Dists.selectAll()
        selected = self.tableWidget_Z_Dists.selectedRanges()
        s = ""

        for r in range(selected[0].topRow(), selected[0].bottomRow() + 1):
            for c in range(selected[0].leftColumn(), selected[0].rightColumn() + 1):
                try:
                    s += str(self.tableWidget_Z_Dists.item(r, c).text()) + "\t"
                except AttributeError:
                    s += "\t"
            s = s[:-1] + "\n"  # eliminate last '\t'
        self.clip.setText(s)

    def show(self):
        self.window.show()

    def close(self):
        self.window.hide()

    def clear(self):
        self.tableWidget_Z_Dists.setRowCount(0)
        self.tableWidget_Z_Dists.setHorizontalHeaderLabels(("Z", "H Dist", "V Dist"))
        self.tableWidget_Z_Dists.horizontalHeader().sortIndicatorOrder()

