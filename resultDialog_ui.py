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
        self.reselectPushButton.setGeometry(QtCore.QRect(350, 310, 113, 32))
        self.reselectPushButton.setObjectName("reselectPushButton")
        self.close = QtWidgets.QPushButton(Dialog)
        self.close.setGeometry(QtCore.QRect(480, 310, 113, 32))
        self.close.setObjectName("close")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 90, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 180, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.accuracy = QtWidgets.QLabel(Dialog)
        self.accuracy.setGeometry(QtCore.QRect(340, 90, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.accuracy.setFont(font)
        self.accuracy.setText("")
        self.accuracy.setObjectName("accuracy")
        self.predicting_stars = QtWidgets.QLabel(Dialog)
        self.predicting_stars.setGeometry(QtCore.QRect(340, 180, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.predicting_stars.setFont(font)
        self.predicting_stars.setText("")
        self.predicting_stars.setObjectName("predicting_stars")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.reselectPushButton.setText(_translate("Dialog", "reselect"))
        self.close.setText(_translate("Dialog", "close"))
        self.label.setText(_translate("Dialog", "Accuracy:"))
        self.label_2.setText(_translate("Dialog", "Predicting stars:"))

