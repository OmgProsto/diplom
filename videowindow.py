# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)

        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(80, 70, 150, 30))
        self.pushButton_1.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 140, 150, 30))
        self.pushButton_2.setObjectName("pushButton_1")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 140, 150, 30))
        self.pushButton_3.setObjectName("pushButton_2")

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 70, 150, 30))
        self.pushButton_4.setObjectName("pushButton_3")

        #self.label_1 = QtWidgets.QLabel(Dialog)
        #self.label_1.setGeometry(QtCore.QRect(300, -150, 500, 500))
        #self.label_1.setObjectName("label_1")

        #self.label_2 = QtWidgets.QLabel(Dialog)
        #self.label_2.setGeometry(QtCore.QRect(300, -50, 500, 500))
        #self.label_2.setObjectName("label_2")

        #self.label_3 = QtWidgets.QLabel(Dialog)
        #self.label_3.setGeometry(QtCore.QRect(300, 50, 500, 500))
        #self.label_3.setObjectName("label_3")

       # self.label_4 = QtWidgets.QLabel(Dialog)
        #self.label_4.setGeometry(QtCore.QRect(300, 150, 500, 500))
       # self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Видеоматериалы"))
        self.pushButton_1.setIcon(QtGui.QIcon('img/icon/icon.jpg'))
        self.pushButton_1.setText(_translate("Dialog", "Триггеры ч.1"))

        self.pushButton_2.setText(_translate("Dialog", "Триггеры ч.1"))
        self.pushButton_3.setText(_translate("Dialog", "Триггеры ч.2"))
        self.pushButton_4.setText(_translate("Dialog", "Сумматоры"))
        
