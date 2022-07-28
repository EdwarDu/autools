#!/usr/bin/env python3

import serial
import serial.tools.list_ports
import numpy as np
from threading import Lock
from PyQt5.QtWidgets import QWidget
from .ksc101_config_ui import Ui_KSC101_Config_Window
from PyQt5.QtGui import QDoubleValidator
import traceback
import logging
from PyQt5.QtCore import QObject, pyqtSignal

from .APTComm import APTComm

_SPLIT_LOG = False

if _SPLIT_LOG:
    ksc101_logger = logging.getLogger("ksc101")
    ksc101_logger.setLevel(logging.DEBUG)
    ksc101_fh = logging.FileHandler("ksc101.log")
    ksc101_formatter = logging.Formatter('%(asctime)s [%(component)s] - %(levelname)s - %(message)s')
    ksc101_fh.setFormatter(ksc101_formatter)
    ksc101_logger.addHandler(ksc101_fh)

    ksc101_ch = logging.StreamHandler()
    ksc101_ch.setFormatter(ksc101_formatter)
    ksc101_logger.addHandler(ksc101_ch)
else:
    ksc101_logger = logging.getLogger("autools_setup_main")


class KSC101Man(QObject):
    """Helper (man) Class for communicate with KSC101"""

    opened = pyqtSignal()
    closed = pyqtSignal()
    axis_value_changed = pyqtSignal(int, float, name='axisValueChanged')

    _FAKE_DEV = False

    def __init__(self,
                 serial_name=None,
                 uart_lock=None):
        super().__init__()
        self.com_dev = serial_name

        if self.com_dev is None:
            self.ser = None
        else:
            self.ser = serial.Serial(port=serial_name,
                                     baudrate=115200,
                                     bytesize=serial.EIGHTBITS,
                                     parity=serial.PARITY_NONE,
                                     stopbits=serial.STOPBITS_ONE,
                                     rtscts=True)
            self.ser.inter_byte_timeout = 0.1  # when device failed to send next byte within 0.1 read will exit
            if not self.ser.is_open:
                raise IOError(f"Failed to open the device {self.com_dev}")

        if uart_lock is None:
            self.ser_lock = Lock()
        else:
            self.ser_lock = uart_lock

        self.quiet = False
        self.config_window = None

    def open(self):
        if self.ser is not None and self.ser.is_open:
            self.ser.close()

        self.ser = serial.Serial(port=self.com_dev, baudrate=115200, bytesize=serial.EIGHTBITS,
                                 parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, rtscts=True)

        self.ser.inter_byte_timeout = 0.1

        if not self.ser.is_open:
            raise IOError(f"Failed to open the device {self.com_dev}")
        else:
            self.com_end = '\r'
            self.opened.emit()

    def close(self):
        if self.ser is not None and self.ser.is_open:
            self.ser.close()
        self.closed.emit()
        self.ser = None

    def is_open(self):
        return self.ser is not None and self.ser.is_open

    def send_msg(self, msg: bytes | bytearray):
        global ksc101_logger

        ksc101_logger.debug(f"Sending bytes <{msg}>", extra={"component": "KSC101"})

        with self.ser_lock:
            self.ser.write(msg)

    def get_resp(self,):
        resp = None
        with self.ser_lock:
            ans = self.ser.read(6)
            if ans[4] & 0x80 != 0:
                # has data packets
                data_packet_len = int.from_bytes(ans[2:4], byteorder='little', signed=False)
                resp = ans + self.ser.read(data_packet_len)
            else:
                resp = ans
        ksc101_logger.debug(f"Got resp: <resp>", extra={"component": "KSC101"})
        return resp

    def get_sol_state(self,):
        self.send_msg(APTComm.req_sol_state(1))
        _, state = APTComm.get_sol_state(self.get_resp())
        return state

    def set_sol_state(self, on_off: bool):
        self.send_msg(APTComm.set_sol_state(1, on_off))

    def show_config_window(self):
        if self.config_window is None:
            self.config_window = KSC101ConfigWindow(self)

        self.config_window.show()

    def get_current_settings(self, with_header: bool = True):
        if self.config_window is not None:
            return self.config_window.get_current_settings(with_header)
        else:
            return ""


def ask_selection(choices, prompt_str: str = 'Select: ', allow_invalid=False):
    choice = None
    while choice is None:
        for i in range(0, len(choices)):
            print(f'[{i: 3d}] : {choices[i]}')
        try:
            choice = int(input(prompt_str))
            if 0 <= choice < len(choices):
                return choice
            raise ValueError("Invalid")
        except Exception as e:
            if allow_invalid:
                return None
            print('Invalid, again!')
            choice = None
            continue


