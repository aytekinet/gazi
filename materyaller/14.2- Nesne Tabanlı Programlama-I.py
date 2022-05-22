# -*- coding: utf-8 -*-
#%%
# bu programlama dilinin bütün felsefesi, ‘bir kez yazılan kodların en verimli
# sekilde tekrar tekrar kullanılabilmesi’ fikrine dayanıyor.
# ------------Sınıflar------------
# Sınıflar, nesne üretmemizi saglayan veri tipleridir.
# Nesne tabanlı programlama ise nesneler (ve dolayısıyla sınıflar) temel
# alınarak gerçeklestirilen bir programlama faaliyetidir.
#%%
# ------------Sınıflar ne işe yarar?------------
# Sınıflar, öteki veri tipleri (list, tuple, str...) gibi verileri manipüle
# etmemizi saglayan bir veri tipidir.
# Şimdi, kullanıcının girdigi bir kelimedeki sesli harfleri sayan bir kod
# yazalım.
sesliler="aeıioöuü"
kelime="Nesne Tabanlı Programlama"
sayac=0
for i in kelime:
    if i in sesliler:
        sayac=sayac+1
print("{} ifadesinde {} adet sesli harf vardır.".format(kelime,sayac))
# Yukarıdaki kodlara yeni kodlar ekledikçe programımız karmasık hale gelecek,
# kodları anlamak zorlasacaktır. Kod yapısını biraz olsun rahatlatmak için
# bazı önlemler alabiliriz. Mesela kullanıcı tarafından girilen kelimedeki
# bir harfin sesli olup olmadıgını denetleyen kodları bir fonksiyon içine almak
# gibi.
kelime="Nesne Tabanlı Programlama"
def seslidir(harf):
    return harf in "aeıioöuü"
sayac=0
for i in kelime:
    if seslidir(i):
        sayac=sayac+1
print("{} ifadesinde {} adet sesli harf vardır.".format(kelime,sayac))
# Kodların daha anlaşılır olması için küçük parçalara bölelim.
kelime="Nesne Tabanlı Programlama"
def seslidir(harf):
    return harf in "aeıioöuü"
def sesliSay():
    sayac=0
    for i in kelime:
        if seslidir(i):
            sayac=sayac+1
    return sayac
def calistir():
    print("{} ifadesinde {} adet sesli harf vardır.".format(kelime,sesliSay()))
calistir()
# Bu sekilde hem hangi islevin nerede oldugunu bulmak kolaylastı,
# hem de kodların görünüsü daha anlasılır oldu.
# Şimdi bunu basit bir sınıf içinde ifade edelim.
class HarfSayacı():
    def __init__(self):
        self.kelime="Nesne Tabanlı Programlama"
        self.sayac=0
    def seslidir(self,harf):
        return harf in "aeıioöuü"
    def sesliSay(self):
        for i in self.kelime:
            if self.seslidir(i):
                self.sayac=self.sayac+1
        return self.sayac
    def calistir(self):
        print("{} ifadesinde {} adet sesli harf vardır.".format(self.kelime,self.sesliSay()))
saydır=HarfSayacı()
saydır.calistir()
#%%
#-------------Sınıf Tanımlamak--------------
# Aşağıdaki gibi iki şekilde sınıf tanımlanabilir. Bu sınıflar şu anda boş.
# İlk harf büyük olur (jargon). Devamı yine büyük harfle başlar.
class Calisan:
    pass
class Calisan():
    pass
class CalisanSinifi:
    pass
class CalisanSinifi():
    pass
#%%
#-------------Sınıf Nitelikleri--------------
# Yukarıda, bos bir sınıfı nasıl tanımlayacagımızı ögrendik.
# Elbette tanımladıgımız sınıflar hep bos kalmayacak.
# Bu sınıflara birtakım nitelikler ekleyerek bu sınıfları kullanıslı hale
# getirebiliriz.
class Calisan():
    kabiliyetleri=[]
    unvani="isci"
    print(kabiliyetleri)
    print(unvani)
