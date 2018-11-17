# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WrongPasswordErrorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wrongPasswordWindow(object):
    def setupUi(self, wrongPasswordWindow):
        wrongPasswordWindow.setObjectName("wrongPasswordWindow")
        wrongPasswordWindow.resize(823, 113)
        wrongPasswordWindow.setStyleSheet("background :rgb(114, 159, 207);\n"
"font: 75 italic 18pt \"URW Bookman L\";")
        self.wrongPasswordLabel = QtWidgets.QLabel(wrongPasswordWindow)
        self.wrongPasswordLabel.setGeometry(QtCore.QRect(110, 20, 601, 51))
        self.wrongPasswordLabel.setStyleSheet("color :rgb(235, 18, 18);")
        self.wrongPasswordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.wrongPasswordLabel.setObjectName("wrongPasswordLabel")
        self.pushButton = QtWidgets.QPushButton(wrongPasswordWindow)
        self.pushButton.setGeometry(QtCore.QRect(340, 70, 89, 25))
        self.pushButton.setStyleSheet("color :rgb(143, 89, 2)")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(wrongPasswordWindow)
        QtCore.QMetaObject.connectSlotsByName(wrongPasswordWindow)

    def retranslateUi(self, wrongPasswordWindow):
        _translate = QtCore.QCoreApplication.translate
        wrongPasswordWindow.setWindowTitle(_translate("wrongPasswordWindow", "Dialog"))
        self.wrongPasswordLabel.setText(_translate("wrongPasswordWindow", "UserName and Password Does not Match"))
        self.pushButton.setText(_translate("wrongPasswordWindow", "Ok"))

