import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
import random

class MayinTarlasi(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("mayin_UI.ui",self)
        self.btn_list=[self.pushButton_1,self.pushButton_2,self.pushButton_3,self.pushButton_4,self.pushButton_5,
        self.pushButton_6,self.pushButton_7,self.pushButton_8,self.pushButton_9,self.pushButton_10,
        self.pushButton_11,self.pushButton_12,self.pushButton_13,self.pushButton_14,self.pushButton_15,
        self.pushButton_16,self.pushButton_17,self.pushButton_18,self.pushButton_19,self.pushButton_20]
        self.pushButton_1.clicked.connect(self.oyun)
        self.pushButton_2.clicked.connect(self.oyun)
        self.pushButton_3.clicked.connect(self.oyun)
        self.pushButton_4.clicked.connect(self.oyun)
        self.pushButton_5.clicked.connect(self.oyun)
        self.pushButton_6.clicked.connect(self.oyun)
        self.pushButton_7.clicked.connect(self.oyun)
        self.pushButton_8.clicked.connect(self.oyun)
        self.pushButton_9.clicked.connect(self.oyun)
        self.pushButton_10.clicked.connect(self.oyun)
        self.pushButton_11.clicked.connect(self.oyun)
        self.pushButton_12.clicked.connect(self.oyun)
        self.pushButton_13.clicked.connect(self.oyun)
        self.pushButton_14.clicked.connect(self.oyun)
        self.pushButton_15.clicked.connect(self.oyun)
        self.pushButton_16.clicked.connect(self.oyun)
        self.pushButton_17.clicked.connect(self.oyun)
        self.pushButton_18.clicked.connect(self.oyun)
        self.pushButton_19.clicked.connect(self.oyun)
        self.pushButton_20.clicked.connect(self.oyun)
        self.mayın=[0 for i in range(0,20)]
        sayac=0
        while sayac<5:
            rastgele_mayın=random.randint(0,19)
            if self.mayın[rastgele_mayın]==0:
                self.mayın[rastgele_mayın]=1
                sayac+=1
            



    def oyun(self):
        self.kliklenen=str(self.sender().objectName())
        self.kliklenen=int(self.kliklenen[11:])-1
        if self.mayın[self.kliklenen]==0:
            self.btn_list[self.kliklenen].setIcon(QIcon("check-green.gif"))
        else:
            self.btn_list[self.kliklenen].setIcon(QIcon("mayin.png"))





uygulama=QApplication(sys.argv)
anaPencere=MayinTarlasi()
anaPencere.show()
sys.exit(uygulama.exec_())