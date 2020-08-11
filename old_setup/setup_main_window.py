#!/usr/bin/env python3
from datetime import datetime
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
import concurrent.futures

import threading
from threading import Thread, Event, Lock

from .setup_main_ui import Ui_SetupMainWindow

import serial
import serial.tools.list_ports
import logging

setup_main_logger = logging.getLogger("autools_setup_main")

setup_main_logger.setLevel(logging.INFO)
setup_main_logger_fh = logging.FileHandler("autools_setup_main.log")
setup_main_logger_formatter = logging.Formatter('%(asctime)s [%(component)s] - %(levelname)s - %(message)s')
setup_main_logger_fh.setFormatter(setup_main_logger_formatter)
setup_main_logger.addHandler(setup_main_logger_fh)

setup_main_logger_ch = logging.StreamHandler()
setup_main_logger_ch.setFormatter(setup_main_logger_formatter)
setup_main_logger.addHandler(setup_main_logger_ch)

_TEST_NO_SR830 = False
_TEST_NO_NIDAQ = False

from ..SRS.SR830Man import SR830Man, float2str
from ..NIDAQ.NIDAQDevMan import NIDAQDevMan

from .save_settings_window import SaveSettingsWindow


# noinspection PyPep8Naming
def get_available_COMs():
    com_port_list = serial.tools.list_ports.comports()
    return {com.device: f'{com.manufacturer} {com.description}' for com in com_port_list}


