#distutils: language = c++
cimport rtc6_sdk as rtc6
from cpython.mem cimport PyMem_Malloc, PyMem_Free
from cpython.pycapsule cimport PyCapsule_New, PyCapsule_GetPointer
import numpy as np
import logging

_SPLIT_LOG = False

if _SPLIT_LOG:
    rtc6_logger = logging.getLogger("rtc6")
    rtc6_logger.setLevel(logging.DEBUG)
    rtc6_fh = logging.FileHandler("rtc6.log")
    rtc6_formatter = logging.Formatter('%(asctime)s [%(component)s] - %(levelname)s - %(message)s')
    rtc6_fh.setFormatter(rtc6_formatter)
    rtc6_logger.addHandler(rtc6_fh)

    rtc6_ch = logging.StreamHandler()
    rtc6_ch.setFormatter(rtc6_formatter)
    rtc6_logger.addHandler(rtc6_ch)
else:
    rtc6_logger = logging.getLogger("autools_setup_main")


cdef class RTC6Man:
  """
  Cython class for wrapping API calls to RTC6_SDK
  [WARNING]:not all features will be implemented here
  """

  def __cinit__(self):
    """
    TODO: device initialization.
    """
    rtc6.init_rtc6_dll()
    rtc6.set_rtc6_mode()

  def __dealloc__(self):
    """
    TODO: device finalise/close procedure
    """
    rtc6.free_rtc6_dll()


