# -*- coding: utf-8 -*-
# SQLite ile Veritabanı Programlama
#%%
# Bu bölümde, Python’daki ileri düzey konulardan biri olan veritabanı
# programlamayı (database programming) inceleyecegiz.
# Öncelikle ‘veritabanı’ kavramının ne oldugunu anlamaya çalısarak ise baslayalım.
# Veritabanı, herkesin bildigi ve kullandıgı anlamıyla, içinde veri barındıran bir ‘sey’dir.
# Teknik tarifi;
# Sistematik erisim imkanı olan, yönetilebilir, güncellenebilir, tasınabilir,
# birbirleri arasında tanımlı iliskiler bulunabilen veriler kümesidir.
# Bir baska tanımı da, bir bilgisayarda sistematik sekilde saklanmıs,
# programlarca islenebilecek veri yıgınıdır.
# Python’la veritabanı programlama islemleri için pek çok alternatif var.
# Python’la hangi veritabanı sistemlerini kullanabileceginizi görmek için
# http://wiki.python.org/moin/DatabaseInterfaces adresindeki listeyi inceleyebilirsiniz.
#%%
#---------------Neden SQLite?-----------------
# Biz bunlar içinde, sadeligi, basitligi ve kullanım kolaylıgı nedeniyle SQLite
# adlı veritabanı yönetim sistemini ele alacagız.
# Sqlite’ın öteki sistemlere göre pek çok avantajı bulunur.
# Sqlite’ın bazı avantajları:
# 1) Her seyden önce Sqlite Python’un 2.5 sürümlerinden bu yana bu dilin bir parçasıdır.
# Anaconda Prompt üzerinde conda list yazarsanız sqlite'in yüklü olduğunu görürsünüz.
# Dolayısıyla eger kullandıgınız Python sürümü 2.5 veya üstü ise Sqlite’ı Python’daki
# herhangi bir modül gibi içe aktarabilir ve kullanmaya baslayabilirsiniz.
# 2) Sqlite herhangi bir yazılım veya sunucu kurulumu gerektirmez. Bu sayede, bu
# modülü kullanabilmek için öncelikle bir sunucu yapılandırmanıza da gerek yoktur.
# Bazı veritabanlarını kullanabilmek için arka planda bir veritabanı sunucusu çalıstırıyor
# olmanız gerekir. Sqlite’ta ise böyle bir sey yapmazsınız.
# 3) Sqlite, öteki pek çok veritabanı alternatifine göre basittir. Bu yüzden Sqlite’ı çok kısa bir
# sürede kavrayıp kullanmaya baslayabilirsiniz.
# 4) Sqlite özgür bir yazılımdır. Bu yazılımın bastan asagı bütün kodları kamuya açıktır.
# Dolayısıyla Sqlite kodlarının her zerresini istediginiz gibi kullanabilir, degisiklige
# ugratabilir, satabilir ve ticari olan/olmayan bütün uygulamalarınızda gönül rahatlıgıyla
# kullanabilirsiniz.
# 5) Sqlite’ın sade ve basit olması sizi yanıltmasın. Bu özelliklerine bakarak, Sqlite’ın
# yeteneksiz bir veritabanı sistemi oldugunu düsünmeyin. Bugün Sqlite’ı aktif olarak
# kullanan pek çok büyük ve tanınmıs sirket bulunur. Mesela, Adobe, Apple,
# Mozilla/Firefox, Google, Symbian ve Sun bu sirketlerden bazılarıdır.
#%%
#-------------------SQLite'ın Yapısı-----------------------------
# Daha önce tarif ettiğimiz gibi Veritabanları, verileri sonradan kullanılmak
# üzere içinde tutan bir sistemdir.
# Bütün iliskisel veritabanlarında oldugu gibi, Sqlite da bu verileri tablo
# benzeri bir yapı içinde tutar.
# Bir Sqlite veritabanı içindeki veriler söyle bir yapıya sahiptir:
#Sütun 1   Sütun 2   Sütun 3   Sütun 4   Sütun 5
#Deger 1/1 Deger 2/1 Deger 3/1 Deger 4/1 Deger 5/1
#Deger 1/2 Deger 2/2 Deger 3/2 Deger 4/2 Deger 5/2
#Deger 1/3 Deger 2/3 Deger 3/3 Deger 4/3 Deger 5/3
#Deger 1/4 Deger 2/4 Deger 3/4 Deger 4/4 Deger 5/4
# Sqlite içinde olusturulan yukarıdakine benzer her tablonun bir de ismi vardır.
# Yani, Sqlite ile bir tablo olustururken, bu tabloya bir de ad vermemiz gerekir.
# Sqlite ile çalısırken veriler üzerinde yapacagımız islemleri, yukarıdaki
# tablonun adını ve bu tablodaki sütunları kullanarak gerçeklestirecegiz.
# Bu yüzden Sqlite’ın yapısını anlamak büyük önem tasır.
# Gördügünüz gibi, bu veritabanı sisteminin yapısını anlamak da öyle zor degildir.
#%%
#----------------Yardımcı Araçlar--------------------------
# Veritabanları üzerinde yapacagımız çalısmalar sırasında, islerimizi
# kolaylastırmak için bazı harici araçlara da ihtiyaç duyacagız.
#----------------SQLite Browser------------------------------
# Sqlitebrowser, Sqlite veritabanlarının içerigini grafik bir arayüz aracılıgıyla
# görüntüleyebilmemizi saglayan bir programdır.
# Bu program sayesinde, veritabanı üzerinde yaptıgınız çalısmanın dogru sonuç
# verip vermedigini teyit edebilir, elinizdeki veritabanının içeriginde hangi
# verilerin oldugunu açık seçik görebilirsiniz.
# Bu programı indirmek için ziyaret etmemiz gereken adres:
#    http://sqlitebrowser.org/
# Download kısmından size uygun olanı seçerek yükleyebilirsiniz.
# Kendiniz yeni bir veritabanı oluşturun. Öğeleri aşağıdakiler olsun:
    # SıraNo    Adı Soyadı     Yaşı
