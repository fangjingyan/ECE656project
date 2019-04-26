# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choosedialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(601, 428)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 30, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.no_clean = QtWidgets.QRadioButton(Dialog)
        self.no_clean.setGeometry(QtCore.QRect(480, 280, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.no_clean.setFont(font)
        self.no_clean.setObjectName("no_clean")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 270, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.yes_clean = QtWidgets.QRadioButton(Dialog)
        self.yes_clean.setGeometry(QtCore.QRect(390, 280, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yes_clean.setFont(font)
        self.yes_clean.setChecked(True)
        self.yes_clean.setObjectName("yes_clean")
        self.restart = QtWidgets.QPushButton(Dialog)
        self.restart.setGeometry(QtCore.QRect(350, 340, 113, 32))
        self.restart.setObjectName("restart")
        self.next = QtWidgets.QPushButton(Dialog)
        self.next.setGeometry(QtCore.QRect(480, 340, 113, 32))
        self.next.setObjectName("next")
        self.b_average_stars = QtWidgets.QCheckBox(Dialog)
        self.b_average_stars.setEnabled(False)
        self.b_average_stars.setGeometry(QtCore.QRect(240, 100, 121, 20))
        self.b_average_stars.setChecked(True)
        self.b_average_stars.setObjectName("b_average_stars")
        self.b_review_count = QtWidgets.QCheckBox(Dialog)
        self.b_review_count.setGeometry(QtCore.QRect(240, 130, 181, 20))
        self.b_review_count.setObjectName("b_review_count")
        self.u_average_stars = QtWidgets.QCheckBox(Dialog)
        self.u_average_stars.setEnabled(False)
        self.u_average_stars.setGeometry(QtCore.QRect(240, 160, 151, 20))
        self.u_average_stars.setChecked(True)
        self.u_average_stars.setObjectName("u_average_stars")
        self.u_review_count = QtWidgets.QCheckBox(Dialog)
        self.u_review_count.setGeometry(QtCore.QRect(240, 190, 141, 20))
        self.u_review_count.setObjectName("u_review_count")
        self.u_fans = QtWidgets.QCheckBox(Dialog)
        self.u_fans.setGeometry(QtCore.QRect(240, 220, 87, 20))
        self.u_fans.setObjectName("u_fans")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "features important for prediction"))
        self.no_clean.setText(_translate("Dialog", "No"))
        self.label_2.setText(_translate("Dialog", "Do you want to clean data?"))
        self.yes_clean.setText(_translate("Dialog", "Yes"))
        self.restart.setText(_translate("Dialog", "restart"))
        self.next.setText(_translate("Dialog", "analyze"))
        self.b_average_stars.setText(_translate("Dialog", "businees.stars"))
        self.b_review_count.setText(_translate("Dialog", "business.review_count"))
        self.u_average_stars.setText(_translate("Dialog", "user.average_stars"))
        self.u_review_count.setText(_translate("Dialog", "user.review_count"))
        self.u_fans.setText(_translate("Dialog", "user.fans"))

