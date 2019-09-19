import serial
from .NKTMan import NKTMan
import numpy as np


class NKTMan_Fianium(NKTMan):
    """
    With specific register read/write for Fianium
    """
    def __init__(self,
                 module_addr,
                 serial_name,
                 baudrate=9600,
                 parity=serial.PARITY_NONE,
                 stopbits=serial.STOPBITS_ONE,
                 host_addr=0x52):
        super(NKTMan_Fianium, self).__init__(serial_name, baudrate, parity, stopbits, host_addr)
        self.module_addr = module_addr
        if self.get_module_type(module_addr) != 0x60:
            raise IOError(f'Module at {module_addr} is not SuperK EXTREME (S4x2)/Fianium')

    @property
    def system_type(self):
        raw_data = self.read_reg(self.module_addr, 0x6B)
        return raw_data[0]

    @property
    def inlet_temperature(self):
        raw_data = self.read_reg(self.module_addr, 0x11)
        return np.frombuffer(raw_data, dtype='<i2')[0] / 10

    @property
    def emission(self):
        raw_data = self.read_reg(self.module_addr, 0x30)
        if raw_data[0] == 0:
            return False
        elif raw_data[0] == 3:
            return True
        else:
            raise ValueError(f'Unknown emission status {raw_data[0]}')

    @emission.setter
    def emission(self, b_on: bool):
        data = b'\x03' if b_on else b'\x00'
        self.write_reg(self.module_addr, 0x30, data)

    @property
    def monitor_input2_gain(self):
        raw_data = self.read_reg(self.module_addr, 0x33)
        return raw_data[0]

    @monitor_input2_gain.setter
    def monitor_input2_gain(self, gain: int):
        if not 0 <= gain <= 7:
            raise ValueError(f'gain must by U8 [0, 7]')
        else:
            self.write_reg(self.module_addr, 0x33, np.array([gain, ], dtype='<u1').tobytes())

    @property
    def rf_switch(self):
        raw_data = self.read_reg(self.module_addr, 0x34)
        return raw_data[0]

    @rf_switch.setter
    def rf_switch(self, value: int):
        if not 0 <= value <= 1:
            raise ValueError(f'value must by U8 [0, 1]')
        else:
            self.write_reg(self.module_addr, 0x34, np.array([value, ], dtype='<u1').tobytes())

    @property
    def monitor_switch(self):
        raw_data = self.read_reg(self.module_addr, 0x34)
        return raw_data[0]

    @monitor_switch.setter
    def monitor_switch(self, value: int):
        if not 0 <= value <= 255:
            raise ValueError(f'value must by U8 [0, 1]')
        else:
            self.write_reg(self.module_addr, 0x34, np.array([value, ], dtype='<u1').tobytes())

    @property
    def crystal1_minimal_wavelength(self):
        raw_data = self.read_reg(self.module_addr, 0x9)
        return np.frombuffer(raw_data, dtype='<u4')[0]

    @property
    def crystal1_maximal_wavelength(self):
        raw_data = self.read_reg(self.module_addr, 0x91)
        return np.frombuffer(raw_data, dtype='<u4')[0]

    @property
    def crystal2_minimal_wavelength(self):
        raw_data = self.read_reg(self.module_addr, 0xA0)
        return np.frombuffer(raw_data, dtype='<u4')[0]

    @property
    def crystal2_maximal_wavelength(self):
        raw_data = self.read_reg(self.module_addr, 0xA1)
        return np.frombuffer(raw_data, dtype='<u4')[0]

    @property
    def serial_number(self):
        return self.read_reg(self.module_addr, 0x65).decode('utf-8')

    @property
    def status(self):
        raw_data = self.read_reg(self.module_addr, 0x66)
        return np.frombuffer(raw_data, dtype='<u2')[0]

    def status_interlock_off(self, status=None):
        if status is None:
            status = self.status

        return (status & (0x0001 << 1)) != 0x0000

    def status_interlock_loop_in(self, status=None):
        if status is None:
            status = self.status

        return (status & (0x0001 << 2)) != 0x0000

    def status_interlock_loop_out(self, status=None):
        if status is None:
            status = self.status

        return (status & (0x0001 << 3)) != 0x0000

    def status_supply_voltage_low(self, status=None):
        if status is None:
            status = self.status

        return (status & (0x0001 << 5)) != 0x0000

    def status_module_temp_range(self, status=None):
        if status is None:
            status = self.status

        return (status & (0x0001 << 6)) != 0x0000

    def status_shutter_sensor1(self, status=None):
        if status is None:
            status = self.status

        return (status & (0x0001 << 8)) != 0x0000

    def status_shutter_sensor2(self, status=None):
        if status is None:
            status = self.status

        return (status & (0x0001 << 9)) != 0x0000

    def status_new_crystal1_temperature(self, status=None):
        if status is None:
            status = self.status

        return (status & (0x0001 << 10)) != 0x0000

    def status_new_crystal2_temperature(self, status=None):
        if status is None:
            status = self.status

        return (status & (0x0001 << 11)) != 0x0000

    def status_error_code_present(self, status=None):
        if status is None:
            status = self.status

        return (status & (0x0001 << 15)) != 0x0000

    @property
    def error_code(self):
        return self.read_reg(self.module_addr, 0x67)[0]

