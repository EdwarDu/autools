#!/usr/bin/env python3

import serial
import serial.tools.list_ports
import numpy as np
from threading import Lock
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QDoubleValidator
from .fl266_config_ui import Ui_FL266_Config_Window

import traceback
import logging
from PyQt5.QtCore import QObject, pyqtSignal


_SPLIT_LOG = False

if _SPLIT_LOG:
    fl266_logger = logging.getLogger("fl266")
    fl266_logger.setLevel(logging.DEBUG)
    fl266_fh = logging.FileHandler("fl266.log")
    fl266_formatter = logging.Formatter('%(asctime)s [%(component)s] - %(levelname)s - %(message)s')
    fl266_fh.setFormatter(fl266_formatter)
    fl266_logger.addHandler(fl266_fh)

    fl266_ch = logging.StreamHandler()
    fl266_ch.setFormatter(fl266_formatter)
    fl266_logger.addHandler(fl266_ch)
else:
    fl266_logger = logging.getLogger("autools_setup_main")


class FL266Man(QObject):
    """
    """
    opened = pyqtSignal()
    closed = pyqtSignal()
    power_changed = pyqtSignal(int, name='powerChanged')
    frequency_changed = pyqtSignal(int, name='frequencyChanged')
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

    CMD_SET=0x01
    CMD_GET=0x00

    def send_cmd(self, cmd: bytes or bytearray, cmd_type: int):
        if cmd_type not in (FL266Man.CMD_SET, FL266Man.CMD_GET):
            raise ValueError(f"Unknown command type: {cmd_type}")
        fl266_logger.debug(f"Sending command: {'GET' if cmd_type == FL266Man.CMD_GET else 'SET'}: {cmd}", extra={"component": "FL266"})
        with self.ser_lock:
            self.ser.write(cmd)
            if cmd_type == FL266Man.CMD_GET:
                ans = self.ser.read(10)
            else:
                ans = self.ser.read(9)

            return ans

    @staticmethod
    def fill_cmd_checksum(cmd: bytes or bytearray):
        if type(cmd) is bytes:
            cmd = bytearray(cmd)
        ck = sum(cmd)
        return ck&0xFF
 
    @staticmethod
    def compose_cmd(ch: int, cmd_type: int, data: bytes):
        if cmd_type not in (FL266Man.CMD_SET, FL266Man.CMD_GET):
            raise ValueError(f"Unknown command type: {cmd_type}")
        cmd_pre = b'\x53\x0a'+(ch&0xFF).to_bytes(1, byteorder='big') + (cmd_type&0xFF).to_bytes(1, byteorder='big') + data[0:4]
        cmd = cmd_pre + FL266Man.fill_cmd_checksum(cmd_pre).to_bytes(1, byteorder='big') + b'\x0d'
        return cmd

    @staticmethod
    def check_response(res: bytes or bytearray, ch: int, cmd_type: int): 
        if cmd_type not in (FL266Man.CMD_SET, FL266Man.CMD_GET):
            raise ValueError(f"Unknown command type: {cmd_type}")
        if (cmd_type == FL266Man.CMD_GET and len(res) != 9) or \
            (cmd_type == FL266Man.CMD_SET and len(res) != 10):
            return False, f"wrong response length: {len(res)}"
        if type(res) is bytes:
            res = bytearray(res)
        # check header
        if (cmd_type == FL266Man.CMD_SET and res[0:2] != b'\x41\x09') or \
                (cmd_type == FL266Man.CMD_GET and res[0:2] != b'\x53\x0a'):
            return False, f"wrong response header: {res[0:2]}"
        # check ch
        if res[2] != ch & 0xFF:
            return False, f"wrong response CH: {res[2]}"
        if res[3] != cmd_type:
            return False, f"wrong response CMD: {res[3]}"

        if cmd_type == FL266Man.CMD_SET:
            if res[4:7] == b'\x4f\x4b\x21':
                pass
            elif res[4:7] == b'\x45\x52\x52':
                return False, f"ERROR response"
            else:
                return False, f"UNKNOWN response"

            if res[7] != FL266Man.fill_cmd_checksum(res[:7]):
                return False, f"wrong response CHKSUM: {res[7]}"
            if res[8] != b'\x0d':
                return False, f"wrong response tail: {res[8]}"
            return True, ""
        else:
            if res[8] != FL266Man.fill_cmd_checksum(res[:8]):
                return False, f"wrong response CHKSUM: {res[8]}"
            if res[9] != b'\x0d':
                return False, f"wrong response tail: {res[8]}"
            return True, res[4:8]

    def set_power_perc(self, perc: int):
        if perc < 0:
            perc = 0
        elif perc > 100:
            perc = 100
        cmd = FL266Man.compose_cmd(0x01, FL266Man.CMD_SET, perc)
        ack = self.send_cmd(cmd, FL266Man.CMD_SET)
        ok, msg = FL266Man.check_response(ack, 0x01, FL266Man.CMD_SET)
        if not ok:
            fl266_logger.error(f"Failed to set power {perc}: {msg}", extra={"component": "FL266"})
        else:
            fl266_logger.debug(f"Set power {perc} OK", extra={"component": "FL266"})
            self.power_changed.emit(perc)

    def set_frequency(self, freq: int):
        # 100kHz (0064) - 1Mhz
        # FIXME: Missing the part for freq -> payload
        cmd = FL266Man.compose_cmd(0x0e, FL266Man.CMD_SET, freq)
        ack = self.send_cmd(cmd, FL266Man.CMD_SET)
        ok, msg = FL266Man.check_response(ack, 0x0e, FL266Man.CMD_SET)
        if not ok:
            fl266_logger.error(f"Failed to set frequency {freq}: {msg}", extra={"component": "FL266"})
        else:
            fl266_logger.debug(f"Set frequency with {freq} OK", extra={"component": "FL266"})
            self.frequency_changed.emit(freq)

    def turn_on_off(self, on_off: bool):
        cmd = FL266Man.compose_cmd(0x00, FL266Man.CMD_SET, b'\x00\x00\x00\x01' if on_off else b'\x00\x00\x00\x00')
        ack = self.send_cmd(cmd, FL266Man.CMD_SET)
        ok, msg = FL266Man.check_response(ack, 0x00, FL266Man.CMD_SET)
        if not ok:
            fl266_logger.error(f"Failed to turn laser {'on' if on_off else 'off'}: {msg}", extra={"component": "FL266"})
        else:
            fl266_logger.debug(f"Turn laser {'on' if on_off else 'off'} OK", extra={"component": "FL266"})
            self.laser_state_changed.emit(on_off)

    def show_config_window(self):
        if self.config_window is None:
            self.config_window = FL266ConfigWindow(self)

        self.config_window.show()


