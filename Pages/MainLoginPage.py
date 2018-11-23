# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainLoginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from DialogBox.WrongPasswordErrorWindow import *
from DialogBox.SuccessfulRegistrationDialogBox import *
import psycopg2 as pg2
from Pages.superadminmainPage import *
from Pages.DispensaryMainPage import *
from Pages.BloodBankMainWindow import *


class HoverButton(QPushButton):
    def __init__(self, parent=None):
        QPushButton.__init__(self, parent)
        self.setMouseTracking(True)


class Ui_MainLoginWindow(object):
    def setupUi(self, MainLoginWindow):
        MainLoginWindow.setObjectName("MainLoginWindow")
        MainLoginWindow.resize(1387, 915)
        MainLoginWindow.setStyleSheet("background: rgb(66, 140, 244);")
        self.centralwidget = QtWidgets.QWidget(MainLoginWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(460, 50, 521, 121))
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
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(640, 480, 201, 31))
        self.loginButton.setStyleSheet("\n"
"font: 75 20pt \"URW Bookman L\";")
        self.loginButton.setObjectName("loginButton")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(440, 370, 171, 31))
        self.usernameLabel.setStyleSheet("\n"
"font: 75 20pt \"URW Bookman L\";")
        self.usernameLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.usernameLabel.setObjectName("usernameLabel")
        self.userNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.userNameInput.setGeometry(QtCore.QRect(630, 370, 471, 31))
        self.userNameInput.setStyleSheet("border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: rgb(211, 215, 207);\n"
"    selection-background-color: darkgray;")
        self.userNameInput.setText("")
        self.userNameInput.setObjectName("userNameInput")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(440, 420, 171, 31))
        self.passwordLabel.setStyleSheet("\n"
"font: 75 20pt \"URW Bookman L\";")
        self.passwordLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(630, 420, 471, 31))
        self.passwordInput.setStyleSheet("border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: rgb(211, 215, 207);\n"
"    selection-background-color: darkgray;\n"
"lineedit-password-character: 9679;")
        self.passwordInput.setText("")
        self.passwordInput.setObjectName("passwordInput")
        self.forgotPasswordLink = HoverButton(self.centralwidget)
        self.forgotPasswordLink.setGeometry(QtCore.QRect(440, 480, 171, 25))
        self.forgotPasswordLink.setStyleSheet("COLOR : RED;\n"
"border-top: 3px transparent;\n"
"border-bottom: 3px transparent;\n"
"font: 57 oblique 11pt \"Tlwg Typo\";\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;\n"
"text-decoration : underline;")
        self.forgotPasswordLink.setObjectName("forgotPasswordLink")
        MainLoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainLoginWindow)
        QtCore.QMetaObject.connectSlotsByName(MainLoginWindow)

    def retranslateUi(self, MainLoginWindow):
        _translate = QtCore.QCoreApplication.translate
        MainLoginWindow.setWindowTitle(_translate("MainLoginWindow", "MainWindow"))
        self.Logo.setText(_translate("Ma   inLoginWindow", "Md Touch"))
        self.loginButton.setText(_translate("MainLoginWindow", "LOGIN"))
        self.usernameLabel.setText(_translate("MainLoginWindow", "USERNAME"))
        self.passwordLabel.setText(_translate("MainLoginWindow", "PASSWORD"))
        self.forgotPasswordLink.setText(_translate("MainLoginWindow", "FORGOT PASSWORD?"))

        self.eventsUi(MainLoginWindow)
        #self.loginEvent(MainLoginWindow)


    def eventsUi(self,MainLoginWindow):
        self.forgotPasswordLink.clicked.connect(lambda:self.forgotPasswordEvent(MainLoginWindow))
        self.loginButton.clicked.connect(lambda : self.loginEvent(MainLoginWindow))


    def forgotPasswordEvent(self,MainLoginWindow):

        # forgot Password Email Sent

        try :
            self.window = QtWidgets.QDialog()
            self.dialog = Ui_Successful_registration()
            self.dialog.setupUi(self.window,"The link to generate new password is sent to your email")
            self.window.setModal(True)
            self.window.setWindowTitle("Message Box")
            self.window.show()

        except:
            self.window = QtWidgets.QDialog()
            self.dialog = Ui_Successful_registration()
            self.dialog.setupUi(self.window, "Something happend with connection Try Again! Check Your Internet Connection")
            self.window.setModal(True)
            self.window.setWindowTitle("Message Box")
            self.window.show()

    def loginEvent(self,MainLoginWindow):
        #self.bloodbankadminpage = Ui_BloodBankMainWindow()
        #self.bloodbankadminpage.setupUi(MainLoginWindow)
        #return
        # Database Connectivity
        #################################
        #
        #
        #
        #
        #################################
        #try:

        conn = pg2.connect(database='MDTouch', user='postgres', password='abhi2109')
        cur = conn.cursor()
        username = self.userNameInput.text()
        password = self.passwordInput.text()
        if username == '' or password == '':
            self.window = QtWidgets.QDialog()
            self.dialog = Ui_Successful_registration()
            self.dialog.setupUi(self.window, "Please fill all the details")
            self.window.setModal(True)
            self.window.setWindowTitle("Message Box")
            self.window.show()
            return

        cur.execute('''select dept from "MDTouch_login" where username = '{}' and password = '{}';'''.format(username, password))
        l = cur.fetchall()

        # Please Delete This Line OtherWise You will be Fucked
        ############################################################
        #l.append(['D'])
        ###############################################################
        if len(l) == 0:
            self.window = QtWidgets.QDialog()
            self.dialog = Ui_Successful_registration()
            self.dialog.setupUi(self.window, "Username and Password Does not match")
            self.window.setModal(True)
            self.window.setWindowTitle("Message Box")
            self.window.show()
        elif l[0][0] == 'SA':
            self.superadminmainpage = Ui_MainWindow()
            self.superadminmainpage.setupUi(MainLoginWindow)
        elif l[0][0] == 'D':
            self.dispemsaryadminpage = Ui_DispensaryMainWindow()
            self.dispemsaryadminpage.setupUi(MainLoginWindow,"Dispensary Name")
        elif l[0][0] == 'B':
            self.bloodbankadminpage = Ui_BloodBankMainWindow()
            self.bloodbankadminpage.setupUi(MainLoginWindow)
        elif l[0][0] == 'D':
            # Doctor Ka Kholna hai
            pass
        elif l[0][0] == 'T':
            # Open Test Center
            pass
        elif l[0][0] == 'ES':
            #Open Emergency Services
        else:
            # Nothing


        conn.close()
        #except:
            #self.window = QtWidgets.QDialog()
            #self.dialog = Ui_Successful_registration()
            #self.dialog.setupUi(self.window,"Something happend with connection Try Again! Check Your Internet Connection")
            #self.window.setModal(True)
            #self.window.setWindowTitle("Message Box")
            #self.window.show()


