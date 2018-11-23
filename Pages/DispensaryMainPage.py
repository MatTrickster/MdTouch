# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DispensaryMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from DialogBox.EventDialogBox import *
from DialogBox.changePassword import *
from DialogBox.AddNewMedicineDialogBox import *
from DialogBox.MedicineInfodialogBox import *

class Ui_DispensaryMainWindow(object):
    def setupUi(self, DispensaryMainWindow,username):
        DispensaryMainWindow.setObjectName("DispensaryMainWindow")
        DispensaryMainWindow.resize(1390, 915)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DispensaryMainWindow.sizePolicy().hasHeightForWidth())
        DispensaryMainWindow.setSizePolicy(sizePolicy)
        DispensaryMainWindow.setStyleSheet("background: rgb(66, 140, 244);")
        self.centralwidget = QtWidgets.QWidget(DispensaryMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(430, 0, 521, 121))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Logo.setFont(font)
        self.Logo.setAlignment(QtCore.Qt.AlignCenter)
        self.Logo.setObjectName("Logo")
        self.dispensaryNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.dispensaryNameLabel.setGeometry(QtCore.QRect(10, 120, 1371, 31))
        self.dispensaryNameLabel.setStyleSheet("text-transform : uppercase;\n"
"text-decoration : underline;\n"
"font: 75 20pt \"URW Bookman L\";")
        self.dispensaryNameLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.dispensaryNameLabel.setObjectName("dispensaryNameLabel")
        self.usernameLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel_2.setGeometry(QtCore.QRect(520, 290, 171, 31))
        self.usernameLabel_2.setStyleSheet("\n"
"font: 75 20pt \"URW Bookman L\";")
        self.usernameLabel_2.setText("")
        self.usernameLabel_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.usernameLabel_2.setObjectName("usernameLabel_2")
        self.logoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logoutButton.setGeometry(QtCore.QRect(1338, 0, 51, 41))
        self.logoutButton.setObjectName("logoutButton")
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(1290, 0, 51, 41))
        self.refreshButton.setObjectName("refreshButton")
        self.MedicineSearchTable = QtWidgets.QTableWidget(self.centralwidget)
        self.MedicineSearchTable.setGeometry(QtCore.QRect(340, 210, 731, 701))
        self.MedicineSearchTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MedicineSearchTable.setAutoFillBackground(False)
        self.MedicineSearchTable.setStyleSheet("background: rgb(225,225,255);\n"
"text-align : left;")
        self.MedicineSearchTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.MedicineSearchTable.setAutoScrollMargin(100)
        self.MedicineSearchTable.setShowGrid(True)
        self.MedicineSearchTable.setWordWrap(True)
        self.MedicineSearchTable.setCornerButtonEnabled(True)
        self.MedicineSearchTable.setRowCount(5)
        self.MedicineSearchTable.setColumnCount(7)
        self.MedicineSearchTable.setObjectName("MedicineSearchTable")
        item = QtWidgets.QTableWidgetItem()
        self.MedicineSearchTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.MedicineSearchTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.MedicineSearchTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.MedicineSearchTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.MedicineSearchTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.MedicineSearchTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.MedicineSearchTable.setHorizontalHeaderItem(6, item)
        self.MedicineSearchTable.horizontalHeader().setCascadingSectionResizes(False)
        self.MedicineSearchTable.horizontalHeader().setStretchLastSection(True)
        self.filterComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.filterComboBox.setGeometry(QtCore.QRect(750, 180, 211, 31))
        self.filterComboBox.setStyleSheet("background : rgb(225,225,225);")
        self.filterComboBox.setObjectName("filterComboBox")
        self.filterComboBox.addItem("")
        self.filterComboBox.addItem("")
        self.filterComboBox.addItem("")
        self.filterComboBox.addItem("")
        self.filterComboBox.addItem("")
        self.filterComboBox.addItem("")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(960, 180, 111, 31))
        self.searchButton.setStyleSheet("background : rgb(225,225,225);")
        self.searchButton.setObjectName("searchButton")
        self.searchInput = QtWidgets.QLineEdit(self.centralwidget)
        self.searchInput.setGeometry(QtCore.QRect(340, 180, 411, 31))
        self.searchInput.setStyleSheet("background : rgb(255,255,255);")
        self.searchInput.setObjectName("searchInput")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(50, 180, 264, 731))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.addEventButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.addEventButton.setStyleSheet("background : rgb(225,225,220);")
        self.addEventButton.setObjectName("addEventButton")
        self.verticalLayout_2.addWidget(self.addEventButton)
        self.searchEventButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.searchEventButton.setStyleSheet("background : rgb(225,225,220);")
        self.searchEventButton.setObjectName("searchEventButton")
        self.verticalLayout_2.addWidget(self.searchEventButton)
        self.deletEventButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.deletEventButton.setStyleSheet("background : rgb(225,225,220);")
        self.deletEventButton.setObjectName("deletEventButton")
        self.verticalLayout_2.addWidget(self.deletEventButton)
        self.allEventButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.allEventButton.setStyleSheet("background : rgb(225,225,220);")
        self.allEventButton.setObjectName("allEventButton")
        self.verticalLayout_2.addWidget(self.allEventButton)
        self.editEventButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.editEventButton.setStyleSheet("background : rgb(225,225,220);")
        self.editEventButton.setObjectName("editEventButton")
        self.verticalLayout_2.addWidget(self.editEventButton)
        self.allDistributionButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.allDistributionButton.setStyleSheet("background : rgb(225,225,220);")
        self.allDistributionButton.setObjectName("allDistributionButton")
        self.verticalLayout_2.addWidget(self.allDistributionButton)
        self.createDistributionBillButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.createDistributionBillButton.setStyleSheet("background : rgb(225,225,220);")
        self.createDistributionBillButton.setObjectName("createDistributionBillButton")
        self.verticalLayout_2.addWidget(self.createDistributionBillButton)
        self.searchBillButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.searchBillButton.setStyleSheet("background : rgb(225,225,220);")
        self.searchBillButton.setObjectName("searchBillButton")
        self.verticalLayout_2.addWidget(self.searchBillButton)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 160, 1371, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.deleteIdInput = QtWidgets.QLineEdit(self.centralwidget)
        self.deleteIdInput.setGeometry(QtCore.QRect(1100, 320, 161, 31))
        self.deleteIdInput.setStyleSheet("background : rgb(255,255,255);")
        self.deleteIdInput.setObjectName("deleteIdInput")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(1260, 320, 111, 31))
        self.deleteButton.setStyleSheet("background : rgb(225,225,225);")
        self.deleteButton.setObjectName("deleteButton")
        self.setMedicineIdInput = QtWidgets.QLineEdit(self.centralwidget)
        self.setMedicineIdInput.setGeometry(QtCore.QRect(1100, 430, 161, 31))
        self.setMedicineIdInput.setStyleSheet("background : rgb(255,255,255);")
        self.setMedicineIdInput.setText("")
        self.setMedicineIdInput.setObjectName("setMedicineIdInput")
        self.setQuantityButton = QtWidgets.QPushButton(self.centralwidget)
        self.setQuantityButton.setGeometry(QtCore.QRect(1100, 460, 281, 31))
        self.setQuantityButton.setStyleSheet("background : rgb(225,225,225);")
        self.setQuantityButton.setObjectName("setQuantityButton")
        self.quantityInput = QtWidgets.QLineEdit(self.centralwidget)
        self.quantityInput.setGeometry(QtCore.QRect(1260, 430, 121, 31))
        self.quantityInput.setStyleSheet("background : rgb(255,255,255);")
        self.quantityInput.setText("")
        self.quantityInput.setObjectName("quantityInput")
        self.newPriceInput = QtWidgets.QLineEdit(self.centralwidget)
        self.newPriceInput.setGeometry(QtCore.QRect(1260, 580, 121, 31))
        self.newPriceInput.setStyleSheet("background : rgb(255,255,255);")
        self.newPriceInput.setText("")
        self.newPriceInput.setObjectName("newPriceInput")
        self.changePriceIdInput = QtWidgets.QLineEdit(self.centralwidget)
        self.changePriceIdInput.setGeometry(QtCore.QRect(1100, 580, 161, 31))
        self.changePriceIdInput.setStyleSheet("background : rgb(255,255,255);")
        self.changePriceIdInput.setText("")
        self.changePriceIdInput.setObjectName("changePriceIdInput")
        self.changePriceButton = QtWidgets.QPushButton(self.centralwidget)
        self.changePriceButton.setGeometry(QtCore.QRect(1100, 610, 281, 31))
        self.changePriceButton.setStyleSheet("background : rgb(225,225,225);")
        self.changePriceButton.setObjectName("changePriceButton")
        self.change_password_button = QtWidgets.QPushButton(self.centralwidget)
        self.change_password_button.setGeometry(QtCore.QRect(1110, 830, 262, 25))
        self.change_password_button.setStyleSheet("background : rgb(225,225,220);")
        self.change_password_button.setObjectName("change_password_button")
        self.editDetialsButton = QtWidgets.QPushButton(self.centralwidget)
        self.editDetialsButton.setGeometry(QtCore.QRect(1110, 730, 262, 25))
        self.editDetialsButton.setStyleSheet("background : rgb(225,225,220);")
        self.editDetialsButton.setObjectName("editDetialsButton")
        self.addMedicineButton = QtWidgets.QPushButton(self.centralwidget)
        self.addMedicineButton.setGeometry(QtCore.QRect(1100, 220, 262, 25))
        self.addMedicineButton.setStyleSheet("background : rgb(225,225,220);")
        self.addMedicineButton.setObjectName("addMedicineButton")
        DispensaryMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DispensaryMainWindow)
        QtCore.QMetaObject.connectSlotsByName(DispensaryMainWindow)

    def retranslateUi(self, DispensaryMainWindow):
        _translate = QtCore.QCoreApplication.translate
        DispensaryMainWindow.setWindowTitle(_translate("DispensaryMainWindow", "MainWindow"))
        self.Logo.setText(_translate("DispensaryMainWindow", "Md Touch"))
        self.dispensaryNameLabel.setText(_translate("DispensaryMainWindow", "DISPENSARY NAME"))
        #self.logoutButton.setText(_translate("DispensaryMainWindow", "B"))
        #self.refreshButton.setText(_translate("DispensaryMainWindow", "R"))
        self.MedicineSearchTable.horizontalHeader().setStretchLastSection(True)
        item = self.MedicineSearchTable.horizontalHeaderItem(0)
        item.setText(_translate("DispensaryMainWindow", "Medicine ID"))
        item = self.MedicineSearchTable.horizontalHeaderItem(1)
        item.setText(_translate("DispensaryMainWindow", "Name"))
        item = self.MedicineSearchTable.horizontalHeaderItem(2)
        item.setText(_translate("DispensaryMainWindow", "Price"))
        item = self.MedicineSearchTable.horizontalHeaderItem(3)
        item.setText(_translate("DispensaryMainWindow", "Quantity"))
        item = self.MedicineSearchTable.horizontalHeaderItem(4)
        item.setText(_translate("DispensaryMainWindow", "Batch No"))
        item = self.MedicineSearchTable.horizontalHeaderItem(5)
        item.setText(_translate("DispensaryMainWindow", "Manufacture Date"))
        item = self.MedicineSearchTable.horizontalHeaderItem(6)
        self.MedicineSearchTable.setColumnWidth(0,100)
        self.MedicineSearchTable.setColumnWidth(1, 300)
        self.MedicineSearchTable.setColumnWidth(2, 150)
        self.MedicineSearchTable.setColumnWidth(4, 150)
        self.MedicineSearchTable.setColumnWidth(5, 150)
        self.MedicineSearchTable.setColumnWidth(6, 150)
        self.MedicineSearchTable.setColumnWidth(7, 150)
        item.setText(_translate("DispensaryMainWindow", "Expiary Date"))
        self.filterComboBox.setItemText(0, _translate("DispensaryMainWindow", "Search By Name"))
        self.filterComboBox.setItemText(1, _translate("DispensaryMainWindow", "All medicines"))
        self.filterComboBox.setItemText(2, _translate("DispensaryMainWindow", "Search By  Id"))
        self.filterComboBox.setItemText(3, _translate("DispensaryMainWindow", "Search by Batch Id"))
        self.filterComboBox.setItemText(4, _translate("DispensaryMainWindow", "Sort by Mf Date"))
        self.filterComboBox.setItemText(5, _translate("DispensaryMainWindow", "Sort by Expiary Date"))
        self.searchButton.setText(_translate("DispensaryMainWindow", "SEARCH"))
        self.searchInput.setPlaceholderText(_translate("DispensaryMainWindow", "Search for Medicines"))
        self.addEventButton.setText(_translate("DispensaryMainWindow", "ADD EVENT"))
        self.searchEventButton.setText(_translate("DispensaryMainWindow", "SEARCH EVENT"))
        self.deletEventButton.setText(_translate("DispensaryMainWindow", "DELETE UPCOMING EVENT"))
        self.allEventButton.setText(_translate("DispensaryMainWindow", "SEE ALL PAST EVENTS"))
        self.editEventButton.setText(_translate("DispensaryMainWindow", "EDIT EVENT"))
        self.allDistributionButton.setText(_translate("DispensaryMainWindow", "SEE ALL DISTRIBUTION"))
        self.createDistributionBillButton.setText(_translate("DispensaryMainWindow", "CREATE DISTRIBUTION BILL"))
        self.searchBillButton.setText(_translate("DispensaryMainWindow", "SEARCH DISTRIBUTION BILL"))
        self.deleteIdInput.setPlaceholderText(_translate("DispensaryMainWindow", "Enter Medicine Id"))
        self.deleteButton.setText(_translate("DispensaryMainWindow", "DELETE"))
        self.setMedicineIdInput.setPlaceholderText(_translate("DispensaryMainWindow", "Enter Medicine Id"))
        self.setQuantityButton.setText(_translate("DispensaryMainWindow", "SET QUANTITY"))
        self.quantityInput.setPlaceholderText(_translate("DispensaryMainWindow", "Quantity"))
        self.newPriceInput.setPlaceholderText(_translate("DispensaryMainWindow", "New Price"))
        self.changePriceIdInput.setPlaceholderText(_translate("DispensaryMainWindow", "Enter Medicine Id"))
        self.changePriceButton.setText(_translate("DispensaryMainWindow", "CHANGE PRICE"))
        self.change_password_button.setText(_translate("DispensaryMainWindow", "CHANGE PASSWORD"))
        self.editDetialsButton.setText(_translate("DispensaryMainWindow", "EDIT PERSONAL DETAILS"))
        self.addMedicineButton.setText(_translate("DispensaryMainWindow", "ADD NEW MEDICINE"))

        ##################################################################################

        self.events(DispensaryMainWindow)

    def events(self,DispensaryMainWindow):
        self.MedicineSearchTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Refresh and Logout Button Icon Setup

        self.logoutButton.setIcon(QIcon('Images/LogoutIcon.png'))
        self.refreshButton.setIcon(QIcon('Images/refreshIcon.png'))
        self.refreshButton.setIconSize(QSize(51, 41))
        self.logoutButton.setIconSize(QSize(51, 41))
        self.logoutButton.setStyleSheet("background: rgb(66, 140, 244);")
        self.refreshButton.setStyleSheet("background: rgb(66, 140, 244);")

        # Add Event Method

        self.addEventButton.clicked.connect(lambda :self.eventAddFunction(DispensaryMainWindow))

        # Log Out Method

        self.logoutButton.clicked.connect(lambda: self.logoutFunction(DispensaryMainWindow))

        # Refresh Method

        self.refreshButton.clicked.connect(lambda: self.refreshFunction(DispensaryMainWindow))

        # Password Change Method

        self.change_password_button.clicked.connect(lambda: self.changePasswordFunction(DispensaryMainWindow))

        self.addMedicineButton.clicked.connect(lambda : self.addMedicineEventFunction(DispensaryMainWindow))

    # Event Add Functionality

    def eventAddFunction(self, MainWindow):
        self.window = QtWidgets.QDialog()
        self.dialog = Ui_EventDialog()
        self.dialog.setupUi(self.window)
        self.window.setModal(True)
        self.window.setWindowTitle("Add Event")
        self.window.show()

    # Delete Event Functionality

    def deleteEventFunction(self, MainWindow):
        pass

    # Logout Functionality

    def logoutFunction(self,MainWindow):
        MainWindow.loginpage.setupUi(MainWindow)

    # Refresh Functionality

    def refreshFunction(self,MainWindow):
        ### Nothing to Do Here ###
        pass

    # Change Password functionality

    def changePasswordFunction(self,MainWindow):

        # Database Check Hoga abhi Yaha
        # To find old password so that it can be transfer to Dilaog Box

        old_password = "1234"
        self.window = QtWidgets.QDialog()
        self.dialog = Ui_password_changebox()
        self.dialog.setupUi(self.window,old_password)
        self.window.setModal(True)
        self.window.setWindowTitle("Change Password")
        self.window.show()

    def addMedicineEventFunction(self,MainWindow):
        self.window = QtWidgets.QDialog()
        self.dialog = Ui_addNewMedicineDialog()
        self.dialog.setupUi(self.window)
        self.window.show()


