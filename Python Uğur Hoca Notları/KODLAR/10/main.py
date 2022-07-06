import sys
from PyQt5.QtWidgets import *
from parolaUI import *
from anaSayfaUI import *
import time

uygulama=QApplication(sys.argv)
anaPencere=QMainWindow()
anaSayfa=QMainWindow()
ui=Ui_MainWindow()
ui2=Ui_anaSayfa()
ui.setupUi(anaPencere)
ui2.setupUi(anaSayfa)
anaPencere.show()

def tamam():
    parolamız="454545"
    kullanıcı="ugur"
    if ui.lneKullanici.text()!=kullanıcı:
        ui.statusbar.showMessage("Kullanıcı adı hatalı",5000)
    else:
        if ui.lneParola.text()!=parolamız:
            ui.statusbar.showMessage("Parola hatalı...",5000)
        else:
            ui.statusbar.showMessage("İşlem başarılı...",5000)
            anaPencere.close()
            anaSayfa.show()

def iptal():
    yanıt=QMessageBox.question(anaPencere,"Uyarı","İptal etmek istediğinize emin misiniz?",QMessageBox.Yes|QMessageBox.No)
    if yanıt==QMessageBox.Yes:
        ui.statusbar.showMessage("Çıkma işlemi yapılıyor...",5000)
        time.sleep(6)
        anaPencere.close()
        uygulama.quit()
    else:
        QMessageBox.information(anaPencere,"Bilgi","Çıkış işlemi iptal edildi",QMessageBox.Ok)
def goster():
    anaSayfa.close()
    anaPencere.show()

ui.btnIptal.clicked.connect(iptal)
ui.btnTamam.clicked.connect(tamam)
ui2.menuGoster.triggered.connect(goster)
sys.exit(uygulama.exec_())