class SetupMainWindow(Ui_SetupMainWindow):
    """
    Inherited from Ui_MainWindow to allow data source and signal/slot connection
    """
    def __init__(self):
        self.window = QMainWindow()
        Ui_SetupMainWindow.__init__(self)
        self.setupUi(self.window)

        self.sr830_man: SR830Man = SR830Man()
        self.pushButton_SR830_Config.clicked.connect(lambda: self.sr830_man.show_config_window())
        self.sr830_man.opened.connect(lambda: self.label_SR830_Conn_Status.setStyleSheet("background: green"))
        self.sr830_man.closed.connect(lambda: self.label_SR830_Conn_Status.setStyleSheet("background: red"))
        self.sr830_man.axis_value_changed.connect(self.sr830_axis_value_changed)

        self.nidaq_man: NIDAQDevMan = NIDAQDevMan()
        self.pushButton_NIDAQ_Config.clicked.connect(lambda: self.nidaq_man.show_config_window())
        self.nidaq_man.opened.connect(lambda: self.label_NIDAQ_Conn_Status.setStyleSheet("background: green"))
        self.nidaq_man.closed.connect(lambda: self.label_NIDAQ_Conn_Status.setStyleSheet("background: red"))
        self.nidaq_man.task_channels_changed.connect(self.nidaq_task_channels_changed)
        self.nidaq_man.ai_values_changed.connect(self.nidaq_ai_values_changed)
        self.nidaq_man.ao_values_changed.connect(self.nidaq_ao_values_changed)

        # PDV
        self.pdv_update_ts = None
        self.pushButton_PDV_Refresh.clicked.connect(self.pdv_refresh)
        self.pushButton_PDV_AutoRefresh.toggled.connect(self.pdv_autorefresh)

        # Map Measurement
        self.doubleSpinBox_MapM_X0.valueChanged.connect(self.mapm_x_changed)
        self.doubleSpinBox_MapM_X1.valueChanged.connect(self.mapm_x_changed)
        self.doubleSpinBox_MapM_Y0.valueChanged.connect(self.mapm_y_changed)
        self.doubleSpinBox_MapM_Y1.valueChanged.connect(self.mapm_y_changed)
        self.spinBox_MapM_XSamples.valueChanged.connect(self.mapm_x_changed)
        self.spinBox_MapM_YSamples.valueChanged.connect(self.mapm_y_changed)
        self.mapm_x_changed()
        self.mapm_y_changed()

        self.piezo_cur_x = 0
        self.piezo_cur_y = 0
        self.mapm_pause_requested = False
        self.pushButton_MapM_Pause.setEnabled(False)

        self.pushButton_MapM_Pause.clicked.connect(lambda: self.mapm_request_pause())

        self.pushButton_MapM_GoX0.clicked.connect(
            lambda: self.piezo_goto_xyz(x=self.doubleSpinBox_MapM_X0.value(), y=self.piezo_cur_y))
        self.pushButton_MapM_GoY0.clicked.connect(
            lambda: self.piezo_goto_xyz(x=self.piezo_cur_x, y=self.doubleSpinBox_MapM_Y0.value()))

        self.pushButton_MapM_Measure.clicked.connect(
            lambda: self.mapm_measure(lockin_n_avg=self.spinBox_MapM_NSamplesAvgLockIn.value(),
                                      pdv_n_avg=self.spinBox_MapM_NSamplesAvgPD.value()))
        self.pushButton_MapM_Auto.clicked.connect(lambda: self.mapm_measure_auto())
        self.pushButton_MapM_Export.clicked.connect(self.mapm_export)
        self.pushButton_MapM_Load.clicked.connect(self.mapm_load_npraw)

        self.save_settings_diag = SaveSettingsWindow(self.sr830_man, self.nidaq_man)
        self.pushButton_SaveSettings.clicked.connect(lambda: self.save_settings_diag.show())

        self.checkBox_ShowPreLine.toggled.connect(self.mapm_show_last_line_changed)

        self.mapm_last_incomplete_scan = None
        self.window.show()

    def mapm_show_last_line_changed(self):
        self.widget_MeasurementPlot1.show_h_pre_line(self.checkBox_ShowPreLine.isChecked())
        self.widget_MeasurementPlot2.show_h_pre_line(self.checkBox_ShowPreLine.isChecked())
        self.widget_MeasurementPlot3.show_h_pre_line(self.checkBox_ShowPreLine.isChecked())

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

    def _get_lockin_xy(self, lockin_n_avg: int = 1):
        if _TEST_NO_SR830:
            return np.random.random(2)
            # return self.piezo_cur_x, self.piezo_cur_y

        x_l = np.zeros(lockin_n_avg)
        y_l = np.zeros(lockin_n_avg)
        for i in range(0, lockin_n_avg):
            x_l[i], y_l[i] = self.sr830_man.get_parameters_value(SR830Man.GET_PARAMETER_X, SR830Man.GET_PARAMETER_Y)
        return np.average(x_l), np.average(y_l)

    def _get_pdv_vol(self, pdv_n_avg: int = 1500):
        if _TEST_NO_NIDAQ:
            # return self.piezo_cur_x + self.piezo_cur_y
            return np.random.random(1)[0]

        pdv_arr = np.array([])
        samples_left = pdv_n_avg
        while samples_left != 0:
            samples2read = min(samples_left, 1024)
            pdv_arr = np.append(pdv_arr, self.nidaq_man.read_task_channels("ai", samples2read)[self.comboBox_MapM_NIDAQChIn.currentText()])
            samples_left = samples_left-samples2read
        return np.average(pdv_arr)

    def mapm_measure(self, lockin_n_avg: int = 1, pdv_n_avg: int = 1500):
        # x_l, y_l, vol_l = [np.zeros(n_avg, dtype=np.float) for i in range(0, 3)]
        #
        # for i in range(0, n_avg):
        #     # Lock In
        #     if _MAPM_TEST:
        #         x_l[i], y_l[i], vol_l[i] = np.abs(np.random.randn(3))
        #     else:
        #         x_l[i], y_l[i] = self.sr830_man.get_parameters_value(SR830Man.GET_PARAMETER_X, SR830Man.GET_PARAMETER_Y)
        #         vol_l[i] = np.average(self.nidaq_man.read_task_channels("ai", 1500)[
        #                                   self.comboBox_MapM_NIDAQChIn.currentText()
        #                               ])
        #         setup_main_logger.debug(f"Measurement: {x_l[i]} {y_l[i]} {vol_l[i]}",
        #                                 extra={"component": "Main/MAPM"})
        # x, y, vol = np.average(x_l), np.average(y_l), np.average(vol_l)
        # setup_main_logger.debug(f"Measurement AVG: {x} {y} {vol}",
        #                         extra={"component": "Main/MAPM"})
        # self.lineEdit_MapM_LockInX.setText(float2str(x))
        # self.lineEdit_MapM_LockInY.setText(float2str(y))
        # self.lineEdit_MapM_NiVolIn.setText(float2str(vol))

        with concurrent.futures.ThreadPoolExecutor() as executor:
            lockin_future = executor.submit(self._get_lockin_xy, lockin_n_avg)
            pdv_future = executor.submit(self._get_pdv_vol, pdv_n_avg)
            lockin_x, lockin_y = lockin_future.result()
            pdv_vol = pdv_future.result()

        return lockin_x, lockin_y, pdv_vol

    def mapm_request_pause(self):
        self.mapm_pause_requested = True

    def mapm_measure_auto(self):
        # TODO: Run Automeasure task
        self.pushButton_MapM_Pause.setEnabled(True)
        if self.mapm_last_incomplete_scan is not None and \
                len(self.mapm_last_incomplete_scan) != 0:
            x0 = self.mapm_last_incomplete_scan["x0"]
            y0 = self.mapm_last_incomplete_scan["y0"]
            x1 = self.mapm_last_incomplete_scan["x1"]
            y1 = self.mapm_last_incomplete_scan["y1"]
            x_samples = self.mapm_last_incomplete_scan["x_samples"]
            y_samples = self.mapm_last_incomplete_scan["y_samples"]
            ni_x_ch = self.mapm_last_incomplete_scan['ni_x_ch']
            ni_y_ch = self.mapm_last_incomplete_scan['ni_y_ch']
            ni_in_ch = self.mapm_last_incomplete_scan['ni_in_ch']

            n_lockin_samples = self.mapm_last_incomplete_scan['n_lockin_samples']
            n_pdv_samples = self.mapm_last_incomplete_scan['n_pdv_samples']
            measure_delay_ms = self.spinBox_MapM_MeasureDelay.value()

            ans = QMessageBox.question(self.window, f"Previous scan incomplete",
                                       f"Map scan from {x0:.6f},{y0:.6f} to {x1:.6f},{y1:.6f} \n"
                                       f"#Samples X={x_samples}, Y={y_samples} \n"
                                       f"NIDAQ Ch X={ni_x_ch}, Y={ni_y_ch} In={ni_in_ch} \n"
                                       f"Average LockIn {n_lockin_samples} PDV(NI) {n_pdv_samples} \n"
                                       f"Measure delay {measure_delay_ms} ms \n"
                                       f"Continue from last scan's last position?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            start_new = ans == QMessageBox.No
        else:
            start_new = True

        if start_new:
            x0 = self.doubleSpinBox_MapM_X0.value()
            y0 = self.doubleSpinBox_MapM_Y0.value()
            x1 = self.doubleSpinBox_MapM_X1.value()
            y1 = self.doubleSpinBox_MapM_Y1.value()
            x_samples = self.spinBox_MapM_XSamples.value()
            y_samples = self.spinBox_MapM_YSamples.value()
            ni_x_ch = self.comboBox_MapM_NIDAQChX.currentText()
            ni_y_ch = self.comboBox_MapM_NIDAQChY.currentText()
            ni_in_ch = self.comboBox_MapM_NIDAQChIn.currentText()
            x_values = np.linspace(x0, x1, x_samples)
            y_values = np.linspace(y0, y1, y_samples)
            n_lockin_samples = self.spinBox_MapM_NSamplesAvgLockIn.value()
            n_pdv_samples = self.spinBox_MapM_NSamplesAvgPD.value()
            measure_delay_ms = self.spinBox_MapM_MeasureDelay.value()

            setup_main_logger.info(f"Map scan from {x0:.6f},{y0:.6f} to {x1:.6f},{y1:.6f} "
                                   f"#Samples X={x_samples}, Y={y_samples} "
                                   f"NIDAQ Ch X={ni_x_ch}, Y={ni_y_ch} In={ni_in_ch} "
                                   f"Average LockIn {n_lockin_samples} PDV(NI) {n_pdv_samples} "
                                   f"Measure delay {measure_delay_ms} ms", extra={"component": "Main/MAPM"})

            self.piezo_goto_xyz(x=x0, y=y0)
            self.mapm_last_incomplete_scan = {
                "x0": x0, "y0": y0, "x1": x1, "y1": y1, "x_samples": x_samples, "y_samples": y_samples,
                "ni_x_ch": ni_x_ch, "ni_y_ch": ni_y_ch, "ni_in_ch": ni_in_ch,
                "measure_delay_ms": measure_delay_ms,
                "n_lockin_samples": n_lockin_samples, "n_pdv_samples": n_pdv_samples,
                "scanned_data": {}
            }
        else:
            x0 = self.mapm_last_incomplete_scan["x0"]
            y0 = self.mapm_last_incomplete_scan["y0"]
            x1 = self.mapm_last_incomplete_scan["x1"]
            y1 = self.mapm_last_incomplete_scan["y1"]
            x_samples = self.mapm_last_incomplete_scan["x_samples"]
            y_samples = self.mapm_last_incomplete_scan["y_samples"]
            ni_x_ch = self.mapm_last_incomplete_scan['ni_x_ch']
            ni_y_ch = self.mapm_last_incomplete_scan['ni_y_ch']
            ni_in_ch = self.mapm_last_incomplete_scan['ni_in_ch']
            n_lockin_samples = self.mapm_last_incomplete_scan['n_lockin_samples']
            n_pdv_samples = self.mapm_last_incomplete_scan['n_pdv_samples']
            measure_delay_ms = self.mapm_last_incomplete_scan["measure_delay_ms"]

            x_values = np.linspace(x0, x1, x_samples)
            y_values = np.linspace(y0, y1, y_samples)

            self.doubleSpinBox_MapM_X0.setValue(x0)
            self.doubleSpinBox_MapM_Y0.setValue(y0)
            self.doubleSpinBox_MapM_X1.setValue(x1)
            self.doubleSpinBox_MapM_Y1.setValue(y1)
            self.spinBox_MapM_NSamplesAvgLockIn.setValue(n_lockin_samples)
            self.spinBox_MapM_NSamplesAvgPD.setValue(n_pdv_samples)
            self.comboBox_MapM_NIDAQChX.setCurrentText(ni_x_ch)
            self.comboBox_MapM_NIDAQChY.setCurrentText(ni_y_ch)
            self.comboBox_MapM_NIDAQChIn.setCurrentText(ni_in_ch)
            self.spinBox_MapM_MeasureDelay.setValue(measure_delay_ms)
            QtWidgets.qApp.processEvents()

            setup_main_logger.info(f"Resume map scan from {x0:.6f},{y0:.6f} to {x1:.6f},{y1:.6f} "
                                   f"#Samples X={x_samples}, Y={y_samples} "
                                   f"NIDAQ Ch X={ni_x_ch} Y={ni_y_ch} In={ni_in_ch} "
                                   f"Average LockIn {n_lockin_samples} PDV(NI) {n_pdv_samples} "
                                   f"Measure delay {measure_delay_ms} ms", extra={"component": "Main/MAPM"})

        self.spinBox_MapM_NSamplesAvgPD.setEnabled(False)
        self.spinBox_MapM_NSamplesAvgLockIn.setEnabled(False)
        # if not b_only_check_pzt:
        # Set up plots
        self.widget_MeasurementPlot1.set_xy_list(x_values, y_values)
        self.widget_MeasurementPlot2.set_xy_list(x_values, y_values)
        self.widget_MeasurementPlot3.set_xy_list(x_values, y_values)

        row_index = 0
        for y in y_values:
            x_track = x_values  # if row_index % 2 == 0 else np.flip(x_values)
            for x in x_track:
                # Go to x, y
                setup_main_logger.info(f"Piezo going to {x:.6f}, {y:.6f}", extra={"component": "Main/MAPM"})
                self.piezo_goto_xyz(x=x, y=y)
                QtWidgets.qApp.processEvents()
                if (x, y) not in self.mapm_last_incomplete_scan["scanned_data"].keys():
                    t0 = datetime.now()
                    while (datetime.now() - t0).total_seconds() < measure_delay_ms / 1000:
                        QtWidgets.qApp.processEvents()
                        if self.mapm_pause_requested:
                            ans = QMessageBox.question(self.window, f"Scan paused",
                                                       f"Stopped at X={x} Y={y}, Yes to continue or ABORT current scan",
                                                       QMessageBox.Abort | QMessageBox.Yes, QMessageBox.Yes)
                            if ans == QMessageBox.Abort:
                                ans = QMessageBox.question(self.window, f"Abort scan",
                                                           f"Are you sure?",
                                                           QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
                                if ans == QMessageBox.Yes:
                                    self.mapm_pause_requested = False
                                    self.pushButton_MapM_Pause.setEnabled(False)
                                    self.spinBox_MapM_NSamplesAvgPD.setEnabled(True)
                                    self.spinBox_MapM_NSamplesAvgLockIn.setEnabled(True)
                                    return
                            self.mapm_pause_requested = False
                    setup_main_logger.debug(f"Starting measurement", extra={"component": "Main/MAPM"})
                    lockin_x, lockin_y, pdv_vol = self.mapm_measure(lockin_n_avg=self.spinBox_MapM_NSamplesAvgLockIn.value(),
                                                                pdv_n_avg=self.spinBox_MapM_NSamplesAvgPD.value())
                    setup_main_logger.info(f"Measurement got values SR830 X={lockin_x}, Y={lockin_y}, PDV={pdv_vol}",
                                           extra={"component": "Main/MAPM"})
                else:
                    lockin_x, lockin_y, pd_vol = self.mapm_last_incomplete_scan["scanned_data"][(x, y)]

                self.widget_MeasurementPlot1.set_xy_value(x, y, lockin_x)
                self.widget_MeasurementPlot2.set_xy_value(x, y, lockin_y)
                self.widget_MeasurementPlot3.set_xy_value(x, y, pdv_vol)
                self.mapm_last_incomplete_scan["scanned_data"][(x, y)] = (lockin_x, lockin_y, pdv_vol)
            else:
                row_index += 1
                self.widget_MeasurementPlot1.move_sec_h_line(y_values[row_index-1])
                self.widget_MeasurementPlot2.move_sec_h_line(y_values[row_index-1])
                self.widget_MeasurementPlot3.move_sec_h_line(y_values[row_index-1])
                continue

        self.mapm_last_incomplete_scan = None  # scan complete remove incomplete save
        self.pushButton_MapM_Pause.setEnabled(False)
        self.spinBox_MapM_NSamplesAvgPD.setEnabled(True)
        self.spinBox_MapM_NSamplesAvgLockIn.setEnabled(True)

    def mapm_x_changed(self):
        x0 = self.doubleSpinBox_MapM_X0.value()
        x1 = self.doubleSpinBox_MapM_X1.value()
        x_samples = self.spinBox_MapM_XSamples.value()
        x_step = (x1-x0) / (x_samples-1)
        self.lineEdit_MapM_XStep.setText(f"{x_step:.6f}")

    def mapm_y_changed(self):
        y0 = self.doubleSpinBox_MapM_Y0.value()
        y1 = self.doubleSpinBox_MapM_Y1.value()
        y_samples = self.spinBox_MapM_YSamples.value()
        y_step = (y1 - y0) / (y_samples - 1)
        self.lineEdit_MapM_YStep.setText(f"{y_step:.6f}")

    def nidaq_task_channels_changed(self, ch_type: str, chs: list):
        if ch_type == 'ao':
            nidaq_ao_chs = chs
            setup_main_logger.debug(f"{nidaq_ao_chs}", extra={"component": "Main"})
            self.comboBox_MapM_NIDAQChX.clear()
            self.comboBox_MapM_NIDAQChX.addItems(nidaq_ao_chs)

            self.comboBox_MapM_NIDAQChY.clear()
            self.comboBox_MapM_NIDAQChY.addItems(nidaq_ao_chs)

            # self.comboBox_MapM_NIDAQChZ.clear()
            # self.comboBox_MapM_NIDAQChZ.addItems(nidaq_ao_chs)
        elif ch_type == 'ai':
            nidaq_ai_chs = chs
            setup_main_logger.debug(f"{nidaq_ai_chs}", extra={"component": "Main"})

            self.comboBox_MapM_NIDAQChIn.clear()
            self.comboBox_MapM_NIDAQChIn.addItems(nidaq_ai_chs)

            self.comboBox_PhotoDiode_NIDAQ_Channel.clear()
            self.comboBox_PhotoDiode_NIDAQ_Channel.addItems(nidaq_ai_chs)

    def nidaq_ai_values_changed(self, values: dict):
        # TODO
        # global setup_main_logger
        # for ch in values.keys():
        #    setup_main_logger.debug(f"NI DAQ Get {ch} = {np.average(values[ch])}", extra={"component": "Main"})
        self.lineEdit_MapM_NiVolIn.setText(f"{float2str(np.average(values[self.comboBox_MapM_NIDAQChIn.currentText()]))}")

    def nidaq_ao_values_changed(self, values: dict):
        # TODO
        # global setup_main_logger
        # setup_main_logger.debug(f"{values}", extra={"component": "Main"})
        x_ch = self.comboBox_MapM_NIDAQChX.currentText()
        y_ch = self.comboBox_MapM_NIDAQChY.currentText()
        # z_ch = self.comboBox_MapM_NIDAQChZ.currentText()

        if x_ch in values.keys():
            self.label_Piezo_X.setText(f"{(values[x_ch]-5)*10:.4f}")
            self.lineEdit_MapM_NiVolX.setText(f"{float2str(values[x_ch])}")
        if y_ch in values.keys():
            self.label_Piezo_Y.setText(f"{(values[y_ch]-5)*10:.4f}")
            self.lineEdit_MapM_NiVolY.setText(f"{float2str(values[y_ch])}")

        # if z_ch in values.keys():
        #     self.label_Piezo_Z.setText(f"{(values[z_ch]-5)*10:.4f}")

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

    def piezo_goto_xyz(self, x: float, y: float, z: float or None = None):
        x_ch = self.comboBox_MapM_NIDAQChX.currentText()
        y_ch = self.comboBox_MapM_NIDAQChY.currentText()
        # z_ch = self.comboBox_MapM_NIDAQChZ.currentText()

        ao_dict = {x_ch: 0.1*x+5, y_ch: 0.1*y+5}

        # if z is not None:
        #     z_value_dict = {z_ch: 0.1*y+5}
        # else:
        #     z_value_dict = {}
        z_value_dict = {}

        if _TEST_NO_NIDAQ:
            x_ch = 'ao0'
            y_ch = 'ao1'
            self.nidaq_man.ao_values_changed.emit(ao_dict)
        else:
            self.nidaq_man.write_task_channels('ao', ao_dict)

        self.piezo_cur_x = x
        self.piezo_cur_y = y
        setup_main_logger.debug(f"Move piezo stage to x, y, z ({x}, {y}, {z})"
                                f"by {ao_dict}", extra={"component": "Main/MAPM"})

    def pdv_refresh(self, b_auto: bool = False, interval: int = 1000):
        pdv_ai_ch = self.comboBox_PhotoDiode_NIDAQ_Channel.currentText()
        if pdv_ai_ch != "":
            res_dict = self.nidaq_man.read_task_channels('ai', 128)
            ts = time.time() * 1000
            if pdv_ai_ch not in res_dict.keys():
                setup_main_logger.error(f"PDV CH {pdv_ai_ch} not in the NIDAQ enabled AI channels",
                                        extra={"component": "Main/PDV"})
                return
            if self.pdv_update_ts is None:
                self.widget_PDVPlot.add_data(0, np.average(res_dict[pdv_ai_ch]))
                self.pdv_update_ts = ts
            else:
                self.widget_PDVPlot.add_data(ts - self.pdv_update_ts, np.average(res_dict[pdv_ai_ch]))
        else:
            setup_main_logger.error(f"Invalid PDV NIDAQ Channel",
                                    extra={"component": "Main/PDV"})

        if b_auto:
            if self.pushButton_PDV_AutoRefresh.isChecked():
                QTimer.singleShot(interval, lambda: self.pdv_refresh(True, interval))

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


if __name__ == '__main__':
    # import pdb
    # pdb.set_trace()
    app = QApplication(sys.argv)
    main_control = SetupMainWindow()

    app.exec_()

