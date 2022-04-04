#!/usr/bin/env python3

import serial
import serial.tools.list_ports
import io
import pyvisa
import numpy as np
from typing import Union
from threading import Lock
from PyQt5.QtWidgets import QWidget
from .proscan3_config_ui import Ui_ProScan3_Config_Window
from PyQt5.QtGui import QDoubleValidator
import traceback
import logging
from PyQt5.QtCore import QObject, pyqtSignal

_SPLIT_LOG = False

if _SPLIT_LOG:
    ProScan3_logger = logging.getLogger("ProScan3")
    ProScan3_logger.setLevel(logging.DEBUG)
    ProScan3_fh = logging.FileHandler("ProScan3.log")
    ProScan3_formatter = logging.Formatter('%(asctime)s [%(component)s] - %(levelname)s - %(message)s')
    ProScan3_fh.setFormatter(ProScan3_formatter)
    ProScan3_logger.addHandler(ProScan3_fh)

    ProScan3_ch = logging.StreamHandler()
    ProScan3_ch.setFormatter(ProScan3_formatter)
    ProScan3_logger.addHandler(ProScan3_ch)
else:
    ProScan3_logger = logging.getLogger("autools_setup_main")


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


class ProScan3Man(QObject):
    """Helper (man) Class for communicate with ProScan3"""

    opened = pyqtSignal()
    closed = pyqtSignal()
    axis_value_changed = pyqtSignal(int, float, name='axisValueChanged')

    AXIS_ID = { "X": 1, "Y": 2, "Z": 3, "A": 4, "F3": 4, "F1": 5, "F2": 6, "F4": 7, "F5": 8, "F6": 9 }

    _FAKE_DEV = False

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
            self.sio = None
        else:
            self.open()

        if uart_lock is None:
            self.ser_lock = Lock()
        else:
            self.ser_lock = uart_lock

        self.quiet = False
        self.config_window = None

    def open(self):
        self.close()

        self.ser = serial.Serial(port=self.com_dev, baudrate=self.ser_baudrate, bytesize=serial.EIGHTBITS,
                                 parity=self.ser_parity, stopbits=self.ser_stopbits, timeout=10)

        self.ser.inter_byte_timeout = 0.1

        if not self.ser.is_open:
            raise IOError(f"Failed to open the device {self.com_dev}")
        self.sio = io.TextIOWrapper(io.BufferedRWPair(self.ser, self.ser), newline="\r", encoding="ascii")
        self.opened.emit()

    def close(self):
        if self.ser is not None and self.ser.is_open:
            if self.ser is not None:
                self.sio.close()
            self.ser.close()
            self.closed.emit()
        self.ser = None
        self.sio = None

    def is_open(self):
        return self.ser is not None and self.ser.is_open

    WAIT_FOR_1LINE=1
    WAIT_FOR_END=2
    def send_cmd(self, cmd: str, wait_for: int, *args):
        global ProScan3_logger
        cmd_str = cmd + " " + ','.join([str(arg) for arg in args if arg is not None]) + "\r"

        cmd_str_replaced = cmd_str.replace("\r", "\\r")
        ProScan3_logger.debug(f"Sending command <{cmd_str_replaced}>", extra={"component": "ProScan3"})

        with self.ser_lock:
            self.sio.write(cmd_str)
            self.sio.flush()
            if wait_for == ProScan3man.WAIT_FOR_1LINE:
                res = sio.readline()
            elif wait_for == ProScan3man.WAIT_FOR_END:
                res = ""
                while True:
                    l = sio.readline()
                    res += l
                    if l == "END\r":
                        break
            else:
                raise ValueError(f"Donot know what to wait {wait_for}")

            ans_replaced = res.replace("\r", "\\r")
            ProScan3_logger.debug(f"Got answer: <{ans_replaced}>", extra={"component": "ProScan3"})
            return res.strip()

    def show_config_window(self):
        if self.config_window is None:
            self.config_window = ProScan3ConfigWindow(self)

        self.config_window.show()

    def get_current_settings(self, with_header: bool = True):
        if self.config_window is not None:
            return self.config_window.get_current_settings(with_header)
        else:
            return ""

    def get_peripherals_info(self):
        return self.send_cmd("?", ProScan3man.WAIT_FOR_END)

    def check_limit_switch(self):
        ans = self.send_cmd("=", ProScan3man.WAIT_FOR_1LINE)
        ans_byte = int(ans) & 0xFF
        res = {
                "-A": ans_byte & 0x80 != 0,
                "+A": ans_byte & 0x40 != 0,
                "-Z": ans_byte & 0x20 != 0,
                "+Z": ans_byte & 0x10 != 0,
                "-Y": ans_byte & 0x08 != 0,
                "+Y": ans_byte & 0x04 != 0,
                "-X": ans_byte & 0x02 != 0,
                "+X": ans_byte & 0x01 != 0
              }
        return res

    def get_axis_motion_status(self, axis: str | None):
        allowed_axis = ("X", "Y", "S", "Z", "A", "F", "F1", "F2")
        if axis is not None and axis not in allowed_axis:
            ProScan3_logger.error(f"Invalid axis: <{axis}>", extra={"component": "ProScan3"})
            raise ValueError(f"{axis} is not allowed as parameter for $, only {allowed_axis}")
        else:
            ans = self.send_cmd("$", ProScan3man.WAIT_FOR_1LINE, axis)
            ans_byte = int(ans) & 0x3F
            if axis is None:
                res = {
                        "F2": ans_byte & 0x20 != 0,
                        "F1": ans_byte & 0x10 != 0,
                        "A": ans_byte & 0x08 != 0,
                        "Z": ans_byte & 0x04 != 0,
                        "Y": ans_byte & 0x02 != 0,
                        "X": ans_byte & 0x01 != 0,
                       }
                return res
            elif axis == "S":
                res = {
                        "Y": ans_byte & 0x02 != 0,
                        "X": ans_byte & 0x01 != 0,
                      }
                return res
            elif axis == "F":
                res = {
                        "F2": ans_byte & 0x02 != 0,
                        "F1": ans_byte & 0x01 != 0,
                      }
                return res
            else:
                res = { axis : ans_byte & 0x01 != 0 }
                return res

    def change_baudrate(self, baudrate: int):
        # FIXME: This is tricky to handle, need to test
        allowed_baudrate_dict = {9600: 96, 19200: 19, 38400: 38, 115400: 115}
        if baudrate not in allowed_baudrate_dict.keys():
            ProScan3_logger.error(f"Invalid baudrate: <{baudrate}>", extra={"component": "ProScan3"})
            raise ValueError(f"{baudrate} is not allowed as parameter for BAUD, only {allowed_baudrate_dict.keys()}")
        else:
            try:
                ans = self.send_cmd("BAUD", ProScan3man.WAIT_FOR_1LINE, allowed_baudrate_dict[baudrate])
            except Exception as e:
                ProScan3_logger.warning(f"Exception when try to set baudrate to {baudrate}: <{e}>", extra={"component": "ProScan3"})
            finally:
                self.ser_baudrate = baudrate
                self.close()
                self.open()

    def get_command_mode(self):
        return self.send_cmd("COMP", ProScan3man.WAIT_FOR_1LINE)

    def set_command_mode(self, b_compatibility: bool):
        return self.send_cmd("COMP", ProScan3man.WAIT_FOR_1LINE, 1 if b_compatibility else 0)

    #def get_instrument_info(self):
    #    return self.send_cmd("DATE", ????)

    def set_error_code_mode(self, b_human_readable: bool):
        return self.send_cmd("ERROR", ProScan3man.WAIT_FOR_1LINE, 1 if b_human_readable else 0)

    def stop_movement(self):
        return self.send_cmd("I", ProScan3man.WAIT_FOR_1LINE)

    def kill_movement(self):
        return self.send_cmd("K", ProScan3man.WAIT_FOR_1LINE)

    def macro_start_stop(self):
        return self.send_cmd("MACRO", ProScan3man.WAIT_FOR_1LINE)

    def get_serial_num(self):
        return self.send_cmd("SERIAL", ProScan3man.WAIT_FOR_1LINE)

    def get_limit_switch_status(self):
        ans = self.send_cmd("LMT", ProScan3man.WAIT_FOR_1LINE)
        ans_byte = int(ans)&0xFF
        res = {
                "-A": ans_byte & 0x80 != 0,
                "+A": ans_byte & 0x40 != 0,
                "-Z": ans_byte & 0x20 != 0,
                "+Z": ans_byte & 0x10 != 0,
                "-Y": ans_byte & 0x08 != 0,
                "+Y": ans_byte & 0x04 != 0,
                "-X": ans_byte & 0x02 != 0,
                "+X": ans_byte & 0x01 != 0
              }
        return res

    def soak_test(self):
        return self.send_cmd("SOAK", ProScan3man.WAIT_FOR_1LINE)

    def get_software_version(self):
        return self.send_cmd("VERSION", ProScan3man.WAIT_FOR_1LINE)

    def insert_wait(self, ms: int):
        return self.send_cmd("WAIT", ProScan3man.WAIT_FOR_1LINE, ms)

    def get_stage_step_size(self,):
        ans = self.send_cmd("X", ProScan3man.WAIT_FOR_1LINE)
        u, v = re.split(r"[,\s]+", ans)
        return (u, v)

    def set_stage_step_size(self, x_step: int, y_step: int):
        return self.send_cmd("X", ProScan3man.WAIT_FOR_1LINE, x_step, y_step)

    def set_stage_backlash(self, b_for_ser_joystick: bool, bl_enable: bool, bl_value: int | None = None):
        return self.send_cmd("BLSH" if b_for_ser_joystick else "BLSJ", ProScan3man.WAIT_FOR_1LINE, 1 if bl_enable else 0, bl_value)

    def get_stage_backlash(self):
        ans = self.send_cmd("BLSH" if b_for_ser_joystick else "BLSJ", ProScan3man.WAIT_FOR_1LINE)
        return re.split(r"[,\s]+", ans)
 
    def move_back(self, steps: int | None):
        #FIXME: if steps is None then it will move v steps defined by X command ?? doc is unclear, need to test
        return self.send_cmd("B", ProScan3man.WAIT_FOR_1LINE, steps)

    def move_forward(self, steps: int | None):
        #FIXME: if steps is None then it will move v steps defined by X command ?? doc is unclear, need to test
        return self.send_cmd("F", ProScan3man.WAIT_FOR_1LINE, steps)

    def move_left(self, steps: int | None):
        #FIXME: if steps is None then it will move v steps defined by X command ?? doc is unclear, need to test
        return self.send_cmd("L", ProScan3man.WAIT_FOR_1LINE, steps)

    def move_to(self, x: int, y: int, z: int | None):
        return self.send_cmd("G", ProScan3man.WAIT_FOR_1LINE, x, y, z)

    def move_by(self, x: int, y: int, z: int | None):
        return self.send_cmd("GR", ProScan3man.WAIT_FOR_1LINE, x, y, z)

    def move_x_to(self, x: int):
        return self.send_cmd("GX", ProScan3man.WAIT_FOR_1LINE, x)

    def move_y_to(self, y: int):
        return self.send_cmd("GY", ProScan3man.WAIT_FOR_1LINE, y)

    def turn_joystick(self, b_on_off):
        #FIXME: ??? Doc unclear
        return self.send_cmd("J" if b_on_off else "H", ProScan3man.WAIT_FOR_1LINE)

    def set_joystick_direction(self, b_x_y: bool, b_inverted: bool):
        return self.send_cmd("JXD" if b_x_y else "JYD", ProScan3man.WAIT_FOR_1LINE, -1 if b_inverted else 1)

    def get_joystick_direction(self, b_x_y):
        return self.send_cmd("JXD" if b_x_y else "JYD", ProScan3man.WAIT_FOR_1LINE)

    def move_focus_to_zero(self):
        return self.send_cmd("M", ProScan3man.WAIT_FOR_1LINE)


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