# Yine kendiniz örneğin bir .csv dosyasını içe aktarın.
#%%
#-----------------Yeni Bir Veritabanı Olusturmak----------------------
#-----------------Varolan Bir Veritabanına Bağlanmak------------------
# Öncelikle sqlite modülünü import edelim.
import sqlite3
# Şimdi "gazi_teknoloji" adında bir veritabanı oluşturalım. Veritabanı aktif
# çalışma dizininde oluşturulacak. Eger belirtilen isimde bir veritabanı
# bulunmuyorsa o adla yeni bir veritabanı olusturulacaktır. Varsa, varolan
# veritabanına bağlanacak. Aktif çalışma dizinin dışındaki bir dizinden veritabanına
# bağlanmak isterseniz yol (path) belirtmeniz gerekir.
veritabanım=sqlite3.connect("gazi_teknoloji.sqlite")
veritabanıma_bağlan=sqlite3.connect("ilkVeritabanim.db")
# Bu arada, veritabanı dosyasının uzantısı olarak .sqlite‘ı seçtik.
# Ama eger siz isterseniz kendinize uygun baska bir uzantı da belirleyebilirsiniz.
# Veritabanı dosyasının uzantısının ne olması gerektigi konusunda kesin kurallar bulunmaz.
# .sqlite uzantısının yerine, .sqlite3, .db veya .db3 gibi uzantıları tercih edebilisiniz.
# Hatta eger siz isterseniz veritabanınızın uzantısını .ankara olarak dahi
# belirleyebilirsiniz. Bu konuda herhangi bir kısıtlama bulunmaz.
# Yukarıdaki komut yardımıyla sabit disk üzerinde bir Sqlite veritabanı dosyası
# olusturmus oluyoruz. Ancak isterseniz sqlite3 ile geçici bir veritabanı da
# olusturabilirsiniz:
geçici_veritabanım_bellek=sqlite3.connect(":memory:") # ":memory:" ifadesini kullanmanız gerekir.
# Olusturdugunuz bu geçici veritabanı RAM (bellek) üzerinde çalısır. Veritabanını
# kapattıgınız anda da bu geçici veritabanı silinir.
# Eger isterseniz, sabit disk üzerinde de geçici veritabanları olusturabilirsiniz.
geçici_veritabanım_sabitDisk=sqlite3.connect("") # "" ifadesinde boşluk olmayacak.
# Tıpkı :memory: kullanımında oldugu gibi, bos karakter dizisiyle olusturulan geçici
# veritabanları da veritabanı baglantısının kesilmesiyle birlikte ortadan kalkacaktır.
# Geçici veritabanı olusturmak, özellikle çesitli testler veya denemeler
# yaptıgınız durumlarda isinize yarar.
# Sonradan nasıl olsa sileceginiz, sırf test amaçlı tuttugunuz bir veritabanını
# disk üzerinde olusturmak yerine RAM üzerinde olusturmayı tercih edebilirsiniz.
# Ayrıca, geçici veritabanları sayesinde, yazdıgınız bir kodu test ederken bir
# hatayla karsılasırsanız sorunun veritabanı içinde varolan verilerden degil,
# yazdıgınız koddan kaynaklandıgından da emin olabilirsiniz.
# Çünkü, programın her yeniden çalısısında veritabanı yukarıdaki kodlarla bastan
# olusturulacaktır.
#%%
#-------------------İmleç Oluşturma-----------------
# connect() metodu, bir veritabanı üzerinde islem yapabilmemizin ilk adımıdır.
# Veritabanını olusturduktan veya varolan bir veritabanı ile baglantı kurduktan
# sonra, veritabanı üzerinde islem yapabilmek için sonraki adımda bir imleç
# olusturmamız gerekir.
imlecim=veritabanım.cursor()
# Yukarıda olusturdugumuz imlecim nesnesinin execute() metodunu kullanarak
# SQL komutlarını çalıstıriz.
#%%
#------------------Tablo Oluşturma---------------------
# Şimdi en baştan başlayarak bir tablo oluşturalım.
import sqlite3
vt=sqlite3.connect("calisan_db.sqlite")
im=vt.cursor()
# Simdi de yukarıda olusturdugumuz imlecin execute() adlı metodunu kullanarak
# veritabanı içinde bir tablo olusturalım:
im.execute("CREATE TABLE calisan_tablosu(adı,soyadı)")
# Burada yapılan sey, calisan_tablosu isimli bir tablo olusturup, bu tabloya
# adı ve soyadı isimli iki sütun eklemekten ibarettir.
# Bu komuttaki CREATE TABLE kısmı bir SQL komutudur ve bir tablo olusturulmasını saglar.
# Büyük harfle yazılması adettendir. Küçük harfle de yazılabilir.
# Bu kodları kullanarak olusturdugunuz calisan_db.sqlite adlı veritabanı
# dosyasının içerigini kontrol etmek için SQLite browser ile görüntüleyin.
#%%
#-------------Sartlı Tablo Olusturma-------------------
# Yukarıda tablo oluşturma kodunu tekrar çalıştırırsanız hata alırsınız.
# OperationalError: table calisan_tablosu already exists
# Bir veritabanı üzerinde islem yaparken, aynı ada sahip iki tablo olusturamayız.
# Bu hatayı önlemek için sartlı tablo olusturma yönteminden yararlanacagız.
import sqlite3
vt=sqlite3.connect("calisan_db.sqlite")
im=vt.cursor()
im.execute("CREATE TABLE IF NOT EXISTS calisan_tablosu(adı,soyadı)")
# Eger veritabanında bu tablo yoksa olusturacak, bu adla zaten bir tablo varsa
# sessizce yoluna devam edecektir.
#%%
#-------------Tabloya Veri Girme-------------------------
im.execute("INSERT INTO calisan_tablosu VALUES('Uğur','Özcan')")
# Bu kodları çalıstırdıktan sonra, eger veritabanının içerigini Sqlitebrowser
# ile kontrol ettiyseniz verilerin veritabanına islenmedigini göreceksiniz.
# Burada INSERT INTO tablo_adı VALUES adlı yeni bir SQL komutu daha ögreniyoruz.
#%%
#------------Verilerin Veritabanına Islenmesi-------------
# Buraya kadar sadece verileri girdik. Ama verileri veritabanına islemedik.
vt.commit()
# Dikkate edilmesi gereken bir husus; commit() imlecin degil, baglantı nesnesinin
# (yani burada vt degiskeninin) bir metodudur.
# Eger vt.commit() satırını yazmazsak, veritabanı, tablo ve sütun baslıkları
# olusturulur, ama sütunların içerigi veritabanına islenmez.
#%%
#-----------Veritabanının Kapatılması-------------------
# Bir veritabanı üzerinde yapacagımız bütün islemleri tamamladıktan sonra, o
# veritabanını kapatmamız gerekir.
vt.close()
# Bu sekilde, veritabanının ilk açıldıgı andan itibaren, isletim sisteminin
# devreye soktugu kaynakları serbest bırakmıs oluyoruz.
# Şimdi kodları birleştirelim.
import sqlite3
vt=sqlite3.connect("calisan_db.sqlite")
im=vt.cursor()
im.execute("CREATE TABLE IF NOT EXISTS calisan_tablosu(adı,soyadı)")
im.execute("INSERT INTO calisan_tablosu VALUES('Uğur','Özcan')")
vt.commit()
vt.close()
# Eger üzerinde islem yaptıgınız veritabanının her sey bittikten sonra otomatik
# olarak kapanmasını garantilemek isterseniz, with ifadesini kullanabilirsiniz.
import sqlite3
with sqlite3.connect("calisan_db.sqlite") as vt:
    im=vt.cursor()
    im.execute("CREATE TABLE IF NOT EXISTS calisan_tablosu(adı,soyadı)")
    im.execute("INSERT INTO calisan_tablosu VALUES('Ali','Can')")
    vt.commit()
