from .NKTMan import NKTMan, nkt_logger
import numpy as np


class NKT_M60:
    """
    Class for Module type 60 SuperK Extreme (S4x2), Fianium
    """
    def __init__(self, nkt_man: NKTMan,
                 module_addr: int = 0x15):
        self.nkt_man = nkt_man
        self.module_addr = module_addr

        # Verify
        assert(self.nkt_man.get_module_type(self.module_addr) == 0x60)

    def read_reg(self, reg_addr: int, dtype=None):
        return self.nkt_man.read_reg(self.module_addr, reg_addr, dtype)

    def write_reg(self, reg_addr: int, data):
        self.nkt_man.write_reg(self.module_addr, reg_addr, data)

    @property
    def system_type(self):
        return self.read_reg(0x6B, '<u1')[0]

    @property
    def inlet_temperature(self):
        return self.read_reg(0x11, '<i2')[0] / 10

    @property
    def emission(self):
        return self.read_reg(0x30, '<u1')[0]

    @emission.setter
    def emission(self, b_on: bool):
        self.write_reg(0x30, b'\x03' if b_on else b'\x00')

    @property
    def setup(self):
        return self.read_reg(0x31, '<u2')[0]

    @setup.setter
    def setup(self, mode: int):
        if 0 <= mode <= 4:
            self.write_reg(0x31, np.array([mode, ], dtype='<u2').tobytes())
        else:
            raise ValueError(f"Setup should be in range [0, 4]")

    @property
    def interlock(self):
        lsb, msb = self.read_reg(0x32, '<u1')
        return lsb, msb

    @interlock.setter
    def interlock(self, b_reset: bool):
        self.write_reg(0x32, b'\x01' if b_reset else b'\x00')

    @property
    def pulse_picker_ratio(self):
        raw_data = self.read_reg(0x34)
        if len(raw_data) == 1:
            return np.frombuffer(raw_data, '<u1')
        elif len(raw_data) == 2:
            return np.frombuffer(raw_data, '<u2')
        else:
            raise ValueError(f"Unexpected pulse picker ratio value {raw_data}")

    @pulse_picker_ratio.setter
    def pulse_picker_ratio(self, r: int):
        self.write_reg(0x34, np.array([r, ], dtype='<u2').tobytes())

    @property
    def watchdog_interval(self):
        return self.read_reg(0x36, '<u1')[0]

    @watchdog_interval.setter
    def watchdog_interval(self, interv: int):
        self.write_reg(0x36, np.array([interv, ], dtype='<u2').tobytes())

    @property
    def power_level(self):
        return self.read_reg(0x37, '<u2')[0]/1000

    @property
    def current_level(self):
        return self.read_reg(0x38, '<u2')[0] / 1000

    @power_level.setter
    def power_level(self, lv: float):
        lv_i = int(lv*1000)
        self.write_reg(0x37, np.array([lv_i, ], dtype='<u2').tobytes())

    @current_level.setter
    def current_level(self, lv: float):
        lv_i = int(lv * 1000)
        self.write_reg(0x38, np.array([lv_i, ], dtype='<u2').tobytes())

    @property
    def nim_delay(self):
        return self.read_reg(0x39, '<u2')[0]

    @nim_delay.setter
    def nim_delay(self, delay: int):
        self.write_reg(0x39, np.array([delay, ], dtype='<u2').tobytes())

    @property
    def status(self):
        return self.read_reg(0x66, '<u2')[0]

    STATUS_BIT_EMISSION_ON = (0x0001 << 0)
    STATUS_BIT_INTERLOCK_RELAY_OFF = (0x0001 << 1)
    STATUS_BIT_INTERLOCK_POWER_FAILURE = (0x0001 << 2)
    STATUS_BIT_INTERLOCK_LOOP_OPEN = (0x0001 << 3)
    STATUS_BIT_OUTPUT_CTRL_SIG_LOW = (0x0001 << 4)
    STATUS_BIT_SUPPLY_VOL_LOW = (0x0001 << 5)
    STATUS_BIT_INLET_TEMP_OOR = (0x0001 << 6)
    STATUS_BIT_CLOCK_BATTERY_LOW = (0x0001 << 7)
    STATUS_BIT_CRC_ERROR_START = (0x0001 << 13)
    STATUS_BIT_LOG_ERROR = (0x0001 << 14)
    STATUS_BIT_SYS_ERROR = (0x0001 << 15)