class ProScan3ConfigWindow(Ui_ProScan3_Config_Window):
    """
        ProScan3 Helper class with configuration window
    """
    def __init__(self, ProScan3man: ProScan3Man):
        self.ProScan3man = ProScan3man
        self.window = QWidget()
        Ui_ProScan3_Config_Window.__init__(self)
        self.setupUi(self.window)

        self.pushButton_COM_Refresh.clicked.connect(self.refresh_comlist)
        self.pushButton_COM_Open.clicked.connect(self.open_conn_clicked)

        self.comboBox_COM_BaudRate.currentTextChanged.connect(self.baudrate_changed)
        self.comboBox_COM_Parity.currentTextChanged.connect(self.parity_changed)
        self.comboBox_CONN.currentIndexChanged.connect(self.conn_changed)

        # Force to change
        self.baudrate_changed(self.comboBox_COM_BaudRate.currentText())
        self.parity_changed(self.comboBox_COM_Parity.currentText())
        self.conn_changed(self.comboBox_CONN.currentData())

        self.radioButton_Interf_GPIB.clicked.connect(self.interface_changed)
        self.radioButton_Interf_RS232.clicked.connect(self.interface_changed)

        self.refresh_comlist()

        # ProScan3 Settings
        self.comboBox_TimeConstant.currentTextChanged.connect(
            lambda t: self.ProScan3man.time_constant(False, ProScan3Man.time_constant_str2int(t)))
        self.comboBox_Sensitivity.currentTextChanged.connect(
            lambda t: self.ProScan3man.sensitivity(False, ProScan3Man.sensitivity_str2int(t)))
        self.pushButton_SetHarmonic.clicked.connect(
            lambda: self.ProScan3man.detection_harmonic(False, self.spinBox_Harmonic.value()))
        self.comboBox_FilterSlope.currentIndexChanged.connect(
            lambda i: self.ProScan3man.low_pass_filter_slope(False, i))

        self.pushButton_GetX.clicked.connect(
            lambda: self.lineEdit_X.setText(float2str(self.ProScan3man.get_axis_value(ProScan3Man.GET_AXIS_VALUE_X)))
        )
        self.pushButton_GetY.clicked.connect(
            lambda: self.lineEdit_Y.setText(float2str(self.ProScan3man.get_axis_value(ProScan3Man.GET_AXIS_VALUE_Y)))
        )
        self.pushButton_GetR.clicked.connect(
            lambda: self.lineEdit_R.setText(float2str(self.ProScan3man.get_axis_value(ProScan3Man.GET_AXIS_VALUE_R)))
        )
        self.pushButton_GetTheta.clicked.connect(
            lambda: self.lineEdit_Theta.setText(float2str(self.ProScan3man.get_axis_value(ProScan3Man.GET_AXIS_VALUE_THETA)))
        )
        self.pushButton_GetAll.clicked.connect(self.snap_all_values)

        self.lineEdit_phase.setValidator(
            # FIXME: validation
            QDoubleValidator(bottom=0.0, top=99.99, decimals=6))
        self.pushButton_SetPhase.clicked.connect(self.set_phase_clicked)
        self.pushButton_Autophase.clicked.connect(
            lambda: self.lineEdit_phase.setText(f"{self.ProScan3man.ref_phase_shift(True):.4f}"))
        self.radioButton_ref_src_external.toggled.connect(self.ref_src_changed)
        self.radioButton_ref_src_internal.toggled.connect(self.ref_src_changed)

        self.interface_changed()

    def snap_all_values(self):
        x, y, r, theta, f = self.ProScan3man.get_parameters_value(ProScan3Man.GET_PARAMETER_X,
                                                               ProScan3Man.GET_PARAMETER_Y,
                                                               ProScan3Man.GET_PARAMETER_R,
                                                               ProScan3Man.GET_PARAMETER_THETA,
                                                               ProScan3Man.GET_PARAMETER_REF_FREQ)
        self.lineEdit_X.setText(float2str(x))
        self.lineEdit_Y.setText(float2str(y))
        self.lineEdit_R.setText(float2str(r))
        self.lineEdit_Theta.setText(float2str(theta))
        self.lineEdit_Frequency.setText(f"{f:.6f}")

        self.refresh_comlist()

    def ref_src_changed(self):
        if self.radioButton_ref_src_external.isChecked():
            self.radioButton_ref_src_internal.setChecked(False)
            self.ProScan3man.ref_source(False, ProScan3Man.REF_SOURCE_EXTERNAL)
            self.pushButton_SetFrequency.setEnabled(False)
            self.lineEdit_Frequency.setText(f"{self.ProScan3man.ref_frequency(True): .6f}")

        if self.radioButton_ref_src_internal.isChecked():
            self.radioButton_ref_src_external.setChecked(False)
            self.ProScan3man.ref_source(False, ProScan3Man.REF_SOURCE_INTERNAL)
            self.lineEdit_Frequency.setText(f"{self.ProScan3man.ref_frequency(True): .6f}")
            self.pushButton_SetFrequency.setEnabled(True)

    def set_phase_clicked(self):
        try:
            if not self.lineEdit_phase.hasAcceptableInput():
                raise ValueError("Not acceptable phase value")
            new_phase = float(self.lineEdit_phase.text())
            self.ProScan3man.ref_phase_shift(False, new_phase)
            self.pushButton_SetPhase.setStyleSheet("background: green")
        except ValueError as ve:
            self.pushButton_SetPhase.setStyleSheet("background: red")
            self.lineEdit_phase.setText(f"{self.ProScan3man.ref_phase_shift(True):.4f}")

    def sync_current_settings(self):
        if self.ProScan3man is not None:
            self.comboBox_TimeConstant.setCurrentText(
                ProScan3Man.time_constant_int2str(self.ProScan3man.time_constant(True)))
            self.comboBox_Sensitivity.setCurrentText(
                ProScan3Man.sensitivity_int2str(self.ProScan3man.sensitivity(True)))
            self.comboBox_FilterSlope.setCurrentIndex(self.ProScan3man.low_pass_filter_slope(True))
            self.lineEdit_phase.setText(f"{self.ProScan3man.ref_phase_shift(True):.4f}")
            if self.ProScan3man.ref_source(True) == 1:
                self.radioButton_ref_src_internal.setChecked(True)
                self.radioButton_ref_src_external.setChecked(False)
            else:
                self.radioButton_ref_src_internal.setChecked(False)
                self.radioButton_ref_src_external.setChecked(True)
            self.ref_src_changed()
            self.spinBox_Harmonic.setValue(self.ProScan3man.detection_harmonic(True))
            self.snap_all_values()

    def conn_changed(self, i: int):
        if self.radioButton_Interf_RS232.isChecked():
            self.ProScan3man.com_dev = self.comboBox_CONN.currentData()
        elif self.radioButton_Interf_GPIB.isChecked():
            self.ProScan3man.visa_dev = self.comboBox_CONN.currentText()

    def parity_changed(self, p: str):
        if p == 'None':
            self.ProScan3man.ser_parity = serial.PARITY_NONE
        elif p == 'ODD':
            self.ProScan3man.ser_parity = serial.PARITY_ODD
        elif p == 'EVEN':
            self.ProScan3man.ser_parity = serial.PARITY_EVEN
        else:
            raise ValueError(f"Unknown parity {p}")

    def baudrate_changed(self, b: int or str):
        if type(b) is str:
            b = int(b)
        self.ProScan3man.ser_baudrate = b

    def refresh_comlist(self):
        self.comboBox_CONN.clear()
        if self.radioButton_Interf_RS232.isChecked():
            com_dict = get_available_COMs()
            for com_dev in com_dict.keys():
                self.comboBox_CONN.addItem(com_dev + ':' + com_dict[com_dev], com_dev)
        elif self.radioButton_Interf_GPIB.isChecked():
            self.comboBox_CONN.addItems(self.ProScan3man.visa_rm.list_resources())

    def open_conn_clicked(self, state):
        if not state:  # post event state
            self.close_conn()
        else:
            # FIXME: Actually open connection
            self.open_conn()

    def open_conn(self):
        global ProScan3_logger
        try:
            self.ProScan3man.open()
            self.pushButton_COM_Open.setText("Close")
            self.pushButton_COM_Open.setChecked(True)
            # Disable the COM configuration input
            self.comboBox_CONN.setDisabled(True)
            self.comboBox_COM_BaudRate.setDisabled(True)
            self.comboBox_COM_Parity.setDisabled(True)
            self.pushButton_COM_Refresh.setDisabled(True)
            # Enable the settings input
            self.groupBox_Settings.setDisabled(False)
            self.label_COM_Status.setStyleSheet("background: green")

            # update current settings
            self.sync_current_settings()
            ProScan3_logger.info(f"ProScan3 COM connection opened", extra={"component": "ProScan3"})
            if self.radioButton_Interf_RS232.isChecked():
                ProScan3_logger.debug(f"ProScan3 COM: {self.ProScan3man.com_dev} "
                                   f"B:{self.ProScan3man.ser_baudrate} "
                                   f"P:{self.ProScan3man.ser_parity} "
                                   f"S:{self.ProScan3man.ser_stopbits}", extra={"component": "ProScan3"})
            else:
                ProScan3_logger.debug(f"ProScan3 Visa addr:: {self.ProScan3man.visa_dev} ", extra={"component": "ProScan3"})
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            ProScan3_logger.error(f"Failed to open ProScan3 COM connection", extra={"component": "ProScan3"})
            self.close_conn()

    def close_conn(self):
        global ProScan3_logger
        self.ProScan3man.close()
        # FIXME: stop all the ProScan3 update activities
        self.pushButton_COM_Open.setText("Open")
        self.pushButton_COM_Open.setChecked(False)
        # Enable the COM configuration input
        self.comboBox_CONN.setDisabled(False)
        if self.radioButton_Interf_RS232.isChecked():
            self.comboBox_COM_BaudRate.setDisabled(False)
            self.comboBox_COM_Parity.setDisabled(False)
        self.pushButton_COM_Refresh.setDisabled(False)
        # Disable the settings input
        self.groupBox_Settings.setDisabled(True)
        self.label_COM_Status.setStyleSheet("background: red")
        ProScan3_logger.info(f"ProScan3 COM connection closed", extra={"component": "ProScan3"})

    def show(self):
        self.window.show()

    def close(self):
        self.window.hide()

    def get_current_settings(self, with_header: bool = True):
        if self.ProScan3man.is_open():
            if with_header:
                setting_str = "--------SRS ProScan3-------\n"
            else:
                setting_str = ""
            setting_str = setting_str + f"Time constant: {self.comboBox_TimeConstant.currentText()}\n" \
                          f"Sensitivity: {self.comboBox_Sensitivity.currentText()}\n" \
                          f"Filter Slope: {self.comboBox_FilterSlope.currentText()}\n" \
                          f"Frequency: {self.lineEdit_Frequency.text()}\n" \
                          f"Harmony: {self.spinBox_Harmonic.value()}\n"
            return setting_str
        else:
            return ""

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])

    ProScan3_man = ProScan3Man()
    print(f'Starting...')
    ProScan3_man.show_config_window()
    QApplication.instance().exec_()
