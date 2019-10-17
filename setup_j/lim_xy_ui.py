# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lim_xy.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LIM_XYTable(object):
    def setupUi(self, LIM_XYTable):
        LIM_XYTable.setObjectName("LIM_XYTable")
        LIM_XYTable.resize(635, 678)
        self.verticalLayout = QtWidgets.QVBoxLayout(LIM_XYTable)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Copy = QtWidgets.QPushButton(LIM_XYTable)
        self.pushButton_Copy.setObjectName("pushButton_Copy")
        self.horizontalLayout.addWidget(self.pushButton_Copy)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_Clear = QtWidgets.QPushButton(LIM_XYTable)
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.horizontalLayout.addWidget(self.pushButton_Clear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget_XY = QtWidgets.QTableWidget(LIM_XYTable)
        self.tableWidget_XY.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_XY.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_XY.setAlternatingRowColors(True)
        self.tableWidget_XY.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.tableWidget_XY.setColumnCount(4)
        self.tableWidget_XY.setObjectName("tableWidget_XY")
        self.tableWidget_XY.setRowCount(0)
        self.tableWidget_XY.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_XY.horizontalHeader().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.tableWidget_XY)

        self.retranslateUi(LIM_XYTable)
        QtCore.QMetaObject.connectSlotsByName(LIM_XYTable)

    def retranslateUi(self, LIM_XYTable):
        _translate = QtCore.QCoreApplication.translate
        LIM_XYTable.setWindowTitle(_translate("LIM_XYTable", "Form"))
        self.pushButton_Copy.setText(_translate("LIM_XYTable", "Copy"))
        self.pushButton_Clear.setText(_translate("LIM_XYTable", "Clear Records"))
        self.tableWidget_XY.setSortingEnabled(True)


