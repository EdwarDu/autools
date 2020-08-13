from .NKTMan import NKTMan, nkt_logger
from .NKT_M66 import NKT_M66 as NKT_SuperKRF
from .NKT_M60 import NKT_M60 as NKT_SuperK
from .NKT_M67 import NKT_M67 as NKT_SuperKSelect

from PyQt5.QtCore import QObject, pyqtSignal


class NKT_SuperKEgMan(QObject):
    # TODO: Unify the API to control the setup (different operations have to be done with different modules)
    def __init__(self):
        super().__init__()
        pass


class NKT_SuperKEgConfigWindow:
    # TODO
    def __init__(self, nkt_superk_man: NKT_SuperKEgMan):
        self.man = nkt_superk_man