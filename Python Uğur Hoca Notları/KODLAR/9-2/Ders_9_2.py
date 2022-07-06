# -*- coding: utf-8 -*-
#%% Veritabanı
import sqlite3
vt=sqlite3.connect("veritabanı.ugur")#harddisk kalıcı
#vt=sqlite3.connect(":memory:") #ram üzerinde geçici
#vt=sqlite3.connect("") #harddisk üzerinde geçici
im=vt.cursor()
im.execute("") #SQL komutları buraya yazılır
vt.commit() #yapılan işlemleri kalıcı hale getirir
vt.close() #işimiz bittikten sonra kapatıyoruz
#%% tablo ekleme
import sqlite3
vt=sqlite3.connect("veritabanı.ugur")
im=vt.cursor()
#im.execute("CREATE TABLE ilkTablo(ADI,SOYADI)")
im.execute("CREATE TABLE IF NOT EXISTS ilkTablo(ADI,SOYADI)")
vt.commit()
vt.close()
#%%tablo silme
import sqlite3
vt=sqlite3.connect("veritabanı.ugur")
im=vt.cursor()
im.execute("CREATE TABLE ikinciTablo(ADI,SOYADI)")
#im.execute("DROP TABLE ikinciTablo")
im.execute("DROP TABLE IF EXISTS ikinciTablo")
vt.commit()
vt.close()
#%% kayıt ekleme
import sqlite3
vt=sqlite3.connect("OGRENCİ.db")
im=vt.cursor()
im.execute("""CREATE TABLE IF NOT EXISTS tablo(
          ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
          ADI TEXT NOT NULL,
          SOYADI TEXT NOT NULL,
          NOTU NUMERIC NOT NULL,
          YASI INTEGER)""")
#im.execute("""INSERT INTO tablo(ADI,SOYADI,NOTU,YASI) 
#           VALUES('Uğur','Özcan',98,44)""")
#im.execute("""INSERT INTO tablo(ADI,SOYADI,NOTU,YASI) 
#           VALUES(?,?,?,?)""",('Ahmet','Can',57,18))           

adi1='Ali'
soyadi1='Öz'
notu1=78
yasi1=28
im.execute(f"INSERT INTO tablo(ADI,SOYADI,NOTU,YASI) VALUES('{adi1}','{soyadi1}',{notu1},{yasi1})")


liste=[("İsmet","Kara",85,32),("Hikmet","Kaya",45,23),("Ahmet","Kasa",87,40)]
for i in liste:
    im.execute("INSERT INTO tablo (ADI,SOYADI,NOTU,YASI) VALUES (?,?,?,?)",i)
im.executemany("INSERT INTO tablo (ADI,SOYADI,NOTU,YASI) VALUES (?,?,?,?)",liste)
vt.commit()
vt.close()
#%% kayıt silme
import sqlite3
vt=sqlite3.connect("OGRENCİ.db")
im=vt.cursor()
im.execute("""CREATE TABLE IF NOT EXISTS tablo(
          ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
          ADI TEXT NOT NULL,
          SOYADI TEXT NOT NULL,
          NOTU NUMERIC NOT NULL,
          YASI INTEGER)""")
im.execute("DELETE FROM tablo WHERE ID=8")
im.execute("DELETE FROM tablo WHERE ADI='Ahmet'")
im.execute("DELETE FROM tablo") #TUM TABLOYU SİLER
vt.commit()
vt.close()    
#%% sutun ekleme ve silme
import sqlite3
vt=sqlite3.connect("OGRENCİ.db")
im=vt.cursor()
im.execute("""CREATE TABLE IF NOT EXISTS tablo(
          ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
          ADI TEXT NOT NULL,
          SOYADI TEXT NOT NULL,
          NOTU NUMERIC NOT NULL,
          YASI INTEGER)""")
