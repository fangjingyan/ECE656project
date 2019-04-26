# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultDialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(604, 430)
        self.reselectPushButton = QtWidgets.QPushButton(Dialog)
        self.reselectPushButton.setGeometry(QtCore.QRect(160, 180, 113, 32))
        self.reselectPushButton.setObjectName("reselectPushButton")
        self.close = QtWidgets.QPushButton(Dialog)
        self.close.setGeometry(QtCore.QRect(290, 180, 113, 32))
        self.close.setObjectName("close")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.reselectPushButton.setText(_translate("Dialog", "reselect"))
        self.close.setText(_translate("Dialog", "close"))

