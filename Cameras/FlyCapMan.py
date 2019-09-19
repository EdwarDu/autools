#!/usr/bin/python3

import numpy as np
import re
from .CameraMan import CameraMan
import PyCapture2


class FlyCapMan(CameraMan):
    def __init__(self, cam_index: int = None):
        super().__init__(cam_type='flycap')
        self.bus = PyCapture2.BusManager()
        self.cam_if = PyCapture2.Camera()
        self._cam_index = cam_index
        self.uid = self.bus.getCameraFromIndex(self._cam_index) \
            if self._cam_index is not None else None
        self._frame_width = 0
        self._frame_height = 0
        self._frame_channels = 0

    def get_dev_id(self):
        return self.uid

    def open(self):
        if self.uid is None:
            self.uid = self.bus.getCameraFromIndex(self._cam_index)
        self.cam_if.connect(self.uid)
        self.cam_if.startCapture()

    def is_open(self):
        return self.cam_if.isConnected

    def close(self):
        self.cam_if.stopCapture()
        self.cam_if.disconnect()

    # def get_frame_size(self):
    #     cam_info = self.cam_if.getCameraInfo()
    #     width, height = [int(x) for x in re.split("[xX ]", cam_info.sensorResolution.decode('ascii')) if x != ""]
    #     if cam_info.isColorCamera:
    #         self._frame_channels = 3
    #     else:
    #         self._frame_channels = 1
    #     self._frame_width = width
    #     self._frame_height = height
    #     return self._frame_width, self._frame_height, self._frame_channels

    def get_frame_size(self, b_force = True):
        if b_force:
            cam_info = self.cam_if.getCameraInfo()
            self._frame_channels = 3 if cam_info.isColorCamera else 1
            try:
                img = self.cam_if.retrieveBuffer()
                self._frame_width = img.getCols()
                self._frame_height = img.getRows()
            except PyCapture2.Fc2error as e:
                pass 

        return self._frame_width, self._frame_height, self._frame_channels 

    def grab_frame(self, n_channel_index: int):
        try:
            img = self.cam_if.retrieveBuffer()
        except PyCapture2.Fc2error as e:
            return None

        img1 = img.convert(PyCapture2.PIXEL_FORMAT.BGR)
        frame = np.array(img1.getData(), dtype="uint8").reshape((img1.getRows(), img1.getCols(), self._frame_channels))
        if self._frame_channels == 1:
            return frame
        elif self._frame_channels == 3 and n_channel_index < 3:
            return frame[:, :, n_channel_index]
        else:  # n_channel_index > 3
            frame_blue = frame[:, :, 0]
            frame_green = frame[:, :, 1]
            frame_red = frame[:, :, 2]
            frame_gray = 0.3 * frame_red + 0.59 * frame_green + 0.11 * frame_blue
            # frame_gray = (frame_red + frame_green + frame_blue) / 3
            return frame_gray

    def show_config_window(self):
        #FIXME: There is no configuration window
        pass

    @staticmethod
    def get_all_cams():
        bus = PyCapture2.BusManager()
        num_cams = bus.getNumOfCameras()
        all_cams = []
        for i in range(0, num_cams):
            all_cams.append(FlyCapMan(i))

        return all_cams

