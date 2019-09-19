#!/usr/bin/env python3

import visa
import numpy as np
from threading import Lock
from PyQt5.QtWidgets import QWidget
from .m3390_config_ui import Ui_M3390_Config_Window
from PyQt5.QtGui import QDoubleValidator
import traceback
import logging
from PyQt5.QtCore import QObject, pyqtSignal

_SPLIT_LOG = False

if _SPLIT_LOG:
    m3390_logger = logging.getLogger("m3390")
    m3390_logger.setLevel(logging.DEBUG)
    m3390_fh = logging.FileHandler("m3390.log")
    m3390_formatter = logging.Formatter('%(asctime)s [%(component)s] - %(levelname)s - %(message)s')
    m3390_fh.setFormatter(m3390_formatter)
    m3390_logger.addHandler(m3390_fh)

    m3390_ch = logging.StreamHandler()
    m3390_ch.setFormatter(m3390_formatter)
    m3390_logger.addHandler(m3390_ch)
else:
    m3390_logger = logging.getLogger("autools_setup_main")


class M3390Man(QObject):
    """Helper (man) Class for communicate with M3390 via PyVisa"""

    opened = pyqtSignal()
    closed = pyqtSignal()
    output_state_changed = pyqtSignal(bool, name='outputStateChanged')
    sig_changed = pyqtSignal('QString', float, 'QString', name='sigChanged')

    # FIXME: in 50Ohm mode only
    frequency_value_dict = {
        'uHz': (1, 5e13),
        'mHz': (1e-3, 5e10),
        'Hz':  (1e-6, 5e7),
        'kHz': (1e-9, 5e4),
        'MHz': (1e-12, 50),
    }
    sig_amp_value_dict = {
        'mV': (10, 10000),
        'V': (1e-2, 10),
    }
    sig_offset_value_dict = {
        'mV': (-5000, 5000),
        'V': (-5, 5),
    }

    def __init__(self, dev_addr: str = None):
        super().__init__()
        self.dev_addr = dev_addr
        self.rm = visa.ResourceManager()
        if self.dev_addr is not None:
            self.dev_inst = self.rm.open_resource(self.dev_addr)
        else:
            self.dev_inst = None

        self.config_window = None

    def set_dev_addr(self, addr: str):
        self.dev_addr = addr

    def open(self, dev_addr: str = None):
        if dev_addr is not None:
            self.dev_addr = dev_addr

        if self.dev_addr is None:
            raise ValueError(f"Device address must not be None")

        self.dev_inst = self.rm.open_resource(self.dev_addr)
        self.opened.emit()
        m3390_logger.info(f"M3390 Device opened with {self.dev_addr}", extra={"component": "M3390"})

    def close(self):
        if self.dev_inst is not None:
            self.dev_inst.close()
            self.closed.emit()
            self.dev_inst = None
            m3390_logger.info(f"M3390 device closed", extra={"component": "M3390"})

    def is_open(self):
        return self.dev_inst is not None

    def get_dev_id(self):
        return self.dev_inst.query("*IDN?")

    def set_sig_funct(self, func: str):
        if func not in ('SINusoid', 'SIN', 'SQUare', 'SQ', 'RAMP', 'PULSe', 'PUL', 'NOISe', 'NOI', 'DC', 'USER'):
            m3390_logger.error(f"Unknown function {func}", extra={"component": "M3390"})
        self.dev_inst.write(f'FUNCtion {func}')
        m3390_logger.debug(f"Setting function {func}", extra={"component": "M3390"})

    def set_frequency(self, value: float, unit: str):
        if unit in M3390Man.frequency_value_dict.keys():
            min_v, max_v = M3390Man.frequency_value_dict[unit]
            if not min_v <= value <= max_v:
                m3390_logger.error(f"Wrong frequency value {value} {unit}", extra={"component": "M3390"})
                return
        else:
            m3390_logger.error(f"Unknown frequency unit {unit}", extra={"component": "M3390"})
            return

        self.dev_inst.write(f"FREQuency {value:.6f} {unit}")
        m3390_logger.debug(f"Setting frequency {value:.6f} {unit}", extra={"component": "M3390"})
        self.sig_changed.emit('frequency', value, unit)

    def set_voltage_unit(self, unit: str):
        if unit not in ('Vpp', 'Vrms', 'dBm'):
            m3390_logger.error(f"Unknown voltage unit {unit}", extra={"component": "M3390"})
        self.dev_inst.write(f'VOLTage:UNIT {unit}')
        m3390_logger.debug(f"Setting voltage unit {unit}", extra={"component": "M3390"})

    def set_sig_amplitude(self, value: float, unit: str):
        if unit in M3390Man.sig_amp_value_dict.keys():
            min_v, max_v = M3390Man.sig_amp_value_dict[unit]
            if not min_v <= value <= max_v:
                m3390_logger.error(f"Wrong signal amplitude value {value} {unit}", extra={"component": "M3390"})
                return
        else:
            m3390_logger.error(f"Unknown signal amplitude unit {unit}", extra={"component": "M3390"})
            return

        self.dev_inst.write(f'VOLTage {value:.6f} {unit}')
        m3390_logger.debug(f"Setting signal amplitude {value:.6f} {unit}", extra={"component": "M3390"})
        self.sig_changed.emit('amplitude', value, unit)

    def set_sig_offset(self, value: float, unit: str):
        if unit in M3390Man.sig_offset_value_dict.keys():
            min_v, max_v = M3390Man.sig_offset_value_dict[unit]
            if not min_v <= value <= max_v:
                m3390_logger.error(f"Wrong signal offset value {value} {unit}", extra={"component": "M3390"})
                return
        else:
            m3390_logger.error(f"Unknown signal offset unit {unit}", extra={"component": "M3390"})
            return

        self.dev_inst.write(f'VOLTage:OFFSet {value:.6f} {unit}')
        m3390_logger.debug(f"Setting signal offset {value:.6f} {unit}", extra={"component": "M3390"})
        self.sig_changed.emit('offset', value, unit)

    def turn_output(self, on_off: bool):
        if on_off:
            self.dev_inst.write(f"OUTPut ON")
            m3390_logger.info(f"Output ON", extra={"component": "M3390"})
        else:
            self.dev_inst.write(f"OUTPut OFF")
            m3390_logger.info(f"Output OFF", extra={"component": "M3390"})

        self.output_state_changed.emit(on_off)

    def show_config_window(self):
        if self.config_window is None:
            self.config_window = M3390ConfigWindow(self)

        self.config_window.show()


