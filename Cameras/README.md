# Simple capture API for Cameras
Main APIs as in **CameraMan.py**:
```python
def open(self):
def is_open(self):
def close(self):
def get_frame_size(self):
def grab_frame(self, n_channel_index: int):
def show_config_window(self):
```

## OpenCV (CVCameraMan.py)
Any camera supported by OpenCV, apparently it is possible to custom build OpenCV to support more cameras.

A lot of native features is not accessible through the implemented configuration window, and may be erroneous.

## FlyCapture SDK (FlyCapMan.py)
Any camera supported by FlyCapture SDK (Windows / Linux), only wrapper. PyCap2 packages has to be installed.
Currently max Python3.6 is supported.

** NO CONFIGURATION WINDOW ** (TODO)

## Andor (AndorCameraMan.py)
Neon CMOS camera from Andor using Andor3SDK [check Python3 Binding](../AndorSDK3/README.md)

Configuration window is automatically populated (TODO)
