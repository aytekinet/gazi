import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class XOX(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("XOX_UI.ui",self)
        self.btn_0.clicked.connect(self.oyna)
        self.btn_1.clicked.connect(self.oyna)
        self.btn_2.clicked.connect(self.oyna)
        self.btn_3.clicked.connect(self.oyna)
        self.btn_4.clicked.connect(self.oyna)
        self.btn_5.clicked.connect(self.oyna)
        self.btn_6.clicked.connect(self.oyna)
        self.btn_7.clicked.connect(self.oyna)
        self.btn_8.clicked.connect(self.oyna)
        self.btn_liste=[self.btn_0,self.btn_1,self.btn_2,
                        self.btn_3,self.btn_4,self.btn_5,
                        self.btn_6,self.btn_7,self.btn_8]
        self.tahta=[0 for i in range(0,9)]
        self.sıra="X"
        self.lbl_.setText("Önce X başlar")
        #cevap,indeks=QInputDialog().getText(self,"Bilgi","İsminiz: ")
        #self.lbl_2.setText(cevap)
        self.skor_X=0
        self.skor_O=0
    def oyna(self):
        self.kliklenen=str(self.sender().objectName())
        self.kliklenen=int(self.kliklenen[4])

        if self.tahta[self.kliklenen] != 0:
            self.statusBar().showMessage("Burası oynandı",2000)
            #QMessageBox.information(anaPencere,"Uyarı","Burası oynandı",QMessageBox.Ok)
        else:
            if self.sıra=="X":
                self.btn_liste[self.kliklenen].setText("X")
                self.tahta[self.kliklenen]="X"
                self.kontrol()
            else:
                self.btn_liste[self.kliklenen].setText("O")
                self.tahta[self.kliklenen]="O"
                self.kontrol()
    
    def kontrol(self):
        if self.tahta[0]==self.tahta[1]==self.tahta[2] and self.tahta[1]!=0:
            self.kazanan()
        elif self.tahta[3]==self.tahta[4]==self.tahta[5] and self.tahta[4]!=0:
            self.kazanan()
        elif self.tahta[6]==self.tahta[7]==self.tahta[8] and self.tahta[7]!=0:
            self.kazanan()
        elif self.tahta[0]==self.tahta[3]==self.tahta[6] and self.tahta[3]!=0:
            self.kazanan()
        elif self.tahta[1]==self.tahta[4]==self.tahta[7] and self.tahta[4]!=0:
            self.kazanan()
        elif self.tahta[2]==self.tahta[5]==self.tahta[8] and self.tahta[5]!=0:
            self.kazanan()
        elif self.tahta[0]==self.tahta[4]==self.tahta[8] and self.tahta[4]!=0:
            self.kazanan()
        elif self.tahta[2]==self.tahta[4]==self.tahta[6] and self.tahta[4]!=0:
            self.kazanan()
        else:
            if self.sıra=="X":
                self.sıra="O"
                self.lbl_.setText("Sıra O'da")
            else:
                self.sıra="X"
                self.lbl_.setText("Sıra X'te")

    def kazanan(self):
        if self.sıra=="X":
            self.lbl_.setText("Kazanan X")
            self.skor_X+=1
            yazdır="X:"+str(self.skor_X)+", O:"+str(self.skor_O)
            self.lbl_2.setText(yazdır)
        else:
            self.lbl_.setText("Kazanan O")
            self.skor_O+=1
            yazdır="X:"+str(self.skor_X)+", O:"+str(self.skor_O)
            self.lbl_2.setText(yazdır)

        yanıt=QMessageBox.question(anaPencere,"Çıkış","Tekrar Oynamak ister misiniz?",QMessageBox.Yes|QMessageBox.No)
        if yanıt==QMessageBox.Yes:
            self.tahta=[0 for i in range(0,9)]
            self.sıra="X"
            self.lbl_.setText("Önce X başlar")
            for i in range(0,9):
                self.btn_liste[i].setText("")
        else:
            anaPencere.close()
            uygulama.quit()

'''
def main():
    uygulama=QApplication(sys.argv)
    anaPencere=XOX()
    anaPencere.show()
    sys.exit(uygulama.exec_())
if __name__=="__main__":
    main()
'''

uygulama=QApplication(sys.argv)
anaPencere=XOX()
anaPencere.show()
sys.exit(uygulama.exec_())
