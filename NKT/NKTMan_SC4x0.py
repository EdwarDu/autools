#!/usr/bin/python3

import serial
import serial.tools.list_ports


class NKTMan_SC4x0:

    CMD_TERMINATOR = '\r'
    ANS_TERMINATOR = '\r'

    def __init__(self,
                 serial_name,
                 baudrate=19200,
                 parity=serial.PARITY_NONE,
                 stopbits=serial.STOPBITS_ONE):
        self.ser = serial.Serial(port=serial_name,
                                 baudrate=baudrate,
                                 bytesize=serial.EIGHTBITS,
                                 parity=parity,
                                 stopbits=stopbits)

        self.ser.inter_byte_timeout = 0.1  # when device failed to send next byte within 3 read will exit

        if not self.ser.is_open():
            raise IOError(f"Failed to open {serial_name}")

    def send_cmd(self, cmd: str, b_query: bool, *args):
        cmd_str = cmd + \
                  ('?' if b_query else '=') + \
                  ' '.join([str(arg) for arg in args if arg is not None]) + \
                  NKTMan_SC4x0.CMD_TERMINATOR
        self.ser.write(cmd_str.encode('utf-8'))
        if b_query:
            return self.ser.read_until(NKTMan_SC4x0.ANS_TERMINATOR)
        else:
            # FIXME: Verify
            return None

    @property
    def alarms(self):
        alarms_str = self.send_cmd('A', True).decode('utf-8')
        return alarms_str

    def clear_all_alarms(self):
        self.send_cmd('A', False, 0)

    @property
    def back_reflection_monitor_value(self):
        return float(self.send_cmd('B', True).decode('utf-8'))

    @property
    def amp_alarm_threshold(self):
        return float(self.send_cmd('C', True).decode('utf-8'))

    @property
    def master_source_alarm_level(self):
        return float(self.send_cmd('D', True).decode('utf-8'))

    @property
    def cmd_list(self):
        return self.send_cmd('H', True).decode('utf-8')

    @property
    def status_display_interval(self):
        return float(self.send_cmd('I', True).decode('utf-8'))

    @status_display_interval.setter
    def status_display_interval(self, value):
        self.send_cmd('I', False, value)


