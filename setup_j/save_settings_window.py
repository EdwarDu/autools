from .save_settings_ui import Ui_SaveSettingsDialog
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5 import QtCore, QtGui


class SaveSettingsWindow(Ui_SaveSettingsDialog):
    def __init__(self, *men):
        self.window = QWidget()
        Ui_SaveSettingsDialog.__init__(self)
        self._men = men
        self._s_str = ""
        self.pushButton_Refresh.clicked.connect(self.refresh)
        self.pushButton_Save2File.clicked.connect(self.save2file)

    def refresh(self):
        settings_str = ""
        for man in self._men:
            settings_str = settings_str + man.get_current_settings()

        self._s_str = settings_str
        self.textBrowser_Settings.setText(settings_str)

    def save2file(self):
        fname, _ = QFileDialog.getSaveFileName(self.window, "Save settings to file", ".",
                                               "All Files (*.*)")
        if fname is not None and fname != "":
            with open(fname, "w") as f_setting:
                f_setting.write(self._s_str)

    def show(self):
        self.window.show()