#im.execute("ALTER TABLE tablo ADD MAHALLE TEXT") #EKLEME
im.execute("ALTER TABLE tablo DROP SEHIR") #SİLME
vt.commit()
vt.close()
#%% KAYIT GUNCELLEME
import sqlite3
vt=sqlite3.connect("OGRENCİ.db")
im=vt.cursor()
im.execute("""CREATE TABLE IF NOT EXISTS tablo(
          ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
          ADI TEXT NOT NULL,
          SOYADI TEXT NOT NULL,
          NOTU NUMERIC NOT NULL,
          YASI INTEGER)""")
#im.execute("UPDATE tablo SET NOTU=NOTU+10")
im.execute("UPDATE tablo SET NOTU=NOTU+20 WHERE NOTU=55")
vt.commit()
vt.close()
#%% fetchone(), fetchmany(),fetchall()
import sqlite3
vt=sqlite3.connect("OGRENCİ.db")
im=vt.cursor()
im.execute("""CREATE TABLE IF NOT EXISTS tablo(
          ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
          ADI TEXT NOT NULL,
          SOYADI TEXT NOT NULL,
          NOTU NUMERIC NOT NULL,
          YASI INTEGER)""")
#im.execute("SELECT ADI,SOYADI FROM tablo")
#im.fetchone()[1]
im.execute("SELECT * FROM tablo")
#im.fetchmany(2)[0][3]
veri=im.fetchall()[2:5]
veri
veri=im.execute("SELECT * FROM tablo").fetchall()
veri
vt.commit()
vt.close()
#%% filtreleme
import sqlite3
vt=sqlite3.connect("OGRENCİ.db")
im=vt.cursor()
im.execute("""CREATE TABLE IF NOT EXISTS tablo(
          ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
          ADI TEXT NOT NULL,
          SOYADI TEXT NOT NULL,
          NOTU NUMERIC NOT NULL,
          YASI INTEGER)""")
veri=im.execute("SELECT * FROM tablo WHERE ADI='İsmet'").fetchall()
veri=im.execute("SELECT * FROM tablo WHERE ADI LIKE '%met'").fetchall()
veri=im.execute("SELECT * FROM tablo WHERE ADI LIKE '%m%' AND NOTU>90").fetchall()
veri=im.execute("SELECT * FROM tablo WHERE ADI LIKE '%m%' AND NOTU>90 AND YASI>35").fetchall()
veri=im.execute("SELECT * FROM tablo WHERE ADI LIKE '%m%' OR NOTU>90 OR YASI>35").fetchall()
veri=im.execute("SELECT * FROM tablo WHERE ADI LIKE '%m%' OR (NOTU>90 AND YASI>35)").fetchall()
veri=im.execute("SELECT * FROM tablo WHERE NOTU BETWEEN 60 AND 90").fetchall()
veri=im.execute("SELECT * FROM tablo WHERE YASI BETWEEN 20 AND 40").fetchall()
veri=im.execute("SELECT * FROM tablo ORDER BY NOTU").fetchall()
veri=im.execute("SELECT * FROM tablo ORDER BY NOTU DESC").fetchall()
veri=im.execute("SELECT * FROM tablo ORDER BY YASI").fetchall()
veri=im.execute("SELECT * FROM tablo ORDER BY YASI DESC").fetchall()
veri=im.execute("SELECT * FROM tablo ORDER BY YASI DESC LIMIT 4").fetchall()

print(veri)
vt.commit()
vt.close()
#%%
import sqlite3
vt=sqlite3.connect("OGRENCİ.db")
im=vt.cursor()
im.execute("""CREATE TABLE IF NOT EXISTS tablo(
          ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
          ADI TEXT NOT NULL,
          SOYADI TEXT NOT NULL,
          NOTU NUMERIC NOT NULL,
          YASI INTEGER)""")
veri=im.execute("SELECT name FROM sqlite_master").fetchall()
veri=im.execute("SELECT sql FROM sqlite_master").fetchall()
print(veri)
vt.commit()
vt.close()
#%%



