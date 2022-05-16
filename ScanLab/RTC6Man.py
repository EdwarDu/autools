#!/usr/bin/env python3

import serial
import serial.tools.list_ports
import pyvisa
import numpy as np
from threading import Lock
from PyQt5.QtWidgets import QWidget
from .rtc6_config_ui import Ui_RTC6_Config_Window
from PyQt5.QtGui import QDoubleValidator
import traceback
import logging
from PyQt5.QtCore import QObject, pyqtSignal

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
    axis_value_changed = pyqtSignal(int, float, name='axisValueChanged')

    _FAKE_DEV = False

    def __init__(self, visa_addr: str = None,
                 serial_name=None,
                 baudrate=9600,
                 parity=serial.PARITY_NONE,
                 stopbits=serial.STOPBITS_ONE,
                 uart_lock=None):
        super().__init__()
        
        self.quiet = False
        self.config_window = None

    def open(self):
        pass

    def close(self):
        pass

    def is_open(self):
        pass

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
            self.rtc6man.open()
            self.label_COM_Status.setStyleSheet("background: green")
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            self.close_conn()

    def close_conn(self):
        global rtc6_logger
        self.rtc6man.close()
        self.label_COM_Status.setStyleSheet("background: red")
        rtc6_logger.info(f"RTC6 COM connection closed", extra={"component": "RTC6"})

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