class M3390ConfigWindow(Ui_M3390_Config_Window):
    def __init__(self, m3390man: M3390Man):
        Ui_M3390_Config_Window.__init__(self)
        self.m3390man = m3390man
        self.window = QWidget()
        self.setupUi(self.window)

        self.refresh_resources()

        self.pushButton_Refresh.clicked.connect(self.refresh_resources)
        self.comboBox_ResourceAddr.currentTextChanged.connect(lambda t: self.m3390man.set_dev_addr(t))
        self.pushButton_Open.clicked.connect(self.dev_open_clicked)

        self.comboBox_FrequencyUnit.currentTextChanged.connect(self.freq_unit_changed)
        self.comboBox_SigAmpUnit.currentTextChanged.connect(self.sigamp_unit_changed)
        self.comboBox_SigOffsetUnit.currentTextChanged.connect(self.sigoffset_unit_changed)

        self.pushButton_SetFreq.clicked.connect(
            lambda: self.m3390man.set_frequency(
                self.doubleSpinBox_FrequencyValue.value(),
                self.comboBox_FrequencyUnit.currentText()))

        self.pushButton_SetFunc.clicked.connect(
            lambda: self.m3390man.set_sig_funct(
                self.comboBox_Function.currentText()
            )
        )

        self.pushButton_SetSigAmp.clicked.connect(
            lambda: self.m3390man.set_sig_amplitude(
                self.doubleSpinBox_SigAmpValue.value(),
                self.comboBox_SigAmpUnit.currentText()
            )
        )

        self.pushButton_SetSigOffset.clicked.connect(
            lambda: self.m3390man.set_sig_offset(
                self.doubleSpinBox_SigOffsetValue.value(),
                self.comboBox_SigOffsetUnit.currentText()
            )
        )

        self.pushButton_SetVolUnit.clicked.connect(
            lambda : self.m3390man.set_voltage_unit(
                self.comboBox_VoltageUnit.currentText()
            )
        )

        self.radioButton_OutputOn.clicked.connect(lambda: self.output_on_off(True))
        self.radioButton_OutputOff.clicked.connect(lambda: self.output_on_off(False))

        self.freq_unit_changed()
        self.sigamp_unit_changed()
        self.sigoffset_unit_changed()
        self.sigoffset_unit_changed()

    def freq_unit_changed(self):
        unit = self.comboBox_FrequencyUnit.currentText()
        min_v, max_v = M3390Man.frequency_value_dict[unit]
        self.doubleSpinBox_FrequencyValue.setMinimum(min_v)
        self.doubleSpinBox_FrequencyValue.setMaximum(max_v)

    def sigamp_unit_changed(self):
        unit = self.comboBox_SigAmpUnit.currentText()
        min_v, max_v = M3390Man.sig_amp_value_dict[unit]
        self.doubleSpinBox_SigAmpValue.setMinimum(min_v)
        self.doubleSpinBox_SigAmpValue.setMaximum(max_v)

    def sigoffset_unit_changed(self):
        unit = self.comboBox_SigOffsetUnit.currentText()
        min_v, max_v = M3390Man.sig_offset_value_dict[unit]
        self.doubleSpinBox_SigOffsetValue.setMinimum(min_v)
        self.doubleSpinBox_SigOffsetValue.setMaximum(max_v)

    def output_on_off(self, on_off: bool):
        self.m3390man.turn_output(on_off)
        self.radioButton_OutputOn.setChecked(on_off)
        self.radioButton_OutputOff.setChecked(not on_off)

    def dev_open_clicked(self, state):
        if not state:  # Close
            self.output_on_off(False)
            self.m3390man.close()
            self.groupBox_Settings.setDisabled(True)
            self.pushButton_Refresh.setEnabled(True)
            self.comboBox_ResourceAddr.setEnabled(True)
            self.pushButton_Open.setText("Open")
            self.label_CONN_Status.setStyleSheet("background: red")
        else:  # Open
            try:
                self.m3390man.open(self.comboBox_ResourceAddr.currentText())
                self.groupBox_Settings.setDisabled(False)
                self.pushButton_Refresh.setEnabled(False)
                self.comboBox_ResourceAddr.setEnabled(False)
                self.pushButton_Open.setText("Close")
                self.label_CONN_Status.setStyleSheet("background: green")
                #FIXME: this is fixed
                self.m3390man.set_sig_funct(self.comboBox_Function.currentText())
                self.m3390man.set_voltage_unit(self.comboBox_VoltageUnit.currentText())
                self.output_on_off(False)
            except Exception as e:
                traceback.print_tb(e.__traceback__)

                m3390_logger.error(f"Failed to open {self.m3390man.dev_addr}", extra={"component": "DG5000"})
                self.pushButton_Open.setChecked(False)

    def refresh_resources(self):
        self.comboBox_ResourceAddr.clear()
        rs = self.m3390man.rm.list_resources()
        for r in rs:
            self.comboBox_ResourceAddr.addItem(r)

    def show(self):
        self.window.show()

    def close(self):
        self.window.hide()


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])

    m3390_man = M3390Man()
    print(f'Starting...')
    m3390_man.show_config_window()
    QApplication.instance().exec_()
