import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from cal import *

uygulama= QApplication(sys.argv)
anaPen = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(anaPen)
anaPen.show()


def method1():
    text=ui.lineEdit.text()
    ui.lineEdit.setText(text+"1")

def method2():
    text=ui.lineEdit.text()
    ui.lineEdit.setText(text+"2")

def method3():
    text=ui.lineEdit.text()
    ui.lineEdit.setText(text+"3")

def method4():
    text=ui.lineEdit.text()
    ui.lineEdit.setText(text+"4")

def method5():
    text=ui.lineEdit.text()
    ui.lineEdit.setText(text+"5")

def method6():
    text=ui.lineEdit.text()
    ui.lineEdit.setText(text+"6")

def method7():
    text=ui.lineEdit.text()
    ui.lineEdit.setText(text+"7")

def method8():
    text=ui.lineEdit.text()
    ui.lineEdit.setText(text+"8")

def method9():
    text=ui.lineEdit.text()
    ui.lineEdit.setText(text+"9")

def method0():
    text=ui.lineEdit.text()
    ui.lineEdit.setText(text+"0")

def methodTopla():
    text=ui.lineEdit.text()
    ui.lineEdit.setText(text+"+")

def methodCikart():
    text=ui.lineEdit.text()
    ui.lineEdit.setText(text+"-")

def methodBol():
    text=ui.lineEdit.text()
    ui.lineEdit.setText(text+"/")

def methodNokta():
    text=ui.lineEdit.text()
    ui.lineEdit.setText(text+".")

def methodCarp():
    text=ui.lineEdit.text()
    ui.lineEdit.setText(text+"*")

def methodSil():
    ui.lineEdit.setText("")

def methodEsittir():
    text=ui.lineEdit.text()

    try:
        ans=eval(text)
        ui.lineEdit.setText(str(ans))
    except:
        ui.lineEdit.setText("Hata")



ui.btn_0.clicked.connect(method0)
ui.btn_1.clicked.connect(method1)
ui.btn_2.clicked.connect(method2)
ui.btn_3.clicked.connect(method3)
ui.btn_4.clicked.connect(method4)
ui.btn_5.clicked.connect(method5)
ui.btn_6.clicked.connect(method6)
ui.btn_7.clicked.connect(method7)
ui.btn_8.clicked.connect(method8)
ui.btn_9.clicked.connect(method9)
ui.btn_nokta.clicked.connect(methodNokta)
ui.btn_esittir.clicked.connect(methodEsittir)
ui.btn_topla.clicked.connect(methodTopla)
ui.btn_cikart.clicked.connect(methodCikart)
ui.btn_carp.clicked.connect(methodCarp)
ui.btn_bol.clicked.connect(methodBol)
ui.btn_sil.clicked.connect(methodSil)

sys.exit(uygulama.exec_())


