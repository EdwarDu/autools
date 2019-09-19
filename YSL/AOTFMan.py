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
    aotf_logger = logging.getLogger("yslaotf")
    aotf_logger.setLevel(logging.DEBUG)
    aotf_fh = logging.FileHandler("yslaotf.log")
    aotf_formatter = logging.Formatter('%(asctime)s [%(component)s] - %(levelname)s - %(message)s')
    aotf_fh.setFormatter(aotf_formatter)
    aotf_logger.addHandler(aotf_fh)

    aotf_ch = logging.StreamHandler()
    aotf_ch.setFormatter(aotf_formatter)
    aotf_logger.addHandler(aotf_ch)
else:
    aotf_logger = logging.getLogger("autools_setup_main")


# FIXME: Should follow the dll wrapper log
class AOTFMan(QObject):
    """
    Helper class for the Fianium AOTF
    """

    MAX_POWER = 16383
    # TODO: Verify
    RF1_CAL_TUNING = [767.99000, -2.33515, 0.00283, -1.22334E-6]
    RF2_CAL_TUNING = [286.40267, -0.42251, 2.63119E-4, -5.96069E-8]

    RF1_MIN = 450
    RF1_MAX = 700
    RF2_MIN = 650
    RF2_MAX = 1100

    _FAKE_DEV = False

    opened = pyqtSignal()
    closed = pyqtSignal()
    wavelength_changed = pyqtSignal(int, int, name='wavelengthChanged')
    power_changed = pyqtSignal(int, float, name='powerChanged')

    def __init__(self, aotf_libpath: str = None):
        super().__init__()
        self.aotf_libpath = aotf_libpath
        if self.aotf_libpath is None:
            self.lib_aotf = None
        else:
            aotf_logger.debug(f"Loading AOTF Library DLL {aotf_libpath}", extra={"component": "AOTF"})
            self.lib_aotf = Aotf64(lib_path=self.aotf_libpath)
        self.h_device = 0
        self.config_window = None

    def open(self):
        aotf_logger.info(f"Opening AOTF connection", extra={"component": "AOTF"})
        if not AOTFMan._FAKE_DEV:
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

        dev_id = 0
        if not AOTFMan._FAKE_DEV:
            self.h_device = self.lib_aotf.open(dev_id)
        else:
            self.h_device = dev_id + 1

        if self.h_device != 0:
            self.send_cmd("dds amplitude 0 0\r")
            aotf_logger.info(f"Device {dev_id} Opened, power set to 0",
                             extra={"component": "AOTF"})
            self.opened.emit()
        else:
            aotf_logger.error(f"Failed to open device {dev_id}", extra={"component": "AOTF"})

        return self.h_device

    def is_open(self):
        return self.h_device != 0

    def close(self):
        if AOTFMan._FAKE_DEV:
            aotf_logger.info(f"All channels power set to 0, device closed", extra={"component": "AOTF"})
            self.closed.emit()
            return

        if self.h_device != 0:
            self.send_cmd("dds amplitude 0 0\r")
            self.lib_aotf.close(self.h_device)
            aotf_logger.info(f"AOTF {self.h_device} power set to 0, device closed", extra={"component": "AOTF"})

        self.closed.emit()
        self.dispose()
        self.h_device = 0

    def dispose(self):
        self.lib_aotf.shutdown_server32(kill_timeout=5)
        del self.lib_aotf
        self.lib_aotf = None

    def send_cmd(self, cmd: str):
        global aotf_logger
        cmd_replaced = cmd.replace('\r', '\\r')
        aotf_logger.debug(f"Sending cmd <{cmd_replaced}> to {self.h_device}", extra={"component": "AOTF"})

        if AOTFMan._FAKE_DEV:
            return

        ret = self.lib_aotf.command(self.h_device, cmd)
        aotf_logger.debug(f"Got <{ret}>", extra={"component": "AOTF"})
        return ret

    def get_board_serial(self):
        return self.send_cmd("boardid serial\r")

    def get_board_version(self,):
        return self.send_cmd("boardid version\r")

    @staticmethod
    def is_wavelength_available(wlen: int):
        if AOTFMan.RF1_MIN <= wlen <= AOTFMan.RF1_MAX or AOTFMan.RF2_MIN <= wlen <= AOTFMan.RF2_MAX:
            return True
        else:
            return False

    @staticmethod
    def calc_freq_from_wlen(wlen: int):
        if AOTFMan.RF1_MIN <= wlen <= AOTFMan.RF1_MAX:
            coeff = AOTFMan.RF1_CAL_TUNING
        elif AOTFMan.RF2_MIN <= wlen <= AOTFMan.RF2_MAX:
            coeff = AOTFMan.RF2_CAL_TUNING
        else:
            return None

        freq = coeff[0]  + coeff[1] * wlen + coeff[2]* wlen**2 + coeff[3] * wlen**3
        return freq

    def set_wavelength(self, wlen: int, ch: int = 0):
        freq = AOTFMan.calc_freq_from_wlen(wlen)
        self.send_cmd(f"dds frequency 0 !{freq:.1f}\r")
        self.wavelength_changed.emit(ch, wlen)
        return True

    def set_power_percent(self, pow_percent: float, ch: int = 0):
        val = pow_percent * AOTFMan.MAX_POWER
        self.set_power(val, ch)

    def set_power(self, power: float, ch: int = 0):
        self.send_cmd(f"dds amplitude {ch} {min(power, AOTFMan.MAX_POWER):.1f}\r")
        self.power_changed.emit(ch, min(power, AOTFMan.MAX_POWER))

    def show_config_window(self):
        if self.config_window is None:
            self.config_window = AOTFConfigWindow(self)
        self.config_window.show()


