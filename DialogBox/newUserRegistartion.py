from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2 as pg2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class newuseraddadmin():
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(857, 471)
        Dialog.setMinimumSize(QtCore.QSize(857, 471))
        Dialog.setWindowTitle("Add New User")
        self.adduserlogo = QtWidgets.QLabel(Dialog)
        self.adduserlogo.setGeometry(QtCore.QRect(10, 10, 841, 51))
        self.adduserlogo.setStyleSheet("font: 75 19pt \"Ubuntu Mono\";")
        self.adduserlogo.setAlignment(QtCore.Qt.AlignCenter)
        self.adduserlogo.setObjectName("adduserlogo")
        self.logo_line = QtWidgets.QFrame(Dialog)
        self.logo_line.setGeometry(QtCore.QRect(350, 50, 151, 20))
        self.logo_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.logo_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.logo_line.setObjectName("logo_line")
        self.dept_inputcombobox = QtWidgets.QComboBox(Dialog)
        self.dept_inputcombobox.setGeometry(QtCore.QRect(420, 130, 231, 25))
        self.dept_inputcombobox.setObjectName("dept_inputcombobox")
        self.dept_inputcombobox.addItem('Doctor')
        self.dept_inputcombobox.addItem('Hospital Manager')
        self.dept_inputcombobox.addItem('Dispensaries')
        self.dept_inputcombobox.addItem('Emergency Services')
        self.dept_inputcombobox.addItem('Blood Bank Centers')
        self.dept_inputcombobox.addItem('Admin')
        self.dept_inputcombobox.addItem('Test Center')
        self.dept_label = QtWidgets.QLabel(Dialog)
        self.dept_label.setGeometry(QtCore.QRect(220, 120, 171, 41))
        self.dept_label.setStyleSheet("font: 57 17pt \"Ubuntu\";")
        self.dept_label.setObjectName("dept_label")
        self.email_label = QtWidgets.QLabel(Dialog)
        self.email_label.setGeometry(QtCore.QRect(220, 190, 171, 41))
        self.email_label.setStyleSheet("font: 57 17pt \"Ubuntu\";")
        self.email_label.setObjectName("email_label")
        self.password_label = QtWidgets.QLabel(Dialog)
        self.password_label.setGeometry(QtCore.QRect(220, 250, 171, 41))
        self.password_label.setStyleSheet("font: 57 17pt \"Ubuntu\";")
        self.password_label.setObjectName("password_label")
        self.email_inputbox = QtWidgets.QLineEdit(Dialog)
        self.email_inputbox.setGeometry(QtCore.QRect(420, 200, 361, 25))
        self.email_inputbox.setObjectName("email_inputbox")
        self.password_inputbox = QtWidgets.QLineEdit(Dialog)
        self.password_inputbox.setGeometry(QtCore.QRect(420, 260, 361, 25))
        self.password_inputbox.setObjectName("password_inputbox")
        self.create_user_button = QtWidgets.QPushButton(Dialog)
        self.create_user_button.setGeometry(QtCore.QRect(340, 364, 171, 31))
        self.create_user_button.setStyleSheet("background:rgb(114, 159, 207);")
        self.create_user_button.setObjectName("create_user_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.adduserlogo.setText(_translate("Dialog", "ADD NEW USER "))
        self.dept_label.setText(_translate("Dialog", "Department :"))
        self.email_label.setText(_translate("Dialog", "New Email :"))
        self.password_label.setText(_translate("Dialog", "Password :"))
        self.create_user_button.setText(_translate("Dialog", "CREATE USER"))

        self.actions(Dialog)


    def actions(self,Dialog):

        self.create_user_button.clicked.connect(lambda: self.exitdialog(Dialog))

    def exitdialog(self,Dialog):
        pass