#%%
#------------------Parametreli Sorgular----------------
# Yukarıdaki örneklerde verileri tek tek biz oluşturduğumuzda uygun bir
# yaklaşım ancak dışarıdan veri alırken bunu uygulayamayız. Örneğin:
veri=[('Uğur','Özcan'),('Ali','Can'),('Ahmet','Öz'),('Mehmet','Canlı'),('Ayşe','Özlü')]
veri=[['Uğur','Özcan'],['Ali','Can'],('Ahmet','Öz'),('Mehmet','Canlı'),['Ayşe','Özlü']]
veri=(['Uğur','Özcan'],['Ali','Can'],('Ahmet','Öz'),('Mehmet','Canlı'),['Ayşe','Özlü'])
# Bunun için;
import sqlite3
vt=sqlite3.connect("calisan_db.sqlite")
im=vt.cursor()
im.execute("CREATE TABLE IF NOT EXISTS calisan_tablosu(adı,soyadı)")
for i in veri:
    im.execute("INSERT INTO calisan_tablosu VALUES(?,?)", i)
vt.commit()
vt.close()
# Burada veritabanına islenecek veriler, veri adlı bir degiskenden geliyor.
# veri değişkeni liste ve tuple olarak tanımlanmış. Bu degisken içindeki verileri
# veritabanına nasıl yerlestirdigimize dikkat edin: her bir sütunun altına
# gelecek her bir deger için bir adet ‘?’ isareti yerlestirdik.
# '?' isareti SQL injection'dan kaçınmanın yollarından birisidir.
# Bir tabloya birden fazla veri girişini aşağıdaki şekilde yaparsak daha pratik 
# olur.
veri=[('Uğur','Özcan'),('Ali','Can'),('Ahmet','Öz'),('Mehmet','Canlı'),('Ayşe','Özlü')]
import sqlite3
vt=sqlite3.connect("calisan_db.sqlite")
im=vt.cursor()
im.executemany("INSERT INTO calisan_tablosu VALUES(?,?)", veri)
vt.commit()
vt.close()
#%%
#---------------------Tablodaki Verileri Seçmek-------------------
# Veritabanından herhangi bir veri alabilmek için ilk olarak
# SELECT veri FROM tablo_adı adlı bir SQL komutundan yararlanarak ilgili
# verileri seçmemiz gerekiyor.
import sqlite3
vt=sqlite3.connect("calisan_dp.sqlite")
im=vt.cursor()
im.execute("SELECT * FROM calisan_tablosu")
# Burada * ifadesi calisan_tablosundaki herşeyin seçilmesini sağlar.
#%%
#---------------------Seçilen Verileri Almak----------------------
#%%
#-------fetchall() Metodu-------
# Veritabanındaki verileri seçtikten sonra bir değişkene atayalım ve yazdıralım.
import sqlite3
vt = sqlite3.connect('calisan_db.sqlite')
im = vt.cursor()
im.execute("SELECT * FROM calisan_tablosu")
veriler = im.fetchall()
vt.close()
print(veriler)
# fetchall() imlecin bir metodudur.
# Yukarıda gördügümüz SELECT * FROM calisan_tablosu komutu tablodaki bütün
# verileri seçiyordu. fetchall() metodu ise seçilen bu verileri alma islevi
# görüyor.
# Ayrıca fetchall() ile bir veritabanındaki bütün tabloların adlarını alabiliriz.
# SQLite browser üzerinden de veritabanını açtıktan sonra içindeki tabloları
# görebilirsiniz. Ama kod yazmak istersek:
import sqlite3
vt=sqlite3.connect("calisan_db.sqlite")
im=vt.cursor()
im.execute("SELECT name FROM sqlite_master")
im.fetchall() # fetchall() tablo içeriğinden name niteliğini verdi
# Bütün Sqlite veritabanlarında, ilgili veritabanının semasını gösteren
# ‘sqlite_master’ adlı bir tablo bulunur.
# Iste bu tabloyu sorgulayarak veritabanı hakkında bilgi edinebiliriz.
# Yukarıdaki örnekte, bu ‘sqlite_master’ tablosunun ‘name’ (isim) niteligini
# sorguladık. Şimdi de kodun devamına aşağıdakileri yazarak verilere ulaşabiliriz.
im.execute("SELECT * FROM calisan_tablosu")
im.fetchall() # fetchall() burda da tablo içeriğini verdi
vt.close()
# Tabloda belirli bir satırı veya satırları almak istersek;
im.fetchall()[0] # tablonun ilk satırını getirir
im.fetchall()[2:4] # tablonun 2. ve 3. satırını getirir
# Bu indeksleme fonksiyonun özelliğinden değil, tipinin list olmasından dolayıdır.
# rowid ile almak ve yazdırmak istersek;
import sqlite3
vt=sqlite3.connect("calisan_db.sqlite")
im=vt.cursor()
im.execute("SELECT rowid, * FROM calisan_tablosu")
veri=im.fetchall()
for i in veri:
    print(i)
