#!/usr/bin/env python3

import serial
import serial.tools.list_ports

from threading import Lock


class FianiumSC400Man:
    """
    Separate Fianium SC400 Helper Class
    FIXME: Command format unclear from doc
    """

    COMMAND_END = '\r'

    def __init__(self, serial_name, uart_lock=None):
        self.ser = serial.Serial(port=serial_name,
                                 baudrate=19200,
                                 bytesize=serial.EIGHTBITS,
                                 parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE)
        self.ser.inter_byte_timeout = 0.1

        if not self.ser.is_open:
            raise IOError(f'Failed to open {serial_name}')

        if uart_lock is None:
            self.ser_lock = Lock()
        else:
            self.ser_lock = uart_lock

    def send_cmd(self, cmd: str, b_query: bool, *args):
        cmd_str = cmd + ('?' if b_query else '=') + \
                  ','.join([str(arg) for arg in args if arg is not None]) + \
                  FianiumSC400Man.COMMAND_END

        with self.ser_lock:
            self.ser.write(cmd_str.encode('utf-8'))
            if b_query:
                return self.ser.read_until(terminator=FianiumSC400Man.COMMAND_END.encode('utf-8'))
            else:
                return None

    def get_alarms(self):
        return self.send_cmd('A', True)

    def clear_all_alarms(self):
        self.send_cmd('A', False, 0)

    def get_reflection_monitor_value(self):
        return self.send_cmd('B', True)

    def get_amplifier_alarm_threshold(self):
        return self.send_cmd('C', True)

    def get_master_source_alarm_lvl(self):
        return self.send_cmd('D', True)

    def get_list_commands(self):
        return self.send_cmd('H', True)

    def get_status_display_interval(self):
        return self.send_cmd('I', True)

    def set_status_display_interval(self, x):
        self.send_cmd('I', False, x)

    def get_laser_serial_number(self):
        self.send_cmd('J', True)

    def get_reflection_alarm_level(self):
        return self.send_cmd('L', True)

    def get_laser_control_mode(self):
        return self.send_cmd('M', True)

    def get_master_source_warmup_timer_status(self):
        return self.send_cmd('O', True)

    def get_preamplifier_monitor_value(self):
        return self.send_cmd('P', True)

    def get_amplifier_control_dac_value(self):
        return self.send_cmd('Q', True)

    def set_amplifier_current_control_dac_value(self, x):
        self.send_cmd('Q', False, x)

    def get_maximum_permissible_q_value(self):
        return self.send_cmd('S', True)

    def get_repetition_rate(self):
        return self.send_cmd('R', True)

    def set_repetition_rate(self, x):
        self.send_cmd('R', False, x)

    def get_chassis_temperature(self):
        return self.send_cmd('T', True)

    def get_control_software_info(self):
        return self.send_cmd('V', True)

    def get_laser_operating_time_counter(self):
        return self.send_cmd('W', True)

    def get_status_display_mode(self):
        return self.send_cmd('X', True)

    def set_status_display_mode(self, x):
        self.send_cmd('X', False, x)

    def release_laser_control(self):
        self.send_cmd('switch', False, 0)

    def dispose(self):
        self.ser.close()
