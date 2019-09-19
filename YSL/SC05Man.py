#!/usr/bin/env python3

import serial
import serial.tools.list_ports
import numpy as np
from threading import Lock
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QDoubleValidator
from .sc05_config_ui import Ui_SC05_Config_Window

import traceback
import logging
from PyQt5.QtCore import QObject, pyqtSignal


_SPLIT_LOG = False

if _SPLIT_LOG:
    sc05_logger = logging.getLogger("sc05")
    sc05_logger.setLevel(logging.DEBUG)
    sc05_fh = logging.FileHandler("sc05.log")
    sc05_formatter = logging.Formatter('%(asctime)s [%(component)s] - %(levelname)s - %(message)s')
    sc05_fh.setFormatter(sc05_formatter)
    sc05_logger.addHandler(sc05_fh)

    sc05_ch = logging.StreamHandler()
    sc05_ch.setFormatter(sc05_formatter)
    sc05_logger.addHandler(sc05_ch)
else:
    sc05_logger = logging.getLogger("autools_setup_main")


class SC05Man(QObject):
    """

    """

    opened = pyqtSignal()
    closed = pyqtSignal()
    power_changed = pyqtSignal(int, name='powerChanged')
    laser_state_changed = pyqtSignal(bool, name="laserStateChanged")

    def __init__(self,
                 serial_name=None,
                 baudrate=9600,
                 parity=serial.PARITY_NONE,
                 stopbits=serial.STOPBITS_ONE,
                 uart_lock=None):
        super().__init__()
        self.com_dev = serial_name
        self.ser_baudrate = baudrate
        self.ser_parity = parity
        self.ser_stopbits = stopbits

        if self.com_dev is None:
            self.ser = None
        else:
            self.ser = serial.Serial(port=serial_name,
                                     baudrate=baudrate,
                                     bytesize=serial.EIGHTBITS,
                                     parity=parity,
                                     stopbits=stopbits)
            self.ser.inter_byte_timeout = 0.1  # when device failed to send next byte within 0.1 read will exit
            if not self.ser.is_open:
                raise IOError(f"Failed to open the device {self.com_dev}")

        if uart_lock is None:
            self.ser_lock = Lock()
        else:
            self.ser_lock = uart_lock

        self.config_window = None

    def open(self):
        if self.ser is not None and self.ser.is_open:
            self.ser.close()

        self.ser = serial.Serial(port=self.com_dev, baudrate=self.ser_baudrate, bytesize=serial.EIGHTBITS,
                                 parity=self.ser_parity, stopbits=self.ser_stopbits)

        self.ser.inter_byte_timeout = 0.1

        if not self.ser.is_open:
            raise IOError(f"Failed to open the device {self.com_dev}")
        else:
            self.opened.emit()

    def close(self):
        if self.ser is not None and self.ser.is_open:
            self.ser.close()
        self.closed.emit()
        self.ser = None

    def is_open(self):
        return self.ser is not None and self.ser.is_open

    def send_cmd(self, cmd: bytes or bytearray):
        with self.ser_lock:
            self.ser.write(cmd)
            ans = self.ser.read(len(cmd))
            return ans

    @staticmethod
    def fill_cmd_checksum(cmd: bytes or bytearray):
        if len(cmd) != 8:
            return None
        if type(cmd) is bytes:
            cmd = bytearray(cmd)

        ck = cmd[0] ^ 1
        for i in range(1, 8):
            if i != 6:
                ck = ck ^ cmd[i]

        cmd[6] = ck
        return cmd

    def set_power_perc(self, perc: int):
        cmd = bytearray(b'\x55\xaa\x01\x08\x01\x00\x00\x0d')
        if perc < 0:
            perc = 0
        elif perc > 100:
            perc = 100

        cmd[5] = perc
        cmd = SC05Man.fill_cmd_checksum(cmd)
        exp_ack = cmd[:]
        exp_ack[0] = 0xaa
        exp_ack[1] = 0x55
        ack = self.send_cmd(cmd)
        if ack != exp_ack:
            sc05_logger.error(f"Wrong ack from device {ack} when setting power {perc}", extra={"component": "SC05"})
        else:
            self.power_changed.emit(perc)

    def turn_on_off(self, on_off: bool):
        on_cmd = b'\x55\xaa\x01\x02\x01\x0b\xf1\x0d'
        on_ack = b'\xaa\x55\x01\x02\x01\x0b\xf1\x0d'
        off_cmd = b'\x55\xaa\x01\x02\x01\xb0\x4c\x0d'
        off_ack = b'\xaa\x55\x01\x02\x01\xb0\x4c\x0d'

        ack = self.send_cmd(on_cmd if on_off else off_cmd)
        if ack != (on_ack if on_off else off_ack):
            sc05_logger.error(f"Wrong ack from device {ack} when turn laser {'ON' if on_off else 'OFF'}",
                             extra={"component": "SC05"})
        else:
            self.laser_state_changed.emit(on_off)

    def err_check(self):
        check_cmd = b'\x55\xaa\x01\x05\x01\x01\xf8\x0d'
        ack = self.send_cmd(check_cmd)
        if ack == b'\xaa\x55\x01\x0b\x01\x00\x53\x0d':
            return None
        elif ack == b'\xaa\x55\x01\x0b\x01\x01\xf2\x0d':
            return 1
        elif ack == b'\xaa\x55\x01\x0b\x01\x02\xf1\x0d':
            return 2
        elif ack == b'\xaa\x55\x01\x0b\x01\x03\xf0\x0d':
            return 3
        elif ack == b'\xaa\x55\x01\x0b\x01\x04\xef\x0d':
            return 4
        elif ack == b'\xaa\x55\x01\x0b\x01\x05\xee\x0d':
            return 5
        elif ack == b'\xaa\x55\x01\x0b\x01\x06\xed\x0d':
            return 6
        elif ack == b'\xaa\x55\x01\x0b\x01\x07\xec\x0d':
            return 7
        elif ack == b'\xaa\x55\x01\x0b\x01\x08\xeb\x0d':
            return 8
        elif ack == b'\xaa\x55\x01\x0b\x01\x09\xea\x0d':
            return 9
        elif ack == b'\xaa\x55\x01\x0b\x01\x0a\xe9\x0d':
            return 10
        else:
            sc05_logger.error(f"Wrong ack from device {ack} when checking error",
                              extra={"component": "SC5"})

    def show_config_window(self):
        if self.config_window is None:
            self.config_window = SC05ConfigWindow(self)

        self.config_window.show()


