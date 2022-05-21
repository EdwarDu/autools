#!/usr/bin/env python3

import pyvisa
import numpy as np
from threading import Lock
from PyQt5.QtWidgets import QWidget
from .afg31000_config_ui import Ui_AFG31000_Config_Window
from PyQt5.QtGui import QDoubleValidator
import traceback
import logging
from PyQt5.QtCore import QObject, pyqtSignal
from typing import Union
import re

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
    """Helper (man) Class for communicate with AFG31000
        for now: to set OUTPUT to BURST mode with PULSE output + voltage level settings should be enough
    """

    opened = pyqtSignal()
    closed = pyqtSignal()

    _FAKE_DEV = False

    def __init__(self, visa_addr: str = None):
        super().__init__()
        self.visa_rm = pyvisa.ResourceManager()
        self.visa_dev = None
        self.visa_inst = None

        if visa_addr is not None:
            self.visa_dev = visa_addr
            self.visa_inst = self.visa_rm.open_resource(self.visa_dev)

        self.quiet = False
        self.config_window = None

    def open(self):
        if self.visa_inst is not None:
            self.visa_inst.close()
        self.visa_inst = self.visa_rm.open_resource(self.visa_dev)
        self.opened.emit()

    def close(self):
        if self.visa_inst is not None:
            self.visa_inst.close()
            self.visa_inst = None
        self.closed.emit()

    def is_open(self):
        return self.visa_inst is not None

    def send_cmd(self, cmd: str, b_query: bool, *args):
        global afg31000_logger
        cmd_str = cmd + ('? ' if b_query else ' ') + \
                  ','.join([str(arg) for arg in args if arg is not None])

        afg31000_logger.debug(f"Sending command <{cmd_str}>", extra={"component": "AFG31000"})

        if b_query:
            return self.visa_inst.query(cmd_str)
        else:
            self.visa_inst.write(cmd_str)
        return None

    def output_config(self, ch: Union[int, str] = "", what: str = None, b_query : bool = True, value: Union[str, None] = None):
        # WARNING: no error check, we just directly forward the command as it is
        #    CHECK THE DOC

        #if not 1<=which<=2 and which != "":
        #    raise ValueError(f"output_config ch can be either 1, 2 or '', {which}")
        #what = tolower(what)
        #if what == "impedance":
        #    if not b_query and re.match("\d+(OHM)?", value) is None and tolower(value) not in ("inf", "min", "max"):
        #        raise ValueError(f"output_config impedance value can be either number[OHM], INF, MIN or MAX, {value}")
        #elif what == "polarity":
        #    if not b_query and tolower(value) not in ("normal", "inverted"):
        #        raise ValueError(f"output_config polarity value can be either NORMAL or INVERTED, {value}")
        #elif what == "state" or what == "":
        #    if not b_query and tolower(value) not in ("on", "off"):
        #        raise ValueError(f"output_config state value can be either ON or OFF, {value}")
        #elif what == "trigger:mode":
        #    if not b_query and tolower(value) not in ("trigger", "sync"):
        #        raise ValueError(f"output_config trigger:mode value can be either TRIGGER or SYNC, {value}")
        #else:
        #    raise ValueError(f"output_config can only set impedance, polarity, state, trigger:mode, {what}")

        return self.send_cmd(f"OUTPUT{ch}:{what}", b_query, value)

    def internal_am_mod_freq(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:AM:INTERNAL:FREQUENCY", b_query, value)

    def internal_am_mod_waveform(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:AM:INTERNAL:FUNCTION", b_query, value)

    def internal_am_mod_waveform_efile(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:AM:INTERNAL:FUNCTION:EFILE", b_query, value)

    def am_mod_source(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:AM:SOURCE", b_query, value)

    def am_mod(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:AM:STATE", b_query, value)

    def reset_burst_state(self, ch: Union[int, str] = ""):
        return self.send_cmd(f"SOURCE{ch}:BURST:INFINITE:REARM", False)

    def burst_idle_state(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd("SOURCE{ch}:BURST:IDLE", b_query, value)

    def burst_mode(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd("SOURCE{ch}:BURST:MODE", b_query, value)

    def burst_n_cycles(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd("SOURCE{ch}:BURST:NCYCLES", b_query, value)

    def burst_state(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd("SOURCE{ch}:BURST:STATE", b_query, value)

    def burst_delay_time(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd("SOURCE{ch}:BURST:TDELAY", b_query, value)

    def combine_feed(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd("SOURCE{ch}:COMBINE:FEED", b_query, value)

    def fm_modulation_peak_freq_deviation(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd("SOURCE{ch}:FM:DEVIATION", b_query, value)

    def internal_fm_mod_freq(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:FM:INTERNAL:FREQUENCY", b_query, value)

    def internal_fm_mod_waveform(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:FM:INTERNAL:FUNCTION", b_query, value)

    def internal_fm_mod_waveform_efile(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:FM:INTERNAL:FUNCTION:EFILE", b_query, value)

    def fm_mod_source(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:FM:SOURCE", b_query, value)

    def fm_mod(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:FM:STATE", b_query, value)

    def roscillator_source(self, b_query: bool = True, value: Union[str, None] = None):
        #TODO: error check
        return self.send_cmd("SOURCE:ROSCILLATOR:SOURCE", b_query, value)

    # TODO: SWEEP MODE COMMANDs
    #def sweep_hold_time(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
    #    return self.send_cmd(f"SOURCE{ch}:SWEEP:HTIME", b_query, value)

    #def sweep_mode(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
    #    return self.send_cmd(f"SOURCE{ch}:SWEEP:MODE", b_query, value)

    #def sweep_return_time(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
    #    return self.send_cmd(f"SOURCE{ch}:SWEEP:RTIME", b_query, value)

    #def sweep_spacing(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
    #    return self.send_cmd(f"SOURCE{ch}:SWEEP:SPACING", b_query, value)

    #def sweep_time(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
    #    return self.send_cmd(f"SOURCE{ch}:SWEEP:TIME", b_query, value)

    # We are only interested in Square or Pulse? and BURST / PWM
    def output_function(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:FUNCTION:SHAPE", b_query, value)

    def output_phase(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:PHASE:ADJUST", b_query, value)

    # WARNING: command is NOT supported if dev only has one ch
    def output_phase_concurrent(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:PHASE:CONCURRENT:STATE", b_query, value)

    # WARNING: command is NOT supported if dev only has one ch
    def output_phase_initiate(self, ch: Union[int, str] = ""):
        return self.send_cmd(f"SOURCE{ch}:PHASE:INITIATE", False)

    # TODO: no PM commands
    def pulse_dutye_cycle(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:PULSE:DCYCLE", b_query, value)

    def pulse_lead_delay(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:PULSE:DELAY", b_query, value)

    def pulse_hold(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:PULSE:HOLD", b_query, value)

    def pulse_period(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:PULSE:PERIOD", b_query, value)

    def pulse_lead_edge_time(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:PULSE:TRANSITION:LEADING", b_query, value)

    def pulse_trail_edge_time(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:PULSE:TRANSITION:TRAILING", b_query, value)

    def pulse_width(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:PULSE:WIDTH", b_query, value)

    # TODO: PWM commands? or PULSE is okay for now

    def voltage_concurrent(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:VOLTAGE:CONCURRENT:STATE", b_query, value)

    def voltage_level_imm_high(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:VOLTAGE:LEVEL:IMMEDIATE:HIGH", b_query, value)

    def voltage_level_imm_low(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:VOLTAGE:LEVEL:IMMEDIATE:LOW", b_query, value)

    def voltage_level_imm_offset(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:VOLTAGE:LEVEL:IMMEDIATE:OFFSET", b_query, value)

    def voltage_level_imm_amplitude(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:VOLTAGE:LEVEL:IMMEDIATE:AMPLITUDE", b_query, value)

    def voltage_limit_high(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:VOLTAGE:LIMIT:HIGH", b_query, value)

    def voltage_limit_low(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:VOLTAGE:LIMIT:LOW", b_query, value)

    def voltage_unit(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
        return self.send_cmd(f"SOURCE{ch}:VOLTAGE:UNIT", b_query, value)

    #def internal_noise_level(self, ch: Union[int, str] = "", b_query: bool = True, value: Union[str, None] = None):
    #    return self.send_cmd(f"SOURCE{ch}:POWER:LEVEL:IMMEDIATE:AMPLITUDE", b_query, value)

    def trigger(self,):
        return self.send_cmd(f"*TRG", False)

    def trigger_force(self,):
        return self.send_cmd(f"TRIGGER:SEQUENCE:IMMEDIATE", False)

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

        self.comboBox_CONN.currentIndexChanged.connect(self.conn_changed)

        self.refresh_comlist()
        self.conn_changed(self.comboBox_CONN.currentData())


    def sync_current_settings(self):
        pass

    def conn_changed(self, i: int):
        self.afg31000man.visa_dev = self.comboBox_CONN.currentText()

    def refresh_comlist(self):
        self.comboBox_CONN.clear()
        self.comboBox_CONN.addItems(self.afg31000man.visa_rm.list_resources())

    def open_conn_clicked(self, state):
        if not state:  # post event state
            self.close_conn()
        else:
            self.open_conn()

    def open_conn(self):
        global afg31000_logger
        try:
            self.afg31000man.open()
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
            afg31000_logger.info(f"AFG31000 COM connection opened", extra={"component": "AFG31000"})
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
        pass

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])

    afg31000_man = AFG31000Man()
    print(f'Starting...')
    afg31000_man.show_config_window()
    QApplication.instance().exec_()
