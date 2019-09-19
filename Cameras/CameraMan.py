#!/usr/bin/python3

import numpy as np
from PyQt5.QtCore import QObject


class CameraMan(QObject):
    """
    Helper class for manage cameras:
    1. OpenCV compatible cameras
    2. Andor Camera
    """
    def __init__(self, cam_type: str):
        super().__init__()
        self.cam_type = cam_type

    def __del__(self):
        pass

    def open(self):
        pass

    def is_open(self):
        pass

    def close(self):
        pass

    def get_frame_size(self):
        pass

    def grab_frame(self, n_channel_index: int):
        pass

    def show_config_window(self):
        pass

    @staticmethod
    def normal_frame(frame, b_autorange=False):
        if not b_autorange:
            if frame.dtype == 'float':
                min_orig = 0
                max_orig = 1
            else:
                iinfo_orig = np.iinfo(frame.dtype)
                min_orig = iinfo_orig.min
                max_orig = iinfo_orig.max
        else:
            min_orig = np.min(frame)
            max_orig = np.max(frame)

        return (frame.astype('float') - min_orig) / (max_orig - min_orig) if max_orig != min_orig else \
            np.zeros(frame.shape, dtype='float')

