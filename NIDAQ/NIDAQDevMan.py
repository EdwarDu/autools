#!/usr/bin/python3

import nidaqmx
from nidaqmx.constants import Edge, AcquisitionType, LineGrouping, TerminalConfiguration
import logging
from .nidaq_config_ui import Ui_NIDAQ_Config_Window
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QObject, pyqtSignal
import re
import numpy as np


_SPLIT_LOG = False

if _SPLIT_LOG:
    nidaq_logger = logging.getLogger("nidaq")
    nidaq_logger.setLevel(logging.INFO)
    nidaq_fh = logging.FileHandler("nidaq.log")
    nidaq_formatter = logging.Formatter('%(asctime)s [%(component)s] - %(levelname)s - %(message)s')
    nidaq_fh.setFormatter(nidaq_formatter)
    nidaq_logger.addHandler(nidaq_fh)

    nidaq_ch = logging.StreamHandler()
    nidaq_ch.setFormatter(nidaq_formatter)
    nidaq_logger.addHandler(nidaq_ch)
else:
    nidaq_logger = logging.getLogger("autools_setup_main")


class NIDAQDevMan(QObject):
    """
    Simple helper class to control AI and AO channels of NI Box
    """

    opened = pyqtSignal()
    closed = pyqtSignal()
    task_channels_changed = pyqtSignal(str, list, name='taskChannelsChanged')
    ai_values_changed = pyqtSignal(dict, name="aiValuesChanged")
    ao_values_changed = pyqtSignal(dict, name='aoValuesChanged')
    di_values_changed = pyqtSignal(dict, name='diValuesChanged')

    def __init__(self, dev_name: str = "Dev1"):
        super().__init__()
        self.dev_name = dev_name
        self._ni_sys = nidaqmx.system.System.local()
        self.device = None  # self._ni_sys.devices[self._dev_name]
        self.ch_dict = {
            'ai': {'task': None, 'chs': []},
            'ao': {'task': None, 'chs': []},
            'di': {'task': None, 'chs': []},
            'do': {'task': None, 'chs': []},
        }

        self.ch_term_dict = {}
        self.config_window = None

    def open(self, dev_name: str = None):
        if dev_name is None:
            if self.dev_name is not None:
                self.device = self._ni_sys.devices[self.dev_name]
        else:
            self.dev_name = dev_name
            self.device = self._ni_sys.devices[self.dev_name]
        for ch_type in self.ch_dict.keys():
            self.ch_dict[ch_type] = {'task': nidaqmx.Task(), 'chs': []}
        self.opened.emit()
        return self._ni_sys.driver_version

    def is_open(self):
        return self.device is not None

    def close(self):
        for ch_type in self.ch_dict.keys():
            if self.ch_dict[ch_type]['task'] is not None:
                self.ch_dict[ch_type]['task'].close()
                self.ch_dict[ch_type]['task'] = None
        self.closed.emit()
        self.ch_term_dict = {}

    def __del__(self):
        self.close()

    def get_ai_channels(self):
        return [ch.name for ch in self.device.ai_physical_chans]

    def get_ao_channels(self):
        return [ch.name for ch in self.device.ao_physical_chans]

    def get_di_lines(self):
        return [ch.name for ch in self.device.di_lines]

    def get_do_lines(self):
        return [ch.name for ch in self.device.do_lines]

    def get_task_channels(self, ch_type: str):
        if ch_type not in self.ch_dict.keys():
            return []
        return self.ch_dict[ch_type]['chs']

    def set_task_channels(self, ch_type: str, chs):
        if ch_type not in self.ch_dict.keys():
            nidaq_logger.error(f'Unsupported {ch_type}', extra={"component": "NIDAQ"})
            raise ValueError(f'Unsupported channel type {ch_type}')

        self.ch_dict[ch_type]['task'].close()
        self.ch_dict[ch_type]['task'] = nidaqmx.Task()
        self.ch_dict[ch_type]['chs'].clear()
        for ch in set(chs):
            if ch_type == 'ai':
                self.ch_dict[ch_type]['task'].ai_channels.add_ai_voltage_chan(ch)
            elif ch_type == 'ao':
                self.ch_dict[ch_type]['task'].ao_channels.add_ao_voltage_chan(ch)
            elif ch_type == 'di':
                self.ch_dict[ch_type]['task'].di_channels.add_di_chan(ch, line_grouping=LineGrouping.CHAN_PER_LINE)
            else:  # if ch_type == 'do':
                self.ch_dict[ch_type]['task'].do_channels.add_do_chan(ch, line_grouping=LineGrouping.CHAN_PER_LINE)
            self.ch_dict[ch_type]['chs'].append(ch)
        if ch_type == 'ai':
            self._update_ai_ch_timing()
        self.task_channels_changed.emit(ch_type, self.ch_dict[ch_type]['chs'])

    def _update_ai_ch_timing(self):
        self.ch_dict['ai']['task'].input_buf_size = 10240
        self.ch_dict['ai']['task'].timing.cfg_samp_clk_timing(5000,
                                                              sample_mode=nidaqmx.constants.AcquisitionType.FINITE,
                                                              samps_per_chan=1024)
        self.ch_dict['ai']['task'].in_stream.read_all_avail_samp = True

    def add_task_channel(self, ch_type: str, ch):
        if ch_type not in self.ch_dict.keys():
            nidaq_logger.error(f'Unsupported {ch_type}', extra={"component": "NIDAQ"})
            raise ValueError(f'Unsupported channel type {ch_type}')

        if ch not in self.ch_dict[ch_type]['chs']:
            nidaq_logger.debug(f'Adding {ch} to {ch_type} task', extra={"component": "NIDAQ"})
            if ch_type == 'ai':
                if ch in self.ch_term_dict.keys():
                    nidaq_logger.debug(f'{self.ch_term_dict[ch]}', extra={"component": "NIDAQ"})
                    if self.ch_term_dict[ch] == "Differential":
                        self.ch_dict[ch_type]['task'].ai_channels\
                            .add_ai_voltage_chan(ch, terminal_config=TerminalConfiguration.DIFFERENTIAL)
                    elif self.ch_term_dict[ch] == "RSE":
                        self.ch_dict[ch_type]['task'].ai_channels\
                            .add_ai_voltage_chan(ch, terminal_config=TerminalConfiguration.RSE)
                    elif self.ch_term_dict[ch] == "NRSE":
                        self.ch_dict[ch_type]['task'].ai_channels\
                            .add_ai_voltage_chan(ch, terminal_config=TerminalConfiguration.NRSE)
                    else:
                        self.ch_dict[ch_type]['task'].ai_channels.add_ai_voltage_chan(ch)
                else:
                    self.ch_dict[ch_type]['task'].ai_channels.add_ai_voltage_chan(ch)
            elif ch_type == 'ao':
                self.ch_dict[ch_type]['task'].ao_channels.add_ao_voltage_chan(ch, min_val=0, max_val=10)
            elif ch_type == 'di':
                self.ch_dict[ch_type]['task'].di_channels.add_di_chan(ch, line_grouping=LineGrouping.CHAN_PER_LINE)
            else:  # if ch_type == 'do':
                self.ch_dict[ch_type]['task'].do_channels.add_do_chan(ch, line_grouping=LineGrouping.CHAN_PER_LINE)
            self.ch_dict[ch_type]['chs'].append(ch)
            if ch_type == 'ai':
                self._update_ai_ch_timing()
            self.task_channels_changed.emit(ch_type, self.ch_dict[ch_type]['chs'])

    def remove_task_channel(self, ch_type: str, ch):
        if ch_type not in self.ch_dict.keys():
            nidaq_logger.error(f'Unsupported {ch_type}', extra={"component": "NIDAQ"})
            raise ValueError(f'Unsupported channel type {ch_type}')

        if ch in self.ch_dict[ch_type]['chs']:
            nidaq_logger.debug(f'Removing {ch} from {ch_type} task', extra={'component': 'NIDAQ'})
            chs = self.ch_dict[ch_type]['chs'][:]
            chs.remove(ch)
            self.set_task_channels(ch_type, chs)

    def read_task_channels(self, ch_type: str, n_samples: int = 1):
        if ch_type not in ('ai', 'di'):
            nidaq_logger.error(f"Can't read {ch_type}", extra={"component": "NIDAQ"})
            return {}

        if len(self.ch_dict[ch_type]['chs']) == 0:
            res = {}
        elif len(self.ch_dict[ch_type]['chs']) == 1:
            res = {self.ch_dict[ch_type]['chs'][0]:
                       np.array(self.ch_dict[ch_type]['task'].read(n_samples) if n_samples != 1 else
                           self.ch_dict[ch_type]['task'].read(n_samples))}
        else:
            res = {c: v for c, v in zip(self.ch_dict[ch_type]['chs'],
                                        [np.array(x) for x in self.ch_dict[ch_type]['task'].read(n_samples)]
                                        if n_samples != 1 else
                                        self.ch_dict[ch_type]['task'].read(n_samples))}

            if ch_type == 'ai':
                for c in res.keys():
                    if c in self.ch_term_dict.keys() and self.ch_term_dict[c] == "Differential":
                        c_d = self.get_ai_corresponding_diff_ch(c)
                        if c_d is not None:
                            # nidaq_logger.debug(f"Differential {c} ({res[c]}) + {c_d} ({res[c_d]})", extra={"component": "NIDAQ"})
                            res[c] = res[c] + res[c_d]

        self.ai_values_changed.emit(res)
        return res

    def write_task_channels(self, ch_type: str, ch_value_dict: dict):
        if ch_type not in ('ao', 'do'):
            nidaq_logger.error(f"Can't write {ch_type}", extra={"component": "NIDAQ"})
            return {}

        default_values = {c: 0 if ch_type == 'ao' else False for c in self.ch_dict[ch_type]['chs']}
        for key, value in ch_value_dict.items():
            if key in default_values.keys():
                default_values[key] = value

        values = [default_values[key] for key in self.ch_dict[ch_type]['chs']]
        nidaq_logger.debug(f"Writing {ch_type} {ch_value_dict} {values}", extra={"component": "NIDAQ"})
        self.ch_dict[ch_type]['task'].write(values, auto_start=True)
        self.ao_values_changed.emit(default_values)

    def change_ch_term(self, ch_type: str, ch_name: str, term: str):
        nidaq_logger.debug(f"Setting {ch_type} {ch_name} {term}", extra={"component": "NIDAQ"})
        self.ch_term_dict[ch_name] = term

    def get_ai_corresponding_diff_ch(self, ch_name: str):
        total_lines = len(self.get_ai_channels())
        ch_name_reg = r'(?P<ch_prefix>.*)(?P<ch_id>\d+)'
        ch_name_m = re.match(ch_name_reg, ch_name)
        ch_id = int(ch_name_m.group('ch_id'))
        if 0 <= ch_id < total_lines/2:
            return f"{ch_name_m.group('ch_prefix')}{int(ch_id+total_lines/2)}"
        else:
            return None

    def get_current_settings(self):
        return f"[FIXME]: Using NI device {self.dev_name} ..."

    @staticmethod
    def get_nidaq_devices():
        return [dev.name for dev in nidaqmx.system.System.local().devices]

    def show_config_window(self):
        if self.config_window is None:
            self.config_window = NIDAQConfigWindow(self)

        self.config_window.show()


