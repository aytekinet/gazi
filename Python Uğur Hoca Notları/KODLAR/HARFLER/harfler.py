import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import random

class Harfler(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("harf_UI.ui",self)
        self.tr_liste=["Sıfat","Sonra","Hava","Cevap","Sanat"]
        self.en_liste=["Adjective","After","Air","Answer","Art"]
        self.lbl_liste=[self.lbl_1,self.lbl_2,self.lbl_3,self.lbl_4,self.lbl_5,
            self.lbl_6,self.lbl_7,self.lbl_8,self.lbl_9,self.lbl_10]
        for i in range(0,10):
            self.lbl_liste[i].setText("")
        self.lbl_text.setText("")
        self.lbl_1.mousePressEvent=self.label_1
        self.lbl_2.mousePressEvent=self.label_2
        self.lbl_3.mousePressEvent=self.label_3
        self.lbl_4.mousePressEvent=self.label_4
        self.lbl_5.mousePressEvent=self.label_5
        self.lbl_6.mousePressEvent=self.label_6
        self.lbl_7.mousePressEvent=self.label_7
        self.lbl_8.mousePressEvent=self.label_8
        self.lbl_9.mousePressEvent=self.label_9
        self.lbl_10.mousePressEvent=self.label_10
        self.ilkSira=100
        self.ikinciSira=100
        self.ilkHarf=""
        self.ikinciHarf=""
        self.btn_basla.clicked.connect(self.basla)
        self.btn_joker.clicked.connect(self.joker)
    
    def joker(self):
        kelimemiz=""
        for i in range(0,self.uzunluk):
            kelimemiz=kelimemiz+self.lbl_liste[i].text()
        if self.en_kelime==kelimemiz:
            self.lbl_text.setText(f"Tebrikler, {self.tr_liste[self.indeks]}")
        else:
            self.jokerr()
    def jokerr(self):
        for i in range(0,self.uzunluk):
            if self.lbl_liste[i].text()!=self.en_kelime[i]:
                ilk=self.lbl_liste[i].text()
                ilk_indeks=i
                ikinci=self.en_kelime[i]
               
                for j in range(0,self.uzunluk):
                    if self.lbl_liste[j].text()==ikinci and self.lbl_liste[j]!=self.en_kelime[j]:
                        ikinci_indeks=j
                        break
                break    
        self.lbl_liste[ilk_indeks].setText(ikinci)
        self.lbl_liste[ikinci_indeks].setText(ilk)


    def basla(self):
        for i in range(0,10):
            self.lbl_liste[i].setText("")
        self.lbl_text.setText("")
        self.secilen=random.choice(self.en_liste)
        self.indeks=self.en_liste.index(self.secilen)
        self.uzunluk=len(self.secilen)
        self.en_kelime=self.secilen
        self.secilen=list(self.secilen)
        for i in range(0,self.uzunluk):
            sec=random.choice(self.secilen)
            self.lbl_liste[i].setText(sec)
            self.secilen.remove(sec)
        

    def label_1(self,event):
        self.kliklenen=1
        self.harf()
    def label_2(self,event):
        self.kliklenen=2
        self.harf()
    def label_3(self,event):
        self.kliklenen=3
        self.harf()
    def label_4(self,event):
        self.kliklenen=4
        self.harf()
    def label_5(self,event):
        self.kliklenen=5
        self.harf()
    def label_6(self,event):
        self.kliklenen=6
        self.harf()
    def label_7(self,event):
        self.kliklenen=7
        self.harf()
    def label_8(self,event):
        self.kliklenen=8
        self.harf()
    def label_9(self,event):
        self.kliklenen=9
        self.harf()
    def label_10(self,event):
        self.kliklenen=10
        self.harf()
        
        
    def harf(self):
        if self.ilkSira==100:
            self.ilkSira=self.kliklenen
            self.ilkHarf=self.lbl_liste[self.kliklenen-1].text()
            self.lbl_liste[self.kliklenen-1].setStyleSheet("color: red")
        else:
            if self.ikinciSira==100:
                self.ikinciSira=self.kliklenen
                self.ikinciHarf=self.lbl_liste[self.kliklenen-1].text()
                self.lbl_liste[self.kliklenen-1].setStyleSheet("color: red")

                self.lbl_liste[self.ilkSira-1].setText(self.ikinciHarf)
                self.lbl_liste[self.ikinciSira-1].setText(self.ilkHarf)
                self.lbl_liste[self.ilkSira-1].setStyleSheet("color: black")
                self.lbl_liste[self.ikinciSira-1].setStyleSheet("color: black")
                kelimemiz=""
                for i in range(0,self.uzunluk):
                    kelimemiz=kelimemiz+self.lbl_liste[i].text()
                if self.en_kelime==kelimemiz:
                    self.lbl_text.setText(f"Tebrikler, {self.tr_liste[self.indeks]}")
                self.ilkSira=100
                self.ikinciSira=100
                self.ilkHarf=""
                self.ikinciHarf=""

uygulama=QApplication(sys.argv)
anaPencere=Harfler()
anaPencere.show()
sys.exit(uygulama.exec_())



