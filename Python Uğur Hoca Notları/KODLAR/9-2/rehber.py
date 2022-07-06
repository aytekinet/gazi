# -*- coding: utf-8 -*-
class Rehber():
    import sqlite3
    vt=sqlite3.connect("rehber.db")
    im=vt.cursor()
    im.execute("""CREATE TABLE IF NOT EXISTS tablo(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        ADI TEXT NOT NULL,
        SOYADI TEXT NOT NULL,
        TELEFON INTEGER NOT NULL)""")
    def kayıt_ekle(self):
        adı=input("Adı: ")
        soyadı=input("Soyadı: ")
        telefonu=input("Telefonu: ")
        self.im.execute("""INSERT INTO tablo(ADI,SOYADI,TELEFON)
                        VALUES(?,?,?)""",(adı,soyadı,telefonu))
        self.vt.commit()
    def kayıt_sil(self):
        silinecek=int(input("Silinecek ID: "))
        self.im.execute(f"DELETE FROM tablo WHERE ID={silinecek}")
        self.vt.commit()
    def kayıt_güncelle(self):
        guncellenecek=int(input("Güncellenecek ID: "))
        başlık=input("Güncellenecek başlık: ")
        yeni_değer=input("Yeni değer: ")
        self.im.execute(f"UPDATE tablo SET {başlık}='{yeni_değer}' WHERE ID={guncellenecek}")
        self.vt.commit()
    def çıkış(self):
        self.vt.close()
    def listele(self):
        veri=self.im.execute("SELECT * FROM tablo").fetchall()
        print(veri)
    def bul(self):
        bulunacak=input("Bul: ")
        veri=self.im.execute(f"SELECT * FROM tablo WHERE (ADI LIKE '%{bulunacak}%') OR (SOYADI LIKE '%{bulunacak}%') OR (TELEFON LIKE '%{bulunacak}%') ").fetchall()
        print(veri)
r=Rehber()
r.kayıt_ekle() 
r.kayıt_sil()
r.kayıt_güncelle()
r.listele()
r.bul()

