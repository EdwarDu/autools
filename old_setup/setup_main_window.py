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

_MAPM_TEST = False

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

        self.pushButton_MapM_GoX0.clicked.connect(
            lambda: self.piezo_goto_xyz(x=self.doubleSpinBox_MapM_X0.value(), y=self.piezo_cur_y))
        self.pushButton_MapM_GoY0.clicked.connect(
            lambda: self.piezo_goto_xyz(x=self.piezo_cur_x, y=self.doubleSpinBox_MapM_Y0.value()))

        self.pushButton_MapM_Measure.clicked.connect(
            lambda: self.mapm_measure(n_avg=self.spinBox_MapM_NSamplesAvg.value()))
        self.pushButton_MapM_Auto.clicked.connect(lambda: self.mapm_measure_auto())
        self.pushButton_MapM_Export.clicked.connect(self.mapm_export)
        self.pushButton_MapM_Load.clicked.connect(self.mapm_load_npraw)

        self.save_settings_diag = SaveSettingsWindow(self.sr830_man, self.nidaq_man)
        self.pushButton_SaveSettings.clicked.connect(lambda: self.save_settings_diag.show())

        self.mapm_last_incomplete_scan = None
        self.window.show()

    def mapm_export(self):
        folder = os.path.normpath(QFileDialog.getExistingDirectory(
            self.window, 'Select folder to put the exported images'))
        prefix = os.path.join(folder, "lockin_x")
        self.widget_MeasurementPlot1.export_image(prefix)
        prefix = os.path.join(folder, "lockin_y")
        self.widget_MeasurementPlot2.export_image(prefix)
        prefix = os.path.join(folder, "pd_vol")
        self.widget_MeasurementPlot3.export_image(prefix)
        setup_main_logger.info(f"Files exported to {folder} with prefix {{lockin_x/lockin_y}}",
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

    def mapm_measure(self, n_avg: int = 1):
        x_l, y_l, vol_l = [np.zeros(n_avg, dtype=np.float) for i in range(0, 3)]

        for i in range(0, n_avg):
            # Lock In
            if _MAPM_TEST:
                x_l[i], y_l[i], vol_l[i] = np.abs(np.random.randn(2))
            else:
                x_l[i], y_l[i] = self.sr830_man.get_parameters_value(SR830Man.GET_PARAMETER_X, SR830Man.GET_PARAMETER_Y)
                vol_l[i] = self.nidaq_man.read_task_channels("ai")[self.comboBox_MapM_NIDAQChIn.currentText()]
                setup_main_logger.debug(f"Measurement: {x_l[i]} {y_l[i]} {vol_l[i]}",
                                        extra={"component": "Main/MAPM"})
        x, y, vol = np.average(x_l), np.average(y_l), np.average(vol_l)
        setup_main_logger.debug(f"Measurement AVG: {x} {y} {vol}",
                                extra={"component": "Main/MAPM"})
        self.lineEdit_MapM_LockInX.setText(float2str(x))
        self.lineEdit_MapM_LockInY.setText(float2str(y))
        self.lineEdit_MapM_NiVolIn.setText(float2str(vol))
        return x, y, vol

    def mapm_measure_auto(self):
        # TODO: Run Automeasure task
        if self.mapm_last_incomplete_scan is not None and \
                len(self.mapm_last_incomplete_scan) != 0:
            ans = QMessageBox.question(self.window, f"Previous scan incomplete", "Continue?",
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

            measure_delay_ms = self.spinBox_MapM_MeasureDelay.value()

            setup_main_logger.info(f"Map scan from {x0:.6f},{y0:.6f} to {x1:.6f},{y1:.6f} "
                                   f"#Samples X={x_samples}, Y={y_samples} "
                                   f"NIDAQ Ch X={ni_x_ch}, Y={ni_y_ch} In={ni_in_ch} "
                                   f"Measure delay {measure_delay_ms} ms", extra={"component": "Main/MAPM"})

            self.piezo_goto_xyz(x=x0, y=y0)

            # we only overwrite this if it is "check pzt"
            self.mapm_last_incomplete_scan = {
                "x0": x0, "y0": y0, "x1": x1, "y1": y1, "x_samples": x_samples, "y_samples": y_samples,
                "measure_delay_ms": measure_delay_ms,
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

            self.doubleSpinBox_MapM_X0.setValue(x0)
            self.doubleSpinBox_MapM_Y0.setValue(y0)
            self.doubleSpinBox_MapM_X1.setValue(x1)
            self.doubleSpinBox_MapM_Y1.setValue(y1)

            x_values = np.linspace(x0, x1, x_samples)
            y_values = np.linspace(y0, y1, y_samples)

            measure_delay_ms = self.mapm_last_incomplete_scan["measure_delay_ms"]

            self.comboBox_MapM_NIDAQChX.setCurrentText(ni_x_ch)
            self.comboBox_MapM_NIDAQChY.setCurrentText(ni_y_ch)
            self.comboBox_MapM_NIDAQChIn.setCurrentText(ni_in_ch)
            self.spinBox_MapM_MeasureDelay.setValue(measure_delay_ms)
            QtWidgets.qApp.processEvents()

            setup_main_logger.info(f"Resume map scan from {x0:.6f},{y0:.6f} to {x1:.6f},{y1:.6f} "
                                   f"#Samples X={x_samples}, Y={y_samples} "
                                   f"NIDAQ Ch X={ni_x_ch}, Y={ni_y_ch} In={ni_in_ch} "
                                   f"Measure delay {measure_delay_ms} ms", extra={"component": "Main/MAPM"})

        # if not b_only_check_pzt:
        # Set up plots
        self.widget_MeasurementPlot1.set_xy_list(x_values, y_values)
        self.widget_MeasurementPlot2.set_xy_list(x_values, y_values)
        self.widget_MeasurementPlot3.set_xy_list(x_values, y_values)

        row_index = 0
        for y in y_values:
            x_track = x_values if row_index % 2 == 0 else np.flip(x_values)
            for x in x_track:
                # Go to x, y
                setup_main_logger.info(f"Piezo going to {x:.6f}, {y:.6f}", extra={"component": "Main/MAPM"})
                self.piezo_goto_xyz(x=x, y=y)
                QtWidgets.qApp.processEvents()
                if (x, y) not in self.mapm_last_incomplete_scan["scanned_data"].keys():
                    t0 = datetime.now()
                    while (datetime.now() - t0).total_seconds() < measure_delay_ms / 1000:
                        QtWidgets.qApp.processEvents()
                    lockin_x, lockin_y, vol = self.mapm_measure(n_avg=self.spinBox_MapM_NSamplesAvg.value())
                else:
                    lockin_x, lockin_y, vol = self.mapm_last_incomplete_scan["scanned_data"][(x, y)]

                self.widget_MeasurementPlot1.set_xy_value(x, y, lockin_x)
                self.widget_MeasurementPlot2.set_xy_value(x, y, lockin_y)
                self.widget_MeasurementPlot3.set_xy_value(x, y, vol)
                self.mapm_last_incomplete_scan["scanned_data"][(x, y)] = (lockin_x, lockin_y, vol)
            else:
                row_index += 1
                continue

        self.mapm_last_incomplete_scan = None  # scan complete remove incomplete save

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

            self.comboBox_MapM_NIDAQChZ.clear()
            self.comboBox_MapM_NIDAQChZ.addItems(nidaq_ao_chs)
        elif ch_type == 'ai':
            nidaq_ai_chs = chs
            setup_main_logger.debug(f"{nidaq_ai_chs}", extra={"component": "Main"})

            self.comboBox_MapM_NIDAQChIn.clear()
            self.comboBox_MapM_NIDAQChIn.addItems(nidaq_ai_chs)

    def nidaq_ai_values_changed(self, values):
        # TODO
        # global setup_main_logger
        # setup_main_logger.debug(f"{values}", extra={"component": "Main"})
        pass

    def nidaq_ao_values_changed(self, values: dict):
        # TODO
        # global setup_main_logger
        # setup_main_logger.debug(f"{values}", extra={"component": "Main"})
        x_ch = self.comboBox_MapM_NIDAQChX.currentText()
        y_ch = self.comboBox_MapM_NIDAQChY.currentText()
        # z_ch = self.comboBox_MapM_NIDAQChZ.currentText()

        if x_ch in values.keys():
            self.label_Piezo_X.setText(f"{(values[x_ch]-5)*10:.4f}")
        if y_ch in values.keys():
            self.label_Piezo_Y.setText(f"{(values[y_ch]-5)*10:.4f}")
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

        if _MAPM_TEST:
            self.nidaq_man.ao_values_changed.emit(ao_dict)
        else:
            self.nidaq_man.write_task_channels('ao', ao_dict)
        self.piezo_cur_x = x
        self.piezo_cur_y = y
        setup_main_logger.debug(f"Move piezo stage to x, y, z ({x}, {y}, {z})"
                                f"by {ao_dict}", extra={"component": "Main/MAPM"})

if __name__ == '__main__':
    # import pdb
    # pdb.set_trace()
    app = QApplication(sys.argv)
    main_control = SetupMainWindow()

    app.exec_()

