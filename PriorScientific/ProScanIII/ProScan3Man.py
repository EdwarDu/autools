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
from enum import Enum

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

    ERROR_CODE_DICT = {0: "NO_ERROR", 1: "NO_STAGE", 2: "NOT_IDLE", 3: "NO_DRIVE", 4: "STRING_PARSE", 5: "COMMAND_NOT_FOUND",
            6: "INVALID_SHUTTER", 7: "NO_FOCUS", 8: "VALUE_OUT_OF_RANGE", 9: "INVALID_WHEEL", 10: "ARG1_OUT_OF_RANGE", 
            11: "ARG2_OUT_OF_RANGE",12: "ARG3_OUT_OF_RANGE",13: "ARG4_OUT_OF_RANGE",14: "ARG5_OUT_OF_RANGE",15: "ARG6_OUT_OF_RANGE",
            16: "INCORRECT_STATE", 17: "NO_FILTER_WHEEL", 18: "QUEUE_FULL", 19: "COMP_MODE_SET", 20: "SHUTTER_NOT_FITTED",
            21: "INVALID_CHECKSUM", 22: "NOT_ROTARY", 40: "NO_FOURTH_AXIS", 41: "AUTOFOCUS_IN_PROG", 42: "NO_VIDEO",
            43: "NO_ENCODER", 44: "SIS_NOT_DONE", 45: "NO_VACUUM_DETECTOR", 46: "NO_SHUTTLE", 47: "VACUUM_QUEUED",
            48: "SIZ_NOT_DONE", 49: "NOT_SLIDE_LOADER", 50: "ALREADY_PRELOADED", 51: "STAGE_NOT_MAPPED", 52: "TRIGGER_NOT_FITTED",
            52: "INTERPOLATOR_NOT_FITTED"}

    class ProScan3Error(Exception):
        pass

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
            if wait_for == ProScan3Man.WAIT_FOR_1LINE:
                res = sio.readline()
            elif wait_for == ProScan3Man.WAIT_FOR_END:
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
 
            if res.startswith("E,"):
                # This is an error
                err_code_m = re.match(r"\s*\d+", res[2:])
                if err_code_m is not None:
                    err_code = int(err_code_m[0])
                    if err_code not in ProScan3Man.ERROR_CODE_DICT.keys():
                        err_msg = f"UNKNOWN ERROR CODE {err_code}"
                    else:
                        err_msg = ProScan3Man.ERROR_CODE_DICT[err_code]
                else:
                    err_msg = res[2:]

                raise ProScan3Man.ProScan3Error(err_msg)

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
        return self.send_cmd("?", ProScan3Man.WAIT_FOR_END)

    def check_limit_switch(self):
        ans = self.send_cmd("=", ProScan3Man.WAIT_FOR_1LINE)
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
            ans = self.send_cmd("$", ProScan3Man.WAIT_FOR_1LINE, axis)
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
                ans = self.send_cmd("BAUD", ProScan3Man.WAIT_FOR_1LINE, allowed_baudrate_dict[baudrate])
            except Exception as e:
                ProScan3_logger.warning(f"Exception when try to set baudrate to {baudrate}: <{e}>", extra={"component": "ProScan3"})
            finally:
                self.ser_baudrate = baudrate
                self.close()
                self.open()

    def get_command_mode(self):
        return self.send_cmd("COMP", ProScan3Man.WAIT_FOR_1LINE)

    def set_command_mode(self, b_compatibility: bool):
        return self.send_cmd("COMP", ProScan3Man.WAIT_FOR_1LINE, 1 if b_compatibility else 0)

    #def get_instrument_info(self):
    #    return self.send_cmd("DATE", ????)

    def set_error_code_mode(self, b_human_readable: bool):
        return self.send_cmd("ERROR", ProScan3Man.WAIT_FOR_1LINE, 1 if b_human_readable else 0)

    def stop_movement(self):
        return self.send_cmd("I", ProScan3Man.WAIT_FOR_1LINE)

    def kill_movement(self):
        return self.send_cmd("K", ProScan3Man.WAIT_FOR_1LINE)

    def macro_start_stop(self):
        return self.send_cmd("MACRO", ProScan3Man.WAIT_FOR_1LINE)

    def get_serial_num(self):
        return self.send_cmd("SERIAL", ProScan3Man.WAIT_FOR_1LINE)

    def get_limit_switch_status(self):
        ans = self.send_cmd("LMT", ProScan3Man.WAIT_FOR_1LINE)
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
        return self.send_cmd("SOAK", ProScan3Man.WAIT_FOR_1LINE)

    def get_software_version(self):
        return self.send_cmd("VERSION", ProScan3Man.WAIT_FOR_1LINE)

    def insert_wait(self, ms: int):
        return self.send_cmd("WAIT", ProScan3Man.WAIT_FOR_1LINE, ms)

    def get_stage_step_size(self,):
        ans = self.send_cmd("X", ProScan3Man.WAIT_FOR_1LINE)
        u, v = re.split(r"[,\s]+", ans)
        return (u, v)

    def set_stage_step_size(self, x_step: int, y_step: int):
        return self.send_cmd("X", ProScan3Man.WAIT_FOR_1LINE, x_step, y_step)

    def set_stage_backlash(self, b_stage_z: bool, b_for_ser_joystick: bool, bl_enable: bool, bl_value: int | None = None):
        return self.send_cmd("BL"+("S" if b_stage_z else "Z") + ("H" if b_for_ser_joystick else "J"), 
                ProScan3Man.WAIT_FOR_1LINE, 1 if bl_enable else 0, bl_value)

    def get_stage_backlash(self, b_stage_z: bool):
        ans = self.send_cmd("BL"+("S" if b_stage_z else "Z") + ("H" if b_for_ser_joystick else "J"), ProScan3Man.WAIT_FOR_1LINE)
        return re.split(r"[,\s]+", ans)
 
    def move_in_dir(self, d: str, steps: int | None):
        if d not in ("B", "F", "L", "R", "U", "D"):
            ProScan3_logger.error(f"Direction {d} invalid (B, F, L, R, U, D)", extra={"component": "ProScan3"})
            raise ValueError(f"Direction {d} invalid (B, F, L, R, U, D)")
        return self.send_cmd(d, ProScan3Man.WAIT_FOR_1LINE, steps)

    def move_to(self, x: int, y: int, z: int | None):
        return self.send_cmd("G", ProScan3Man.WAIT_FOR_1LINE, x, y, z)

    def move_by(self, x: int, y: int, z: int | None):
        return self.send_cmd("GR", ProScan3Man.WAIT_FOR_1LINE, x, y, z)

    def move_xyz_to(self, axis_x_y_z: str, pos: int):
        if axis_x_y_z not in ("X", "Y", "Z"):
            ProScan3_logger.error(f"Axis {axis_x_y_z} invalid (X, Y, Z)", extra={"component": "ProScan3"})
            raise ValueError(f"Axis {axis_x_y_z} invalid (X, Y, Z)")
        return self.send_cmd("G"+axis_x_y_z, ProScan3Man.WAIT_FOR_1LINE, pos)

    def turn_joystick(self, b_on_off):
        #FIXME: ??? Doc unclear
        return self.send_cmd("J" if b_on_off else "H", ProScan3Man.WAIT_FOR_1LINE)

    def set_direction(self, b_for_ser_joystick: bool, axis_x_y_z: str, b_inverted: bool):
        if axis_x_y_z not in ("X", "Y", "Z"):
            ProScan3_logger.error(f"Axis {axis_x_y_z} invalid (X, Y, Z)", extra={"component": "ProScan3"})
            raise ValueError(f"Axis {axis_x_y_z} invalid (X, Y, Z)")
        return self.send_cmd(("" if b_for_ser_joystick else "J")+axis_x_y_z+"D", ProScan3Man.WAIT_FOR_1LINE, -1 if b_inverted else 1)

    def get_direction(self, b_for_ser_joystick: bool, axis_x_y_z: str):
        if axis_x_y_z not in ("X", "Y", "Z"):
            ProScan3_logger.error(f"Axis {axis_x_y_z} invalid (X, Y, Z)", extra={"component": "ProScan3"})
            raise ValueError(f"Axis {axis_x_y_z} invalid (X, Y, Z)")
        return self.send_cmd(("" if b_for_ser_joystick else "J")+axis_x_y_z+"D", ProScan3Man.WAIT_FOR_1LINE)

    def move_xyz_to_zero(self):
        return self.send_cmd("M", ProScan3Man.WAIT_FOR_1LINE)

    def set_speed_joystick(self, b_stage_z: bool, speed_perc: int):
        if 1 <= speed_perc <= 100:
            return self.send_cmd("O" if b_stage_z else "OF", ProScan3Man.WAIT_FOR_1LINE, speed_perc)
        else:
            ProScan3_logger.error(f"Speed percentage {speed_perc} out of range [1, 100]", extra={"component": "ProScan3"})
            raise ValueError(f"Speed percentage {speed_perc} out of range [1, 100]")

    def get_speed_joystick(self, b_stage_z: bool):
        #FIXME: doc is not clear
        return int(self.send_cmd("O" if b_stage_z else "OF", ProScan3Man.WAIT_FOR_1LINE))

    def get_xyz_axes_pos(self):
        ans = self.send_cmd("P", ProScan3Man.WAIT_FOR_1LINE)
        return re.split(r"[,\s]+", ans)

    def set_xyz_axes_pos(self, x: int, y: int, z: int):
        #WARNING: no range check
        return self.send_cmd("P", ProScan3Man.WAIT_FOR_1LINE, x, y, z)

    def get_axis_pos(self, axis_x_y_z: str):
        if axis_x_y_z not in ("X", "Y", "Z"):
            ProScan3_logger.error(f"Axis {axis_x_y_z} invalid (X, Y, Z)", extra={"component": "ProScan3"})
            raise ValueError(f"Axis {axis_x_y_z} invalid (X, Y, Z)")
        return int(self.send_cmd("P"+axis_x_y_z, ProScan3Man.WAIT_FOR_1LINE))

    def set_x_axis_pos(self, axis_x_y_z: str, pos: int):
        if axis_x_y_z not in ("X", "Y", "Z"):
            ProScan3_logger.error(f"Axis {axis_x_y_z} invalid (X, Y, Z)", extra={"component": "ProScan3"})
            raise ValueError(f"Axis {axis_x_y_z} invalid (X, Y, Z)")
        return self.send_cmd("P"+axis_x_y_z, ProScan3Man.WAIT_FOR_1LINE, pos)

    def set_unit_step_size(self, b_stage_z: bool, n_microsteps: int):
        return self.send_cmd("SS"+("" if b_stage_z else "Z"), ProScan3Man.WAIT_FOR_1LINE, n_microsteps)

    def get_unit_step_size(self, b_stage_z: bool):
        #WARNING: DOC: in COMPATABILITY mode, this value is based on the older 100 microsteps/fullstep of H127/128 sys
        return int(self.send_cmd("SS"+("" if b_stage_z else "Z"), ProScan3Man.WAIT_FOR_1LINE))

    def set_resolution(self, b_stage_z: bool, resolution: float):
        #FIXME: DOC: NO RESPONSE????? WAIT FOR NOTHING???
        return self.send_cmd("RES", ProScan3Man.WAIT_FOR_1LINE, "S" if b_stage_z else "Z", f"{resolution:.2f}")

    def get_resolution(self, axis: str):
        #FIXME: DOC: NO RESPONSE????? WAIT FOR NOTHING???
        allowed_axis = ("X", "Y", "S", "Z", "A", "F", "F1", "F2")
        if axis not in allowed_axis:
            ProScan3_logger.error(f"Invalid axis: <{axis}>", extra={"component": "ProScan3"})
            raise ValueError(f"{axis} is not allowed as parameter for RES, only {allowed_axis}")
        return float(self.send_cmd("RES", ProScan3Man.WAIT_FOR_1LINE, axis))

    def restore_index_of_stage(self):
        #WARNING: check doc
        return self.send_cmd("RIS", ProScan3Man.WAIT_FOR_1LINE)

    def set_index_of_stage(self):
        #WARNING: check doc
        return self.send_cmd("SIS", ProScan3Man.WAIT_FOR_1LINE)

    class Unit_type(Enum):
        UNIFIED = 1
        INTRINSIC = 2
        MICRONS = 3

    def set_max_stage_acc(self, acc: int, acc_type: ProScan3Man.Unit_type):
        if acc_typpe == self.Unit_type.UNIFIED and not 1 <= acc <= 1000:
            ProScan3_logger.error(f"Stage max acceleration (UNIFIED) {acc} out of range [1, 1000]", extra={"component": "ProScan3"})
            raise ValueError(f"Stage max acceleration (UNIFIED) {acc} out of range [1, 1000]")
        else:
            if acc_type == self.Unit_type.UNIFIED:
                return self.send_cmd("SAS", ProScan3Man.WAIT_FOR_1LINE, acc)
            elif acc_type == self.Unit_type.INTRINSIC:
                return self.send_cmd("SAS,n,i", ProScan3Man.WAIT_FOR_1LINE, acc)
            else:
                #elif acc_type == self.Unit_type.MICRONS:
                return self.send_cmd("SAS,n,u", ProScan3Man.WAIT_FOR_1LINE, acc)

    def get_max_stage_acc(self, acc_type: ProScan3Man.Unit_type):
        if acc_type == ProScan3Man.Unit_type.UNIFIED:
            return int(self.send_cmd("SAS", ProScan3Man.WAIT_FOR_1LINE))
        elif acc_type == ProScan3Man.Unit_type.INTRINSIC:
            return int(self.send_cmd("SAS,i", ProScan3Man.WAIT_FOR_1LINE))
        else: #if acc_type == ProScan3Man.Unit_type.UNIFIED:
            return int(self.send_cmd("SAS,u", ProScan3Man.WAIT_FOR_1LINE))

    def set_max_stage_speed(self, speed: int, speed_type: ProScan3Man.Unit_type):
        if speed_typpe == self.Unit_type.UNIFIED and not 1 <= speed <= 1000:
            ProScan3_logger.error(f"Stage max speed (UNIFIED) {speed} out of range [1, 1000]", extra={"component": "ProScan3"})
            raise ValueError(f"Stage max speed (UNIFIED) {speed} out of range [1, 1000]")
        else:
            if speed_type == self.Unit_type.UNIFIED:
                return self.send_cmd("SMS", ProScan3Man.WAIT_FOR_1LINE, speed)
            elif speed_type == self.Unit_type.INTRINSIC:
                return self.send_cmd("SMS,n,i", ProScan3Man.WAIT_FOR_1LINE, speed)
            else:
                #elif speed_type == self.Unit_type.MICRONS:
                return self.send_cmd("SMS,n,u", ProScan3Man.WAIT_FOR_1LINE, speed)

    def get_max_stage_speed(self, speed_type: ProScan3Man.Unit_type):
        if speed_type == ProScan3Man.Unit_type.UNIFIED:
            return int(self.send_cmd("SMS", ProScan3Man.WAIT_FOR_1LINE))
        elif speed_type == ProScan3Man.Unit_type.INTRINSIC:
            return int(self.send_cmd("SMS,i", ProScan3Man.WAIT_FOR_1LINE))
        else: #if speed_type == ProScan3Man.Unit_type.UNIFIED:
            return int(self.send_cmd("SMS,u", ProScan3Man.WAIT_FOR_1LINE))

    def set_stage_scurve_value(self, c: int):
        if 1 <= c <= 1000:
            return self.send_cmd("SCS", ProScan3Man.WAIT_FOR_1LINE, c)
        else:
            ProScan3_logger.error(f"Stage S-curve value {c} out of range [1, 1000]", extra={"component": "ProScan3"})
            raise ValueError(f"Stage S-curve value {c} out of range [1, 1000]")

    def get_stage_scurve_value(self):
        return int(self.send_cmd("SCS", ProScan3Man.WAIT_FOR_1LINE))

    def get_stage_info(self):
        return self.send_cmd("STAGE", ProScan3Man.WAIT_FOR_END)

    def get_skew_angle(self):
        #FIXME: DOC is not clear
        return float(self.send_cmd("SKEW", ProScan3Man.WAIT_FOR_1LINE))

    def set_stage_focus_to_zero(self):
        #FIXME: DOC is not clear?? set current stage and focus position to ZERO?
        return self.send_cmd("Z", ProScan3Man.WAIT_FOR_1LINE)

    def turn_motor(self, motor: str | int, b_on_off: bool):
        if (type(motor) is str and motor not in ProScan3Man.AXIS_ID.keys()) or \
                (type(motor) is int and motor not in ProScan3Man.AXIS_ID.values()):
            ProScan3_logger.error(f"Motor {motor} invalid ({ProScan3Man.AXIS_ID})", extra={"component": "ProScan3"})
            raise ValueError(f"Motor {motor} invalid ({ProScan3Man.AXIS_ID})")
        else:
            return self.send_cmd("MOTOR", ProScan3Man.WAIT_FOR_1LINE, motor, 1 if b_on_off else 0)

    def set_curr_pos_as_sw_limit(self, axis: str | int, b_low_high: bool):
        if (type(axis) is str and axis not in ProScan3Man.AXIS_ID.keys()) or \
                (type(axis) is int and axis not in ProScan3Man.AXIS_ID.values()):
            ProScan3_logger.error(f"Axis {axis} invalid ({ProScan3Man.AXIS_ID})", extra={"component": "ProScan3"})
            raise ValueError(f"Axis {axis} invalid ({ProScan3Man.AXIS_ID})")
        else:
            return self.send_cmd("SWLL" if b_low_high else "SWLH", ProScan3Man.WAIT_FOR_1LINE, axis)

    def clear_curr_pos_as_sw_limit(self, axis: str | int):
        if (type(axis) is str and axis not in ProScan3Man.AXIS_ID.keys()) or \
                (type(axis) is int and axis not in ProScan3Man.AXIS_ID.values()):
            ProScan3_logger.error(f"Axis {axis} invalid ({ProScan3Man.AXIS_ID})", extra={"component": "ProScan3"})
            raise ValueError(f"Axis {axis} invalid ({ProScan3Man.AXIS_ID})")
        else:
            return self.send_cmd("SWLC", ProScan3Man.WAIT_FOR_1LINE, axis)

    def move_xy_at_speed(self, x_speed: int, y_speed: int):
        return self.send_cmd("VS", ProScan3Man.WAIT_FOR_1LINE, x_speed, y_speed)


    # Z Axis commands
    def get_z_step_size(self):
        return int(self.send_cmd("C", ProScan3Man.WAIT_FOR_1LINE))

    def set_z_step_size(self, z_step: int):
        return self.send_cmd("C", ProScan3Man.WAIT_FOR_1LINE, z_step)

    def get_z_info(self):
        return self.send_cmd("FOCUS", ProScan3Man.WAIT_FOR_END)

    def set_max_z_acc(self, acc: int)
        if not 1 <= acc <= 100:
            ProScan3_logger.error(f"Focus max acceleration {acc} out of range [1, 100]", extra={"component": "ProScan3"})
            raise ValueError(f"Focus max acceleration {acc} out of range [1, 100]")
        else:
            return self.send_cmd("SAZ", ProScan3Man.WAIT_FOR_1LINE, acc)

    def get_max_z_acc(self):
        return int(self.send_cmd("SAZ", ProScan3Man.WAIT_FOR_1LINE))

    def set_max_z_speed(self, speed: int):
        if not 1 <= speed <= 100:
            ProScan3_logger.error(f"Focus max speed {speed} out of range [1, 100]", extra={"component": "ProScan3"})
            raise ValueError(f"Focus max speed {speed} out of range [1, 100]")
        else:
            return self.send_cmd("SMZ", ProScan3Man.WAIT_FOR_1LINE, speed)

    def get_max_z_speed(self):
        return int(self.send_cmd("SMZ", ProScan3Man.WAIT_FOR_1LINE))

    def set_z_scurve_value(self, c: int):
        if 1 <= c <= 100:
            return self.send_cmd("SCZ", ProScan3Man.WAIT_FOR_1LINE, c)
        else:
            ProScan3_logger.error(f"Stage S-curve value {c} out of range [1, 100]", extra={"component": "ProScan3"})
            raise ValueError(f"Stage S-curve value {c} out of range [1, 100]")

    def get_z_scurve_value(self):
        return int(self.send_cmd("SCZ", ProScan3Man.WAIT_FOR_1LINE))

    def set_unit_per_revolution(self, n_micros: int):
        return self.send_cmd("UPR", ProScan3Man.WAIT_FOR_1LINE, "Z", n_micros)

    def get_unit_per_revolution(self):
        return int(self.send_cmd("UPR", ProScan3Man.WAIT_FOR_1LINE, "Z"))

    def zplane_tracking_set_point(self, point_123: int):
        if 1 <= point_123 <= 3:
            return self.send_cmd("ZPLANE", ProScan3Man.WAIT_FOR_1LINE, point_123)
        else:
            ProScan3_logger.error(f"ZPLANE tracks 3 points (1, 2, 3) {point_123}", extra={"component": "ProScan3"})
            raise ValueError(f"ZPLANE tracks 3 points (1, 2, 3) {point_123}")

    def zplane_tracking(self, b_enable_disable: bool):
        return self.send_cmd("ZPLANE", ProScan3Man.WAIT_FOR_1LINE, "E" if b_enable_disable else "D")

    def zplane_tracking_status(self):
        return self.send_cmd("ZPLANE", ProScan3Man.WAIT_FOR_1LINE) == "1"

    class FilterWheelCommand(Enum):
        NEXT_FILTER = 0
        PREVIOUS_FILTER = 1
        REPORT_FILTER_POS = 2 
        HOME_ROUTINE = 3 
        SET_STARTUP_AUTOHOME = 4 
        UNSET_STARTUP_AUTOHOME = 5

        FW_CMD = ["N", "P", "F", "H", "A", "D"]

        def __str__(self):
            return FilterWheelCommand.FW_CMD[self.value]

    @static_method
    def _only_3_filter_wheel(fw_123: int):
        if not 1 <= fw_123 <= 3:
            ProScan3_logger.error(f"Max 3 Filter Wheel (1, 2, 3) {fw_123}", extra={"component": "ProScan3"})
            raise ValueError(f"Max 3 Filter Wheel (1, 2, 3) {fw_123}")

    # Filter Wheel Commands
    def filter_wheel_command(self, fw_123: int, fw_cmd: ProScan3Man.FilterWheelCommand):
        ProScan3Man._only_3_filter_wheel(fw_123)
        return self.send_cmd("7", ProScan3Man.WAIT_FOR_1LINE, fw_cmd)

    def filter_wheel_set_pos(self, f1: int, f2: int, f3: int):
        #WARNING: only in COMP 0 mode
        return self.send_cmd("7", ProScan3Man.WAIT_FOR_1LINE, f1, f2, f3)

    def filter_wheel_enable_auto_shutter(self, b_enable_disable: bool):
        return self.send_cmd("7", ProScan3Man.WAIT_FOR_1LINE, "C" if b_enable_disable else "D")

    def filter_wheel_filter_tag(self, fw_123: int, fp: int, text: str | None = None):
        # pass text = None to get tag
        ProScan3Man._only_3_filter_wheel(fw_123)
        if text is not None and len(text) > 6:
            ProScan3_logger.warning(f"Filter Tag can only be 6 ch max, truncating {text} to {text[:6]}", extra={"component": "ProScan3"})
            text = text[:6]
        return self.send_cmd("7", ProScan3Man.WAIT_FOR_1LINE, fw_123, "T", "P", text)

    def filter_wheel_get_info(self, fw_123: int):
        ProScan3Man._only_3_filter_wheel(fw_123)
        return self.send_cmd("FILTER", ProScan3Man.WAIT_FOR_END, fw_123)

    def filter_wheel_n_pos(self, fw_123: int):
        ProScan3Man._only_3_filter_wheel(fw_123)
        return int(self.send_cmd("FPW", ProScan3Man.WAIT_FOR_1LINE, fw_123))

    def filter_wheel_get_acc(self, fw_123: int):
        ProScan3Man._only_3_filter_wheel(fw_123)
        return int(self.send_cmd("SAF", ProScan3Man.WAIT_FOR_1LINE, fw_123))

    def filter_wheel_set_acc(self, fw_123: int, perc: int):
        ProScan3Man._only_3_filter_wheel(fw_123)
        if not 1 <= perc <= 100:
            ProScan3_logger.error(f"Filter Wheel acceleration percentage {perc} out of range [1, 100]", extra={"component": "ProScan3"})
            raise ValueError(f"Filter Wheel acceleration percentage {perc} out of range [1, 100]")
        return self.send_cmd("SAF", ProScan3Man.WAIT_FOR_1LINE, fw_123, perc)

    def filter_wheel_get_scurve(self, fw_123: int):
        ProScan3Man._only_3_filter_wheel(fw_123)
        return int(self.send_cmd("SCF", ProScan3Man.WAIT_FOR_1LINE, fw_123))

    def filter_wheel_set_scurve(self, fw_123: int, perc: int):
        ProScan3Man._only_3_filter_wheel(fw_123)
        if not 1 <= perc <= 100:
            ProScan3_logger.error(f"Filter Wheel S-Curve setting {perc} out of range [1, 100]", extra={"component": "ProScan3"})
            raise ValueError(f"Filter Wheel S-Curve setting {perc} out of range [1, 100]")
        return self.send_cmd("SCF", ProScan3Man.WAIT_FOR_1LINE, fw_123, perc)

    def filter_wheel_get_max_speed(self, fw_123: int):
        ProScan3Man._only_3_filter_wheel(fw_123)
        return int(self.send_cmd("SMF", ProScan3Man.WAIT_FOR_1LINE, fw_123))

    def filter_wheel_set_max_speed(self, fw_123: int, perc: int):
        ProScan3Man._only_3_filter_wheel(fw_123)
        if not 1 <= perc <= 100:
            ProScan3_logger.error(f"Filter Wheel max speed {perc} out of range [1, 100]", extra={"component": "ProScan3"})
            raise ValueError(f"Filter Wheel max speed {perc} out of range [1, 100]")
        return self.send_cmd("SMF", ProScan3Man.WAIT_FOR_1LINE, fw_123, perc)

    # Shutter Commands
    @static_method
    def _only_3_shutter(sht_123: int):
        if not 1 <= sht_123 <= 3:
            ProScan3_logger.error(f"Max 3 Shutters (1, 2, 3) {sht_123}", extra={"component": "ProScan3"})
            raise ValueError(f"Max 3 Shutters (1, 2, 3) {sht_123}")

    def shutter_switch(self, sht_123: int, b_open_close: bool, duration_ms: int | None):
        ProScan3Man._only_3_shutter(sht_123)
        return self.send_cmd("8", ProScan3Man.WAIT_FOR_1LINE, sht_123, 0 if b_open_close else 1, duration_ms)

    def shutter_startup_state(self, s1_open_close: bool, s2_open_close: bool, s3_open_close: bool):
        return self.send_cmd("8", ProScan3Man.WAIT_FOR_1LINE, 0, 
                0 if s1_open_close else 1, 
                0 if s2_open_close else 1, 
                0 if s3_open_close else 1)

    def shutter_status_open(self, sht_123: int) -> bool:
        # 0 is open
        ProScan3Man._only_3_shutter(sht_123)
        return int(self.send_cmd("8", ProScan3Man.WAIT_FOR_1LINE, sht_123)) == 0

    def shutter_get_info(self, sht_123: int):
        ProScan3Man._only_3_shutter(sht_123)
        return self.send_cmd("Shutter", ProScan3Man.WAIT_FOR_END, sht_123)

    # NOT IMPLEMENTED: Lumen Pro Commands, Pattern Commands, OEM Commands

    def get_stage_mapping_status(self, b_with_4_values: bool):
        ans = self.send_cmd("CORRECT", ProScan3Man.WAIT_FOR_1LINE, "?" if b_with_4_values else None)
        return re.split(r"[,\s]+", ans)

    def enable_stage_mapping(self, b_enable_disable: bool):
        return self.send_cmd("CORRECT", ProScan3Man.WAIT_FOR_1LINE, "E" if b_enable_disable else "D")

    def start_stage_mapping(self):
        # Needs a SIS command first
        return self.send_cmd("CORRECT", ProScan3Man.WAIT_FOR_1LINE, "M")

    def get_error_state(self):
        return self.send_cmd("ERRORSTAT", ProScan3Man.WAIT_FOR_END)


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
    def __init__(self, ps3_man: ProScan3Man):
        self.ps3_man = ps3_man
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

        self.refresh_comlist()

        # ProScan3 Settings

    def conn_changed(self, i: int):
        if self.radioButton_Interf_RS232.isChecked():
            self.ps3_man.com_dev = self.comboBox_CONN.currentData()
        elif self.radioButton_Interf_GPIB.isChecked():
            self.ps3_man.visa_dev = self.comboBox_CONN.currentText()

    def parity_changed(self, p: str):
        if p == 'None':
            self.ps3_man.ser_parity = serial.PARITY_NONE
        elif p == 'ODD':
            self.ps3_man.ser_parity = serial.PARITY_ODD
        elif p == 'EVEN':
            self.ps3_man.ser_parity = serial.PARITY_EVEN
        else:
            raise ValueError(f"Unknown parity {p}")

    def baudrate_changed(self, b: int or str):
        if type(b) is str:
            b = int(b)
        self.ps3_man.ser_baudrate = b

    def refresh_comlist(self):
        self.comboBox_CONN.clear()
        if self.radioButton_Interf_RS232.isChecked():
            com_dict = get_available_COMs()
            for com_dev in com_dict.keys():
                self.comboBox_CONN.addItem(com_dev + ':' + com_dict[com_dev], com_dev)
        elif self.radioButton_Interf_GPIB.isChecked():
            self.comboBox_CONN.addItems(self.ps3_man.visa_rm.list_resources())

    def open_conn_clicked(self, state):
        if not state:  # post event state
            self.close_conn()
        else:
            # FIXME: Actually open connection
            self.open_conn()

    def open_conn(self):
        global ProScan3_logger
        try:
            self.ps3_man.open()
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
            ProScan3_logger.debug(f"ProScan3 COM: {self.ps3_man.com_dev} "
                               f"B:{self.ps3_man.ser_baudrate} "
                               f"P:{self.ps3_man.ser_parity} "
                               f"S:{self.ps3_man.ser_stopbits}", extra={"component": "ProScan3"})
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            ProScan3_logger.error(f"Failed to open ProScan3 COM connection", extra={"component": "ProScan3"})
            self.close_conn()

    def close_conn(self):
        global ProScan3_logger
        self.ps3_man.close()
        # FIXME: stop all the ProScan3 update activities
        self.pushButton_COM_Open.setText("Open")
        self.pushButton_COM_Open.setChecked(False)
        # Enable the COM configuration input
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
        if self.ps3_man.is_open():
            if with_header:
                setting_str = "--------SRS ProScan3-------\n"
            else:
                setting_str = ""
            setting_str = setting_str 
            return setting_str
        else:
            return ""

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])

    ps3man = ProScan3Man()
    print(f'Starting...')
    ps3man.show_config_window()
    QApplication.instance().exec_()
