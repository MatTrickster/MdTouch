# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddNewMedicineDialogBox.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addNewMedicineDialog(object):
    def setupUi(self, addNewMedicineDialog):
        addNewMedicineDialog.setObjectName("addNewMedicineDialog")
        addNewMedicineDialog.setWindowModality(QtCore.Qt.WindowModal)
        addNewMedicineDialog.resize(731, 479)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addNewMedicineDialog.sizePolicy().hasHeightForWidth())
        addNewMedicineDialog.setSizePolicy(sizePolicy)
        addNewMedicineDialog.setStyleSheet("background : rgb(114, 159, 207);")
        self.medicineInfolabel = QtWidgets.QLabel(addNewMedicineDialog)
        self.medicineInfolabel.setGeometry(QtCore.QRect(270, 30, 201, 20))
        self.medicineInfolabel.setStyleSheet("font: 75 15pt \"Serif\";\n"
"text-decoration : underline;")
        self.medicineInfolabel.setObjectName("medicineInfolabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(addNewMedicineDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 80, 141, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.name_label.setStyleSheet("font: 75 15pt \"Serif\";")
        self.name_label.setObjectName("name_label")
        self.verticalLayout.addWidget(self.name_label)
        self.quantity_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.quantity_label.setStyleSheet("font: 75 15pt \"Serif\";")
        self.quantity_label.setObjectName("quantity_label")
        self.verticalLayout.addWidget(self.quantity_label)
        self.price_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.price_label.setStyleSheet("font: 75 15pt \"Serif\";")
        self.price_label.setObjectName("price_label")
        self.verticalLayout.addWidget(self.price_label)
        self.batch_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.batch_label.setStyleSheet("font: 75 15pt \"Serif\";")
        self.batch_label.setObjectName("batch_label")
        self.verticalLayout.addWidget(self.batch_label)
        self.expiry_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.expiry_label.setStyleSheet("font: 75 15pt \"Serif\";")
        self.expiry_label.setObjectName("expiry_label")
        self.verticalLayout.addWidget(self.expiry_label)
        self.mfDate_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mfDate_label.setStyleSheet("font: 75 15pt \"Serif\";")
        self.mfDate_label.setObjectName("mfDate_label")
        self.verticalLayout.addWidget(self.mfDate_label)
        self.mfDateInput = QtWidgets.QDateEdit(addNewMedicineDialog)
        self.mfDateInput.setGeometry(QtCore.QRect(220, 350, 151, 41))
        self.mfDateInput.setStyleSheet("background : rgb(238, 238, 236);")
        self.mfDateInput.setObjectName("mfDateInput")
        self.expDateInput = QtWidgets.QDateEdit(addNewMedicineDialog)
        self.expDateInput.setGeometry(QtCore.QRect(220, 300, 151, 41))
        self.expDateInput.setStyleSheet("background : rgb(238, 238, 236);")
        self.expDateInput.setObjectName("expDateInput")
        self.priceInput = QtWidgets.QLineEdit(addNewMedicineDialog)
        self.priceInput.setGeometry(QtCore.QRect(220, 190, 361, 41))
        self.priceInput.setStyleSheet("background : rgb(238, 238, 236);")
        self.priceInput.setObjectName("priceInput")
        self.batchNOInput = QtWidgets.QLineEdit(addNewMedicineDialog)
        self.batchNOInput.setGeometry(QtCore.QRect(220, 240, 361, 41))
        self.batchNOInput.setStyleSheet("background : rgb(238, 238, 236);")
        self.batchNOInput.setObjectName("batchNOInput")
        self.quantityInput = QtWidgets.QLineEdit(addNewMedicineDialog)
        self.quantityInput.setGeometry(QtCore.QRect(220, 140, 361, 41))
        self.quantityInput.setStyleSheet("background : rgb(238, 238, 236);")
        self.quantityInput.setObjectName("quantityInput")
        self.nameInput = QtWidgets.QLineEdit(addNewMedicineDialog)
        self.nameInput.setGeometry(QtCore.QRect(220, 90, 361, 41))
        self.nameInput.setStyleSheet("background : rgb(238, 238, 236);")
        self.nameInput.setText("")
        self.nameInput.setObjectName("nameInput")
        self.addButton = QtWidgets.QPushButton(addNewMedicineDialog)
        self.addButton.setGeometry(QtCore.QRect(260, 420, 151, 31))
        self.addButton.setStyleSheet("background : rgb(252, 233, 79);")
        self.addButton.setObjectName("addButton")

        self.retranslateUi(addNewMedicineDialog)
        QtCore.QMetaObject.connectSlotsByName(addNewMedicineDialog)

    def retranslateUi(self, addNewMedicineDialog):
        _translate = QtCore.QCoreApplication.translate
        addNewMedicineDialog.setWindowTitle(_translate("addNewMedicineDialog", "Dialog"))
        self.medicineInfolabel.setText(_translate("addNewMedicineDialog", "Medicine Info"))
        self.name_label.setText(_translate("addNewMedicineDialog", "Name  "))
        self.quantity_label.setText(_translate("addNewMedicineDialog", "Quantity"))
        self.price_label.setText(_translate("addNewMedicineDialog", "Price"))
        self.batch_label.setText(_translate("addNewMedicineDialog", "Batch No"))
        self.expiry_label.setText(_translate("addNewMedicineDialog", "Expiry Date"))
        self.mfDate_label.setText(_translate("addNewMedicineDialog", "MF Date"))
        self.addButton.setText(_translate("addNewMedicineDialog", "ADD "))
        self.eventsUi(addNewMedicineDialog)

    def eventsUi(self,addNewMedicineDialog):

        # Add Medicine Button
        self.addButton.clicked.connect(lambda : self.addNewMedicineFunction(addNewMedicineDialog))

    def addNewMedicineFunction(self,addNewMedicineDialog):

        # Check the Constraints

        print("Kaam Kar raha hai")





        ##############

        addNewMedicineDialog.close()

