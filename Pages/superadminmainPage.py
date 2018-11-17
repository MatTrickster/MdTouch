# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'superadminMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2 as pg2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from DialogBox.changePassword import *
from DialogBox.EventDialogBox import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1390, 915)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background: rgb(66, 140, 244);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(430, 0, 521, 121))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.logoLabel.setFont(font)
        self.logoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.logoLabel.setObjectName("logoLabel")
        self.superadminLabel = QtWidgets.QLabel(self.centralwidget)
        self.superadminLabel.setGeometry(QtCore.QRect(490, 120, 371, 31))
        self.superadminLabel.setStyleSheet("text-decoration: underline;\n"
"font: 75 20pt \"URW Bookman L\";")
        self.superadminLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.superadminLabel.setObjectName("superadminLabel")
        self.logoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logoutButton.setGeometry(QtCore.QRect(1338, 0, 51, 41))
        self.logoutButton.setObjectName("logoutButton")
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(1290, 0, 51, 41))
        self.refreshButton.setObjectName("refreshButton")

        # Refresh and Logout Button Icon Setup

        self.logoutButton.setIcon(QIcon('Images/LogoutIcon.png'))
        self.refreshButton.setIcon(QIcon('Images/refreshIcon.png'))
        self.refreshButton.setIconSize(QSize(51,41))
        self.logoutButton.setIconSize(QSize(51,41))
        self.logoutButton.setStyleSheet("background: rgb(66, 140, 244);")
        self.refreshButton.setStyleSheet("background: rgb(66, 140, 244);")

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(860, 210, 251, 701))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.search_hospital_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.search_hospital_button.setStyleSheet("background : rgb(225,225,220);")
        self.search_hospital_button.setObjectName("search_hospital_button")
        self.verticalLayout_4.addWidget(self.search_hospital_button)
        self.search_doctor_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.search_doctor_button.setStyleSheet("background : rgb(225,225,220);")
        self.search_doctor_button.setObjectName("search_doctor_button")
        self.verticalLayout_4.addWidget(self.search_doctor_button)
        self.search_testcenter_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.search_testcenter_button.setStyleSheet("background : rgb(225,225,220);")
        self.search_testcenter_button.setObjectName("search_testcenter_button")
        self.verticalLayout_4.addWidget(self.search_testcenter_button)
        self.saerch_specifictest_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.saerch_specifictest_button.setStyleSheet("background : rgb(225,225,220);")
        self.saerch_specifictest_button.setObjectName("saerch_specifictest_button")
        self.verticalLayout_4.addWidget(self.saerch_specifictest_button)
        self.search_emergencyservices_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.search_emergencyservices_button.setStyleSheet("background : rgb(225,225,220);")
        self.search_emergencyservices_button.setObjectName("search_emergencyservices_button")
        self.verticalLayout_4.addWidget(self.search_emergencyservices_button)
        self.search_ambulances_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.search_ambulances_button.setStyleSheet("background : rgb(225,225,220);")
        self.search_ambulances_button.setObjectName("search_ambulances_button")
        self.verticalLayout_4.addWidget(self.search_ambulances_button)
        self.search_bloodbakcenter_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.search_bloodbakcenter_button.setStyleSheet("background : rgb(225,225,220);")
        self.search_bloodbakcenter_button.setObjectName("search_bloodbakcenter_button")
        self.verticalLayout_4.addWidget(self.search_bloodbakcenter_button)
        self.search_bloodsamples_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.search_bloodsamples_button.setStyleSheet("background : rgb(225,225,220);")
        self.search_bloodsamples_button.setObjectName("search_bloodsamples_button")
        self.verticalLayout_4.addWidget(self.search_bloodsamples_button)
        self.search_dispensaries_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.search_dispensaries_button.setStyleSheet("background : rgb(225,225,220);")
        self.search_dispensaries_button.setObjectName("search_dispensaries_button")
        self.verticalLayout_4.addWidget(self.search_dispensaries_button)
        self.search_medicines = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.search_medicines.setStyleSheet("background : rgb(225,225,220);")
        self.search_medicines.setObjectName("search_medicines")
        self.verticalLayout_4.addWidget(self.search_medicines)
        self.search_patient_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.search_patient_button.setStyleSheet("background : rgb(225,225,220);")
        self.search_patient_button.setObjectName("search_patient_button")
        self.verticalLayout_4.addWidget(self.search_patient_button)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(580, 210, 251, 701))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.viewall_administrator_button = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.viewall_administrator_button.setStyleSheet("background : rgb(225,225,220);")
        self.viewall_administrator_button.setObjectName("viewall_administrator_button")
        self.verticalLayout_5.addWidget(self.viewall_administrator_button)
        self.viewall_hospital_button = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.viewall_hospital_button.setStyleSheet("background : rgb(225,225,220);")
        self.viewall_hospital_button.setObjectName("viewall_hospital_button")
        self.verticalLayout_5.addWidget(self.viewall_hospital_button)
        self.viewAllDoctorButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.viewAllDoctorButton.setStyleSheet("background : rgb(225,225,220);")
        self.viewAllDoctorButton.setObjectName("viewAllDoctorButton")
        self.verticalLayout_5.addWidget(self.viewAllDoctorButton)
        self.viewall_testcenter_button = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.viewall_testcenter_button.setStyleSheet("background : rgb(225,225,220);")
        self.viewall_testcenter_button.setObjectName("viewall_testcenter_button")
        self.verticalLayout_5.addWidget(self.viewall_testcenter_button)
        self.viewall_emergencyservices_button = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.viewall_emergencyservices_button.setStyleSheet("background : rgb(225,225,220);")
        self.viewall_emergencyservices_button.setObjectName("viewall_emergencyservices_button")
        self.verticalLayout_5.addWidget(self.viewall_emergencyservices_button)
        self.viewAllEventButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.viewAllEventButton.setStyleSheet("background : rgb(225,225,220);")
        self.viewAllEventButton.setObjectName("viewAllEventButton")
        self.verticalLayout_5.addWidget(self.viewAllEventButton)
        self.viewall_bloodbankcenters_button = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.viewall_bloodbankcenters_button.setStyleSheet("background : rgb(225,225,220);")
        self.viewall_bloodbankcenters_button.setObjectName("viewall_bloodbankcenters_button")
        self.verticalLayout_5.addWidget(self.viewall_bloodbankcenters_button)
        self.viewall_dispensaries_button = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.viewall_dispensaries_button.setStyleSheet("background : rgb(225,225,220);")
        self.viewall_dispensaries_button.setObjectName("viewall_dispensaries_button")
        self.verticalLayout_5.addWidget(self.viewall_dispensaries_button)
        self.viewall_doctors_button = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.viewall_doctors_button.setStyleSheet("background : rgb(225,225,220);")
        self.viewall_doctors_button.setObjectName("viewall_doctors_button")
        self.verticalLayout_5.addWidget(self.viewall_doctors_button)
        self.view_all_medicines = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.view_all_medicines.setStyleSheet("background : rgb(225,225,220);")
        self.view_all_medicines.setObjectName("view_all_medicines")
        self.verticalLayout_5.addWidget(self.view_all_medicines)
        self.view_all_patient = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.view_all_patient.setStyleSheet("background : rgb(225,225,220);")
        self.view_all_patient.setObjectName("view_all_patient")
        self.verticalLayout_5.addWidget(self.view_all_patient)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(1130, 210, 251, 701))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.viewAllRegistrationButton = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.viewAllRegistrationButton.setStyleSheet("background : rgb(225,225,220);")
        self.viewAllRegistrationButton.setObjectName("viewAllRegistrationButton")
        self.verticalLayout_6.addWidget(self.viewAllRegistrationButton)
        self.hospital_records_button = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.hospital_records_button.setStyleSheet("background : rgb(225,225,220);")
        self.hospital_records_button.setObjectName("hospital_records_button")
        self.verticalLayout_6.addWidget(self.hospital_records_button)
        self.testcenters_button = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.testcenters_button.setStyleSheet("background : rgb(225,225,220);")
        self.testcenters_button.setObjectName("testcenters_button")
        self.verticalLayout_6.addWidget(self.testcenters_button)
        self.emergencyservices_records_button = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.emergencyservices_records_button.setStyleSheet("background : rgb(225,225,220);")
        self.emergencyservices_records_button.setObjectName("emergencyservices_records_button")
        self.verticalLayout_6.addWidget(self.emergencyservices_records_button)
        self.eventRecordsButton = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.eventRecordsButton.setStyleSheet("background : rgb(225,225,220);")
        self.eventRecordsButton.setObjectName("eventRecordsButton")
        self.verticalLayout_6.addWidget(self.eventRecordsButton)
        self.bloodbankcenters_records_button = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.bloodbankcenters_records_button.setStyleSheet("background : rgb(225,225,220);")
        self.bloodbankcenters_records_button.setObjectName("bloodbankcenters_records_button")
        self.verticalLayout_6.addWidget(self.bloodbankcenters_records_button)
        self.dispensaries_records_button = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.dispensaries_records_button.setStyleSheet("background : rgb(225,225,220);")
        self.dispensaries_records_button.setObjectName("dispensaries_records_button")
        self.verticalLayout_6.addWidget(self.dispensaries_records_button)
        self.patientRecordButton = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.patientRecordButton.setStyleSheet("background : rgb(225,225,220);")
        self.patientRecordButton.setObjectName("patientRecordButton")
        self.verticalLayout_6.addWidget(self.patientRecordButton)
        self.medicine_records_button = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.medicine_records_button.setStyleSheet("background : rgb(225,225,220);")
        self.medicine_records_button.setObjectName("medicine_records_button")
        self.verticalLayout_6.addWidget(self.medicine_records_button)
        self.doctors_records_button = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.doctors_records_button.setStyleSheet("background : rgb(225,225,220);")
        self.doctors_records_button.setObjectName("doctors_records_button")
        self.verticalLayout_6.addWidget(self.doctors_records_button)
        self.ambulance_records_button = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.ambulance_records_button.setStyleSheet("background : rgb(225,225,220);")
        self.ambulance_records_button.setObjectName("ambulance_records_button")
        self.verticalLayout_6.addWidget(self.ambulance_records_button)
        self.bloodsamples_records_button = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.bloodsamples_records_button.setStyleSheet("background : rgb(225,225,220);")
        self.bloodsamples_records_button.setObjectName("bloodsamples_records_button")
        self.verticalLayout_6.addWidget(self.bloodsamples_records_button)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(300, 210, 262, 701))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.edit_hospital_button = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.edit_hospital_button.setStyleSheet("background : rgb(225,225,220);")
        self.edit_hospital_button.setObjectName("edit_hospital_button")
        self.verticalLayout_7.addWidget(self.edit_hospital_button)
        self.editAdministratorButton = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.editAdministratorButton.setStyleSheet("background : rgb(225,225,220);")
        self.editAdministratorButton.setObjectName("editAdministratorButton")
        self.verticalLayout_7.addWidget(self.editAdministratorButton)
        self.remove_user_button = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.remove_user_button.setStyleSheet("background : rgb(225,225,220);")
        self.remove_user_button.setObjectName("remove_user_button")
        self.verticalLayout_7.addWidget(self.remove_user_button)
        self.editDoctorButton = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.editDoctorButton.setStyleSheet("background : rgb(225,225,220);")
        self.editDoctorButton.setObjectName("editDoctorButton")
        self.verticalLayout_7.addWidget(self.editDoctorButton)
        self.editTestCenterButton = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.editTestCenterButton.setStyleSheet("background : rgb(225,225,220);")
        self.editTestCenterButton.setObjectName("editTestCenterButton")
        self.verticalLayout_7.addWidget(self.editTestCenterButton)
        self.editEsButton = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.editEsButton.setStyleSheet("background : rgb(225,225,220);")
        self.editEsButton.setObjectName("editEsButton")
        self.verticalLayout_7.addWidget(self.editEsButton)
        self.editEventButton = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.editEventButton.setStyleSheet("background : rgb(225,225,220);")
        self.editEventButton.setObjectName("editEventButton")
        self.verticalLayout_7.addWidget(self.editEventButton)
        self.editBbcButton = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.editBbcButton.setStyleSheet("background : rgb(225,225,220);")
        self.editBbcButton.setObjectName("editBbcButton")
        self.verticalLayout_7.addWidget(self.editBbcButton)
        self.editDispensaryButton = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.editDispensaryButton.setStyleSheet("background : rgb(225,225,220);\n"
"")
        self.editDispensaryButton.setObjectName("editDispensaryButton")
        self.verticalLayout_7.addWidget(self.editDispensaryButton)
        self.editAmbulanceButton = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.editAmbulanceButton.setStyleSheet("background : rgb(225,225,220);")
        self.editAmbulanceButton.setObjectName("editAmbulanceButton")
        self.verticalLayout_7.addWidget(self.editAmbulanceButton)
        self.allAppointmentButton = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.allAppointmentButton.setStyleSheet("background : rgb(225,225,220);")
        self.allAppointmentButton.setObjectName("allAppointmentButton")
        self.verticalLayout_7.addWidget(self.allAppointmentButton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 159, 1381, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainMenuLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.mainMenuLabel.setStyleSheet("text-decoration: underline;\n"
"font: 75 20pt \"URW Bookman L\";")
        self.mainMenuLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.mainMenuLabel.setObjectName("mainMenuLabel")
        self.horizontalLayout.addWidget(self.mainMenuLabel)
        self.editMenuLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.editMenuLabel.setStyleSheet("text-decoration: underline;\n"
"font: 75 20pt \"URW Bookman L\";")
        self.editMenuLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.editMenuLabel.setObjectName("editMenuLabel")
        self.horizontalLayout.addWidget(self.editMenuLabel)
        self.viewMenuLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.viewMenuLabel.setStyleSheet("text-decoration: underline;\n"
"font: 75 20pt \"URW Bookman L\";")
        self.viewMenuLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.viewMenuLabel.setObjectName("viewMenuLabel")
        self.horizontalLayout.addWidget(self.viewMenuLabel)
        self.searchMenuLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.searchMenuLabel.setStyleSheet("text-decoration: underline;\n"
"font: 75 20pt \"URW Bookman L\";")
        self.searchMenuLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.searchMenuLabel.setObjectName("searchMenuLabel")
        self.horizontalLayout.addWidget(self.searchMenuLabel)
        self.recordsMenuLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.recordsMenuLabel.setStyleSheet("text-decoration: underline;\n"
"font: 75 20pt \"URW Bookman L\";")
        self.recordsMenuLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.recordsMenuLabel.setObjectName("recordsMenuLabel")
        self.horizontalLayout.addWidget(self.recordsMenuLabel)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 210, 264, 701))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.addNewAdministratorButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.addNewAdministratorButton.setStyleSheet("background : rgb(225,225,220);")
        self.addNewAdministratorButton.setObjectName("addNewAdministratorButton")
        self.verticalLayout_2.addWidget(self.addNewAdministratorButton)
        self.addEventButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.addEventButton.setStyleSheet("background : rgb(225,225,220);")
        self.addEventButton.setObjectName("addEventButton")
        self.verticalLayout_2.addWidget(self.addEventButton)
        self.change_password_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.change_password_button.setStyleSheet("background : rgb(225,225,220);")
        self.change_password_button.setObjectName("change_password_button")
        self.verticalLayout_2.addWidget(self.change_password_button)
        self.addHospitalButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.addHospitalButton.setStyleSheet("background : rgb(225,225,220);")
        self.addHospitalButton.setObjectName("addHospitalButton")
        self.verticalLayout_2.addWidget(self.addHospitalButton)
        self.addDoctorButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.addDoctorButton.setStyleSheet("background : rgb(225,225,220);")
        self.addDoctorButton.setObjectName("addDoctorButton")
        self.verticalLayout_2.addWidget(self.addDoctorButton)
        self.addTestCenterButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.addTestCenterButton.setStyleSheet("background : rgb(225,225,220);")
        self.addTestCenterButton.setObjectName("addTestCenterButton")
        self.verticalLayout_2.addWidget(self.addTestCenterButton)
        self.addBbcButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.addBbcButton.setStyleSheet("background : rgb(225,225,220);")
        self.addBbcButton.setObjectName("addBbcButton")
        self.verticalLayout_2.addWidget(self.addBbcButton)
        self.addEmergencyServicesButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.addEmergencyServicesButton.setStyleSheet("background : rgb(225,225,220);")
        self.addEmergencyServicesButton.setObjectName("addEmergencyServicesButton")
        self.verticalLayout_2.addWidget(self.addEmergencyServicesButton)
        self.addDispensaryButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.addDispensaryButton.setStyleSheet("background : rgb(225,225,220);")
        self.addDispensaryButton.setObjectName("addDispensaryButton")
        self.verticalLayout_2.addWidget(self.addDispensaryButton)
        self.addAmbulanceButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.addAmbulanceButton.setStyleSheet("background : rgb(225,225,220);")
        self.addAmbulanceButton.setObjectName("addAmbulanceButton")
        self.verticalLayout_2.addWidget(self.addAmbulanceButton)
        self.remove_test_button_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.remove_test_button_3.setStyleSheet("background : rgb(225,225,220);")
        self.remove_test_button_3.setObjectName("remove_test_button_3")
        self.verticalLayout_2.addWidget(self.remove_test_button_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logoLabel.setText(_translate("MainWindow", "Md Touch"))
        self.superadminLabel.setText(_translate("MainWindow", "SUPERADMIN PAGE"))
        self.search_hospital_button.setText(_translate("MainWindow", "SEARCH HOSPITAL"))
        self.search_doctor_button.setText(_translate("MainWindow", "SEARCH DOCTOR"))
        self.search_testcenter_button.setText(_translate("MainWindow", "SEARCH TEST CENTERS"))
        self.saerch_specifictest_button.setText(_translate("MainWindow", "SEARCH SPECIFIC TEST"))
        self.search_emergencyservices_button.setText(_translate("MainWindow", "SEARCH EMERGENCY SERVICES"))
        self.search_ambulances_button.setText(_translate("MainWindow", "SEARCH AMBULANCES"))
        self.search_bloodbakcenter_button.setText(_translate("MainWindow", "SEARCH BLOOD BANK CENTERS"))
        self.search_bloodsamples_button.setText(_translate("MainWindow", "SEARCH BLOOD SAMPLES"))
        self.search_dispensaries_button.setText(_translate("MainWindow", "SEARCH DISPENSARIES"))
        self.search_medicines.setText(_translate("MainWindow", "SEARCH MEDICINES"))
        self.search_patient_button.setText(_translate("MainWindow", "SEARCH PATIENT"))
        self.viewall_administrator_button.setText(_translate("MainWindow", "VIEW ALL ADMINISTRATOR"))
        self.viewall_hospital_button.setText(_translate("MainWindow", "VIEW ALL HOSPITAL"))
        self.viewAllDoctorButton.setText(_translate("MainWindow", "VIEW ALL DOCTORS"))
        self.viewall_testcenter_button.setText(_translate("MainWindow", "VIEW ALL TEST CENTERS"))
        self.viewall_emergencyservices_button.setText(_translate("MainWindow", "VIWE ALL EMERGENCY SERVICES"))
        self.viewAllEventButton.setText(_translate("MainWindow", "VIEW ALL EVENTS"))
        self.viewall_bloodbankcenters_button.setText(_translate("MainWindow", "VIEW ALL BLOOD BANK CENTERS"))
        self.viewall_dispensaries_button.setText(_translate("MainWindow", "VIEW ALL DISPENSARIES"))
        self.viewall_doctors_button.setText(_translate("MainWindow", "VIEW ALL DOCTOR"))
        self.view_all_medicines.setText(_translate("MainWindow", "VIEW ALL MEDICINES"))
        self.view_all_patient.setText(_translate("MainWindow", "VIEW ALL PATIENTS"))
        self.viewAllRegistrationButton.setText(_translate("MainWindow", "VIEW ALL REGISTRATIONS"))
        self.hospital_records_button.setText(_translate("MainWindow", " HOSPITAL RECORDS"))
        self.testcenters_button.setText(_translate("MainWindow", " TEST CENTERS RECORDS"))
        self.emergencyservices_records_button.setText(_translate("MainWindow", "EMERGENCY SERVICES RECORDS"))
        self.eventRecordsButton.setText(_translate("MainWindow", "EVENT RECORDS"))
        self.bloodbankcenters_records_button.setText(_translate("MainWindow", "BLOOD BANK CENTERS RECORDS"))
        self.dispensaries_records_button.setText(_translate("MainWindow", " DISPENSARIES RECORDS"))
        self.patientRecordButton.setText(_translate("MainWindow", "PATIENT RECORDS"))
        self.medicine_records_button.setText(_translate("MainWindow", "MEDICINES RECORDS"))
        self.doctors_records_button.setText(_translate("MainWindow", "DOCTOR RECORDS"))
        self.ambulance_records_button.setText(_translate("MainWindow", " AMBULANCE RECORDS"))
        self.bloodsamples_records_button.setText(_translate("MainWindow", "BLOOD SAMPLE RECORDS"))
        self.edit_hospital_button.setText(_translate("MainWindow", "EDIT/VIEW HOSPITAL "))
        self.editAdministratorButton.setText(_translate("MainWindow", "EDIT ADMINISTRATOR"))
        self.remove_user_button.setText(_translate("MainWindow", "REMOVE ADMINISTRATOR"))
        self.editDoctorButton.setText(_translate("MainWindow", "EDIT/VEW DOCTOR"))
        self.editTestCenterButton.setText(_translate("MainWindow", "EDIT/VIEW TEST CENTER "))
        self.editEsButton.setText(_translate("MainWindow", "EDIT/VIEW EMERGENCY SERVICES "))
        self.editEventButton.setText(_translate("MainWindow", "EDIT EVENT"))
        self.editBbcButton.setText(_translate("MainWindow", "EDIT/VIEW BLOOD BANK CENTER "))
        self.editDispensaryButton.setText(_translate("MainWindow", "EDIT/VIEW DISPENSARIES "))
        self.editAmbulanceButton.setText(_translate("MainWindow", "EDIT AMBULANCE "))
        self.allAppointmentButton.setText(_translate("MainWindow", "ALL APPOINTMENTS"))
        self.mainMenuLabel.setText(_translate("MainWindow", "MAIN MENU"))
        self.editMenuLabel.setText(_translate("MainWindow", "EDIT MENU"))
        self.viewMenuLabel.setText(_translate("MainWindow", "VIEW MENU"))
        self.searchMenuLabel.setText(_translate("MainWindow", "SEARCH MENU"))
        self.recordsMenuLabel.setText(_translate("MainWindow", "RECORDS MENU"))
        self.addNewAdministratorButton.setText(_translate("MainWindow", "ADD NEW ADMINISTRATOR"))
        self.addEventButton.setText(_translate("MainWindow", "ADD EVENT"))
        self.change_password_button.setText(_translate("MainWindow", "CHANGE PASSWORD"))
        self.addHospitalButton.setText(_translate("MainWindow", "ADD HOSPITAL"))
        self.addDoctorButton.setText(_translate("MainWindow", "ADD DOCTOR"))
        self.addTestCenterButton.setText(_translate("MainWindow", "ADD TESTCENTER"))
        self.addBbcButton.setText(_translate("MainWindow", "ADD BLOODBANKCENTER"))
        self.addEmergencyServicesButton.setText(_translate("MainWindow", "ADD EMERGENCY SERVICES"))
        self.addDispensaryButton.setText(_translate("MainWindow", "ADD DISPENSARY"))
        self.addAmbulanceButton.setText(_translate("MainWindow", "ADD AMBULANCE "))
        self.remove_test_button_3.setText(_translate("MainWindow", "ADD NURSE"))

###################################################################################################################
###################################################################################################################
        self.events(MainWindow)

    def events(self,MainWindow):

        # Log Out Method

        self.logoutButton.clicked.connect(lambda : self.logoutFunction(MainWindow))

        # Refresh Method

        self.refreshButton.clicked.connect(lambda : self.refreshFunction(MainWindow))

        # Password Change Method

        self.change_password_button.clicked.connect(lambda: self.changePasswordFunction(MainWindow))

        # Event Add Method

        self.addEventButton.clicked.connect(lambda : self.eventAddFunction(MainWindow))

        # Add New Adminstrator Method

        self.addNewAdministratorButton.clicked.connect(lambda: self.addAdministratorFunction(MainWindow))

        # Add Hospital Method

        self.addHospitalButton.clicked.connect(lambda : self.addHospitalFunction(MainWindow))

        # Add Doctor Method

        self.addDoctorButton.clicked.connect(lambda : self.addDoctorFunction(MainWindow))

        # Add TestCenter Method

        self.addTestCenterButton.clicked.connect(lambda : self.addTestCenterFunction(MainWindow))

        # Add Blood Bank Center Method
        self.addBbcButton.clicked.connect(lambda: self.addBloodBankCenterFunction(MainWindow))

        # Add ES Method

        self.addEmergencyServicesButton.clicked.connect(lambda: self.addEmergencyServicesFunction(MainWindow))

        # Add dispensary Method

        self.addDispensaryButton.clicked.connect(lambda: self.addDispensaryFunction(MainWindow))

        # Add Ambulance Method

        self.addAmbulanceButton.clicked.connect(lambda : self.addAmbulanceFunction(MainWindow))

        # Add Nurse
        self.remove_test_button_3.clicked.connect(lambda: self.addNurseFunction(MainWindow))

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


    # Event Add Functionality

    def eventAddFunction(self, MainWindow):
        self.window = QtWidgets.QDialog()
        self.dialog = Ui_EventDialog()
        self.dialog.setupUi(self.window)
        self.window.setModal(True)
        self.window.setWindowTitle("Add Event")
        self.window.show()

    # Delete Event Functionality

    def deleteEventFunction(self,MainWindow):
        pass

    # Add Hospital Functionality

    def addHospitalFunction(self, MainWindow):
        pass


    # Add Nurse Functionality

    def addNurseFunction(self,MainWindow):
        pass


    # Add Test Center Functionality

    def addTestCenterFunction(self, MainWindow):
        pass


    # Add Blood Bank Functionality

    def addBloodBankCenterFunction(self, MainWindow):
        pass

    # Add Dispensary Functionality

    def addDispensaryFunction(self, MainWindow):
        pass

    # Add Ambulance Functionality

    def addAmbulanceFunction(self, MainWindow):
        pass

    # Add Doctor Functionality

    def addDoctorFunction(self, MainWindow):
        pass

    # Add New Adminstrator Functionality

    def addAdministratorFunction(self, MainWindow):
        pass

    #Add EmergencyServices Functionality

    def addEmergencyServicesFunction(self, MainWindow):
        pass





