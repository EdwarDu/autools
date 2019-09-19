# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dg5000_config.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DG5000_Config_Window(object):
    def setupUi(self, DG5000_Config_Window):
        DG5000_Config_Window.setObjectName("DG5000_Config_Window")
        DG5000_Config_Window.resize(583, 416)
        self.verticalLayout = QtWidgets.QVBoxLayout(DG5000_Config_Window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_Resource = QtWidgets.QGroupBox(DG5000_Config_Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_Resource.sizePolicy().hasHeightForWidth())
        self.groupBox_Resource.setSizePolicy(sizePolicy)
        self.groupBox_Resource.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_Resource.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox_Resource.setObjectName("groupBox_Resource")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_Resource)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(6, -1, 6, -1)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox_Resource)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_ResourceAddr = QtWidgets.QComboBox(self.groupBox_Resource)
        self.comboBox_ResourceAddr.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_ResourceAddr.sizePolicy().hasHeightForWidth())
        self.comboBox_ResourceAddr.setSizePolicy(sizePolicy)
        self.comboBox_ResourceAddr.setObjectName("comboBox_ResourceAddr")
        self.gridLayout.addWidget(self.comboBox_ResourceAddr, 0, 1, 1, 2)
        self.pushButton_Open = QtWidgets.QPushButton(self.groupBox_Resource)
        self.pushButton_Open.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_Open.setCheckable(True)
        self.pushButton_Open.setFlat(False)
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.gridLayout.addWidget(self.pushButton_Open, 1, 2, 1, 1)
        self.pushButton_Refresh = QtWidgets.QPushButton(self.groupBox_Resource)
        self.pushButton_Refresh.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_Refresh.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_Refresh.setCheckable(False)
        self.pushButton_Refresh.setObjectName("pushButton_Refresh")
        self.gridLayout.addWidget(self.pushButton_Refresh, 1, 1, 1, 1)
        self.label_CONN_Status = QtWidgets.QLabel(self.groupBox_Resource)
        self.label_CONN_Status.setStyleSheet("background : red")
        self.label_CONN_Status.setText("")
        self.label_CONN_Status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_CONN_Status.setObjectName("label_CONN_Status")
        self.gridLayout.addWidget(self.label_CONN_Status, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox_Resource)
        self.groupBox_Settings = QtWidgets.QGroupBox(DG5000_Config_Window)
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
        self.verticalLayout.addWidget(self.groupBox_Settings)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(DG5000_Config_Window)
        QtCore.QMetaObject.connectSlotsByName(DG5000_Config_Window)

    def retranslateUi(self, DG5000_Config_Window):
        _translate = QtCore.QCoreApplication.translate
        DG5000_Config_Window.setWindowTitle(_translate("DG5000_Config_Window", "SR830 Configuration"))
        self.groupBox_Resource.setTitle(_translate("DG5000_Config_Window", "DG5000 COM"))
        self.label.setText(_translate("DG5000_Config_Window", "Resource Addr:"))
        self.pushButton_Open.setText(_translate("DG5000_Config_Window", "Open"))
        self.pushButton_Refresh.setText(_translate("DG5000_Config_Window", "Refresh"))
        self.groupBox_Settings.setTitle(_translate("DG5000_Config_Window", "DG5000 Settings"))


