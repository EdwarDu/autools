# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sr830_config.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SR830_Config_Window(object):
    def setupUi(self, SR830_Config_Window):
        SR830_Config_Window.setObjectName("SR830_Config_Window")
        SR830_Config_Window.resize(583, 767)
        self.verticalLayout = QtWidgets.QVBoxLayout(SR830_Config_Window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_CONN = QtWidgets.QGroupBox(SR830_Config_Window)
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
        self.comboBox_CONN = QtWidgets.QComboBox(self.groupBox_CONN)
        self.comboBox_CONN.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_CONN.sizePolicy().hasHeightForWidth())
        self.comboBox_CONN.setSizePolicy(sizePolicy)
        self.comboBox_CONN.setObjectName("comboBox_CONN")
        self.gridLayout.addWidget(self.comboBox_CONN, 1, 1, 1, 2)
        self.label_COM_Status = QtWidgets.QLabel(self.groupBox_CONN)
        self.label_COM_Status.setStyleSheet("background : red")
        self.label_COM_Status.setText("")
        self.label_COM_Status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_COM_Status.setObjectName("label_COM_Status")
        self.gridLayout.addWidget(self.label_COM_Status, 4, 0, 1, 1)
        self.pushButton_COM_Open = QtWidgets.QPushButton(self.groupBox_CONN)
        self.pushButton_COM_Open.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_COM_Open.setCheckable(True)
        self.pushButton_COM_Open.setFlat(False)
        self.pushButton_COM_Open.setObjectName("pushButton_COM_Open")
        self.gridLayout.addWidget(self.pushButton_COM_Open, 4, 2, 1, 1)
        self.comboBox_COM_Parity = QtWidgets.QComboBox(self.groupBox_CONN)
        self.comboBox_COM_Parity.setObjectName("comboBox_COM_Parity")
        self.comboBox_COM_Parity.addItem("")
        self.comboBox_COM_Parity.addItem("")
        self.comboBox_COM_Parity.addItem("")
        self.gridLayout.addWidget(self.comboBox_COM_Parity, 3, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.groupBox_CONN)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.pushButton_COM_Refresh = QtWidgets.QPushButton(self.groupBox_CONN)
        self.pushButton_COM_Refresh.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_COM_Refresh.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_COM_Refresh.setCheckable(False)
        self.pushButton_COM_Refresh.setObjectName("pushButton_COM_Refresh")
        self.gridLayout.addWidget(self.pushButton_COM_Refresh, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_CONN)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_CONN)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.comboBox_COM_BaudRate = QtWidgets.QComboBox(self.groupBox_CONN)
        self.comboBox_COM_BaudRate.setEditable(False)
        self.comboBox_COM_BaudRate.setObjectName("comboBox_COM_BaudRate")
        self.comboBox_COM_BaudRate.addItem("")
        self.comboBox_COM_BaudRate.addItem("")
        self.comboBox_COM_BaudRate.addItem("")
        self.comboBox_COM_BaudRate.addItem("")
        self.comboBox_COM_BaudRate.addItem("")
        self.gridLayout.addWidget(self.comboBox_COM_BaudRate, 2, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox_CONN)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.radioButton_Interf_GPIB = QtWidgets.QRadioButton(self.groupBox_CONN)
        self.radioButton_Interf_GPIB.setMinimumSize(QtCore.QSize(0, 0))
        self.radioButton_Interf_GPIB.setObjectName("radioButton_Interf_GPIB")
        self.gridLayout.addWidget(self.radioButton_Interf_GPIB, 0, 1, 1, 1)
        self.radioButton_Interf_RS232 = QtWidgets.QRadioButton(self.groupBox_CONN)
        self.radioButton_Interf_RS232.setMinimumSize(QtCore.QSize(0, 0))
        self.radioButton_Interf_RS232.setChecked(True)
        self.radioButton_Interf_RS232.setObjectName("radioButton_Interf_RS232")
        self.gridLayout.addWidget(self.radioButton_Interf_RS232, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox_CONN)
        self.groupBox_Settings = QtWidgets.QGroupBox(SR830_Config_Window)
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
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.groupBox_Settings)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 5, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.groupBox_Settings)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 9, 0, 1, 2)
        self.pushButton_GetAll = QtWidgets.QPushButton(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_GetAll.sizePolicy().hasHeightForWidth())
        self.pushButton_GetAll.setSizePolicy(sizePolicy)
        self.pushButton_GetAll.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_GetAll.setObjectName("pushButton_GetAll")
        self.gridLayout_5.addWidget(self.pushButton_GetAll, 12, 3, 1, 2)
        self.pushButton_GetY = QtWidgets.QPushButton(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_GetY.sizePolicy().hasHeightForWidth())
        self.pushButton_GetY.setSizePolicy(sizePolicy)
        self.pushButton_GetY.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_GetY.setToolTip("")
        self.pushButton_GetY.setObjectName("pushButton_GetY")
        self.gridLayout_5.addWidget(self.pushButton_GetY, 9, 4, 1, 1)
        self.comboBox_TimeConstant = QtWidgets.QComboBox(self.groupBox_Settings)
        self.comboBox_TimeConstant.setObjectName("comboBox_TimeConstant")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.comboBox_TimeConstant.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_TimeConstant, 0, 2, 1, 3)
        self.line = QtWidgets.QFrame(self.groupBox_Settings)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 7, 0, 1, 5)
        self.pushButton_SetHarmonic = QtWidgets.QPushButton(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SetHarmonic.sizePolicy().hasHeightForWidth())
        self.pushButton_SetHarmonic.setSizePolicy(sizePolicy)
        self.pushButton_SetHarmonic.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_SetHarmonic.setToolTip("")
        self.pushButton_SetHarmonic.setObjectName("pushButton_SetHarmonic")
        self.gridLayout_5.addWidget(self.pushButton_SetHarmonic, 6, 3, 1, 2)
        self.pushButton_GetTheta = QtWidgets.QPushButton(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_GetTheta.sizePolicy().hasHeightForWidth())
        self.pushButton_GetTheta.setSizePolicy(sizePolicy)
        self.pushButton_GetTheta.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_GetTheta.setToolTip("")
        self.pushButton_GetTheta.setObjectName("pushButton_GetTheta")
        self.gridLayout_5.addWidget(self.pushButton_GetTheta, 11, 4, 1, 1)
        self.lineEdit_Theta = QtWidgets.QLineEdit(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Theta.sizePolicy().hasHeightForWidth())
        self.lineEdit_Theta.setSizePolicy(sizePolicy)
        self.lineEdit_Theta.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_Theta.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_Theta.setObjectName("lineEdit_Theta")
        self.gridLayout_5.addWidget(self.lineEdit_Theta, 11, 2, 1, 2)
        self.comboBox_FilterSlope = QtWidgets.QComboBox(self.groupBox_Settings)
        self.comboBox_FilterSlope.setObjectName("comboBox_FilterSlope")
        self.comboBox_FilterSlope.addItem("")
        self.comboBox_FilterSlope.addItem("")
        self.comboBox_FilterSlope.addItem("")
        self.comboBox_FilterSlope.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_FilterSlope, 2, 2, 1, 3)
        self.radioButton_ref_src_external = QtWidgets.QRadioButton(self.groupBox_Settings)
        self.radioButton_ref_src_external.setMinimumSize(QtCore.QSize(0, 0))
        self.radioButton_ref_src_external.setObjectName("radioButton_ref_src_external")
        self.gridLayout_5.addWidget(self.radioButton_ref_src_external, 4, 2, 1, 1)
        self.pushButton_SetPhase = QtWidgets.QPushButton(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SetPhase.sizePolicy().hasHeightForWidth())
        self.pushButton_SetPhase.setSizePolicy(sizePolicy)
        self.pushButton_SetPhase.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_SetPhase.setToolTip("")
        self.pushButton_SetPhase.setObjectName("pushButton_SetPhase")
        self.gridLayout_5.addWidget(self.pushButton_SetPhase, 3, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_Frequency = QtWidgets.QLineEdit(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Frequency.sizePolicy().hasHeightForWidth())
        self.lineEdit_Frequency.setSizePolicy(sizePolicy)
        self.lineEdit_Frequency.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_Frequency.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_Frequency.setObjectName("lineEdit_Frequency")
        self.gridLayout_5.addWidget(self.lineEdit_Frequency, 5, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_Settings)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 2, QtCore.Qt.AlignRight)
        self.comboBox_Sensitivity = QtWidgets.QComboBox(self.groupBox_Settings)
        self.comboBox_Sensitivity.setObjectName("comboBox_Sensitivity")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.comboBox_Sensitivity.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_Sensitivity, 1, 2, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.groupBox_Settings)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 3, 0, 1, 2, QtCore.Qt.AlignRight)
        self.label_14 = QtWidgets.QLabel(self.groupBox_Settings)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 6, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.groupBox_Settings)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 4, 0, 1, 2, QtCore.Qt.AlignRight)
        self.pushButton_GetFrequency = QtWidgets.QPushButton(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_GetFrequency.sizePolicy().hasHeightForWidth())
        self.pushButton_GetFrequency.setSizePolicy(sizePolicy)
        self.pushButton_GetFrequency.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_GetFrequency.setToolTip("")
        self.pushButton_GetFrequency.setObjectName("pushButton_GetFrequency")
        self.gridLayout_5.addWidget(self.pushButton_GetFrequency, 5, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_Settings)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 8, 0, 1, 2)
        self.pushButton_Autophase = QtWidgets.QPushButton(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Autophase.sizePolicy().hasHeightForWidth())
        self.pushButton_Autophase.setSizePolicy(sizePolicy)
        self.pushButton_Autophase.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_Autophase.setToolTip("")
        self.pushButton_Autophase.setObjectName("pushButton_Autophase")
        self.gridLayout_5.addWidget(self.pushButton_Autophase, 3, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_GetR = QtWidgets.QPushButton(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_GetR.sizePolicy().hasHeightForWidth())
        self.pushButton_GetR.setSizePolicy(sizePolicy)
        self.pushButton_GetR.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_GetR.setToolTip("")
        self.pushButton_GetR.setObjectName("pushButton_GetR")
        self.gridLayout_5.addWidget(self.pushButton_GetR, 10, 4, 1, 1)
        self.lineEdit_phase = QtWidgets.QLineEdit(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_phase.sizePolicy().hasHeightForWidth())
        self.lineEdit_phase.setSizePolicy(sizePolicy)
        self.lineEdit_phase.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_phase.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_phase.setObjectName("lineEdit_phase")
        self.gridLayout_5.addWidget(self.lineEdit_phase, 3, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_Settings)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 11, 0, 1, 2)
        self.radioButton_ref_src_internal = QtWidgets.QRadioButton(self.groupBox_Settings)
        self.radioButton_ref_src_internal.setMinimumSize(QtCore.QSize(0, 0))
        self.radioButton_ref_src_internal.setObjectName("radioButton_ref_src_internal")
        self.gridLayout_5.addWidget(self.radioButton_ref_src_internal, 4, 3, 1, 2)
        self.lineEdit_R = QtWidgets.QLineEdit(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_R.sizePolicy().hasHeightForWidth())
        self.lineEdit_R.setSizePolicy(sizePolicy)
        self.lineEdit_R.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_R.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_R.setObjectName("lineEdit_R")
        self.gridLayout_5.addWidget(self.lineEdit_R, 10, 2, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.groupBox_Settings)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 2, 0, 1, 2)
        self.pushButton_GetX = QtWidgets.QPushButton(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_GetX.sizePolicy().hasHeightForWidth())
        self.pushButton_GetX.setSizePolicy(sizePolicy)
        self.pushButton_GetX.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_GetX.setToolTip("")
        self.pushButton_GetX.setObjectName("pushButton_GetX")
        self.gridLayout_5.addWidget(self.pushButton_GetX, 8, 4, 1, 1)
        self.spinBox_Harmonic = QtWidgets.QSpinBox(self.groupBox_Settings)
        self.spinBox_Harmonic.setKeyboardTracking(False)
        self.spinBox_Harmonic.setMinimum(1)
        self.spinBox_Harmonic.setMaximum(19999)
        self.spinBox_Harmonic.setObjectName("spinBox_Harmonic")
        self.gridLayout_5.addWidget(self.spinBox_Harmonic, 6, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_Settings)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 10, 0, 1, 2)
        self.lineEdit_X = QtWidgets.QLineEdit(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_X.sizePolicy().hasHeightForWidth())
        self.lineEdit_X.setSizePolicy(sizePolicy)
        self.lineEdit_X.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_X.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_X.setObjectName("lineEdit_X")
        self.gridLayout_5.addWidget(self.lineEdit_X, 8, 2, 1, 2)
        self.lineEdit_Y = QtWidgets.QLineEdit(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Y.sizePolicy().hasHeightForWidth())
        self.lineEdit_Y.setSizePolicy(sizePolicy)
        self.lineEdit_Y.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_Y.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_Y.setObjectName("lineEdit_Y")
        self.gridLayout_5.addWidget(self.lineEdit_Y, 9, 2, 1, 2)
        self.pushButton_SetFrequency = QtWidgets.QPushButton(self.groupBox_Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SetFrequency.sizePolicy().hasHeightForWidth())
        self.pushButton_SetFrequency.setSizePolicy(sizePolicy)
        self.pushButton_SetFrequency.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_SetFrequency.setToolTip("")
        self.pushButton_SetFrequency.setObjectName("pushButton_SetFrequency")
        self.gridLayout_5.addWidget(self.pushButton_SetFrequency, 5, 4, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_5)
        self.verticalLayout.addWidget(self.groupBox_Settings)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(SR830_Config_Window)
        self.comboBox_COM_Parity.setCurrentIndex(1)
        self.comboBox_COM_BaudRate.setCurrentIndex(1)
        self.comboBox_TimeConstant.setCurrentIndex(10)
        self.comboBox_FilterSlope.setCurrentIndex(0)
        self.comboBox_Sensitivity.setCurrentIndex(10)
        QtCore.QMetaObject.connectSlotsByName(SR830_Config_Window)
        SR830_Config_Window.setTabOrder(self.radioButton_Interf_GPIB, self.radioButton_Interf_RS232)
        SR830_Config_Window.setTabOrder(self.radioButton_Interf_RS232, self.comboBox_CONN)
        SR830_Config_Window.setTabOrder(self.comboBox_CONN, self.comboBox_COM_BaudRate)
        SR830_Config_Window.setTabOrder(self.comboBox_COM_BaudRate, self.comboBox_COM_Parity)
        SR830_Config_Window.setTabOrder(self.comboBox_COM_Parity, self.pushButton_COM_Refresh)
        SR830_Config_Window.setTabOrder(self.pushButton_COM_Refresh, self.pushButton_COM_Open)
        SR830_Config_Window.setTabOrder(self.pushButton_COM_Open, self.comboBox_TimeConstant)
        SR830_Config_Window.setTabOrder(self.comboBox_TimeConstant, self.comboBox_Sensitivity)
        SR830_Config_Window.setTabOrder(self.comboBox_Sensitivity, self.comboBox_FilterSlope)
        SR830_Config_Window.setTabOrder(self.comboBox_FilterSlope, self.lineEdit_phase)
        SR830_Config_Window.setTabOrder(self.lineEdit_phase, self.pushButton_SetPhase)
        SR830_Config_Window.setTabOrder(self.pushButton_SetPhase, self.pushButton_Autophase)
        SR830_Config_Window.setTabOrder(self.pushButton_Autophase, self.radioButton_ref_src_external)
        SR830_Config_Window.setTabOrder(self.radioButton_ref_src_external, self.radioButton_ref_src_internal)
        SR830_Config_Window.setTabOrder(self.radioButton_ref_src_internal, self.lineEdit_Frequency)
        SR830_Config_Window.setTabOrder(self.lineEdit_Frequency, self.pushButton_GetFrequency)
        SR830_Config_Window.setTabOrder(self.pushButton_GetFrequency, self.pushButton_SetFrequency)
        SR830_Config_Window.setTabOrder(self.pushButton_SetFrequency, self.spinBox_Harmonic)
        SR830_Config_Window.setTabOrder(self.spinBox_Harmonic, self.pushButton_SetHarmonic)
        SR830_Config_Window.setTabOrder(self.pushButton_SetHarmonic, self.lineEdit_X)
        SR830_Config_Window.setTabOrder(self.lineEdit_X, self.pushButton_GetX)
        SR830_Config_Window.setTabOrder(self.pushButton_GetX, self.lineEdit_Y)
        SR830_Config_Window.setTabOrder(self.lineEdit_Y, self.pushButton_GetY)
        SR830_Config_Window.setTabOrder(self.pushButton_GetY, self.lineEdit_R)
        SR830_Config_Window.setTabOrder(self.lineEdit_R, self.pushButton_GetR)
        SR830_Config_Window.setTabOrder(self.pushButton_GetR, self.lineEdit_Theta)
        SR830_Config_Window.setTabOrder(self.lineEdit_Theta, self.pushButton_GetTheta)
        SR830_Config_Window.setTabOrder(self.pushButton_GetTheta, self.pushButton_GetAll)

    def retranslateUi(self, SR830_Config_Window):
        _translate = QtCore.QCoreApplication.translate
        SR830_Config_Window.setWindowTitle(_translate("SR830_Config_Window", "SR830 Configuration"))
        self.groupBox_CONN.setTitle(_translate("SR830_Config_Window", "SR830 COM"))
        self.pushButton_COM_Open.setText(_translate("SR830_Config_Window", "Open"))
        self.comboBox_COM_Parity.setCurrentText(_translate("SR830_Config_Window", "ODD"))
        self.comboBox_COM_Parity.setItemText(0, _translate("SR830_Config_Window", "None"))
        self.comboBox_COM_Parity.setItemText(1, _translate("SR830_Config_Window", "ODD"))
        self.comboBox_COM_Parity.setItemText(2, _translate("SR830_Config_Window", "EVEN"))
        self.label_7.setText(_translate("SR830_Config_Window", "Parity:"))
        self.pushButton_COM_Refresh.setText(_translate("SR830_Config_Window", "Refresh"))
        self.label.setText(_translate("SR830_Config_Window", "CONN:"))
        self.label_6.setText(_translate("SR830_Config_Window", "BaudRate:"))
        self.comboBox_COM_BaudRate.setCurrentText(_translate("SR830_Config_Window", "19200"))
        self.comboBox_COM_BaudRate.setItemText(0, _translate("SR830_Config_Window", "9600"))
        self.comboBox_COM_BaudRate.setItemText(1, _translate("SR830_Config_Window", "19200"))
        self.comboBox_COM_BaudRate.setItemText(2, _translate("SR830_Config_Window", "38400"))
        self.comboBox_COM_BaudRate.setItemText(3, _translate("SR830_Config_Window", "57600"))
        self.comboBox_COM_BaudRate.setItemText(4, _translate("SR830_Config_Window", "115200"))
        self.label_4.setText(_translate("SR830_Config_Window", "Interface:"))
        self.radioButton_Interf_GPIB.setText(_translate("SR830_Config_Window", "&GPIB"))
        self.radioButton_Interf_RS232.setText(_translate("SR830_Config_Window", "RS&232"))
        self.groupBox_Settings.setTitle(_translate("SR830_Config_Window", "SR830 Settings"))
        self.label_2.setText(_translate("SR830_Config_Window", "Time Const.:"))
        self.label_16.setText(_translate("SR830_Config_Window", "Frequency:"))
        self.label_11.setText(_translate("SR830_Config_Window", "Y:"))
        self.pushButton_GetAll.setToolTip(_translate("SR830_Config_Window", "Get X, Y, R, Theta, F"))
        self.pushButton_GetAll.setText(_translate("SR830_Config_Window", "GetAll"))
        self.pushButton_GetY.setText(_translate("SR830_Config_Window", "Get"))
        self.comboBox_TimeConstant.setItemText(0, _translate("SR830_Config_Window", "10 us"))
        self.comboBox_TimeConstant.setItemText(1, _translate("SR830_Config_Window", "30 us"))
        self.comboBox_TimeConstant.setItemText(2, _translate("SR830_Config_Window", "100 us"))
        self.comboBox_TimeConstant.setItemText(3, _translate("SR830_Config_Window", "300 us"))
        self.comboBox_TimeConstant.setItemText(4, _translate("SR830_Config_Window", "1 ms"))
        self.comboBox_TimeConstant.setItemText(5, _translate("SR830_Config_Window", "3 ms"))
        self.comboBox_TimeConstant.setItemText(6, _translate("SR830_Config_Window", "10 ms"))
        self.comboBox_TimeConstant.setItemText(7, _translate("SR830_Config_Window", "30 ms"))
        self.comboBox_TimeConstant.setItemText(8, _translate("SR830_Config_Window", "100 ms"))
        self.comboBox_TimeConstant.setItemText(9, _translate("SR830_Config_Window", "300 ms"))
        self.comboBox_TimeConstant.setItemText(10, _translate("SR830_Config_Window", "1 s"))
        self.comboBox_TimeConstant.setItemText(11, _translate("SR830_Config_Window", "3 s"))
        self.comboBox_TimeConstant.setItemText(12, _translate("SR830_Config_Window", "10 s"))
        self.comboBox_TimeConstant.setItemText(13, _translate("SR830_Config_Window", "30 s"))
        self.comboBox_TimeConstant.setItemText(14, _translate("SR830_Config_Window", "100 s"))
        self.comboBox_TimeConstant.setItemText(15, _translate("SR830_Config_Window", "300 s"))
        self.comboBox_TimeConstant.setItemText(16, _translate("SR830_Config_Window", "1 ks"))
        self.comboBox_TimeConstant.setItemText(17, _translate("SR830_Config_Window", "3 ks"))
        self.comboBox_TimeConstant.setItemText(18, _translate("SR830_Config_Window", "10 ks"))
        self.comboBox_TimeConstant.setItemText(19, _translate("SR830_Config_Window", "30 ks"))
        self.pushButton_SetHarmonic.setText(_translate("SR830_Config_Window", "Set"))
        self.pushButton_GetTheta.setText(_translate("SR830_Config_Window", "Get"))
        self.lineEdit_Theta.setToolTip(_translate("SR830_Config_Window", "SR830 Phase (float)"))
        self.comboBox_FilterSlope.setItemText(0, _translate("SR830_Config_Window", "6 dB/oct"))
        self.comboBox_FilterSlope.setItemText(1, _translate("SR830_Config_Window", "12 dB/oct"))
        self.comboBox_FilterSlope.setItemText(2, _translate("SR830_Config_Window", "18 dB/oct"))
        self.comboBox_FilterSlope.setItemText(3, _translate("SR830_Config_Window", "24 dB/oct"))
        self.radioButton_ref_src_external.setText(_translate("SR830_Config_Window", "E&xternal"))
        self.pushButton_SetPhase.setText(_translate("SR830_Config_Window", "Set"))
        self.lineEdit_Frequency.setToolTip(_translate("SR830_Config_Window", "SR830 Phase (float)"))
        self.label_3.setText(_translate("SR830_Config_Window", "Sensitivity:"))
        self.comboBox_Sensitivity.setItemText(0, _translate("SR830_Config_Window", "2 nV/fA"))
        self.comboBox_Sensitivity.setItemText(1, _translate("SR830_Config_Window", "5 nV/fA"))
        self.comboBox_Sensitivity.setItemText(2, _translate("SR830_Config_Window", "2 nV/fA"))
        self.comboBox_Sensitivity.setItemText(3, _translate("SR830_Config_Window", "5 nV/fA"))
        self.comboBox_Sensitivity.setItemText(4, _translate("SR830_Config_Window", "10 nV/fA"))
        self.comboBox_Sensitivity.setItemText(5, _translate("SR830_Config_Window", "20 nV/fA"))
        self.comboBox_Sensitivity.setItemText(6, _translate("SR830_Config_Window", "50 nV/fA"))
        self.comboBox_Sensitivity.setItemText(7, _translate("SR830_Config_Window", "100 nV/fA"))
        self.comboBox_Sensitivity.setItemText(8, _translate("SR830_Config_Window", "200 nV/fA"))
        self.comboBox_Sensitivity.setItemText(9, _translate("SR830_Config_Window", "500 nV/fA"))
        self.comboBox_Sensitivity.setItemText(10, _translate("SR830_Config_Window", "1 uV/pA"))
        self.comboBox_Sensitivity.setItemText(11, _translate("SR830_Config_Window", "2 uV/pA"))
        self.comboBox_Sensitivity.setItemText(12, _translate("SR830_Config_Window", "5 uV/pA"))
        self.comboBox_Sensitivity.setItemText(13, _translate("SR830_Config_Window", "10 uV/pA"))
        self.comboBox_Sensitivity.setItemText(14, _translate("SR830_Config_Window", "20 uV/pA"))
        self.comboBox_Sensitivity.setItemText(15, _translate("SR830_Config_Window", "50 uV/pA"))
        self.comboBox_Sensitivity.setItemText(16, _translate("SR830_Config_Window", "100 uV/pA"))
        self.comboBox_Sensitivity.setItemText(17, _translate("SR830_Config_Window", "200 uV/pA"))
        self.comboBox_Sensitivity.setItemText(18, _translate("SR830_Config_Window", "500 uV/pA"))
        self.comboBox_Sensitivity.setItemText(19, _translate("SR830_Config_Window", "1 mV/nA"))
        self.comboBox_Sensitivity.setItemText(20, _translate("SR830_Config_Window", "2 mV/nA"))
        self.comboBox_Sensitivity.setItemText(21, _translate("SR830_Config_Window", "5 mV/nA"))
        self.comboBox_Sensitivity.setItemText(22, _translate("SR830_Config_Window", "10 mV/nA"))
        self.comboBox_Sensitivity.setItemText(23, _translate("SR830_Config_Window", "20 mV/nA"))
        self.comboBox_Sensitivity.setItemText(24, _translate("SR830_Config_Window", "50 mV/nA"))
        self.comboBox_Sensitivity.setItemText(25, _translate("SR830_Config_Window", "100 mV/nA"))
        self.comboBox_Sensitivity.setItemText(26, _translate("SR830_Config_Window", "200 mV/nA"))
        self.comboBox_Sensitivity.setItemText(27, _translate("SR830_Config_Window", "500 mV/nA"))
        self.comboBox_Sensitivity.setItemText(28, _translate("SR830_Config_Window", "1 V/uA"))
        self.label_8.setText(_translate("SR830_Config_Window", "Phase:"))
        self.label_14.setText(_translate("SR830_Config_Window", "Harmonic:"))
        self.label_9.setText(_translate("SR830_Config_Window", "Ref Source:"))
        self.pushButton_GetFrequency.setText(_translate("SR830_Config_Window", "Get"))
        self.label_10.setText(_translate("SR830_Config_Window", "X:"))
        self.pushButton_Autophase.setText(_translate("SR830_Config_Window", "Auto"))
        self.pushButton_GetR.setText(_translate("SR830_Config_Window", "Get"))
        self.lineEdit_phase.setToolTip(_translate("SR830_Config_Window", "SR830 Phase (float)"))
        self.label_12.setText(_translate("SR830_Config_Window", "Theta:"))
        self.radioButton_ref_src_internal.setText(_translate("SR830_Config_Window", "I&nternal"))
        self.lineEdit_R.setToolTip(_translate("SR830_Config_Window", "SR830 Phase (float)"))
        self.label_15.setText(_translate("SR830_Config_Window", "Filter Slope:"))
        self.pushButton_GetX.setText(_translate("SR830_Config_Window", "Get"))
        self.label_13.setText(_translate("SR830_Config_Window", "R:"))
        self.lineEdit_X.setToolTip(_translate("SR830_Config_Window", "SR830 Phase (float)"))
        self.lineEdit_Y.setToolTip(_translate("SR830_Config_Window", "SR830 Phase (float)"))
        self.pushButton_SetFrequency.setText(_translate("SR830_Config_Window", "Set"))
