# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SaveSettingsDialog(object):
    def setupUi(self, SaveSettingsDialog):
        SaveSettingsDialog.setObjectName("SaveSettingsDialog")
        SaveSettingsDialog.resize(645, 403)
        self.gridLayout = QtWidgets.QGridLayout(SaveSettingsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_Refresh = QtWidgets.QPushButton(SaveSettingsDialog)
        self.pushButton_Refresh.setObjectName("pushButton_Refresh")
        self.gridLayout.addWidget(self.pushButton_Refresh, 1, 0, 1, 1)
        self.pushButton_Save2File = QtWidgets.QPushButton(SaveSettingsDialog)
        self.pushButton_Save2File.setObjectName("pushButton_Save2File")
        self.gridLayout.addWidget(self.pushButton_Save2File, 1, 1, 1, 1)
        self.textBrowser_Settings = QtWidgets.QTextBrowser(SaveSettingsDialog)
        self.textBrowser_Settings.setObjectName("textBrowser_Settings")
        self.gridLayout.addWidget(self.textBrowser_Settings, 0, 0, 1, 2)

        self.retranslateUi(SaveSettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(SaveSettingsDialog)

    def retranslateUi(self, SaveSettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SaveSettingsDialog.setWindowTitle(_translate("SaveSettingsDialog", "Save settings..."))
        self.pushButton_Refresh.setText(_translate("SaveSettingsDialog", "Refresh"))
        self.pushButton_Save2File.setText(_translate("SaveSettingsDialog", "Save ..."))
