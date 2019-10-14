from .pcali_wlen_power_ui import Ui_PCali_WLenPowerTable
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QFileDialog
from PyQt5 import QtCore, QtGui


class PCaliWLenPowerWindow(Ui_PCali_WLenPowerTable):
    def __init__(self):
        self.window = QWidget()
        Ui_PCali_WLenPowerTable.__init__(self)
        self.setupUi(self.window)

        self.tableWidget_WLen_Power.setColumnCount(2)
        self.tableWidget_WLen_Power.setRowCount(0)
        self.tableWidget_WLen_Power.setHorizontalHeaderLabels(("Wave Length", "Power %"))
        self.pushButton_Clear.clicked.connect(self.clear)
        self.tableWidget_WLen_Power.horizontalHeader().sortIndicatorOrder()

        self.pushButton_Copy.clicked.connect(self.copy_all)
        self.pushButton_SaveCSV.clicked.connect(self.save_as_csv)

        self.clip = QtGui.QGuiApplication.clipboard()

    def add_record(self, wlen, power):
        row_count = self.tableWidget_WLen_Power.rowCount()
        self.tableWidget_WLen_Power.setRowCount(row_count + 1)
        self.tableWidget_WLen_Power.setItem(row_count, 0, QTableWidgetItem(f"{wlen:d}"))
        self.tableWidget_WLen_Power.setItem(row_count, 1, QTableWidgetItem(f"{power:.2f}"))

    def add_records(self, wlen_power: list):
        for wlen, power in wlen_power:
            self.add_record(wlen, power)

    def copy_all(self, e):
        self.tableWidget_WLen_Power.selectAll()
        selected = self.tableWidget_WLen_Power.selectedRanges()
        s = ""

        for r in range(selected[0].topRow(), selected[0].bottomRow() + 1):
            for c in range(selected[0].leftColumn(), selected[0].rightColumn() + 1):
                try:
                    s += str(self.tableWidget_WLen_Power.item(r, c).text()) + "\t"
                except AttributeError:
                    s += "\t"
            s = s[:-1] + "\n"  # eliminate last '\t'
        self.clip.setText(s)

    def show(self):
        self.window.show()

    def close(self):
        self.window.hide()

    def clear(self):
        self.tableWidget_WLen_Power.setRowCount(0)
        self.tableWidget_WLen_Power.setHorizontalHeaderLabels(("Wave Length", "Power %"))

    def save_as_csv(self):
        fname, _ = QFileDialog.getSaveFileName(self.window, "Save as CSV file ...", ".", "CSV (*.csv)")
        if fname is not None and fname != '':
            with open(fname, 'w') as f_csv:
                self.tableWidget_WLen_Power.selectAll()
                selected = self.tableWidget_WLen_Power.selectedRanges()
                last_c = selected[0].rightColumn()

                for r in range(selected[0].topRow(), selected[0].bottomRow() + 1):
                    for c in range(selected[0].leftColumn(), selected[0].rightColumn() + 1):
                        try:
                            f_csv.write(str(self.tableWidget_WLen_Power.item(r, c).text()) +
                                        ("," if c != last_c else ""))
                        except AttributeError:
                            if c != last_c:
                                f_csv.write(",")

                    f_csv.write("\n")  # eliminate last '\t'

