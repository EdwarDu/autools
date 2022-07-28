#!/usr/bin/env python3

class APTComm:
    """Helper function for assemble messages for ThorLabs devices"""

    @staticmethod
    def mod_identify(chan_id: int):
        return bytearray([0x23, 0x02, 0xFF & chan_id, 0x00, 0x11, 0x01])

    @staticmethod
    def set_chan_enable(chan_id: int, enable: bool, dst: int = 0x50):
        return bytearray([0x10, 0x02, 0xFF&chan_id, 0x01 if enable else 0x02, dst, 0x01])

    @staticmethod
    def set_sol_state(chan_id: int, on_off: bool, dst: int = 0x50):
        return bytearray([0xCB, 0x04, 0xFF & chan_id, 0x01 if on_off else 0x02, dst, 0x01])

    @staticmethod
    def req_sol_state(chan_id: int, dst: int = 0x50):
        return bytearray([0xCC, 0x04, 0xFF & chan_id, 0x00, dst, 0x01])

    @staticmethod
    def get_sol_state(resp: bytes | bytearray):
        if len(resp) != 6:
            raise ValueError("Wrong length of response")
        if resp[0] != 0xCD or resp[1] != 0x04 or resp[3] not in (0x01, 0x02) or resp[4] != 0x01 or resp[5] != 0x50:
            raise ValueError("Wrong format of response")
        return (int(resp[2]), True if resp[3] == 0x01 else False)

