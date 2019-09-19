from msl.loadlib import Server32
import ctypes
import time


class Aotf32(Server32):
    def __init__(self, host, port, quiet, **kwargs):
        super().__init__(kwargs['lib_path'], 'cdll', host, port, quiet)

    def open(self, dev_id: int):
        return self.lib.AotfOpen(dev_id)

    def command(self, h_dev: int, cmd: str):
        strbuf = ctypes.create_string_buffer(1024)
        bytesread = ctypes.c_uint()

        # Flush
        for i in range(0, 10):
            if self.lib.AotfIsReadDataAvailable(h_dev):
                val = self.lib.AotfRead(h_dev, len(strbuf),
                                        ctypes.byref(strbuf),
                                        ctypes.byref(bytesread))

        self.lib.AotfWrite(h_dev, len(cmd), cmd.encode('ascii'))
        # Read reply
        ret = ''
        i = 0
        while i < 20:
            if self.lib.AotfIsReadDataAvailable(h_dev):
                val = self.lib.AotfRead(h_dev, len(strbuf),
                                        ctypes.byref(strbuf),
                                        ctypes.byref(bytesread))
                if val != 1:
                    break
                ret += strbuf[:bytesread.value].decode('ascii')
                if ret.startswith(cmd):
                    ret = ret[len(cmd):]

                if "* " in ret:
                    break
            else:
                time.sleep(0.02)
                i += 1

        ret = ret.replace("* ", "").strip()
        return ret

    def close(self, h_dev: int):
        self.lib.AotfClose(h_dev)