# Burada unvanı ve kabiliyetleri adlı iki degisken tanımladık.
# Teknik dilde bu degiskenlere ‘sınıf niteligi’ (class attribute ) adı verilir.
# Sınıflar fonksiyonlara benzer ancak bazı farklar da vardır.
# Bir fonksiyonu tanımlarsınız ve sonra çağırdığınızda çalışır.
# Sınıflar ise tanımlamanızla birlikte çalışır.
# Aynı durum başka bir dosyadan sınıfın import edilmesinde de yaşanır.
def Calisan():
    kabiliyetleri=[]
    unvani="isci"
    print(kabiliyetleri)
    print(unvani)
Calisan()
# Bu nedenle sınıf niteliklerini kendimiz kontrol etmek istediğimizde, bunu
# sınıf dışında yaparız.
class Calisan():
    kabiliyetleri=[]
    unvani="isci"
print(Calisan.kabiliyetleri)
print(Calisan.unvani)
# Sınıf niteliklerine erişmek için dogrudan sınıfın adını parantezsiz
# bir sekilde kullanıyoruz.
# Şimdi Calisan sınıfına bir kaç nitelik daha ekleyelim.
class Calisan():
    kabiliyetleri=[]
    unvani="isci"
    maasi=3000
    memleketi=""
    dogum_tarihi=""
# Burada ‘Çalısan’ adlı bir grubun ortak niteliklerini belirledik.
# Elbette her çalısanın memleketi ve dogum tarihi farklı olacagı için
# sınıf içinde bu degiskenlere belli bir deger atamadık.
#%%
#--------------Sınıfların Örneklenmesi---------------------
# Tanımladığımız bu sınıfın bir ise yarayabilmesi için bu sınıfı temel alarak,
# bu sınıfta belirtilen nitelikleri tasıyan birden fazla sınıf üyesi meydana
# getirebilmemiz lazım. Bunun için sınıfı bir değişkene atarız.
# Buna örnekleme-örneklendirme (instantiation) denir.
class Calisan():
    kabiliyetleri=[]
    unvani="isci"
    maasi=3000
    memleketi=""
    dogum_tarihi=""
Ugur=Calisan()
# Python programlama dilinde bir fonksiyonu kullanıslı hale getirme islemine
# ‘çagırma’, bir sınıfı kullanıslı hale getirme islemine ise ‘örnekleme’ denir.
# Burada Ugur ait olduğu sınıfın bir ‘sureti’ veya ‘örnegi’dir (instance).
# yani Ugur Calisan() sınıfının bütün özelliklerini tasıyan bir üyesidir.
# Şimdi bir çalışan daha örnekleyelim.
Ahmet=Calisan()
# Şimdi de bu çalışana bir kabiliyet tanımlayalım.
Ahmet.kabiliyetleri.append("Python")
print(Ahmet.kabiliyetleri)
# Ahmet çalışanına kabiliyet olarak "Python" ekledik.
# Aynı değişiklik Ugur çalışanı için de oldu!
print(Ugur.kabiliyetleri)
# Sınıf niteliklerinin bir baska önemli özelligi,
# bu niteliklere atanan degerlerin ve sonradan yapılan degisikliklerin
# o sınıfın bütün örneklerini etkiliyor olmasıdır.
Ahmet.unvani="Mühendis"
print(Ahmet.unvani)
print(Ugur.unvani)
# Eger ilgili sınıf niteligi; karakter dizisi, demet ve sayı gibi
# degistirilemeyen (immutable) bir veri tipi ise bu sınıf niteligi üzerinde
# zaten degisiklik yapamazsınız. Yaptıgınız sey ancak ilgili sınıf
# niteligini yeniden tanımlamak olacaktır.
# Ancak eger sınıf niteligi, liste, sözlük ve küme gibi degistirilebilir
# (mutable) bir veri tipi ise bu nitelik üzerinde yapacagınız degisiklikler
# bütün sınıf örneklerine yansıyacaktır.
# Yazdıgınız program açısından bu özellik arzu ettiginiz bir sey olabilir
# veya olmayabilir.
#%%
#--------------Örnek Nitelikleri---------------------
# Peki o halde, degerinin her örnekte ortak degil de her örnege özgü olmasını
# istedigimiz nitelikleri nasıl tanımlayacagız?
# Elbette sınıf nitelikleri yerine örnek nitelikleri denen baska bir kavramdan
# yararlanarak...
# Python’da sınıf niteliklerini tanımlamak için yapmamız gereken tek sey,
# sınıf tanımının hemen altına bunları alelade birer degisken gibi yazmaktan
# ibarettir:
class Calisan():
    kabiliyetleri=[]
    unvani="isci"
    maasi=3000
    memleketi=""
    dogum_tarihi=""