#%%
#------------------fetchone() Metodu-------------
# fetchone() metodu, bir veritabanından seçilen verilerin tek tek
# alınabilmesine izin verir.
import sqlite3
vt=sqlite3.connect("calisan_db.sqlite")
im=vt.cursor()
im.execute("SELECT * FROM calisan_tablosu")
im.fetchone()
# ilk satırı verdi, bir alt satırı daha almak istersek;
im.fetchone()
vt.close()
# Aldığımız satırın beliri bir öğesini ve öğrelerini almak istersek;
im.fetchone()[0] #ilgili satırın ilk öğesini getirir
im.fetchone()[0:2] #ilgili satırın ilk iki öğesini getirir
#%%
#----------------fetchmany() Metodu--------------
# Bu metot, bir veritabanından seçtiginiz verilerin istediginiz kadarını
# alabilmenize imkan tanır. İlk satırdan itibaren verir.
import sqlite3
vt=sqlite3.connect("calisan_db.sqlite")
im=vt.cursor()
im.execute("SELECT * FROM calisan_tablosu")
im.fetchmany(3) # İlk beş veriyi aldık.
vt.close()
#%%
# Bu metotların dısında, for döngüsünden yararlanarak da veri çekebilirsiniz.
import sqlite3
vt=sqlite3.connect("calisan_db.sqlite")
im=vt.cursor()
im.execute("SELECT * FROM calisan_tablosu")
for i in im.fetchall():
    print(i)
