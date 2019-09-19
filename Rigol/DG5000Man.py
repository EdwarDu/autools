#!/usr/bin/env python3

import visa
import numpy as np
from threading import Lock
from PyQt5.QtWidgets import QWidget
from .dg5000_config_ui import Ui_DG5000_Config_Window
from PyQt5.QtGui import QDoubleValidator
import traceback
import logging
from PyQt5.QtCore import QObject, pyqtSignal

_SPLIT_LOG = False

if _SPLIT_LOG:
    dg5000_logger = logging.getLogger("dg5000")
    dg5000_logger.setLevel(logging.DEBUG)
    dg5000_fh = logging.FileHandler("dg5000.log")
    dg5000_formatter = logging.Formatter('%(asctime)s [%(component)s] - %(levelname)s - %(message)s')
    dg5000_fh.setFormatter(dg5000_formatter)
    dg5000_logger.addHandler(dg5000_fh)

    dg5000_ch = logging.StreamHandler()
    dg5000_ch.setFormatter(dg5000_formatter)
    dg5000_logger.addHandler(dg5000_ch)
else:
    dg5000_logger = logging.getLogger("autools_setup_main")


class DG5000Man(QObject):
    """Helper (man) Class for communicate with DG5000 via PyVisa"""

    opened = pyqtSignal()
    closed = pyqtSignal()

    def __init__(self, dev_addr: str = None):
        super().__init__()
        self.dev_addr = dev_addr
        self.rm = visa.ResourceManager('@py')
        if self.dev_addr is not None:
            self.dev_inst = self.rm.open_resource(self.dev_addr)
        else:
            self.dev_inst = None

        self.config_window = None

    def set_dev_addr(self, addr: str):
        self.dev_addr = addr

    def open(self):
        if self.dev_addr is None:
            raise ValueError(f"Device address must not be None")

        self.dev_inst = self.rm.open_resource(self.dev_addr)
        self.opened.emit()
        dg5000_logger.info(f"DG5000 Device opened with {self.dev_addr}", extra={"component": "DG5000"})

    def close(self):
        if self.dev_inst is not None:
            self.dev_inst.close()
            self.closed.emit()
            self.dev_inst = None
            dg5000_logger.info(f"DG5000 device closed", extra={"component": "DG5000"})

    def is_open(self):
        return self.dev_inst is not None

    def get_dev_id(self):
        return self.dev_inst.query("*IDN?")

    def show_config_window(self):
        if self.config_window is None:
            self.config_window = DG5000ConfigWindow(self)

        self.config_window.show()


class DG5000ConfigWindow(Ui_DG5000_Config_Window):
    def __init__(self, dg5000man: DG5000Man):
        Ui_DG5000_Config_Window.__init__(self)
        self.dg5000man = dg5000man
        self.window = QWidget()
        self.setupUi(self.window)

        self.refresh_resources()

        self.pushButton_Refresh.clicked.connect(self.refresh_resources)
        self.comboBox_ResourceAddr.currentTextChanged.connect(lambda t: self.dg5000man.set_dev_addr(t))
        self.pushButton_Open.clicked.connect(self.dev_open_clicked)

    def dev_open_clicked(self, state):
        if not state:  # Close
            self.dg5000man.close()
            self.groupBox_Settings.setDisabled(True)
            self.pushButton_Refresh.setEnabled(True)
            self.comboBox_ResourceAddr.setEnabled(True)
            self.pushButton_Open.setText("Open")
            self.label_CONN_Status.setStyleSheet("background: red")
        else:  # Open
            try:
                self.dg5000man.open()
                self.groupBox_Settings.setDisabled(False)
                self.pushButton_Refresh.setEnabled(False)
                self.comboBox_ResourceAddr.setEnabled(False)
                self.pushButton_Open.setText("Close")
                self.label_CONN_Status.setStyleSheet("background: green")
            except Exception as e:
                traceback.print_tb(e.__traceback__)

                dg5000_logger.error(f"Failed to open {self.dg5000man.dev_addr}", extra={"component": "DG5000"})
                self.pushButton_Open.setChecked(False)

    def refresh_resources(self):
        self.comboBox_ResourceAddr.clear()
        rs = self.dg5000man.rm.list_resources()
        for r in rs:
            self.comboBox_ResourceAddr.addItem(r)

    def show(self):
        self.window.show()

    def close(self):
        self.window.hide()


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])

    dg5000_man = DG5000Man()
    print(f'Starting...')
    dg5000_man.show_config_window()
    QApplication.instance().exec_()
