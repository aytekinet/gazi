import sys
from PyQt5.QtWidgets import *
from hastaUI import *
import sqlite3
import datetime
import time

uygulama=QApplication(sys.argv)
anaPencere=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(anaPencere)
anaPencere.show()

vt=sqlite3.connect("hasta.db")
im=vt.cursor()
im.execute("""CREATE TABLE IF NOT EXISTS tablo(
            ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            TC TEXT NOT NULL UNIQUE,
            ADI TEXT NOT NULL,
            SOYADI TEXT NOT NULL,
            MEDENIHAL TEXT,
            KANGRUBU TEXT,
            KILO TEXT,
            DTARIHI TEXT, 
            CINSIYET TEXT,
            SERVIS TEXT)""")

def ekle():
    _TC=ui.lneTC.text()
    _adi=ui.lneAdi.text()
    _soyadi=ui.lneSoyadi.text()
    if ui.chkMedeni.isChecked():
        _medeni="Evli"
    else:
        _medeni="Bekar"
    _kangrubu=ui.cmbKanGrubu.currentText()
    _kilo=str(ui.spnKilo.value())
    _dtarihi=ui.calwDTarihi.selectedDate().toString(QtCore.Qt.ISODate)
    if ui.rdErkek.isChecked():
        _cinsiyet="Erkek"
    elif ui.rdKadin.isChecked():
        _cinsiyet="Kadın"
    else:
        _cinsiyet="Belirtilmedi"
    _servis=ui.lstServis.currentItem().text()
    try:
        im.execute("""INSERT INTO tablo (TC,ADI,SOYADI,MEDENIHAL,KANGRUBU,KILO,DTARIHI,CINSIYET,SERVIS)
        VALUES (?,?,?,?,?,?,?,?,?) """,(_TC,_adi,_soyadi,_medeni,_kangrubu,_kilo,_dtarihi,_cinsiyet,_servis))
        vt.commit()
        listele()
        temizle()
    except Exception as hata:
        QMessageBox.information(anaPencere,"Hata",f"{hata}",QMessageBox.Ok)
    