# noinspection PyPep8Naming
def get_available_COMs():
    com_port_list = serial.tools.list_ports.comports()
    return {com.device: f'{com.manufacturer} {com.description}' for com in com_port_list}


class FL266ConfigWindow(Ui_FL266_Config_Window):
    def __init__(self, fl266man: FL266Man):
        self.fl266man = fl266man
        self.window = QWidget()
        Ui_FL266_Config_Window.__init__(self)
        self.setupUi(self.window)

        self.pushButton_COM_Refresh.clicked.connect(self.refresh_comlist)
        self.pushButton_COM_Open.clicked.connect(self.open_conn_clicked)

        self.comboBox_COM_BaudRate.currentTextChanged.connect(self.baudrate_changed)
        self.comboBox_COM_Parity.currentTextChanged.connect(self.parity_changed)
        self.comboBox_COM.currentIndexChanged.connect(self.com_changed)

        self.refresh_comlist()

        self.checkBox_LaserON.clicked.connect(self.laser_onoff_clicked)
        self.pushButton_SetPowerPerc.clicked.connect(
            lambda: self.fl266man.set_power_perc(self.spinBox_PowerPerc.value()))
        self.pushButton_SetFrequency.clicked.connect(
            lambda: self.fl266man.set_frequency(self.spinBox_Frequency.value()))

    def laser_onoff_clicked(self):
        if self.checkBox_LaserON.isChecked():
            self.fl266man.turn_on_off(True)
            self.pushButton_SetPowerPerc.setEnabled(True)
        else:
            self.fl266man.turn_on_off(False)
            self.pushButton_SetPowerPerc.setEnabled(False)

    def refresh_comlist(self):
        self.comboBox_COM.clear()
        com_dict = get_available_COMs()
        for com_dev in com_dict.keys():
            self.comboBox_COM.addItem(com_dev + ':' + com_dict[com_dev], com_dev)

    def com_changed(self):
        self.fl266man.com_dev = self.comboBox_COM.currentData()

    def parity_changed(self, p: str):
        if p == 'None':
            self.fl266man.ser_parity = serial.PARITY_NONE
        elif p == 'ODD':
            self.fl266man.ser_parity = serial.PARITY_ODD
        elif p == 'EVEN':
            self.fl266man.ser_parity = serial.PARITY_EVEN
        else:
            raise ValueError(f"Unknown parity {p}")

    def baudrate_changed(self, b: int or str):
        if type(b) is str:
            b = int(b)
        self.fl266man.ser_baudrate = b

    def open_conn_clicked(self, state):
        if not state:  # post event state
            self.close_conn()
        else:
            self.open_conn()

    def open_conn(self):
        try:
            self.fl266man.open()
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
            fl266_logger.info(f"FL266 COM connection opened", extra={"component": "FL266"})

            fl266_logger.debug(f"FL266 COM: {self.fl266man.com_dev} "
                              f"B:{self.fl266man.ser_baudrate} "
                              f"P:{self.fl266man.ser_parity} "
                              f"S:{self.fl266man.ser_stopbits}", extra={"component": "FL266"})
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            fl266_logger.error(f"Failed to open FL266 COM connection", extra={"component": "FL266"})
            self.close_conn()

    def close_conn(self):
        self.fl266man.close()
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
        self.fl266man.turn_on_off(False)
        fl266_logger.info(f"FL266 COM connection closed", extra={"component": "FL266"})

    def show(self):
        self.window.show()

    def close(self):
        self.window.hide()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])
    fl266man = FL266Man()
    fl266man.show_config_window()
    app.exec_()

