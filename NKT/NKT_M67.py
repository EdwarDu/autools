from .NKTMan import NKTMan, nkt_logger
import numpy as np


class NKT_M67:
    """
    Class for Module type 67 SuperK SELECT (A203)
    """
    def __init__(self, nkt_man: NKTMan,
                 module_addr: int):
        self.nkt_man = nkt_man
        self.module_addr = module_addr

        # Verify
        assert(self.nkt_man.get_module_type(self.module_addr) == 0x67)

    def read_reg(self, reg_addr: int, dtype=None):
        return self.nkt_man.read_reg(self.module_addr, reg_addr, dtype)

    def write_reg(self, reg_addr: int, data):
        self.nkt_man.write_reg(self.module_addr, reg_addr, data)

    @property
    def serial_number(self):
        return self.read_reg(0x65).decode('ascii')

    @property
    def monitor1_readout(self):
        return self.read_reg(0x10, '<u2')[0]

    @property
    def monitor2_readout(self):
        return self.read_reg(0x11, '<u2')[0]

    @property
    def monitor1_gain(self):
        return self.read_reg(0x32, '<u1')[0]

    @monitor1_gain.setter
    def monitor1_gain(self, gain: int):
        """monitor gain can't be modified when it is in external feedback mode"""
        if 0 <= gain <= 7:
            self.write_reg(0x32, np.array([gain, ], dtype='<u1').tobytes())

    @property
    def monitor2_gain(self):
        return self.read_reg(0x33, '<u1')[0]

    @monitor2_gain.setter
    def monitor2_gain(self, gain: int):
        if 0 <= gain <= 7:
            self.write_reg(0x33, np.array([gain, ], dtype='<u1').tobytes())

    @property
    def rf_switch(self):
        return self.read_reg(0x34, '<u1')[0]

    @rf_switch.setter
    def rf_switch(self, sw: bool):
        """ RF power must be off """
        self.write_reg(0x34, b'\x00' if not sw else b'\x01')

    @property
    def monitor_switch(self):
        return self.read_reg(0x35, '<u1')[0]

    @monitor_switch.setter
    def monitor_switch(self, wh: int):
        if 0 <= wh <= 1:
            self.write_reg(0x35, b'\x00' if wh == 0 else b'\x01')

    @property
    def crystal1_min_wavelength(self):
        return self.read_reg(0x90, '<u4')[0]

    @property
    def crystal1_max_wavelength(self):
        return self.read_reg(0x91, '<u4')[0]

    @property
    def crystal2_min_wavelength(self):
        return self.read_reg(0xA0, '<u4')[0]

    @property
    def crystal2_max_wavelength(self):
        return self.read_reg(0xA1, '<u4')[0]

    @property
    def status(self):
        return self.read_reg(0x66, '<u2')[0]

    STATUS_BIT_INTERLOCK_OFF = (0x01 << 1)
    STATUS_BIT_INTERLOCK_LOOP_IN = (0x01 << 2)
    STATUS_BIT_INTERLOCK_LOOP_OUT = (0x01 << 3)
    STATUS_BIT_SUPPLY_VOLTAGE_LOW = (0x01 << 5)
    STATUS_BIT_MODULE_TEMP_OOR = (0x01 << 6)
    STATUS_BIT_SHUTTER_SENSOR1 = (0x01 << 8)
    STATUS_BIT_SHUTTER_SENSOR2 = (0x01 << 9)
    STATUS_BIT_NEW_CRYSTAL1_TEMP = (0x01 << 10)
    STATUS_BIT_NEW_CRYSTAL2_TEMP = (0x01 << 11)
    STATUS_BIT_ERROR_CODE_PRESENT = (0x01 << 15)

    @property
    def error_code(self):
        return self.read_reg(0x67, '<u1')[0]
