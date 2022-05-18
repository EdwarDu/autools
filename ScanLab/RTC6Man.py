#!/usr/bin/env python3

import os
import numpy as np
from typing import Union
from threading import Lock
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from .rtc6_config_ui import Ui_RTC6_Config_Window
from PyQt5.QtGui import QDoubleValidator
import traceback
import logging
from PyQt5.QtCore import QObject, pyqtSignal

from pyscanlab import RTC6Helper

_SPLIT_LOG = False

if _SPLIT_LOG:
    rtc6_logger = logging.getLogger("rtc6")
    rtc6_logger.setLevel(logging.DEBUG)
    rtc6_fh = logging.FileHandler("rtc6.log")
    rtc6_formatter = logging.Formatter('%(asctime)s [%(component)s] - %(levelname)s - %(message)s')
    rtc6_fh.setFormatter(rtc6_formatter)
    rtc6_logger.addHandler(rtc6_fh)

    rtc6_ch = logging.StreamHandler()
    rtc6_ch.setFormatter(rtc6_formatter)
    rtc6_logger.addHandler(rtc6_ch)
else:
    rtc6_logger = logging.getLogger("autools_setup_main")


def float2str(value: float):
    if 1e9 <= abs(value) < 1e12:
        return f"{value:.6} G"
    elif 1e6 <= abs(value) < 1e9:
        return f"{value:.6} M"
    elif 1e3 <= abs(value) < 1e6:
        return f"{value:.6} K"
    elif 1 <= abs(value) < 1e3:
        return f"{value:.6}"
    elif 1e-3 <= abs(value) < 1:
        return f"{value*1000:.6f} m"
    elif 1e-6 <= abs(value) < 1e-3:
        return f"{value*1e6:.6f} u"
    elif 1e-9 <= abs(value) < 1e-6:
        return f"{value*1e9:.6f} n"
    else:
        return f"{value:.6G}"


class RTC6Man(QObject):
    """Helper (man) Class for communicate with RTC6"""

    opened = pyqtSignal()
    closed = pyqtSignal()
    axis_value_changed = pyqtSignal(int, int, name='axisValueChanged')

    def __init__(self, ):
        super().__init__()
        self._rtc6_helper = None
        self.config_window = None
        self._x = 0
        self._y = 0

    def open(self, cfg_path: Union[bytes, str, os.PathLike, None] = None, 
                   cor_file: Union[bytes, str, os.PathLike, None] = None):
        if self._rtc6_helper is None:
            try:
                self._rtc6_helper = RTC6Helper(True)
                self._rtc6_helper.load_program_file(cfg_path)
                self._rtc6_helper.load_correction_file(cor_file, 1, 2)  # load to table 1 for 2D
                self._rtc6_helper.reset_error() # reset all error
                self._rtc6_helper.config_list(4000, 4000) # number from example
                self._rtc6_helper.goto_xy(0, 0) # go to origin by default
                self.axis_value_changed.emit(0, 0)
                self._x = 0
                self._y = 0
                self.opened.emit()
            except Exception as e:
                traceback.print_tb(e.__traceback__)
                print(e)
                self._rtc6_helper = None

    def close(self,):
        if self._rtc6_helper is not None:
            self._rtc6_helper.free_dll() #explictly free the dll, can't rely on __dealloc__
            self._rtc6_helper = None
        self.closed.emit()

    def is_open(self,):
        return self._rtc6_helper is not None

    @property
    def x(self,):
        return self._x

    @property
    def y(self,):
        return self._y

    def goto_xy(self, x: int, y: int):
        x1 = min(max(-524288, x), 524287)
        y1 = min(max(-524288, y), 524287)
        self._x, self._y = self._rtc6_helper.goto_xy(x1, y1)
        self.axis_value_changed.emit(self._x, self._y)
        return self._x, self._y

    def step_x(self, s: int):
        return self.goto_xy(self._x + s, self._y)

    def step_y(self, s: int):
        return self.goto_xy(self._x, self._y + s)

    def step_xy(self, sx: int, sy: int):
        return self.goto_xy(self._x + sx, self._y + sy)

    def show_config_window(self):
        if self.config_window is None:
            self.config_window = RTC6ConfigWindow(self)

        self.config_window.show()

    def get_current_settings(self, with_header: bool = True):
        if self.config_window is not None:
            return self.config_window.get_current_settings(with_header)
        else:
            return ""


