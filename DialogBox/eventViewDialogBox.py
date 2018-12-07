from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Ui_EventListDialog(object):
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
        EventListDialog.setWindowTitle(_translate("EventListDialog", "Dialog"))
        self.eventListHeader.setText(_translate("EventListDialog", "Event View Box"))
        self.searchEventInput.setPlaceholderText(_translate("EventListDialog", "Enter Event ID or Name"))
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
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tablewidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Event ID")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("Event Title")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("Description")
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText("Date")
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText("Place")
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText("Edit")

        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 550)
        self.tableWidget.setColumnWidth(3, 110)
        self.tableWidget.setColumnWidth(4, 200)
        self.tableWidget.setColumnWidth(5, 110)

        # Ab rows fill honge

        self.addRowDataFunction(EventListDialog)


    # Add data From Database

    def addRowDataFunction(self,EventListDialog):

        # fetch data from Database
        EventId = [101,156,324,789]
        EventName = ["First Aid Distribution 1", "Blood Camps", "Organ Donation Camp", "Seminar"]
        Desription = ["agvhhhhhhhhhhhhhhhhhhhhhhh snsjsn askjjas asjjsmlkas ", "ygwdbahbh duhiuasb asjkashk asnkjsji", "bdjkj kjasnkjas hjwuiqhq  asjkshs asjijsaiojl", "sdnjhkbasjbjhkjlnasn,naskjhkashabahkha"]
        Date = ["12/12/23","12/3/06","12/02/12",'23/2/16']
        Place = ["AnandNagar","indrapuri", "Bihar", "Delhi"]
        self.tableWidget.setRowCount(4)
        for i in range(4):

            item1 = QTextBrowser()
            item1.setText(str(EventId[i]))
            item1.setReadOnly(True)
            item1.setAlignment(Qt.AlignCenter)
            self.tableWidget.setCellWidget(i,0,item1)

            item2 = QTextBrowser()
            item2.setText(str(EventName[i]))
            item2.setReadOnly(True)
            item2.setAlignment(Qt.AlignCenter)
            self.tableWidget.setCellWidget(i,1,item2)

            item3 = QTextBrowser()
            item3.setAlignment(Qt.AlignCenter)
            item3.setReadOnly(True)
            item3.setText(Desription[i])
            self.tableWidget.setCellWidget(i,2,item3)

            item4 = QTextBrowser()
            item4.setAlignment(Qt.AlignCenter)
            item4.setReadOnly(True)
            item4.setText(Date[i])
            self.tableWidget.setCellWidget(i,3,item4)

            item5 = QTextBrowser()
            item5.setAlignment(Qt.AlignCenter)
            item5.setReadOnly(True)
            item5.setText(Place[i])
            self.tableWidget.setCellWidget(i,4,item5)



            self.editButton = QPushButton()
            self.editButton.setFixedSize(110,30)
            self.editButton.setText('Edit')
            self.editButton.setStyleSheet("background : rgb(0,0,225);")
            self.editButton.clicked.connect(self.editButtonClicked)

            self.tableWidget.setCellWidget(i,5,self.editButton)
            self.tableWidget.setRowHeight(i,100)

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