def ask_com_port():
    while True:
        com_port_list = serial.tools.list_ports.comports()
        menu = [f'{com.device} {com.manufacturer} {com.description}' for com in com_port_list]
        menu.append('[REFRESH LIST]')
        c = ask_selection(menu, 'Which COM to use? ')
        if c != len(menu) - 1:
            return com_port_list[c].device


# noinspection PyPep8Naming
def get_available_COMs():
    com_port_list = serial.tools.list_ports.comports()
    return {com.device: f'{com.manufacturer} {com.description}' for com in com_port_list}


class KSC101ConfigWindow(Ui_KSC101_Config_Window):
    """
        KSC101 Helper class with configuration window
    """
    def __init__(self, ksc101man: KSC101Man):
        self.ksc101man = ksc101man
        self.window = QWidget()
        Ui_KSC101_Config_Window.__init__(self)
        self.setupUi(self.window)

        self.pushButton_COM_Refresh.clicked.connect(self.refresh_comlist)
        self.pushButton_COM_Open.clicked.connect(self.open_conn_clicked)

        self.comboBox_CONN.currentIndexChanged.connect(self.conn_changed)

        # Force to change
        self.conn_changed(self.comboBox_CONN.currentData())

        self.refresh_comlist()

        # KSC101 Settings
        self.pushButton_SOLOnOff.clicked.connect(self.sol_onff_clicked)

    def sync_current_settings(self):
        if self.ksc101man is not None:
            pass

    def conn_changed(self, i: int):
        self.ksc101man.com_dev = self.comboBox_CONN.currentData()

    def refresh_comlist(self):
        self.comboBox_CONN.clear()
        com_dict = get_available_COMs()
        for com_dev in com_dict.keys():
            self.comboBox_CONN.addItem(com_dev + ':' + com_dict[com_dev], com_dev)

    def open_conn_clicked(self, state):
        if not state:  # post event state
            self.close_conn()
        else:
            # FIXME: Actually open connection
            self.open_conn()

    def open_conn(self):
        global ksc101_logger
        try:
            self.ksc101man.open()
            self.pushButton_COM_Open.setText("Close")
            self.pushButton_COM_Open.setChecked(True)
            # Disable the COM configuration input
            self.comboBox_CONN.setDisabled(True)
            self.pushButton_COM_Refresh.setDisabled(True)
            # Enable the settings input
            self.groupBox_Settings.setDisabled(False)
            self.label_COM_Status.setStyleSheet("background: green")

            # update current settings
            self.sync_current_settings()
            ksc101_logger.info(f"KSC101 COM connection opened", extra={"component": "KSC101"})
            ksc101_logger.debug(f"KSC101 COM: {self.ksc101man.com_dev} ",extra={"component": "KSC101"})
            self._update_ui(sol_onoff = self.ksc101man.get_sol_state())
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            ksc101_logger.error(f"Failed to open KSC101 COM connection", extra={"component": "KSC101"})
            self.close_conn()

    def close_conn(self):
        global ksc101_logger
        self.ksc101man.close()
        # FIXME: stop all the KSC101 update activities
        self.pushButton_COM_Open.setText("Open")
        self.pushButton_COM_Open.setChecked(False)
        # Enable the COM configuration input
        self.comboBox_CONN.setDisabled(False)
        self.pushButton_COM_Refresh.setDisabled(False)
        # Disable the settings input
        self.groupBox_Settings.setDisabled(True)
        self.label_COM_Status.setStyleSheet("background: red")
        ksc101_logger.info(f"KSC101 COM connection closed", extra={"component": "KSC101"})

    def sol_onff_clicked(self, state):
        if not state:
            self.ksc101man.set_sol_state(False)
        else:
            self.ksc101man.set_sol_state(True)
        self._update_ui(sol_onoff = self.ksc101man.get_sol_state())

    def _update_ui(self, sol_onoff: bool | None = None):
        if sol_onoff is not None:
            if sol_onoff:
                self.pushButton_SOLOnOff.setText("ON")
                self.pushButton_SOLOnOff.setStyleSheet("background: green")
            else:
                self.pushButton_SOLOnOff.setText("OFF")
                self.pushButton_SOLOnOff.setStyleSheet("background: red")

    def show(self):
        self.window.show()

    def close(self):
        self.window.hide()

    def get_current_settings(self, with_header: bool = True):
        if self.ksc101man.is_open():
            if with_header:
                setting_str = "--------ThorLabs KSC101-------\n"
            else:
                setting_str = ""
            return setting_str
        else:
            return ""

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])

    ksc101_man = KSC101Man()
    print(f'Starting...')
    ksc101_man.show_config_window()
    QApplication.instance().exec_()