class RTC6ConfigWindow(Ui_RTC6_Config_Window):
    """
        RTC6 Helper class with configuration window
    """
    def __init__(self, rtc6man: RTC6Man):
        self.rtc6man = rtc6man
        self.window = QWidget()
        Ui_RTC6_Config_Window.__init__(self)
        self.setupUi(self.window)
        self.pushButton_CONN_Open.clicked.connect(self.open_conn_clicked)
        self.pushButton_StepXPlus.clicked.connect(lambda : self.step_xy_clicked(1, 0))
        self.pushButton_StepYPlus.clicked.connect(lambda : self.step_xy_clicked(0, 1))
        self.pushButton_StepXMinus.clicked.connect(lambda : self.step_xy_clicked(-1, 0))
        self.pushButton_StepYMinus.clicked.connect(lambda : self.step_xy_clicked(0, -1))
        self.pushButton_GoToOrigin.clicked.connect(lambda : self.rtc6man.goto_xy(0, 0))
        self.pushButton_GoToXY.clicked.connect(lambda : self.rtc6man.goto_xy(self.spinBox_X.value(), self.spinBox_Y.value()))
        self.pushButton_PickConfigPath.clicked.connect(self.pick_config_path)
        self.pushButton_PickCorFile.clicked.connect(self.pick_cor_file)
        self.rtc6man.axis_value_changed.connect(self.rtc6_xy_changed)

    def pick_config_path(self,):
        folder = os.path.normpath(
                QFileDialog.getExistingDirectory(
                    self.window, 'Select Folder with RTC6OUT.out, RTC6RBF.rbf and RTC6DAT.dat inside:'))
        b_clear_field = False
        if folder is not None and len(folder) != 0:
            files_to_check = ('RTC6OUT.out', 'RTC6RBF.rbf', 'RTC6DAT.dat')
            for f in files_to_check:
                file_path = os.path.join(folder, f)
                if not os.path.exists(file_path):
                    QMessageBox.critical(self.window, "Error",
                            f"{file_path} does not exists, leave the field empty to use the default one")
                    b_clear_field = True
            if b_clear_field:
                self.lineEdit_ConfigPath.setText("")

    def pick_cor_file(self, ):
        fname, _a = QFileDialog.getOpenFileName(self.window, 
                        'Select the correction file to load to table 1 for 2D', '.', 'ct5 (*.ct5) | All Files (*.*)')
        if fname is not None and len(fname) != 0 and not os.path.exists(fname):
            QMessageBox.critical(self.window, "Error",
                    f"{fname} does not exists, leave the field empty to use the default one")
            self.lineEdit_CorFile.setText("")

    def sync_current_settings(self):
        pass

    def open_conn_clicked(self, state):
        if not state:  # post event state
            self.close_conn()
        else:
            # FIXME: Actually open connection
            self.open_conn()

    def open_conn(self):
        global rtc6_logger
        try:
            self.rtc6man.open(self.lineEdit_ConfigPath.text(), self.lineEdit_CorFile.text())
            self.label_CONN_Status.setStyleSheet("background: green")
            rtc6_logger.info(f"RTC6 connection opened", extra={"component": "RTC6"})
            self.pushButton_CONN_Open.setText("Close")
            self.groupBox_Settings.setEnabled(True)
            self.lineEdit_CorFile.setEnabled(False)
            self.lineEdit_ConfigPath.setEnabled(False)
            self.pushButton_PickCorFile.setEnabled(False)
            self.pushButton_PickConfigPath.setEnabled(False)
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            print(e)
            self.close_conn()

    def close_conn(self):
        global rtc6_logger
        self.rtc6man.close()
        self.label_CONN_Status.setStyleSheet("background: red")
        rtc6_logger.info(f"RTC6 connection closed", extra={"component": "RTC6"})
        self.pushButton_CONN_Open.setText("Open")
        self.groupBox_Settings.setEnabled(False)
        self.lineEdit_CorFile.setEnabled(True)
        self.lineEdit_ConfigPath.setEnabled(True)
        self.pushButton_PickCorFile.setEnabled(True)
        self.pushButton_PickConfigPath.setEnabled(True)

    def step_xy_clicked(self, x_dir: int, y_dir: int):
        sx = self.spinBox_StepX.value() * x_dir
        sy = self.spinBox_StepY.value() * y_dir
        self.rtc6man.step_xy(sx, sy)

    def rtc6_xy_changed(self, x: int, y: int):
        self.spinBox_X.setValue(x)
        self.spinBox_Y.setValue(y)

    def show(self):
        self.window.show()

    def close(self):
        self.window.hide()

    def get_current_settings(self, with_header: bool = True):
        if self.rtc6man.is_open():
            if with_header:
                setting_str = "--------ScanLab RTC6-------\n"
            else:
                setting_str = ""
            # FIXME: PlaceHolder for possible settings
            setting_str = setting_str + f"NOTHING YET"
            return setting_str
        else:
            return ""

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])

    rtc6_man = RTC6Man()
    print(f'Starting...')
    rtc6_man.show_config_window()
    QApplication.instance().exec_()
