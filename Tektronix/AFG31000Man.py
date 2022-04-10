#!/usr/bin/env python3

import serial
import serial.tools.list_ports
import pyvisa
import numpy as np
from threading import Lock
from PyQt5.QtWidgets import QWidget
from .afg31000_config_ui import Ui_AFG31000_Config_Window
from PyQt5.QtGui import QDoubleValidator
import traceback
import logging
from PyQt5.QtCore import QObject, pyqtSignal

_SPLIT_LOG = False

if _SPLIT_LOG:
    afg31000_logger = logging.getLogger("afg31000")
    afg31000_logger.setLevel(logging.DEBUG)
    afg31000_fh = logging.FileHandler("afg31000.log")
    afg31000_formatter = logging.Formatter('%(asctime)s [%(component)s] - %(levelname)s - %(message)s')
    afg31000_fh.setFormatter(afg31000_formatter)
    afg31000_logger.addHandler(afg31000_fh)

    afg31000_ch = logging.StreamHandler()
    afg31000_ch.setFormatter(afg31000_formatter)
    afg31000_logger.addHandler(afg31000_ch)
else:
    afg31000_logger = logging.getLogger("autools_setup_main")


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


class AFG31000Man(QObject):
    """Helper (man) Class for communicate with AFG31000"""

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
        self.com_dev = serial_name
        self.ser_baudrate = baudrate
        self.ser_parity = parity
        self.ser_stopbits = stopbits

        self.visa_rm = pyvisa.ResourceManager()
        self.visa_dev = None
        self.visa_inst = None
        self.com_mode = 'rs232'
        self.com_end = '\r'

        if visa_addr is not None:
            self.visa_dev = visa_addr
            self.visa_inst = self.visa_rm.open_resource(self.visa_dev)
            if not AFG31000Man._FAKE_DEV:
                self.output_interface(False, AFG31000Man.OUTPUT_INTERFACE_GPIB)
                self.gpib_override_remote_state(False, AFG31000Man.GPIB_OVERRIDE_REMOTE_STATE_ON)

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

            if not AFG31000Man._FAKE_DEV:
                self.output_interface(False, AFG31000Man.OUTPUT_INTERFACE_RS232)
                self.gpib_override_remote_state(False, AFG31000Man.GPIB_OVERRIDE_REMOTE_STATE_ON)

        if uart_lock is None:
            self.ser_lock = Lock()
        else:
            self.ser_lock = uart_lock

        self.quiet = False
        self.config_window = None

    def open(self):
        if self.com_mode == 'rs232':
            if self.ser is not None and self.ser.is_open:
                self.ser.close()

            self.ser = serial.Serial(port=self.com_dev, baudrate=self.ser_baudrate, bytesize=serial.EIGHTBITS,
                                     parity=self.ser_parity, stopbits=self.ser_stopbits)

            self.ser.inter_byte_timeout = 0.1

            if not self.ser.is_open:
                raise IOError(f"Failed to open the device {self.com_dev}")
            else:
                self.output_interface(False, AFG31000Man.OUTPUT_INTERFACE_RS232)
                self.gpib_override_remote_state(False, AFG31000Man.GPIB_OVERRIDE_REMOTE_STATE_ON)
                self.com_end = '\r'
                self.opened.emit()
        elif self.com_mode == 'gpib':
            if self.visa_inst is not None:
                self.visa_inst.close()
                self.visa_inst = self.visa_rm.open_resource(self.visa_dev)
                self.com_end = '\n'
                self.output_interface(False, AFG31000Man.OUTPUT_INTERFACE_GPIB)
                self.gpib_override_remote_state(False, AFG31000Man.GPIB_OVERRIDE_REMOTE_STATE_ON)
        else:
            raise ValueError(f"Unknown type of mode {self.com_mode}")

    def close(self):
        if self.ser is not None and self.ser.is_open:
            self.ser.close()
        if self.visa_inst is not None:
            self.visa_inst.close()
            self.visa_inst = None
        self.closed.emit()
        self.ser = None

    def is_open(self):
        if self.com_mode == 'rs232':
            return self.ser is not None and self.ser.is_open
        elif self.com_mode == 'gpib':
            return self.visa_inst is not None

    def send_cmd(self, cmd: str, b_query: bool, *args):
        global afg31000_logger
        cmd_str = cmd + ('? ' if b_query else ' ') + \
                  ','.join([str(arg) for arg in args if arg is not None]) + \
                  (self.com_end if self.com_mode == 'rs232' else '')

        cmd_str_replaced = cmd_str.replace("\r", "\\r").replace("\n", "\\n")
        afg31000_logger.debug(f"Sending command <{cmd_str_replaced}>", extra={"component": "AFG31000"})

        if self.com_mode == 'rs232':
            with self.ser_lock:
                self.ser.write(cmd_str.encode('ascii'))
                if b_query:
                    ans = self.ser.read_until(terminator=self.com_end.encode('ascii')).decode('ascii')
                    ans_replaced = ans.replace("\r", "\\r")
                    afg31000_logger.debug(f"Got answer: <{ans_replaced}>", extra={"component": "AFG31000"})
                    return ans
                else:
                    return None
        elif self.com_mode == 'gpib':
            if b_query:
                return self.visa_inst.query(cmd_str)
            else:
                self.visa_inst.write(cmd_str)

    def ref_phase_shift(self, b_query: bool = True, x: float = None):
        if AFG31000Man._FAKE_DEV:
            return np.random.rand(1)[0]

        res = self.send_cmd("PHAS", b_query, x)
        if b_query:
            return float(res)

    REF_SOURCE_INTERNAL = 1
    REF_SOURCE_EXTERNAL = 0

    def ref_source(self, b_query: bool = True, i: int = None):
        if AFG31000Man._FAKE_DEV:
            return 1

        res = self.send_cmd("FMOD", b_query, i)
        if b_query:
            return int(res)

    def ref_frequency(self, b_query: bool = True, f: float = None):
        if AFG31000Man._FAKE_DEV:
            return 1000

        res = self.send_cmd("FREQ", b_query, f)
        if b_query:
            return float(res)

    REF_TRIGGER_SLOPE2SINE = 0
    REF_TRIGGER_TTL_RISING = 1
    REF_TRIGGER_TTL_FALLING = 2

    def ref_trigger(self, b_query: bool = True, i: int = None):
        res = self.send_cmd("RSLP", b_query, i)
        if b_query:
            return int(res)

    def detection_harmonic(self, b_query: bool = True, i: int = None):
        """1 <= i <= 19999 and i*f <= 102kHz"""
        res = self.send_cmd("HARM", b_query, i)
        if b_query:
            return int(res)

    def sine_output_amp(self, b_query: bool = True, x: float = None):
        """0.004 <= x <= 5.000"""
        res = self.send_cmd("SLVL", b_query, x)
        if b_query:
            return float(res)

    INPUT_CFG_A = 0
    INPUT_CFG_A_B = 1
    INPUT_CFG_I_1M_OHM = 2
    INPUT_CFG_I_100M_OHM = 3

    def input_config(self, b_query: bool = True, i: int = None):
        res = self.send_cmd("ISRC", b_query, i)
        if b_query:
            return int(res)

    INPUT_SHIELD_GND_FLOAT = 0
    INPUT_SHIELD_GND_GROUND = 1

    def input_shield_gnd(self, b_query: bool = True, i: int = None):
        res = self.send_cmd("IGND", b_query, i)
        if b_query:
            return int(res)

    INPUT_COUPLING_AC = 0
    INPUT_COUPLING_DC = 1

    def input_coupling(self, b_query: bool = True, i: int = None):
        res = self.send_cmd("ICPL", b_query, i)
        if b_query:
            return int(res)

    LINE_NOTCH_FILTERS_OUT = 0
    LINE_NOTCH_FILTERS_LINEIN = 1
    LINE_NOTCH_FILTERS_2XLINEIN = 2
    LINE_NOTCH_FILTERS_BOTHIN = 3

    def line_notch_filters(self, b_query: bool = True, i: int = None):
        res = self.send_cmd("ILIN", b_query, i)
        if b_query:
            return int(res)

    SENSITIVITY_LST = ("2 nV/fA", "5 nV/fA", "10 nV/fA", "20 nV/fA",
                       "50 nV/fA", "100 nV/fA", "200 nV/fA", "500 nV/fA",
                       "1 uV/pA", "2 uV/pA", "5 uV/pA", "10 uV/pA", "20 uV/pA",
                       "50 uV/pA", "100 uV/pA", "200 uV/pA", "500 uV/pA",
                       "1 mV/nA", "2 mV/nA", "5 mV/nA", "10 mV/nA",
                       "20 mV/nA", "50 mV/nA", "100 mV/nA", "200 mV/nA", "500 mV/nA", "1 V/uA")

    @staticmethod
    def sensitivity_str2int(sens: str):
        if sens not in AFG31000Man.SENSITIVITY_LST:
            return None
        else:
            return AFG31000Man.SENSITIVITY_LST.index(sens)

    @staticmethod
    def sensitivity_int2str(sens_i: int):
        if 0 <= sens_i < len(AFG31000Man.SENSITIVITY_LST):
            return AFG31000Man.SENSITIVITY_LST[sens_i]
        else:
            return None

    def sensitivity(self, b_query: bool = True, i: int = None):
        """ 2nV (0) <= i <= 1V (26)"""
        if AFG31000Man._FAKE_DEV:
            return 4

        res = self.send_cmd("SENS", b_query, i)
        if b_query:
            return int(res)

    DYN_RESERVE_MODE_HIGHRESERVE = 0
    DYN_RESERVE_MODE_NORMAL = 1
    DYN_RESERVE_MODE_LOWNOISE = 2

    def dyn_reserve_mode(self, b_query: bool = True, i: int = None):
        res = self.send_cmd("RMOD", b_query, i)
        if b_query:
            return int(res)

    TIME_CONSTANT_LST = ("10 us", "30 us", "100 us", "300 us", "1 ms",
                         "3 ms", "10 ms", "30 ms", "100 ms", "300 ms",
                         "1 s", "3 s", "10 s", "30 s", "100 s",
                         "300 s", "1 ks", "3 ks", "10 ks", "30 ks")

    @staticmethod
    def time_constant_str2int(tcons: str):
        if tcons not in AFG31000Man.TIME_CONSTANT_LST:
            return None
        else:
            return AFG31000Man.TIME_CONSTANT_LST.index(tcons)

    @staticmethod
    def time_constant_int2str(tcons_i: int):
        if 0 <= tcons_i < len(AFG31000Man.TIME_CONSTANT_LST):
            return AFG31000Man.TIME_CONSTANT_LST[tcons_i]
        else:
            return None

    def time_constant(self, b_query: bool = True, i: int = None):
        """
        use AFG31000Man.time_constant_str2int, and AFG31000Man.time_constant_int2str
        for the parameter
        """
        if AFG31000Man._FAKE_DEV:
            return 5

        res = self.send_cmd("OFLT", b_query, i)
        if b_query:
            return int(res)

    LOW_PASS_FILTER_SLOPE_6DB_OCT = 0
    LOW_PASS_FILTER_SLOPE_12DB_OCT = 1
    LOW_PASS_FILTER_SLOPE_18DB_OCT = 2
    LOW_PASS_FILTER_SLOPE_24DB_OCT = 3

    def low_pass_filter_slope(self, b_query: bool = True, i: int = None):
        res = self.send_cmd("OFSL", b_query, i)
        if b_query:
            return int(res)

    SYNC_FILTER_OFF = 0
    SYNC_FILTER_ON_BELOW_200HZ = 1

    def sync_filter(self, b_query: bool = True, i: int = None):
        res = self.send_cmd("SYNC", b_query, i)
        if b_query:
            return int(res)

    DISPLAY_CH_CH1 = 1
    DISPLAY_CH_CH2 = 2
    DISPLAY_CH_DIS_XY = 0
    DISPLAY_CH_DIS_R_THETA = 1
    DISPLAY_CH_DIS_XNYN = 2
    DISPLAY_CH_DIS_AUX1_3 = 3
    DISPLAY_CH_DIS_AUX2_4 = 4
    DISPLAY_CH_RATIO_DIS_NONE = 0
    DISPLAY_CH_RATIO_DIS_AUX1_3 = 1
    DISPLAY_CH_RATIO_DIS_AUX2_4 = 2

    def display_ch1_2(self, ch: int, b_query: bool = True, dis: int = None, ratio_dis: int = None):
        res = self.send_cmd("DDEF", b_query, ch, dis, ratio_dis)
        if b_query:
            return [int(x) for x in res.split(",") if x != '']

    OUTPUT_SOURCE_CH_CH1 = 1
    OUTPUT_SOURCE_CH_CH2 = 2
    OUTPUT_SOURCE_DIS_X_Y = 1
    OUTPUT_SOURCE_DIS_DISPLAY = 0

    def output_source(self, ch: int, b_query: bool = True, dis: int = None):
        res = self.send_cmd("FPOP", b_query, ch, dis)
        if b_query:
            return int(res)

    OFFSET_EXPAND_AXIS_X = 1
    OFFSET_EXPAND_AXIS_Y = 2
    OFFSET_EXPAND_AXIS_R = 3
    OFFSET_EXPAND_EXPAND1 = 0
    OFFSET_EXPAND_EXPAND10 = 1
    OFFSET_EXPAND_EXPAND100 = 2

    def offset_expand(self, axis: int, b_query: bool = True, offset_percent: float = None, expand: int = None):
        """ -105.00 <= offset_percent <= 105.00"""
        res = self.send_cmd("OEXP", b_query, axis, offset_percent, expand)
        if b_query:
            res_part = res.split(",")
            return [float(res_part[0]), int(res_part[1])]

    AUTO_OFFSET_AXIS_X = 1
    AUTO_OFFSET_AXIS_Y = 2
    AUTO_OFFSET_AXIS_R = 3

    def auto_offset(self, axis: int):
        self.send_cmd("AOFF", False, axis)

    def get_aux_input(self, which: int):
        """
        Get AUX input voltage
        :param which: [1,4] Aux Input
        :return Aux input voltage in Volts, 1/3mV resolution
        """
        res = self.send_cmd("OAUX", True, which)
        return float(res)

    def aux_output_voltage(self, which: int, b_query: bool = True, vols: float = None):
        """
        Set or query AUX output voltage
        :param which: [1,4]
        :param b_query:
        :param vols: output voltage in Volts (nearest mV)
        :return: if b_query then return output voltage
        """
        """ -10.5 <= vols <= 10.5"""
        res = self.send_cmd("AUXV", b_query, which, vols)
        if b_query:
            return float(res)

    OUTPUT_INTERFACE_RS232 = 0
    OUTPUT_INTERFACE_GPIB = 1

    def output_interface(self, b_query: bool = True, i: int = None):
        res = self.send_cmd("OUTX", b_query, i)
        if b_query:
            return int(res)

    GPIB_OVERRIDE_REMOTE_STATE_OFF = 0
    GPIB_OVERRIDE_REMOTE_STATE_ON = 1

    def gpib_override_remote_state(self, b_query: bool = True, i: int = None):
        res = self.send_cmd("OVRM", b_query, i)
        if b_query:
            return int(res)

    KEY_CLICK_OFF = 0
    KEY_CLICK_ON = 1

    def key_click(self, b_query: bool = True, i: int = None):
        res = self.send_cmd("KCLK", b_query, i)
        if b_query:
            return int(res)

    ALARMS_OFF = 0
    ALARMS_ON = 1

    def alarms(self, b_query: bool = True, i: int = None):
        res = self.send_cmd("ALRM", b_query, i)
        if b_query:
            return int(res)

    def save_cur_setup(self, i: int):
        self.send_cmd("SSET", False, i)

    def load_setup(self, i: int):
        self.send_cmd("RSET", False, i)

    def auto_gain(self):
        self.send_cmd("AGAN", False)

    def auto_reserve(self):
        self.send_cmd("ARSV", False)

    def auto_phase(self):
        self.send_cmd("APHS", False)

    DATA_SAMPLE_RATE_LST = ("62.5 mHz", "125 mHz", "250 mHz", "500 mHz",
                            "1 Hz", "2 Hz", "4 Hz", "8 Hz", "16 Hz",
                            "32 Hz", "64 Hz", "128 Hz", "256 Hz",
                            "512 Hz", "Trigger")

    @staticmethod
    def data_sample_rate_str2int(srt: str):
        if srt not in AFG31000Man.DATA_SAMPLE_RATE_LST:
            return None
        else:
            return AFG31000Man.DATA_SAMPLE_RATE_LST.index(srt)

    @staticmethod
    def data_sample_rate_int2str(srt_i: int):
        if 0 <= srt_i < len(AFG31000Man.DATA_SAMPLE_RATE_LST):
            return AFG31000Man.DATA_SAMPLE_RATE_LST[srt_i]
        else:
            return None

    def data_sample_rate(self, b_query: bool = True, i: int = None):
        """62.5mHz (0) <= i <= 512Hz (13) / Tigger (14)"""
        res = self.send_cmd("SRAT", b_query, i)
        if b_query:
            return int(res)

    DATA_SCAN_MODE_SHOT = 0
    DATA_SCAN_MODE_LOOP = 1

    def data_scan_mode(self, b_query: bool = True, i: int = None):
        res = self.send_cmd("SEND", b_query, i)
        if b_query:
            return int(res)

    def trigger(self):
        self.send_cmd("TRIG", False)

    TRIGGER_STARTS_SCAN_NO = 0
    TRIGGER_STARTS_SCAN_YES = 1

    def trigger_starts_can(self, b_query: bool = True, i: int = None):
        res = self.send_cmd("TSTR", b_query, i)
        if b_query:
            return int(res)

    def start_scan(self):
        self.send_cmd("STRT", False)

    def pause_scan(self):
        self.send_cmd("PAUS", False)

    def reset_scan(self):
        self.send_cmd("REST", False)

    GET_AXIS_VALUE_X = 1
    GET_AXIS_VALUE_Y = 2
    GET_AXIS_VALUE_R = 3
    GET_AXIS_VALUE_THETA = 4

    def get_axis_value(self, which: int):
        if AFG31000Man._FAKE_DEV:
            return np.random.rand(1)[0] + which

        res = float(self.send_cmd("OUTP", True, which))
        self.axis_value_changed.emit(which, res)
        return res

    GET_DISPLAY_VALUE_1 = 1
    GET_DISPLAY_VALUE_2 = 2

    def get_display_value(self, which: int):
        res = self.send_cmd("OUTR", True, which)
        return float(res)

    GET_PARAMETER_X = 1
    GET_PARAMETER_Y = 2
    GET_PARAMETER_R = 3
    GET_PARAMETER_THETA = 4
    GET_PARAMETER_AUX_IN1 = 5
    GET_PARAMETER_AUX_IN2 = 6
    GET_PARAMETER_AUX_IN3 = 7
    GET_PARAMETER_AUX_IN4 = 8
    GET_PARAMETER_REF_FREQ = 9
    GET_PARAMETER_CH1_DISPLAY = 10
    GET_PARAMETER_CH2_DISPLAY = 11

    def get_parameters_value(self, i: int, j: int, k: int = None, l: int = None, m: int = None, n: int = None):
        res = self.send_cmd("SNAP", True, i, j, k, l, m, n)
        values = [float(x) for x in res.split(",") if x != '']
        axes = [wh for wh in (i,j,k,l,m,n) if wh is not None]
        for index in range(0, len(axes)):
            self.axis_value_changed.emit(axes[index], values[index])
        return values

    def get_number_in_display_buffer(self):
        res = self.send_cmd("SPTS", True)
        return int(res)

    def get_points_ascii(self, dis: int, start_index: int, n_points: int):
        res = self.send_cmd("TRCA", True, dis, start_index, n_points)
        return [float(x) for x in res.split(",") if x != '']

    def get_points_ieee_float(self, dis: int, start_index: int, n_points: int):
        cmd_str = f'TRCB? {dis},{start_index},{n_points}' + (self.com_end if self.com_mode == 'rs232' else '')

        if self.com_mode == 'rs232':
            self.ser.write(cmd_str.encode('ascii'))
            raw_bytes = self.ser.read(n_points * 4)
        elif self.com_mode == 'gpib':
            raw_bytes = self.visa_inst.read_raw()
        else:
            raw_bytes = b''
        
        res = np.frombuffer(raw_bytes, dtype='<f4')
        return res

    @staticmethod
    def non_normalized_float_from_bytes(raw_bytes: bytes):
        values = []
        for i in range(0, len(raw_bytes)-3, 4):
            mantissa = np.frombuffer(raw_bytes[i:i+2], dtype='<i2')[0]
            exp = raw_bytes[i+2]
            byte3 = raw_bytes[i+3]   # should always be 0
            values.append(mantissa * pow(2, exp-124))

        return values

    def get_points_binary_float(self, dis: int, start_index: int, n_points: int):
        cmd_str = f'TRCL? {dis},{start_index},{n_points}' + (self.com_end if self.com_mode == 'rs232' else '')
        if self.com_mode == 'rs232':
            self.ser.write(cmd_str.encode('ascii'))
            raw_bytes = self.ser.read(n_points * 4)
        elif self.com_mode == 'gpib':
            raw_bytes = self.visa_inst.read_raw()
        else:
            raw_bytes = b''
        
        return AFG31000Man.non_normalized_float_from_bytes(raw_bytes)

    FAST_DATA_TRANSFER_MODE_ON = 1
    FAST_DATA_TRANSFER_MODE_OFF = 0

    def fast_data_transfer_mode(self, b_query: bool = True, i: int = None):
        res = self.send_cmd("FAST", b_query, i)
        if b_query:
            return int(res)

    def start_scan_500ms_delay(self):
        self.send_cmd("STRD", False)

    def reset_default_config(self):
        self.send_cmd("*RST", False)

    def get_device_id(self):
        return self.send_cmd("*IDN", True).decode('ascii')

    LOCAL_REMOTE_STATE_LOCAL = 0
    LOCAL_REMOTE_STATE_REMOTE = 1
    LOCAL_REMOTE_STATE_LOCAL_LOCKOUT = 2

    def local_remote_state(self, b_query: bool = True, i: int = None):
        res = self.send_cmd("LOCL", b_query, i)
        if b_query:
            return int(res)

    def clear_status(self):
        """
        Clears all status register, status enable register is not cleared
        :return:
        """
        self.send_cmd("*CLS", False)

    STANDARD_EVENT_STATUS_INP = 0
    STANDARD_EVENT_STATUS_QRY = 2
    STANDARD_EVENT_STATUS_EXE = 4
    STANDARD_EVENT_STATUS_CMD = 5
    STANDARD_EVENT_STATUS_URQ = 6
    STANDARD_EVENT_STATUS_PON = 7

    def standard_event_status_enable(self, b_query: bool = True, i: int = None, j: int = None):
        res = self.send_cmd("*ESE", b_query, i, j)
        if b_query:
            return int(res)

    def standard_event_status(self, i: int = None):
        res = self.send_cmd("*ESR", True, i)
        return int(res)

    def is_command_queue_overflow(self):
        return True if self.standard_event_status(AFG31000Man.STANDARD_EVENT_STATUS_INP) == 1 else False

    def is_command_output_overflow(self):
        return True if self.standard_event_status(AFG31000Man.STANDARD_EVENT_STATUS_QRY) == 1 else False

    def is_command_cannot_execute(self):
        return True if self.standard_event_status(AFG31000Man.STANDARD_EVENT_STATUS_EXE) == 1 else False

    def is_command_illegal(self):
        return True if self.standard_event_status(AFG31000Man.STANDARD_EVENT_STATUS_CMD) == 1 else False

    SERIAL_POLL_STATUS_SCN = 0
    SERIAL_POLL_STATUS_IFC = 1
    SERIAL_POLL_STATUS_ERR = 2
    SERIAL_POLL_STATUS_LIA = 3
    SERIAL_POLL_STATUS_MAV = 4
    SERIAL_POLL_STATUS_ESB = 5
    SERIAL_POLL_STATUS_SRQ = 6

    def serial_poll_enable(self, b_query: bool = True, i: int = None, j: int = None):
        res = self.send_cmd("*SRE", b_query, i, j)
        if b_query:
            return int(res)

    def serial_poll_status(self, i: int = None):
        res = self.send_cmd("*STB", True, i)
        return int(res)

    def is_no_scan_in_progress(self):
        return True if self.serial_poll_status(AFG31000Man.SERIAL_POLL_STATUS_SCN) == 1 else False

    POWER_ON_STATUS_CLEAR_SET = 1
    POWER_ON_STATUS_CLEAR_CLEAR = 0

    def power_on_status_clear(self, b_query: bool = True, i: int = None):
        res = self.send_cmd("*PSC", b_query, i)
        if b_query:
            return int(res)

    ERROR_STATUS_BACKUP = 1
    ERROR_STATUS_RAM = 2
    ERROR_STATUS_ROM = 4
    ERROR_STATUS_GPIB = 5
    ERROR_STATUS_DSP = 6
    ERROR_STATUS_MATH = 7

    def error_status_enable(self, b_query: bool = True, i: int = None, j: int = None):
        res = self.send_cmd("ERRE", b_query, i, j)
        if b_query:
            return int(res)

    def error_status(self, i: int = None):
        res = self.send_cmd("ERRS", True, i)
        return int(res)

    LIA_STATUS_RSRV_INPT = 0
    LIA_STATUS_FILTR = 1
    LIA_STATUS_OUTPT = 2
    LIA_STATUS_UNLK = 3
    LIA_STATUS_RANGE = 4
    LIA_STATUS_TC = 5
    LIA_STATUS_TRIG = 6

    def lia_status_enable(self, b_query: bool = True, i: int = None, j: int = None):
        res = self.send_cmd("LIAE", b_query, i, j)
        if b_query:
            return int(res)

    def lia_status(self, i: int = None):
        res = self.send_cmd("LIAS", True, i)
        return int(res)

    def is_input_amp_overload(self):
        return True if self.lia_status(AFG31000Man.LIA_STATUS_RSRV_INPT) == 1 else False

    def is_time_constant_filter_overload(self):
        return True if self.lia_status(AFG31000Man.LIA_STATUS_FILTR) == 1 else False

    def is_output_overloaded(self):
        return True if self.lia_status(AFG31000Man.LIA_STATUS_OUTPT) == 1 else False

    def is_reference_unlocked(self):
        return True if self.lia_status(AFG31000Man.LIA_STATUS_UNLK) == 1 else False

    def is_freq_out_of_range(self):
        return True if self.lia_status(AFG31000Man.LIA_STATUS_RANGE) == 1 else False

    def is_time_constant_changed(self):
        return True if self.lia_status(AFG31000Man.LIA_STATUS_TC) == 1 else False

    def is_triggered(self):
        return True if self.lia_status(AFG31000Man.LIA_STATUS_TRIG) == 1 else False

    def show_config_window(self):
        if self.config_window is None:
            self.config_window = AFG31000ConfigWindow(self)

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