# Örnek niteliklerini tanımlamak için ise iki yardımcı araca ihtiyacımız var:
# __init__() fonksiyonu ve self.
class Calisan():
    def __init__(self):
        self.kabiliyetleri=[]
        self.unvani="isci"
        self.maasi=3000
        self.memleketi=""
        self.dogum_tarihi=""
# __init__(self) fonksiyonun görevi, sınıfımızı örnekledigimiz sırada,
# yani mesela Ugur = Çalışan() gibi bir komut verdigimiz anda olusturulacak
# nitelikleri ve gerçeklestirilecek islemleri tanımlamaktır.Bu fonksiyonun
# ilk parametresi her zaman self olmak zorundadır.
# Sınıf niteliklerini anlatırken bunların önemli bir özelliginin,
# sınıfın çagrılmasına gerek olmadan çalısmaya baslaması oldugunu söylemistik:
class Merhaba():
    selam="Merhaba"
    print(selam)
# Bu kodları çalıstırdıgımız anda ekrana ‘merhaba’ çıktısı verilecektir.
# Örnek nitelikleri ise farklıdır:
class Calisan():
    def __init__(self):
        self.kabiliyetleri=[]
        print(self.kabiliyetleri)
# Bu kodları çalıstırdıgınızda herhangi bir çıktı almazsınız.
# Bu kodların çıktı verebilmesi için sınıfımızı mutlaka örneklememiz lazım:
Ugur=Calisan()
# Çünkü self.kabiliyetleri bir sınıf niteligi degil, bir örnek niteligidir.
# Örnek niteliklerine erisebilmek için de ilgili sınıfı mutlaka örneklememiz
# gerekir.
# Ayrıca sınıf niteliklerinin aksine, örnek niteliklerine sınıf adları
# üzerinden erisemeyiz. Yani self.kabiliyetleri adlı örnek niteligine erismeye
# yönelik söyle bir girisim bizi hüsrana ugratacaktır:
print(Calisan.kabiliyetleri)
# Bu örnek niteligine erismek için örneklendirme mekanizmasından yararlanmamız
# lazım:
print(Calisan().kabiliyetleri) #paranteze dikkat!
# Şimdi aşağıdaki sınıfı örneklendirelim ve Ugur ve Ahmet örneklerine atayalım.
class Calisan():
    def __init__(self):
        self.kabiliyetleri=[]
Ugur=Calisan()
Ahmet=Calisan()
Ugur.kabiliyetleri.append("mühendis")
print(Ahmet.kabiliyetleri)
# Gördüğünüz gibi Ugur çalışanındaki değişiklik Ahmet çalışanını etkilemedi.
# Burada, __init__() fonksiyonu çalısmaya baslar ve Ugur ve Ahmet örnekleri
# için, kabiliyetleri adlı bos birer örnek niteligi olusturur.
# self kelimesi ise Python programlama dili söz diziminin gerektirdigi bir ögedir.
# Burada bu kelime, Çalışan() adlı sınıfın örneklerini temsil ediyor.
# Yani Ugur ve Ahmet çalışanlarını ayrı ayrı temsil ediyor.
# Bu arada, örnek isimlerini (mesela ahmet) yalnızca örnek niteliklerine
# erismek için kullanmıyoruz. Bunları aynı zamanda sınıf niteliklerine erismek
# için de kullanabiliyoruz. Dolayısıyla eger yukarıdaki sınıf tanımı içinde,
# self.kabiliyetleri adlı örnek niteligi‘nin yanısıra personel adlı bir sınıf
# niteligi de bulunsaydı:
class Calisan():
    personel=[]
    def __init__(self):
        self.kabiliyetleri=[]
