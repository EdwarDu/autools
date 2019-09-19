#!/usr/bin/python3

import cv2
from PyQt5.QtWidgets import QWidget
from .CameraMan import CameraMan
from .CVCameraConfig_ui import Ui_Form_CVCameraConfig
from PyQt5.QtGui import QIntValidator


class CVCameraMan(CameraMan):
    """
    Helper class for manage cameras:
    1. OpenCV compatible cameras
    2. Andor Camera
    """

    CAP_PROP_FRAME_WIDTH = cv2.CAP_PROP_FRAME_WIDTH
    CAP_PROP_FRAME_HEIGHT = cv2.CAP_PROP_FRAME_HEIGHT
    CAP_PROP_BRIGHTNESS = cv2.CAP_PROP_BRIGHTNESS
    CAP_PROP_CONTRAST = cv2.CAP_PROP_CONTRAST
    CAP_PROP_SATURATION = cv2.CAP_PROP_SATURATION
    CAP_PROP_HUE = cv2.CAP_PROP_HUE
    CAP_PROP_GAIN = cv2.CAP_PROP_GAIN
    CAP_PROP_EXPOSURE = cv2.CAP_PROP_EXPOSURE
    CAP_PROP_MONOCHROME = cv2.CAP_PROP_MONOCHROME
    CAP_PROP_SHARPNESS = cv2.CAP_PROP_SHARPNESS
    CAP_PROP_AUTO_EXPOSURE = cv2.CAP_PROP_AUTO_EXPOSURE
    CAP_PROP_GAMMA = cv2.CAP_PROP_GAMMA
    CAP_PROP_TEMPERATURE = cv2.CAP_PROP_TEMPERATURE
    CAP_PROP_ZOOM = cv2.CAP_PROP_ZOOM
    CAP_PROP_FOCUS = cv2.CAP_PROP_FOCUS
    CAP_PROP_AUTOFOCUS = cv2.CAP_PROP_AUTOFOCUS
    CAP_PROP_AUTO_WB = cv2.CAP_PROP_AUTO_WB
    CAP_PROP_WB_TEMPERATURE = cv2.CAP_PROP_WB_TEMPERATURE

    def __init__(self, cv_index: int):
        super().__init__(cam_type="cv")
        self.cv_index = cv_index
        self.cv_cap = cv2.VideoCapture(self.cv_index)
        if not self.cv_cap.isOpened():
            raise Exception(f"Failed to open camera")
        else:
            self.frame_width, self.frame_height, self.frame_channels = 0, 0, 0
            self.get_frame_size_force()
            self.cv_cap.release()
            self.cv_cap = None

        self.cam_config_window = None

    def show_config_window(self):
        if self.cam_config_window is None:
            self.cam_config_window = CVCameraConfigWindow(self)
        self.cam_config_window.show()

    def open(self):
        self.cv_cap = cv2.VideoCapture(self.cv_index)
        return self.cv_cap.isOpened()

    def is_open(self):
        if self.cv_cap is None or not self.cv_cap.isOpened():
            return False
        else:
            return True

    def close(self):
        if self.cv_cap is not None:
            self.cv_cap.release()
            self.cv_cap = None

    def get_frame_size_force(self):
        ret, frame = self.cv_cap.read()
        if not ret:
            # FIXME: not a good way
            return
        else:
            self.frame_width = frame.shape[1]
            self.frame_height = frame.shape[0]
            if len(frame.shape) == 3:
                self.frame_channels = frame.shape[2]
            else:
                self.frame_channels = 1

    def get_frame_size(self, b_force: bool = False):
        if b_force:
            self.get_frame_size_force()
        return self.frame_width, self.frame_height, self.frame_channels

    def get_cam_property(self, propid):
        if self.cv_cap is not None:
            value = self.cv_cap.get(propid)
            if value == -1:
                return None
            else:
                return value
        else:
            return None

    def set_cam_proerty(self, propid, value):
        if self.cv_cap is not None:
            self.cv_cap.set(propid, value)
            return self.cv_cap.get(propid)
        else:
            return None

    def set_frame_size(self, frame_width, frame_height):
        self.set_cam_proerty(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
        self.set_cam_proerty(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
        return self.get_frame_size(b_force=True)

    def grab_frame(self, n_channel_index: int):
        ret, frame = self.cv_cap.read()
        if ret:
            frame_norm = CameraMan.normal_frame(frame, b_autorange=False)
            if self.frame_channels == 1:
                return frame
            elif self.frame_channels == 3 and n_channel_index < 3:
                return frame[:, :, n_channel_index]
            else:  # n_channel_index > 3
                frame_blue = frame_norm[:, :, 0]
                frame_green = frame_norm[:, :, 1]
                frame_red = frame_norm[:, :, 2]
                frame_gray = 0.3 * frame_red + 0.59 * frame_green + 0.11 * frame_blue
                # frame_gray = (frame_red + frame_green + frame_blue) / 3
                return frame_gray
        else:
            return None

    @staticmethod
    def get_all_cams():
        # First get all the CV2 supported cam
        cv_index = 0
        cam_lst = []
        while cv_index < 4:
            try:
                cam_man = CVCameraMan(cv_index=cv_index)
                cam_lst.append(cam_man)
            except:
                # Ignored
                pass

            cv_index += 1

        return cam_lst


class CVCameraConfigWindow(Ui_Form_CVCameraConfig):
    """
    Popup window for change CV Camera settings
    """

    def __init__(self, cam_man: CVCameraMan):
        self.window = QWidget()
        Ui_Form_CVCameraConfig.__init__(self)
        self.setupUi(self.window)

        self.cam_man = cam_man
        self.lineEdit_FrameHeight.setValidator(QIntValidator(240, 4000))
        self.lineEdit_FrameWidth.setValidator(QIntValidator(320, 4000))

        # Load init values
        value = self.cam_man.get_cam_property(CVCameraMan.CAP_PROP_FRAME_WIDTH)
        if value is None:
            self.lineEdit_FrameWidth.setDisabled(True)
            self.pushButton_SetFrameSize.setDisabled(True)
        else:
            self.lineEdit_FrameWidth.setText(f"{int(value):d}")

        value = self.cam_man.get_cam_property(CVCameraMan.CAP_PROP_FRAME_HEIGHT)
        if value is None:
            self.lineEdit_FrameHeight.setDisabled(True)
            self.pushButton_SetFrameSize.setDisabled(True)
        else:
            self.lineEdit_FrameHeight.setText(f"{int(value):d}")

        self.pushButton_SetFrameSize.clicked.connect(self.set_framesize_clicked)

        value = self.cam_man.get_cam_property(CVCameraMan.CAP_PROP_BRIGHTNESS)
        if value is None:
            self.doubleSpinBox_Brightness.setDisabled(True)
        else:
            self.doubleSpinBox_Brightness.setValue(value)

        value = self.cam_man.get_cam_property(CVCameraMan.CAP_PROP_CONTRAST)
        if value is None:
            self.doubleSpinBox_Contrast.setDisabled(True)
        else:
            self.doubleSpinBox_Contrast.setValue(value)

        value = self.cam_man.get_cam_property(CVCameraMan.CAP_PROP_SATURATION)
        if value is None:
            self.doubleSpinBox_Saturation.setDisabled(True)
        else:
            self.doubleSpinBox_Saturation.setValue(value)

        value = self.cam_man.get_cam_property(CVCameraMan.CAP_PROP_HUE)
        if value is None:
            self.doubleSpinBox_Hue.setDisabled(True)
        else:
            self.doubleSpinBox_Hue.setValue(value)

        value = self.cam_man.get_cam_property(CVCameraMan.CAP_PROP_GAIN)
        if value is None:
            self.doubleSpinBox_Gain.setDisabled(True)
        else:
            self.doubleSpinBox_Gain.setValue(value)

        value = self.cam_man.get_cam_property(CVCameraMan.CAP_PROP_EXPOSURE)
        if value is None:
            self.doubleSpinBox_Exposure.setDisabled(True)
        else:
            self.doubleSpinBox_Exposure.setValue(value)

        value = self.cam_man.get_cam_property(CVCameraMan.CAP_PROP_AUTO_EXPOSURE)
        if value is None:
            self.doubleSpinBox_AutoExposure.setDisabled(True)
        else:
            self.doubleSpinBox_AutoExposure.setValue(value)

        value = self.cam_man.get_cam_property(CVCameraMan.CAP_PROP_MONOCHROME)
        if value is None:
            self.checkBox_Monochrome.setDisabled(True)
        else:
            self.checkBox_Monochrome.setChecked(value == 1.0)

        value = self.cam_man.get_cam_property(CVCameraMan.CAP_PROP_SHARPNESS)
        if value is None:
            self.doubleSpinBox_Sharpness.setDisabled(True)
        else:
            self.doubleSpinBox_Sharpness.setValue(value)

        value = self.cam_man.get_cam_property(CVCameraMan.CAP_PROP_GAMMA)
        if value is None:
            self.doubleSpinBox_Gamma.setDisabled(True)
        else:
            self.doubleSpinBox_Gamma.setValue(value)

        value = self.cam_man.get_cam_property(CVCameraMan.CAP_PROP_TEMPERATURE)
        if value is None:
            self.checkBox_WBAuto.setChecked(True)
            self.checkBox_WBAuto.setDisabled(True)
            self.doubleSpinBox_Temperature.setDisabled(True)
        else:
            self.doubleSpinBox_Temperature.setValue(value)

        value = self.cam_man.get_cam_property(CVCameraMan.CAP_PROP_ZOOM)
        if value is None:
            self.doubleSpinBox_Zoom.setDisabled(True)
        else:
            self.doubleSpinBox_Zoom.setValue(value)

        value = self.cam_man.get_cam_property(CVCameraMan.CAP_PROP_FOCUS)
        if value is None:
            self.checkBox_FocusAuto.setChecked(True)
            self.checkBox_FocusAuto.setDisabled(True)
            self.doubleSpinBox_Focus.setDisabled(True)
        else:
            self.doubleSpinBox_Focus.setValue(value)

        self.doubleSpinBox_Brightness.valueChanged.connect(
            lambda a: self.config_value_changed(self.doubleSpinBox_Brightness, CVCameraMan.CAP_PROP_BRIGHTNESS, a))
        self.doubleSpinBox_Contrast.valueChanged.connect(
            lambda a: self.config_value_changed(self.doubleSpinBox_Contrast, CVCameraMan.CAP_PROP_CONTRAST, a))
        self.doubleSpinBox_Saturation.valueChanged.connect(
            lambda a: self.config_value_changed(self.doubleSpinBox_Saturation, CVCameraMan.CAP_PROP_SATURATION, a))
        self.doubleSpinBox_Hue.valueChanged.connect(
            lambda a: self.config_value_changed(self.doubleSpinBox_Hue, CVCameraMan.CAP_PROP_HUE, a))
        self.doubleSpinBox_Gain.valueChanged.connect(
            lambda a: self.config_value_changed(self.doubleSpinBox_Gain, CVCameraMan.CAP_PROP_GAIN, a))
        self.doubleSpinBox_Exposure.valueChanged.connect(
            lambda a: self.config_value_changed(self.doubleSpinBox_Exposure, CVCameraMan.CAP_PROP_EXPOSURE, a))
        self.doubleSpinBox_AutoExposure.valueChanged.connect(
            lambda a: self.config_value_changed(self.doubleSpinBox_AutoExposure, CVCameraMan.CAP_PROP_AUTO_EXPOSURE, a))
        self.doubleSpinBox_Sharpness.valueChanged.connect(
            lambda a: self.config_value_changed(self.doubleSpinBox_Sharpness, CVCameraMan.CAP_PROP_SHARPNESS, a))
        self.doubleSpinBox_Gamma.valueChanged.connect(
            lambda a: self.config_value_changed(self.doubleSpinBox_Gamma, CVCameraMan.CAP_PROP_GAMMA, a))
        self.doubleSpinBox_Temperature.valueChanged.connect(
            lambda a: self.config_value_changed(self.doubleSpinBox_Temperature, CVCameraMan.CAP_PROP_TEMPERATURE, a))
        self.doubleSpinBox_Zoom.valueChanged.connect(
            lambda a: self.config_value_changed(self.doubleSpinBox_Zoom, CVCameraMan.CAP_PROP_ZOOM, a))
        self.doubleSpinBox_Focus.valueChanged.connect(
            lambda a: self.config_value_changed(self.doubleSpinBox_Focus, CVCameraMan.CAP_PROP_FOCUS, a))

        self.checkBox_Monochrome.stateChanged.connect(
            lambda b: self.config_bvalue_changed(self.checkBox_Monochrome, CVCameraMan.CAP_PROP_MONOCHROME, b))
        self.checkBox_FocusAuto.stateChanged.connect(
            lambda b: self.config_bvalue_changed(self.checkBox_FocusAuto, CVCameraMan.CAP_PROP_AUTOFOCUS, b))
        self.checkBox_WBAuto.stateChanged.connect(
            lambda b: self.config_bvalue_changed(self.checkBox_WBAuto, CVCameraMan.CAP_PROP_AUTO_WB, b))

    def set_framesize_clicked(self):
        width = self.cam_man.set_cam_proerty(CVCameraMan.CAP_PROP_FRAME_WIDTH,
                                             int(self.lineEdit_FrameWidth.text()))
        height = self.cam_man.set_cam_proerty(CVCameraMan.CAP_PROP_FRAME_HEIGHT,
                                              int(self.lineEdit_FrameHeight.text()))
        self.lineEdit_FrameWidth.setText(f"{int(width)}")
        self.lineEdit_FrameHeight.setText(f"{int(height)}")

    def config_value_changed(self, ctrl, propid, value):
        value_actual = self.cam_man.set_cam_proerty(propid, value)
        if value != value_actual:
            ctrl.setValue(value_actual)

    def config_bvalue_changed(self, ctrl, propid, value):
        value_actual = self.cam_man.set_cam_proerty(propid, 1.0 if value else 0.0)
        if value_actual == 1.0:
            ctrl.setChecked(True)
        else:
            ctrl.setChecked(False)

    def show(self):
        self.window.show()

    def close(self):
        self.window.hide()

