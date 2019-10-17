#!/usr/bin/python3

# Original code from: https://github.com/heeres/qtlab/blob/master/instrument_plugins/Fianium_AOTF.py

# FIXME: no check, no verification

import ctypes
import logging
from .aotf_config_ui import Ui_AOTF_Config_Window
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QTimer, QDir
import os
import traceback
from PyQt5.QtCore import QObject, pyqtSignal
from .Aotf64 import Aotf64

_SPLIT_LOG = False

if _SPLIT_LOG:
    aotf_logger = logging.getLogger("aotf")
    aotf_logger.setLevel(logging.DEBUG)
    aotf_fh = logging.FileHandler("aotf.log")
    aotf_formatter = logging.Formatter('%(asctime)s [%(component)s] - %(levelname)s - %(message)s')
    aotf_fh.setFormatter(aotf_formatter)
    aotf_logger.addHandler(aotf_fh)

    aotf_ch = logging.StreamHandler()
    aotf_ch.setFormatter(aotf_formatter)
    aotf_logger.addHandler(aotf_ch)
else:
    aotf_logger = logging.getLogger("autools_setup_main")


# FIXME: Should follow the dll wrapper log
class FianiumAOTFMan(QObject):
    """
    Helper class for the Fianium AOTF
    """

    MAX_POWER = 16383
    # TODO: Verify
    VIS_CAL_TUNING = [7.638000E+2, -2.600000E+0, 3.469000E-3, -1.635000E-6]
    NIR1_CAL_TUNING = [3.602000E+2, -7.491000E-1, 6.420000E-4, -1.979000E-7]
    NIR2_CAL_TUNING = [7.638000E+2, -2.600000E+0, 3.469000E-3, -1.635000E-6]

    VIS_MIN = 450
    VIS_MAX = 700
    NIR1_MIN = 650
    NIR1_MAX = 1100
    NIR2_MIN = 1100
    NIR2_MAX = 2200

    # 400 - 650nm
    VIS_OPT_POWER = (
        (370, 600, 5600),
        (600, 670, 6000)
    )
    # 650 - 1100nm
    NIR1_OPT_POWER = (
        (600, 670, 3800),
        (670, 740, 3600),
        (740, 810, 3800),
        (810, 880, 4000),
        (880, 950, 4400),
        (950, 1020, 4600),
        (1020, 1100, 4900)
    )
    # 1100 - 2200nm
    NIR2_OPT_POWER = (
        (1100, 2300, 5570),
    )

    _FAKE_DEV = False

    opened = pyqtSignal()
    closed = pyqtSignal()
    wavelength_changed = pyqtSignal(int, int, name='wavelengthChanged')
    power_changed = pyqtSignal(int, int, name='powerChanged')

    def __init__(self, aotf_libpath: str = None):
        super().__init__()
        self.aotf_libpath = aotf_libpath
        if self.aotf_libpath is None:
            self.lib_aotf = None
        else:
            aotf_logger.debug(f"Loading AOTF Library DLL {aotf_libpath}", extra={"component": "AOTF"})
            self.lib_aotf = Aotf64(lib_path=self.aotf_libpath)
        self.h_devices = [0, 0]
        self.dev_modes = ["", ""]
        self.dev_serials = ["", ""]
        self.curr_wavelength = 0
        self.curr_power = 0
        self.curr_aotf_dev = None
        self.config_window = None

    def open(self):
        global aotf_logger
        aotf_logger.info(f"Opening AOTF connection (dual AOTF mode)", extra={"component": "AOTF"})

        if not FianiumAOTFMan._FAKE_DEV:
            if self.lib_aotf is None:
                if self.aotf_libpath is not None:
                    try:
                        aotf_logger.debug(f"Loading AOTF Library DLL {self.aotf_libpath}", extra={"component": "AOTF"})
                        self.lib_aotf = Aotf64(lib_path=self.aotf_libpath)
                    except Exception as e:
                        traceback.print_tb(e.__traceback__)
                        self.lib_aotf = None
                else:
                    self.lib_aotf = None

            if self.lib_aotf is None:
                aotf_logger.error(f"Unable to load the AOTF library", extra={"component": "AOTF"})
                return 0

        self.h_devices = [0, 0]
        for dev_id in range(0, 2):
            if not FianiumAOTFMan._FAKE_DEV:
                h_dev = self.lib_aotf.open(dev_id)
            else:
                h_dev = dev_id + 1

            if h_dev != 0:
                self.send_cmd(h_dev, "\r")
                self.send_cmd(h_dev, f"dau en;mod dac * {FianiumAOTFMan.MAX_POWER}\r")
                self.send_cmd(h_dev, "dds fsk * 0\r")
                # set all channels power to 0
                for i in range(0, 8):
                    self.send_cmd(h_dev, f"dds a {i} 0\r")
                aotf_logger.info(f"Device {dev_id} Opened, MAX_POWER {FianiumAOTFMan.MAX_POWER}, "
                                 f"all channels power set to 0",
                                 extra={"component": "AOTF"})
                self.h_devices[dev_id] = h_dev
                self.dev_serials[dev_id] = self.get_board_serial(h_dev)
            else:
                aotf_logger.error(f"Failed to open device {dev_id}", extra={"component": "AOTF"})
                self.h_devices[dev_id] = 0

        if self.h_devices[0] != 0 or self.h_devices[1] != 0:
            if self.h_devices[0] != 0:
                self.curr_aotf_dev = 0
            else:
                self.curr_aotf_dev = 1
            self.opened.emit()

        return self.h_devices

    def is_open(self):
        return self.h_devices[0] != 0 or self.h_devices[1] != 0

    def close(self):
        global aotf_logger
        if FianiumAOTFMan._FAKE_DEV:
            aotf_logger.info(f"All channels power set to 0, device closed", extra={"component": "AOTF"})
            self.closed.emit()
            return

        for h_dev in self.h_devices:
            if h_dev != 0:
                self.send_cmd(h_dev, "dds fsk * 0\r")
                # set all channels power to 0
                for i in range(0, 8):
                    self.send_cmd(h_dev, f"dds a {i} 0\r")
                self.lib_aotf.close(h_dev)
                aotf_logger.info(f"All channels of {h_dev} power set to 0, device closed", extra={"component": "AOTF"})

        self.closed.emit()
        self.dispose()
        self.h_devices = [0, 0]
        self.dev_serials = ["", ""]
        self.dev_modes = ["", ""]

    def dispose(self):
        self.lib_aotf.shutdown_server32(kill_timeout=5)
        del self.lib_aotf
        self.lib_aotf = None

    def send_cmd(self, h_dev, cmd: str):
        global aotf_logger
        cmd_replaced = cmd.replace('\r', '\\r')
        aotf_logger.debug(f"Sending cmd <{cmd_replaced}> to {h_dev}", extra={"component": "AOTF"})

        if FianiumAOTFMan._FAKE_DEV:
            return

        ret = self.lib_aotf.command(h_dev, cmd)
        aotf_logger.debug(f"Got <{ret}>", extra={"component": "AOTF"})
        return ret

    def get_board_serial(self, h_dev):
        if FianiumAOTFMan._FAKE_DEV:
            if h_dev == self.h_devices[0]:
                return "BOARD1"
            elif h_dev == self.h_devices[1]:
                return "BOARD2"
            else:
                return "N/A"

        return self.send_cmd(h_dev, "boardid serial\r")

    def get_board_version(self, h_dev):
        return self.send_cmd(h_dev, "boardid version\r")

    def set_mode(self, h_dev, mod: str):
        if h_dev == 0 or mod not in ("NIR1", "NIR2", "VIS"):
            return
        if h_dev == self.h_devices[0]:
            self.dev_modes[0] = mod
            self.set_calibration(h_dev, mod)
        elif h_dev == self.h_devices[1]:
            self.dev_modes[1] = mod
            self.set_calibration(h_dev, mod)

    def set_calibration(self, h_dev, mode: str):
        if mode == "VIS":
            cal_params = FianiumAOTFMan.VIS_CAL_TUNING
        elif mode == "NIR2":
            cal_params = FianiumAOTFMan.NIR2_CAL_TUNING
        elif mode == "NIR1":
            cal_params = FianiumAOTFMan.NIR1_CAL_TUNING
        else:
            return

        for i in range(0, 4):
            self.send_cmd(h_dev, f"cal tuning {i} {cal_params[i]:g}\r")
        return

    def is_wavelength_available(self, wlen):
        mods = []
        if FianiumAOTFMan.VIS_MIN <= wlen <= FianiumAOTFMan.VIS_MAX:
            mods.append("VIS")

        if FianiumAOTFMan.NIR1_MIN <= wlen <= FianiumAOTFMan.NIR1_MAX:
            mods.append("NIR1")

        if FianiumAOTFMan.NIR2_MIN <= wlen <= FianiumAOTFMan.NIR2_MAX:
            mods.append("NIR2")

        if self.dev_modes[0] in mods:
            h_dev = self.h_devices[0]
            return True, 0
        elif self.dev_modes[1] in mods:
            h_dev = self.h_devices[1]
            return True, 1
        else:
            return False, None

    def set_wavelength(self, wlen: int, ch: int = 0):
        global aotf_logger
        if FianiumAOTFMan.VIS_MIN <= wlen <= FianiumAOTFMan.VIS_MAX:
            mod = "VIS"
        elif FianiumAOTFMan.NIR1_MIN <= wlen <= FianiumAOTFMan.NIR1_MAX:
            mod = "NIR1"
        elif FianiumAOTFMan.NIR2_MIN <= wlen <= FianiumAOTFMan.NIR2_MAX:
            mod = "NIR2"
        else:
            aotf_logger.error(f"{wlen} out of range (400, 2200)", extra={"component": "AOTF"})
            return False

        if self.dev_modes[0] == mod:
            curr_dev = 0
            h_dev = self.h_devices[0]
            aotf_logger.debug(f"Using AOTF1 {h_dev} to set wavelength to {wlen}", extra={"component": "AOTF"})
        elif self.dev_modes[1] == mod:
            curr_dev = 1
            h_dev = self.h_devices[1]
            aotf_logger.debug(f"Using AOTF2 {h_dev} to set wavelength to {wlen}", extra={"component": "AOTF"})
        else:
            aotf_logger.error(f"{wlen} unavailable with current AOTF", extra={"component": "AOTF"})
            return False

        if curr_dev != self.curr_aotf_dev:
            self.send_cmd(self.h_devices[self.curr_aotf_dev], "dds fsk * 0\r")  # Turn off the previous AOTF
            self.curr_aotf_dev = curr_dev

        self.send_cmd(h_dev, f'dds f {ch} #{wlen:d} \r')
        self.wavelength_changed.emit(ch, wlen)
        return True

    def set_power_percent(self, pow_percent: float, ch: int = 0):
        val = int(pow_percent * FianiumAOTFMan.MAX_POWER)
        self.set_power(val, ch)

    def set_power(self, power: int, ch: int = 0):
        self.send_cmd(self.h_devices[self.curr_aotf_dev], f"dds a {ch} {min(power, FianiumAOTFMan.MAX_POWER)}\r")
        self.power_changed.emit(ch, min(power, FianiumAOTFMan.MAX_POWER))

    def set_wavelength_opt_power(self, wlen: int, ch: int = 0):
        opt_power = self.get_wavelength_opt_power(wlen)
        if opt_power is not None:
            self.send_cmd(self.h_devices[self.curr_aotf_dev], f"dds a {ch} {opt_power}\r")

    def get_wavelength_opt_power(self, wlen: int, dev_index=None):
        global aotf_logger

        if dev_index is None:
            dev_index = self.curr_aotf_dev

        if dev_index is None:
            return None

        mod = self.dev_modes[dev_index]

        if mod == "VIS":
            min_wl = FianiumAOTFMan.VIS_MIN
            max_wl = FianiumAOTFMan.VIS_MAX
            opt_power_list = FianiumAOTFMan.VIS_OPT_POWER
        elif mod == "NIR1":
            min_wl = FianiumAOTFMan.NIR1_MIN
            max_wl = FianiumAOTFMan.NIR1_MAX
            opt_power_list = FianiumAOTFMan.NIR1_OPT_POWER
        elif mod == "NIR2":
            min_wl = FianiumAOTFMan.NIR2_MIN
            max_wl = FianiumAOTFMan.NIR2_MAX
            opt_power_list = FianiumAOTFMan.NIR2_OPT_POWER
        else:
            return None

        if not min_wl <= wlen <= max_wl:
            aotf_logger.error(f"{wlen} out of range of current dev "
                              f"{self.h_devices[dev_index]}@{dev_index}:"
                              f"{self.dev_modes[dev_index]}"
                              f"({min_wl}, {max_wl})", extra={"component": "AOTF"})
            return
        for low, high, opt_p in opt_power_list:
            if low <= wlen <= high:
                return opt_p
        return None

    def show_config_window(self):
        if self.config_window is None:
            self.config_window = AOTFConfigWindow(self)
        self.config_window.show()

    def get_current_settings(self, with_header: bool = True):
        if self.config_window is not None:
            return self.config_window.get_current_settings(with_header)
        else:
            return ""