Ugur=Calisan()
Ugur.personel # bütün örnekler için aynı olur
Ugur.kabiliyetleri # her örnek için farklı olur
# Aynı adı taşıyan sınıf ve örnek niteliklerinde Python önceliği örnek
# niteliklerine verir.
class Calisan():
    kabiliyetleri=["Sınıf Niteliği"]
    def __init__(self):
        self.kabiliyetleri=["Örnek Niteliği"]
Ugur=Calisan()
Ugur.kabiliyetleri
# Peki sınıf niteliğine ulaşmak istersek:
Calisan.kabiliyetleri
# O halde; örnek niteliğine erişmek için örnek adlarını, sınıf niteliğine
# erişmek için sınıf adlarını kullanıyoruz.
# Kısacası; eger bir örnek niteligi tanımlıyorsak, bu niteligin basına bir self
# getirmemiz gerekir. Ayrıca bu self kelimesini de, örnek niteliginin
# bulundugu fonksiyonun parametre listesinde ilk sıraya yerlestirmis olmalıyız.
# self kelimesi ancak ve ancak, içinde geçtigi fonksiyonun parametre listesinde
# ilk sırada kullanıldıgında anlam kazanır.
# Bu noktada size çok önemli bir bilgi verelim: Python sınıflarında örnek
# niteliklerini temsil etmesi için kullanacagınız kelimenin self olması sart
# degildir. Bunun yerine istediginiz baska bir kelimeyi kullanabilirsiniz.
# Ancak, self kullanımı Python toplulugu içinde çok güçlü ve sıkı sıkıya
# yerlesmis bir gelenektir. Bu gelenegi kimse bozmaz. Siz de bozmayın.
class Calisan():
    def __init__(falanca):
        falanca.kabiliyetleri=[]
Ahmet=Calisan()
Ahmet.kabiliyetleri
# Python’da bu konuya iliskin kural sudur:
# Sınıf içindeki bir fonksiyonun ilk parametresi ne ise, o fonksiyon içindeki
# örnek niteliklerini temsil eden kelime de odur.
class XY():
    sinifNiteligi=[]
    def __init__(a,b,c):
        a.ornekNiteligi=[]
#%%
#--------------Örnek Metotları---------------------
# Örnek metotları, bir sınıfın örnekleri vasıtasıyla çagrılabilen fonksiyonlardır.
# Bu fonksiyonların ilk parametresi her zaman self kelimesidir.
# Ayrıca bu fonksiyonlara sınıf içinde atıfta bulunurken de yine self
# kelimesini kullanıyoruz.
class Calisan():
    personel=[]
    def __init__(self,isim):
        self.isim=isim
        self.kabiliyetleri=[]
        self.personel_ekle() # Örnek metoduna atıf
    def personel_ekle(self): # Örnek metodu
        self.personel.append(self.isim)
    def personel_goruntule(self): # Örnek metodu
        print(self.personel)
    def kabiliyet_ekle(self, kabiliyet): # Örnek metodu
        self.kabiliyetleri.append(kabiliyet)
    def kabiliyet_goruntule(self): # Örnek metodu
        print(self.kabiliyetleri)
