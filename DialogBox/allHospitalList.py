from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Ui_HospitalListDialog(object):
    def setupUi(self, EventListDialog):
        EventListDialog.setObjectName("EventListDialog")
        EventListDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        EventListDialog.resize(1291, 745)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EventListDialog.sizePolicy().hasHeightForWidth())
        EventListDialog.setSizePolicy(sizePolicy)
        self.tableWidget = QtWidgets.QTableWidget(EventListDialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 1271, 581))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.eventListHeader = QtWidgets.QLabel(EventListDialog)
        self.eventListHeader.setGeometry(QtCore.QRect(10, 0, 1281, 61))
        self.eventListHeader.setStyleSheet("font: 68 39pt \"Ubuntu\";\n"
                                           "text-decoration : underline;\n"
                                           "")
        self.eventListHeader.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.eventListHeader.setObjectName("eventListHeader")
        self.searchEventInput = QtWidgets.QLineEdit(EventListDialog)
        self.searchEventInput.setGeometry(QtCore.QRect(700, 70, 461, 31))
        self.searchEventInput.setObjectName("searchEventInput")
        self.searchButton = QtWidgets.QPushButton(EventListDialog)
        self.searchButton.setGeometry(QtCore.QRect(1170, 70, 111, 31))
        self.searchButton.setObjectName("searchButton")
        self.exitButton = QtWidgets.QPushButton(EventListDialog)
        self.exitButton.setGeometry(QtCore.QRect(580, 700, 121, 25))
        self.exitButton.setObjectName("exitButton")

        self.retranslateUi(EventListDialog)
        QtCore.QMetaObject.connectSlotsByName(EventListDialog)

    def retranslateUi(self, EventListDialog):
        _translate = QtCore.QCoreApplication.translate
        EventListDialog.setWindowTitle(_translate("HospitalListDialog", "Dialog"))
        self.eventListHeader.setText(_translate("EventListDialog", "HOSPITALS"))
        self.searchEventInput.setPlaceholderText(_translate("EventListDialog", "Enter Hospital ID or Name"))
        self.searchButton.setText(_translate("EventListDialog", "Search"))
        self.exitButton.setText(_translate("EventListDialog", "Exit"))


        #############

        self.fillEventdata(EventListDialog)
        self.events(EventListDialog)


    # Fil rows and column in an data

    def fillEventdata(self,EventListDialog):


        # table Widget Ka Functionality Add Up Hua

        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setAutoScrollMargin(100)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowHeight(0,125)
        self.tableWidget.setStyleSheet("background : rgb(255,255,255);")
        #self.MedicineSearchTable.setRowCount(5)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tablewidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Hospital ID")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("Hospital Name")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("Place")
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText("Go To")

        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1, 600)
        self.tableWidget.setColumnWidth(2, 300)
        self.tableWidget.setColumnWidth(3, 120)

        # Ab rows fill honge

        self.addRowDataFunction(EventListDialog)


    # Add data From Database

    def addRowDataFunction(self,EventListDialog):
        pass

        # fetch data from Database
        HospitalId = [101,156,324,789]
        HospitalName = ["First Aid Distribution 1", "Blood Camps", "Organ Donation Camp", "Seminar"]
        Place = ["AnandNagar","indrapuri", "Bihar", "Delhi"]
        self.tableWidget.setRowCount(4)
        for i in range(4):

            item1 = QTextBrowser()
            item1.setText(str(HospitalId[i]))
            item1.setReadOnly(True)
            item1.setAlignment(Qt.AlignCenter)
            self.tableWidget.setCellWidget(i,0,item1)

            item2 = QTextBrowser()
            item2.setText(str(HospitalName[i]))
            item2.setReadOnly(True)
            item2.setAlignment(Qt.AlignCenter)
            self.tableWidget.setCellWidget(i,1,item2)

            item3 = QTextBrowser()
            item3.setAlignment(Qt.AlignCenter)
            item3.setReadOnly(True)
            item3.setText(Place[i])
            self.tableWidget.setCellWidget(i,2,item3)

            self.editButton = QPushButton()
            #self.editButton.setFixedSize(160,30)
            self.editButton.setText('Click Here')
            self.editButton.setStyleSheet("background : rgb(245,245,245);")
            self.editButton.clicked.connect(self.editButtonClicked)

            self.tableWidget.setCellWidget(i,3,self.editButton)
            self.tableWidget.setRowHeight(i,50)

    def editButtonClicked(self):
        #button = QtGui.qApp.focusWidget()
        # or button = self.sender()
        #index = self.table.indexAt(button.pos())
        #if index.isValid():
        #print(index.row(), index.column())
        pass


    def events(self,EventListDialog):

        # Exit Button Functionality

        self.exitButton.clicked.connect(lambda : self.exitFunction(EventListDialog))


    # Exit Button FUnction

    def exitFunction(self,EventListDialog):
        EventListDialog.close()

