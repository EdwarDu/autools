#!/usr/bin/env python3

import re
from threading import Lock
from typing import Callable
import numpy as np

import serial
import serial.tools.list_ports
import logging
from PyQt5.QtCore import QObject, pyqtSignal


_SPLIT_LOG = False

if _SPLIT_LOG:
    piezo_logger = logging.getLogger("piezo")
else:
    piezo_logger = logging.getLogger("autools_setup_main")


class PiezoGCSCom(QObject):
    """
    Helper (man) Class for communicate with Piezo with PI GCS protocol
    WARNING: NO CONFIRMATION ON ANY DEVICE YET
    """

    COMM_MODE = 'rs232'
    COMMAND_END = '\n' if COMM_MODE == 'rs232' else '\r'

    _FAKE_DEV = False

    opened = pyqtSignal()
    closed = pyqtSignal()
    axis_position_changed = pyqtSignal(dict, name="axisPositionChanged")

    def __init__(self, serial_name=None, baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                 uart_lock=None):
        super().__init__()
        self.com_dev = serial_name
        self.ser_baudrate = baudrate
        self.ser_parity = parity
        self.ser_stopbits = stopbits

        if self.com_dev is None:
            self.ser = None
        else:
            self.ser = serial.Serial(port=self.com_dev,
                                     baudrate=self.ser_baudrate,
                                     bytesize=serial.EIGHTBITS,
                                     parity=self.ser_parity,
                                     stopbits=self.ser_stopbits)
            self.ser.inter_byte_timeout = 0.1  # when device failed to send next byte within 0.1 read will exit

            if not self.ser.is_open:
                raise IOError(f'Failed to open {self.com_dev}')
            else:
                self.opened.emit()

        if uart_lock is None:
            self.ser_lock = Lock()
        else:
            self.ser_lock = uart_lock

        self.quiet = False

    def open(self):
        if self.ser is not None and self.ser.is_open:
            self.ser.close()

        self.ser = serial.Serial(port=self.com_dev,
                                 baudrate=self.ser_baudrate,
                                 bytesize=serial.EIGHTBITS,
                                 parity=self.ser_parity,
                                 stopbits=self.ser_stopbits)
        self.ser.inter_byte_timeout = 0.1  # when device failed to send next byte within 0.1 read will exit

        if not self.ser.is_open:
            raise IOError(f'Failed to open {self.com_dev}')
        else:
            self.opened.emit()

    def close(self):
        if self.ser is not None and self.ser.is_open:
            self.ser.close()
        self.closed.emit()
        self.ser = None

    def is_open(self):
        return self.ser is not None and self.ser.is_open

    def send_cmd(self, cmd: str, b_query: bool, *args):
        global piezo_logger

        cmd_str = cmd + ('? ' if b_query else ' ') + \
                  ' '.join([f"{arg:.6f}" if type(arg) is float else str(arg) for arg in args if arg is not None]) + \
                  PiezoGCSCom.COMMAND_END
        cmd_str_replaced = cmd_str.replace("\n", "\\n")
        piezo_logger.debug(f"Sending command <{cmd_str_replaced}>", extra={"component": "PIEZO"})

        if PiezoGCSCom._FAKE_DEV:
            if not b_query:
                return

            if cmd == 'VOL' and b_query:
                ans_str = ""
                for arg in args:
                    ans_str += arg + "=" + str(np.random.random()) + PiezoGCSCom.COMMAND_END

                ans_replaced = ans_str.replace("\r", "\\r")
                piezo_logger.debug(f"Got answer <{ans_replaced}>", extra={"component": "PIEZO"})
                return ans_str
            elif cmd == 'POS' and b_query:
                ans_str = ""
                for arg in args:
                    ans_str += arg + "=" + str(np.random.random()) + PiezoGCSCom.COMMAND_END

                ans_replaced = ans_str.replace("\r", "\\r")
                piezo_logger.debug(f"Got answer <{ans_replaced}>", extra={"component": "PIEZO"})
                return ans_str
            elif cmd == "TMN" and b_query:
                ans_str = ""
                for arg in args:
                    ans_str += arg + "=" + str(0.0) + PiezoGCSCom.COMMAND_END

                ans_replaced = ans_str.replace("\r", "\\r")
                piezo_logger.debug(f"Got answer <{ans_replaced}>", extra={"component": "PIEZO"})
                return ans_str
            elif cmd == "TMX" and b_query:
                ans_str = ""
                for arg in args:
                    ans_str += arg + "=" + str(100.0) + PiezoGCSCom.COMMAND_END

                ans_replaced = ans_str.replace("\r", "\\r")
                piezo_logger.debug(f"Got answer <{ans_replaced}>", extra={"component": "PIEZO"})
                return ans_str
            elif cmd == "ONL" and b_query:
                ans_str = ""
                for arg in args:
                    ans_str += arg + "=1" + PiezoGCSCom.COMMAND_END

                ans_replaced = ans_str.replace("\r", "\\r")
                piezo_logger.debug(f"Got answer <{ans_replaced}>", extra={"component": "PIEZO"})
                return ans_str
            elif cmd == "SVO" and b_query:
                ans_str = ""
                for arg in args:
                    ans_str += arg + "=1" + PiezoGCSCom.COMMAND_END

                ans_replaced = ans_str.replace("\r", "\\r")
                piezo_logger.debug(f"Got answer <{ans_replaced}>", extra={"component": "PIEZO"})
                return ans_str
            elif cmd == "VMA" and b_query:
                ans_str = ""
                for arg in args:
                    ans_str += arg + "=100" + PiezoGCSCom.COMMAND_END

                ans_replaced = ans_str.replace("\r", "\\r")
                piezo_logger.debug(f"Got answer <{ans_replaced}>", extra={"component": "PIEZO"})
                return ans_str
            elif cmd == "VMI" and b_query:
                ans_str = ""
                for arg in args:
                    ans_str += arg + "=0" + PiezoGCSCom.COMMAND_END

                ans_replaced = ans_str.replace("\r", "\\r")
                piezo_logger.debug(f"Got answer <{ans_replaced}>", extra={"component": "PIEZO"})
                return ans_str

        with self.ser_lock:
            self.ser.write(cmd_str.encode('utf-8'))
            if b_query:
                ans = ""
                while True:
                    ans_line = self.ser.read_until(terminator=PiezoGCSCom.COMMAND_END.encode('utf-8')).decode('utf-8')
                    ans += ans_line
                    if ans_line[-2] != ' ':
                        break
                ans_replaced = ans.replace("\r", "\\r")
                piezo_logger.debug(f"Got answer <{ans_replaced}>", extra={"component": "PIEZO"})
                return ans
            else:
                return None

    def send_fast_polling_cmd(self, cmd: bytes or bytearray, b_query: bool):
        with self.ser_lock:
            self.ser.write(cmd)
            if b_query:
                return self.ser.read_until(terminator=PiezoGCSCom.COMMAND_END.encode('utf-8'))
            else:
                return None

    def is_axes_moving(self):
        ans = int(self.send_fast_polling_cmd(b'\x05', True))
        axis1_moving = (ans & 0x01) != 0
        axis2_moving = (ans & 0x02) != 0
        axis3_moving = (ans & 0x04) != 0

        return axis1_moving, axis2_moving, axis3_moving

    def is_axes_position_changed(self):
        ans = int(self.send_fast_polling_cmd(b'\x06', True))
        axis1_moved = (ans & 0x01) != 0
        axis2_moved = (ans & 0x02) != 0
        axis3_moved = (ans & 0x04) != 0

        return axis1_moved, axis2_moved, axis3_moved

    def is_controller_ready(self):
        ans = int(self.send_fast_polling_cmd(b'\x07', True))
        if ans == 0xB1:
            return True
        elif ans == 0xB0:
            return False
        else:
            raise ValueError(f"Controller Ready? Wrong ans {ans}")

    def is_running_macro(self):
        ans = int(self.send_fast_polling_cmd(b'\x08', True))
        if ans == 0:
            return False
        elif ans == 1:
            return True
        else:
            raise ValueError(f"Running Macro? Wrong ans {ans}")

    def is_wave_generators_running(self):
        ans = int(self.send_fast_polling_cmd(b'\x09', True))
        wg1_running = (ans & 0x01) != 0
        wg2_running = (ans & 0x02) != 0
        wg3_running = (ans & 0x04) != 0

        return wg1_running, wg2_running, wg3_running

    def stop_all_axes(self):
        """
        Command: #24
        """
        self.send_fast_polling_cmd(b'\x18', False)

    def get_dev_id(self):
        return self.send_cmd("*IDN", True)

    @staticmethod
    def load_gcs_table(ans: str, gen_rec: Callable = None):
        ans_dict = {"DATA": []}
        for ans_line in re.split(PiezoGCSCom.COMMAND_END, ans):
            if ans_line.startswith("#"):
                ans_parts = [x for x in re.split("[#=\r]", ans_line) if x != ""]
                ans_key = ans_parts[0].strip()
                if ans_key == "TYPE":
                    ans_dict[ans_key] = int(ans_parts[1])
                elif ans_key == "SEPARATOR":
                    ans_dict[ans_key] = chr(int(ans_parts[1]))
                elif ans_key == "DIM":
                    ans_dict[ans_key] = int(ans_parts[1])
                elif ans_key == "SAMPLE_TIME":
                    ans_dict[ans_key] = float(ans_parts[1])
                elif ans_key == "NDATA":
                    ans_dict[ans_key] = int(ans_parts[1])
                elif len(ans_parts) == 2:
                    ans_dict[ans_key] = ans_parts[1].strip()
            else:
                ans_parts = [gen_rec(x) if gen_rec is not None else x
                             for x in re.split(f"[{ans_dict['SEPARATOR']}{PiezoGCSCom.COMMAND_END}]", ans_line)
                             if x != ""]
                ans_dict["DATA"].append(ans_parts)

        return ans_dict

    @staticmethod
    def load_ans_pairs(ans: str, delim="=", gen_left: Callable = None, gen_right: Callable = None):
        ans_dict = {}
        for ans_line in [x for x in re.split(f"{PiezoGCSCom.COMMAND_END}", ans) if x != '']:
            ans_left, ans_right = [x.strip() for x in re.split(delim, ans_line)]
            if gen_left is not None:
                ans_left = gen_left(ans_left)
            if gen_right is not None:
                ans_right = gen_right(ans_right)

            ans_dict[ans_left] = ans_right
        return ans_dict

    AUTO_CALIBRATION_COMPLETE = 1
    AUTO_CALIBRATION_SENSOR_MONITOR_ADC = 2
    AUTO_CALIBRATION_DAC_CONTROL_VOLTAGE = 3
    AUTO_CALIBRATION_SENSOR_INPUT_PI_CONTROLLER = 4
    AUTO_CALIBRATION_VOLTAGE_MONITOR_ADC = 5
    AUTO_CALIBRATION_MONITOR_VOLTAGE_AMPLIFIER = 6

    def start_auto_calibration(self, *ch_option_pairs):
        """
        :param ch_option_pairs: [(channel_id:str, option:int), ], channel_id: 1, 2, 3
        :return:
        """
        args = []
        for ch_option_pair in ch_option_pairs:
            args += ch_option_pair

        self.send_cmd('ATC', False, *args)

    def get_auto_calibration_settings(self, *ch_ids):
        """
        :param ch_ids: [channel_id:str, ]
        :return: [(channel_id:str, option:int),]
        """
        ans = self.send_cmd("ATC", True, *ch_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: int(x))

    def get_auto_calibration_status(self, *ch_option_pairs):
        """
        :param ch_option_pairs: [(channel_id:str, option:int), ], channel_id: 1, 2, 3
        :return: [[[channel_id:str, option:int], err:str], ], err: '0' no error
        """
        args = []
        for ch, option in ch_option_pairs:
            args.append(ch)
            args.append(option)

        ans = self.send_cmd("ATS", True, *args)
        ans_dec = PiezoGCSCom.load_ans_pairs(ans, gen_left=lambda s: re.findall(r'\S+', s))
        # Patch the option type to int
        for ans_key, ans_value in ans_dec.items():
            ans_dec[ans_key] = int(ans_value)
        return ans_dec

    def set_cmd_level(self, lvl: int, passwd: str = "advanced"):
        """
        :param lvl: command level: 0 or 1
        :param passwd: only required when lvl = 1
        :return:
        """
        if lvl == 0:
            self.send_cmd("CCL", False, 0)
        elif lvl == 1:
            self.send_cmd("CCL", False, 1, passwd)
        else:
            raise ValueError(f"Unsupported command level {lvl}")

    def get_cmd_level(self):
        return int(self.send_cmd("CCL", True))

    def set_syntax_version(self, version: str = "2.0"):
        """
        USE WITH CARE
        :param version:str: 1.0 or 2.0
        :return:
        """
        self.send_cmd("CSV", False, version)

    def get_syntax_version(self):
        """
        :return:str: 1.0 or 2.0
        """
        return self.send_cmd("CSV", True).strip()

    TRIGGER_OUT_CFG_ID_DIO1 = 1
    TRIGGER_OUT_CFG_ID_DIO2 = 2
    TRIGGER_OUT_CFG_ID_DIO3 = 3
    TRIGGER_OUT_CFG_CTOPAM_TRIGGER_STEP = 1
    # Value: StepSize default 0.1
    TRIGGER_OUT_CFG_CTOPAM_AXIS = 2
    TRIGGER_OUT_CFG_CTOPAM_TRIGGER_MODE = 3
    TRIGGER_OUT_CFG_TRIGGER_MODE_POS_DIST = 0
    # a trigger pulse is written whenever the axis has covered the Trigger Step distance
    TRIGGER_OUT_CFG_TRIGGER_MODE_ON_TARGET = 2
    # ref: ONT?
    TRIGGER_OUT_CFG_TRIGGER_MODE_MINMAX_THRESHOLD = 3
    TRIGGER_OUT_CFG_TRIGGER_MODE_GENERATOR = 4

    TRIGGER_OUT_CFG_CTOPAM_TRIGGER_DELAY = 4 # Always 0
    TRIGGER_OUT_CFG_CTOPAM_MIN_THRESHOLD = 5
    TRIGGER_OUT_CFG_CTOPAM_MAX_THRESHOLD = 6
    TRIGGER_OUT_CFG_CTOPAM_POLARITY = 7
    TRIGGER_OUT_CFG_POLARITY_ACTIVE_LOW = 0
    TRIGGER_OUT_CFG_POLARITY_ACTIVE_HIGH = 1

    def set_trigger_out_config(self, *trigoutid_ctopam_value_pairs):
        """
        :param trigoutid_ctopam_value_pairs: [[TrigOutID:str, CTOPam:int, Value:float or int], ],
                TrigOutID: 1, 2 or 3
        :return:
        """
        args = []
        for trig_out_id, cto_pam, value in trigoutid_ctopam_value_pairs:
            args.append(trig_out_id)
            args.append(cto_pam)
            args.append(value)

        self.send_cmd("CTO", False, *args)

    def get_trigger_out_config(self, *trigoutid_ctopam_pairs):
        """
        :param trigoutid_ctopam_pairs: [[TrigOutID:str, CTOPam:int], ]
        :return: [[[TrigOUTID:str, CTOPam:int], value:float or int], ], value is different type according to CTOPam
        """
        args = []
        for trig_out_id, cto_pam in trigoutid_ctopam_pairs:
            args.append(trig_out_id)
            args.append(cto_pam)

        ans = self.send_cmd("CTO", True, *args)
        ans_lst = []
        for ans_line in re.split(PiezoGCSCom.COMMAND_END, ans):
            trigoutid_ctopam, value = re.split("=", ans_line)
            trig_out_id, cto_pam = re.findall(r'\S+', trigoutid_ctopam)
            cto_pam = int(cto_pam)

            if cto_pam == PiezoGCSCom.TRIGGER_OUT_CFG_CTOPAM_TRIGGER_STEP:
                value = float(value)
            elif cto_pam == PiezoGCSCom.TRIGGER_OUT_CFG_CTOPAM_AXIS:
                value = int(value)
            elif cto_pam == PiezoGCSCom.TRIGGER_OUT_CFG_CTOPAM_TRIGGER_MODE:
                value = int(value)
            elif cto_pam == PiezoGCSCom.TRIGGER_OUT_CFG_CTOPAM_TRIGGER_DELAY:
                value = float(value)
            elif cto_pam == PiezoGCSCom.TRIGGER_OUT_CFG_CTOPAM_MIN_THRESHOLD:
                value = float(value)
            elif cto_pam == PiezoGCSCom.TRIGGER_OUT_CFG_CTOPAM_MAX_THRESHOLD:
                value = float(value)
            elif cto_pam == PiezoGCSCom.TRIGGER_OUT_CFG_CTOPAM_POLARITY:
                value = int(value)
            else:
                raise ValueError(f"Get trigger out cfg: wrong CTO PAM {cto_pam}")

            ans_lst.append([[trig_out_id, cto_pam], value])

        return ans_lst

    DRIFT_COMPENSATION_MODE_ON = 1
    DRIFT_COMPENSATION_MODE_OFF = 0

    def set_drift_compensation_mode(self, *axis_dcostate_pairs):
        """
        :param axis_dcostate_pairs: [[AxisID:str, DCOState:int], ], AxisID: single ASCII char, DCOState: 0 or 1
        :return:
        """
        args = []
        for axis_id, dcostate in axis_dcostate_pairs:
            args.append(axis_id)
            args.append(dcostate)

        self.send_cmd("DCO", False, *args)

    def get_drift_compensation_mode(self, *axis_ids):
        """
        :param axis_ids: [AxisID:str, ]
        :return: [[AxisID:str, DCOState:int], ], DCOState: 0 OFF 1 ON
        """
        ans = self.send_cmd("DCO", True, *axis_ids)
        return PiezoGCSCom.load_ans_pairs(ans,
                                         gen_right=lambda x: int(x))

    def delay_command_interpreter(self, delay_ms: int):
        """
        :param delay_ms:int
        :return:
        """
        self.send_cmd("DEL", False, delay_ms)

    def define_home_position(self, *axis_ids):
        """
        :param axis_ids: [AxisID:str, ]
        :return:
        """
        self.send_cmd("DFH", False, *axis_ids)

    def get_home_position_definition(self, *axis_ids):
        """
        :param axis_ids: [AxisID:str, ]
        :return: [[AxisID:str, SensorPosition:float], ]
        """
        ans = self.send_cmd("DFH", True, *axis_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: float(x))

    def get_digital_input_lines(self, *dio_ids):
        """
        :param dio_ids: [DIO_ID:str, ], DIO_ID: [1, 2, 3]
        :return: [[DIO_ID:str, ON_OFF: int], ], ON_OFF: 0 OFF, 1 ON
        """
        ans = self.send_cmd("DIO", True, *dio_ids)
        return PiezoGCSCom.load_ans_pairs(ans,
                                         gen_right=lambda x: int(x))

    DATA_RECORDER_CFG_OPTION_AXIS_TARGET_POS = 1
    DATA_RECORDER_CFG_OPTION_AXIS_CURRENT_POS = 2
    DATA_RECORDER_CFG_OPTION_AXIS_POS_ERROR = 3
    DATA_RECORDER_CFG_OPTION_AXIS_CTRL_OUT = 15
    DATA_RECORDER_CFG_OPTION_CH_CTRL_VOLTAGE = 7

    def set_data_recorder_cfg(self, rec_table_id: int, source: str, rec_option: int):
        """
        :param rec_table_id:str : 1, 2 or 3
        :param source: AxisID:str when rec_option in [1, 2, 3, 15] or Channel_ID:int when rec_option is 7
        :param rec_option:
        :return:
        """
        self.send_cmd("DRC", False, rec_table_id, source, rec_option)

    def get_data_recorder_cfg(self, *rec_table_ids):
        """
        :param rec_table_ids: [RecTableID: str]
        :return: [[RecTableID, [Source:str, RecOption:int]], ]
        """

        ans = self.send_cmd("DRC", True, *rec_table_ids)
        ans_nodec = PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda s: re.findall(r'\S+', s))
        # Patch RecOption to int
        for ans_entry in ans_nodec:
            ans_entry[1][1] = int(ans_entry[1][1])
        return ans_nodec

    def get_recorded_data_values(self, start_point: int = None, number_points: int = None, *rec_table_ids):
        """
        DRR? [<StartPoint> [<NumberOfPoints> [{<RecTableID>}]]]
        :param start_point:int:
        :param number_points:int:
        :param rec_table_ids:[RecTableID:str, ]
        :return:
        {
            "TYPE":int,
            "SEPARATOR":str(1),
            "DIM":int,
            "SAMPLE_TIME":float,
            "NDATA":int,
            ....
            "DATA": [[data:float, ], ]
        }
        """
        args = []
        if start_point is not None:
            args.append(start_point)
            if number_points is not None:
                args.append(number_points)

                for rec_table_id in rec_table_ids:
                    args.append(rec_table_id)

        ans = self.send_cmd("DRR", True, *args)
        return PiezoGCSCom.load_gcs_table(ans, gen_rec=lambda s: float(s))

    def get_error_number(self):
        """
        :return: error:int
        """
        return int(self.send_cmd("ERR", True))

    def go_to_home_position(self, *axis_ids):
        """
        :param axis_ids: [AxisID:str, ]
        :return:
        """
        self.send_cmd("GOH", False, *axis_ids)

    def get_wave_table_data(self, start_point: int = None, number_points: int = None, *wave_table_ids):
        """
        GWD? [<StartPoint> [<NumberOfPoints> [{<RecTableID>}]]]
        :param start_point:int:
        :param number_points:int:
        :param rec_table_ids:[RecTableID:str, ]
        :return:
        {
            "TYPE":int,
            "SEPARATOR":str(1),
            "DIM":int,
            "SAMPLE_TIME":float,
            "NDATA":int,
            ....
            "DATA": [[data:float, ], ]
        }
        """
        args = []
        if start_point is not None:
            args.append(start_point)
            if number_points is not None:
                args.append(number_points)

                for wave_table_id in wave_table_ids:
                    args.append(wave_table_id)

        ans = self.send_cmd("GWD", True, *args)
        return PiezoGCSCom.load_gcs_table(ans, gen_rec=lambda s: float(s))

    def get_all_data_recorder_options(self):
        """
        Incomplete
        :return:
        """
        # FIXME: Not parsed
        return self.send_cmd("HDR", True)

    def get_list_commands(self):
        """
        Incomplete
        :return:
        """
        # FIXME: Not parsed
        return self.send_cmd("HLP", True)

    def halt_motion(self, *axis_ids):
        """
        :param axis_ids: [AxisID:str, ]
        :return:
        """
        self.send_cmd("HLT", False, *axis_ids)

    def get_list_parameters(self):
        """
        :return: [[ParameterID:str, Description:str], ]
        """
        ans = self.send_cmd("HPA", True)
        ans_lst = []
        for ans_line in re.split(f"{PiezoGCSCom.COMMAND_END}", ans):
            first_equal = ans_line.find("=")
            ans_left = ans_line[:first_equal]
            ans_right = ans_line[first_equal+1:]
            ans_lst.append([ans_left, ans_right])
        return ans_lst

    def set_interface_parameter_temp(self, *interface_pam_value_pairs):
        """
        :param interface_pam_value_pairs: [[InterfacePam:str, PamValue:str], ]
            InterfacePam:str: RSBAUD, GPADR, IPADR, IPSTART, IPMASK
        :return:
        """
        args = []
        for pam_value in interface_pam_value_pairs:
            args += pam_value
        self.send_cmd("IFC", False, *args)

    def get_interface_parameter(self, *interface_pams):
        """
        :param interface_pams: [InterfacePam:str, ]
            InterfacePam:str: RSBAUD, GPADR, IPADR, IPSTART, IPMASK, MACADR
        :return:
        """
        ans = self.send_cmd("IFC", True, *interface_pams)
        return PiezoGCSCom.load_ans_pairs(ans)

    def set_interface_parameter_default(self, passwd:str = "100", *interface_pam_value_pairs):
        """
        :param passwd:str: default 100
        :param interface_pam_value_pairs: [[InterfacePam:str, PamValue:str], ]
            InterfacePam:str: RSBAUD, GPADR, IPADR, IPSTART, IPMASK
        :return:
        """
        args = [passwd, ]
        for pam_value in interface_pam_value_pairs:
            args += pam_value
        self.send_cmd("IFS", False, *args)

    def get_interface_parameter_default(self, *interface_pams):
        """
        :param interface_pams: [InterfacePam:str, ]
            InterfacePam:str: RSBAUD, GPADR, IPADR, IPSTART, IPMASK, MACADR
        :return:
        """
        ans = self.send_cmd("IFS", True, *interface_pams)
        return PiezoGCSCom.load_ans_pairs(ans)

    def start_impulse_response_measurement(self, axis_id:str, amplitude:float):
        """
        :param axis_id:str
        :param amplitude:float
        :return:
        """
        self.send_cmd("IMP", False, axis_id, f"{amplitude:e}")

    def get_imp_settings(self, *axis_ids):
        """
        :param axis_ids: [AxisID:str, ]
        :return:
        """
        ans = self.send_cmd("IMP", True, *axis_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x:float(x))

    def macro_begin(self, macroname:str):
        """
        MAC BEG
        :param macroname:str
        :return:
        """
        self.send_cmd("MAC BEG", False, macroname)

    def macro_define(self, macroname:str):
        """
        set specified macro as startup
        :param macroname:str: None to remove current startup macro
        :return:
        """
        self.send_cmd("MAC DEF", False, macroname)

    def macro_get_define(self):
        """
        :return: current startup macro
        """
        return self.send_cmd("MA DEF", True)

    def macro_delete(self, macroname:str):
        """
        delete specified macroname
        :param macroname: "*.*" to remove all
        :return:
        """
        self.send_cmd("MAC DEL", False, macroname)

    def macro_end(self):
        """
        :return:
        """
        self.send_cmd("MAC END", False)

    def mac_free(self):
        """
        :return:
        """
        return int(self.send_cmd("MAC FREE", True))

    def mac_repeat(self, macroname:str, times:int):
        """
        :param macroname:str
        :param times:
        :return:
        """
        self.send_cmd("MAC NSTART", False, macroname, times)

    def mac_start(self, macroname:str):
        """
        :param macroname:
        :return:
        """
        self.send_cmd("MAC START", False, macroname)

    def list_macros(self, macroname:str = None):
        """
        :param macroname: None to list all macronames, otherwise list the content of the macro
        :return: str
        """
        return self.send_cmd("MAC", True, macroname)

    def set_target_pos(self, *axis_id_position_pairs):
        """
        :param axis_id_position_pairs: [[AxisID:str, position:float],]
        :return:
        """
        args = []
        for axis_id_pos in axis_id_position_pairs:
            args += axis_id_pos
        self.send_cmd("MOV", False, *args)

    def get_target_pos(self, *axis_ids):
        """
        :param axis_ids:
        :return: [[AxisID:str, pos:float], ]
        """
        ans = self.send_cmd("MOV", True, *axis_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x:float(x))

    def set_relative_target_pos(self, *axis_id_dist_pairs):
        """
        :param axis_id_dist_pairs: [[AxisID:str, distance:float], ]
        :return:
        """
        args = []
        for axis_id_dist in axis_id_dist_pairs:
            args += axis_id_dist
        self.send_cmd("MVR", False, *args)

    def set_low_pos_soft_limit(self, *axis_id_limit_pairs):
        """
        :param axis_id_limit_pairs:
        :return:
        """
        args = []
        for axis_id_limit in axis_id_limit_pairs:
            args += axis_id_limit
        self.send_cmd("NLM", False, *args)

    def get_low_pos_soft_limit(self, *axis_ids):
        """
        :param axis_ids:
        :return: [[AxisID:str, limit:float], ]
        """
        ans = self.send_cmd("NLM", True, *axis_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: float(x))

    def set_control_mode(self, *out_sig_id_mode_pairs):
        """
        :param out_sig_id_mode_pairs: [[OutputSignalID:str, Mode:int], ] Mode: 0 Offline, 1 Onlline
        :return:
        """
        args = []
        for outsig_id_mode in out_sig_id_mode_pairs:
            args += outsig_id_mode
        self.send_cmd("ONL", False, *args)

    def get_control_mode(self, *outsig_ids):
        """
        :param outsig_ids: [OutputSignalID:str, ]
        :return: [[OutputSignalID:str, Mode:int], ]
        """
        ans = self.send_cmd("ONL", True, *outsig_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: int(x) == 1)

    def get_on_target_status(self, *axis_ids):
        """
        :param axis_ids: [AxisID:str, ]
        :return: [[AxisID:str, on-target:int], ], on-target: 1, 0 otherwise
        """
        ans = self.send_cmd("ONT", True, *axis_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: int(x) == 1)

    def get_overflow_state(self, *axis_ids):
        """
        only in Closed-loop state
        :param axis_ids: [AxisID:str, ]
        :return: [[AxisID:str, overflow:int], ], overflow: 1, 0 otherwise
        """
        ans = self.send_cmd("OVF", True, *axis_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: int(x))

    def set_high_pos_soft_limit(self, *axis_id_limit_pairs):
        """
        :param axis_id_limit_pairs:
        :return:
        """
        args = []
        for axis_id_limit in axis_id_limit_pairs:
            args += axis_id_limit
        self.send_cmd("PLM", False, *args)

    def get_high_pos_soft_limit(self, *axis_ids):
        """
        :param axis_ids:
        :return: [[AxisID:str, limit:float], ]
        """
        ans = self.send_cmd("PLM", True, *axis_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: float(x))

    def get_real_position(self, *axis_ids):
        """closed loop
        :param axis_ids:
        :return: [[AxisID:str, pos:float], ]
        """
        ans = self.send_cmd("POS", True, *axis_ids)
        res = PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: float(x))
        self.axis_position_changed.emit(res)
        return res

    def reboot(self):
        """
        CAUTION: Reboot, Power-on reset
        This will case COM connection drop, must re-open
        :return:
        """
        self.send_cmd("RBT", False)
        while True:
            try:
                self.ser.open()
                if self.ser.is_open:
                    break
            except Exception as e:
                pass

    def reload_parameters_in_mem(self, *item_pam_pairs):
        """
        :param imem_pam_pairs: [[ItemID:str, PamID:str], ]
        :return:
        """
        args = []
        for item_pam in item_pam_pairs:
            args += item_pam
        self.send_cmd("RPA", False, *args)

    def set_record_table_rate(self, record_table_rate: int):
        """
        Rec. Duration = Servo Update Time * RTR value * NumberOfPoints
        :param record_table_rate: int > 0
        :return:
        """
        self.send_cmd("RTR", False, record_table_rate)

    def get_record_table_rate(self):
        return int(self.send_cmd("RTR", True))

    def set_current_axis_id(self, *axis_id_new_pairs):
        """
        :param axis_id_new_pairs: [[AxisID:str, newAxisID:str], ]
        :return:
        """
        args = []
        for axis_id_new in axis_id_new_pairs:
            args += axis_id_new
        self.send_cmd("SAI", False, *args)

    def get_current_axis_ids(self, b_all: bool = False):
        """
        :param b_all: True to ensure also "deactivated" axis
        :return: [AxisIDs, ]
        """
        ans = self.send_cmd("SAI", True, "ALL" if b_all else None)
        return [x.strip() for x in re.split(PiezoGCSCom.COMMAND_END, ans)]

    def save_parameters_in_nvm(self, passwd: str = "100", *item_pam_value_pairs):
        """
        CAUTION: wrong settings may damage device
        :param passwd:
        :param item_pam_value_pairs: [[ItemID:str, PamID:str, Value], ]
        :return:
        """
        args = [passwd, ]
        for item_pam_value in item_pam_value_pairs:
            args += item_pam_value
        self.send_cmd("SEP", False, *args)

    def get_parameters_from_nvm(self, *item_pam_pairs):
        """
        :param item_pam_pairs: [[ItemID:str, PamID:str], ]
        :return: [ [[ItemID:str, PamID:str], Value:str], ]
        """
        args = []
        for item_pam in item_pam_pairs:
            args += item_pam
        ans = self.send_cmd("SEP", True, *args)
        return PiezoGCSCom.load_ans_pairs(ans,
                                         gen_left=lambda s: [x for x in re.findall(r'\S+', s)])

    def set_parameters_in_mem(self,  *item_pam_value_pairs):
        """
        CAUTION: wrong settings may damage device
        :param item_pam_value_pairs: [[ItemID:str, PamID:str, Value], ]
        :return:
        """
        args = [ ]
        for item_pam_value in item_pam_value_pairs:
            args += item_pam_value
        self.send_cmd("SPA", False, *args)

    def get_parameters_from_mem(self, *item_pam_pairs):
        """
        :param item_pam_pairs: [[ItemID:str, PamID:str], ]
        :return: [ [[ItemID:str, PamID:str], Value:str], ]
        """
        args = []
        for item_pam in item_pam_pairs:
            args += item_pam
        ans = self.send_cmd("SPA", True, *args)
        return PiezoGCSCom.load_ans_pairs(ans,
                                         gen_left=lambda s: [x for x in re.findall(r'\S+', s)])

    def get_device_ssn(self):
        return self.send_cmd("SSN", True)

    def start_step_response_measurement(self, axis_id: str, amplitude: float):
        """
        :param axis_id:
        :param amplitude:
        :return:
        """
        self.send_cmd("STE", False, axis_id, amplitude)

    def get_ste_settings(self, *axis_ids):
        """
        :param axis_ids:
        :return: [[AxisID:str, amplitude:float], ]
        """
        ans = self.send_cmd("STE", True, *axis_ids)
        return PiezoGCSCom.load_ans_pairs(ans,
                                         gen_right=lambda x: float(x))

    def stop_all_motion(self):
        """
        err code set to 10
        :return:
        """
        self.send_cmd("STP", False)

    def set_openloop_axis_value(self, *axis_id_amp_pairs):
        """
        :param axis_id_amp_pairs:
        :return:
        """
        args = []
        for axis_id_amp in axis_id_amp_pairs:
            args += axis_id_amp
        self.send_cmd("SVA", False, *args)

    def get_openloop_axis_value(self, *axis_ids):
        """openloop
        :param axis_ids:
        :return: [[AxisID:str, value:float], ]
        """
        ans = self.send_cmd("SVA", True, *axis_ids)
        res = PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: float(x))
        self.axis_position_changed.emit(res)
        return res

    def set_servo_state(self, *axis_state_pairs):
        """
        :param axis_state_pairs: [[AxisID:str, state:int], ], state 1: on (closed-loop) 0: off (open-loop)
        :return:
        """
        args = []
        for axis_state in axis_state_pairs:
            args += axis_state
        self.send_cmd("SVO", False, *args)

    def get_servo_state(self, *axis_ids):
        """
        :param axis_ids: [AxisID:str, ],
        :return: [[AxisID:str, state:int], ], state 1: on (closed-loop) 0: off (open-loop)
        """
        ans = self.send_cmd("SVO", True, *axis_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: int(x) == 1)

    def set_relative_openloop_axis_value(self, *axis_id_diff_pairs):
        """
        :param axis_id_diff_pairs:
        :return:
        """
        args = []
        for axis_id_diff in axis_id_diff_pairs:
            args += axis_id_diff
        self.send_cmd("SVR", False, *args)

    def get_input_sig_adc_value(self, *input_sig_ids):
        """
        :param input_sig_ids:
        :return: [[InputSignalID:str, value: int], ]
        """
        ans = self.send_cmd("TAD", True, *input_sig_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: int(x))

    def tell_dio_lines(self):
        """
        :return: (n_in, n_out) #  [["I", lines:int], ["O", lines:int]]
        """
        ans = self.send_cmd("TIO", True)
        ans_lst = PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda s: int(s))
        if ans_lst[0][0] == "I" and ans_lst[1][0] == "O":
            n_in = ans_lst[0][1]
            n_out = ans_lst[1][1]
        else:
            n_in = ans_lst[1][1]
            n_out = ans_lst[0][1]
        return n_in, n_out

    def get_min_commandable_position(self, *axis_ids):
        """
        :param axis_ids: [AxisID:str, ],
        :return: [[AxisID:str, min_pos:float], ],
        """
        ans = self.send_cmd("TMN", True, *axis_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: float(x))

    def get_max_commandable_position(self, *axis_ids):
        """
        :param axis_ids: [AxisID:str, ],
        :return: [[AxisID:str, min_pos:float], ],
        """
        ans = self.send_cmd("TMX", True, *axis_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: float(x))

    def get_number_of_record_tables(self):
        return int(self.send_cmd("TNR", True))

    def get_number_of_outsig_channels(self):
        return int(self.send_cmd("TPC", True))

    def get_number_of_insig_channels(self):
        return int(self.send_cmd("TSC", True))

    def get_insig_pos_value(self, *insig_ids):
        """
        :param insig_ids: [InSigID:str, ],
        :return: [[InSigID:str, min_pos:float], ],
        """
        ans = self.send_cmd("TSP", True, *insig_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: float(x))

    def tell_valid_chset_for_axis_id(self):
        return self.send_cmd("TVI", True).strip()

    def clear_all_wave_related_triggers(self):
        self.send_cmd("TWC", False)

    def get_number_of_wave_generators(self):
        return int(self.send_cmd("TWG", True))

    def set_trigger_line_action_to_waveform_point(self, *trigoutid_pointnumber_switch_pairs):
        """
        :param trigoutid_pointnumber_switch_pairs: [[TrigOutID:str, PointNumber:int, Switch:int], ]
        :return:
        """
        args = []
        for trig_pnum_switch in trigoutid_pointnumber_switch_pairs:
            args += trig_pnum_switch
        self.send_cmd("TWS", False, *args)

    def get_trigger_line_action_at_waveform_point(self, start_point: int = None, number_points: int = None,
                                                  *trigout_ids):
        """
        TWS? [<StartPoint> [<NumberOfPoints> [{<TrigOutID>}]]]
        :param start_point:int:
        :param number_points:int:
        :param trigout_ids:[TrigOutID:str, ]
        :return:
        {
            "TYPE":int,
            "SEPARATOR":str(1),
            "DIM":int,
            "SAMPLE_TIME":float,
            "NDATA":int,
            ....
            "DATA": [[data:int, ], ]
        }
        """
        args = []
        if start_point is not None:
            args.append(start_point)
            if number_points is not None:
                args.append(number_points)

                for rec_table_id in trigout_ids:
                    args.append(rec_table_id)

        ans = self.send_cmd("TWS", True, *args)
        return PiezoGCSCom.load_gcs_table(ans, gen_rec=lambda s: int(s))

    def set_velocity_control_mode(self, *axis_id_mode_pairs):
        """
        :param axis_id_mode_pairs:
        :return:
        """
        args = []
        for axis_id_mode in axis_id_mode_pairs:
            args += axis_id_mode
        self.send_cmd("VCO", False, *args)

    def get_velocity_control_mode(self, *axis_ids):
        """
        :param axis_ids: [AxisID:str, ],
        :return: [[AxisID:str, mode:int], ],
        """
        ans = self.send_cmd("VCO", True, *axis_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: int(x))

    def set_closedloop_velocity(self, *axis_id_v_pairs):
        """
        velocity: V/s
        :param axis_id_v_pairs: [[AxisID:str, v:float], ]
        :return:
        """
        args = []
        for axis_id_v in axis_id_v_pairs:
            args += axis_id_v
        self.send_cmd("VEL", False, *args)

    def get_closedloop_velocity(self, *axis_ids):
        """
        :param axis_ids: [AxisID:str, ],
        :return: [[AxisID:str, v:float], ],
        """
        ans = self.send_cmd("VEL", True, *axis_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: float(x))

    def get_firmware_driver_version(self):
        return self.send_cmd("VER", True)

    def set_voltage_out_high_limit(self, *outsig_limit_pairs):
        """
        :param outsig_limit_pairs: [[OutputSigID:str, Voltage:float], ]
        :return:
        """
        args = []
        for outsig_limit in outsig_limit_pairs:
            args += outsig_limit
        self.send_cmd("VMA", False, *args)

    def get_out_voltage_high_limit(self, *outsig_ids):
        """
        :param outsig_ids:
        :return:
        """
        ans = self.send_cmd("VMA", True, *outsig_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: float(x))

    def set_out_voltage_low_limit(self, *outsig_limit_pairs):
        """
        :param outsig_limit_pairs: [[OutputSigID:str, Voltage:float], ]
        :return:
        """
        args = []
        for outsig_limit in outsig_limit_pairs:
            args += outsig_limit
        self.send_cmd("VMI", False, *args)

    def get_out_voltage_low_limit(self, *outsig_ids):
        """
        :param outsig_ids:
        :return:
        """
        ans = self.send_cmd("VMI", True, *outsig_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: float(x))

    def get_out_voltage(self, *outsig_ids):
        """
        :param outsig_ids:
        :return:
        """
        ans = self.send_cmd("VOL", True, *outsig_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: float(x))

    def set_waveform_definition(self, wave_table_id:str, append_wave:str, wave_type:str, *wave_type_parameters):
        """
        :param wave_table_id:
        :param append_wave: "X" clears wave table and restart from first point; "&" appends; "+" accumulate the values
        :param wave_type: PNT: user-defined; SIN_P: inverted cosine; RAMP; LIN: single scan line; SIN; POL: Polynomial;
                        TAN; CFG: Special type which configures additionally parameters for a waveform
        :param wave_type_parameters:
                PNT: SegStartPoint WaveLength {WavePoint}
                SIN_P: SegLength Amp Offset WaveLength StartPoint CurveCenterPoint
                RAMP: SegLength Amp Offset WaveLength StartPoint SpeedUpDown CurveCenterPoint
                LIN: SegLength Amp Offset WaveLength StartPoint SpeedUpDown
                SIN: SegStartPoint SegLength A N_p x_0 Theta B
                POL: SegStartPoint WaveLength x_0 A_0 [{A_n}]
                TAN: SegStartPoint SegLength A N_p x_0 Theta B
                CFG: n m p k s L
        :return:
        """
        self.send_cmd("WAV", False, wave_table_id, append_wave, wave_type, *wave_type_parameters)

    def get_waveform_definition(self, *wavetable_id_pam_pairs):
        """
        :param wavetable_id_pam_pairs:
        :return: [[[WaveTableID:str, WaveParameterID:str], value:float], ]
        """
        args = []
        for wt_id_pam in wavetable_id_pam_pairs:
            args += wt_id_pam

        ans = self.send_cmd("WAV", True, *args)
        return PiezoGCSCom.load_ans_pairs(ans,
                                          gen_left=lambda s: [x.strip() for x in re.findall(r"\S+", s)],
                                          gen_right=lambda s: float(s))

    def clear_wave_table_data(self, *wavetable_ids):
        self.send_cmd("WCL", False, *wavetable_ids)

    def set_wave_generator_cycle_num(self, *wavegen_id_cycle_pairs):
        args = []
        for wavegen_id_cycle in wavegen_id_cycle_pairs:
            args += wavegen_id_cycle
        self.send_cmd("WGC", False, *args)

    def get_wave_generator_cycle_num(self, *wavegen_ids):
        ans = self.send_cmd("WGC", True, *wavegen_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda s: int(s))

    def set_wave_generator_start_stop_mode(self, *wavegen_id_mode_pairs):
        # FIXME: Incomplete
        args = []
        for wavegen_id_cycle in wavegen_id_mode_pairs:
            args += wavegen_id_cycle
        self.send_cmd("WGO", False, *args)

    def get_wave_generator_start_stop_mode(self, *wavegen_ids):
        # FIXME: Incomplete
        ans = self.send_cmd("WGO", True, *wavegen_ids)
        return PiezoGCSCom.load_ans_pairs(ans)

    def start_recording_sync_with_wg(self):
        self.send_cmd("WGR", False)

    def get_max_num_of_wavetable_points(self, *wavetable_ids):
        ans = self.send_cmd("WMS", True, *wavetable_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda x: int(x))

    def set_wave_generator_output_offset(self, *wavegen_id_offset_pairs):
        args = []
        for wavegen_id_offset in wavegen_id_offset_pairs:
            args += wavegen_id_offset
        self.send_cmd("WOS", False, *args)

    def get_wave_generator_output_offset(self, *wavegen_ids):
        ans = self.send_cmd("WOS", True, *wavegen_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda s: float(s))

    def save_parameters_to_nvm(self, passwd: str = "100", *item_pam_value_pairs):
        """
        CAUTION: wrong settings may damage device
        :param passwd:
        :param item_pam_value_pairs: [[ItemID:str, PamID:str, Value], ]
        :return:
        """
        args = [passwd, ]
        for item_pam_value in item_pam_value_pairs:
            args += item_pam_value
        self.send_cmd("WPA", False, *args)

    def set_wave_generator_table_rate(self, *wavegen_id_rate_type_pairs):
        # FIXME: Incomplete
        args = []
        for wg_id_rate_type in wavegen_id_rate_type_pairs:
            args += wg_id_rate_type

        self.send_cmd("WTR", False, *args)

    def get_wave_generator_table_rate(self, *wavegen_ids):
        # FIXME: Incomplete
        ans = self.send_cmd("WTR", True, *wavegen_ids)
        return PiezoGCSCom.load_ans_pairs(ans, gen_right=lambda s: [x.strip() for x in re.findall(r"\S+", s)])

