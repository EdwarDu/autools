# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fl266_config.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FL266_Config_Window(object):
    def setupUi(self, FL266_Config_Window):
        FL266_Config_Window.setObjectName("FL266_Config_Window")
        FL266_Config_Window.resize(414, 463)
        self.verticalLayout = QtWidgets.QVBoxLayout(FL266_Config_Window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_CONN = QtWidgets.QGroupBox(FL266_Config_Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_CONN.sizePolicy().hasHeightForWidth())
        self.groupBox_CONN.setSizePolicy(sizePolicy)
        self.groupBox_CONN.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_CONN.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox_CONN.setObjectName("groupBox_CONN")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_CONN)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(6, -1, 6, -1)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_COM_Refresh = QtWidgets.QPushButton(self.groupBox_CONN)
        self.pushButton_COM_Refresh.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_COM_Refresh.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_COM_Refresh.setCheckable(False)
        self.pushButton_COM_Refresh.setObjectName("pushButton_COM_Refresh")
        self.gridLayout.addWidget(self.pushButton_COM_Refresh, 3, 1, 1, 1)
        self.pushButton_COM_Open = QtWidgets.QPushButton(self.groupBox_CONN)
        self.pushButton_COM_Open.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_COM_Open.setCheckable(True)
        self.pushButton_COM_Open.setFlat(False)
        self.pushButton_COM_Open.setObjectName("pushButton_COM_Open")
        self.gridLayout.addWidget(self.pushButton_COM_Open, 3, 2, 1, 1)
        self.comboBox_COM_BaudRate = QtWidgets.QComboBox(self.groupBox_CONN)
        self.comboBox_COM_BaudRate.setEditable(False)
        self.comboBox_COM_BaudRate.setObjectName("comboBox_COM_BaudRate")
        self.comboBox_COM_BaudRate.addItem("")
        self.gridLayout.addWidget(self.comboBox_COM_BaudRate, 1, 1, 1, 2)
        self.comboBox_COM_Parity = QtWidgets.QComboBox(self.groupBox_CONN)
        self.comboBox_COM_Parity.setObjectName("comboBox_COM_Parity")
        self.comboBox_COM_Parity.addItem("")
        self.gridLayout.addWidget(self.comboBox_COM_Parity, 2, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox_CONN)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_COM_Status = QtWidgets.QLabel(self.groupBox_CONN)
        self.label_COM_Status.setStyleSheet("background : red")
        self.label_COM_Status.setText("")
        self.label_COM_Status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_COM_Status.setObjectName("label_COM_Status")
        self.gridLayout.addWidget(self.label_COM_Status, 3, 0, 1, 1)
        self.comboBox_COM = QtWidgets.QComboBox(self.groupBox_CONN)
        self.comboBox_COM.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_COM.sizePolicy().hasHeightForWidth())
        self.comboBox_COM.setSizePolicy(sizePolicy)
        self.comboBox_COM.setObjectName("comboBox_COM")
        self.gridLayout.addWidget(self.comboBox_COM, 0, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.groupBox_CONN)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_CONN)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox_CONN)
        self.groupBox_Settings = QtWidgets.QGroupBox(FL266_Config_Window)
        self.groupBox_Settings.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_Settings.sizePolicy().hasHeightForWidth())
        self.groupBox_Settings.setSizePolicy(sizePolicy)
        self.groupBox_Settings.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_Settings.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox_Settings.setObjectName("groupBox_Settings")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_Settings)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setContentsMargins(6, -1, 6, -1)
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_Settings)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 2)
        self.checkBox_LaserON = QtWidgets.QCheckBox(self.groupBox_Settings)
        self.checkBox_LaserON.setObjectName("checkBox_LaserON")
        self.gridLayout_5.addWidget(self.checkBox_LaserON, 0, 2, 1, 3)
        self.label_15 = QtWidgets.QLabel(self.groupBox_Settings)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 2, 0, 1, 2)
        self.pushButton_SetFrequency = QtWidgets.QPushButton(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SetFrequency.sizePolicy().hasHeightForWidth())
        self.pushButton_SetFrequency.setSizePolicy(sizePolicy)
        self.pushButton_SetFrequency.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_SetFrequency.setToolTip("")
        self.pushButton_SetFrequency.setObjectName("pushButton_SetFrequency")
        self.gridLayout_5.addWidget(self.pushButton_SetFrequency, 2, 3, 1, 2)
        self.spinBox_PowerPerc = QtWidgets.QSpinBox(self.groupBox_Settings)
        self.spinBox_PowerPerc.setKeyboardTracking(False)
        self.spinBox_PowerPerc.setMinimum(1)
        self.spinBox_PowerPerc.setMaximum(100)
        self.spinBox_PowerPerc.setObjectName("spinBox_PowerPerc")
        self.gridLayout_5.addWidget(self.spinBox_PowerPerc, 1, 2, 1, 1)
        self.pushButton_SetPowerPerc = QtWidgets.QPushButton(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SetPowerPerc.sizePolicy().hasHeightForWidth())
        self.pushButton_SetPowerPerc.setSizePolicy(sizePolicy)
        self.pushButton_SetPowerPerc.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_SetPowerPerc.setToolTip("")
        self.pushButton_SetPowerPerc.setObjectName("pushButton_SetPowerPerc")
        self.gridLayout_5.addWidget(self.pushButton_SetPowerPerc, 1, 3, 1, 2)
        self.spinBox_Frequency = QtWidgets.QSpinBox(self.groupBox_Settings)
        self.spinBox_Frequency.setKeyboardTracking(False)
        self.spinBox_Frequency.setMinimum(1)
        self.spinBox_Frequency.setMaximum(19999)
        self.spinBox_Frequency.setObjectName("spinBox_Frequency")
        self.gridLayout_5.addWidget(self.spinBox_Frequency, 2, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_Settings)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 1, 0, 1, 2)
        self.verticalLayout_6.addLayout(self.gridLayout_5)
        self.verticalLayout.addWidget(self.groupBox_Settings)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(FL266_Config_Window)
        self.comboBox_COM_BaudRate.setCurrentIndex(0)
        self.comboBox_COM_Parity.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FL266_Config_Window)
        FL266_Config_Window.setTabOrder(self.comboBox_COM, self.comboBox_COM_BaudRate)
        FL266_Config_Window.setTabOrder(self.comboBox_COM_BaudRate, self.comboBox_COM_Parity)
        FL266_Config_Window.setTabOrder(self.comboBox_COM_Parity, self.pushButton_COM_Refresh)
        FL266_Config_Window.setTabOrder(self.pushButton_COM_Refresh, self.pushButton_COM_Open)
        FL266_Config_Window.setTabOrder(self.pushButton_COM_Open, self.spinBox_PowerPerc)

    def retranslateUi(self, FL266_Config_Window):
        _translate = QtCore.QCoreApplication.translate
        FL266_Config_Window.setWindowTitle(_translate("FL266_Config_Window", "SR830 Configuration"))
        self.groupBox_CONN.setTitle(_translate("FL266_Config_Window", "FL266 COM"))
        self.pushButton_COM_Refresh.setText(_translate("FL266_Config_Window", "Refresh"))
        self.pushButton_COM_Open.setText(_translate("FL266_Config_Window", "Open"))
        self.comboBox_COM_BaudRate.setCurrentText(_translate("FL266_Config_Window", "9600"))
        self.comboBox_COM_BaudRate.setItemText(0, _translate("FL266_Config_Window", "9600"))
        self.comboBox_COM_Parity.setCurrentText(_translate("FL266_Config_Window", "None"))
        self.comboBox_COM_Parity.setItemText(0, _translate("FL266_Config_Window", "None"))
        self.label.setText(_translate("FL266_Config_Window", "COM:"))
        self.label_7.setText(_translate("FL266_Config_Window", "Parity:"))
        self.label_6.setText(_translate("FL266_Config_Window", "BaudRate:"))
        self.groupBox_Settings.setTitle(_translate("FL266_Config_Window", "FL266 Settings"))
        self.label_2.setText(_translate("FL266_Config_Window", "Laser:"))
        self.checkBox_LaserON.setText(_translate("FL266_Config_Window", "ON"))
        self.label_15.setText(_translate("FL266_Config_Window", "Frequency:"))
        self.pushButton_SetFrequency.setText(_translate("FL266_Config_Window", "Set"))
        self.pushButton_SetPowerPerc.setText(_translate("FL266_Config_Window", "Set"))
        self.label_14.setText(_translate("FL266_Config_Window", "Power %:"))
