from msl.loadlib import Client64


class Aotf64(Client64):
    """Send a request to 'MyServer' to execute the 'add' method and get the response."""

    def __init__(self, lib_path: str):
        super(Aotf64, self).__init__(module32='autools.YSL.Aotf32', lib_path=lib_path)

    def __getattr__(self, method32):
        def send(*args, **kwargs):
            return self.request32(method32, *args, **kwargs)

        return send

