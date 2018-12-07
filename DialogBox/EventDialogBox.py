# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EventDialogBox.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Ui_EventDialog(QWidget):
    def setupUi(self, EventDialog):
        EventDialog.setObjectName("EventDialog")
        EventDialog.resize(857, 471)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EventDialog.sizePolicy().hasHeightForWidth())
        #EventDialog.setSizePolicy(sizePolicy)
        #EventDialog.setModal(True)
        self.evenLabel = QtWidgets.QLabel(EventDialog)
        self.evenLabel.setGeometry(QtCore.QRect(6, 0, 841, 41))
        self.evenLabel.setStyleSheet("font: 75 24pt \"Tibetan Machine Uni\";text-decoration : underline;")
        self.evenLabel.setTextFormat(QtCore.Qt.RichText)
        self.evenLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.evenLabel.setObjectName("evenLabel")
        self.titleLabel = QtWidgets.QLabel(EventDialog)
        self.titleLabel.setGeometry(QtCore.QRect(30, 80, 131, 31))
        self.titleLabel.setStyleSheet("font: 16 14pt \"Ubuntu Condensed\";")
        self.titleLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.titleInput = QtWidgets.QLineEdit(EventDialog)
        self.titleInput.setGeometry(QtCore.QRect(180, 70, 611, 41))
        self.titleInput.setStyleSheet("font: 75 14pt \"Ubuntu Condensed\";background : rgb(225,225,225);")
        self.titleInput.setText("")
        self.titleInput.setObjectName("titleInput")
        self.DescriptionInput = QtWidgets.QTextEdit(EventDialog)
        self.DescriptionInput.setGeometry(QtCore.QRect(180, 120, 611,150))
        self.DescriptionInput.setStyleSheet("background : rgb(225,225,225);")
        self.DescriptionInput.setObjectName("DescriptionInput")
        self.descriptionLabel = QtWidgets.QLabel(EventDialog)
        self.descriptionLabel.setGeometry(QtCore.QRect(30, 160, 141, 31))
        self.descriptionLabel.setStyleSheet("font: 75 14pt \"Ubuntu Condensed\";")
        self.descriptionLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.descriptionLabel.setObjectName("descriptionLabel")

        self.dateOfEventLabel = QtWidgets.QLabel(EventDialog)
        self.dateOfEventLabel.setGeometry(30,280,141,31)
        self.dateOfEventLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.dateOfEventLabel.setObjectName("dateOfEventLabel")
        self.dateOfEventLabel.setStyleSheet("font: 75 14pt \"Ubuntu Condensed\";")
        self.dateOfEventInput  = QtWidgets.QDateEdit(EventDialog)
        self.dateOfEventInput.setGeometry(180,280,141,31)

        self.selectFileButton = QtWidgets.QPushButton(EventDialog)
        self.selectFileButton.setGeometry(QtCore.QRect(700, 320, 89, 31))
        self.selectFileButton.setObjectName("selectFileButton")
        self.imageFileInput = QtWidgets.QLineEdit(EventDialog)
        self.imageFileInput.setGeometry(QtCore.QRect(180, 320, 511, 31))
        self.imageFileInput.setStyleSheet("font: 75 14pt \"Ubuntu Condensed\";background : rgb(225,225,225);")
        self.imageFileInput.setText("")
        self.imageFileInput.setObjectName("imageFileInput")
        self.ImageLabel = QtWidgets.QLabel(EventDialog)
        self.ImageLabel.setGeometry(QtCore.QRect(70, 320, 71, 31))
        self.ImageLabel.setStyleSheet("font: 75 14pt \"Ubuntu Condensed\";")
        #self.ImageLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.ImageLabel.setObjectName("ImageLabel")
        self.placeLabel = QtWidgets.QLabel(EventDialog)
        self.placeLabel.setGeometry(QtCore.QRect(70, 370, 71, 31))
        self.placeLabel.setStyleSheet("font: 75 14pt \"Ubuntu Condensed\";")
        #self.placeLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.placeLabel.setObjectName("placeLabel")
        self.placeInput = QtWidgets.QLineEdit(EventDialog)
        self.placeInput.setGeometry(QtCore.QRect(180, 360, 611, 41))
        self.placeInput.setStyleSheet("font: 75 14pt \"Ubuntu Condensed\"; background : rgb(225,225,225);")
        self.placeInput.setText("")
        self.placeInput.setObjectName("placeInput")
        self.submitButton = QtWidgets.QPushButton(EventDialog)
        self.submitButton.setGeometry(QtCore.QRect(390, 420, 89, 25))
        self.submitButton.setObjectName("submitButton")

        self.retranslateUi(EventDialog)
        QtCore.QMetaObject.connectSlotsByName(EventDialog)

    def retranslateUi(self, EventDialog):
        _translate = QtCore.QCoreApplication.translate
        EventDialog.setWindowTitle(_translate("EventDialog", "Dialog"))
        self.evenLabel.setText(_translate("EventDialog", "Event Description"))
        self.titleLabel.setText(_translate("EventDialog", "Title "))
        self.dateOfEventLabel.setText(_translate("EventDialog","Date"))
        self.descriptionLabel.setText(_translate("EventDialog", "Description"))
        self.selectFileButton.setText(_translate("EventDialog", "select File"))
        self.imageFileInput.setPlaceholderText(_translate("EventDialog", "select an image by clicking on the select file button"))
        self.ImageLabel.setText(_translate("EventDialog", "Image"))
        self.placeLabel.setText(_translate("EventDialog", "Place"))
        self.submitButton.setText(_translate("EventDialog", "Submit"))

        self.selectFileButton.clicked.connect(self.open)


    # Opening the ffile
    def open (self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '.')
        self.imageFileInput.setText(str(filename))