# noinspection PyPep8Naming
def get_available_COMs():
    com_port_list = serial.tools.list_ports.comports()
    return {com.device: f'{com.manufacturer} {com.description}' for com in com_port_list}


class SC05ConfigWindow(Ui_SC05_Config_Window):
    def __init__(self, sc05man: SC05Man):
        self.sc05man = sc05man
        self.window = QWidget()
        Ui_SC05_Config_Window.__init__(self)
        self.setupUi(self.window)

        self.pushButton_COM_Refresh.clicked.connect(self.refresh_comlist)
        self.pushButton_COM_Open.clicked.connect(self.open_conn_clicked)

        self.comboBox_COM_BaudRate.currentTextChanged.connect(self.baudrate_changed)
        self.comboBox_COM_Parity.currentTextChanged.connect(self.parity_changed)
        self.comboBox_COM.currentIndexChanged.connect(self.com_changed)

        self.refresh_comlist()

        self.checkBox_LaserON.clicked.connect(self.laser_onoff_clicked)
        self.pushButton_SetPowerPerc.clicked.connect(
            lambda: self.sc05man.set_power_perc(self.spinBox_PowerPerc.value()))
        self.pushButton_CheckError.clicked.connect(
            lambda: self.lineEdit_Error.setText(f"Error {self.sc05man.err_check()}"))

    def laser_onoff_clicked(self):
        if self.checkBox_LaserON.isChecked():
            self.sc05man.turn_on_off(True)
            self.pushButton_SetPowerPerc.setEnabled(True)
        else:
            self.sc05man.turn_on_off(False)
            self.pushButton_SetPowerPerc.setEnabled(False)

    def refresh_comlist(self):
        self.comboBox_COM.clear()
        com_dict = get_available_COMs()
        for com_dev in com_dict.keys():
            self.comboBox_COM.addItem(com_dev + ':' + com_dict[com_dev], com_dev)

    def com_changed(self):
        self.sc05man.com_dev = self.comboBox_COM.currentData()

    def parity_changed(self, p: str):
        if p == 'None':
            self.sc05man.ser_parity = serial.PARITY_NONE
        elif p == 'ODD':
            self.sc05man.ser_parity = serial.PARITY_ODD
        elif p == 'EVEN':
            self.sc05man.ser_parity = serial.PARITY_EVEN
        else:
            raise ValueError(f"Unknown parity {p}")

    def baudrate_changed(self, b: int or str):
        if type(b) is str:
            b = int(b)
        self.sc05man.ser_baudrate = b

    def open_conn_clicked(self, state):
        if not state:  # post event state
            self.close_conn()
        else:
            self.open_conn()

    def open_conn(self):
        try:
            self.sc05man.open()
            self.pushButton_COM_Open.setText("Close")
            self.pushButton_COM_Open.setChecked(True)
            # Disable the COM configuration input
            self.comboBox_COM.setDisabled(True)
            self.comboBox_COM_BaudRate.setDisabled(True)
            self.comboBox_COM_Parity.setDisabled(True)
            self.pushButton_COM_Refresh.setDisabled(True)
            # Enable the settings input
            self.groupBox_Settings.setDisabled(False)
            self.pushButton_SetPowerPerc.setDisabled(True)
            self.label_COM_Status.setStyleSheet("background: green")
            sc05_logger.info(f"SC05 COM connection opened", extra={"component": "SC05"})

            sc05_logger.debug(f"SC05 COM: {self.sc05man.com_dev} "
                              f"B:{self.sc05man.ser_baudrate} "
                              f"P:{self.sc05man.ser_parity} "
                              f"S:{self.sc05man.ser_stopbits}", extra={"component": "SC05"})
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            sc05_logger.error(f"Failed to open SC05 COM connection", extra={"component": "SC05"})
            self.close_conn()

    def close_conn(self):
        self.sc05man.close()
        self.pushButton_COM_Open.setText("Open")
        self.pushButton_COM_Open.setChecked(False)
        # Enable the COM configuration input
        self.comboBox_COM.setDisabled(False)
        self.comboBox_COM_BaudRate.setDisabled(False)
        self.comboBox_COM_Parity.setDisabled(False)
        self.pushButton_COM_Refresh.setDisabled(False)
        # Disable the settings input
        self.groupBox_Settings.setDisabled(True)
        self.label_COM_Status.setStyleSheet("background: red")
        self.sc05man.turn_on_off(False)
        sc05_logger.info(f"SC05 COM connection closed", extra={"component": "SC05"})

    def show(self):
        self.window.show()

    def close(self):
        self.window.hide()
