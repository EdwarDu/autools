#!/usr/bin/env python3

import serial
import serial.tools.list_ports
import numpy as np
from PyQt5.QtCore import pyqtSignal
import logging

_SPLIT_LOG = False

if _SPLIT_LOG:
    nkt_logger = logging.getLogger("nkt")
    nkt_logger.setLevel(logging.DEBUG)
    nkt_fh = logging.FileHandler("nkt.log")
    nkt_formatter = logging.Formatter('%(asctime)s [%(component)s] - %(levelname)s - %(message)s')
    nkt_fh.setFormatter(nkt_formatter)
    nkt_logger.addHandler(nkt_fh)

    nkt_ch = logging.StreamHandler()
    nkt_ch.setFormatter(nkt_formatter)
    nkt_logger.addHandler(nkt_ch)
else:
    nkt_logger = logging.getLogger("autools_setup_main")


class NKTMan:
    """
    NKT (Man) Class for managing communication with NKT Devices
    """

    opened = pyqtSignal()
    closed = pyqtSignal()

    TELEGRAM_START = 0x0D
    TELEGRAM_END = 0x0A

    def __init__(self,
                 serial_name=None,
                 baudrate=115200,
                 parity=serial.PARITY_NONE,
                 stopbits=serial.STOPBITS_ONE,
                 host_addr=0xA1):
        self.host_addr=host_addr
        self.com_dev = serial_name
        self.ser_baudrate = baudrate
        self.ser_parity = parity
        self.ser_stopbits = stopbits

        if self.com_dev is None:
            self.ser = None
        else:
            self.ser = serial.Serial(port=self.com_dev,
                                     baudrate=self.ser_baudrate,
                                     bytesize=serial.EIGHTBITS,
                                     parity=self.ser_parity,
                                     stopbits=self.ser_stopbits)
            self.ser.timeout = 0.1  # Timeout set to 100ms
            self.ser.inter_byte_timeout = 0.1

            if not self.ser.is_open():
                raise IOError(f"Failed to open {serial_name}")
            else:
                self.opened.emit()

    def open(self):
        if self.ser is not None and self.ser.is_open:
            self.ser.close()

        self.ser = serial.Serial(port=self.com_dev, baudrate=self.ser_baudrate, bytesize=serial.EIGHTBITS,
                                 parity=self.ser_parity, stopbits=self.ser_stopbits)

        self.ser.inter_byte_timeout = 0.1

        if not self.ser.is_open:
            raise IOError(f"Failed to open the device {self.com_dev}")
        else:
            self.opened.emit()

    def close(self):
        if self.ser is not None and self.ser.is_open:
            self.ser.close()
        self.closed.emit()
        self.ser = None

    MESSAGE_TYPE_NACK = 0x00
    MESSAGE_TYPE_CRC_ERR = 0x01
    MESSAGE_TYPE_BUSY = 0x02
    MESSAGE_TYPE_ACK = 0x03
    MESSAGE_TYPE_READ = 0x04
    MESSAGE_TYPE_WRITE = 0x05
    MESSAGE_TYPE_WRITE_SET = 0x06
    MESSAGE_TYPE_WRITE_CLR = 0x07
    MESSAGE_TYPE_DATAGRAM = 0x08
    MESSAGE_TYPE_WRITE_TGL = 0x09

    MODULE_TYPE_DICT = {
        0x0: "N/A",
        0x20: "Koheras AdjustiK/BoostiK (K81-1 to K83-1)",
        0x21: "Koheras BasiK Module (K80-1)",
        0x33: "Koheras BASIK Module (K1x2)",
        0x34: "Koheras ADJUSTIK/ACOUSTIK (K822 / K852)",
        0x36: "Koheras BASIK MIKRO Module (K0x2)",
        0x60: "SuperK Extreme (S4x2), Fianium",
        0x61: "SuperK Extreme Front panel",
        0x66: "RF Driver (A901) & SuperK Select (A203)",
        0x67: "SuperK SELECT (A203)",
        0x68: "SuperK VARIA (A301)",
        0x6B: "Extend UV (A351)",
        0x70: "BoostiK OEM Amplifier (N83)",
        0x74: "SuperK COMPACT (S024)",
        0x7D: "SuperK EVO (S2x1)"
    }

    @staticmethod
    def get_crc16(data: bytearray, poly: int = 0x1021):
        reg = 0x0000
        calc_data = data + b'\x00\x00'
        for byte in calc_data:
            mask = 0x80
            while mask > 0:
                reg <<= 1
                if byte & mask:
                    reg += 1
                mask >>= 1
                if reg > 0xffff:
                    reg &= 0xffff
                    reg ^= poly
        return reg & 0xFF, (reg & 0xFF00) >> 8

    @staticmethod
    def construct_message(dest: int, src: int, msg_type: int, reg_num: int,
                          data: bytes or bytearray):
        msg = bytearray()
        msg.append(dest)
        msg.append(src)
        msg.append(msg_type)
        msg.append(reg_num)
        msg += data
        crc_lsb, crc_msb = NKTMan.get_crc16(msg)
        msg.append(crc_msb)
        msg.append(crc_lsb)

        return msg

    @staticmethod
    def message2telegram(msg: bytes or bytearray):
        telegram = bytearray()
        telegram.append(NKTMan.TELEGRAM_START)
        for b in msg:
            if b == 0x0A:
                telegram.append(0x5E)
                telegram.append(0x4A)
            elif b == 0x0D:
                telegram.append(0x5E)
                telegram.append(0x4D)
            elif b == 0x5E:
                telegram.append(0x5E)
                telegram.append(0x9E)
            else:
                telegram.append(b)
        telegram.append(NKTMan.TELEGRAM_END)
        return telegram

    @staticmethod
    def telegram2message(tg: bytes or bytearray):
        if type(tg) is bytes:
            tg = bytearray(tg)

        assert(tg[0] == 0x0D)
        assert(tg[-1] == 0x0A)

        msg = bytearray()
        b_previous_5e = False
        for b in tg[1:-1]:
            if b_previous_5e:
                msg.append(b-64)
                b_previous_5e = False
            elif b == 0x5E:
                b_previous_5e = True
            else:
                msg.append(b)

        return msg

    @staticmethod
    def deconstruct_message(msg: bytes or bytearray):
        if type(msg) is bytes:
            msg = bytearray(msg)
        dest = msg[0]
        src = msg[1]
        msg_type = msg[2]
        reg_num = [3]
        data = msg[4:-2]

        crc_lsb, crc_msb = NKTMan.get_crc16(msg[0:-2])
        if crc_lsb != msg[-1] or crc_msb != msg[-2]:
            crc_error = True
        else:
            crc_error = False
        return dest, src, msg_type, reg_num, data, crc_error

    @staticmethod
    def print_bytes_hex(bs):
        for b in bs:
            print(hex(b)[2:].zfill(2), end=' ')
        print('')

    def send_telegram(self, tg: bytes or bytearray):
        self.ser.write(tg)

    def get_response_msg(self):
        self.ser.read_until(NKTMan.TELEGRAM_START)
        raw_data = self.ser.read_until(NKTMan.TELEGRAM_END)
        raw_data.insert(0, NKTMan.TELEGRAM_START)
        return NKTMan.telegram2message(raw_data)

    def read_reg(self, module_addr, reg_addr, dtype=None):
        """ read register, dtype is used to decode as in numpy"""
        # FIXME: Verify if module_addr does not exist, IOError will be raised
        msg = NKTMan.construct_message(dest=module_addr, src=self.host_addr,
                                       msg_type=NKTMan.MESSAGE_TYPE_READ,
                                       reg_num=reg_addr,
                                       data=b'')
        tg = NKTMan.message2telegram(msg)
        self.send_telegram(tg)
        msg_res = NKTMan.deconstruct_message(self.get_response_msg())
        r_dst, r_src, r_type, r_reg_n, r_data, r_crc_error = msg_res
        if r_crc_error:
            raise IOError(f'Register read to {reg_addr}@{module_addr} failed with crc error')
        elif r_dst != self.host_addr:
            raise IOError(f'Wrong dst addr {r_dst} instead of {self.host_addr}')
        elif r_src != module_addr:
            raise IOError(f'Wrong addr {r_src} instead of {module_addr} ')
        elif r_type != NKTMan.MESSAGE_TYPE_ACK:
            raise IOError(f'Wrong respond message type f{r_type}')
        elif r_reg_n != reg_addr:
            raise IOError(f'Wrong ACK register {r_reg_n} instead of {reg_addr}')
        else:
            if dtype is None:
                return r_data
            else:
                return np.frombuffer(r_data, dtype=dtype)

    def write_reg(self, module_addr, reg_addr, data: bytes or bytearray):
        msg = NKTMan.construct_message(dest=module_addr, src=self.host_addr,
                                       msg_type=NKTMan.MESSAGE_TYPE_WRITE,
                                       reg_num=reg_addr,
                                       data=data)
        tg = NKTMan.message2telegram(msg)
        self.send_telegram(tg)
        msg_res = NKTMan.deconstruct_message(self.get_response_msg())
        r_dst, r_src, r_type, r_reg_n, r_data, r_crc_error = msg_res
        if r_crc_error:
            raise IOError(f'Register read to {reg_addr}@{module_addr} failed with crc error')
        elif r_dst != self.host_addr:
            raise IOError(f'Wrong dst addr {r_dst} instead of {self.host_addr}')
        elif r_src != module_addr:
            raise IOError(f'Wrong addr {r_src} instead of {module_addr} ')
        elif r_type != NKTMan.MESSAGE_TYPE_ACK:
            raise IOError(f'Wrong respond message type f{r_type}')
        elif r_reg_n != reg_addr:
            raise IOError(f'Wrong ACK register {r_reg_n} instead of {reg_addr}')
        else:
            return

    def get_module_type(self, module_addr):
        try:
            module_type = self.read_reg(module_addr, 0x61)[0]
            return module_type
        except (serial.Timeout, IOError) as toe:
            return None

    def get_firmware_code(self, module_addr):
        return self.read_reg(module_addr, 0x64)

    def get_all_modules(self):
        module_lst = []
        for module_addr in range(1, 161):
            module_type = self.get_module_type(module_addr)
            if module_type is None:
                continue
            elif module_type not in NKTMan.MODULE_TYPE_DICT.keys():
                module_lst.append((module_addr, module_type, "UNKNOWN") )
            else:
                module_lst.append((module_addr, module_type, NKTMan.MODULE_TYPE_DICT[module_type]))
        return module_lst


if __name__ == '__main__':
    msg = NKTMan.construct_message(0x0A, 0xA2, 0x05, 0x23, bytearray(b'\x88\x13'),)
    NKTMan.print_bytes_hex(msg)
    tg = NKTMan.message2telegram(msg)
    NKTMan.print_bytes_hex(tg)

    tg_ack = b'\x0D\xA2\x5E\x4A\x03\x23\x81\x8D\x0A'
    msg_ack = NKTMan.telegram2message(tg_ack)
    NKTMan.print_bytes_hex(msg_ack)
    print(NKTMan.deconstruct_message(msg_ack))