class NIDAQConfigWindow(Ui_NIDAQ_Config_Window):
    def __init__(self, nidaq_man: NIDAQDevMan):
        self.nidaq_man = nidaq_man
        self.window = QWidget()
        Ui_NIDAQ_Config_Window.__init__(self)
        self.setupUi(self.window)
        self.comboBox_Device.clear()
        devices = NIDAQDevMan.get_nidaq_devices()
        for dev in devices:
            self.comboBox_Device.addItem(dev)

        if self.nidaq_man.is_open():
            self.comboBox_Device.setCurrentText(self.nidaq_man.dev_name)
        else:
            self.nidaq_man.dev_name = self.comboBox_Device.currentText()

        self.pushButton_Conn.clicked.connect(self.open_clicked)
        self.chs_widget_dict = {'ai': {'parent': self.gridLayout_AiChs, 'chs_dict': {}},
                                'ao': {'parent': self.gridLayout_AoChs, 'chs_dict': {}},
                                'di': {'parent': self.gridLayout_DiChs, 'chs_dict': {}},
                                'do': {'parent': self.gridLayout_DoChs, 'chs_dict': {}}}
        self.pushButton_ReadAi.clicked.connect(self.sync_ai_values)
        self.pushButton_ReadDi.clicked.connect(self.sync_di_values)
        self.pushButton_WriteAo.clicked.connect(self.sync_ao_values)
        self.pushButton_WriteDo.clicked.connect(self.sync_do_values)

    def open_clicked(self, b_checked):
        if b_checked:
            self.nidaq_man.open(self.comboBox_Device.currentText())
            if self.nidaq_man.is_open():
                nidaq_logger.info(f"{self.nidaq_man.dev_name} opened", extra={"component": "NIDAQ"})
                self.populate_channel_list()
                self.groupBox_Control.setEnabled(True)
                self.pushButton_Conn.setText("Close")
                self.label_Conn_Status.setStyleSheet("background: green")
            else:
                nidaq_logger.error(f"Failed to open {self.nidaq_man.dev_name}", extra={"component": "NIDAQ"})
        else:
            self.nidaq_man.close()
            self.pushButton_Conn.setText("Open")
            self.label_Conn_Status.setStyleSheet("background: red")
            nidaq_logger.info(f"{self.nidaq_man.dev_name} closed", extra={"component": "NIDAQ"})
            self.groupBox_Control.setEnabled(False)

    def sync_ai_values(self):
        ch_dict = self.nidaq_man.read_task_channels('ai')
        for c, v in ch_dict.items():
            if c in self.chs_widget_dict['ai']['chs_dict'].keys():
                line_edit = self.chs_widget_dict['ai']['chs_dict'][c][3][0]
                line_edit.setText(f"{np.average(v):.4f}")

    def sync_di_values(self):
        ch_dict = self.nidaq_man.read_task_channels('di')
        for c, v in ch_dict.items():
            if c in self.chs_widget_dict['di']['chs_dict'].keys():
                spin_box: QtWidgets.QSpinBox = self.chs_widget_dict['di']['chs_dict'][c][3][0]
                spin_box.setValue(1 if v[-1] else 0)

    def sync_ao_values(self):
        ch_value_dict = {}
        for channel_name, (ch_type, ch_w_label, ch_w_enable, ch_w) in self.chs_widget_dict['ao']['chs_dict'].items():
            if ch_w_enable.isChecked():
                ch_w_value = ch_w[0]
                ch_value = ch_w_value.value()
                ch_value_dict[channel_name] = ch_value

        self.nidaq_man.write_task_channels('ao', ch_value_dict)

    def sync_do_values(self):
        ch_value_dict = {}
        for channel_name, (ch_type, ch_w_label, ch_w_enable, ch_w) in self.chs_widget_dict['do']['chs_dict'].items():
            if ch_w_enable.isChecked():
                ch_w_value = ch_w[0]
                ch_value = ch_w_value.value() == 1
                ch_value_dict[channel_name] = ch_value

        self.nidaq_man.write_task_channels('do', ch_value_dict)

    def populate_channel_list(self):
        for ch_type in self.chs_widget_dict.keys():
            parent_widget: QtWidgets.QGridLayout = self.chs_widget_dict[ch_type]['parent']
            widget_dict = self.chs_widget_dict[ch_type]['chs_dict']
            for ch_name, (ch_type, ch_w_label, ch_w_enable, ch_w) in widget_dict.items():
                parent_widget.removeWidget(ch_w_label)
                parent_widget.removeWidget(ch_w_enable)
                for ch_w_s in ch_w:
                    parent_widget.removeWidget(ch_w_s)

            widget_dict.clear()

        for ch_type in self.chs_widget_dict.keys():
            parent_widget: QtWidgets.QGridLayout = self.chs_widget_dict[ch_type]['parent']
            widget_dict = self.chs_widget_dict[ch_type]['chs_dict']
            if ch_type == 'ai':
                chs = self.nidaq_man.get_ai_channels()
            elif ch_type == 'ao':
                chs = self.nidaq_man.get_ao_channels()
            elif ch_type == 'di':
                chs = self.nidaq_man.get_di_lines()
            elif ch_type == 'do':
                chs = self.nidaq_man.get_do_lines()
            else:
                raise ValueError(f'Unknown channel type {ch_type}')

            row_index = 0

            for ch in chs:
                label = QtWidgets.QLabel(self.groupBox_Control)
                label.setText(ch)
                label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                parent_widget.addWidget(label, row_index, 0, 1, 1)
                chbox_enable = QtWidgets.QCheckBox(self.groupBox_Control)
                chbox_enable.setText("Enable")
                # FIXME: needs unified function
                chbox_enable.toggled.connect(
                    lambda b_checked, c_t=ch_type, c_name=ch:
                    self.nidaq_man.add_task_channel(c_t, c_name) if b_checked else
                    self.nidaq_man.remove_task_channel(c_t, c_name))
                parent_widget.addWidget(chbox_enable, row_index, 1, 1, 1)
                if ch_type == 'ai':
                    line_edit = QtWidgets.QLineEdit(self.groupBox_Control)
                    line_edit.setReadOnly(True)
                    parent_widget.addWidget(line_edit, row_index, 2, 1, 1)
                    combbox_term = QtWidgets.QComboBox(self.groupBox_Control)
                    if row_index < len(chs) / 2:
                        combbox_term.addItems(["Auto", "Differential", "RSE", "NRSE"])
                    else:
                        combbox_term.addItems(["Auto", "RSE", "NRSE"])
                    combbox_term.currentTextChanged.connect(
                        lambda term, c_t=ch_type, c_name=ch: self.nidaq_man.change_ch_term(c_t, c_name, term))
                    ctrl_w = [line_edit, combbox_term]
                elif ch_type == 'ao':
                    spin_box = QtWidgets.QDoubleSpinBox(self.groupBox_Control)
                    spin_box.setMaximum(10)
                    spin_box.setMinimum(0)
                    spin_box.setSingleStep(0.01)
                    ctrl_w = [spin_box, ]
                elif ch_type == 'di':
                    spin_box = QtWidgets.QSpinBox(self.groupBox_Control)
                    spin_box.setMinimum(0)
                    spin_box.setMaximum(1)
                    spin_box.setSingleStep(1)
                    spin_box.setReadOnly(True)
                    ctrl_w = [spin_box, ]
                else:  # do
                    spin_box = QtWidgets.QSpinBox(self.groupBox_Control)
                    spin_box.setMinimum(0)
                    spin_box.setMaximum(1)
                    spin_box.setSingleStep(1)
                    ctrl_w = [spin_box, ]

                col_index = 2
                for ctrl in ctrl_w:
                    parent_widget.addWidget(ctrl, row_index, col_index, 1, 1)
                    col_index = col_index + 1
                widget_dict[ch] = (ch_type, label, chbox_enable, ctrl_w)
                row_index += 1

    def show(self):
        self.window.show()

    def close(self):
        self.window.hide()


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])

    nidaq_man = NIDAQDevMan()
    print(f'Starting...')
    nidaq_man.show_config_window()
    QApplication.instance().exec_()