#veya
for i in range(5):
    print(im.fetchone())
vt.close()
#%%
#------Veri Süzme-------
# Bir veritabanından bütün verileri seçmek için aşağıdaki kodları kullanmıştık.
# SELECT * FROM tablo_adı
# Ancak amacımız bir tablo içindeki bütün verileri seçmek olmayabilir.
# Yalnızca belli ölçütlere uyan verileri seçmek isteyebiliriz.
# Verileri süzme isini WHERE adlı bir SQL komutu yardımıyla gerçeklestiririz.
# SELECT * FROM tablo_adı WHERE sütun_başlığı = aranan_veri
# Gördügünüz gibi, bu sorguyu gerçeklestirebilmek için tablodaki sütun
# baslıklarını bilmemiz gerekiyor. Tablo isimlerini soyle alıyorduk:
# SELECT name FROM sqlite_master
# Adını ögrendigimiz tablodaki sütun baslıklarını elde etmek için de:
import sqlite3
vt=sqlite3.connect("calisan_db.sqlite")
im=vt.cursor()
im.execute("SELECT name FROM sqlite_master")
im.fetchall()
im.execute("SELECT sql FROM sqlite_master")
im.fetchall()
# ‘sqlite_master’ adlı tablonun ‘sql’ niteligini sorguladıgımızda, ilgili
# tabloyu olusturmak için kullanılan SQL komutunu görüyoruz. Bu komuttan sutun
# baslıklarını görebiliriz. Yine bunun için SQLite Browser da kullanılabilir.
# Şimdi, bize gereken bilgileri aldıktan sonra sorgulama yapalım.
im.execute("SELECT * FROM calisan_tablosu WHERE adı = 'Uğur'")
im.fetchall()
vt.close()


























