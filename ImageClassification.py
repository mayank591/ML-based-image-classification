# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Mayank\ProductDevelopment\ImageClassification.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(967, 522)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pwclogo/pwclogo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(144, 144, 144);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"\n"
"border-color: black;\n"
"padding: 4px;")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(590, 470, 341, 32))
        self.buttonBox.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"font: 75 10pt \"Georgia\";\n"
"border-radius: 15px;")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 30, 731, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 15px;")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 130, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(203, 203, 203);")
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(310, 120, 371, 51))
        self.plainTextEdit.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 15px;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(710, 130, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 15px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 340, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 15px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(500, 230, 141, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("\n"
"background-color: rgb(203, 203, 203);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(310, 230, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(203, 203, 203);")
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 340, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 15px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 340, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 15px;")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Image Classification"))
        self.label_2.setText(_translate("Dialog", "Machine Learning Based Image Classification"))
        self.label.setText(_translate("Dialog", "Input Directory"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.pushButton_2.setText(_translate("Dialog", "Start Model Training"))
        self.comboBox.setItemText(0, _translate("Dialog", "SVM"))
        self.comboBox.setItemText(1, _translate("Dialog", "Random Forest"))
        self.comboBox.setItemText(2, _translate("Dialog", "ANN"))
        self.comboBox.setItemText(3, _translate("Dialog", "XGBoost"))
        self.label_3.setText(_translate("Dialog", "Select Classifier"))
        self.pushButton_3.setText(_translate("Dialog", "Classify"))
        self.pushButton_4.setText(_translate("Dialog", "Accuracy Assessment"))

import resources_rc
