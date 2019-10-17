# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pcali_wlen_power.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PCali_WLenPowerTable(object):
    def setupUi(self, PCali_WLenPowerTable):
        PCali_WLenPowerTable.setObjectName("PCali_WLenPowerTable")
        PCali_WLenPowerTable.resize(329, 659)
        self.verticalLayout = QtWidgets.QVBoxLayout(PCali_WLenPowerTable)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_SaveCSV = QtWidgets.QPushButton(PCali_WLenPowerTable)
        self.pushButton_SaveCSV.setObjectName("pushButton_SaveCSV")
        self.horizontalLayout.addWidget(self.pushButton_SaveCSV)
        self.pushButton_Copy = QtWidgets.QPushButton(PCali_WLenPowerTable)
        self.pushButton_Copy.setObjectName("pushButton_Copy")
        self.horizontalLayout.addWidget(self.pushButton_Copy)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_Clear = QtWidgets.QPushButton(PCali_WLenPowerTable)
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.horizontalLayout.addWidget(self.pushButton_Clear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget_WLen_Power = QtWidgets.QTableWidget(PCali_WLenPowerTable)
        self.tableWidget_WLen_Power.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_WLen_Power.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_WLen_Power.setAlternatingRowColors(True)
        self.tableWidget_WLen_Power.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.tableWidget_WLen_Power.setColumnCount(2)
        self.tableWidget_WLen_Power.setObjectName("tableWidget_WLen_Power")
        self.tableWidget_WLen_Power.setRowCount(0)
        self.tableWidget_WLen_Power.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_WLen_Power.horizontalHeader().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.tableWidget_WLen_Power)

        self.retranslateUi(PCali_WLenPowerTable)
        QtCore.QMetaObject.connectSlotsByName(PCali_WLenPowerTable)

    def retranslateUi(self, PCali_WLenPowerTable):
        _translate = QtCore.QCoreApplication.translate
        PCali_WLenPowerTable.setWindowTitle(_translate("PCali_WLenPowerTable", "Form"))
        self.pushButton_SaveCSV.setText(_translate("PCali_WLenPowerTable", "Save CSV"))
        self.pushButton_Copy.setText(_translate("PCali_WLenPowerTable", "Copy"))
        self.pushButton_Clear.setText(_translate("PCali_WLenPowerTable", "Clear Records"))
        self.tableWidget_WLen_Power.setSortingEnabled(True)


