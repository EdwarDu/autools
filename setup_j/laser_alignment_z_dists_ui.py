# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laser_alignment_z_dists.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LaserAlignment_Z_DistTable(object):
    def setupUi(self, LaserAlignment_Z_DistTable):
        LaserAlignment_Z_DistTable.setObjectName("LaserAlignment_Z_DistTable")
        LaserAlignment_Z_DistTable.resize(475, 868)
        self.verticalLayout = QtWidgets.QVBoxLayout(LaserAlignment_Z_DistTable)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Copy = QtWidgets.QPushButton(LaserAlignment_Z_DistTable)
        self.pushButton_Copy.setObjectName("pushButton_Copy")
        self.horizontalLayout.addWidget(self.pushButton_Copy)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_Clear = QtWidgets.QPushButton(LaserAlignment_Z_DistTable)
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.horizontalLayout.addWidget(self.pushButton_Clear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget_Z_Dists = QtWidgets.QTableWidget(LaserAlignment_Z_DistTable)
        self.tableWidget_Z_Dists.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_Z_Dists.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Z_Dists.setAlternatingRowColors(True)
        self.tableWidget_Z_Dists.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.tableWidget_Z_Dists.setColumnCount(3)
        self.tableWidget_Z_Dists.setObjectName("tableWidget_Z_Dists")
        self.tableWidget_Z_Dists.setRowCount(0)
        self.tableWidget_Z_Dists.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_Z_Dists.horizontalHeader().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.tableWidget_Z_Dists)

        self.retranslateUi(LaserAlignment_Z_DistTable)
        QtCore.QMetaObject.connectSlotsByName(LaserAlignment_Z_DistTable)

    def retranslateUi(self, LaserAlignment_Z_DistTable):
        _translate = QtCore.QCoreApplication.translate
        LaserAlignment_Z_DistTable.setWindowTitle(_translate("LaserAlignment_Z_DistTable", "Form"))
        self.pushButton_Copy.setText(_translate("LaserAlignment_Z_DistTable", "Copy"))
        self.pushButton_Clear.setText(_translate("LaserAlignment_Z_DistTable", "Clear Records"))
        self.tableWidget_Z_Dists.setSortingEnabled(True)


