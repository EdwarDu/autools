# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup_main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetupMainWindow(object):
    def setupUi(self, SetupMainWindow):
        SetupMainWindow.setObjectName("SetupMainWindow")
        SetupMainWindow.resize(2006, 1177)
        self.centralwidget = QtWidgets.QWidget(SetupMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 253, 985))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(6, 0, 6, 0)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_SR830 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_SR830.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_SR830.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_SR830.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_SR830.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_SR830.setObjectName("groupBox_SR830")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_SR830)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_SR830_Conn_Status = QtWidgets.QLabel(self.groupBox_SR830)
        self.label_SR830_Conn_Status.setStyleSheet("background: red\n"
"")
        self.label_SR830_Conn_Status.setText("")
        self.label_SR830_Conn_Status.setObjectName("label_SR830_Conn_Status")
        self.horizontalLayout_5.addWidget(self.label_SR830_Conn_Status)
        self.pushButton_SR830_Config = QtWidgets.QPushButton(self.groupBox_SR830)
        self.pushButton_SR830_Config.setObjectName("pushButton_SR830_Config")
        self.horizontalLayout_5.addWidget(self.pushButton_SR830_Config)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_SR830_Theta = QtWidgets.QLabel(self.groupBox_SR830)
        self.label_SR830_Theta.setText("")
        self.label_SR830_Theta.setObjectName("label_SR830_Theta")
        self.gridLayout.addWidget(self.label_SR830_Theta, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_SR830)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_SR830)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_SR830_Y = QtWidgets.QLabel(self.groupBox_SR830)
        self.label_SR830_Y.setText("")
        self.label_SR830_Y.setObjectName("label_SR830_Y")
        self.gridLayout.addWidget(self.label_SR830_Y, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_SR830)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_SR830)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 0, 1, 1)
        self.label_SR830_R = QtWidgets.QLabel(self.groupBox_SR830)
        self.label_SR830_R.setText("")
        self.label_SR830_R.setObjectName("label_SR830_R")
        self.gridLayout.addWidget(self.label_SR830_R, 2, 1, 1, 1)
        self.label_SR830_X = QtWidgets.QLabel(self.groupBox_SR830)
        self.label_SR830_X.setText("")
        self.label_SR830_X.setObjectName("label_SR830_X")
        self.gridLayout.addWidget(self.label_SR830_X, 0, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.groupBox_SR830)
        self.label_29.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 4, 0, 1, 1)
        self.label_SR380_RefFreq = QtWidgets.QLabel(self.groupBox_SR830)
        self.label_SR380_RefFreq.setText("")
        self.label_SR380_RefFreq.setObjectName("label_SR380_RefFreq")
        self.gridLayout.addWidget(self.label_SR380_RefFreq, 4, 1, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox_SR830)
        self.groupBox_NIDaq = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_NIDaq.setObjectName("groupBox_NIDaq")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_NIDaq)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_NIDAQ_Conn_Status = QtWidgets.QLabel(self.groupBox_NIDaq)
        self.label_NIDAQ_Conn_Status.setStyleSheet("background: red\n"
"")
        self.label_NIDAQ_Conn_Status.setText("")
        self.label_NIDAQ_Conn_Status.setObjectName("label_NIDAQ_Conn_Status")
        self.horizontalLayout_9.addWidget(self.label_NIDAQ_Conn_Status)
        self.pushButton_NIDAQ_Config = QtWidgets.QPushButton(self.groupBox_NIDaq)
        self.pushButton_NIDAQ_Config.setObjectName("pushButton_NIDAQ_Config")
        self.horizontalLayout_9.addWidget(self.pushButton_NIDAQ_Config)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.verticalLayout.addWidget(self.groupBox_NIDaq)
        self.groupBox_PiezoStage = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_PiezoStage.setObjectName("groupBox_PiezoStage")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_PiezoStage)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_Piezo_Conn_Status = QtWidgets.QLabel(self.groupBox_PiezoStage)
        self.label_Piezo_Conn_Status.setStyleSheet("background: red\n"
"")
        self.label_Piezo_Conn_Status.setObjectName("label_Piezo_Conn_Status")
        self.horizontalLayout_8.addWidget(self.label_Piezo_Conn_Status)
        self.pushButton_Piezo_Config = QtWidgets.QPushButton(self.groupBox_PiezoStage)
        self.pushButton_Piezo_Config.setEnabled(False)
        self.pushButton_Piezo_Config.setObjectName("pushButton_Piezo_Config")
        self.horizontalLayout_8.addWidget(self.pushButton_Piezo_Config)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_10 = QtWidgets.QLabel(self.groupBox_PiezoStage)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_Piezo_X = QtWidgets.QLabel(self.groupBox_PiezoStage)
        self.label_Piezo_X.setText("")
        self.label_Piezo_X.setObjectName("label_Piezo_X")
        self.gridLayout_4.addWidget(self.label_Piezo_X, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_PiezoStage)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_Piezo_Y = QtWidgets.QLabel(self.groupBox_PiezoStage)
        self.label_Piezo_Y.setText("")
        self.label_Piezo_Y.setObjectName("label_Piezo_Y")
        self.gridLayout_4.addWidget(self.label_Piezo_Y, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_PiezoStage)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_Piezo_Z = QtWidgets.QLabel(self.groupBox_PiezoStage)
        self.label_Piezo_Z.setText("")
        self.label_Piezo_Z.setObjectName("label_Piezo_Z")
        self.gridLayout_4.addWidget(self.label_Piezo_Z, 2, 1, 1, 1)
        self.verticalLayout_11.addLayout(self.gridLayout_4)
        self.verticalLayout.addWidget(self.groupBox_PiezoStage)
        self.pushButton_SaveSettings = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_SaveSettings.setObjectName("pushButton_SaveSettings")
        self.verticalLayout.addWidget(self.pushButton_SaveSettings)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout.setStretch(4, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_7.addWidget(self.scrollArea)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_MapMeasurements = QtWidgets.QWidget()
        self.tab_MapMeasurements.setObjectName("tab_MapMeasurements")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_MapMeasurements)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.gridLayout_MapM_Run = QtWidgets.QGridLayout()
        self.gridLayout_MapM_Run.setObjectName("gridLayout_MapM_Run")
        self.lineEdit_MapM_YStep = QtWidgets.QLineEdit(self.tab_MapMeasurements)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_MapM_YStep.sizePolicy().hasHeightForWidth())
        self.lineEdit_MapM_YStep.setSizePolicy(sizePolicy)
        self.lineEdit_MapM_YStep.setMaximumSize(QtCore.QSize(140, 16777215))
        self.lineEdit_MapM_YStep.setReadOnly(True)
        self.lineEdit_MapM_YStep.setObjectName("lineEdit_MapM_YStep")
        self.gridLayout_MapM_Run.addWidget(self.lineEdit_MapM_YStep, 1, 9, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.tab_MapMeasurements)
        self.label_46.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.gridLayout_MapM_Run.addWidget(self.label_46, 0, 4, 1, 1)
        self.label_68 = QtWidgets.QLabel(self.tab_MapMeasurements)
        self.label_68.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_68.setObjectName("label_68")
        self.gridLayout_MapM_Run.addWidget(self.label_68, 0, 6, 1, 1)
        self.spinBox_MapM_YSamples = QtWidgets.QSpinBox(self.tab_MapMeasurements)
        self.spinBox_MapM_YSamples.setKeyboardTracking(False)
        self.spinBox_MapM_YSamples.setMinimum(2)
        self.spinBox_MapM_YSamples.setMaximum(201)
        self.spinBox_MapM_YSamples.setSingleStep(1)
        self.spinBox_MapM_YSamples.setProperty("value", 11)
        self.spinBox_MapM_YSamples.setObjectName("spinBox_MapM_YSamples")
        self.gridLayout_MapM_Run.addWidget(self.spinBox_MapM_YSamples, 1, 7, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.tab_MapMeasurements)
        self.label_71.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_71.setObjectName("label_71")
        self.gridLayout_MapM_Run.addWidget(self.label_71, 1, 8, 1, 1)
        self.lineEdit_MapM_LockInX = QtWidgets.QLineEdit(self.tab_MapMeasurements)
        self.lineEdit_MapM_LockInX.setReadOnly(True)
        self.lineEdit_MapM_LockInX.setObjectName("lineEdit_MapM_LockInX")
        self.gridLayout_MapM_Run.addWidget(self.lineEdit_MapM_LockInX, 0, 12, 1, 1)
        self.label_72 = QtWidgets.QLabel(self.tab_MapMeasurements)
        self.label_72.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_72.setObjectName("label_72")
        self.gridLayout_MapM_Run.addWidget(self.label_72, 0, 11, 1, 1)
        self.pushButton_MapM_GoY0 = QtWidgets.QPushButton(self.tab_MapMeasurements)
        self.pushButton_MapM_GoY0.setObjectName("pushButton_MapM_GoY0")
        self.gridLayout_MapM_Run.addWidget(self.pushButton_MapM_GoY0, 1, 10, 1, 1)
        self.pushButton_MapM_GoX0 = QtWidgets.QPushButton(self.tab_MapMeasurements)
        self.pushButton_MapM_GoX0.setObjectName("pushButton_MapM_GoX0")
        self.gridLayout_MapM_Run.addWidget(self.pushButton_MapM_GoX0, 0, 10, 1, 1)
        self.doubleSpinBox_MapM_X1 = QtWidgets.QDoubleSpinBox(self.tab_MapMeasurements)
        self.doubleSpinBox_MapM_X1.setKeyboardTracking(False)
        self.doubleSpinBox_MapM_X1.setDecimals(6)
        self.doubleSpinBox_MapM_X1.setMinimum(-200.0)
        self.doubleSpinBox_MapM_X1.setMaximum(200.0)
        self.doubleSpinBox_MapM_X1.setSingleStep(0.01)
        self.doubleSpinBox_MapM_X1.setObjectName("doubleSpinBox_MapM_X1")
        self.gridLayout_MapM_Run.addWidget(self.doubleSpinBox_MapM_X1, 0, 5, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.tab_MapMeasurements)
        self.label_45.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_45.setObjectName("label_45")
        self.gridLayout_MapM_Run.addWidget(self.label_45, 0, 0, 1, 2)
        self.label_73 = QtWidgets.QLabel(self.tab_MapMeasurements)
        self.label_73.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_73.setObjectName("label_73")
        self.gridLayout_MapM_Run.addWidget(self.label_73, 1, 11, 1, 1)
        self.doubleSpinBox_MapM_X0 = QtWidgets.QDoubleSpinBox(self.tab_MapMeasurements)
        self.doubleSpinBox_MapM_X0.setKeyboardTracking(False)
        self.doubleSpinBox_MapM_X0.setDecimals(6)
        self.doubleSpinBox_MapM_X0.setMinimum(-200.0)
        self.doubleSpinBox_MapM_X0.setMaximum(200.0)
        self.doubleSpinBox_MapM_X0.setSingleStep(0.01)
        self.doubleSpinBox_MapM_X0.setObjectName("doubleSpinBox_MapM_X0")
        self.gridLayout_MapM_Run.addWidget(self.doubleSpinBox_MapM_X0, 0, 2, 1, 2)
        self.lineEdit_MapM_XStep = QtWidgets.QLineEdit(self.tab_MapMeasurements)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_MapM_XStep.sizePolicy().hasHeightForWidth())
        self.lineEdit_MapM_XStep.setSizePolicy(sizePolicy)
        self.lineEdit_MapM_XStep.setMaximumSize(QtCore.QSize(140, 16777215))
        self.lineEdit_MapM_XStep.setReadOnly(True)
        self.lineEdit_MapM_XStep.setObjectName("lineEdit_MapM_XStep")
        self.gridLayout_MapM_Run.addWidget(self.lineEdit_MapM_XStep, 0, 9, 1, 1)
        self.doubleSpinBox_MapM_Y0 = QtWidgets.QDoubleSpinBox(self.tab_MapMeasurements)
        self.doubleSpinBox_MapM_Y0.setKeyboardTracking(False)
        self.doubleSpinBox_MapM_Y0.setDecimals(6)
        self.doubleSpinBox_MapM_Y0.setMinimum(-200.0)
        self.doubleSpinBox_MapM_Y0.setMaximum(200.0)
        self.doubleSpinBox_MapM_Y0.setSingleStep(0.01)
        self.doubleSpinBox_MapM_Y0.setObjectName("doubleSpinBox_MapM_Y0")
        self.gridLayout_MapM_Run.addWidget(self.doubleSpinBox_MapM_Y0, 1, 2, 1, 2)
        self.lineEdit_MapM_LockInY = QtWidgets.QLineEdit(self.tab_MapMeasurements)
        self.lineEdit_MapM_LockInY.setReadOnly(True)
        self.lineEdit_MapM_LockInY.setObjectName("lineEdit_MapM_LockInY")
        self.gridLayout_MapM_Run.addWidget(self.lineEdit_MapM_LockInY, 1, 12, 1, 1)
        self.spinBox_MapM_XSamples = QtWidgets.QSpinBox(self.tab_MapMeasurements)
        self.spinBox_MapM_XSamples.setKeyboardTracking(False)
        self.spinBox_MapM_XSamples.setMinimum(2)
        self.spinBox_MapM_XSamples.setMaximum(201)
        self.spinBox_MapM_XSamples.setSingleStep(1)
        self.spinBox_MapM_XSamples.setProperty("value", 11)
        self.spinBox_MapM_XSamples.setObjectName("spinBox_MapM_XSamples")
        self.gridLayout_MapM_Run.addWidget(self.spinBox_MapM_XSamples, 0, 7, 1, 1)
        self.label_70 = QtWidgets.QLabel(self.tab_MapMeasurements)
        self.label_70.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_70.setObjectName("label_70")
        self.gridLayout_MapM_Run.addWidget(self.label_70, 0, 8, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.tab_MapMeasurements)
        self.label_47.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        self.gridLayout_MapM_Run.addWidget(self.label_47, 1, 4, 1, 1)
        self.label_64 = QtWidgets.QLabel(self.tab_MapMeasurements)
        self.label_64.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_64.setObjectName("label_64")
        self.gridLayout_MapM_Run.addWidget(self.label_64, 0, 13, 1, 1)
        self.comboBox_MapM_NIDAQChX = QtWidgets.QComboBox(self.tab_MapMeasurements)
        self.comboBox_MapM_NIDAQChX.setObjectName("comboBox_MapM_NIDAQChX")
        self.gridLayout_MapM_Run.addWidget(self.comboBox_MapM_NIDAQChX, 0, 14, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.tab_MapMeasurements)
        self.label_44.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_44.setObjectName("label_44")
        self.gridLayout_MapM_Run.addWidget(self.label_44, 1, 0, 1, 2)
        self.label_69 = QtWidgets.QLabel(self.tab_MapMeasurements)
        self.label_69.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_69.setObjectName("label_69")
        self.gridLayout_MapM_Run.addWidget(self.label_69, 1, 6, 1, 1)
        self.doubleSpinBox_MapM_Y1 = QtWidgets.QDoubleSpinBox(self.tab_MapMeasurements)
        self.doubleSpinBox_MapM_Y1.setKeyboardTracking(False)
        self.doubleSpinBox_MapM_Y1.setDecimals(6)
        self.doubleSpinBox_MapM_Y1.setMinimum(-200.0)
        self.doubleSpinBox_MapM_Y1.setMaximum(200.0)
        self.doubleSpinBox_MapM_Y1.setSingleStep(0.01)
        self.doubleSpinBox_MapM_Y1.setObjectName("doubleSpinBox_MapM_Y1")
        self.gridLayout_MapM_Run.addWidget(self.doubleSpinBox_MapM_Y1, 1, 5, 1, 1)
        self.lineEdit_MapM_NiVolX = QtWidgets.QLineEdit(self.tab_MapMeasurements)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_MapM_NiVolX.sizePolicy().hasHeightForWidth())
        self.lineEdit_MapM_NiVolX.setSizePolicy(sizePolicy)
        self.lineEdit_MapM_NiVolX.setMaximumSize(QtCore.QSize(160, 16777215))
        self.lineEdit_MapM_NiVolX.setReadOnly(True)
        self.lineEdit_MapM_NiVolX.setObjectName("lineEdit_MapM_NiVolX")
        self.gridLayout_MapM_Run.addWidget(self.lineEdit_MapM_NiVolX, 0, 15, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.tab_MapMeasurements)
        self.label_66.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_66.setObjectName("label_66")
        self.gridLayout_MapM_Run.addWidget(self.label_66, 1, 13, 1, 1)
        self.comboBox_MapM_NIDAQChY = QtWidgets.QComboBox(self.tab_MapMeasurements)
        self.comboBox_MapM_NIDAQChY.setObjectName("comboBox_MapM_NIDAQChY")
        self.gridLayout_MapM_Run.addWidget(self.comboBox_MapM_NIDAQChY, 1, 14, 1, 1)
        self.lineEdit_MapM_NiVolY = QtWidgets.QLineEdit(self.tab_MapMeasurements)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_MapM_NiVolY.sizePolicy().hasHeightForWidth())
        self.lineEdit_MapM_NiVolY.setSizePolicy(sizePolicy)
        self.lineEdit_MapM_NiVolY.setMaximumSize(QtCore.QSize(160, 16777215))
        self.lineEdit_MapM_NiVolY.setReadOnly(True)
        self.lineEdit_MapM_NiVolY.setObjectName("lineEdit_MapM_NiVolY")
        self.gridLayout_MapM_Run.addWidget(self.lineEdit_MapM_NiVolY, 1, 15, 1, 1)
        self.horizontalLayout_17.addLayout(self.gridLayout_MapM_Run)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_74 = QtWidgets.QLabel(self.tab_MapMeasurements)
        self.label_74.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_74.setObjectName("label_74")
        self.horizontalLayout_15.addWidget(self.label_74)
        self.comboBox_MapM_NIDAQChIn = QtWidgets.QComboBox(self.tab_MapMeasurements)
        self.comboBox_MapM_NIDAQChIn.setObjectName("comboBox_MapM_NIDAQChIn")
        self.horizontalLayout_15.addWidget(self.comboBox_MapM_NIDAQChIn)
        self.lineEdit_MapM_NiVolIn = QtWidgets.QLineEdit(self.tab_MapMeasurements)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_MapM_NiVolIn.sizePolicy().hasHeightForWidth())
        self.lineEdit_MapM_NiVolIn.setSizePolicy(sizePolicy)
        self.lineEdit_MapM_NiVolIn.setMaximumSize(QtCore.QSize(160, 16777215))
        self.lineEdit_MapM_NiVolIn.setReadOnly(True)
        self.lineEdit_MapM_NiVolIn.setObjectName("lineEdit_MapM_NiVolIn")
        self.horizontalLayout_15.addWidget(self.lineEdit_MapM_NiVolIn)
        self.label_75 = QtWidgets.QLabel(self.tab_MapMeasurements)
        self.label_75.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_75.setObjectName("label_75")
        self.horizontalLayout_15.addWidget(self.label_75)
        self.spinBox_MapM_NSamplesAvg = QtWidgets.QSpinBox(self.tab_MapMeasurements)
        self.spinBox_MapM_NSamplesAvg.setMinimum(1)
        self.spinBox_MapM_NSamplesAvg.setObjectName("spinBox_MapM_NSamplesAvg")
        self.horizontalLayout_15.addWidget(self.spinBox_MapM_NSamplesAvg)
        self.label_67 = QtWidgets.QLabel(self.tab_MapMeasurements)
        self.label_67.setEnabled(False)
        self.label_67.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_67.setObjectName("label_67")
        self.horizontalLayout_15.addWidget(self.label_67)
        self.comboBox_MapM_NIDAQChZ = QtWidgets.QComboBox(self.tab_MapMeasurements)
        self.comboBox_MapM_NIDAQChZ.setEnabled(False)
        self.comboBox_MapM_NIDAQChZ.setObjectName("comboBox_MapM_NIDAQChZ")
        self.horizontalLayout_15.addWidget(self.comboBox_MapM_NIDAQChZ)
        self.lineEdit_MapM_NiVolZ = QtWidgets.QLineEdit(self.tab_MapMeasurements)
        self.lineEdit_MapM_NiVolZ.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_MapM_NiVolZ.sizePolicy().hasHeightForWidth())
        self.lineEdit_MapM_NiVolZ.setSizePolicy(sizePolicy)
        self.lineEdit_MapM_NiVolZ.setMaximumSize(QtCore.QSize(160, 16777215))
        self.lineEdit_MapM_NiVolZ.setReadOnly(True)
        self.lineEdit_MapM_NiVolZ.setObjectName("lineEdit_MapM_NiVolZ")
        self.horizontalLayout_15.addWidget(self.lineEdit_MapM_NiVolZ)
        self.label_65 = QtWidgets.QLabel(self.tab_MapMeasurements)
        self.label_65.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_65.setObjectName("label_65")
        self.horizontalLayout_15.addWidget(self.label_65)
        self.spinBox_MapM_MeasureDelay = QtWidgets.QSpinBox(self.tab_MapMeasurements)
        self.spinBox_MapM_MeasureDelay.setKeyboardTracking(False)
        self.spinBox_MapM_MeasureDelay.setMinimum(10)
        self.spinBox_MapM_MeasureDelay.setMaximum(50000)
        self.spinBox_MapM_MeasureDelay.setSingleStep(100)
        self.spinBox_MapM_MeasureDelay.setProperty("value", 1000)
        self.spinBox_MapM_MeasureDelay.setObjectName("spinBox_MapM_MeasureDelay")
        self.horizontalLayout_15.addWidget(self.spinBox_MapM_MeasureDelay)
        self.pushButton_MapM_Measure = QtWidgets.QPushButton(self.tab_MapMeasurements)
        self.pushButton_MapM_Measure.setObjectName("pushButton_MapM_Measure")
        self.horizontalLayout_15.addWidget(self.pushButton_MapM_Measure)
        self.pushButton_MapM_Auto = QtWidgets.QPushButton(self.tab_MapMeasurements)
        self.pushButton_MapM_Auto.setObjectName("pushButton_MapM_Auto")
        self.horizontalLayout_15.addWidget(self.pushButton_MapM_Auto)
        spacerItem2 = QtWidgets.QSpacerItem(15, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.pushButton_MapM_Export = QtWidgets.QPushButton(self.tab_MapMeasurements)
        self.pushButton_MapM_Export.setObjectName("pushButton_MapM_Export")
        self.horizontalLayout_15.addWidget(self.pushButton_MapM_Export)
        self.pushButton_MapM_Load = QtWidgets.QPushButton(self.tab_MapMeasurements)
        self.pushButton_MapM_Load.setObjectName("pushButton_MapM_Load")
        self.horizontalLayout_15.addWidget(self.pushButton_MapM_Load)
        self.verticalLayout_10.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.widget_MeasurementPlot1 = MeasurementPlotWidget(self.tab_MapMeasurements)
        self.widget_MeasurementPlot1.setObjectName("widget_MeasurementPlot1")
        self.horizontalLayout_21.addWidget(self.widget_MeasurementPlot1)
        self.widget_MeasurementPlot2 = MeasurementPlotWidget(self.tab_MapMeasurements)
        self.widget_MeasurementPlot2.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_MeasurementPlot2.setObjectName("widget_MeasurementPlot2")
        self.horizontalLayout_21.addWidget(self.widget_MeasurementPlot2)
        self.widget_MeasurementPlot3 = MeasurementPlotWidget(self.tab_MapMeasurements)
        self.widget_MeasurementPlot3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_MeasurementPlot3.setObjectName("widget_MeasurementPlot3")
        self.horizontalLayout_21.addWidget(self.widget_MeasurementPlot3)
        self.horizontalLayout_21.setStretch(0, 1)
        self.horizontalLayout_21.setStretch(1, 1)
        self.horizontalLayout_21.setStretch(2, 1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_21)
        self.verticalLayout_10.setStretch(2, 1)
        self.tabWidget.addTab(self.tab_MapMeasurements, "")
        self.horizontalLayout_7.addWidget(self.tabWidget)
        self.verticalLayout_16.addLayout(self.horizontalLayout_7)
        SetupMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SetupMainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SetupMainWindow)
        SetupMainWindow.setTabOrder(self.pushButton_SR830_Config, self.pushButton_NIDAQ_Config)
        SetupMainWindow.setTabOrder(self.pushButton_NIDAQ_Config, self.pushButton_Piezo_Config)
        SetupMainWindow.setTabOrder(self.pushButton_Piezo_Config, self.tabWidget)
        SetupMainWindow.setTabOrder(self.tabWidget, self.doubleSpinBox_MapM_X0)
        SetupMainWindow.setTabOrder(self.doubleSpinBox_MapM_X0, self.doubleSpinBox_MapM_X1)
        SetupMainWindow.setTabOrder(self.doubleSpinBox_MapM_X1, self.spinBox_MapM_XSamples)
        SetupMainWindow.setTabOrder(self.spinBox_MapM_XSamples, self.lineEdit_MapM_XStep)
        SetupMainWindow.setTabOrder(self.lineEdit_MapM_XStep, self.pushButton_MapM_GoX0)
        SetupMainWindow.setTabOrder(self.pushButton_MapM_GoX0, self.doubleSpinBox_MapM_Y0)
        SetupMainWindow.setTabOrder(self.doubleSpinBox_MapM_Y0, self.doubleSpinBox_MapM_Y1)
        SetupMainWindow.setTabOrder(self.doubleSpinBox_MapM_Y1, self.spinBox_MapM_YSamples)
        SetupMainWindow.setTabOrder(self.spinBox_MapM_YSamples, self.lineEdit_MapM_YStep)
        SetupMainWindow.setTabOrder(self.lineEdit_MapM_YStep, self.pushButton_MapM_GoY0)
        SetupMainWindow.setTabOrder(self.pushButton_MapM_GoY0, self.spinBox_MapM_MeasureDelay)
        SetupMainWindow.setTabOrder(self.spinBox_MapM_MeasureDelay, self.pushButton_MapM_Measure)
        SetupMainWindow.setTabOrder(self.pushButton_MapM_Measure, self.pushButton_MapM_Auto)
        SetupMainWindow.setTabOrder(self.pushButton_MapM_Auto, self.lineEdit_MapM_LockInX)
        SetupMainWindow.setTabOrder(self.lineEdit_MapM_LockInX, self.lineEdit_MapM_LockInY)
        SetupMainWindow.setTabOrder(self.lineEdit_MapM_LockInY, self.pushButton_MapM_Export)
        SetupMainWindow.setTabOrder(self.pushButton_MapM_Export, self.pushButton_MapM_Load)
        SetupMainWindow.setTabOrder(self.pushButton_MapM_Load, self.scrollArea)

    def retranslateUi(self, SetupMainWindow):
        _translate = QtCore.QCoreApplication.translate
        SetupMainWindow.setWindowTitle(_translate("SetupMainWindow", "Setup Main Control"))
        self.groupBox_SR830.setTitle(_translate("SetupMainWindow", "SR830"))
        self.pushButton_SR830_Config.setText(_translate("SetupMainWindow", "Config"))
        self.label_4.setText(_translate("SetupMainWindow", "Theta:"))
        self.label_3.setText(_translate("SetupMainWindow", "R:"))
        self.label_2.setText(_translate("SetupMainWindow", "X:"))
        self.label_16.setText(_translate("SetupMainWindow", "Y:"))
        self.label_29.setText(_translate("SetupMainWindow", "F:"))
        self.groupBox_NIDaq.setTitle(_translate("SetupMainWindow", "NI DAQ"))
        self.pushButton_NIDAQ_Config.setText(_translate("SetupMainWindow", "Config"))
        self.groupBox_PiezoStage.setTitle(_translate("SetupMainWindow", "Piezo Micro Stage"))
        self.label_Piezo_Conn_Status.setText(_translate("SetupMainWindow", "Via NI"))
        self.pushButton_Piezo_Config.setText(_translate("SetupMainWindow", "Config"))
        self.label_10.setText(_translate("SetupMainWindow", "Z:"))
        self.label_8.setText(_translate("SetupMainWindow", "X:"))
        self.label_9.setText(_translate("SetupMainWindow", "Y:"))
        self.pushButton_SaveSettings.setText(_translate("SetupMainWindow", "Save Settings ..."))
        self.label_46.setText(_translate("SetupMainWindow", "X1:"))
        self.label_68.setText(_translate("SetupMainWindow", "#XSample:"))
        self.label_71.setText(_translate("SetupMainWindow", "Y Step:"))
        self.label_72.setText(_translate("SetupMainWindow", "LockIn X:"))
        self.pushButton_MapM_GoY0.setText(_translate("SetupMainWindow", "Go Y0"))
        self.pushButton_MapM_GoX0.setText(_translate("SetupMainWindow", "Go X0"))
        self.label_45.setText(_translate("SetupMainWindow", "X0:"))
        self.label_73.setText(_translate("SetupMainWindow", "LockIn Y:"))
        self.label_70.setText(_translate("SetupMainWindow", "X Step:"))
        self.label_47.setText(_translate("SetupMainWindow", "Y1:"))
        self.label_64.setText(_translate("SetupMainWindow", "X:"))
        self.label_44.setText(_translate("SetupMainWindow", "Y0:"))
        self.label_69.setText(_translate("SetupMainWindow", "#YSample:"))
        self.label_66.setText(_translate("SetupMainWindow", "Y:"))
        self.label_74.setText(_translate("SetupMainWindow", "NI CH IN:"))
        self.label_75.setText(_translate("SetupMainWindow", "#.Avg"))
        self.label_67.setText(_translate("SetupMainWindow", "Z:"))
        self.label_65.setText(_translate("SetupMainWindow", "MDelay (ms):"))
        self.pushButton_MapM_Measure.setText(_translate("SetupMainWindow", "Measure"))
        self.pushButton_MapM_Auto.setText(_translate("SetupMainWindow", "Auto Measure"))
        self.pushButton_MapM_Export.setText(_translate("SetupMainWindow", "Export"))
        self.pushButton_MapM_Load.setText(_translate("SetupMainWindow", "Load Raw"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_MapMeasurements), _translate("SetupMainWindow", "Map Measurements"))
from ..MeasurementPlot.measurement_plot_widget import MeasurementPlotWidget