def bul():
    aranan,durum=QInputDialog.getText(anaPencere,"Bul","Aramak istediğiniz ifade: ")
    if durum:
        try:
            im.execute(f"SELECT * FROM tablo WHERE TC LIKE '%{aranan}%' OR ADI LIKE '%{aranan}%'")
            ui.tblKayit.clear()
            ui.tblKayit.setHorizontalHeaderLabels(("ID","TC","ADI","SOYADI","MEDENIHAL","KANGRUBU","KILO","DTARIHI","CINSIYET","SERVIS"))
            for satırIndeks,satırVeri in enumerate(im):
                for sutunIndeks,sutunVeri in enumerate(satırVeri):
                    ui.tblKayit.setItem(satırIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
        except Exception as hata:
            QMessageBox.information(anaPencere,"Hata",f"{hata}",QMessageBox.Ok)
    else:
        ui.statusbar.showMessage("Arama iptal edildi",3000)
def sil():
    secili=ui.tblKayit.selectedItems()
    _id=int(secili[0].text())
    yanıt=QMessageBox.question(anaPencere,"Sil","Silinsin mi?",QMessageBox.Yes|QMessageBox.No)
    if yanıt==QMessageBox.Yes:
        try:
            im.execute(f"DELETE FROM tablo WHERE ID={_id}")
            vt.commit()
            listele()
        except Exception as hata:
            QMessageBox.information(anaPencere,"Hata",f"{hata}",QMessageBox.Ok)
    else:
        ui.statusbar.showMessage("Silme işlemi iptal edildi",3000)
def listele():
    im.execute("SELECT * FROM tablo")
    ui.tblKayit.clear()
    ui.tblKayit.setHorizontalHeaderLabels(("ID","TC","ADI","SOYADI","MEDENIHAL","KANGRUBU","KILO","DTARIHI","CINSIYET","SERVIS"))
    for satırIndeks,satırVeri in enumerate(im):
        for sutunIndeks,sutunVeri in enumerate(satırVeri):
            ui.tblKayit.setItem(satırIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
    kayıt_sayısı=str(im.execute("SELECT COUNT(*) from tablo").fetchone()[0])
    ui.lblKayitSayisi.setText(kayıt_sayısı)

def guncelle():
    _id=int(ui.tblKayit.selectedItems()[0])
    _TC=ui.lneTC.text()
    _adi=ui.lneAdi.text()
    _soyadi=ui.lneSoyadi.text()
    if ui.chkMedeni.isChecked():
        _medeni="Evli"
    else:
        _medeni="Bekar"
    _kangrubu=ui.cmbKanGrubu.currentText()
    _kilo=str(ui.spnKilo.value())
    _dtarihi=ui.calwDTarihi.selectedDate().toString(QtCore.Qt.ISODate)
    if ui.rdErkek.isChecked():
        _cinsiyet="Erkek"
    elif ui.rdKadin.isChecked():
        _cinsiyet="Kadın"
    else:
        _cinsiyet="Belirtilmedi"
    _servis=ui.lstServis.currentItem().text()
    try:
        im.execute("UPDATE tablo SET TC=?,ADI=?,SOYADI=?,MEDENIHAL=?,KANGRUBU=?,KILO=?,DTARIHI=?,CINSIYET=?,SERVIS=? WHERE ID=? """,(_TC,_adi,_soyadi,_medeni,_kangrubu,_kilo,_dtarihi,_cinsiyet,_servis,_id))
        vt.commit()
        listele()
        temizle()
    except Exception as hata:
        QMessageBox.information(anaPencere,"Hata",f"{hata}",QMessageBox.Ok)
        
def cikis():
    vt.close()
    anaPencere.close()
    uygulama.quit()

def sec():
    try:
        secili=ui.tblKayit.selectedItems()
        _id=int(secili[0].text())
        ui.lneTC.setText(secili[1].text())
        ui.lneAdi.setText(secili[2].text())
        ui.lneSoyadi.setText(secili[3].text())
        if secili[4].text()=="Evli":
            ui.chkMedeni.setChecked(True)
        else:
            ui.chkMedeni.setChecked(False)
        ui.cmbKanGrubu.setCurrentText(secili[5].text())
        ui.spnKilo.setValue(int(secili[6].text()))
        ui.calwDTarihi.setSelectedDate(datetime.datetime(int(secili[7].text()[0:4]),int(secili[7].text()[5:7]),int(secili[7].text()[8:10])))
        if secili[8].text()=="Kadın":
            ui.rdKadin.setChecked(True)
            ui.rdErkek.setChecked(False)
        elif secili[8].text()=="Erkek":
            ui.rdKadin.setChecked(False)
            ui.rdErkek.setChecked(True)
        else:
            ui.rdKadin.setChecked(False)
            ui.rdErkek.setChecked(False)
        if secili[9].text()=="Dahiliye":
            ui.lstServis.item(0).setSelected(True)
            ui.lstServis.setCurrentItem(ui.lstServis.item(0))
        elif secili[9].text=="Ortopedi":
            ui.lstServis.item(1).setSelected(True)
            ui.lstServis.setCurrentItem(ui.lstServis.item(1))
        elif secili[9].text()=="Kardiyoloji":
            ui.lstServis.item(2).setSelected(True)
            ui.lstServis.setCurrentItem(ui.lstServis.item(2))
        elif secili[9]=="Noröloji":
            ui.lstServis.item(3).setSelected(True)
            ui.lstServis.setCurrentItem(ui.lstServis.item(3))
    except:
        temizle()
def temizle():
    ui.lneTC.clear()
    ui.lneAdi.clear()
    ui.lneSoyadi.clear()
    ui.chkMedeni.setChecked(False)
    ui.cmbKanGrubu.setCurrentIndex(-1)
    ui.spnKilo.setValue(40)
    ui.calwDTarihi.setSelectedDate(datetime.datetime.now())
    ui.rdErkek.setChecked(False)
    ui.rdKadin.setChecked(False)
    ui.lstServis.setCurrentIndex(-1)

def hakkinda():
    anaPencere.close()
    time.sleep(5)
    anaPencere.show()

ui.BtnCikis.clicked.connect(cikis)
ui.btnBul.clicked.connect(bul)
ui.btnEkle.clicked.connect(ekle)
ui.btnGuncelle.clicked.connect(guncelle)
ui.btnListele.clicked.connect(listele)
ui.btnSil.clicked.connect(sil)
ui.tblKayit.itemSelectionChanged.connect(sec)
ui.menuHakkinda.triggered.connect(hakkinda)

sys.exit(uygulama.exec_())