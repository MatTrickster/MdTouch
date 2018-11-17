from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import psycopg2 as pg2
from DialogBox.SuccessfulRegistrationDialogBox import *

class Ui_password_changebox(object):

    # Takes parameter extra as user_id


    def setupUi(self, password_changebox,user_id):
        password_changebox.setObjectName("password_changebox")
        password_changebox.resize(625, 424)
        self.email_label = QtWidgets.QLabel(password_changebox)
        self.email_label.setGeometry(QtCore.QRect(100, 100, 91, 31))
        self.email_label.setStyleSheet("font: 57 17pt \"Ubuntu\";")
        self.email_label.setObjectName("email_label")
        self.details_label = QtWidgets.QLabel(password_changebox)
        self.details_label.setGeometry(QtCore.QRect(20, 30, 581, 31))
        self.details_label.setStyleSheet("font: 57 17pt \"Ubuntu\";")
        self.details_label.setAlignment(QtCore.Qt.AlignCenter)
        self.details_label.setObjectName("details_label")
        self.email_inputbox = QtWidgets.QLineEdit(password_changebox)
        self.email_inputbox.setGeometry(QtCore.QRect(220, 100, 391, 31))
        self.email_inputbox.setText("")
        self.email_inputbox.setObjectName("email_inputbox")
        self.oldpass_label = QtWidgets.QLabel(password_changebox)
        self.oldpass_label.setGeometry(QtCore.QRect(30, 150, 161, 31))
        self.oldpass_label.setStyleSheet("font: 57 17pt \"Ubuntu\";")
        self.oldpass_label.setObjectName("oldpass_label")
        self.newpass_label = QtWidgets.QLabel(password_changebox)
        self.newpass_label.setGeometry(QtCore.QRect(30, 210, 181, 31))
        self.newpass_label.setStyleSheet("font: 57 17pt \"Ubuntu\";")
        self.newpass_label.setObjectName("newpass_label")
        self.newpass_label2 = QtWidgets.QLabel(password_changebox)
        self.newpass_label2.setGeometry(QtCore.QRect(30, 270, 181, 31))
        self.newpass_label2.setStyleSheet("font: 57 17pt \"Ubuntu\";")
        self.newpass_label2.setObjectName("newpass_label2")
        self.oldpassword_inputbox = QtWidgets.QLineEdit(password_changebox)
        self.oldpassword_inputbox.setGeometry(QtCore.QRect(220, 150, 391, 31))
        self.oldpassword_inputbox.setObjectName("oldpassword_inputbox")
        self.newpassword_inputbox2 = QtWidgets.QLineEdit(password_changebox)
        self.newpassword_inputbox2.setGeometry(QtCore.QRect(220, 270, 391, 31))
        self.newpassword_inputbox2.setObjectName("newpassword_inputbox2")
        self.newpassword_inputbox = QtWidgets.QLineEdit(password_changebox)
        self.newpassword_inputbox.setGeometry(QtCore.QRect(220, 210, 391, 31))
        self.newpassword_inputbox.setObjectName("newpassword_inputbox")
        self.message_label = QtWidgets.QLabel(password_changebox)
        self.message_label.setGeometry(QtCore.QRect(20, 390, 591, 17))
        self.message_label.setStyleSheet("color :rgb(239, 41, 41);")
        self.message_label.setAlignment(QtCore.Qt.AlignCenter)
        self.message_label.setObjectName("message_label")
        self.changepasswordbutton = QtWidgets.QPushButton(password_changebox)
        self.changepasswordbutton.setGeometry(QtCore.QRect(190, 330, 201, 31))
        self.changepasswordbutton.setStyleSheet("background:rgb(114, 159, 207);")
        self.changepasswordbutton.setObjectName("changepasswordbutton")

        self.retranslateUi(password_changebox,user_id)
        QtCore.QMetaObject.connectSlotsByName(password_changebox)

    def retranslateUi(self, password_changebox,user_id):
        _translate = QtCore.QCoreApplication.translate
        password_changebox.setWindowTitle(_translate("password_changebox", "Dialog"))
        self.email_label.setText(_translate("password_changebox", "   Email  :"))
        self.details_label.setText(_translate("password_changebox", "Enter Your Details "))
        self.oldpass_label.setText(_translate("password_changebox", " Old Password  :"))
        self.newpass_label.setText(_translate("password_changebox", "New Password  :"))
        self.newpass_label2.setText(_translate("password_changebox", "New Password  :"))
        #self.message_label.setText(_translate("password_changebox", "Wrong Details"))
        self.changepasswordbutton.setText(_translate("password_changebox", "CHANGE PASSWORD"))
        self.actions(password_changebox,user_id)


    def actions(self,password_changebox,user_id):
        self.changepasswordbutton.clicked.connect(lambda : self.changepassword_func(password_changebox,user_id))

    def changepassword_func(self,password_changebox,user_id):


        # DataBase Check

        conn = pg2.connect(database='MdTouch', user='postgres', password='abhi2109')
        cur = conn.cursor()
        email = self.email_inputbox.text()
        old_password = self.oldpassword_inputbox.text()
        new_pasword = self.newpassword_inputbox.text()
        new_pasword2 = self.newpassword_inputbox2.text()
        cur.execute("SELECT email,password FROM login where id = {}".format(user_id))
        l = cur.fetchall()
        conn.close()
        if email != l[0][0]:
            self.message_label.setText("The Email Does not matched to your account !")
        elif old_password != l[0][1]:
            self.message_label.setText("Old Password is incorrect !")
        elif new_pasword != new_pasword2:
            self.message_label.setText("Please re-enter the new password.")
        else:
            conn = pg2.connect(database='MDTouch', user='postgres', password='abhi2109')
            cur = conn.cursor()
            cur.execute("UPDATE login SET password = '{}' WHERE id = {}".format(new_pasword,user_id))
            conn.commit()
            conn.close()
            password_changebox.close()
            self.window = QtWidgets.QDialog()
            self.dialog = Ui_Successful_registration()
            self.dialog.setupUi(self.window,"Your Password is changed")
            self.window.setModal(True)
            self.window.show()

