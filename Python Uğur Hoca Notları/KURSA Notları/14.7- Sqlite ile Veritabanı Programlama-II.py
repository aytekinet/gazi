# -*- coding: utf-8 -*-
#--------------------SQL Uygulamaları----------------
# SQL (Structured Query Language), veri tabanındaki verileri okumak,
# güncellemek, yeni veri eklemek, verileri silmek vb. gibi işlemleri yapan,
# program yazarken kolaylıklar sağlayan, satırlarca kodun yaptığı işlemi tek
# bir sorguda yapabilen, yapısal bir sorgulama dilidir.
#----------Veritabanı Oluşturma----------
import sqlite3 # Burada import edildiği için aşağılarda tekrar yazılmayacaktır.
vt=sqlite3.connect("gazi.db")
vt.close()
#---------Veritabanında Bir Tablo Oluşturma----------
vt=sqlite3.connect("gazi.db")
im=vt.cursor()
im.execute("CREATE TABLE IF NOT EXISTS personel_tablo('Personel_no','Adı','Soyadı')")
im.execute("CREATE TABLE IF NOT EXISTS ogrenci_tablo('Öğrenci_no','Adı','Soyadı')")
vt.close()
#---------Veritabanından Bir Tablo Silme----------
vt=sqlite3.connect("gazi.db")
im=vt.cursor()
im.execute("DROP TABLE ogrenci_tablo")
vt.close()
#--------Tabloya Bir Sutun Ekleme--------
vt=sqlite3.connect("gazi.db")
im=vt.cursor()
im.execute("ALTER TABLE personel_tablo ADD 'Maaşı'")
vt.close()
#--------Tablodan Bir Sutun Silme--------
vt=sqlite3.connect("gazi.db")
im=vt.cursor()
im.execute("ALTER TABLE personel_tablo DROP 'Personel_no'")
vt.close()
#-------Tabloya Veri Girme-------
vt=sqlite3.connect("gazi.db")
im=vt.cursor()
im.execute("INSERT INTO personel_tablo VALUES('Uğur','Özcan',3000)")
im.execute("INSERT INTO personel_tablo VALUES('Ali','Can',4000)")
im.execute("INSERT INTO personel_tablo VALUES('Ahmet','Öz',5500)")
im.execute("INSERT INTO personel_tablo VALUES('Mehmet','Mertcan',8000)")
vt.commit()
vt.close()
#%%------Tablodan Bir Satırı Silme-----
vt=sqlite3.connect("gazi.db")
im=vt.cursor()
im.execute("DELETE FROM personel_tablo WHERE Adı='Uğur'")
vt.commit()
vt.close()
# rowid kullanılarakta silinebilir...
#-------Tabloda Bir Sutunu Güncelleme--------
vt=sqlite3.connect("gazi.db")
im=vt.cursor()
im.execute("UPDATE personel_tablo SET Maaşı=Maaşı*1.25")
vt.commit()
vt.close()
# Sorgulu sutun güncelleme
vt=sqlite3.connect("gazi.db")
im=vt.cursor()
im.execute("UPDATE personel_tablo SET Maaşı=Maaşı*1.25 WHERE Maaşı<=5000")
vt.commit()
vt.close()
#------------Tablodan Belirli Bir Sutun Verilerine Erişme--------
vt=sqlite3.connect("gazi.db")
im=vt.cursor()
im.execute("SELECT Adı FROM personel_tablo")
im.fetchall() # bir değişkene atanarak daha sonra kullanılabilir
vt.close()
#------------Tablodan Belirli Birden Fazla Sutun Verilerine Erişme--------
vt=sqlite3.connect("gazi.db")
im=vt.cursor()
im.execute("SELECT Adı,Soyadı FROM personel_tablo")
im.fetchall()
vt.close()
#----------Tablodaki Tüm Alanlara Erişme---------
vt=sqlite3.connect("gazi.db")
im=vt.cursor()
im.execute("SELECT * FROM personel_tablo")
im.fetchall()
vt.close()
#---------Sorgulu Tablo Verilerine Erişme-------
vt=sqlite3.connect("gazi.db")
im=vt.cursor()
im.execute("SELECT * FROM personel_tablo WHERE Maaşı>=5000").fetchall() #Kodda kısaltmaya gittik, yukarıdakilerle aynı işi yapar
im.execute("SELECT Adı,Soyadı FROM personel_tablo WHERE Maaşı>=5000").fetchall()
im.execute("SELECT Adı,Soyadı FROM personel_tablo WHERE NOT Maaşı>=5000").fetchall()
im.execute("SELECT Adı,Maaşı FROM personel_tablo WHERE Maaşı>=5000").fetchall()
im.execute("SELECT * FROM personel_tablo WHERE Maaşı BETWEEN 4000 AND 7000").fetchall()
im.execute("SELECT * FROM personel_tablo WHERE Adı='Uğur'").fetchall()
im.execute("SELECT * FROM personel_tablo WHERE Adı LIKE 'U%'").fetchall()
im.execute("SELECT * FROM personel_tablo WHERE Adı LIKE 'U%' AND Maaşı>=5000").fetchall() # AND arttırılabilir
im.execute("SELECT * FROM personel_tablo WHERE Adı LIKE 'U%' OR Maaşı>=5000").fetchall() # OR arttırılabilir
im.execute("SELECT * FROM personel_tablo WHERE Soyadı LIKE 'can%'").fetchall()
im.execute("SELECT * FROM personel_tablo WHERE Soyadı LIKE '%can'").fetchall()
im.execute("SELECT * FROM personel_tablo WHERE Soyadı LIKE '%can%'").fetchall()
im.execute("SELECT * FROM personel_tablo LIMIT 2").fetchall() # ilk iki kayıt
im.execute("SELECT * FROM personel_tablo ORDER BY rowid DESC LIMIT 2").fetchall() # son iki kayıt