calisan1=Calisan("Ugur")
calisan2=Calisan("Ahmet")
calisan1.personel[0]="Mehmet"
calisan1.personel_goruntule() # Sınıf niteliği
calisan2.personel_goruntule() # Sınıf niteliği
calisan1.kabiliyet_ekle("Python")
calisan1.kabiliyet_goruntule()
#%%
#----------------Sınıf Metotları-------------------
# Bu bölüme kadar öprendiklerimiz:
# 1. Sınıflar (classes )
# 2. Sınıf nitelikleri (class attributes )
# 3. Örnekler (instances)
# 4. Örnek nitelikleri (instance attributes )
# 5. Örnek metotları (instance methods)
# Yukarıdaki Calisan() sınıfında bir personel listesi olusturmamızı,
# personele ekleme yapmamızı, personeli görüntülememizi, personele yeni
# kabiliyet eklememizi ve ekledigimiz kabiliyetleri görüntüleyebilmemizi
# saglayan örnek metotları var. Gelin bu kodlara bir de personel sayısını
# görüntülememizi saglayacak bir baska örnek metodu daha ekleyelim:
class Calisan():
    personel=[]
    def __init__(self,isim):
        self.isim=isim
        self.kabiliyetleri=[]
        self.personel_ekle() # Örnek metoduna atıf
    def personel_ekle(self): # Örnek metodu
        self.personel.append(self.isim)
    def personel_goruntule(self): # Örnek metodu
        print(self.personel)
    def kabiliyet_ekle(self, kabiliyet): # Örnek metodu
        self.kabiliyetleri.append(kabiliyet)
    def kabiliyet_goruntule(self): # Örnek metodu
        print(self.kabiliyetleri)
    def personel_say(self):
        print(len(self.personel))
ç1=Calisan("Ugur")
ç2=Calisan("Ahmet")
ç3=Calisan("Mehmet")
ç1.personel_say()
# Burada yeni olarak personel_say() adlı bir örnek metodu tanımladık. Bu metot,
# bir sınıf niteligi olan personel‘e eriserek bunun uzunlugunu ekrana basıyor.
# Böylece personelin kaç kisiden olustugunu ögrenmis oluyoruz.
# Ancak kodların çalısma mantıgı açısından burada bir tutarsızlıktan söz
# edebiliriz. Bütün personele dair bilgi veren bir fonksiyona örnek
# degiskenleri üzerinden erismek biraz tuhaf. Neticede bu fonksiyon, sınıfın
# herhangi bir örnegi ile dogrudan iliskili degil.Yani bu fonksiyon tek tek
# sınıf örneklerini degil, genel olarak sınıfın bütününü ilgilendiriyor.
# Bu bakımdan, personel_say() fonksiyonunun örnek degiskenlerinden bagımsız
# bir biçimde kullanılabilmesi çok daha mantıklı olacaktır.
# Ayrıca, personel_say() fonksiyonunu örneklerden bagımsız olarak
# kullanamadıgımız için, bu metot yardımıyla personel sayısının 0 oldugu bir
# durumu görüntülememiz de mümkün olmuyor. Çünkü bu fonksiyona erisebilmek için
# öncelikle sınıfı en az bir kez örneklemis olmamız gerekiyor.
# Burada personel_say() fonksiyonu ile bir sınıf niteliğine ulaşmaya çalışıyoruz.
# Ama personel_say()'ı bir örnek metodu olarak tanımladık. O yüzden bu fonksiyonu
# bir sınıf metodu olarak tanımlamamız gerekiyor.
# Her ne kadar Python’da sınıf niteliklerine hem örnekler hem de dogrudan sınıf
# adları üzerinden erisebilsek de örnek niteliklerine ve örnek metotlarına
# yalnızca örnekler üzerinden erisebiliriz. Bir metoda, sınıf adı ile
# erisebilmek için, ilgili metodu bir sınıf metodu olarak tanımlamıs olmalıyız.
#------------------@classmethod Bezeyicisi ve cls------------------
# Örnek metotlarını olusturmak için self adlı bir kelimeden yararlanıyorduk.
# Sınıf metotlarını oluşturmak için ise cls adlı bir kelimeyi kullanırız.
# Ama tek başınsa yeterli değildir, @classmethod ifadesi de kullanılır.
# Python’da isminin önünde @ isareti olan bu tür ögelere ‘bezeyici’ (decorator)
# adı verilir. @classmethod bezeyicisi, bir fonksiyonu sınıf metoduna
# dönüstürme islevi görüyor.
class Calisan():
    personel=[]
    def __init__(self,isim):
        self.isim=isim
        self.kabiliyetleri=[]
        self.personel_ekle() # Örnek metoduna atıf
    def personel_ekle(self): # Örnek metodu
        self.personel.append(self.isim)
    def personel_goruntule(self): # Örnek metodu
        print(self.personel)
    def kabiliyet_ekle(self, kabiliyet): # Örnek metodu
        self.kabiliyetleri.append(kabiliyet)
    def kabiliyet_goruntule(self): # Örnek metodu
        print(self.kabiliyetleri)
    @classmethod
    def personel_say(cls):
        print(len(cls.personel))

