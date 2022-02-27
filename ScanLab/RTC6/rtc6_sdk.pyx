#distutils: language = c++
cimport rtc6_sdk as rtc6
from cpython.mem cimport PyMem_Malloc, PyMem_Free
from cpython.pycapsule cimport PyCapsule_New, PyCapsule_GetPointer
import numpy as np
import logging
import os

#[FIXME]: For testing now, use split log
_SPLIT_LOG = True

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

class RTC6DevError(Exception):
    pass

cdef class RTC6Man:
    """
    Cython class for wrapping API calls to RTC6_SDK
    [WARNING]:not all features will be implemented here
    """

    ERR_CODES = {
        "load_program_file": {
            2: "The board is not running.", # if a renewed call does not bring success, then a power cycle is necessary
            3: "RTC6DAT.dat file or RTC6RBF.rbf file not found",
            5: "Not enough Windows memory",
            6: "Access error: the board is reserved for another user program",
            7: "Version error: RTC6 DLL version, RTC version (firmware file RTC6RBF.rbf) and OUT version (DSP program file RTC6OUT.out) are incompatible with each other",
            8: "RTC6 board driver not found",
            9: "Loading of RTC6OUT.out or RTC6ETH.out failed or has incorrect format or other error",
            11: "Firmware error: loading of RTC6RBF.rbf file failed",
            12: "Error opening/reading file RTC6DAT.dat",
            14: "DSP memory error (external)",
            16: "Verify memory error",
            17: "Externet error",
            18: "NAND memory error (Only RTC6 Ethernet Board)"
        }
    }

    def __cinit__(self, cfg_path=os.path.dirname(os.path.abspath(__file__))):
        """
        TODO: device initialization.
        """
        err = rtc6.init_rtc6_dll()
        if err == 0:
            rtc6_logger.info("RTC6 DLL Init OKAY", extra={"component": "rtc6"})
        else:
            rtc6_logger.info(f"RTC6 DLL Init Failed: {hex(err)}", extra={"component": "rtc6"})

        rtc6.set_rtc6_mode()

        rtc6_logger.info(f"Board reset with config dir: {cfg_path}", extra={"component": "rtc6"})
        if not os.path.exists(cfg_path) or \
            not os.path.exists(os.path.join(cfg_path, "RTC6OUT.out")) or \
            not os.path.exists(os.path.join(cfg_path, "RTC6RBF.rbf")) or \
            not os.path.exists(os.path.join(cfg_path, "RTC6DAT.dat")):
            rtc6_logger.error(f"At least one of the RTC6OUT.out, RTC6RBF.rbf and RTC6DAT.dat "
                              f"does not exist in {cfg_path}", extra={"component": "rtc6"})
            raise FileNotFoundError()

        err = rtc6.load_program_file(cfg_path.encode('utf-8'))
        if err == 0:
            rtc6_logger.info(f"Device reset OKAY", extra={"component": "rtc6"})
        elif err in RTC6Man.ERR_CODES["load_program_files"].keys():
            rtc6_logger.error(f"Device reset Failed: {RTC6Man.ERR_CODES['load_program_files'][err]}",
                              extra={"component": "rtc6"})
            raise RTC6DevError(err)
        else:
            rtc6_logger.error(f"Device reset Failed: unknown error code {err}", extra={"component": "rtc6"})
            raise RTC6DevError(err)

    def __dealloc__(self):
        """
        TODO: device finalise/close procedure
        """
        rtc6.free_rtc6_dll()


