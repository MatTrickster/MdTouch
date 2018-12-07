# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BloodbakMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FingureCanvas
from matplotlib.figure import Figure
import matplotlib
from matplotlib import *
from DialogBox.BloodDonationRecieptDialogBox import *
from DialogBox.changePassword import *
from DialogBox.EventDialogBox import *
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from DialogBox.eventViewDialogBox import *

class Canvas(FingureCanvas):
    def __init__(self, parent = None, width =5, height = 5, dpi =100):

        fig = Figure(figsize=(width, height), dpi=dpi)
        #self.axes = fig.add_subplot(111)
        a = fig.add_subplot(111)
        self.axes = fig.add_subplot(111)
        # Example data
        people = ('A+', 'A-', 'B+', 'B-', 'AB+','AB-','O+','O-')
        y_pos = np.arange(len(people))
        #performance = 3 + 10 * np.random.rand(len(people))

        # blood bank data fetched from the database


        performance = [15,223,893,422,51,116,993,715]




        #error = np.random.rand(len(people))
        self.axes.barh(y_pos, performance, align='center',color='red', ecolor='black')
        self.axes.set_yticks(y_pos)
        self.axes.set_yticklabels(people)
        self.axes.invert_yaxis()  # labels read top-to-bottom
        self.axes.set_xlabel('Quantity in Litre')
        self.axes.set_title('Blood Quantity Table')

        FingureCanvas.__init__(self, fig)
        FingureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FingureCanvas.updateGeometry(self)
        #self.setParent(parent)

        #self.plot()



    def plot(self):
        x = np.array([50, 30, 25])

        labels = ['Apples', 'Bananas', 'Melons']
        ax = self.figure.add_subplot(111)




        ax.pie(x, labels=labels)

