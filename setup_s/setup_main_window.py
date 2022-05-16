#!/usr/bin/env python3

import sys
import traceback
import re
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QMessageBox
from PyQt5.QtCore import QTimer, QDir, pyqtSignal, pyqtSlot
import os
import time
import platform
import numpy as np

import threading
from threading import Thread, Event, Lock

from .setup_main_ui import Ui_SetupMainWindow

import serial
import serial.tools.list_ports
import logging

setup_main_logger = logging.getLogger("autools_setup_main")

setup_main_logger.setLevel(logging.DEBUG)
setup_main_logger_fh = logging.FileHandler("autools_setup_main.log")
setup_main_logger_formatter = logging.Formatter('%(asctime)s [%(component)s] - %(levelname)s - %(message)s')
setup_main_logger_fh.setFormatter(setup_main_logger_formatter)
setup_main_logger.addHandler(setup_main_logger_fh)

setup_main_logger_ch = logging.StreamHandler()
setup_main_logger_ch.setFormatter(setup_main_logger_formatter)
setup_main_logger.addHandler(setup_main_logger_ch)

_HAS_ANDOR = True
from ..Cameras.CVCameraMan import CVCameraMan
if _HAS_ANDOR:
    from ..Cameras.AndorCameraMan import AndorCameraMan
from .save_settings_window import SaveSettingsWindow
from ..CNILaser.FL266Man import FL266Man


# noinspection PyPep8Naming
def get_available_COMs():
    com_port_list = serial.tools.list_ports.comports()
    return {com.device: f'{com.manufacturer} {com.description}' for com in com_port_list}


def gen_2d_gaussian(width, height, sx=1, sy=1, mx=None, my=None):
    x = np.linspace(0, width, num=width)
    y = np.linspace(0, height, num=height)

    x, y = np.meshgrid(x, y)

    if mx is None:
        mx = width / 2
    if my is None:
        my = height / 2

    z = 1 / (2. * np.pi * sx * sy) * np.exp(-((x - mx) ** 2. / (2. * sx ** 2.) + (y - my) ** 2. / (2. * sy ** 2.)))

    z = (z-np.min(z)) / (np.max(z) - np.min(z)) * 256

    return z