class AFG31000ConfigWindow(Ui_AFG31000_Config_Window):
    """
        AFG31000 Helper class with configuration window
    """
    def __init__(self, afg31000man: AFG31000Man):
        self.afg31000man = afg31000man
        self.window = QWidget()
        Ui_AFG31000_Config_Window.__init__(self)
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

        # AFG31000 Settings
        self.comboBox_TimeConstant.currentTextChanged.connect(
            lambda t: self.afg31000man.time_constant(False, AFG31000Man.time_constant_str2int(t)))
        self.comboBox_Sensitivity.currentTextChanged.connect(
            lambda t: self.afg31000man.sensitivity(False, AFG31000Man.sensitivity_str2int(t)))
        self.pushButton_SetHarmonic.clicked.connect(
            lambda: self.afg31000man.detection_harmonic(False, self.spinBox_Harmonic.value()))
        self.comboBox_FilterSlope.currentIndexChanged.connect(
            lambda i: self.afg31000man.low_pass_filter_slope(False, i))

        self.pushButton_GetX.clicked.connect(
            lambda: self.lineEdit_X.setText(float2str(self.afg31000man.get_axis_value(AFG31000Man.GET_AXIS_VALUE_X)))
        )
        self.pushButton_GetY.clicked.connect(
            lambda: self.lineEdit_Y.setText(float2str(self.afg31000man.get_axis_value(AFG31000Man.GET_AXIS_VALUE_Y)))
        )
        self.pushButton_GetR.clicked.connect(
            lambda: self.lineEdit_R.setText(float2str(self.afg31000man.get_axis_value(AFG31000Man.GET_AXIS_VALUE_R)))
        )
        self.pushButton_GetTheta.clicked.connect(
            lambda: self.lineEdit_Theta.setText(float2str(self.afg31000man.get_axis_value(AFG31000Man.GET_AXIS_VALUE_THETA)))
        )
        self.pushButton_GetAll.clicked.connect(self.snap_all_values)

        self.lineEdit_phase.setValidator(
            # FIXME: validation
            QDoubleValidator(bottom=0.0, top=99.99, decimals=6))
        self.pushButton_SetPhase.clicked.connect(self.set_phase_clicked)
        self.pushButton_Autophase.clicked.connect(
            lambda: self.lineEdit_phase.setText(f"{self.afg31000man.ref_phase_shift(True):.4f}"))
        self.radioButton_ref_src_external.toggled.connect(self.ref_src_changed)
        self.radioButton_ref_src_internal.toggled.connect(self.ref_src_changed)

        self.interface_changed()

    def snap_all_values(self):
        x, y, r, theta, f = self.afg31000man.get_parameters_value(AFG31000Man.GET_PARAMETER_X,
                                                               AFG31000Man.GET_PARAMETER_Y,
                                                               AFG31000Man.GET_PARAMETER_R,
                                                               AFG31000Man.GET_PARAMETER_THETA,
                                                               AFG31000Man.GET_PARAMETER_REF_FREQ)
        self.lineEdit_X.setText(float2str(x))
        self.lineEdit_Y.setText(float2str(y))
        self.lineEdit_R.setText(float2str(r))
        self.lineEdit_Theta.setText(float2str(theta))
        self.lineEdit_Frequency.setText(f"{f:.6f}")

    def interface_changed(self):
        if self.radioButton_Interf_RS232.isChecked():
            self.radioButton_Interf_GPIB.setChecked(False)
            self.comboBox_COM_Parity.setEnabled(True)
            self.comboBox_COM_BaudRate.setEnabled(True)
            self.afg31000man.com_mode = 'rs232'

        if self.radioButton_Interf_GPIB.isChecked():
            self.radioButton_Interf_RS232.setChecked(False)
            self.comboBox_COM_Parity.setEnabled(False)
            self.comboBox_COM_BaudRate.setEnabled(False)
            self.afg31000man.com_mode = 'gpib'

        self.refresh_comlist()

    def ref_src_changed(self):
        if self.radioButton_ref_src_external.isChecked():
            self.radioButton_ref_src_internal.setChecked(False)
            self.afg31000man.ref_source(False, AFG31000Man.REF_SOURCE_EXTERNAL)
            self.pushButton_SetFrequency.setEnabled(False)
            self.lineEdit_Frequency.setText(f"{self.afg31000man.ref_frequency(True): .6f}")

        if self.radioButton_ref_src_internal.isChecked():
            self.radioButton_ref_src_external.setChecked(False)
            self.afg31000man.ref_source(False, AFG31000Man.REF_SOURCE_INTERNAL)
            self.lineEdit_Frequency.setText(f"{self.afg31000man.ref_frequency(True): .6f}")
            self.pushButton_SetFrequency.setEnabled(True)

    def set_phase_clicked(self):
        try:
            if not self.lineEdit_phase.hasAcceptableInput():
                raise ValueError("Not acceptable phase value")
            new_phase = float(self.lineEdit_phase.text())
            self.afg31000man.ref_phase_shift(False, new_phase)
            self.pushButton_SetPhase.setStyleSheet("background: green")
        except ValueError as ve:
            self.pushButton_SetPhase.setStyleSheet("background: red")
            self.lineEdit_phase.setText(f"{self.afg31000man.ref_phase_shift(True):.4f}")

    def sync_current_settings(self):
        if self.afg31000man is not None:
            self.comboBox_TimeConstant.setCurrentText(
                AFG31000Man.time_constant_int2str(self.afg31000man.time_constant(True)))
            self.comboBox_Sensitivity.setCurrentText(
                AFG31000Man.sensitivity_int2str(self.afg31000man.sensitivity(True)))
            self.comboBox_FilterSlope.setCurrentIndex(self.afg31000man.low_pass_filter_slope(True))
            self.lineEdit_phase.setText(f"{self.afg31000man.ref_phase_shift(True):.4f}")
            if self.afg31000man.ref_source(True) == 1:
                self.radioButton_ref_src_internal.setChecked(True)
                self.radioButton_ref_src_external.setChecked(False)
            else:
                self.radioButton_ref_src_internal.setChecked(False)
                self.radioButton_ref_src_external.setChecked(True)
            self.ref_src_changed()
            self.spinBox_Harmonic.setValue(self.afg31000man.detection_harmonic(True))
            self.snap_all_values()

    def conn_changed(self, i: int):
        if self.radioButton_Interf_RS232.isChecked():
            self.afg31000man.com_dev = self.comboBox_CONN.currentData()
        elif self.radioButton_Interf_GPIB.isChecked():
            self.afg31000man.visa_dev = self.comboBox_CONN.currentText()

    def parity_changed(self, p: str):
        if p == 'None':
            self.afg31000man.ser_parity = serial.PARITY_NONE
        elif p == 'ODD':
            self.afg31000man.ser_parity = serial.PARITY_ODD
        elif p == 'EVEN':
            self.afg31000man.ser_parity = serial.PARITY_EVEN
        else:
            raise ValueError(f"Unknown parity {p}")

    def baudrate_changed(self, b: int or str):
        if type(b) is str:
            b = int(b)
        self.afg31000man.ser_baudrate = b

    def refresh_comlist(self):
        self.comboBox_CONN.clear()
        if self.radioButton_Interf_RS232.isChecked():
            com_dict = get_available_COMs()
            for com_dev in com_dict.keys():
                self.comboBox_CONN.addItem(com_dev + ':' + com_dict[com_dev], com_dev)
        elif self.radioButton_Interf_GPIB.isChecked():
            self.comboBox_CONN.addItems(self.afg31000man.visa_rm.list_resources())

    def open_conn_clicked(self, state):
        if not state:  # post event state
            self.close_conn()
        else:
            # FIXME: Actually open connection
            self.open_conn()

    def open_conn(self):
        global afg31000_logger
        try:
            self.afg31000man.open()
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
            afg31000_logger.info(f"AFG31000 COM connection opened", extra={"component": "AFG31000"})
            if self.radioButton_Interf_RS232.isChecked():
                afg31000_logger.debug(f"AFG31000 COM: {self.afg31000man.com_dev} "
                                   f"B:{self.afg31000man.ser_baudrate} "
                                   f"P:{self.afg31000man.ser_parity} "
                                   f"S:{self.afg31000man.ser_stopbits}", extra={"component": "AFG31000"})
            else:
                afg31000_logger.debug(f"AFG31000 Visa addr:: {self.afg31000man.visa_dev} ", extra={"component": "AFG31000"})
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            afg31000_logger.error(f"Failed to open AFG31000 COM connection", extra={"component": "AFG31000"})
            self.close_conn()

    def close_conn(self):
        global afg31000_logger
        self.afg31000man.close()
        # FIXME: stop all the AFG31000 update activities
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
        afg31000_logger.info(f"AFG31000 COM connection closed", extra={"component": "AFG31000"})

    def show(self):
        self.window.show()

    def close(self):
        self.window.hide()

    def get_current_settings(self, with_header: bool = True):
        if self.afg31000man.is_open():
            if with_header:
                setting_str = "--------SRS AFG31000-------\n"
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

    afg31000_man = AFG31000Man()
    print(f'Starting...')
    afg31000_man.show_config_window()
    QApplication.instance().exec_()