vt.close()
#-------------Tablo Sutunlarının Belirli Bir Sutuna Göre Sıralanması-------
vt=sqlite3.connect("gazi.db")
im=vt.cursor()
im.execute("SELECT * FROM personel_tablo ORDER BY Soyadı").fetchall() #Artan sıralama yapar
im.execute("SELECT * FROM personel_tablo ORDER BY Soyadı ASC").fetchall() #Artan sıralama yapar
im.execute("SELECT * FROM personel_tablo ORDER BY Soyadı DESC").fetchall() #Azalan sıralama yapar
vt.close()
#%%
# Uygulama Sorusu
'''
Veri tabanınızda "Okul" adında bir tablo oluşturunuz.

Tablonun alan adları ve veri türleri aşağıdaki gibi olsun:
Öğrenci_no (int)
Adı (str)
Soyadı (str)
Yaşı (int)

Tabloya 4 kişinin bilgilerini içerecek şekilde kayıt girişi yapınız.

"Dersler" isminde yeni bir tablo oluşturunuz.

"Dersler" tablosunu siliniz

"Okul" tablosuna Doğum_tarihi sütununu ekleyiniz.

"Okul" tablosundaki tüm öğrencilerin yaşını 2 yaş artırınız.

Yaşı 15’ten küçük olan öğrencileri seçiniz.

"Notlar" isminde yeni bir tablo oluşturunuz. 
Ogr_Not (int) veri türünde bir alan ekleyiniz. Bu tabloya 4 tane not girişi yapınız.

Notu 60 ile 90 arasında olan öğrencileri listeleyiniz.

"Okul" tablosundaki kayıtları soyadı alanına göre sıralayınız.

"Okul" tablosundaki öğrencilerin yaşları toplamını bulunuz.

"Okul" tablosunda en büyük yaşın kaç olduğunu bulunuz.

Öğrencileri yaşlarına göre gruplayınız.
'''
#%%
#-------------------İlişkili Tablolar----------------------
# İlişkisel veri tabanları, birbirleri ile mantıksal ilişkiler içinde olan
# tablolardan oluşmaktadır. Tabloları ortak olarak sahip oldukları alanlarda
# birleştirmek için ilişkiler kullanılır. İlişki ise bir sorguda birleştirmeyle
# gösterilmektedir.
#%%
#------Tabloların Birleştirilmesi-------
# Birden fazla tablodan veri almak gerektiği durumlarda tablolar arasında
# ilişki kurulması gerekmektedir. Bu işleme Join (birleştirme) adı verilir.
# Join işlemi birden fazla tabloyu birbirine bağlayıp bu tablolar üzerinde
# işlem yapabilmemizi sağlamaktadır.
# Birleştirme işlemi yapabilmek için tabloların aynı değerleri içeren
# sütunlarının kullanılması gerekir.
#Tablo birleştirme işlemi yapılırken birleştirmek istediğiniz duruma göre,
# Kartezyen birleşim, eşiti olan birleştirme veya eşiti olmayan birleştirme
# türlerinden uygun olanını kullanabilirsiniz.
# Şimdi 2 tane ilşkisel tablo hazırlayalım.
import sqlite3
vt=sqlite3.connect("kitaplarim.db")
im=vt.cursor()
im.execute("CREATE TABLE IF NOT EXISTS kitap_tablo('Kitap_Adı','Yazarı','Grup_No')")
im.execute("CREATE TABLE IF NOT EXISTS kitap_grup_tablo('Raf_No','Grup_Adı')")
im.execute("INSERT INTO kitap_tablo VALUES('Körlük','Jose Saramago','1')")
im.execute("INSERT INTO kitap_tablo VALUES('Ben Kirke','Madeline Miller','1')")
im.execute("INSERT INTO kitap_tablo VALUES('Çocuklara Nutuk','Mustafa Kemal Atatürk','2')")
im.execute("INSERT INTO kitap_tablo VALUES('Savaş Sanatı','Sun Tzu','2')")
im.execute("INSERT INTO kitap_tablo VALUES('Suçlu İnsan','Cesare Lombroso','2')")
im.execute("INSERT INTO kitap_tablo VALUES('Bitkilerin Bildikleri','Dainel Chamovitz','3')")
im.execute("INSERT INTO kitap_grup_tablo VALUES('1','Edebiyat')")
im.execute("INSERT INTO kitap_grup_tablo VALUES('2','Araştırma-Tarih')")
im.execute("INSERT INTO kitap_grup_tablo VALUES('3','Bilim')")
vt.commit()
vt.close()
#%%
#-----------Kartezyen Çarpımı
# İki tablo arasında birleştirme koşulunun tanımlanmadığı durumlarda Kartezyen
# çarpımından söz edilir. 
# Sırada soldaki tablonun her kaydı için, sağdaki tablodan bütün kayıtları çeker.
# Ek olarak, birleştirme koşulunun geçersiz olduğu ve birinci tablodaki tüm
# satırların ikinci tablodaki tüm satırlarla birleşmediği durumlarda da
# Kartezyen çarpım elde edilir.
vt=sqlite3.connect("kitaplarim.db")
im=vt.cursor()
im.execute("SELECT * FROM kitap_tablo,kitap_grup_tablo").fetchall()
vt.close()
# kitap_tablo tablosunda 6, kitap_grup_tablo tablosunda 3 kayıt bulunmaktadır.
# Bu iki tablonun birleşiminden 6x3=18 satırlık bir birleşim meydana gelecektir.
# 1. tablodaki her kayıt için 2. tablodaki tüm kayıtlar listelenmiştir.
#%%
#------------Eşiti Olan Birleştirme
# İç birleştirme (inner join) olarak da adlandırılan birleştirme türüdür. İç birleştirme
# bir sorguya, birleştirilen tabloların birinde yer alan satırların,
# birleştirilen alanlardaki verileri temel alarak, diğer tablodaki satırlara
# karşılık geldiğini bildirir. 
# İç birleştirme içeren bir sorgu çalıştırıldığında, sorgu işlemlerine
# yalnızca, birleştirilen tabloların her ikisinde de bulunan ortak değere
# sahip olan satırlar eklenir. 
# Birleştirmede yer alan her iki tablodan sadece, birleştirme alanında eşleşen
# satırlar döndürülmek istenildiği zaman iç birleştirme kullanılır.
vt=sqlite3.connect("kitaplarim.db")
im=vt.cursor()
im.execute("SELECT * FROM kitap_tablo,kitap_grup_tablo WHERE kitap_tablo.Grup_No=kitap_grup_tablo.Raf_No").fetchall()
#veya
im.execute("SELECT * FROM kitap_tablo INNER JOIN kitap_grup_tablo ON kitap_tablo.Grup_No=kitap_grup_tablo.Raf_No").fetchall()
vt.close()
#%%
#------------Eşiti Olmayan Birleştirme
# Eşiti olan birleştirme sırasında bir tablodaki bir sütunun içerdiği değerler
# diğer tablonun ilgili sütunu ile eşleştirilip sadece eşleşen değerler
# birleştiriliyordu. Eşleşmeyen satırlar ise birleştirilemiyordu. 
# Eşleşmeyen satırların da birleştirilip sonuca dahil edilmesi istenilen
# durumlarda “Eşiti Olmayan Birleştirme” kullanılmaktadır.
# Eşiti olmayan birleştirmeler (dış birleştirmeler), eşleşmeyen kayıtların
# hangi tabloda olduğuna bakarak sol dış birleştirme veya sağ dış birleştirme
# olmak üzere iki şekilde olabilmektedir.
vt=sqlite3.connect("kitaplarim.db")
im=vt.cursor()
im.execute("SELECT * FROM kitap_tablo RIGHT JOIN kitap_grup_tablo ON kitap_tablo.Grup_No=kitap_grup_tablo.Raf_No").fetchall()
im.execute("SELECT * FROM kitap_tablo LEFT JOIN kitap_grup_tablo ON kitap_tablo.Grup_No=kitap_grup_tablo.Raf_No").fetchall()
vt.close()
# Halihazırda RIGHT JOIN desteklenmiyor.
# OperationalError: RIGHT and FULL OUTER JOINs are not currently supported
# Bunun yerine aşağıdakini kullanabiliriz;
im.execute("SELECT * FROM kitap_grup_tablo LEFT JOIN kitap_tablo ON kitap_tablo.Grup_No=kitap_grup_tablo.Raf_No").fetchall()
#%%
# Uygulama
# Şimdi kitap_tablo'ya 2 yeni sutun ekleyip, bu sutunlara değer verelim.
vt=sqlite3.connect("kitaplarim.db")
im=vt.cursor()
im.execute("ALTER TABLE kitap_tablo ADD 'Fiyatı'")
im.execute("ALTER TABLE kitap_tablo ADD 'İndirim_Oranı'")
im.execute("UPDATE kitap_tablo SET Fiyatı=20, İndirim_Oranı=30 WHERE Kitap_Adı='Körlük'")
im.execute("UPDATE kitap_tablo SET Fiyatı=25, İndirim_Oranı=20 WHERE Kitap_Adı='Ben Kirke'")
im.execute("UPDATE kitap_tablo SET Fiyatı=30, İndirim_Oranı=25 WHERE Kitap_Adı='Çocuklara Nutuk'")
im.execute("UPDATE kitap_tablo SET Fiyatı=35, İndirim_Oranı=35 WHERE Kitap_Adı='Savaş Sanatı'")
im.execute("UPDATE kitap_tablo SET Fiyatı=25, İndirim_Oranı=15 WHERE Kitap_Adı='Suçlu İnsan'")
im.execute("UPDATE kitap_tablo SET Fiyatı=40, İndirim_Oranı=10 WHERE Kitap_Adı='Bitkilerin Bildikleri'")
im.execute("UPDATE kitap_tablo SET Fiyatı=20, İndirim_Oranı=25 WHERE Kitap_Adı='Sanatın Öyküsü'")
vt.commit()
vt.close()
# Şimdi kitap_tabloyu olduğu gibi kopyalayıp, indirim oranını fiyat üzerine
# uygulayıp, indirim oranı sutununu kaldıralım. Tüm bunları Python ile yapalım.
vt=sqlite3.connect("kitaplarim.db")
im=vt.cursor()
veri=im.execute("SELECT * FROM kitap_tablo").fetchall()
vt.close()
print(veri)
len(veri)
type(veri)
type(veri[0])
for i in range(0,len(veri)):
    veri[i]=list(veri[i])
for i in range(0,len(veri)):
    veri[i][3]=veri[i][3]*(1-veri[i][4]/100)
    veri[i]=veri[i][0:4]
print(veri)
vt=sqlite3.connect("kitaplarim.db")
im=vt.cursor()
im.execute("DROP TABLE kitap_tablo")
im.execute("CREATE TABLE IF NOT EXISTS kitap_tablo('Kitap_Adı','Yazarı','Grup_No','Fiyatı')")
for i in veri:
    im.execute("INSERT INTO kitap_tablo VALUES(?,?,?,?)", i)
vt.commit()
vt.close()
# Gördüğünüz gibi verileri bir defa Python ortamına aldığımızda istediğimiz
# her şeyi yapabiliriz.
def kayıtları_göster():
    import sqlite3
    vt=sqlite3.connect("gazi.db")
    im=vt.cursor()
    im.execute("SELECT rowid, * FROM personel_tablo")
    kayıtlar=im.fetchall()
    for i in kayıtlar:
        print(i)
kayıtları_göster()