class SetupMainWindow(Ui_SetupMainWindow):
    """
    Inherited from Ui_MainWindow to allow data source and signal/slot connection
    """
    def __init__(self):
        self.window = QMainWindow()
        Ui_SetupMainWindow.__init__(self)
        self.setupUi(self.window)

        # Laser Profiler
        self.pushButton_CamRefresh.clicked.connect(self.refresh_cam_source)
        self.pushButton_CamConn.clicked.connect(self.cam_conn_clicked)
        self.pushButton_CAM_Config.clicked.connect(self.cam_config_clicked)
        self.current_cam = None
        self.pushButton_Single.clicked.connect(self.cam_single_clicked)
        self.pushButton_FreeRun.clicked.connect(self.cam_freerun_clicked)
        self.pushButton_LP_AddMarker.clicked.connect(lambda: self.widget_LaserProfiler.add_cross_marker())
        self.pushButton_LP_ClearMarkers.clicked.connect(lambda: self.widget_LaserProfiler.remove_all_cross_markers())

        self.checkBox_LP_auto_crosshair.setChecked(self.widget_LaserProfiler.cross_hair_auto_hotspot)
        self.checkBox_LP_gaussian_force.setChecked(self.widget_LaserProfiler.gaussian_fit_force_peak)

        self.checkBox_LP_auto_crosshair.stateChanged.connect(
            lambda checked: self.widget_LaserProfiler.set_cross_hair_auto_hotspot(checked))
        self.checkBox_LP_gaussian_force.stateChanged.connect(
            lambda checked: self.widget_LaserProfiler.set_gaussian_fit_force_peak(checked))
        self.checkBox_LP_gaussian_manual.stateChanged.connect(
            lambda checked: self.widget_LaserProfiler.set_gaussian_fit_manual_mean(checked))
        self.doubleSpinBox_LP_RotateAngle.valueChanged.connect(self.lp_image_rotation_a_changed)
        
        self.spinBox_calcInputNumPixels.valueChanged.connect(self.calc_helper)
        self.spinBox_calcInputWaveLength.valueChanged.connect(self.calc_helper)
        self.doubleSpinBox_CalcInputLens.valueChanged.connect(self.calc_helper)

        self.pushButton_LP_LoadRaw.clicked.connect(self.lp_load_raw)
        self.widget_LaserProfiler.hprof_dsize_changed.connect(self.lp_hprof_d_changed)
        self.widget_LaserProfiler.vprof_dsize_changed.connect(self.lp_vprof_d_changed)

        self._pixel_size = 1
        self._lp_hprof_d = -1 # set the d values to -1 as invalid, res will result to negative value
        self._lp_vprof_d = -1 
        self.calc_helper() # This will calc init pixel size
        self.widget_LaserProfiler.refresh()  # this is force calculate d values

        # CNILaser Settings
        self.aotf_man = FL266Man()
        self.pushButton_AOTF_Config.clicked.connect(self.aotf_config_clicked)
        self.aotf_man.opened.connect(self.aotf_opened)
        self.aotf_man.closed.connect(self.aotf_closed)
        self.aotf_man.power_changed.connect(self.aotf_power_changed)
        self.aotf_man.frequency_changed.connect(self.aotf_frequency_changed)

        # AndorCam
        if _HAS_ANDOR:
            self.andor_man = AndorCameraMan(0)

        self.all_cams = []
        self.window.show()

    def calc_helper(self):
        # wavel = self.spinBox_calcInputWaveLength.value()
        lens = self.doubleSpinBox_CalcInputLens.value()* 1000.0
        pixels = self.spinBox_calcInputNumPixels.value()
        self._pixel_size = lens/pixels
        self.lineEdit_CalcPixelSize.setText(f"{self._pixel_size:.3f}")
        self.lp_hprof_d_changed(None)  # force to recalculate the res values
        self.lp_vprof_d_changed(None)

    def lp_hprof_d_changed(self, d):
        if d is not None:
            self._lp_hprof_d = d
        res = self._lp_hprof_d * self._pixel_size
        res_bar = res / self.spinBox_calcInputWaveLength.value()
        self.lineEdit_CalcHRes.setText(f"{res:.3f}")
        self.lineEdit_CalcHResBar.setText(f"{res_bar:.3f}")

    def lp_vprof_d_changed(self, d):
        if d is not None:
            self._lp_vprof_d = d
        res = self._lp_vprof_d * self._pixel_size
        res_bar = res / self.spinBox_calcInputWaveLength.value()
        self.lineEdit_CalcVRes.setText(f"{res:.3f}")
        self.lineEdit_CalcVResBar.setText(f"{res_bar:.3f}")
    
    def lp_image_rotation_a_changed(self, a):
        self.widget_LaserProfiler.img_rotate_angle = a

    def aotf_config_clicked(self):
        self.aotf_man.show_config_window()

    def aotf_opened(self):
        self.label_AOTF_Conn_Status.setStyleSheet("background: green")

    def aotf_closed(self):
        self.label_AOTF_Conn_Status.setStyleSheet("background: red")

    def aotf_power_changed(self, power_perc):
        self.label_AOTF_PowerPerc.setText(f"{power_perc}")

    def aotf_frequency_changed(self, freq):
        self.label_AOTF_Frequency.setText(f"{freq}")

    def refresh_cam_source(self):
        self.comboBox_CamSource.clear()
        self.all_cams = []
        all_cv_cams = CVCameraMan.get_all_cams()
        for cam in all_cv_cams:
            self.comboBox_CamSource.addItem(f"OpenCV Cam: {cam.cv_index}")
            self.all_cams.append(cam)

        if _HAS_ANDOR:
            try:
                n_andor_cams = self.andor_man.get_device_count()
                for i in range(0, n_andor_cams):
                    if i == 0:
                        self.comboBox_CamSource.addItem(f"Andor Cam: 0", self.andor_man)
                        self.all_cams.append(self.andor_man)
                    else:
                        andor_cam = AndorCameraMan(i)
                        self.comboBox_CamSource.addItem(f"Andor Cam: {andor_cam.get_dev_id()}", andor_cam)
                        self.all_cams.append(andor_cam)
            except Exception as e:
                pass

        try:
            self.comboBox_CamSource.setCurrentIndex(0)
        except:
            pass

    def cam_conn_clicked(self, state):
        if not state:
            if self.current_cam is not None:
                self.current_cam.close()
                self.current_cam = None
            # Enable/Disable Related Control
            self.comboBox_CamSource.setEnabled(True)
            self.pushButton_CamRefresh.setEnabled(True)
            self.pushButton_CamConn.setStyleSheet("")
            self.pushButton_CamConn.setText("Connect")
            self.pushButton_FreeRun.setEnabled(False)
            self.pushButton_Single.setEnabled(False)
            self.pushButton_CAM_Config.setEnabled(False)
        else:
            index = self.comboBox_CamSource.currentIndex()
            if not 0 <= index < len(self.all_cams):
                return

            self.current_cam = self.all_cams[index]
            if self.current_cam is None:
                return
            try:
                self.current_cam.open()
                if not self.current_cam.is_open():
                    return
            except:
                return

            frame_width, frame_height, frame_channels = self.current_cam.get_frame_size()
            self.comboBox_FrameSelect.clear()
            if frame_channels == 1:
                self.comboBox_FrameSelect.addItem("BW", 0)
            elif frame_channels == 3:
                self.comboBox_FrameSelect.addItem("Blue", 0)
                self.comboBox_FrameSelect.addItem("Green", 1)
                self.comboBox_FrameSelect.addItem("Red", 2)
                self.comboBox_FrameSelect.addItem("Grey", 3)
            # Enable/Disable related control
            self.comboBox_CamSource.setEnabled(False)
            self.pushButton_CamRefresh.setEnabled(False)
            self.pushButton_CamConn.setStyleSheet("background: green")
            self.pushButton_CamConn.setText("DisConn")
            self.pushButton_FreeRun.setEnabled(True)
            self.pushButton_Single.setEnabled(True)
            self.pushButton_CAM_Config.setEnabled(True)

    def cam_config_clicked(self):
        if self.current_cam is not None:
            self.current_cam.show_config_window()

    def cam_single_shot(self):
        if self.current_cam is not None:
            frame = self.current_cam.grab_frame(n_channel_index=self.comboBox_FrameSelect.currentData())
            if frame is not None:
                self.widget_LaserProfiler.update_image_data(frame)

            if self.pushButton_FreeRun.isChecked():
                # if camera is closed in middle of freerun, must exit freerun mode
                if self.current_cam.is_open():
                    QtWidgets.qApp.processEvents()
                    QTimer.singleShot(5, self.cam_single_shot)
                else:
                    self.pushButton_FreeRun.setChecked(False)
                    self.pushButton_FreeRun.setStyleSheet("")

    def cam_single_clicked(self):
        self.pushButton_FreeRun.setChecked(False)
        self.pushButton_FreeRun.setStyleSheet("")
        self.cam_single_shot()

    def cam_freerun_clicked(self, state):
        if not state:
            self.pushButton_FreeRun.setStyleSheet("")
        else:
            self.pushButton_FreeRun.setStyleSheet("background: green")
            self.cam_single_shot()

    def lp_load_raw(self):
        fname, _a = QFileDialog.getOpenFileName(self.window, caption='Load NPRAW/image file', 
            filter='Images (*.png *.jpg *.tif *.bmp);;NPRAW (*.npraw);;All files (*.*)')

        if fname is not None and fname != '':
            self.widget_LaserProfiler.load_raw(fname)

    def lp_pixel_size_changed(self, psz):
        self.widget_LaserProfiler.pixel_size = psz


if __name__ == '__main__':
    # import pdb
    # pdb.set_trace()
    app = QApplication(sys.argv)
    main_control = SetupMainWindow()

    app.exec_()

