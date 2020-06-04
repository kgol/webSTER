# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from gsmmodem.modem import GsmModem


import datetime


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QtCore.QSize(480, 640))
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 60, 451, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.naglowek = QtWidgets.QLabel(Dialog)
        self.naglowek.setGeometry(QtCore.QRect(160, 20, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.naglowek.setFont(font)
        self.naglowek.setObjectName("naglowek")
        self.DATA = QtWidgets.QLabel(Dialog)
        self.DATA.setGeometry(QtCore.QRect(60, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.DATA.setFont(font)
        self.DATA.setObjectName("DATA")
        self.DATA_2 = QtWidgets.QLabel(Dialog)
        self.DATA_2.setGeometry(QtCore.QRect(330, 90, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.DATA_2.setFont(font)
        self.DATA_2.setObjectName("DATA_2")
        self.usr = QtWidgets.QLineEdit(Dialog)
        self.usr.setGeometry(QtCore.QRect(110, 220, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.usr.setFont(font)
        self.usr.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.usr.setPlaceholderText('Podaj login')
        self.usr.setMaxLength(13)
        self.usr.setObjectName("usr")
        self.pwd = QtWidgets.QLineEdit(Dialog)
        self.pwd.setGeometry(QtCore.QRect(110, 330, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pwd.setFont(font)
        self.pwd.setObjectName("pwd")
        self.button_ok = QtWidgets.QPushButton(Dialog)
        self.button_ok.setGeometry(QtCore.QRect(250, 550, 101, 41))
        self.button_ok.setObjectName("button_ok")
        self.button_cancel = QtWidgets.QPushButton(Dialog)
        self.button_cancel.setGeometry(QtCore.QRect(130, 550, 101, 41))
        self.button_cancel.setObjectName("button_cancel")
        #self.SMS_button = QtWidgets.QPushButton(Dialog)
        #self.SMS_button.setGeometry(QtCore.QRect(370, 220, 61, 51))
        #self.SMS_button.setObjectName("SMS_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #self.SMS_button.clicked(self.sendSMS())

        self.qTimer=QTimer()
        self.qTimer.setInterval(100) #100ms
        self.qTimer.timeout.connect(self.datetime)
        self.qTimer.start()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.naglowek.setText(_translate("Dialog", "MEW BUGAJ 2020"))
        #self.DATA.setText(_translate("Dialog", "TextLabel"))
        #self.DATA_2.setText(_translate("Dialog", "TextLabel"))
        self.button_ok.setText(_translate("Dialog", "Zatwierdz"))
        self.button_cancel.setText(_translate("Dialog", "Anuluj"))
        #self.SMS_button.setText(_translate("Dialog", "SMS"))

    def datetime(self):
        DateTime = datetime.datetime.now()
        self.DATA.setText(DateTime.strftime('%x'))
        self.DATA_2.setText(DateTime.strftime('%X'))
    
    
    

    '''def sendSMS(self):
        PORT = '/dev/ttyUSB0'
        BAUDRATE = 115200
        #PIN = None # SIM card PIN (if any)
        modem = GsmModem(PORT,BAUDRATE)
        modem.connect()
        modem.sendSms(664873893,'karol')'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
