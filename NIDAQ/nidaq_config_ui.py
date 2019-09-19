# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nidaq_config.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NIDAQ_Config_Window(object):
    def setupUi(self, NIDAQ_Config_Window):
        NIDAQ_Config_Window.setObjectName("NIDAQ_Config_Window")
        NIDAQ_Config_Window.resize(395, 575)
        self.verticalLayout = QtWidgets.QVBoxLayout(NIDAQ_Config_Window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(NIDAQ_Config_Window)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_Conn = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Conn.setToolTip("")
        self.pushButton_Conn.setCheckable(True)
        self.pushButton_Conn.setObjectName("pushButton_Conn")
        self.gridLayout_6.addWidget(self.pushButton_Conn, 1, 3, 1, 1)
        self.label_Conn_Status = QtWidgets.QLabel(self.groupBox)
        self.label_Conn_Status.setMinimumSize(QtCore.QSize(80, 0))
        self.label_Conn_Status.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_Conn_Status.setStyleSheet("background : red")
        self.label_Conn_Status.setText("")
        self.label_Conn_Status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Conn_Status.setObjectName("label_Conn_Status")
        self.gridLayout_6.addWidget(self.label_Conn_Status, 1, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.groupBox)
        self.label_38.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_38.setObjectName("label_38")
        self.gridLayout_6.addWidget(self.label_38, 0, 0, 1, 1)
        self.pushButton_Refresh = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Refresh.setToolTip("")
        self.pushButton_Refresh.setObjectName("pushButton_Refresh")
        self.gridLayout_6.addWidget(self.pushButton_Refresh, 1, 2, 1, 1)
        self.comboBox_Device = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_Device.setObjectName("comboBox_Device")
        self.gridLayout_6.addWidget(self.comboBox_Device, 0, 2, 1, 2)
        self.verticalLayout_7.addLayout(self.gridLayout_6)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_Control = QtWidgets.QGroupBox(NIDAQ_Config_Window)
        self.groupBox_Control.setEnabled(False)
        self.groupBox_Control.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_Control.setObjectName("groupBox_Control")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_Control)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.pushButton_Sync = QtWidgets.QPushButton(self.groupBox_Control)
        self.pushButton_Sync.setObjectName("pushButton_Sync")
        self.verticalLayout_13.addWidget(self.pushButton_Sync)
        self.gridLayout_Channels = QtWidgets.QGridLayout()
        self.gridLayout_Channels.setObjectName("gridLayout_Channels")
        self.verticalLayout_13.addLayout(self.gridLayout_Channels)
        self.verticalLayout.addWidget(self.groupBox_Control)
        spacerItem = QtWidgets.QSpacerItem(20, 815, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(NIDAQ_Config_Window)
        QtCore.QMetaObject.connectSlotsByName(NIDAQ_Config_Window)
        NIDAQ_Config_Window.setTabOrder(self.comboBox_Device, self.pushButton_Refresh)
        NIDAQ_Config_Window.setTabOrder(self.pushButton_Refresh, self.pushButton_Conn)
        NIDAQ_Config_Window.setTabOrder(self.pushButton_Conn, self.pushButton_Sync)

    def retranslateUi(self, NIDAQ_Config_Window):
        _translate = QtCore.QCoreApplication.translate
        NIDAQ_Config_Window.setWindowTitle(_translate("NIDAQ_Config_Window", "NIDAQ Configuration"))
        self.groupBox.setTitle(_translate("NIDAQ_Config_Window", "NI DAQ Connection"))
        self.pushButton_Conn.setText(_translate("NIDAQ_Config_Window", "Open"))
        self.label_38.setText(_translate("NIDAQ_Config_Window", "Dev:"))
        self.pushButton_Refresh.setText(_translate("NIDAQ_Config_Window", "Refresh"))
        self.groupBox_Control.setTitle(_translate("NIDAQ_Config_Window", "NI DAQ Control"))
        self.pushButton_Sync.setText(_translate("NIDAQ_Config_Window", "Sync"))


