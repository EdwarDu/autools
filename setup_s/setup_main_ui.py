# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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
        self.groupBox_AOTF = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_AOTF.setObjectName("groupBox_AOTF")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_AOTF)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_AOTF_Conn_Status = QtWidgets.QLabel(self.groupBox_AOTF)
        self.label_AOTF_Conn_Status.setStyleSheet("background: red\n"
"")
        self.label_AOTF_Conn_Status.setText("")
        self.label_AOTF_Conn_Status.setObjectName("label_AOTF_Conn_Status")
        self.horizontalLayout_6.addWidget(self.label_AOTF_Conn_Status)
        self.pushButton_AOTF_Config = QtWidgets.QPushButton(self.groupBox_AOTF)
        self.pushButton_AOTF_Config.setObjectName("pushButton_AOTF_Config")
        self.horizontalLayout_6.addWidget(self.pushButton_AOTF_Config)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_AOTF_Frequency = QtWidgets.QLabel(self.groupBox_AOTF)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_AOTF_Frequency.sizePolicy().hasHeightForWidth())
        self.label_AOTF_Frequency.setSizePolicy(sizePolicy)
        self.label_AOTF_Frequency.setMinimumSize(QtCore.QSize(120, 0))
        self.label_AOTF_Frequency.setText("")
        self.label_AOTF_Frequency.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_AOTF_Frequency.setObjectName("label_AOTF_Frequency")
        self.gridLayout_3.addWidget(self.label_AOTF_Frequency, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_AOTF)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_AOTF)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_AOTF_PowerPerc = QtWidgets.QLabel(self.groupBox_AOTF)
        self.label_AOTF_PowerPerc.setText("")
        self.label_AOTF_PowerPerc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_AOTF_PowerPerc.setObjectName("label_AOTF_PowerPerc")
        self.gridLayout_3.addWidget(self.label_AOTF_PowerPerc, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.verticalLayout.addWidget(self.groupBox_AOTF)
        self.pushButton_SaveSettings = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_SaveSettings.setEnabled(False)
        self.pushButton_SaveSettings.setObjectName("pushButton_SaveSettings")
        self.verticalLayout.addWidget(self.pushButton_SaveSettings)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout.setStretch(2, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_7.addWidget(self.scrollArea)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_LaserProfiler = QtWidgets.QWidget()
        self.tab_LaserProfiler.setObjectName("tab_LaserProfiler")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_LaserProfiler)
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.tab_LaserProfiler)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.comboBox_CamSource = QtWidgets.QComboBox(self.tab_LaserProfiler)
        self.comboBox_CamSource.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox_CamSource.setObjectName("comboBox_CamSource")
        self.horizontalLayout.addWidget(self.comboBox_CamSource)
        self.label_14 = QtWidgets.QLabel(self.tab_LaserProfiler)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.comboBox_FrameSelect = QtWidgets.QComboBox(self.tab_LaserProfiler)
        self.comboBox_FrameSelect.setObjectName("comboBox_FrameSelect")
        self.horizontalLayout.addWidget(self.comboBox_FrameSelect)
        self.pushButton_CamRefresh = QtWidgets.QPushButton(self.tab_LaserProfiler)
        self.pushButton_CamRefresh.setObjectName("pushButton_CamRefresh")
        self.horizontalLayout.addWidget(self.pushButton_CamRefresh)
        self.pushButton_CamConn = QtWidgets.QPushButton(self.tab_LaserProfiler)
        self.pushButton_CamConn.setCheckable(True)
        self.pushButton_CamConn.setObjectName("pushButton_CamConn")
        self.horizontalLayout.addWidget(self.pushButton_CamConn)
        self.pushButton_CAM_Config = QtWidgets.QPushButton(self.tab_LaserProfiler)
        self.pushButton_CAM_Config.setEnabled(False)
        self.pushButton_CAM_Config.setObjectName("pushButton_CAM_Config")
        self.horizontalLayout.addWidget(self.pushButton_CAM_Config)
        self.pushButton_FreeRun = QtWidgets.QPushButton(self.tab_LaserProfiler)
        self.pushButton_FreeRun.setEnabled(False)
        self.pushButton_FreeRun.setCheckable(True)
        self.pushButton_FreeRun.setObjectName("pushButton_FreeRun")
        self.horizontalLayout.addWidget(self.pushButton_FreeRun)
        self.pushButton_Single = QtWidgets.QPushButton(self.tab_LaserProfiler)
        self.pushButton_Single.setEnabled(False)
        self.pushButton_Single.setObjectName("pushButton_Single")
        self.horizontalLayout.addWidget(self.pushButton_Single)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_20 = QtWidgets.QLabel(self.tab_LaserProfiler)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_2.addWidget(self.label_20)
        self.doubleSpinBox_LP_RotateAngle = QtWidgets.QDoubleSpinBox(self.tab_LaserProfiler)
        self.doubleSpinBox_LP_RotateAngle.setMaximum(360.0)
        self.doubleSpinBox_LP_RotateAngle.setObjectName("doubleSpinBox_LP_RotateAngle")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_LP_RotateAngle)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.tab_LaserProfiler)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBox_calcInputWaveLength = QtWidgets.QSpinBox(self.tab_LaserProfiler)
        self.spinBox_calcInputWaveLength.setMinimum(1)
        self.spinBox_calcInputWaveLength.setMaximum(10000)
        self.spinBox_calcInputWaveLength.setSingleStep(10)
        self.spinBox_calcInputWaveLength.setProperty("value", 405)
        self.spinBox_calcInputWaveLength.setObjectName("spinBox_calcInputWaveLength")
        self.horizontalLayout_2.addWidget(self.spinBox_calcInputWaveLength)
        self.label_4 = QtWidgets.QLabel(self.tab_LaserProfiler)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.doubleSpinBox_CalcInputLens = QtWidgets.QDoubleSpinBox(self.tab_LaserProfiler)
        self.doubleSpinBox_CalcInputLens.setDecimals(2)
        self.doubleSpinBox_CalcInputLens.setMinimum(0.0)
        self.doubleSpinBox_CalcInputLens.setSingleStep(0.5)
        self.doubleSpinBox_CalcInputLens.setProperty("value", 80.0)
        self.doubleSpinBox_CalcInputLens.setObjectName("doubleSpinBox_CalcInputLens")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_CalcInputLens)
        self.label_12 = QtWidgets.QLabel(self.tab_LaserProfiler)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.spinBox_calcInputNumPixels = QtWidgets.QSpinBox(self.tab_LaserProfiler)
        self.spinBox_calcInputNumPixels.setMinimum(1)
        self.spinBox_calcInputNumPixels.setMaximum(100000000)
        self.spinBox_calcInputNumPixels.setSingleStep(100)
        self.spinBox_calcInputNumPixels.setProperty("value", 1700)
        self.spinBox_calcInputNumPixels.setObjectName("spinBox_calcInputNumPixels")
        self.horizontalLayout_2.addWidget(self.spinBox_calcInputNumPixels)
        self.label_19 = QtWidgets.QLabel(self.tab_LaserProfiler)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_2.addWidget(self.label_19)
        self.lineEdit_CalcPixelSize = QtWidgets.QLineEdit(self.tab_LaserProfiler)
        self.lineEdit_CalcPixelSize.setMaximumSize(QtCore.QSize(120, 16777215))
        self.lineEdit_CalcPixelSize.setReadOnly(True)
        self.lineEdit_CalcPixelSize.setObjectName("lineEdit_CalcPixelSize")
        self.horizontalLayout_2.addWidget(self.lineEdit_CalcPixelSize)
        self.label_13 = QtWidgets.QLabel(self.tab_LaserProfiler)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.label_9 = QtWidgets.QLabel(self.tab_LaserProfiler)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.lineEdit_CalcResolution = QtWidgets.QLineEdit(self.tab_LaserProfiler)
        self.lineEdit_CalcResolution.setMaximumSize(QtCore.QSize(120, 16777215))
        self.lineEdit_CalcResolution.setMaxLength(200)
        self.lineEdit_CalcResolution.setReadOnly(True)
        self.lineEdit_CalcResolution.setObjectName("lineEdit_CalcResolution")
        self.horizontalLayout_2.addWidget(self.lineEdit_CalcResolution)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_18 = QtWidgets.QLabel(self.tab_LaserProfiler)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_13.addWidget(self.label_18)
        self.checkBox_LP_auto_crosshair = QtWidgets.QCheckBox(self.tab_LaserProfiler)
        self.checkBox_LP_auto_crosshair.setObjectName("checkBox_LP_auto_crosshair")
        self.horizontalLayout_13.addWidget(self.checkBox_LP_auto_crosshair)
        self.checkBox_LP_gaussian_force = QtWidgets.QCheckBox(self.tab_LaserProfiler)
        self.checkBox_LP_gaussian_force.setObjectName("checkBox_LP_gaussian_force")
        self.horizontalLayout_13.addWidget(self.checkBox_LP_gaussian_force)
        self.checkBox_LP_gaussian_manual = QtWidgets.QCheckBox(self.tab_LaserProfiler)
        self.checkBox_LP_gaussian_manual.setObjectName("checkBox_LP_gaussian_manual")
        self.horizontalLayout_13.addWidget(self.checkBox_LP_gaussian_manual)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.pushButton_LP_AddMarker = QtWidgets.QPushButton(self.tab_LaserProfiler)
        self.pushButton_LP_AddMarker.setObjectName("pushButton_LP_AddMarker")
        self.horizontalLayout_13.addWidget(self.pushButton_LP_AddMarker)
        self.pushButton_LP_ClearMarkers = QtWidgets.QPushButton(self.tab_LaserProfiler)
        self.pushButton_LP_ClearMarkers.setObjectName("pushButton_LP_ClearMarkers")
        self.horizontalLayout_13.addWidget(self.pushButton_LP_ClearMarkers)
        self.pushButton_LP_LoadRaw = QtWidgets.QPushButton(self.tab_LaserProfiler)
        self.pushButton_LP_LoadRaw.setObjectName("pushButton_LP_LoadRaw")
        self.horizontalLayout_13.addWidget(self.pushButton_LP_LoadRaw)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.widget_LaserProfiler = LaserProfilerWidget(self.tab_LaserProfiler)
        self.widget_LaserProfiler.setObjectName("widget_LaserProfiler")
        self.verticalLayout_6.addWidget(self.widget_LaserProfiler)
        self.verticalLayout_6.setStretch(1, 1)
        self.tabWidget.addTab(self.tab_LaserProfiler, "")
        self.horizontalLayout_7.addWidget(self.tabWidget)
        self.verticalLayout_16.addLayout(self.horizontalLayout_7)
        SetupMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SetupMainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SetupMainWindow)
        SetupMainWindow.setTabOrder(self.pushButton_AOTF_Config, self.tabWidget)
        SetupMainWindow.setTabOrder(self.tabWidget, self.comboBox_CamSource)
        SetupMainWindow.setTabOrder(self.comboBox_CamSource, self.comboBox_FrameSelect)
        SetupMainWindow.setTabOrder(self.comboBox_FrameSelect, self.pushButton_CamRefresh)
        SetupMainWindow.setTabOrder(self.pushButton_CamRefresh, self.pushButton_CamConn)
        SetupMainWindow.setTabOrder(self.pushButton_CamConn, self.pushButton_CAM_Config)
        SetupMainWindow.setTabOrder(self.pushButton_CAM_Config, self.pushButton_FreeRun)
        SetupMainWindow.setTabOrder(self.pushButton_FreeRun, self.pushButton_Single)
        SetupMainWindow.setTabOrder(self.pushButton_Single, self.scrollArea)

    def retranslateUi(self, SetupMainWindow):
        _translate = QtCore.QCoreApplication.translate
        SetupMainWindow.setWindowTitle(_translate("SetupMainWindow", "Setup Main Control"))
        self.groupBox_AOTF.setTitle(_translate("SetupMainWindow", "AOTF"))
        self.pushButton_AOTF_Config.setText(_translate("SetupMainWindow", "Config"))
        self.label_11.setText(_translate("SetupMainWindow", "Power%:"))
        self.label_6.setText(_translate("SetupMainWindow", "Wave L.:"))
        self.pushButton_SaveSettings.setText(_translate("SetupMainWindow", "Save Settings ..."))
        self.label_5.setText(_translate("SetupMainWindow", "Source:"))
        self.label_14.setText(_translate("SetupMainWindow", "Frame Select:"))
        self.pushButton_CamRefresh.setText(_translate("SetupMainWindow", "Refresh"))
        self.pushButton_CamConn.setText(_translate("SetupMainWindow", "Connect"))
        self.pushButton_CAM_Config.setText(_translate("SetupMainWindow", "Configure"))
        self.pushButton_FreeRun.setText(_translate("SetupMainWindow", "Free Run"))
        self.pushButton_Single.setText(_translate("SetupMainWindow", "Single Frame"))
        self.label_20.setText(_translate("SetupMainWindow", "Rotation"))
        self.label_2.setText(_translate("SetupMainWindow", "WaveL (nm):"))
        self.label_4.setText(_translate("SetupMainWindow", "Lens (um):"))
        self.label_12.setText(_translate("SetupMainWindow", "#P"))
        self.label_19.setText(_translate("SetupMainWindow", "PixelSize(nm):"))
        self.label_13.setText(_translate("SetupMainWindow", "nm"))
        self.label_9.setText(_translate("SetupMainWindow", "Res.:"))
        self.label_18.setText(_translate("SetupMainWindow", "Options:"))
        self.checkBox_LP_auto_crosshair.setText(_translate("SetupMainWindow", "Cross Hair Auto Hotspot"))
        self.checkBox_LP_gaussian_force.setText(_translate("SetupMainWindow", "Gaussian Fit Force Peak"))
        self.checkBox_LP_gaussian_manual.setText(_translate("SetupMainWindow", "Gaussian Fit Manual Mean"))
        self.pushButton_LP_AddMarker.setText(_translate("SetupMainWindow", "Add Marker"))
        self.pushButton_LP_ClearMarkers.setText(_translate("SetupMainWindow", "Clear Markers"))
        self.pushButton_LP_LoadRaw.setText(_translate("SetupMainWindow", "Load Raw"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_LaserProfiler), _translate("SetupMainWindow", "Laser Alignment"))
from ..LaserProfiler.laser_profiler_widget import LaserProfilerWidget