class AOTFConfigWindow(Ui_AOTF_Config_Window):
    """
    TBA
    """
    def __init__(self, aotf_man: FianiumAOTFMan):
        self.aotf_man = aotf_man
        self.window = QWidget()
        Ui_AOTF_Config_Window.__init__(self)
        self.setupUi(self.window)
        self.pushButton_LibLoc.clicked.connect(self.locate_aotflib)
        self.pushButton_Conn.clicked.connect(self.aotf_connect_clicked)
        self.pushButton_SetPower.clicked.connect(self.set_power_clicked)
        self.pushButton_SetWaveLength.clicked.connect(self.set_wavelength_clicked)
        self.spinBox_WaveLength.valueChanged.connect(self.wavelength_changed)
        self.pushButton_SetOptimalPower.clicked.connect(self.set_opt_power_clicked)
        self.lineEdit_Power.returnPressed.connect(self.power_changed)
        self.doubleSpinBox_PowerPerc.valueChanged.connect(self.power_perc_changed)
        self.pushButton_SetPowerPerc.clicked.connect(self.set_power_clicked)
        self.comboBox_AOTF1Mode.currentTextChanged.connect(
            lambda t: self.aotf_man.set_mode(self.aotf_man.h_devices[0], t))
        self.comboBox_AOTF2Mode.currentTextChanged.connect(
            lambda t: self.aotf_man.set_mode(self.aotf_man.h_devices[1], t))
        self.wavelength_changed()

    def locate_aotflib(self):
        options = QFileDialog.Options()
        aotflib_fname, _ = QFileDialog.getOpenFileName(self.window, "Locate the AotfLibrary.dll", QDir.currentPath(),
                                                       "Aotf Library (AotfLibrary.dll)", options=options)
        if aotflib_fname:
            self.lineEdit_LibPath.setText(aotflib_fname)

    def aotf_connect_clicked(self, b_checked):
        global aotf_logger
        if b_checked:
            try:
                if not os.path.exists(self.lineEdit_LibPath.text()):
                    aotf_logger.error(f"Failed to locate the AOTF library DLL", extra={"component": "AOTF"})
                    raise ValueError(f"Invalid AOTF dll")
                else:
                    self.aotf_open_connection()
            except:
                self.pushButton_Conn.setChecked(False)
        else:
            self.aotf_close_connection()

    def aotf_open_connection(self):
        # TODO
        aotflib_fname = self.lineEdit_LibPath.text()
        self.aotf_man.aotf_libpath = aotflib_fname
        self.aotf_man.open()
        if self.aotf_man.is_open():
            self.pushButton_Conn.setText("Close")
            self.pushButton_Conn.setStyleSheet("background: green")
            self.groupBox_Config.setEnabled(True)
            self.label_Conn_Status.setStyleSheet("background: green")
            if self.aotf_man.h_devices[0] != 0:
                self.lineEdit_AOTF1Serial.setText(self.aotf_man.dev_serials[0])
                self.label_AOTF1_Status.setStyleSheet("background:green")
                self.comboBox_AOTF1Mode.setEnabled(True)
                self.comboBox_AOTF1Mode.setCurrentText("VIS")  # Default
                self.aotf_man.set_mode(self.aotf_man.h_devices[0], "VIS")
            else:
                self.label_AOTF1_Status.setStyleSheet("background:red")
                self.comboBox_AOTF1Mode.setEnabled(False)

            if self.aotf_man.h_devices[1] != 0:
                self.lineEdit_AOTF2Serial.setText(self.aotf_man.dev_serials[1])
                self.label_AOTF2_Status.setStyleSheet("background:green")
                self.comboBox_AOTF2Mode.setEnabled(True)
                self.comboBox_AOTF2Mode.setCurrentText("NIR1")  # Default
                self.aotf_man.set_mode(self.aotf_man.h_devices[1], "NIR1")
            else:
                self.label_AOTF2_Status.setStyleSheet("background:red")
                self.comboBox_AOTF2Mode.setEnabled(False)

            self.wavelength_changed()

    def aotf_close_connection(self):
        if self.aotf_man.is_open():
            self.aotf_man.close()
            self.groupBox_Config.setEnabled(False)
        self.pushButton_Conn.setText("Open")
        self.pushButton_Conn.setStyleSheet("")
        self.label_Conn_Status.setStyleSheet("background: red")
        self.comboBox_AOTF1Mode.setEnabled(False)
        self.label_AOTF1_Status.setStyleSheet("background:red")
        self.comboBox_AOTF2Mode.setEnabled(False)
        self.label_AOTF2_Status.setStyleSheet("background:red")

    def set_power_clicked(self):
        global aotf_logger
        try:
            power = int(self.lineEdit_Power.text())
        except:
            power = -1
        if 0 <= power <= FianiumAOTFMan.MAX_POWER:
            aotf_logger.info(f"Setting ch (0) power to {power}", extra={"component": "AOTF"})
            self.aotf_man.set_power(power)
        else:
            aotf_logger.error(f"Wrong power value {self.lineEdit_Power.text()}", extra={"component": "AOTF"})

    def set_wavelength_clicked(self):
        global aotf_logger
        wavel = self.spinBox_WaveLength.value()
        aotf_logger.info(f"Setting ch (0) wavelength to {wavel}", extra={"component": "AOTF"})
        self.aotf_man.set_wavelength(wavel)

    def wavelength_changed(self):
        wavel = self.spinBox_WaveLength.value()
        b_a, b_index = self.aotf_man.is_wavelength_available(wavel)
        if not b_a:
            self.spinBox_WaveLength.setStyleSheet("background: red")
        else:
            self.spinBox_WaveLength.setStyleSheet("")
            self.lineEdit_OptimalPower.setText(str(self.aotf_man.get_wavelength_opt_power(wavel, b_index)))

    def set_opt_power_clicked(self):
        global aotf_logger
        try:
            power = int(self.lineEdit_OptimalPower.text())
        except:
            power = -1
        if 0 <= power <= FianiumAOTFMan.MAX_POWER:
            aotf_logger.info(f"Setting ch (0) power to {power}", extra={"component": "AOTF"})
            self.aotf_man.set_power(power)
        else:
            aotf_logger.error(f"Wrong power value {self.lineEdit_OptimalPower.text()} [0, 16383]", extra={"component": "AOTF"})

    def power_changed(self):
        global aotf_logger
        try:
            p = int(self.lineEdit_Power.text())
            if 0 <= p <= FianiumAOTFMan.MAX_POWER:
                perc = p / FianiumAOTFMan.MAX_POWER * 100
                self.doubleSpinBox_PowerPerc.setValue(perc)
            else:
                raise ValueError(f"Invalid power value {p}")
        except:
            aotf_logger.error(f"Invalid power setting {self.lineEdit_Power.text()}")

    def power_perc_changed(self):
        global aotf_logger
        p = int(self.doubleSpinBox_PowerPerc.value() * FianiumAOTFMan.MAX_POWER / 100)
        self.lineEdit_Power.setText(f"{p}")

    def show(self):
        self.window.show()

    def close(self):
        self.window.hide()

    def get_current_settings(self, with_header: bool = True):
        if self.aotf_man.is_open():
            if with_header:
                setting_str = "--------NKT AOTF-------\n"
            else:
                setting_str = ""
            setting_str = setting_str + f"AOTF1: [{self.lineEdit_AOTF1Serial.text()}], " \
                                        f"{self.comboBox_AOTF1Mode.currentText()}\n" \
                          f"AOTF1: [{self.lineEdit_AOTF2Serial.text()}], {self.comboBox_AOTF2Mode.currentText()}\n" \
                          f"Wavelength: {self.spinBox_WaveLength.value()} nm\n" \
                          f"Optimal Power: {self.lineEdit_OptimalPower.text()}\n" \
                          f"Power: {self.lineEdit_Power.text()}\n" \
                          f"Power(%): {self.doubleSpinBox_PowerPerc.value()}\n"
            return setting_str
        else:
            return ""

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])

    aotf_man = FianiumAOTFMan()
    print(f'Starting...')
    aotf_man.show_config_window()
    QApplication.instance().exec_()