Calisan.personel_say() #parantez yok dikkat! parantez örnek niteliklerinde var.
# Gördüğünüz gibi sınıfı örneklemeden personel sayısını öğrenebildik.
#----------------------Statik Metotlar----------------------
# Python’da örnek metotları ve sınıf metotları dısında bir de statik metotlar
# bulunur. Bildiginiz gibi, örnek nitelikleri üzerinde islem yapacagımız zaman
# örnek metotlarını kullanıyoruz. Aynı sekilde sınıf nitelikleri üzerinde islem
# yapacagımız zaman ise sınıf metotlarından faydalanıyoruz. Örnek metotları
# içinde herhangi bir örnek niteligine erismek istedigimizde self kelimesini
# kullanıyoruz. Sınıf metotları içinde bir sınıf niteligine erismek için ise
# cls kelimesini kullanıyoruz. Iste eger bir sınıf içindeki herhangi bir
# fonksiyonda örnek veya sınıf niteliklerinin hiçbirine erismeniz gerekmiyorsa,
# statik metotları kullanabilirsiniz.
#--------------@staticmethod Bezeyicisi----------------
# Statik metotları tanımlamak için @staticmethod bezeyicisini kullanıyoruz.
# Statik metotlar, ilk parametre olarak self veya cls benzeri kelimeler almaz.
# Çünkü bu tür sınıfların örnek veya sınıf nitelikleri ile herhangi bir isi yoktur.
class BirSınıf():
    sınıfNiteliği=0
    def __init__(self):
        self.örnekNiteliği=0
    def örnek_metodu(self):
        self.örnekNiteliği=self.örnekNiteliği+1
        return self.örnekNiteliği
    @classmethod
    def sınıf_metodu(cls):
        cls.sınıfNiteliği=cls.sınıfNiteliği+100
        return cls.sınıfNiteliği
    @staticmethod
    def statik_metodu():
        print("statik metodu")
# Peki statik metotlar ne ise yarar?
# Bu metotlar sınıf metotlarına çok benzer. Tıpkı sınıf metotlarında oldugu
# gibi, anlamsal olarak sınıfla ilgili olan, ancak sınıf metotlarının aksine
# bu sınıfın herhangi bir niteligine erismesine gerek olmayan fonksiyonları,
# sınıf dısına atmak yerine, birer statik metot olarak sınıf içine yerlestirebiliriz.
class Mat():
    @staticmethod
    def pi():
        return 22/7
    @staticmethod
    def karekök(sayı):
        return sayı ** 0.5
# Statik metotları hem örnekler hem de sınıf adları üzerinden kullanabiliriz.
örnek1=Mat()
örnek1.pi() #örnek üzerinden kullanma
Mat.pi() #sınıf üzerinden kullanma
# Statik metotların özellikle sınıf adları üzerinden kullanılabilmesi,
# bu tür metotları epey kullanıslı hale getirir.
class Mat():
    cıkarma=0
    def __init__(self,sayı):
        self.sayı=sayı
        self.toplama=0
    def topla(self):
        self.toplama=self.toplama+Mat.pi()*self.sayı
        return self.toplama
    @classmethod
    def cıkar(cls): # Örnek olsun diye verilmiştir, burası bir örnek metodudur.
        cls.cıkarma=cls.cıkarma-Mat.pi()
        return cls.cıkarma
    @staticmethod
    def pi():
        return 22/7
    @staticmethod
    def karekök(sayı):
        return sayı ** 0.5
toplayalım=Mat(9)
toplayalım.topla() # örnek metodu üzerinden statik metodu kullanma
Mat.cıkar() # sınıf metodu üzerinden statik metodu kullanma












