# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BloodDonationRecieptDialogBox.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bloodDonationReciept(object):
    def setupUi(self, bloodDonationReciept):
        bloodDonationReciept.setObjectName("bloodDonationReciept")
        bloodDonationReciept.resize(371, 375)
        self.idInput = QtWidgets.QLineEdit(bloodDonationReciept)
        self.idInput.setGeometry(QtCore.QRect(160, 80, 151, 25))
        self.idInput.setObjectName("idInput")
        self.idLabel = QtWidgets.QLabel(bloodDonationReciept)
        self.idLabel.setGeometry(QtCore.QRect(40, 80, 101, 21))
        self.idLabel.setStyleSheet("font: 57 15pt \"Ubuntu\";")
        self.idLabel.setObjectName("idLabel")
        self.bloodGroupLabel = QtWidgets.QLabel(bloodDonationReciept)
        self.bloodGroupLabel.setGeometry(QtCore.QRect(40, 120, 121, 41))
        self.bloodGroupLabel.setStyleSheet("font: 57 15pt \"Ubuntu\";")
        self.bloodGroupLabel.setObjectName("bloodGroupLabel")
        self.bloodGroupComboBox = QtWidgets.QComboBox(bloodDonationReciept)
        self.bloodGroupComboBox.setGeometry(QtCore.QRect(190, 130, 121, 25))
        self.bloodGroupComboBox.setObjectName("bloodGroupComboBox")
        self.bloodAmountLabel = QtWidgets.QLabel(bloodDonationReciept)
        self.bloodAmountLabel.setGeometry(QtCore.QRect(40, 170, 141, 41))
        self.bloodAmountLabel.setStyleSheet("font: 57 15pt \"Ubuntu\";")
        self.bloodAmountLabel.setObjectName("bloodAmountLabel")
        self.bloodAmountInputBox = QtWidgets.QLineEdit(bloodDonationReciept)
        self.bloodAmountInputBox.setGeometry(QtCore.QRect(190, 180, 121, 25))
        self.bloodAmountInputBox.setObjectName("bloodAmountInputBox")
        self.dateInput = QtWidgets.QDateEdit(bloodDonationReciept)
        self.dateInput.setGeometry(QtCore.QRect(190, 225, 121, 31))
        self.dateInput.setObjectName("dateInput")
        self.dateLabel = QtWidgets.QLabel(bloodDonationReciept)
        self.dateLabel.setGeometry(QtCore.QRect(40, 220, 141, 41))
        self.dateLabel.setStyleSheet("font: 57 15pt \"Ubuntu\";")
        self.dateLabel.setObjectName("dateLabel")
        self.submitButton = QtWidgets.QPushButton(bloodDonationReciept)
        self.submitButton.setGeometry(QtCore.QRect(130, 290, 89, 25))
        self.submitButton.setObjectName("submitButton")
        self.label_5 = QtWidgets.QLabel(bloodDonationReciept)
        self.label_5.setGeometry(QtCore.QRect(40, 20, 291, 31))
        self.label_5.setStyleSheet("text-decoration : underline;\n"
"font: 57 16pt \"Ubuntu\";")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(bloodDonationReciept)
        QtCore.QMetaObject.connectSlotsByName(bloodDonationReciept)

    def retranslateUi(self, bloodDonationReciept):
        _translate = QtCore.QCoreApplication.translate
        bloodDonationReciept.setWindowTitle(_translate("bloodDonationReciept", "Dialog"))
        self.idLabel.setText(_translate("bloodDonationReciept", "Patient Id"))
        self.bloodGroupLabel.setText(_translate("bloodDonationReciept", "Blood Group"))
        self.bloodAmountLabel.setText(_translate("bloodDonationReciept", "Blood Amount"))
        self.dateLabel.setText(_translate("bloodDonationReciept", "Date "))
        self.submitButton.setText(_translate("bloodDonationReciept", "SUBMIT"))
        self.label_5.setText(_translate("bloodDonationReciept", "BLOOD DONATION RECIEPT"))
        self.bloodGroupComboBox.addItem("A+")
        self.bloodGroupComboBox.addItem("A-")
        self.bloodGroupComboBox.addItem("B+")
        self.bloodGroupComboBox.addItem("B-")
        self.bloodGroupComboBox.addItem("O+")
        self.bloodGroupComboBox.addItem("O-")
        self.bloodGroupComboBox.addItem("AB+")
        self.bloodGroupComboBox.addItem("AB-")