class Ui_BloodBankMainWindow(object):
    def setupUi(self, BloodBankMainWindow):
        BloodBankMainWindow.setObjectName("BloodBankMainWindow")
        BloodBankMainWindow.resize(1390, 915)
        #BloodBankMainWindow.setStyleSheet("background: rgb(66, 140, 244);")
        self.centralwidget = QtWidgets.QWidget(BloodBankMainWindow)
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
        self.bloodbankNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.bloodbankNameLabel.setGeometry(QtCore.QRect(10, 120, 1371, 31))
        self.bloodbankNameLabel.setStyleSheet("text-transform : uppercase;\n"
"text-decoration : underline;\n"
"font: 75 20pt \"URW Bookman L\";")
        self.bloodbankNameLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.bloodbankNameLabel.setObjectName("bloodbankNameLabel")
        self.logoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logoutButton.setGeometry(QtCore.QRect(1338, 0, 51, 41))
        self.logoutButton.setText("")
        self.logoutButton.setObjectName("logoutButton")
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(1290, 0, 51, 41))
        self.refreshButton.setText("")
        self.refreshButton.setObjectName("refreshButton")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 120, 264, 800))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.organiseCampsButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        #self.organiseCampsButton.setStyleSheet("background : rgb(225,225,220);")
        self.organiseCampsButton.setObjectName("organiseCampsButton")
        self.verticalLayout_2.addWidget(self.organiseCampsButton)
        self.searchCampButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        #self.searchCampButton.setStyleSheet("background : rgb(225,225,220);")
        self.searchCampButton.setObjectName("searchCampButton")
        self.verticalLayout_2.addWidget(self.searchCampButton)

        self.entryBloodLoss = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        #self.entryBloodLoss.setStyleSheet("background : rgb(225,225,220);")
        self.entryBloodLoss.setObjectName("entryBloodLossButton")
        self.entryBloodLoss.setText("ENTRY BLOOD LOSS DETAILS")
        self.verticalLayout_2.addWidget(self.entryBloodLoss)

        self.seeBloodStatsButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        #self.seeBloodStatsButton.setStyleSheet("background : rgb(225,225,220);")
        self.seeBloodStatsButton.setObjectName("seeBloodStatsButton")
        self.seeBloodStatsButton.setText("BLOOD REPORTS MONTH WISE")
        self.verticalLayout_2.addWidget(self.seeBloodStatsButton)

        self.deletecamButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        #self.deletecamButton.setStyleSheet("background : rgb(225,225,220);")
        self.deletecamButton.setObjectName("deletecamButton")
        self.verticalLayout_2.addWidget(self.deletecamButton)
        self.allCampButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        #self.allCampButton.setStyleSheet("background : rgb(225,225,220);")
        self.allCampButton.setObjectName("allCampButton")
        self.verticalLayout_2.addWidget(self.allCampButton)
        self.editCampButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        #self.editCampButton.setStyleSheet("background : rgb(225,225,220);")
        self.editCampButton.setObjectName("editCampButton")
        self.verticalLayout_2.addWidget(self.editCampButton)
        self.editBankDetailsButton = QtWidgets.QPushButton(self.centralwidget)
        self.editBankDetailsButton.setGeometry(QtCore.QRect(1100, 730, 262, 25))
        self.editBankDetailsButton.setStyleSheet("background : rgb(225,225,220);")
        #self.editBankDetailsButton.setObjectName("editBankDetailsButton")
        self.change_password_button = QtWidgets.QPushButton(self.centralwidget)
        self.change_password_button.setGeometry(QtCore.QRect(1100, 850, 262, 25))
        #self.change_password_button.setStyleSheet("background : rgb(225,225,220);")
        self.change_password_button.setObjectName("change_password_button")
        self.addBloodButton = QtWidgets.QPushButton(self.centralwidget)
        self.addBloodButton.setGeometry(QtCore.QRect(1090, 350, 262, 25))
        #self.addBloodButton.setStyleSheet("background : rgb(225,225,220);")
        self.addBloodButton.setObjectName("addBloodButton")

        self.logoutButton.setIcon(QIcon('Images/LogoutIcon.png'))
        self.refreshButton.setIcon(QIcon('Images/refreshIcon.png'))
        self.refreshButton.setIconSize(QSize(51, 41))
        self.logoutButton.setIconSize(QSize(51, 41))
        #self.logoutButton.setStyleSheet("background: rgb(66, 140, 244);")
        #self.refreshButton.setStyleSheet("background: rgb(66, 140, 244);")
        
        #self.layout = QVBoxLayout(self.centralwidget)
        #self.layout.setGeometry(QtCore.QRect(339, 180, 711, 681))

        #self.widget = QWidget()
        #self.layout.addWidget(self.widget)
        #self.widget.setGeometry(QtCore.QRect(339, 180, 711, 681))
        ########################################


        #self.BloodGraphView = QVBoxLayout()
        #self.BloodGraphView.setObjectName("BloodGraphView")
        #self.BloodGraphView = QtWidgets.QWidget(self.centralwidget)
        #self.BloodGraphView.setGeometry(QtCore.QRect(339, 180, 711, 681))
        #self.BloodGraphView.setObjectName("BloodGraphView")
        self.quantitylabel = QtWidgets.QLabel(self.centralwidget)
        self.quantitylabel.setGeometry(QtCore.QRect(340, 870, 711, 31))
        self.quantitylabel.setStyleSheet("text-transform : uppercase;\n"
"text-decoration : underline;\n"
"font: 75 20pt \"URW Bookman L\";")
        self.quantitylabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.quantitylabel.setObjectName("quantitylabel")
        self.searchBloodRecieptButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchBloodRecieptButton.setGeometry(QtCore.QRect(1100, 600, 262, 25))
        #self.searchBloodRecieptButton.setStyleSheet("background : rgb(225,225,220);")
        self.searchBloodRecieptButton.setObjectName("searchBloodRecieptButton")
        self.allBloodTransferButton = QtWidgets.QPushButton(self.centralwidget)
        self.allBloodTransferButton.setGeometry(QtCore.QRect(1090, 460, 262, 25))
        #self.allBloodTransferButton.setStyleSheet("background : rgb(225,225,220);")
        self.allBloodTransferButton.setObjectName("allBloodTransferButton")
        self.createBloodRecieptButton = QtWidgets.QPushButton(self.centralwidget)
        self.createBloodRecieptButton.setGeometry(QtCore.QRect(1090, 220, 262, 25))
        #self.createBloodRecieptButton.setStyleSheet("background : rgb(225,225,220);")
        self.createBloodRecieptButton.setObjectName("createBloodRecieptButton")
        BloodBankMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(BloodBankMainWindow)
        QtCore.QMetaObject.connectSlotsByName(BloodBankMainWindow)

    def retranslateUi(self, BloodBankMainWindow):
        _translate = QtCore.QCoreApplication.translate
        BloodBankMainWindow.setWindowTitle(_translate("BloodBankMainWindow", "MainWindow"))
        self.Logo.setText(_translate("BloodBankMainWindow", "Md Touch"))
        self.bloodbankNameLabel.setText(_translate("BloodBankMainWindow", "BLOOD BANK CENTER NAME"))
        self.organiseCampsButton.setText(_translate("BloodBankMainWindow", "ORGANISE BLOOD CAMPS"))
        self.searchCampButton.setText(_translate("BloodBankMainWindow", "SEARCH BLOOD CAMPS"))
        self.deletecamButton.setText(_translate("BloodBankMainWindow", "DELETE UPCOMING CAMPS"))
        self.allCampButton.setText(_translate("BloodBankMainWindow", "SEE ALL  CAMPS"))
        self.editCampButton.setText(_translate("BloodBankMainWindow", "EDIT BLOOD CAMP"))
        self.editBankDetailsButton.setText(_translate("BloodBankMainWindow", "EDIT BLOOD BANK  DETAILS"))
        self.change_password_button.setText(_translate("BloodBankMainWindow", "CHANGE PASSWORD"))
        self.addBloodButton.setText(_translate("BloodBankMainWindow", "ADD BLOOD DONATION DETAILS"))
        self.quantitylabel.setText(_translate("BloodBankMainWindow", "QUANTITY  GRAPH"))
        self.searchBloodRecieptButton.setText(_translate("BloodBankMainWindow", "SEARCH BLOOD RECIEPT"))
        self.allBloodTransferButton.setText(_translate("BloodBankMainWindow", "SEE ALL BLOOD TRANSFER"))
        self.createBloodRecieptButton.setText(_translate("BloodBankMainWindow", "CREATE BLOOD TRANSFER RECIEPT"))

        ##############################################
        self.events(BloodBankMainWindow)

    ####################################

    def events(self,BloodBankMainWindow):


        # Blood Bank Data View Start

        self.widget = QWidget(self.centralwidget)
        self.layout = QVBoxLayout()
        self.widget.setGeometry(QRect(339, 180, 711, 681))
        #self.widget.setStyleSheet("background:rgb(255,255,255);")
        self.canvas = Canvas()
        self.layout.addWidget(self.canvas)
        self.widget.setLayout(self.layout)

        # Blood Bank Data View End

        # Add Blood

        self.addBloodButton.clicked.connect(lambda : self.addBloodFunction(BloodBankMainWindow))

        # Change Password

        self.change_password_button.clicked.connect(lambda : self.changePasswordFunction(BloodBankMainWindow))

        # Logout functionality

        self.logoutButton.clicked.connect(lambda: self.logoutFunction(BloodBankMainWindow))

        # Refresh Method

        self.refreshButton.clicked.connect(lambda : self.refreshFunction(BloodBankMainWindow))

        # Add Camps

        self.organiseCampsButton.clicked.connect(lambda: self.eventAddFunction(BloodBankMainWindow))

        # Search camps

        self.searchCampButton.clicked.connect(lambda : self.searchCampFunction(BloodBankMainWindow))

        # delete Upcoming Camps

        self.deletecamButton.clicked.connect(lambda: self.deleteUpcomingCampFunction(BloodBankMainWindow))

        # See all  Camps

        self.allCampButton.clicked.connect(lambda : self.seeAllCampsFunction(BloodBankMainWindow))

        # Edit BloodCamp

        self.editCampButton.clicked.connect(lambda : self.editCampFunction(BloodBankMainWindow))

        # Create Blood Transfer Reciept

        self.createBloodRecieptButton.clicked.connect(lambda : self.createBloodTransferRecieptFunction(BloodBankMainWindow))

        # See All Blood Transfer

        self.allBloodTransferButton.clicked.connect(lambda : self.seeAllBloodTransferFunction(BloodBankMainWindow))

    def addBloodFunction(self,BloodBankMainWindow):
        self.window = QtWidgets.QDialog()
        self.dialog = Ui_bloodDonationReciept()
        self.dialog.setupUi(self.window)
        self.window.setModal(True)
        self.window.show()

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

    # Logout Functionality

    def logoutFunction(self,MainWindow):
        MainWindow.loginpage.setupUi(MainWindow)


    # Refresh Functionality

    def refreshFunction(self,MainWindow):
        ### Nothing to Do Here ###
        pass

    # Event Add Functionality

    def eventAddFunction(self, MainWindow):
        self.window = QtWidgets.QDialog()
        self.dialog = Ui_EventDialog()
        self.dialog.setupUi(self.window)
        self.window.setModal(True)
        self.window.setWindowTitle("Add Event")
        self.window.show()

    # Search camps

    def searchCampFunction(self,BloodBankMainWindow):
        self.window = QtWidgets.QDialog()
        self.dialog = Ui_EventListDialog()
        self.dialog.setupUi(self.window)
        self.window.show()

    # delete Upcoming camps

    def deleteUpcomingCampFunction(self,BloodBankMainWindow):
        pass

    # See All camps Function

    def seeAllCampsFunction(self,BloodBankMainWindow):
        self.window = QtWidgets.QDialog()
        self.dialog = Ui_EventListDialog()
        self.dialog.setupUi(self.window)
        self.window.show()



    # Edit blood camp

    def editCampFunction(self,BloodBankMainWindow):
        pass

    # Create BloodTransfer Recipet

    def createBloodTransferRecieptFunction(self,BloodBankMainWindow):
        pass

    # See All Transfer

    def seeAllBloodTransferFunction(self,BloodbankMainWindow):
        pass




