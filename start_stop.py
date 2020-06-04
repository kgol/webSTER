# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_stop.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, pyqtSlot
from PyQt5.QtWidgets import QMessageBox
from pynput.mouse import Listener




import time
import datetime


lista_log=['0']
time_log=['0']
active=['0']

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
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.button_ok = QtWidgets.QPushButton(Dialog)
        self.button_ok.setGeometry(QtCore.QRect(250, 550, 101, 41))
        self.button_ok.setObjectName("button_ok")
        self.button_cancel = QtWidgets.QPushButton(Dialog)
        self.button_cancel.setGeometry(QtCore.QRect(130, 550, 101, 41))
        self.button_cancel.setObjectName("button_cancel")
        self.SMS_button = QtWidgets.QPushButton(Dialog)
        self.SMS_button.setGeometry(QtCore.QRect(370, 220, 61, 51))
        self.SMS_button.setObjectName("SMS_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.button_ok.clicked.connect(self.checklogin)
        self.button_cancel.clicked.connect(self.AnulujButton)
    

        self.qTimer=QTimer()

        self.qTimer.setInterval(100) #100ms
        self.qTimer.timeout.connect(self.datetime)
        #self.qTimer.timeout.connect(self.mouse_active)
        
        self.qTimer.start()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.naglowek.setText(_translate("Dialog", "MEW BUGAJ 2020"))
        #self.DATA.setText(_translate("Dialog", "TextLabel"))
        #self.DATA_2.setText(_translate("Dialog", "TextLabel"))
        self.button_ok.setText(_translate("Dialog", "Zatwierdz"))
        self.button_cancel.setText(_translate("Dialog", "Anuluj"))
        self.SMS_button.setText(_translate("Dialog", "SMS"))

    def datetime(self):
        DateTime = datetime.datetime.now()
        self.DATA.setText(DateTime.strftime('%x'))
        self.DATA_2.setText(DateTime.strftime('%X'))
    
    

    def checklogin(self):
        logins=['664873893']
        pwds=['karol']
        
        if self.usr.text()==logins[0]:
            if self.pwd.text()==pwds[0]:
                
                
                msg = QMessageBox()
                msg.setWindowTitle('Logowanie')
                msg.setText('Login i haslo prawidlowe')
                lista_log[0]='1'
                time_log[0]=datetime.datetime.now().minute
               
                msg.exec()
      
            else:
                msg = QMessageBox()
                msg.setWindowTitle('Logowanie')
                msg.setText('haslo nieprawidow')
                msg.exec()
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Logowanie')
            msg.setText('Login nieprawidlowy')
            msg.exec()
    
    def AnulujButton(self):
        self.usr.setText('')
        self.pwd.setText('')
        #sys.exit()
    #def on_move(self,x,y):
     #   active[0]='1'
      #  print('mouse moved')
    #def on_click(self,x,y,button,pressed):
    #    active[0]='1'
    #    print('mose clicked')
    #def on_scroll(self,x,y,dx,dy):
     #   active[0]='1'
     #   print('mose scrolled')

    ###
    #def mouse_active(self):
     #   Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll).join
            



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 130, 71, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("run.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 150, 151, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 240, 71, 81))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("stop.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 260, 151, 41))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.T1_button = QtWidgets.QPushButton(self.centralwidget)
        self.T1_button.setGeometry(QtCore.QRect(250, 10, 271, 41))
        self.T1_button.setObjectName("T1_button")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.T1_button.clicked.connect(self.log)
        
        self.qTimer=QTimer()
        self.qTimer.setInterval(100) #100ms
        self.qTimer.timeout.connect(self.logok)
        self.qTimer.timeout.connect(self.noactive)
        self.qTimer.start()

       

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "PLC RUN"))
        self.label_4.setText(_translate("MainWindow", "PLC STOP"))

    def logok(self):
        print(lista_log[0])

    def noactive(self):
        print(time_log[0])
        if ((datetime.datetime.now().minute)-(int(time_log[0])))>3:
            lista_log[0]='0'

   
    def log(self):
        self.app2 = QtWidgets.QDialog()
        self.logui = Ui_Dialog()
        self.logui.setupUi(self.app2)
        self.app2.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
