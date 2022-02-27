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
        },
        "load_correction_file": {
            1: "File error (file corrupt or incomplete)",
            2: "Memory error (RTC6 DLL-internal, Windows system memory)",
            3: "File-open error (empty string submitted for Name parameter, file not found, etc)",
            4: "DSP memory error",
            5: "PCI download error (RTC6 board driver error), Ethernet download error",
            8: "RTC6 board driver not found (get_last_error return code RTC6_ACCESS_DENIED)",
            10: "Parameter error (incorrect No.)",
            11: "Access error (check doc)",
            12: "Warning: 3D correction table or Dim==3 selected, but the Option 3D is not enabled, will continue as 2D system",
            13: "Busy error: no download, board is BUSY or INTERNAL-BUSY",
            14: "PCI upload error (RTC6 board driver error, only applicable for download verification",
            15: "Verify error (only applicable for download verification)"
        }
    }

    # TODO: add get_last_error code
    #RTC6_NO_PCIE_CARD_FOUND

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

        rtc6.reset_error(-1)
        rtc6.config_list(4000, 4000)

        err = rtc6.load_correction_file(os.path.join(cfg_path, "Cor_1to1.ct5").encode('utf-8'), 
                                        1, # correction table
                                        2) # use 2D only
        if err == 0:
            rtc6_logger.info(f"Load correction file OKAY", extra={"component": "rtc6"})
        elif err in RTC6Man.ERR_CODES["load_correction_file"].keys():
            if err != 12:
                rtc6_logger.error(f"Load correction file Failed: {RTC6Man.ERR_CODES['load_correction_file'][err]}",
                              extra={"component": "rtc6"})
                if err == 11:
                    # TODO: get_last_error -> detail
                    # last_err = rtc6.get_last_error()
                    pass
                raise RTC6DevError(err)
            else:
                rtc6_logger.warning(f"Load correction file: {RTC6Man.ERR_CODES['load_correction_file'][err]}",
                              extra={"component": "rtc6"})
        else:
            rtc6_logger.error(f"Load correction file Failed: unknown error code {err}", extra={"component": "rtc6"})
            raise RTC6DevError(err)

    
    def goto_xy(self, x, y):
        x = min(max(-524288, x), 524287)
        y = min(max(-524288, y), 524287)
        rtc6.goto_xy(x, y)


    def __dealloc__(self):
        """
        TODO: device finalise/close procedure
        """
        rtc6.free_rtc6_dll()

