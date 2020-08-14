from .NKTMan import NKTMan, nkt_logger
import numpy as np


class NKT_M66:
    """
    Class for Module type 66 RF Driver (A901) for SuperK SELECT (A203)
    """
    def __init__(self, nkt_man: NKTMan,
                 module_addr: int):
        self.nkt_man = nkt_man
        self.module_addr = module_addr

        # Verify
        assert(self.nkt_man.get_module_type(self.module_addr) == 0x66)

    def read_reg(self, reg_addr: int, dtype=None):
        return self.nkt_man.read_reg(self.module_addr, reg_addr, dtype)

    def write_reg(self, reg_addr: int, data):
        self.nkt_man.write_reg(self.module_addr, reg_addr, data)

    @property
    def serial_number(self):
        return self.read_reg(0x65).decode('ascii')

    @property
    def rf_power(self):
        return self.read_reg(0x30, '<u1')[0]

    @rf_power.setter
    def rf_power(self, b_on: bool):
        self.write_reg(0x30, b'\x01' if b_on else b'\x00')

    @property
    def setup_bits(self):
        return self.read_reg(0x31, '<u1')[0]

    @setup_bits.setter
    def setup_bits(self, s_bits: int):
        self.write_reg(0x31, np.array([s_bits, ], dtype='<u1').tobytes())

    SETUP_BIT_TEMPERATURE_COMPENSATION = (0x01 << 0)
    SETUP_BIT_OPTIMAL_POWER_TABLE = (0x01 << 1)
    SETUP_BIT_BLANKING_LEVEL = (0x01 << 2)

    def setup_use_temperature_compensation(self, b_use: bool):
        curr_setup = self.setup_bits
        if b_use:
            curr_setup = curr_setup | NKT_M66.SETUP_BIT_TEMPERATURE_COMPENSATION
        else:
            curr_setup = curr_setup & (~ NKT_M66.SETUP_BIT_TEMPERATURE_COMPENSATION)
        self.setup_bits = curr_setup

    def setup_use_optimal_power(self, b_use: bool):
        curr_setup = self.setup_bits
        if b_use:
            curr_setup = curr_setup | NKT_M66.SETUP_BIT_OPTIMAL_POWER_TABLE
        else:
            curr_setup = curr_setup & (~ NKT_M66.SETUP_BIT_OPTIMAL_POWER_TABLE)
        self.setup_bits = curr_setup

    def setup_blanking_level(self, b_high: bool):
        curr_setup = self.setup_bits
        if b_high:
            curr_setup = curr_setup | NKT_M66.SETUP_BIT_BLANKING_LEVEL
        else:
            curr_setup = curr_setup & (~ NKT_M66.SETUP_BIT_BLANKING_LEVEL)
        self.setup_bits = curr_setup

    @property
    def min_wavelength(self):
        return self.read_reg(0x34, '<u4')[0]

    @property
    def max_wavelength(self):
        return self.read_reg(0x35, '<u4')[0]

    @property
    def fsk_mode(self):
        return self.read_reg(0x3B, '<u1')[0]

    @fsk_mode.setter
    def fsk_mode(self, mode: int):
        # FIXME: non-free, may need verification
        self.write_reg(0x3B, np.array([mode, ], dtype='<u1').tobytes())

    @property
    def daughter_board_enable(self):
        return self.read_reg(0x3C, '<u1')[0]

    @daughter_board_enable.setter
    def daughter_board_enable(self, b_en: bool):
        self.write_reg(0x3C, b'\x01' if b_en else b'\x00')

    @property
    def connected_crystal(self):
        return self.read_reg(0x75, '<u1')[0]

    def get_wavelength(self, ch: int):
        if 0 <= ch < 8:
            return self.read_reg(0x90 + ch, '<u4')

    def set_wavelength(self, ch: int, wl0: int, wl1=None, wl2=None, wl3=None):
        if 0 <= ch < 8:
            if wl1 is None or wl2 is None or wl3 is None:
                self.write_reg(0x90 + ch, np.array([wl0, ], dtype='<u4').tobytes())
            else:
                self.write_reg(0x90 + ch, np.array([wl0, wl1, wl2, wl3], dtype='<u4').tobytes())

    def get_amplitude(self, ch: int):
        if 0 <= ch < 8:
            return self.read_reg(0xB0 + ch, '<u2')[0]

    def set_amplitude(self, ch: int, amp: int):
        if 0 <= ch < 8:
            self.write_reg(0xB0 + ch, np.array([amp, ], dtype='<u2').tobytes())

    def get_modulation_gain(self, ch: int):
        # FIXME: non-free FSK option
        pass

    def set_modulation_gain(self, ch: int, gain: float):
        # FIXME: non-free FSK option
        pass

    @property
    def status(self):
        return self.read_reg(0x66, '<u2')[0]

    STATUS_BIT_EMISSION = (0x01 << 0)
    STATUS_BIT_SUPPLY_VOLTAGE_LOW = (0x1 << 5)
    STATUS_BIT_MODULE_TEMP_OOR = (0x1 << 6)
    STATUS_BIT_AODS_COMM_TIMEOUT = (0x1 << 13)
    STATUS_BIT_NEEDS_CRYSTAL_INFO = (0x1 << 14)
    STATUS_BIT_ERROR_CODE_PRESENT = (0x1 << 15)

    @property
    def error_code(self):
        return self.read_reg(0x67, '<u1')[0]
