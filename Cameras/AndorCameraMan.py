#!/usr/bin/python3

import os
import ctypes

import time
from .CameraMan import CameraMan
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QDir, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
import json

from pyandor3 import Andor3Man


class AndorCameraMan(CameraMan):
    ANDOR3_FEATURES = {
        "AccumulateCount" : {"type": "i",},
        # "AcquiredCount" : {"type": "i",},
        "AcquisitionStart" : {"type": "c",},
        "AcquisitionStop" : {"type": "c",},
        "AlternatingReadoutDirection" : {"type": "b",},
        "AOIBinning" : {"type": "enum",},
        "AOIHBin" : {"type": "i",},
        "AOIHeight" : {"type": "i",},
        "AOILayout" : {"type": "enum",},
        "AOILeft" : {"type": "i",},
        "AOIStride" : {"type": "i",},
        "AOITop" : {"type": "i",},
        "AOIVBin" : {"type": "i",},
        "AOIWidth" : {"type": "i",},
        "AuxiliaryOutSource" : {"type": "enum",},
        "AuxOutSourceTwo" : {"type": "enum",},
        #"BackoffTemperatureOffset" : {"type": "f",},
        "Baseline" : {"type": "i",},
        "BitDepth" : {"type": "enum",},
        "BufferOverflowEvent" : {"type": "i",},
        "BytesPerPixel" : {"type": "f",},
        "CameraAcquiring" : {"type": "b",},
        "CameraDump" : {"type": "c",},
        #"CameraFamily" : {"type": "s",},
        #"CameraMemory" : {"type": "i",},
        "CameraModel" : {"type": "s",},
        "CameraName" : {"type": "s",},
        "CameraPresent" : {"type": "b",},
        #"ColourFilter" : {"type": "enum",},
        "ControllerID" : {"type": "s",}, # Neo, Zyla (CameraLink)
        #"CoolerPower" : {"type": "f",},
        "CycleMode" : {"type": "enum",},
        #"DDGInsertionDelay" : {"type": "enum",},
        #"DDGIOCEnable" : {"type": "b",},
        #"DDGIOCNumberOfPulses" : {"type": "i",},
        #"DDGIOCPeriod" : {"type": "i",},
        #"DDGOutputDelay" : {"type": "i",},
        #"DDGOutputEnable" : {"type": "b",},
        #"DDGOutputStepEnable" : {"type": "b",},
        #"DDGOpticalWidthEnable" : {"type": "b",},
        #"DDGOutputPolarity" : {"type": "enum",},
        #"DDGOutputSelector" : {"type": "enum",},
        #"DDGOutputWidth" : {"type": "i",},
        #"DDGStepCount" : {"type": "i",},
        #"DDGStepDelayCoefficientA" : {"type": "f",},
        #"DDGStepDelayCoefficientB" : {"type": "f",},
        #"DDGStepDelayMode" : {"type": "enum",},
        #"DDGStepEnabled" : {"type": "b",},
        #"DDGStepUploadProgress" : {"type": "i",},
        #"DDGStepUploadRequired" : {"type": "b",},
        #"DDGStepWidthCoefficientA" : {"type": "f",},
        #"DDGStepWidthCoefficientB" : {"type": "f",},
        #"DDGStepWidthMode" : {"type": "enum",},
        #"DDGQueue" : {"type": "c",},
        #"DDGStepUploadModeValues" : {"type": "c",},
        #"DDR2Type" : {"type": "s",},
        "DeviceCount" : {"type": "i", "system": True},
        "DeviceVideoIndex" : {"type": "i",}, # Neo, Zyla (CameraLink)
        #"DisableShutter" : {"type": "b",},
        #"DriverVersion" : {"type": "s",},
        "ElectronicShutteringMode" : {"type": "enum",},
        "EventEnable" : {"type": "b",},
        "EventsMissedEvent" : {"type": "i",},
        "EventSelector" : {"type": "enum",},
        "ExposedPixelHeight" : {"type": "i",},
        "ExposureTime" : {"type": "f",},
        "ExposureEndEvent" : {"type": "i",},
        "ExposureStartEvent" : {"type": "i",},
        #"ExternalIOReadout" : {"type": "b",},
        "ExternalTriggerDelay" : {"type": "f",},
        "FanSpeed" : {"type": "enum",},
        "FastAOIFrameRateEnable" : {"type": "b",},
        "FirmwareVersion" : {"type": "s",},
        "ForceShutterOpen" : {"type": "b",},
        "FrameCount" : {"type": "i",},
        #"FrameInterval" : {"type": "f",},
        #"FrameIntervalTiming" : {"type": "b",},
        "FrameRate" : {"type": "f",},
        "FullAOIControl" : {"type": "b",},
        #"GateMode" : {"type": "enum",},
        #"HeatSinkTemperature" : {"type": "f",},
        "ImageSizeBytes" : {"type": "i",},
        #"InputVoltage" : {"type": "f",},
        "InterfaceType" : {"type": "s",},
        #"IOControl" : {"type": "f",},
        #"IODirection" : {"type": "enum",},
        #"IOState" : {"type": "b",},
        "IOInvert" : {"type": "b",},
        "IOSelector" : {"type": "enum",},
        #"IRPreFlashEnable" : {"type": "b",},
        #"KeepCleanEnable" : {"type": "b",},
        #"KeepCleanPostExposure Enable" : {"type": "b",},
        "LineScanSpeed" : {"type": "f",},
        "LUTIndex" : {"type": "i",},
        "LUTValue" : {"type": "i",},
        "MaxInterfaceTransferRate" : {"type": "f",},
        #"MCPGain" : {"type": "i",},
        #"MCPIntelligate" : {"type": "b",},
        #"MCPVoltage" : {"type": "i",},
        "MetadataEnable" : {"type": "b",},
        "MetadataFrame" : {"type": "b",},
        "MetadataTimestamp"  : {"type": "b",},
        #"MicrocodeVersion" : {"type": "s",},
        "MultitrackBinned" : {"type": "b",},
        "MultitrackCount" : {"type": "i",},
        "MultitrackEnd" : {"type": "i",},
        "MultitrackSelector" : {"type": "i",},
        "MultitrackStart" : {"type": "i",},
        "Overlap" : {"type": "b",},
        "PixelCorrection" : {"type": "enum",},
        "PixelEncoding" : {"type": "enum",},
        "PixelHeight" : {"type": "f",},
        "PixelReadoutRate" : {"type": "enum",},
        "PixelWidth" : {"type": "f",},
        #"PortSelector" : {"type": "i",},
        #"PreAmpGain" : {"type": "enum",},
        #"PreAmpGainChannel" : {"type": "enum",},
        #"PreAmpGainControl" : {"type": "enum",},
        #"PreAmpGainValue" : {"type": "i",},
        #"PreAmpGainSelector" : {"type": "enum",},
        #"PreAmpOffsetValue" : {"type": "i",},
        #"PreTriggerEnabled" : {"type": "b",},
        "ReadoutTime" : {"type": "f",},
        "RollingShutterGlobalClear" : {"type": "b",},
        "RowNExposureEndEvent" : {"type": "i",},
        "RowNExposureStartEvent" : {"type": "i",},
        "RowReadTime" : {"type": "f",},
        "ScanSpeedControlEnable" : {"type": "b",},
        "SensorCooling" : {"type": "b",},
        "SensorHeight" : {"type": "i",},
        #"SensorModel" : {"type": "s",},
        "SensorReadoutMode" : {"type": "enum",},
        #"SensorType" : {"type": "enum",},
        "SensorTemperature" : {"type": "f",},
        "SensorWidth" : {"type": "i",},
        "SerialNumber" : {"type": "s",},
        #"ShutterAmpControl" : {"type": "b",},
        #"ShutterMode" : {"type": "enum",},
        "ShutterOutputMode" : {"type": "enum",},
        #"ShutterState" : {"type": "b",},
        #"ShutterStrobePeriod" : {"type": "f",},
        #"ShutterStrobePosition" : {"type": "f",},
        "ShutterTransferTime" : {"type": "f",},
        "SimplePreAmpGainControl" : {"type": "enum",},
        "SoftwareTrigger" : {"type": "c",},
        "SoftwareVersion" : {"type": "s",},
        "SpuriousNoiseFilter" : {"type": "b",},
        "StaticBlemishCorrection" : {"type": "b",},
        "Synchronous Triggering" : {"type": "b",},
        #"TargetSensor Temperature" : {"type": "f",},
        "Temperature Control" : {"type": "enum",},
        "Temperature Status" : {"type": "enum",},
        "TimestampClock" : {"type": "i",},
        "TimestampClock Frequency" : {"type": "i",},
        "TimestampClock Reset" : {"type": "c",},
        #"TransmitFrames" : {"type": "b",},
        "TriggerMode" : {"type": "enum",},
        #"UsbProductId" : {"type": "i",},
        #"UsbDeviceId" : {"type": "i",},
        "VerticallyCentreAOI" : {"type": "b",},
    }

    camera_prop_changed = pyqtSignal(list, name="CameraPropChanged")

    def __init__(self, dev_id: int):
        super().__init__(cam_type="andor")
        self._dev_id = dev_id
        self._a3man = Andor3Man()
        self._buffer_ids = []
        self._frame_width = 0
        self._frame_height = 0
        self._frame_stride = 0
        self._dev_h = None
        self._pixel_encoding = None

        self._b_circular_buf_acquiring = False

        self.features = {}

        self.config_window = None
        self.config_window_ui_components = []
        # No Apogee/iStar-sCMOS only feature, check the doc
        self._a3man.load_feature_map(AndorCameraMan.ANDOR3_FEATURES)

        self.camera_prop_changed.connect(self._update_ui_values)

    def _create_circular_buffers(self, n_buffers: int = 10):
        has_binning = self._a3man.is_feature_implemented("AOIBinning")
        if has_binning:
            previous_index = self._a3man.get_e_feature_index("AOIBinning")
            self._a3man.set_e_feature("AOIBinning", "1x1")

        # create max_image_size buffer, so we do not need to re-allocate
        max_image_size = 4 * (self._a3man.get_i_feature_max("AOIWidth") + 4) * self._a3man.get_i_feature_max("AOIHeight")
        
        if has_binning:
            self._a3man.set_e_feature("AOIBinning", previous_index)
        
        for i in range(0, n_buffers):
            self._buffer_ids.append(self._a3man.create_buffer(max_image_size))

    def _start_circular_buffers(self,):
        if len(self._buffer_ids) == 0:
            self._create_circular_buffers()

        if self._a3man.is_feature_writable('AcquisitionStop'):
            self._a3man.send_command("AcquisitionStop")
        self._a3man.flush()
        self._b_circular_buf_acquiring = False

        self._a3man.set_e_feature("CycleMode", "Continuous")
        for buf_id in self._buffer_ids:
            self._a3man.queue_buffer(buf_id)
        if self._a3man.is_feature_writable('AcquisitionStart'):
            self._a3man.send_command("AcquisitionStart") 
        self._b_circular_buf_acquiring = True

    def _stop_circular_buffers(self,):
        if self._a3man.is_feature_writable('AcquisitionStop'):
            self._a3man.send_command("AcquisitionStop")
        self._a3man.flush()
        self._b_circular_buf_acquiring = False

    def __del__(self, ):
        # free all the buffers
        if len(self._buffer_ids) != 0:
            for id in self._buffer_ids:
                self._a3man.free_buffer(id)
            self._buffer_ids = []

    def get_dev_id(self):
        return self._dev_id

    def open(self):
        self._a3man.open_dev(self._dev_id)
        self._dev_h = self._a3man.get_dev_handle()
        self._set_features(AndorCameraMan.ANDOR3_FEATURES, True)
        self._frame_height = self._a3man.get_i_feature("AOIHeight")
        self._frame_width = self._a3man.get_i_feature("AOIWidth")
        self._frame_stride = self._a3man.get_i_feature("AOIStride")
        self._pixel_encoding = self._a3man.get_e_feature_str("PixelEncoding")
        self._start_circular_buffers()
        self._a3man.register_feature_cb("AOIWidth", lambda feature_name: self._frame_width_changed())
        self._a3man.register_feature_cb("AOIHeight", lambda feature_name: self._frame_height_changed())
        self._a3man.register_feature_cb("AOIStride", lambda feature_name: self._frame_stride_changed())
        self._a3man.register_feature_cb('PixelEncoding', lambda feature_name: self._pixel_encoding_changed())

    def is_open(self):
        return self._a3man.is_open()

    def close(self):
        if self.config_window is not None:
            self.config_window.close()
            for feature in self.features.keys():
                if self.features[feature]['type'] != 'c' and \
                        self.features[feature]['b_implemented'] and \
                        ('b_readable' in self.features[feature].keys() and self.features[feature]['b_readable']) and \
                        ('system' not in self.features[feature].keys() or not self.features[feature]['system']):
                    self._a3man.clear_feature_cb(feature)

        # Only single buffer is supported, in case NOT, this needs to be modified also
        if self._buffer_id is not None:
            self._a3man.free_buffer(self._buffer_id)
        self._a3man.close()

    def get_frame_size(self):
        if self._frame_width == 0 or self._frame_height == 0:
            self._frame_width = self._a3man.get_i_feature("AOIWidth")
            self._frame_height = self._a3man.get_i_feature("AOIHeight")
            self._frame_stride = self._a3man.get_i_feature("AOIStride")
        return self._frame_width, self._frame_height, 1

    def _frame_height_changed(self):
        frame_height = self._a3man.get_i_feature("AOIHeight")
        if frame_height != self._frame_height:
            self._frame_height = frame_height
            self._start_circular_buffers()  # causing circular buffer stop, flush and start again
            # WARNING: do not change anything affecting AOIHeight, AOIWidth, AOIStride, and PixelEncoding
            #  Probably is okay, but may have glitch in the image acquisition

    def _frame_width_changed(self):
        frame_width = self._a3man.get_i_feature("AOIWidth")
        if frame_width != self._frame_width:
            self._frame_width = frame_width
            self._start_circular_buffers()

    def _frame_stride_changed(self):
        frame_stride = self._a3man.get_i_feature("AOIStride")
        if frame_stride != self._frame_stride:
            self._frame_stride = frame_stride
            self._start_circular_buffers()

    def _pixel_encoding_changed(self):
        pixel_encoding = self._a3man.get_e_feature_str("PixelEncoding")
        if pixel_encoding != self._pixel_encoding:
            self._pixel_encoding = pixel_encoding
            self._start_circular_buffers()

    # TODO: speed up this with double buffer?
    def grab_frame(self, n_channel_index: int):
        # n_channel_index is ignored as currently only mono cam is supported
        if not self._b_circular_buf_acquiring: self._start_circular_buffers()
        try:
            buffer_id, buffer_rd_size = self._a3man.wait_buffer(30000)  # wait for 30s
            raw_bytes = self._a3man.get_data_from_buffer(buffer_id, buffer_rd_size)
            self._a3man.queue_buffer(buffer_id)
            np_arr = Andor3Man.convert_bytes_to_numpy_array(
                raw_bytes,
                self._pixel_encoding,
                self._frame_stride,
                self._frame_width,
                self._frame_height
            )
            return np_arr
        except:
            return None

    def _set_features(self, features: dict, b_update: bool = False):
        self.features = features
        if b_update:
            for feature in self.features.keys():
                feature_type = self.features[feature]['type']
                self.features[feature]['b_implemented'] = self._a3man.is_feature_implemented(feature)
                if not self.features[feature]['b_implemented']:
                    continue

                if feature_type == 'i' or feature_type == 'f':
                    self.features[feature]['b_readable'] = self._a3man.is_feature_readable(feature)
                    if not self.features[feature]['b_readable']:
                        continue
                    self.features[feature]['b_writable'] = self._a3man.is_feature_writable(feature)
                    self.features[feature]['min'] = self._a3man.get_i_feature_min(feature) if feature_type == 'i' \
                        else self._a3man.get_f_feature_min(feature)
                    self.features[feature]['max'] = self._a3man.get_i_feature_max(feature) if feature_type == 'i' \
                        else self._a3man.get_f_feature_max(feature)
                elif feature_type == 'c':
                    self.features[feature]['b_readable'] = self._a3man.is_feature_readable(feature)
                    if not self.features[feature]['b_readable']:
                        continue
                    self.features[feature]['b_writable'] = self._a3man.is_feature_writable(feature)
                elif feature_type == 's':
                    self.features[feature]['b_readable'] = self._a3man.is_feature_readable(feature)
                    if not self.features[feature]['b_readable']:
                        continue

                    self.features[feature]['b_writable'] = self._a3man.is_feature_writable(feature)
                elif feature_type == 'b':
                    self.features[feature]['b_readable'] = self._a3man.is_feature_readable(feature)
                    if not self.features[feature]['b_readable']:
                        continue

                    self.features[feature]['b_writable'] = self._a3man.is_feature_writable(feature)
                elif feature_type == 'enum':
                    self.features[feature]['b_readable'] = self._a3man.is_feature_readable(feature)
                    if not self.features[feature]['b_readable']:
                        continue

                    self.features[feature]['b_writable'] = self._a3man.is_feature_writable(feature)
                    self.features[feature]['n_options'] = self._a3man.get_e_feature_count(feature)
                    self.features[feature]['options'] = []
                    for i in range(0, self.features[feature]['n_options']):
                        if self._a3man.is_e_feature_index_implemented(feature, i):
                            self.features[feature]['options'].append(self._a3man.get_e_feature_str_at(feature, i))
                        else:
                            self.features[feature]['options'].append(
                                "N/A: " + self._a3man.get_e_feature_str_at(feature, i))

    def _save_config(self):
        options = QFileDialog.Options()
        andor_cam_config_fname, _ = QFileDialog.getSaveFileName(
            self.config_window, "Save the Andor camera paramenters", QDir.currentPath(),
            "Config Files (*.json)", options=options)
        if andor_cam_config_fname:
            config_values = {}
            for feature in self.features.keys():
                feature_type = self.features[feature]['type']
                b_implemented = self.features[feature]['b_implemented']
                if not b_implemented:
                    continue
                b_writable = self.features[feature]['b_writable'] \
                    if 'b_writable' in self.features[feature].keys() else False
                if not b_writable:
                    continue

                config_values[feature] = {}
                if feature_type == 'i' or feature_type == 'f':
                    config_values[feature]['type'] = feature_type
                    config_values[feature]['value'] = self._a3man.get_i_feature(feature) if feature_type == 'i' \
                        else self._a3man.get_f_feature(feature)
                elif feature_type == 's':
                    config_values[feature]['type'] = feature_type
                    config_values[feature]['value'] = self._a3man.get_s_feature(feature)
                elif feature_type == 'b':
                    config_values[feature]['type'] = feature_type
                    config_values[feature]['value'] = self._a3man.get_b_feature(feature)
                elif feature_type == 'enum':
                    config_values[feature]['type'] = feature_type
                    config_values[feature]['value'] = self._a3man.get_e_feature(feature)

            with open(andor_cam_config_fname, 'w') as f_cfg:
                json.dump(config_values, f_cfg)

    def _load_config(self):
        options = QFileDialog.Options()
        andor_cam_config_fname, _ = QFileDialog.getOpenFileName(
            self.config_window, "Load the Andor camera paramenters", QDir.currentPath(),
            "Config Files (*.json)", options=options)
        if andor_cam_config_fname:
            with open(andor_cam_config_fname, 'r') as f_cfg:
                config_values = json.load(f_cfg)

            for feature in config_values.keys():
                if feature not in self.features.keys():
                    continue

                feature_type = config_values[feature]['type']
                b_implemented = self.features[feature]['b_implemented']
                if not b_implemented:
                    continue
                b_writable = self.features[feature]['b_writable'] \
                    if 'b_writable' in self.features[feature].keys() else False
                if not b_writable:
                    continue

                if feature_type == 'i':
                    self._a3man.set_i_feature(feature, config_values[feature]['value'])
                elif feature_type == 'f':
                    self._a3man.set_f_feature(feature, config_values[feature]['value'])
                elif feature_type == 's':
                    self._a3man.set_s_feature(feature, config_values[feature]['value'])
                elif feature_type == 'b':
                    self._a3man.set_b_feature(feature, config_values[feature]['value'])
                elif feature_type == 'enum':
                    self._a3man.set_e_feature(feature, config_values[feature]['value'])

        self._update_ui_values()

    def _populate_config_window(self):
        self.config_window = QtWidgets.QScrollArea(self.config_window)
        self.config_window.setWindowTitle("Andor Camera Configuration")

        scrollarea_contents = QtWidgets.QWidget()
        self.config_window.setWidget(scrollarea_contents)
        self.config_window.setWidgetResizable(True)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        size_policy.setHorizontalStretch(1)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(scrollarea_contents.sizePolicy().hasHeightForWidth())
        scrollarea_contents.setSizePolicy(size_policy)

        self.config_window_ui_components.append(scrollarea_contents)

        features_grid_layout = QtWidgets.QGridLayout()
        self.config_window_ui_components.append(features_grid_layout)

        verticalbox = QtWidgets.QVBoxLayout(scrollarea_contents)
        self.config_window_ui_components.append(verticalbox)

        horizontalbox = QtWidgets.QHBoxLayout(scrollarea_contents)
        save_button = QtWidgets.QPushButton(scrollarea_contents)
        save_button.setText("SAVE ...")
        save_button.clicked.connect(lambda a: self._save_config())
        load_button = QtWidgets.QPushButton(scrollarea_contents)
        load_button.setText("LOAD ...")
        load_button.clicked.connect(lambda a: self._load_config())
        horizontalbox.addWidget(save_button, 1)
        horizontalbox.addWidget(load_button, 1)
        horizontalbox.setSpacing(20)

        verticalbox.addItem(horizontalbox)
        verticalbox.addItem(features_grid_layout)

        verticalbox.addSpacerItem(
            QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        item_index = 0
        for feature in self.features.keys():
            feature_type = self.features[feature]['type']
            item_index_row = int(item_index / 2)
            item_index_col = item_index % 2 * 2

            if not self.features[feature]['b_implemented']:
                continue

            if feature_type == 'i' or feature_type == 'f':
                if not self.features[feature]['b_readable']:
                    continue

                # Label
                label = QtWidgets.QLabel(scrollarea_contents)
                label.setText(feature)
                self.config_window_ui_components.append(label)
                label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                features_grid_layout.addWidget(label, item_index_row, item_index_col, 1, 1)
                # Control / Display Component
                if self.features[feature]['b_writable']:
                    spinbox = QtWidgets.QSpinBox(scrollarea_contents) if feature_type == 'i' \
                        else QtWidgets.QDoubleSpinBox(scrollarea_contents)
                    spinbox.setMinimum(self.features[feature]['min'])
                    spinbox.setMaximum(self.features[feature]['max'])
                    spinbox.setSingleStep(1 if feature_type == 'i' else 0.1)
                    if feature_type == 'f':
                        spinbox.setDecimals(4)
                    spinbox.setKeyboardTracking(False)
                    spinbox.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                    if feature_type == 'i':
                        spinbox.valueChanged.connect(lambda a, f=feature: self._a3man.set_i_feature(f, a))
                    else:
                        spinbox.valueChanged.connect(lambda a, f=feature: self._a3man.set_f_feature(f, a))
                    self.config_window_ui_components.append(spinbox)
                    self.features[feature]['ui_widget'] = spinbox

                    features_grid_layout.addWidget(spinbox, item_index_row, item_index_col + 1, 1, 1)
                else:
                    lineedit = QtWidgets.QLineEdit(scrollarea_contents)
                    lineedit.setReadOnly(True)
                    lineedit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                    self.config_window_ui_components.append(lineedit)
                    self.features[feature]['ui_widget'] = lineedit
                    features_grid_layout.addWidget(lineedit, item_index_row, item_index_col + 1, 1, 1)
                item_index += 1
            elif feature_type == 's':
                if not self.features[feature]['b_readable']:
                    continue

                # Label
                label = QtWidgets.QLabel(scrollarea_contents)
                label.setText(feature)
                self.config_window_ui_components.append(label)
                label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                features_grid_layout.addWidget(label, item_index_row, item_index_col, 1, 1)
                # Control / Display Component
                lineedit = QtWidgets.QLineEdit(scrollarea_contents)
                if self.features[feature]['b_writable']:
                    lineedit.returnPressed.connect(
                        lambda f=feature, le=lineedit: self._a3man.set_s_feature(f, le.text()))
                else:
                    lineedit.setReadOnly(True)
                lineedit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                self.config_window_ui_components.append(lineedit)
                self.features[feature]['ui_widget'] = lineedit
                features_grid_layout.addWidget(lineedit, item_index_row, item_index_col + 1, 1, 1)
                item_index += 1
            elif feature_type == 'b':
                if not self.features[feature]['b_readable']:
                    continue

                checkbox = QtWidgets.QCheckBox(scrollarea_contents)
                checkbox.setText(feature)

                self.config_window_ui_components.append(checkbox)
                if self.features[feature]['b_writable']:
                    checkbox.setCheckable(True)
                    checkbox.clicked.connect(lambda a, f=feature: self._a3man.set_b_feature(f, a))
                else:
                    checkbox.setCheckable(False)
                self.features[feature]['ui_widget'] = checkbox
                features_grid_layout.addWidget(checkbox, item_index_row, item_index_col, 1, 2)
                item_index += 1
            elif feature_type == 'enum':
                if not self.features[feature]['b_readable']:
                    continue

                # Label
                label = QtWidgets.QLabel(scrollarea_contents)
                label.setText(feature)
                self.config_window_ui_components.append(label)
                label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                features_grid_layout.addWidget(label, item_index_row, item_index_col, 1, 1)
                # Control / Display Widget
                if self.features[feature]['b_writable']:
                    combobox = QtWidgets.QComboBox(scrollarea_contents)
                    combobox.setEditable(False)
                    for i in range(0, self.features[feature]['n_options']):
                        combobox.addItem(f"{i:d}: {self.features[feature]['options'][i]}", i)
                    self.config_window_ui_components.append(combobox)
                    combobox.currentIndexChanged.connect(
                        lambda index, f=feature, cbox=combobox:
                        cbox.setCurrentIndex(self._a3man.set_e_feature_check(f, index))
                    )
                    self.features[feature]['ui_widget'] = combobox
                    features_grid_layout.addWidget(combobox, item_index_row, item_index_col + 1, 1, 1)

                else:
                    lineedit = QtWidgets.QLineEdit(scrollarea_contents)
                    lineedit.setReadOnly(True)
                    self.config_window_ui_components.append(lineedit)
                    self.features[feature]['ui_widget'] = lineedit
                    features_grid_layout.addWidget(lineedit, item_index_row, item_index_col + 1, 1, 1)
                item_index += 1
            elif feature_type == 'c':
                pushbutton = QtWidgets.QPushButton(scrollarea_contents)
                pushbutton.setText(f"CMD: {feature}")
                self.config_window_ui_components.append(pushbutton)
                pushbutton.clicked.connect(lambda a, f=feature: self._command_button_pushed(f))
                self.features[feature]['ui_widget'] = pushbutton
                features_grid_layout.addWidget(pushbutton, item_index_row, item_index_col, 1, 2)
                item_index += 1

        features_grid_layout.setColumnStretch(1, 1)
        features_grid_layout.setColumnStretch(3, 1)
        features_grid_layout.setHorizontalSpacing(12)
        features_grid_layout.setVerticalSpacing(6)

        self._update_ui_values()

    @QtCore.pyqtSlot()
    def _command_button_pushed(self, feature):
        try:
            btn = self.sender()
            btn.setStyleSheet("")
            self._a3man.send_command(feature)
            btn.setStyleSheet("background: green")
        except Exception as e:
            btn.setStyleSheet("background: red")

    def _update_ui_values(self, feature_name: str or list or tuple = None):
        features_update = []
        if feature_name is None:
            features_update = self.features.keys()
        elif type(feature_name) is str and feature_name in self.features.keys():
            features_update = [feature_name, ]
        elif type(feature_name) is (list or tuple):
            features_update = [x for x in feature_name if x in self.features.keys()]

        # Manual hack
        if ("Temperature Status" in features_update or "SensorCooling" in features_update) \
                and "SensorTemperature" not in features_update:
            features_update.append("SensorTemperature")

        aoi_features = ["AOIBinning", "AOIHeight", "AOILeft", "AOIStride", "AOITop", "AOIWidth"]
        b_aoi_notified = False
        for feature in features_update:
            if feature.startswith("AOI"):
                b_aoi_notified = True

        if b_aoi_notified:
            for feature in aoi_features:
                if feature not in features_update:
                    features_update.append(feature)

        for feature in features_update:
            if not self.features[feature]['b_implemented']:
                continue

            feature_type = self.features[feature]['type']
            if feature_type == 'i' or feature_type == 'f':
                if not self.features[feature]['b_readable']:
                    continue

                feature_value = self._a3man.get_i_feature(feature) if feature_type == 'i' \
                    else self._a3man.get_f_feature(feature)

                ui_comp = self.features[feature]['ui_widget']
                if self.features[feature]['b_writable']:
                    max_new = self._a3man.get_i_feature_max(feature) if feature_type == 'i' else \
                        self._a3man.get_f_feature_max(feature)
                    min_new = self._a3man.get_i_feature_min(feature) if feature_type == 'i' else \
                        self._a3man.get_f_feature_min(feature)
                    ui_comp.blockSignals(True)
                    ui_comp.setMaximum(max_new)
                    ui_comp.setMinimum(min_new)
                    ui_comp.setValue(feature_value)
                    ui_comp.blockSignals(False)
                else:
                    ui_comp.setText(f"{feature_value}")
            elif feature_type == 's':
                if not self.features[feature]['b_readable']:
                    continue

                feature_value = self._a3man.get_s_feature(feature)
                ui_comp = self.features[feature]['ui_widget']
                ui_comp.blockSignals(True)
                ui_comp.setText(feature_value)
                ui_comp.blockSignals(False)
            elif feature_type == 'b':
                if not self.features[feature]['b_readable']:
                    continue

                ui_comp = self.features[feature]['ui_widget']
                ui_comp.blockSignals(True)
                ui_comp.setChecked(self._a3man.get_b_feature(feature))
                ui_comp.blockSignals(False)
            elif feature_type == 'enum':
                self.features[feature]['b_readable'] = self._a3man.is_feature_readable(feature)
                if not self.features[feature]['b_readable']:
                    continue

                ui_comp = self.features[feature]['ui_widget']
                if self.features[feature]['b_writable']:
                    n_options = self._a3man.get_e_feature_count(feature)
                    options = []
                    for i in range(0, n_options):
                        if self._a3man.is_e_feature_index_implemented(feature, i) and \
                                self._a3man.is_e_feature_index_available(feature, i):
                            options.append(self._a3man.get_e_feature_str_at(feature, i))
                        else:
                            options.append("N/A: " + self._a3man.get_e_feature_str_at(feature, i))

                    self.features[feature]['n_options'] = n_options
                    self.features[feature]['options'] = options

                    feature_index = self._a3man.get_e_feature_index(feature)
                    if ui_comp.currentIndex() != feature_index:
                        ui_comp.blockSignals(True)
                        ui_comp.clear()
                        for i in range(0, n_options):
                            ui_comp.addItem(f"{i}: {self.features[feature]['options'][i]}", i)
                        ui_comp.setCurrentIndex(feature_index)
                        ui_comp.blockSignals(False)
                else:
                    ui_comp.setText(self._a3man.get_e_feature_str(feature))

    def get_device_count(self, ):
        ndevices = self._a3man.get_i_feature("DeviceCount")
        return ndevices

    def show_config_window(self):
        if self.config_window is None:
            self._populate_config_window()
            for feature in self.features.keys():
                if self.features[feature]['type'] != 'c' and \
                        self.features[feature]['b_implemented'] and \
                        ('b_readable' in self.features[feature].keys() and self.features[feature]['b_readable']) and \
                        ('system' not in self.features[feature].keys() or not self.features[feature]['system']):
                    self._a3man.register_feature_cb(
                        feature,
                        lambda feature_name: self.camera_prop_changed.emit([feature_name, ]))
                    pass

        self.config_window.show()


if __name__ == "__main__":
    from pprint import pprint

    app = QApplication([])

    andor_cam = AndorCameraMan(0)
    andor_cam.open()
    # pprint(andor_cam.features)
    andor_cam.show_config_window()
    QApplication.instance().exec_()
