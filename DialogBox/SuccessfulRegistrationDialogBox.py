from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Successful_registration(object):
    def setupUi(self, Successful_registration,text):
        Successful_registration.setObjectName("Successful_registration")
        Successful_registration.resize(810, 124)
        Successful_registration.setWindowTitle("Message Box")
        self.Successful_label = QtWidgets.QLabel(Successful_registration)
        self.Successful_label.setGeometry(QtCore.QRect(80, 30, 661, 31))
        self.Successful_label.setStyleSheet("color :rgb(32, 74, 135);")
        self.Successful_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Successful_label.setObjectName("Successful_label")
        self.closebutton = QtWidgets.QPushButton(Successful_registration)
        self.closebutton.setGeometry(QtCore.QRect(350, 80, 89, 25))
        self.closebutton.setStyleSheet("\n"
"background:rgb(114, 159, 207);")
        self.closebutton.setObjectName("closebutton")

        self.retranslateUi(Successful_registration,text)
        QtCore.QMetaObject.connectSlotsByName(Successful_registration)

    def retranslateUi(self, Successful_registration,text):
        _translate = QtCore.QCoreApplication.translate
        Successful_registration.setWindowTitle(_translate("Successful_registration", "Dialog"))
        self.Successful_label.setText(_translate("Successful_registration",text))
        self.closebutton.setText(_translate("Successful_registration", "CLOSE"))
        self.closebutton.clicked.connect(lambda :self.close(Successful_registration))

    def close(self,Dialog):
        Dialog.close()