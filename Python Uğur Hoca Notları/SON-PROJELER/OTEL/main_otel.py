import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from otelUI import *
import sqlite3
import datetime

uygulama=QApplication(sys.argv)
anaPencere=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(anaPencere)
anaPencere.show()
vt=sqlite3.connect("otel.db")
im=vt.cursor()
im.execute("""CREATE TABLE IF NOT EXISTS tablo(
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    TC INTEGER NOT NULL UNIQUE,
    ADI TEXT NOT NULL,
    SOYADI TEXT NOT NULL,
    ODATIPI TEXT,
    GUNSAYISI INTEGER,
    UCRET NUMERIC,
    COCUKSAYISI TEXT,
    GIRISTARIHI TEXT,
    CIKISTARIHI TEXT,
    PANSIYON TEXT,
    CINSIYET TEXT) """)
vt.commit()
ilkDeger=ui.spnGunSayisi.value()
ui.dateGiris.setDate(datetime.datetime.now())
ui.dateCikis.setDate(datetime.datetime.now())
def kaydet():
    yanıt=QMessageBox.question(anaPencere,"Kaydet","Kayıt işlemini onaylıyor musunuz?",QMessageBox.Yes|QMessageBox.No)
    if yanıt == QMessageBox.Yes:
        try:
            _TC=ui.lneTC.text()
            _ADI=ui.lneAdi.text()
            _SOYADI=ui.lneSoyadi.text()
            _ODATIPI=ui.cmbOdaTipi.currentText()
            _GUNSAYISI=ui.spnGunSayisi.value()
            ui.lblUcret.setText(str(ui.spnGunSayisi.value()*750))
            _UCRET=ui.lblUcret.text()
            _COCUKSAYISI=ui.spnCocukSayisi.value()
            _GIRISTARIHI=ui.dateGiris.text()
            _CIKISTARIHI=ui.dateCikis.text()
            _PANSIYON=ui.lstPansiyon.currentItem().text()
            if ui.rdKadin.isChecked():
                _CINSIYET="Kadın"
            elif ui.rdErkek.isChecked():
                _CINSIYET="Erkek"
            else:
                _CINSIYET="Belirtilmemiş"
            im.execute("""INSERT INTO tablo (TC,ADI,SOYADI,
            ODATIPI,GUNSAYISI,UCRET,COCUKSAYISI,GIRISTARIHI,
            CIKISTARIHI,PANSIYON,CINSIYET) 
            VALUES(?,?,?,?,?,?,?,?,?,?,?) """,(_TC,_ADI,_SOYADI,
            _ODATIPI,_GUNSAYISI,_UCRET,_COCUKSAYISI,_GIRISTARIHI,
            _CIKISTARIHI,_PANSIYON,_CINSIYET))
            vt.commit()
        except Exception as hata:
            QMessageBox.information(anaPencere,"Hata",f"Hata: {hata}")
    else:
        QMessageBox.information(anaPencere,"Info","Kayıt yapılmadı...",QMessageBox.Ok)
    temizle()
    listele()
def eşitle():
    ui.dateCikis.setDate(ui.dateGiris.date())
def arttır_azalt():
    global ilkDeger
    tarih=ui.dateCikis.text()
    tarih=tarih.split(".")
    if ilkDeger<ui.spnGunSayisi.value(): #arttır
        if int(tarih[0])==30 and (int(tarih[1])==4 or int(tarih[1])==6 or int(tarih[1])==9 or int(tarih[1])==11):
            ui.dateCikis.setDate(QDate(int(tarih[2]),int(tarih[1])+1,1))
        elif int(tarih[0])==31 and (int(tarih[1])==1 or int(tarih[1])==3 or int(tarih[1])==5 or int(tarih[1])==7 or int(tarih[1])==8 or int(tarih[1])==11):
            ui.dateCikis.setDate(QDate(int(tarih[2]),int(tarih[1])+1,1))
        elif int(tarih[0])==31 and (int(tarih[1])==12):
            ui.dateCikis.setDate(QDate(int(tarih[2])+1,1,1))
        elif int(tarih[0])==28 and int(tarih[1])==2 and int(tarih[2])%4!=0:
            ui.dateCikis.setDate(QDate(int(tarih[2]),int(tarih[2])+1,1))
        elif int(tarih[0])==28 and int(tarih[1])==2 and int(tarih[2])%4==0:
            ui.dateCikis.setDate(QDate(int(tarih[2]),int(tarih[2]),29))
        elif int(tarih[0])==29 and int(tarih[1])==2 and int(tarih[2])%4==0:
            ui.dateCikis.setDate(QDate(int(tarih[2]),int(tarih[2])+1,1))
        else:
            ui.dateCikis.stepUp()
    elif ilkDeger>ui.spnGunSayisi.value(): #azalt
            ui.dateCikis.stepDown()
def listele():
    ui.tblWKayitlar.clear()
    ui.tblWKayitlar.setHorizontalHeaderLabels(("ID","TC","ADI","SOYADI","ODATIPI","GUNSAYISI","UCRET","COCUKSAYISI","GIRISTARIHI","CIKISTARIHI","PANSIYON","CINSIYET"))
    im.execute("SELECT * FROM tablo")
    for satırIndeks,satırVeri in enumerate(im):
        for sutunIndeks,sutunVeri in enumerate(satırVeri):
            ui.tblWKayitlar.setItem(satırIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
def temizle():
    ui.lneTC.clear()
    ui.lneAdi.clear()
    ui.lneSoyadi.clear()
    ui.cmbOdaTipi.setCurrentIndex(-1)
    ui.spnGunSayisi.setValue(0)
    ui.lblUcret.setText(str(0))
    ui.spnCocukSayisi.setValue(0)
    ui.dateGiris.setDate(datetime.datetime.now())
    ui.dateCikis.setDate(datetime.datetime.now())
    ui.lstPansiyon.setCurrentItem(ui.lstPansiyon.setCurrentRow(-1))
    ui.rdKadin.setChecked(False)
    ui.rdErkek.setChecked(False)

ui.btnTemizle.clicked.connect(temizle)
ui.btnListele.clicked.connect(listele)
ui.spnGunSayisi.valueChanged.connect(arttır_azalt)
ui.dateGiris.dateChanged.connect(eşitle)
ui.btnKaydet.clicked.connect(kaydet)
sys.exit(uygulama.exec_())