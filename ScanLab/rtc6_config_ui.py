# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rtc6_config.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RTC6_Config_Window(object):
    def setupUi(self, RTC6_Config_Window):
        RTC6_Config_Window.setObjectName("RTC6_Config_Window")
        RTC6_Config_Window.resize(596, 767)
        self.verticalLayout = QtWidgets.QVBoxLayout(RTC6_Config_Window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_CONN = QtWidgets.QGroupBox(RTC6_Config_Window)
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
        self.pushButton_CONN_Open = QtWidgets.QPushButton(self.groupBox_CONN)
        self.pushButton_CONN_Open.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_CONN_Open.setCheckable(True)
        self.pushButton_CONN_Open.setFlat(False)
        self.pushButton_CONN_Open.setObjectName("pushButton_CONN_Open")
        self.gridLayout.addWidget(self.pushButton_CONN_Open, 2, 1, 1, 2)
        self.pushButton_PickConfigPath = QtWidgets.QPushButton(self.groupBox_CONN)
        self.pushButton_PickConfigPath.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_PickConfigPath.setCheckable(True)
        self.pushButton_PickConfigPath.setFlat(False)
        self.pushButton_PickConfigPath.setObjectName("pushButton_PickConfigPath")
        self.gridLayout.addWidget(self.pushButton_PickConfigPath, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_CONN)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_CONN_Status = QtWidgets.QLabel(self.groupBox_CONN)
        self.label_CONN_Status.setStyleSheet("background : red")
        self.label_CONN_Status.setText("")
        self.label_CONN_Status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_CONN_Status.setObjectName("label_CONN_Status")
        self.gridLayout.addWidget(self.label_CONN_Status, 2, 0, 1, 1)
        self.lineEdit_ConfigPath = QtWidgets.QLineEdit(self.groupBox_CONN)
        self.lineEdit_ConfigPath.setReadOnly(True)
        self.lineEdit_ConfigPath.setObjectName("lineEdit_ConfigPath")
        self.gridLayout.addWidget(self.lineEdit_ConfigPath, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_CONN)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.lineEdit_CorFile = QtWidgets.QLineEdit(self.groupBox_CONN)
        self.lineEdit_CorFile.setReadOnly(True)
        self.lineEdit_CorFile.setObjectName("lineEdit_CorFile")
        self.gridLayout.addWidget(self.lineEdit_CorFile, 1, 1, 1, 1)
        self.pushButton_PickCorFile = QtWidgets.QPushButton(self.groupBox_CONN)
        self.pushButton_PickCorFile.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_PickCorFile.setCheckable(True)
        self.pushButton_PickCorFile.setFlat(False)
        self.pushButton_PickCorFile.setObjectName("pushButton_PickCorFile")
        self.gridLayout.addWidget(self.pushButton_PickCorFile, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox_CONN)
        self.groupBox_Settings = QtWidgets.QGroupBox(RTC6_Config_Window)
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
        self.spinBox_StepX = QtWidgets.QSpinBox(self.groupBox_Settings)
        self.spinBox_StepX.setMinimum(1)
        self.spinBox_StepX.setMaximum(99999)
        self.spinBox_StepX.setObjectName("spinBox_StepX")
        self.gridLayout_5.addWidget(self.spinBox_StepX, 1, 2, 1, 1)
        self.pushButton_StepYPlus = QtWidgets.QPushButton(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_StepYPlus.sizePolicy().hasHeightForWidth())
        self.pushButton_StepYPlus.setSizePolicy(sizePolicy)
        self.pushButton_StepYPlus.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_StepYPlus.setToolTip("")
        self.pushButton_StepYPlus.setObjectName("pushButton_StepYPlus")
        self.gridLayout_5.addWidget(self.pushButton_StepYPlus, 1, 7, 1, 1)
        self.spinBox_X = QtWidgets.QSpinBox(self.groupBox_Settings)
        self.spinBox_X.setMinimum(-524288)
        self.spinBox_X.setMaximum(524287)
        self.spinBox_X.setObjectName("spinBox_X")
        self.gridLayout_5.addWidget(self.spinBox_X, 0, 2, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.groupBox_Settings)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 1, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_Settings)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_Settings)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 2)
        self.pushButton_StepXMinus = QtWidgets.QPushButton(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_StepXMinus.sizePolicy().hasHeightForWidth())
        self.pushButton_StepXMinus.setSizePolicy(sizePolicy)
        self.pushButton_StepXMinus.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_StepXMinus.setToolTip("")
        self.pushButton_StepXMinus.setObjectName("pushButton_StepXMinus")
        self.gridLayout_5.addWidget(self.pushButton_StepXMinus, 1, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_Settings)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 2)
        self.pushButton_StepYMinus = QtWidgets.QPushButton(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_StepYMinus.sizePolicy().hasHeightForWidth())
        self.pushButton_StepYMinus.setSizePolicy(sizePolicy)
        self.pushButton_StepYMinus.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_StepYMinus.setToolTip("")
        self.pushButton_StepYMinus.setObjectName("pushButton_StepYMinus")
        self.gridLayout_5.addWidget(self.pushButton_StepYMinus, 1, 8, 1, 1)
        self.pushButton_GoToXY = QtWidgets.QPushButton(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_GoToXY.sizePolicy().hasHeightForWidth())
        self.pushButton_GoToXY.setSizePolicy(sizePolicy)
        self.pushButton_GoToXY.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton_GoToXY.setToolTip("")
        self.pushButton_GoToXY.setObjectName("pushButton_GoToXY")
        self.gridLayout_5.addWidget(self.pushButton_GoToXY, 0, 9, 1, 1)
        self.pushButton_StepXPlus = QtWidgets.QPushButton(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_StepXPlus.sizePolicy().hasHeightForWidth())
        self.pushButton_StepXPlus.setSizePolicy(sizePolicy)
        self.pushButton_StepXPlus.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_StepXPlus.setToolTip("")
        self.pushButton_StepXPlus.setObjectName("pushButton_StepXPlus")
        self.gridLayout_5.addWidget(self.pushButton_StepXPlus, 1, 3, 1, 1)
        self.spinBox_Y = QtWidgets.QSpinBox(self.groupBox_Settings)
        self.spinBox_Y.setMinimum(-524288)
        self.spinBox_Y.setMaximum(524287)
        self.spinBox_Y.setObjectName("spinBox_Y")
        self.gridLayout_5.addWidget(self.spinBox_Y, 0, 6, 1, 3)
        self.spinBox_StepY = QtWidgets.QSpinBox(self.groupBox_Settings)
        self.spinBox_StepY.setMinimum(1)
        self.spinBox_StepY.setMaximum(99999)
        self.spinBox_StepY.setObjectName("spinBox_StepY")
        self.gridLayout_5.addWidget(self.spinBox_StepY, 1, 6, 1, 1)
        self.pushButton_GoToOrigin = QtWidgets.QPushButton(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_GoToOrigin.sizePolicy().hasHeightForWidth())
        self.pushButton_GoToOrigin.setSizePolicy(sizePolicy)
        self.pushButton_GoToOrigin.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton_GoToOrigin.setToolTip("")
        self.pushButton_GoToOrigin.setObjectName("pushButton_GoToOrigin")
        self.gridLayout_5.addWidget(self.pushButton_GoToOrigin, 1, 9, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_5)
        self.verticalLayout.addWidget(self.groupBox_Settings)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(RTC6_Config_Window)
        QtCore.QMetaObject.connectSlotsByName(RTC6_Config_Window)

    def retranslateUi(self, RTC6_Config_Window):
        _translate = QtCore.QCoreApplication.translate
        RTC6_Config_Window.setWindowTitle(_translate("RTC6_Config_Window", "RTC6 Configuration"))
        self.groupBox_CONN.setTitle(_translate("RTC6_Config_Window", "RTC6 CONN"))
        self.pushButton_CONN_Open.setText(_translate("RTC6_Config_Window", "Open"))
        self.pushButton_PickConfigPath.setText(_translate("RTC6_Config_Window", "..."))
        self.label_6.setText(_translate("RTC6_Config_Window", "Conifg Path:"))
        self.lineEdit_ConfigPath.setPlaceholderText(_translate("RTC6_Config_Window", "RTC6OUT.out,RTC6RBF.rbf,RTC6DAT.dat"))
        self.label_7.setText(_translate("RTC6_Config_Window", "Conifg Path:"))
        self.lineEdit_CorFile.setPlaceholderText(_translate("RTC6_Config_Window", "Correction File, e.g. Cor_1to1.ct5"))
        self.pushButton_PickCorFile.setText(_translate("RTC6_Config_Window", "..."))
        self.groupBox_Settings.setTitle(_translate("RTC6_Config_Window", "RTC6 Settings"))
        self.pushButton_StepYPlus.setText(_translate("RTC6_Config_Window", "+"))
        self.label_5.setText(_translate("RTC6_Config_Window", "StepY:"))
        self.label_4.setText(_translate("RTC6_Config_Window", "Y:"))
        self.label_2.setText(_translate("RTC6_Config_Window", "X:"))
        self.pushButton_StepXMinus.setText(_translate("RTC6_Config_Window", "-"))
        self.label_3.setText(_translate("RTC6_Config_Window", "StepX:"))
        self.pushButton_StepYMinus.setText(_translate("RTC6_Config_Window", "-"))
        self.pushButton_GoToXY.setText(_translate("RTC6_Config_Window", "Go"))
        self.pushButton_StepXPlus.setText(_translate("RTC6_Config_Window", "+"))
        self.pushButton_GoToOrigin.setText(_translate("RTC6_Config_Window", "Orig."))
