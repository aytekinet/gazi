# -*- coding: utf-8 -*-
SQL-Ozet
#---------Veritabaninda Bir Tablo Olusturma----------
CREATE TABLE IF NOT EXISTS tablo_adi('sutunBaslik_1','sutunBaslik_2')
#---------Veritabanindan Bir Tablo Silme----------
DROP TABLE tablo_adi
#--------Tabloya Bir Sutun Ekleme--------
ALTER TABLE tablo_adi ADD 'sutunBaslik'
#--------Tablodan Bir Sutun Silme--------
ALTER TABLE tablo_adi DROP 'sutunBaslik'
#-------Tabloya Veri Girme-------
INSERT INTO tablo_adi VALUES('Veri_1','Veri_2')
#------Tablodan Bir Satiri Silme-----
DELETE FROM tablo_adi WHERE kosul
#-------Tabloda Bir Sutunu Guncelleme--------
UPDATE tablo_adi SET sutunBaslik=yeniSutunDegeri
# Sorgulu hucre guncelleme
UPDATE tablo_adi SET sutunBaslik=yeniSutunDegeri WHERE kosul
#------------Tablodan Belirli Bir Sutun Verilerine Erisme--------
SELECT sutunBaslik FROM tablo_adi
#------------Tablodan Belirli Birden Fazla Sutun Verilerine Erisme--------
SELECT sutunBaslik_1,sutunBaslik_2 FROM tablo_adi
#----------Tablodaki Tum Alanlara Erisme---------
SELECT * FROM tablo_adi
#---------Sorgulu Tablo Verilerine Erisme-------
SELECT * FROM tablo_adi WHERE kosul
SELECT sutunBaslik_1,sutunBaslik_2 FROM tablo_adi WHERE kosul
#---------Kosul Ornekleri--------
SELECT * FROM tablo_adi ...
WHERE Maaşı>=5000
WHERE NOT Maaşı>=5000
WHERE Maaşı BETWEEN 4000 AND 7000
WHERE Adı='Uğur'
WHERE Adı LIKE 'U%'
WHERE Adı LIKE 'U%' AND Maaşı>=5000
WHERE Adı LIKE 'U%' OR Maaşı>=5000
WHERE Soyadı LIKE 'can%'
WHERE Soyadı LIKE '%can'
WHERE Soyadı LIKE '%can%'
LIMIT 2
ORDER BY rowid DESC LIMIT 2
#-------------Tablo Sutunlarinin Belirli Bir Sutuna Gore Siralanmasi-------
SELECT * FROM tablo_adi ORDER BY sutunBaslik
SELECT * FROM tablo_adi ORDER BY sutunBaslik ASC
SELECT * FROM tablo_adi ORDER BY sutunBaslik DESC
#-------------------İlişkili Tablolar----------------------
#-----------Kartezyen Çarpımı
SELECT * FROM tablo_1,tablo_2
# Bu iki tablonun birleşiminden (tablo_1_kayıt_sayısı * tablo_2_kayıt-sayısı) kadar satırlık bir birleşim meydana gelecektir.
# 1. tablodaki her kayıt için 2. tablodaki tüm kayıtlar listelenir.
#------------Eşiti Olan Birleştirme
SELECT * FROM tablo_1,tablo_2 WHERE tablo_1.iliskili_sutun_1=tablo_2.iliskili_sutun_2
#veya
SELECT * FROM tablo_1 INNER JOIN tablo_2 ON tablo_1.iliskili_sutun_1=tablo_2.iliskili_sutun_2
#------------Eşiti Olmayan Birleştirme
SELECT * FROM tablo_1 LEFT JOIN tablo_2 ON tablo_1.iliskili_sutun_1=tablo_2.iliskili_sutun_2
# Halihazırda RIGHT JOIN desteklenmiyor. Bunun yerine aşağıdakini kullanabiliriz;
SELECT * FROM tablo_2 LEFT JOIN tablo_1 ON tablo_1.iliskili_sutun_1=tablo_2.iliskili_sutun_2
