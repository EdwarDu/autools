# vim:  set syntax=python foldmethod=indent:
#distutils: language = c++
from libcpp cimport bool
from rtc6_sdk cimport *
from cpython.mem cimport PyMem_Malloc, PyMem_Free
from cpython.pycapsule cimport PyCapsule_New, PyCapsule_GetPointer
import numpy as np
import logging
import os
from typing import Union

#[FIXME]: For testing now, use split log, this is not good for packaging
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

cdef class RTC6Helper:
    """
    Cython class for wrapping API calls to RTC6_SDK
    [WARNING]:not all features will be implemented here
    [WARNING]:FIXME: This may need to be a Singleton, client should handle that for now
    """

    ERR_CODES = {
        "load_program_file": {
            # if a renewed call does not bring success, then a power cycle is necessary
            2: "The board is not running.",
            3: "RTC6DAT.dat file or RTC6RBF.rbf file not found",
            5: "Not enough Windows memory",
            6: "Access error: the board is reserved for another user program",
            7: "Version error: RTC6 DLL version, RTC version (firmware file RTC6RBF.rbf) and "
                "OUT version (DSP program file RTC6OUT.out) are incompatible with each other",
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
            12: "Warning: 3D correction table or Dim==3 selected, but the Option 3D is not enabled, "
                "will continue as 2D system",
            13: "Busy error: no download, board is BUSY or INTERNAL-BUSY",
            14: "PCI upload error (RTC6 board driver error, only applicable for download verification",
            15: "Verify error (only applicable for download verification)"
        },
        "acc_error":{
            0: "No RTC6 PCIe Board found",
            1: "Access denied (e.g. resevered by another program)",
            2: "Command not forwarded (internal board driver error/PCI error)",
            3: "No response from board (likely no program has been loaded onto the RTC6)",
            4: "Invalid parameter",
            5: "List processing is (not) active",
            6: "List command rejected, invalid input pointer",
            7: "List command was converted to a list_nop",
            8: "Version error: .dll, .rbf and .out file version are not compatible",
            9: "Verify error",
            10: "Type error: e.g. eth command sent to a PCIe board",
            11: "Out of memory",
            12: "Download error",
            13: "General Ethernet error",
            15: "Unsupported Windows version",
            16: "Error reading PCI configuration register"
        }
    }

    RTC6_NO_PCIE_CARD_FOUND = 0
    RTC6_ACCESS_DENIED = 1
    RTC6_SEND_ERROR = 2
    RTC6_TIMEOUT = 3
    RTC6_PARAM_ERROR = 4
    RTC6_BUSY = 5
    RTC6_REJCTED = 6
    RTC6_IGNORED = 7
    RTC6_VERSION_MISMATCH = 8
    RTC6_VERIFY_ERROR = 9
    RTC6_TYPE_REJECTED = 10
    RTC6_OUT_OF_MEMORY = 11
    RTC6_FLASH_ERROR = 12
    RTC6_ETH_ERROR = 13
    RTC6_WIN_VER_ERROR = 15
    RTC6_CONFIG_ERROR = 16

    cdef int  cardno
    cdef bool do_init
    cdef UINT board_count

    def __cinit__(self, do_init: bool, cardno: int = -1):
        """
        TODO: device initialization.
        """
        self.do_init = do_init
        self.cardno = cardno
        if self.do_init:
            err = _init_rtc6_dll(self.cardno)
            if err == 0:
                rtc6_logger.info("RTC6 DLL Init OKAY", extra={"component": "rtc6"})
            else:
                rtc6_logger.info(f"RTC6 DLL Init Failed: {hex(err)}", extra={"component": "rtc6"})

            _set_rtc6_mode(self.cardno)

        self.board_count = _rtc6_count_cards(self.cardno)
        if self.cardno > 0:
            if self.cardno > self.board_count:
                rtc6_logger.error(f"{cardno} is larger than number of RTC6 board count {self.board_count}")
                raise ValueError(f"{cardno} is larger than number of RTC6 board count {self.board_count}")

    def load_program_file(self, cfg_path: Union[str, None] = None):
        if cfg_path is None:
            cfg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
        rtc6_logger.info(f"Board reset with config dir: {cfg_path}", extra={"component": "rtc6"})
        if not os.path.exists(cfg_path) or \
            not os.path.exists(os.path.join(cfg_path, "RTC6OUT.out")) or \
            not os.path.exists(os.path.join(cfg_path, "RTC6RBF.rbf")) or \
            not os.path.exists(os.path.join(cfg_path, "RTC6DAT.dat")):
            rtc6_logger.error(f"At least one of the RTC6OUT.out, RTC6RBF.rbf and RTC6DAT.dat "
                              f"does not exist in {cfg_path}", extra={"component": "rtc6"})
            raise FileNotFoundError()

        err = _load_program_file(self.cardno, cfg_path.encode('utf-8'))

        if err == 0:
            rtc6_logger.info(f"Device reset OKAY", extra={"component": "rtc6"})
        else:
            if err == 2:
                err = _load_program_file(self.cardno, cfg_path.encode('utf-8'))

            if err == 0:
                rtc6_logger.info(f"Device reset OKAY", extra={"component": "rtc6"})
            elif err in RTC6Helper.ERR_CODES["load_program_file"].keys():
                rtc6_logger.error(f"Device reset Failed: {RTC6Helper.ERR_CODES['load_program_file'][err]}",
                                  extra={"component": "rtc6"})
                if err == 2:
                    rtc6_logger.error(f"Power cycle required", extra={"component": "rtc6"})
                raise RTC6DevError(err)
            else:
                rtc6_logger.error(f"Device reset Failed: unknown error code {err}", extra={"component": "rtc6"})
                raise RTC6DevError(err)

        _reset_error(self.cardno, -1)

    def config_list(self, mem1: int, mem2: int):
        # 8,388,608 (2^23) storage positions
        # mem1 -> list1, mem2 -> list2., rest to protected list list3
        if mem1 <= -1 or mem1 > 1<<23:
            rtc6_logger.warning(f"Mem1 is corrected to 2^23 from {mem1}, "
                                f"which means Mem1=2^23, Mem2=0, List3=0", extra={"component": "rtc6"})
            mem1 = -1
            actual_mem1 = 1<<23
            actual_mem2 = 0
        else:
            if mem1 == 0:
                rtc6_logger.warning(f"Mem1 is corrected to 1 from {mem1}", extra={"component": "rtc6"})
                actual_mem1 = 1
            else:
                actual_mem1 = mem1
            if mem2 <= -1 or mem2 > (1<<23) - actual_mem1:
                actual_mem2 = (1<<23) - actual_mem1
                rtc6_logger.warning(f"Mem1 is corrected to {actual_mem1} from {mem2}",
                                    extra={"component": "rtc6"})
            else:
                actual_mem2 = mem2
        
        rtc6_logger.debug(f"setting mem1={actual_mem1}, mem2={actual_mem2}, "
                          f"list3={(1<<23)-actual_mem1-actual_mem2}", 
                          extra={"component": "rtc6"})
        
        _config_list(self.cardno, mem1, mem2)
        
    def load_correction_file(self, cor_file: Union[None, str], table_no: int, dim: int):
        if cor_file is None:
            cor_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "Cor_1to1.ct5")
        
        if not os.path.exists(cor_file):
            rtc6_logger.error(f"Correction file {cor_file} does not exist", extra={"component": "rtc6"})
            raise IOError()
        if not 1 <= table_no <= 8:
            rtc6_logger.error(f"Table no. should be [1,8]", extra={"component": "rtc6"})
            raise ValueError()
        if dim not in (2, 3):
            rtc6_logger.error(f"Dim should be 2 or 3", extra={"component": "rtc6"})
            raise ValueError()

        rtc6_logger.debug(f"Loading correction file {cor_file} to table {table_no}, dim={dim}", 
                          extra={"component": "rtc6"})

        cor_file_c = cor_file.encode('utf-8')

        err = _load_correction_file(self.cardno, cor_file_c, table_no, dim)
        if err == 0:
            rtc6_logger.info(f"Load correction file OKAY", extra={"component": "rtc6"})
        elif err in RTC6Helper.ERR_CODES["load_correction_file"].keys():
            if err != 12:
                rtc6_logger.error(f"Load correction file Failed: {RTC6Helper.ERR_CODES['load_correction_file'][err]}",
                              extra={"component": "rtc6"})
                if err == 11:
                    last_err = _get_last_error(self.cardno)
                    if RTC6Helper.has_error(last_err, RTC6Helper.RTC6_VERSION_MISMATCH):
                        rtc6_logger.error(f"{RTC6Helper.ERR_CODES['acc_err'][RTC6Helper.RTC6_VERSION_MISMATCH]}", extra={"component": "rtc6"})
                    elif RTC6Helper.has_error(last_err, RTC6Helper.RTC6_ACCESS_DENIED):
                        rtc6_logger.error(f"{RTC6Helper.ERR_CODES['acc_err'][RTC6Helper.RTC6_ACCESS_DENIED]}", extra={"component": "rtc6"})
                    else:
                        rtc6_logger.error(f"Unknown last error {hex(last_err)}")
                raise RTC6DevError(err)
            else:
                rtc6_logger.warning(f"Load correction file: {RTC6Helper.ERR_CODES['load_correction_file'][err]}",
                              extra={"component": "rtc6"})
        else:
            rtc6_logger.error(f"Load correction file Failed: unknown error code {err}", extra={"component": "rtc6"})
            raise RTC6DevError(err)

    @staticmethod
    def has_error(error_code:int, bit_index: int):
        return (error_code & (1<<bit_index)) != 0
    
    def goto_xy(self, x: int, y: int):
        x1 = min(max(-524288, x), 524287)
        y1 = min(max(-524288, y), 524287)
        if x != x1 or y != y1:
            rtc6_logger.warning(f"x or y is out of range [-524288, 524287], clipped", extra={"component": "rtc6"})
        rtc6_logger.debug(f"Going to ({x1},{y1})", extra={"component": "rtc6"})    
        _goto_xy(self.cardno, x1, y1)

    def get_error(self):
        return _get_error(self.cardno)

    def get_last_error(self):
        return _get_last_error(self.cardno)

    def set_laser(self, b_enable: bool):
        return _enable_laser(self.cardno) if b_enable else _disable_laser(self.cardno)
        
    def set_laser_sig(self, b_enable: bool):
        return _laser_signal_on(self.cardno) if b_enable else _laser_signal_off(self.cardno)

    def set_zoom(self, zoom: int):
        return _set_zoom(self.cardno, zoom)

    def __dealloc__(self):
        """
        TODO: device finalise/close procedure
        """
        if self.do_init:
            _free_rtc6_dll(self.cardno)
