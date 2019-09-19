#!/usr/bin/python3

import nidaqmx
import logging
from .nidaq_config_ui import Ui_NIDAQ_Config_Window
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QObject, pyqtSignal


_SPLIT_LOG = False

if _SPLIT_LOG:
    nidaq_logger = logging.getLogger("nidaq")
    nidaq_logger.setLevel(logging.DEBUG)
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
    ao_channels_changed = pyqtSignal(name="aoChannelsChanged")
    ai_channels_changed = pyqtSignal(name="aiChannelsChanged")
    ai_values_changed = pyqtSignal(dict, name="aiValuesChanged")

    def __init__(self, dev_name: str = "Dev1"):
        super().__init__()
        self.dev_name = dev_name
        self._ni_sys = nidaqmx.system.System.local()
        self.device = None  # self._ni_sys.devices[self._dev_name]
        self._ai_task = None  # nidaqmx.Task()
        self._ao_task = None  # nidaqmx.Task()
        self._ai_chs = []
        self._ao_chs = []
        self.config_window = None

    def open(self, dev_name: str = None):
        if dev_name is None:
            if self.dev_name is not None:
                self.device = self._ni_sys.devices[self.dev_name]
        else:
            self.dev_name = dev_name
            self.device = self._ni_sys.devices[self.dev_name]
        self._ai_chs = []
        self._ao_chs = []
        self._ai_task = nidaqmx.Task()
        self._ao_task = nidaqmx.Task()
        self.opened.emit()
        return self._ni_sys.driver_version

    def is_open(self):
        return self.device is not None

    def close(self):
        if self._ai_task is not None:
            self._ai_task.close()
            self._ai_task = None
        if self._ao_task is not None:
            self._ao_task.close()
            self._ao_task = None
        self.closed.emit()

    def get_ai_channels(self):
        return [ch.name for ch in self.device.ai_physical_chans]

    def get_ao_channels(self):
        return [ch.name for ch in self.device.ao_physical_chans]

    def get_ai_task_channels(self):
        return self._ai_chs

    def get_ao_task_channels(self):
        return self._ao_chs

    def set_ai_task_channels(self, chs):
        self._ai_task.close()
        self._ai_task = nidaqmx.Task()
        for ch in set(chs):
            self._ai_task.ai_channels.add_ai_voltage_chan(ch)
        self.get_ai_task_channels()
        self.ai_channels_changed.emit()

    def set_ao_task_channels(self, chs):
        self._ao_task.close()
        self._ao_task = nidaqmx.Task()
        for ch in set(chs):
            self._ao_task.ao_channels.add_ao_voltage_chan(ch)
        self.get_ao_task_channels()
        self.ao_channels_changed.emit()

    def add_ai_channel(self, ch):
        global nidaq_logger
        if ch not in self._ai_chs:
            nidaq_logger.debug(f"Adding AI channel {ch}", extra={"component": "NIDAQ"})
            self._ai_chs.append(ch)
            self._ai_task.ai_channels.add_ai_voltage_chan(ch)
            self.ai_channels_changed.emit()

    def remove_ai_channel(self, ch):
        global nidaq_logger
        if ch in self._ai_chs:
            self._ai_chs.remove(ch)
            nidaq_logger.debug(f"Removing AI channel {ch}", extra={"component": "NIDAQ"})
        self.set_ai_task_channels(self._ai_chs)

    def add_ao_channel(self, ch):
        global nidaq_logger
        if ch not in self._ao_chs:
            nidaq_logger.debug(f"Adding AO channel {ch}", extra={"component": "NIDAQ"})
            self._ao_chs.append(ch)
            self._ao_task.ao_channels.add_ao_voltage_chan(ch)
            self.ao_channels_changed.emit()

    def remove_ao_channel(self, ch):
        global nidaq_logger
        if ch in self._ao_chs:
            self._ao_chs.remove(ch)
            nidaq_logger.debug(f"Removing AO channel {ch}", extra={"component": "NIDAQ"})
        self.set_ao_task_channels(self._ao_chs)

    def read_ai_channels(self):
        res = None
        if len(self._ai_chs) == 0:
            res = {}
        elif len(self._ai_chs) == 1:
            res = {self._ai_chs[0]: self._ai_task.read()}
        else:
            res = {c: v for c, v in zip(self._ai_chs, self._ai_task.read())}

        self.ai_values_changed.emit(res)
        return res

    def write_ao_channels(self, ch_value_dict: dict):
        global nidaq_logger
        default_values = {c: 0.0 for c in self._ao_chs}
        for key, value in ch_value_dict.items():
            if key in default_values.keys():
                default_values[key] = value

        values = [default_values[key] for key in self._ao_chs]
        nidaq_logger.debug(f"Writing AO {ch_value_dict}", extra={"component": "NIDAQ"})
        self._ao_task.write(values, auto_start=True)

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
        self.channel_widget_dict = {}
        self.pushButton_Sync.clicked.connect(self.sync_ai_values)

    def open_clicked(self, b_checked):
        global nidaq_logger
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
        ch_dict = self.nidaq_man.read_ai_channels()
        for c, v in ch_dict.items():
            if c in self.channel_widget_dict.keys():
                line_edit = self.channel_widget_dict[c][3]
                line_edit.setText(f"{v:.4f}")

    def sync_ao_values(self):
        ch_value_dict = {}
        for channel_name, (ch_type, ch_w_label, ch_w_enable, ch_w_value) in self.channel_widget_dict.items():
            if ch_type == 'o' and ch_w_enable.isChecked():
                ch_value = ch_w_value.value()
                ch_value_dict[channel_name] = ch_value

        self.nidaq_man.write_ao_channels(ch_value_dict)

    def populate_channel_list(self):
        for channel_name, (ch_type, ch_w_label, ch_w_enable, ch_w_value) in self.channel_widget_dict.items():
            self.gridLayout_Channels.removeWidget(ch_w_label)
            self.gridLayout_Channels.removeWidget(ch_w_enable)
            self.gridLayout_Channels.removeWidget(ch_w_value)

        self.channel_widget_dict.clear()
        ai_channels = self.nidaq_man.get_ai_channels()
        row_index = 0
        for ai_ch in ai_channels:
            label = QtWidgets.QLabel(self.groupBox_Control)
            label.setText(ai_ch)
            label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.gridLayout_Channels.addWidget(label, row_index, 0, 1, 1)
            chbox_enable = QtWidgets.QCheckBox(self.groupBox_Control)
            chbox_enable.setText("Enable")
            chbox_enable.toggled.connect(
                lambda b_checked, ch_name=ai_ch: self.nidaq_man.add_ai_channel(ch_name) if b_checked else
                self.nidaq_man.remove_ai_channel(ch_name))
            self.gridLayout_Channels.addWidget(chbox_enable, row_index, 1, 1, 1)
            line_edit = QtWidgets.QLineEdit(self.groupBox_Control)
            line_edit.setReadOnly(True)
            self.gridLayout_Channels.addWidget(line_edit, row_index, 2, 1, 1)
            self.channel_widget_dict[ai_ch] = ('i', label, chbox_enable, line_edit)
            row_index += 1

        ao_channels = self.nidaq_man.get_ao_channels()
        for ao_ch in ao_channels:
            label = QtWidgets.QLabel(self.groupBox_Control)
            label.setText(ao_ch)
            label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            self.gridLayout_Channels.addWidget(label, row_index, 0, 1, 1)
            chbox_enable = QtWidgets.QCheckBox(self.groupBox_Control)
            chbox_enable.setText("Enable")
            chbox_enable.toggled.connect(
                lambda b_checked, ch_name=ao_ch: self.nidaq_man.add_ao_channel(ch_name) if b_checked else
                self.nidaq_man.remove_ao_channel(ch_name))
            self.gridLayout_Channels.addWidget(chbox_enable, row_index, 1, 1, 1)
            spin_box = QtWidgets.QDoubleSpinBox(self.groupBox_Control)
            spin_box.setMaximum(10)
            spin_box.setMinimum(0)
            spin_box.setSingleStep(0.01)
            self.gridLayout_Channels.addWidget(spin_box, row_index, 2, 1, 1)
            spin_box.valueChanged.connect(self.sync_ao_values)
            self.channel_widget_dict[ao_ch] = ('o', label, chbox_enable, spin_box)
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