class AOTFConfigWindow(Ui_AOTF_Config_Window):
    """
    TBA
    """
    def __init__(self, aotf_man: AOTFMan):
        self.aotf_man = aotf_man
        self.window = QWidget()
        Ui_AOTF_Config_Window.__init__(self)
        self.setupUi(self.window)
        self.pushButton_LibLoc.clicked.connect(self.locate_aotflib)
        self.pushButton_Conn.clicked.connect(self.aotf_connect_clicked)
        self.pushButton_SetPower.clicked.connect(self.set_power_clicked)
        self.pushButton_SetWaveLength.clicked.connect(self.set_wavelength_clicked)
        self.spinBox_WaveLength.valueChanged.connect(self.wavelength_changed)
        self.doubleSpinBox_Power.valueChanged.connect(self.power_changed)
        self.doubleSpinBox_PowerPerc.valueChanged.connect(self.power_perc_changed)
        self.pushButton_SetPowerPerc.clicked.connect(self.set_power_clicked)
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
            self.wavelength_changed()

    def aotf_close_connection(self):
        if self.aotf_man.is_open():
            self.aotf_man.close()
            self.groupBox_Config.setEnabled(False)
        self.pushButton_Conn.setText("Open")
        self.pushButton_Conn.setStyleSheet("")
        self.label_Conn_Status.setStyleSheet("background: red")

    def set_power_clicked(self):
        try:
            power = self.doubleSpinBox_Power.value()
        except:
            power = -1
        if 0 <= power <= AOTFMan.MAX_POWER:
            aotf_logger.info(f"Setting ch (0) power to {power}", extra={"component": "AOTF"})
            self.aotf_man.set_power(power)
        else:
            aotf_logger.error(f"Wrong power value {power}", extra={"component": "AOTF"})

    def set_wavelength_clicked(self):
        global aotf_logger
        wavel = self.spinBox_WaveLength.value()
        aotf_logger.info(f"Setting ch (0) wavelength to {wavel}", extra={"component": "AOTF"})
        self.aotf_man.set_wavelength(wavel)

    def wavelength_changed(self):
        wavel = self.spinBox_WaveLength.value()
        if not self.aotf_man.is_wavelength_available(wavel):
            self.spinBox_WaveLength.setStyleSheet("background: red")
        else:
            self.spinBox_WaveLength.setStyleSheet("")

    def power_changed(self):
        global aotf_logger
        try:
            p = self.doubleSpinBox_Power.value()
            if 0 <= p <= AOTFMan.MAX_POWER:
                perc = p / AOTFMan.MAX_POWER * 100
                self.doubleSpinBox_PowerPerc.setValue(perc)
            else:
                raise ValueError(f"Invalid power value {p}")
        except:
            aotf_logger.error(f"Invalid power setting {self.doubleSpinBox_Power.value()}")

    def power_perc_changed(self):
        global aotf_logger
        p = self.doubleSpinBox_PowerPerc.value() * AOTFMan.MAX_POWER / 100
        self.doubleSpinBox_Power.setValue(p)

    def show(self):
        self.window.show()

    def close(self):
        self.window.hide()


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])

    aotf_man = AOTFMan()
    print(f'Starting...')
    aotf_man.show_config_window()
    QApplication.instance().exec_()
