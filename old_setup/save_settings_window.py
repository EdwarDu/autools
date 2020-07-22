from .save_settings_ui import Ui_SaveSettingsDialog
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5 import QtCore, QtGui


class SaveSettingsWindow(Ui_SaveSettingsDialog):
    def __init__(self, *men):
        self.window = QWidget()
        Ui_SaveSettingsDialog.__init__(self)
        self.setupUi(self.window)

        self._men = men
        self._s_str = ""
        self.pushButton_Refresh.clicked.connect(self.refresh)
        self.pushButton_Save2File.clicked.connect(self.save2file)

    def refresh(self):
        settings_str = ""
        for man in self._men:
            settings_str = settings_str + man.get_current_settings()

        settings_str = settings_str + '\n--------------USER NOTE-------------\n'
        self._s_str = settings_str
        self.textBrowser_Settings.setText(settings_str)

    def save2file(self):
        fname, _ = QFileDialog.getSaveFileName(self.window, caption="Save settings to file",
                                               directory="./settings.txt",
                                               filter="All Files (*.*)",
                                              )
        if fname is not None and fname != "":
            with open(fname, "w") as f_setting:
                f_setting.write(self.textBrowser_Settings.toPlainText())

    def show(self):
        self.window.show()
