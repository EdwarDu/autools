#!/usr/bin/env python3

import sys
import traceback
import re
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QTimer, QDir
import os
import time
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

_AUTOZ_TEST = False
_MAPM_TEST = False

from ..SRS.SR830Man import SR830Man, float2str
from ..Cameras.CVCameraMan import CVCameraMan
from ..Cameras.AndorCameraMan import AndorCameraMan


try:
    from ..Cameras.FlyCapMan import FlyCapMan
    _HAS_FLY = True
except ImportError:
    _HAS_FLY = False

from ..PI.PiezoMan import PiezoMan
from ..NKT.FianiumAOTFMan import FianiumAOTFMan
from ..YSL.AOTFMan import AOTFMan as YSLAOTFMan
from ..YSL.SC05Man import SC05Man
from ..NIDAQ.NIDAQDevMan import NIDAQDevMan
from ..Keithley.M3390Man import M3390Man

from .laser_alignment_z_dists_window import LaserAlignmentZDistsWindow
from .pcali_wlen_power_window import PCaliWLenPowerWindow
from .lim_xy_window import LIM_XYWindow


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
        self.checkBox_LP_gaussian_force.stateChanged.connect(
            lambda checked: self.widget_ZDepthProfiler_H.set_gaussian_fit_force_peak(checked))
        self.checkBox_LP_gaussian_force.stateChanged.connect(
            lambda checked: self.widget_ZDepthProfiler_V.set_gaussian_fit_force_peak(checked))
        self.widget_ZDepthProfiler_H.set_title('Horizontal(X) Z Depth Profile')

        self.checkBox_LP_gaussian_manual.stateChanged.connect(
            lambda checked: self.widget_LaserProfiler.set_gaussian_fit_manual_mean(checked))
        self.checkBox_LP_gaussian_manual.stateChanged.connect(
            lambda checked: self.widget_ZDepthProfiler_H.set_gaussian_fit_manual_mean(checked))
        self.checkBox_LP_gaussian_manual.stateChanged.connect(
            lambda checked: self.widget_ZDepthProfiler_V.set_gaussian_fit_manual_mean(checked))
        self.widget_ZDepthProfiler_V.set_title('Vertical(Y) Z Depth Profile')

        self.pushButton_LP_LoadRaw.clicked.connect(self.lp_load_raw)
        self.pushButton_ZDepthProfile_LoadRawH.clicked.connect(lambda: self.zdepth_load_raw('H'))
        self.pushButton_ZDepthProfile_LoadRawV.clicked.connect(lambda: self.zdepth_load_raw('V'))

        self.pushButton_ExportZDepthProfile.clicked.connect(lambda: self.laser_align_zdepth_export())

        self.sr830_man: SR830Man = SR830Man()
        self.pushButton_SR830_Config.clicked.connect(lambda: self.sr830_man.show_config_window())
        self.sr830_man.opened.connect(lambda: self.label_SR830_Conn_Status.setStyleSheet("background: green"))
        self.sr830_man.closed.connect(lambda: self.label_SR830_Conn_Status.setStyleSheet("background: red"))
        self.sr830_man.axisValueChanged.connect(self.sr830_axis_value_changed)

        self.f_aotfman: FianiumAOTFMan = FianiumAOTFMan()
        self.y_aotfman: YSLAOTFMan = YSLAOTFMan()
        self.sc05man: SC05Man = SC05Man()
        self.aotf_man = self.f_aotfman
        self.pushButton_AOTF_Config.clicked.connect(self.aotf_config_clicked)
        self.aotf_man.opened.connect(self.aotf_opened)
        self.aotf_man.closed.connect(self.aotf_closed)
        self.aotf_man.wavelength_changed.connect(self.aotf_wlen_changed)
        self.aotf_man.power_changed.connect(self.aotf_power_changed)
        self.radioButton_AOTF_Fianium.clicked.connect(self.aotf_selected)
        self.radioButton_AOTF_YSL.clicked.connect(self.aotf_selected)

        self.nidaq_man: NIDAQDevMan = NIDAQDevMan()
        self.pushButton_NIDAQ_Config.clicked.connect(lambda: self.nidaq_man.show_config_window())
        self.nidaq_man.opened.connect(lambda: self.label_NIDAQ_Conn_Status.setStyleSheet("background: green"))
        self.nidaq_man.closed.connect(lambda: self.label_NIDAQ_Conn_Status.setStyleSheet("background: red"))
        self.nidaq_man.ao_channels_changed.connect(self.nidaq_ao_channels_changed)
        self.nidaq_man.ai_channels_changed.connect(self.nidaq_ai_channels_changed)
        self.nidaq_man.ai_values_changed.connect(self.nidaq_ai_values_changed)

        self.piezo_man: PiezoMan = PiezoMan()
        self.pushButton_Piezo_Config.clicked.connect(lambda: self.piezo_man.show_config_window())
        self.piezo_man.opened.connect(self.piezo_opened)
        self.piezo_man.closed.connect(lambda: self.label_Piezo_Conn_Status.setStyleSheet("background: red"))
        self.piezo_man.axis_position_changed.connect(self.piezo_axis_position_changed)
        self.doubleSpinBox_Z0.valueChanged.connect(lambda x: self.doubleSpinBox_Z1.setMinimum(x))
        self.pushButton_RunAutoZ.clicked.connect(self.run_autoz_task)
        self.pushButton_LaserAlignmentFolderSelect.clicked.connect(self.pick_laser_alignment_folder)
        self.pushButton_GotoZ0.clicked.connect(lambda: self.laser_align_z_task_goto(self.doubleSpinBox_Z0.value()))
        self.pushButton_NextZ.clicked.connect(self.laser_align_next_z)
        self.pushButton_ExportProfile.clicked.connect(lambda: self.laser_align_z_task_export(None))

        self.k3390man: M3390Man = M3390Man()
        self.pushButton_Keithley3390_Config.clicked.connect(lambda: self.k3390man.show_config_window())
        self.k3390man.opened.connect(self.k3390_opened)
        self.k3390man.closed.connect(lambda: self.label_Keithley3390_Conn_Status.setStyleSheet("background: red"))
        self.k3390man.sig_changed.connect(self.k3390_sig_changed)
        self.k3390man.output_state_changed.connect(self.k3390_output_state_changed)

        # AndorCam
        self.andor_man = AndorCameraMan(0)

        # PDV plot
        self.laser_align_z_dists_tablewin = LaserAlignmentZDistsWindow()
        self.pushButton_ShowZDistWin.clicked.connect(lambda: self.laser_align_z_dists_tablewin.show())
        self.pdv_update_ts = None
        self.pushButton_PDV_Refresh.clicked.connect(self.pdv_refresh)
        self.pushButton_PDV_AutoRefresh.toggled.connect(self.pdv_autorefresh)

        # PCali
        self.pushButton_PCaliSetWL.clicked.connect(lambda: self.pcali_setwl())
        self.spinBox_PCaliWL0.valueChanged.connect(lambda value: self.spinBox_PCaliWL1.setMinimum(value))
        self.pushButton_PCaliNextWL.clicked.connect(lambda: self.pcali_nextwl())
        self.pushButton_PCaliSetPower.clicked.connect(lambda: self.pcali_setpower())
        self.pushButton_PCaliGetVol.clicked.connect(self.pcali_getvol)
        self.doubleSpinBox_PCaliVolTarget.valueChanged.connect(lambda value: self.widget_PCaliPlot.move_ch2_hline(value))
        self.pushButton_PCaliClear.clicked.connect(self.pcali_clearplots)
        self.pushButton_PCaliRun.clicked.connect(self.pcali_run)
        self.pcali_wlen_power_tablewin = PCaliWLenPowerWindow()
        self.pushButton_PCaliShowRes.clicked.connect(lambda: self.pcali_wlen_power_tablewin.show())
        self.pcali_wlen_power_res = {}
        # FIXME: the MaxVol should be verified
        self.doubleSpinBox_PCaliVolTarget.valueChanged.connect(
            lambda value: self.doubleSpinBox_PCaliMaxVol.setMinimum(value + 0.1))

        # Lock-In Measurement (LIM)
        self.pushButton_LIM_SetWL0.clicked.connect(lambda: self.lim_setwl())
        self.lineEdit_LIM_WLCurr.textChanged.connect(lambda: self.lim_wl_changed())
        self.spinBox_LIM_WL0.valueChanged.connect(lambda value: self.spinBox_LIM_WL1.setMinimum(value))
        self.pushButton_LIM_NextWL.clicked.connect(lambda: self.lim_nextwl())
        self.pushButton_LIM_SetPower.clicked.connect(lambda: self.lim_setpower())
        self.pushButton_LIM_SetCaliPower.clicked.connect(lambda: self.lim_setcalipower())
        self.pushButton_LIM_Measure.clicked.connect(lambda: self.lim_measure())
        self.pushButton_LIM_Auto.clicked.connect(self.lim_run)
        self.pushButton_LIM_ClearPlots.clicked.connect(self.lim_clearplots)
        self.lim_xy_tablewin = LIM_XYWindow()
        self.pushButton_LIM_ShowResult.clicked.connect(lambda: self.lim_xy_tablewin.show())

        # Map Measurement
        self.doubleSpinBox_MapM_X0.valueChanged.connect(self.mapm_x_changed)
        self.doubleSpinBox_MapM_X1.valueChanged.connect(self.mapm_x_changed)
        self.doubleSpinBox_MapM_Y0.valueChanged.connect(self.mapm_y_changed)
        self.doubleSpinBox_MapM_Y1.valueChanged.connect(self.mapm_y_changed)
        self.spinBox_MapM_XSamples.valueChanged.connect(self.mapm_x_changed)
        self.spinBox_MapM_YSamples.valueChanged.connect(self.mapm_y_changed)
        self.mapm_x_changed()
        self.mapm_y_changed()

        self.pushButton_MapM_GoX0.clicked.connect(
            lambda: self.piezo_man.set_target_pos(["A", self.doubleSpinBox_MapM_X0.value()]))
        self.pushButton_MapM_GoY0.clicked.connect(
            lambda: self.piezo_man.set_target_pos(["B", self.doubleSpinBox_MapM_Y0.value()]))

        self.pushButton_MapM_Measure.clicked.connect(self.mapm_measure)
        self.pushButton_MapM_Auto.clicked.connect(self.mapm_measure_auto)
        self.pushButton_MapM_Export.clicked.connect(self.mapm_export)
        self.pushButton_MapM_Load.clicked.connect(self.mapm_load_npraw)

        self.all_cams = []
        self.window.show()

    def aotf_selected(self):
        if self.radioButton_AOTF_Fianium.isChecked():
            self.radioButton_AOTF_YSL.setChecked(False)
            self.aotf_man = self.f_aotfman
        elif self.radioButton_AOTF_YSL.isChecked():
            self.radioButton_AOTF_Fianium.setChecked(False)
            self.aotf_man = self.y_aotfman

    def aotf_config_clicked(self):
        if self.radioButton_AOTF_Fianium.isChecked():
            self.f_aotfman.show_config_window()
        elif self.radioButton_AOTF_YSL.isChecked():
            self.sc05man.show_config_window()
            self.y_aotfman.show_config_window()

    def aotf_opened(self):
        self.radioButton_AOTF_Fianium.setEnabled(False)
        self.radioButton_AOTF_YSL.setEnabled(False)
        self.label_AOTF_Conn_Status.setStyleSheet("background: green")

    def aotf_closed(self):
        self.label_AOTF_Conn_Status.setStyleSheet("background: red")
        self.radioButton_AOTF_Fianium.setEnabled(True)
        self.radioButton_AOTF_YSL.setEnabled(True)

    def aotf_wlen_changed(self, ch, wlen):
        self.label_AOTF_WaveLength.setText(f"{wlen}")

    def aotf_power_changed(self, ch, power):
        self.label_AOTF_Power.setText(f"{power}")
        max_power = FianiumAOTFMan.MAX_POWER if self.radioButton_AOTF_Fianium.isChecked() else YSLAOTFMan.MAX_POWER
        self.label_AOTF_PowerPerc.setText(f"{power / max_power * 100:.2f}")

    def mapm_export(self):
        folder = os.path.normpath(QFileDialog.getExistingDirectory(
            self.window, 'Select folder to put the exported images'))
        prefix = os.path.join(folder, "lockin_x")
        self.widget_MeasurementPlot1.export_image(prefix)
        prefix = os.path.join(folder, "lockin_y")
        self.widget_MeasurementPlot2.export_image(prefix)
        prefix = os.path.join(folder, "pd_vol")
        self.widget_MeasurementPlot3.export_image(prefix)
        setup_main_logger.info(f"Files exported to {folder} with prefix {{lockin_x/lockin_y/pd_vol}}",
                               extra={"component": "Main/MAPM"})

    def mapm_load_npraw(self):
        folder = os.path.normpath(QFileDialog.getExistingDirectory(
            self.window, 'Select folder with the exported images inside'))
        x_filename = os.path.join(folder, "lockin_x_map_img.npraw")
        if os.path.exists(x_filename):
            self.widget_MeasurementPlot1.load_raw(x_filename)
        else:
            setup_main_logger.error(f"No file {x_filename} to load",
                                   extra={"component": "Main/MAPM"})
        y_filename = os.path.join(folder, "lockin_y_map_img.npraw")
        if os.path.exists(y_filename):
            self.widget_MeasurementPlot2.load_raw(y_filename)
        else:
            setup_main_logger.error(f"No file {y_filename} to load",
                                   extra={"component": "Main/MAPM"})
        vol_filename = os.path.join(folder, "pd_vol_map_img.npraw")
        if os.path.exists(vol_filename):
            self.widget_MeasurementPlot3.load_raw(vol_filename)
        else:
            setup_main_logger.error(f"No file {vol_filename} to load",
                                    extra={"component": "Main/MAPM"})

    def mapm_measure(self):
        # Lock In
        x, y = self.sr830_man.get_parameters_value(SR830Man.GET_PARAMETER_X, SR830Man.GET_PARAMETER_Y)
        self.lineEdit_MapM_LockInX.setText(float2str(x))
        self.lineEdit_MapM_LockInY.setText(float2str(y))
        # NI DAQ
        vol = self.nidaq_man.read_ai_channels()[self.comboBox_MapM_NIDAQCh.currentText()]
        self.lineEdit_MapM_NiVol.setText(float2str(vol))
        return x, y, vol

    def pzt_goto_xy(self, x, y, wait_10ms=300):
        self.piezo_man.set_target_pos(["A", x], ["B", y])
        i = 0
        while i < wait_10ms:
            pos = self.piezo_man.get_real_position("A", "B")
            pos_x, pos_y = pos["A"], pos["B"]
            if abs(pos_x - x) <= 0.01 and abs(pos_y - y) <= 0.01:
                return
            else:
                time.sleep(0.01)
                i += 1
        raise TimeoutError(f"PZT Unable to go to {x},{y} in {wait_10ms} x 10ms")

    def mapm_measure_auto(self):
        # TODO: Run Automeasure task
        # Pzt to X0, Y0
        x0 = self.doubleSpinBox_MapM_X0.value()
        y0 = self.doubleSpinBox_MapM_Y0.value()
        x1 = self.doubleSpinBox_MapM_X1.value()
        y1 = self.doubleSpinBox_MapM_Y1.value()
        x_samples = self.spinBox_MapM_XSamples.value()
        y_samples = self.spinBox_MapM_YSamples.value()

        x_values = np.linspace(x0, x1, x_samples)
        y_values = np.linspace(y0, y1, y_samples)

        ni_ch = self.comboBox_MapM_NIDAQCh.currentText()
        measure_delay_ms = self.spinBox_MapM_MeasureDelay.value()

        setup_main_logger.info(f"Map scan from {x0:.6f},{y0:.6f} to {x1:.6f},{y1:.6f} "
                               f"#Samples X={x_samples}, Y={y_samples} "
                               f"With NIDAQ ch {ni_ch} "
                               f"Measure delay {measure_delay_ms} ms", extra={"component": "Main/MAPM"})

        try:
            if not _MAPM_TEST:
                self.pzt_goto_xy(x0, y0)
        except TimeoutError as te:
            setup_main_logger.error(te, extra={"component": "Main/MAPM"})
            return

        # Set up plots
        self.widget_MeasurementPlot1.set_xy_list(x_values, y_values)
        self.widget_MeasurementPlot2.set_xy_list(x_values, y_values)
        self.widget_MeasurementPlot3.set_xy_list(x_values, y_values)

        # Sig gen ON
        if not _MAPM_TEST:
            self.k3390man.turn_output(True)

        for y in y_values:
            for x in x_values:
                # Go to x, y
                if not _MAPM_TEST:
                    self.pzt_goto_xy(x, y)
                QtWidgets.qApp.processEvents()
                time.sleep(measure_delay_ms/1000)
                if not _MAPM_TEST:
                    lockin_x, lockin_y, vol = self.mapm_measure()
                else:
                    lockin_x, lockin_y, vol = x, y, x+y
                self.widget_MeasurementPlot1.set_xy_value(x, y, lockin_x)
                self.widget_MeasurementPlot2.set_xy_value(x, y, lockin_y)
                self.widget_MeasurementPlot3.set_xy_value(x, y, vol)
                QtWidgets.qApp.processEvents()

        # Sig gen OFF
        if not _MAPM_TEST:
            self.k3390man.turn_output(False)

    def mapm_x_changed(self):
        x0 = self.doubleSpinBox_MapM_X0.value()
        self.doubleSpinBox_MapM_X1.setMinimum(x0)
        x1 = self.doubleSpinBox_MapM_X1.value()
        x_samples = self.spinBox_MapM_XSamples.value()
        x_step = (x1-x0) / (x_samples-1)
        self.lineEdit_MapM_XStep.setText(f"{x_step:.6f}")

    def mapm_y_changed(self):
        y0 = self.doubleSpinBox_MapM_Y0.value()
        self.doubleSpinBox_MapM_Y1.setMinimum(y0)
        y1 = self.doubleSpinBox_MapM_Y1.value()
        y_samples = self.spinBox_MapM_YSamples.value()
        y_step = (y1 - y0) / (y_samples - 1)
        self.lineEdit_MapM_YStep.setText(f"{y_step:.6f}")

    def lim_setwl(self, wlen: int = None):
        global setup_main_logger
        if wlen is None:
            wlen = self.spinBox_LIM_WL0.value()

        self.lineEdit_LIM_WLCurr.setText(f"{wlen}")

        b_a, _ = self.aotf_man.is_wavelength_available(wlen)

        if not b_a:
            self.lineEdit_LIM_WLCurr.setStyleSheet("background: red")
            setup_main_logger.error(f"Wave Length {wlen} unavailable, check AOTF settings",
                                    extra={"component": "Main/LIM"})
            return None
        else:
            self.lineEdit_LIM_WLCurr.setStyleSheet("")
            self.aotf_man.set_wavelength(wlen)
            setup_main_logger.info(f"Set Wave Length to {wlen}", extra={"component": "Main/LIM"})
            return wlen

    def lim_nextwl(self, next_wlen: int = None):
        if next_wlen is None:
            try:
                cur_wlen = int(self.lineEdit_LIM_WLCurr.text())
            except:
                setup_main_logger.error(f"Current Wave Length <{self.lineEdit_LIM_WLCurr.text()}> invalid",
                                        extra={"component": "Main/LIM"})
                return None

            next_wlen = cur_wlen + self.spinBox_LIM_WLs.value()

        if next_wlen > self.spinBox_LIM_WL1.value():
            return None

        self.lineEdit_LIM_WLCurr.setText(f"{next_wlen}")
        b_a, _= self.aotf_man.is_wavelength_available(next_wlen)
        if not b_a:
            self.lineEdit_LIM_WLCurr.setStyleSheet("background: red")
            setup_main_logger.error(f"Wave Length {next_wlen} unavailable, check AOTF settings",
                                    extra={"component": "Main/LIM"})
            return None
        else:
            self.lineEdit_LIM_WLCurr.setStyleSheet("")
            self.aotf_man.set_wavelength(next_wlen)
            setup_main_logger.info(f"Set Wave Length to {next_wlen}", extra={"component": "Main/LIM"})
            return next_wlen

    def lim_wl_changed(self,):
        wl = int(self.lineEdit_LIM_WLCurr.text())
        if wl in self.pcali_wlen_power_res.keys():
            power = self.pcali_wlen_power_res[wl]
            self.doubleSpinBox_LIM_CaliPowerPerc.setValue(power)
            self.doubleSpinBox_LIM_CaliPowerPerc.setStyleSheet("")
        else:
            self.doubleSpinBox_LIM_CaliPowerPerc.setStyleSheet("background: red")

    def lim_setpower(self, power: float = None):
        global setup_main_logger
        if power is None:
            power = self.doubleSpinBox_LIM_PowerPerc.value()

        if power < 0:
            power = 0
        elif power > 100:
            power = 100

        self.lineEdit_LIM_PowerCurr.setText(f"{power:.2f}")
        self.aotf_man.set_power_percent(power/100)
        setup_main_logger.info(f"Set power percent to {power:.2f}", extra={"component": "Main/LIM"})
        return power

    def lim_setcalipower(self, power: float = None):
        global setup_main_logger
        if power is None:
            power = self.doubleSpinBox_LIM_CaliPowerPerc.value()

        if power < 0:
            power = 0
        elif power > 100:
            power = 100

        self.lineEdit_LIM_PowerCurr.setText(f"{power:.2f}")
        self.aotf_man.set_power_percent(power/100)
        setup_main_logger.info(f"Set power percent to {power:.2f}", extra={"component": "Main/LIM"})
        return power

    def lim_measure(self):
        # Only SR830 NOW
        x, y = self.sr830_man.get_parameters_value(SR830Man.GET_PARAMETER_X, SR830Man.GET_PARAMETER_Y)
        self.lineEdit_LIM_X.setText(float2str(x))
        self.lineEdit_LIM_Y.setText(float2str(y))
        return x, y

    def lim_clearplots(self):
        self.widget_LockInPlot.clear_data()

    def lim_run(self):
        # TODO: Once task start part of GUI should be locked
        global setup_main_logger
        setup_main_logger.info(f"Start scanning run", extra={"component": "Main/LIM"})
        wl0 = self.spinBox_LIM_WL0.value()
        wl1 = self.spinBox_LIM_WL1.value()
        wls = self.spinBox_LIM_WLs.value()
        measure_delay = self.spinBox_LIM_MeasureDelay.value()

        self.pushButton_LIM_Auto.setText("Running")
        self.pushButton_LIM_Auto.setEnabled(False)
        setup_main_logger.info(f"Wave Length from {wl0} to {wl1} by {wls}, "
                               f"Measure Delay = {measure_delay} ms",
                               extra={"component": "Main/LIM"})
        self.lim_clearplots()
        self.lim_xy_tablewin.clear()

        try:
            wl = wl0
            while wl <= wl1:
                self.lim_setwl(wl)
                if wl not in self.pcali_wlen_power_res.keys():
                    raise ValueError(f"wave length {wl} not in the results of AOTF Power Calibration result")
                p = self.pcali_wlen_power_res[wl]
                self.lim_setpower(p)
                time.sleep(measure_delay/1000)
                x, y = self.lim_measure()
                self.widget_LockInPlot.add_data(wl, x, y)
                self.lim_xy_tablewin.add_record(wl, p, x, y)
                QtWidgets.qApp.processEvents()
                wl += wls

            self.pushButton_PCaliRun.setStyleSheet("")
        except Exception as e:
            setup_main_logger.error(f"Failed to complete the task {e}", extra={"component": "Main/LIM"})
            self.pushButton_PCaliRun.setStyleSheet("background: red")

        self.lim_xy_tablewin.show()
        self.pushButton_LIM_Auto.setEnabled(True)
        self.pushButton_LIM_Auto.setText("Run")

    def pcali_setwl(self, wlen: int = None):
        global setup_main_logger
        if wlen is None:
            wlen = self.spinBox_PCaliWL0.value()

        self.lineEdit_PCaliWLCurr.setText(f"{wlen}")

        b_a, _ = self.aotf_man.is_wavelength_available(wlen)
        if not b_a:
            self.lineEdit_PCaliWLCurr.setStyleSheet("background: red")
            setup_main_logger.error(f"Wave Length {wlen} unavailable, check AOTF settings",
                                    extra={"component": "Main/PCali"})
            return None
        else:
            self.lineEdit_PCaliWLCurr.setStyleSheet("")
            self.aotf_man.set_wavelength(wlen)
            setup_main_logger.info(f"Set Wave Length to {wlen}", extra={"component": "Main/PCali"})
            return wlen

    def pcali_nextwl(self, next_wlen: int = None):
        if next_wlen is None:
            try:
                cur_wlen = int(self.lineEdit_PCaliWLCurr.text())
            except:
                setup_main_logger.error(f"Current Wave Length <{self.lineEdit_PCaliWLCurr.text()}> invalid",
                                        extra={"component": "Main/PCali"})
                return None

            next_wlen = cur_wlen + self.spinBox_PCaliWLs.value()

        if next_wlen > self.spinBox_PCaliWL1.value():
            return None

        self.lineEdit_PCaliWLCurr.setText(f"{next_wlen}")
        b_a, _= self.aotf_man.is_wavelength_available(next_wlen)
        if not b_a:
            self.lineEdit_PCaliWLCurr.setStyleSheet("background: red")
            setup_main_logger.error(f"Wave Length {next_wlen} unavailable, check AOTF settings",
                                    extra={"component": "Main/PCali"})
            return None
        else:
            self.lineEdit_PCaliWLCurr.setStyleSheet("")
            self.aotf_man.set_wavelength(next_wlen)
            setup_main_logger.info(f"Set Wave Length to {next_wlen}", extra={"component": "Main/PCali"})
            return next_wlen

    def pcali_setpower(self, power: float = None):
        global setup_main_logger
        if power is None:
            power = self.doubleSpinBox_PCaliPower0Perc.value()

        if power < 0:
            power = 0
        elif power > 100:
            power = 100

        self.lineEdit_PCaliPowerCurr.setText(f"{power:.2f}")
        self.aotf_man.set_power_percent(power/100)
        setup_main_logger.info(f"Set power percent to {power:.2f}", extra={"component": "Main/PCali"})
        return power

    def pcali_nextpower(self, next_power: float = None):
        global setup_main_logger
        if next_power is None:
            try:
                cur_power = float(self.lineEdit_PCaliPowerCurr.text())
            except:
                setup_main_logger.error(f"Current power percent <{self.lineEdit_LIM_PowerCurr.text()}> invalid",
                                        extra={"component": "Main/PCali"})
                return False

            next_power = cur_power + self.doubleSpinBox_PCaliPowerSPerc.value()
        else:
            if next_power < 0:
                next_power = 0
            elif next_power > 100:
                next_power = 100

        self.lineEdit_PCaliPowerCurr.setText(f"{next_power:.2f}")
        self.aotf_man.set_power_percent(next_power/100)
        setup_main_logger.info(f"Set Wave Length to {next_power:.2f}", extra={"component": "Main/PCali"})
        return next_power

    def pcali_getvol(self):
        global setup_main_logger
        nidaq_ch = self.comboBox_PCCaliNIDAQCh.currentText()
        ai_values = self.nidaq_man.read_ai_channels()
        if nidaq_ch in ai_values.keys():
            vol = ai_values[nidaq_ch]
            self.lineEdit_PCaliVol.setText(f"{vol:.6f}")
            return vol
        else:
            return None

    def pcali_clearplots(self):
        self.widget_PCaliPlot.clear_data()

    def pcali_run(self):
        # TODO: Once task start part of GUI should be locked
        global setup_main_logger
        setup_main_logger.info(f"Start scanning run", extra={"component": "Main/PCali"})
        wl0 = self.spinBox_PCaliWL0.value()
        wl1 = self.spinBox_PCaliWL1.value()
        wls = self.spinBox_PCaliWLs.value()
        power0 = self.doubleSpinBox_PCaliPower0Perc.value()
        power1 = self.doubleSpinBox_PCaliPower1Perc.value()
        powerstep = self.doubleSpinBox_PCaliPowerSPerc.value()
        vol_ch = self.comboBox_PCCaliNIDAQCh.currentText()
        vol_target = self.doubleSpinBox_PCaliVolTarget.value()
        measure_delay = self.spinBox_PCaliMDelay.value()
        vol_max = self.doubleSpinBox_PCaliMaxVol.value()

        self.pushButton_PCaliRun.setText("Running")
        self.pushButton_PCaliRun.setEnabled(False)
        setup_main_logger.info(f"Wave Length from {wl0} to {wl1} by {wls}, "
                               f"Power % from {power0:.2f} to {power1:.2f} by {powerstep:.2f},"
                               f"Vol from {vol_ch} with target {vol_target:.4f} and max vol {vol_max:.4f},"
                               f"Measure Delay = {measure_delay} ms",
                               extra={"component": "Main/PCali"})
        self.pcali_clearplots()
        self.pcali_wlen_power_tablewin.clear()
        self.pcali_wlen_power_res = {}

        try:
            wl = wl0
            while wl <= wl1:
                self.pcali_setwl(wl)
                self.widget_PCaliPlot.add_ch2_line(wl, wls)
                p = power0
                wl_map = []
                vol = 0
                while p < power1+powerstep and vol < vol_max:
                    p = self.pcali_setpower(p)
                    QtWidgets.qApp.processEvents()
                    time.sleep(measure_delay / 1000)
                    vol = np.average([self.pcali_getvol() for i in range(0, 5)])
                    wl_map.append((p, vol))
                    self.widget_PCaliPlot.add_data_ch2(p, vol)
                    p += powerstep
                    QtWidgets.qApp.processEvents()
                # Find the proper power
                power_target = None
                # FIXME: Assuming Linear
                for i in range(0, len(wl_map)-1):
                    if wl_map[i][1] == vol_target:
                        power_target = wl_map[i][0]
                        break
                    elif wl_map[i][1] <= vol_target <= wl_map[i+1][1] or wl_map[i][1] >= vol_target >= wl_map[i+1][1]:
                        power_target = (vol_target - wl_map[i][1]) / (wl_map[i+1][1] - wl_map[i][1]) * powerstep + \
                                       wl_map[i][0]
                        break

                if power_target is None:
                    raise Exception(f"Unable to find target power for wavelength {wl}")
                self.widget_PCaliPlot.add_data(wl, power_target)
                self.pcali_wlen_power_tablewin.add_record(wl, power_target)
                self.pcali_wlen_power_res[wl] = power_target
                QtWidgets.qApp.processEvents()
                wl += wls

            self.pushButton_PCaliRun.setStyleSheet("")
        except Exception as e:
            setup_main_logger.error(f"Failed to complete the task {e}", extra={"component": "Main/PCali"})
            self.pushButton_PCaliRun.setStyleSheet("background: red")

        self.pcali_wlen_power_tablewin.show()
        self.pushButton_PCaliRun.setEnabled(True)
        self.pushButton_PCaliRun.setText("Run")

    def pdv_refresh(self, b_auto = False, interval = 1000):
        global setup_main_logger
        pdv_ai_ch = self.comboBox_PhotoDiode_NIDAQ_Channel.currentText()
        if pdv_ai_ch != "":
            res_dict = self.nidaq_man.read_ai_channels()
            ts = time.time() * 1000
            if pdv_ai_ch not in res_dict.keys():
                setup_main_logger.error(f"PDV CH {pdv_ai_ch} not in the NIDAQ enabled AI channels",
                                        extra={"component": "Main/PDV"})
                return
            if self.pdv_update_ts is None:
                self.widget_PDVPlot.add_data(0, res_dict[pdv_ai_ch])
                self.pdv_update_ts = ts
            else:
                self.widget_PDVPlot.add_data(ts - self.pdv_update_ts, res_dict[pdv_ai_ch])
        else:
            setup_main_logger.error(f"Invalid PDV NIDAQ Channel",
                                    extra={"component": "Main/PDV"})

        if b_auto:
            if self.pushButton_PDV_AutoRefresh.isChecked():
                QTimer.singleShot(interval, lambda: self.pdv_refresh(True, interval) )

    def _pdv_autorefresh_task(self):
        try:
            interval = int(self.comboBox_PDV_Interval.currentText())
            if interval < 0:
                raise ValueError(f"Invalid interval")
        except:
            setup_main_logger.error(f"Invalid PDV Interval {self.comboBox_PDV_Interval.currentText()}, reset to 1000ms",
                                    extra={"component": "Main/PDV"})
            interval = 1000
            self.comboBox_PDV_Interval.setCurrentText("1000")

        self.pdv_refresh(True, interval)

    def pdv_autorefresh(self, b_checked):
        if b_checked:
            self._pdv_autorefresh_task()

    def pick_laser_alignment_folder(self):
        folder = os.path.normpath(
            QFileDialog.getExistingDirectory(self.window,
                                             'Select folder to put the exported images'))
        self.lineEdit_LaserAlignmentFolder.setText(folder)

    def piezo_opened(self):
        self.label_Piezo_Conn_Status.setStyleSheet("background: green")
        min_pos = self.piezo_man.get_min_commandable_position("A", "B", "C")
        max_pos = self.piezo_man.get_max_commandable_position("A", "B", "C")
        z_min = min_pos["C"]
        z_max = max_pos["C"]
        self.doubleSpinBox_Z0.setMinimum(z_min)
        self.doubleSpinBox_Z1.setMinimum(z_min)
        self.doubleSpinBox_Z0.setMaximum(z_max)
        self.doubleSpinBox_Z1.setMaximum(z_max)
        x_min = min_pos["A"]
        x_max = max_pos["A"]
        y_min = min_pos["B"]
        y_max = max_pos["B"]
        self.doubleSpinBox_MapM_X0.setMinimum(x_min)
        self.doubleSpinBox_MapM_X0.setMaximum(x_max)
        self.doubleSpinBox_MapM_X1.setMinimum(x_min)
        self.doubleSpinBox_MapM_X1.setMaximum(x_max)
        self.doubleSpinBox_MapM_Y0.setMinimum(y_min)
        self.doubleSpinBox_MapM_Y0.setMaximum(y_max)
        self.doubleSpinBox_MapM_Y1.setMinimum(y_min)
        self.doubleSpinBox_MapM_Y1.setMaximum(y_max)

    def laser_align_z_task_goto(self, z):
        global setup_main_logger
        # MOVE PIEZO
        self.piezo_man.set_target_pos(["C", z])
        # Wait till Z moved to target
        while True:
            z_pos = self.piezo_man.get_real_position("C")["C"]
            setup_main_logger.debug(f"Z Pos {z_pos:.6f}", extra={"component": "Main/AutoZ"})
            # FIXME: Test
            if _AUTOZ_TEST:
                break
            # FIXME: Error Margin
            if abs(z_pos - z) <= 0.01:
                break
        setup_main_logger.info(f"Z Pos {z_pos:.6f}", extra={"component": "Main/AutoZ"})

    def laser_align_z_task_cap_cal(self):
        global setup_main_logger
        # FIXME: No error checking
        while True:
            frame = self.current_cam.grab_frame(n_channel_index=self.comboBox_FrameSelect.currentData())
            if frame is None:
                setup_main_logger.error(f"Failed to grab frame", extra={"component": "Main/AutoZ"})
                continue
            self.widget_LaserProfiler.update_image_data(frame)
            QtWidgets.qApp.processEvents()
            h_dist, v_dist = self.widget_LaserProfiler.get_profile_distances()
            setup_main_logger.info(f"H Dist:{h_dist:.6f}, V Dist:{v_dist:.6f}", extra={"component": "Main/AutoZ"})
            return h_dist, v_dist

    def laser_align_z_task_export(self, z):
        global setup_main_logger
        if z is None:
            z = self.piezo_man.get_real_position("C")["C"]
        prefix = os.path.join(self.lineEdit_LaserAlignmentFolder.text(), f"{z:.6f}")
        self.widget_LaserProfiler.export_image(prefix)
        setup_main_logger.info(f"Saving images to {prefix}_profile.svg and {prefix}_image.png",
                               extra={"component": "Main/AutoZ"})

    def laser_align_zdepth_export(self):
        global setup_main_logger
        prefix = os.path.join(self.lineEdit_LaserAlignmentFolder.text(), f"ZDepthHProfile")
        self.widget_ZDepthProfiler_H.export_image(prefix)
        setup_main_logger.info(f"Saving ZDepthProfile(H) images to {prefix}_profile.svg and {prefix}_image.png",
                               extra={"component": "Main/AutoZ"})
        prefix = os.path.join(self.lineEdit_LaserAlignmentFolder.text(), f"ZDepthVProfile")
        self.widget_ZDepthProfiler_V.export_image(prefix)
        setup_main_logger.info(f"Saving ZDepthProfile(V) images to {prefix}_profile.svg and {prefix}_image.png",
                               extra={"component": "Main/AutoZ"})

    def laser_align_next_z(self):
        global setup_main_logger
        current_z = self.piezo_man.get_real_position("C")["C"]
        if current_z + self.doubleSpinBox_Zs.value() <= self.doubleSpinBox_Z1.value():
            current_z += self.doubleSpinBox_Zs.value()
            self.laser_align_z_task_goto(current_z)
            setup_main_logger.info(f"Moving piezo stage Z to {current_z:.6f}", extra={"component": "Main/AutoZ"})
        else:
            setup_main_logger.error(f"Unable to move to next Z {current_z + self.doubleSpinBox_Zs.value():.6f}",
                                    extra={"component": "Main/AutoZ"})

    def run_autoz_task(self):
        global setup_main_logger
        self.pushButton_GotoZ0.setEnabled(False)
        self.pushButton_NextZ.setEnabled(False)
        self.pushButton_ExportProfile.setEnabled(False)
        b_single_enabled = self.pushButton_Single.isEnabled()
        if b_single_enabled:
            self.pushButton_Single.setEnabled(False)
        if self.pushButton_FreeRun.isChecked():
            self.pushButton_FreeRun.setChecked(False)
            QtWidgets.qApp.processEvents()
            time.sleep(1)

        self.laser_align_z_dists_tablewin.clear()

        z0 = self.doubleSpinBox_Z0.value()
        z1 = self.doubleSpinBox_Z1.value()
        zs = self.doubleSpinBox_Zs.value()

        # FIXME: AUTOZ Test
        if _AUTOZ_TEST:
            image_width, image_height, ch = 640, 480, 1
        else:
            image_width, image_height, ch = self.current_cam.get_frame_size()

        self.widget_ZDepthProfiler_H.set_z_list(z0, z1, zs)
        self.widget_ZDepthProfiler_H.set_height(image_width)

        self.widget_ZDepthProfiler_V.set_z_list(z0, z1, zs)
        self.widget_ZDepthProfiler_V.set_height(image_height)

        z = z0
        while z <= z1:
            self.laser_align_z_task_goto(z)
            # FIXME: AUTOZ Test
            if _AUTOZ_TEST:
                frame = gen_2d_gaussian(640, 480, sx=(z-z0)/(z1-z0)*image_width/2+0.1,
                                        sy=(z-z0)/(z1-z0)*image_height/3+0.1,
                                        mx=320,
                                        my=200)
                self.widget_LaserProfiler.update_image_data(frame)
                QtWidgets.qApp.processEvents()
            else:
                h_dist, v_dist = self.laser_align_z_task_cap_cal()

            h_dist, v_dist = self.widget_LaserProfiler.get_profile_distances()
            self.label_LaserAlign_HDist.setText(f"{h_dist:.6f}")
            self.label_LaserAlign_VDist.setText(f"{v_dist:.6f}")
            h_frame_line, h_index = self.widget_LaserProfiler.get_h_frame_line()
            v_frame_line, v_index = self.widget_LaserProfiler.get_v_frame_line()
            self.widget_ZDepthProfiler_H.set_frame_line(z, h_frame_line, v_index)
            self.widget_ZDepthProfiler_V.set_frame_line(z, v_frame_line, h_index)
            self.laser_align_z_dists_tablewin.add_record(z, h_dist, v_dist)
            QtWidgets.qApp.processEvents()
            self.laser_align_z_task_export(z)
            z += zs

        self.pushButton_GotoZ0.setEnabled(True)
        self.pushButton_NextZ.setEnabled(True)
        self.pushButton_ExportProfile.setEnabled(True)
        self.pushButton_Single.setEnabled(b_single_enabled)
        self.laser_align_z_dists_tablewin.show()
        self.laser_align_zdepth_export()

    def nidaq_ao_channels_changed(self):
        # TODO
        global setup_main_logger
        setup_main_logger.debug(f"{self.nidaq_man.get_ao_task_channels()}", extra={"component": "Main"})

    def nidaq_ai_channels_changed(self):
        # TODO
        global setup_main_logger
        nidaq_ai_chs = self.nidaq_man.get_ai_task_channels()
        setup_main_logger.debug(f"{nidaq_ai_chs}", extra={"component": "Main"})
        self.comboBox_PhotoDiode_NIDAQ_Channel.clear()
        self.comboBox_PhotoDiode_NIDAQ_Channel.addItems(nidaq_ai_chs)

        self.comboBox_PCCaliNIDAQCh.clear()
        self.comboBox_PCCaliNIDAQCh.addItems(nidaq_ai_chs)

        self.comboBox_MapM_NIDAQCh.clear()
        self.comboBox_MapM_NIDAQCh.addItems(nidaq_ai_chs)

    def nidaq_ai_values_changed(self, values):
        # TODO
        # global setup_main_logger
        # setup_main_logger.debug(f"{values}", extra={"component": "Main"})
        pass

    def piezo_axis_position_changed(self, pos_dict: dict):
        # FIXME: Must be in closed loop
        global setup_main_logger
        setup_main_logger.debug(f"{pos_dict}", extra={"component": "Main"})
        if 'A' in pos_dict.keys():
            self.label_Piezo_X.setText(f"{pos_dict['A']:.6f}")
        if 'B' in pos_dict.keys():
            self.label_Piezo_Y.setText(f"{pos_dict['B']:.6f}")
        if 'C' in pos_dict.keys():
            self.label_Piezo_Z.setText(f"{pos_dict['C']:.6f}")
            self.label_LaserAlign_CurrZ.setText(f"{pos_dict['C']:.6f}")

    def sr830_axis_value_changed(self, axis: int, value: float):
        global setup_main_logger
        if axis == SR830Man.GET_PARAMETER_X:
            self.label_SR830_X.setText(float2str(value))
        elif axis == SR830Man.GET_PARAMETER_Y:
            self.label_SR830_Y.setText(float2str(value))
        elif axis == SR830Man.GET_PARAMETER_R:
            self.label_SR830_R.setText(float2str(value))
        elif axis == SR830Man.GET_PARAMETER_THETA:
            self.label_SR830_Theta.setText(float2str(value))
        elif axis == SR830Man.GET_PARAMETER_REF_FREQ:
            self.label_SR380_RefFreq.setText(float2str(value))
        else:
            setup_main_logger.warning(f"Unknown (from main) SR830 axis:{axis}", extra={"component": "Main"})

    def refresh_cam_source(self):
        self.comboBox_CamSource.clear()
        self.all_cams = []
        all_cv_cams = CVCameraMan.get_all_cams()
        for cam in all_cv_cams:
            self.comboBox_CamSource.addItem(f"OpenCV Cam: {cam.cv_index}")
            self.all_cams.append(cam)

        if _HAS_FLY:
            all_fly_cams = FlyCapMan.get_all_cams()
            for cam in all_fly_cams:
                self.comboBox_CamSource.addItem(f"FlyCap Cam: {cam.get_dev_id()}")
                self.all_cams.append(cam)

        try:
            n_andor_cams = self.andor_man.get_device_count()
            print(n_andor_cams)
            for i in range(0, n_andor_cams):
                print(i)
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
        fname, _a = QFileDialog.getOpenFileName(self.window, 'Load NPRAW file', '.', 'NPRAW (*.npraw)')

        if fname is not None and fname != '':
            self.widget_LaserProfiler.load_raw(fname)

    def zdepth_load_raw(self, which):
        if which not in ('H', 'V'):
            return
        fname, _a = QFileDialog.getOpenFileName(self.window, f'Load ZDeth ({which}) NPRAW file', '.', 'NPRAW (*.npraw)')
        if fname is not None and fname != '':
            if which == 'H':
                self.widget_ZDepthProfiler_H.load_raw(fname)
            else:
                self.widget_ZDepthProfiler_V.load_raw(fname)

    def k3390_opened(self):
        self.label_Keithley3390_Conn_Status.setStyleSheet("background: green")

    def k3390_sig_changed(self, name, value, unit):
        if name == 'frequency':
            self.label_Keithley3390_Freq.setText(f'{value:.6f} {unit}')
        elif name == 'amplitude':
            self.label_Keithley3390_Amp.setText(f'{value:.6f} {unit}')
        elif name == 'offset':
            self.label_Keithley3390_Offset.setText(f'{value:.6f} {unit}')
        else:
            return

    def k3390_output_state_changed(self, on_off):
        self.label_Keithley3390_Output.setText(f"{'ON' if on_off else 'OFF'}")
        self.label_Mapm_SigGenOutput.setText(f"{'ON' if on_off else 'OFF'}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_control = SetupMainWindow()

    sys.exit(app.exec_())
