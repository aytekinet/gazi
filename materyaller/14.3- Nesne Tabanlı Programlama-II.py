# -*- coding: utf-8 -*-

# if, def, and, or gibi deyim ve isleçler hariç Python’da her sey bir nesnedir.
class Sınıf():
    pass
dir(Sınıf)
obj=Sınıf()
dir(obj)
#%%
class Sınıf():
    sınıfNiteliği=[]
    def __init__(self):
        self.örnekNiteliği=[]
    def örnek_metodu(self):
        self.örnekNiteliği.append("Örnek Niteliği")
    @classmethod
    def sınıf_metodu(cls):
        cls.sınıfNiteliği.append("Sınıf Niteliği")
    @staticmethod
    def statik_metod():
        print("Statik Metod")
dir(Sınıf())
dir(list)
dizin="kelime"
dir(dizin)
#%%
# ---------------------Birinci sınıf öğeler--------------------------
# Python’da nesneler birinci sınıf ögeler’dir.
# 1. Baska bir fonksiyona veya sınıfa parametre olarak atanabilirler.
# 2. Bir fonksiyondan döndürülebilirler.
# 3. Bir degiskene atanabilirler.
class BirinciSınıf():
    def __init__(self):
        self.değer=0
    def metod(self):
        self.metod_değeri=1
# print() fonksiyonuna parametre oluyor
print(BirinciSınıf())
# bir fonsiyondan dönüyor
def fonk():
    return BirinciSınıf()
fonk()
# bir değişkene atanabiliyor
obj=BirinciSınıf()
obj.değer # örnek değerine ulaşmak için önce sınıf örneklendirilmelidir.
obj.metod() # örnek metoduna ulaşmak için önce sınıf örneklendirilmelidir.
obj.metod_değeri # örnek metodu altındaki metod_değerine ulaşmak için önce
                 # örnek metodu çalıştırılmalıdır.
#%%
# ------------------Sınıf Üyeleri------------------------------
# Python’da bir sınıf içinde bulunan nitelikler, degiskenler, metotlar,
# fonksiyonlar ve buna benzer baska veri tipleri, o sınıfın üyelerini meydana
# getirir. Bir sınıfın üyelerini genel olarak üçe ayırarak inceleyebiliriz:
#   1. Aleni üyeler (public members)
#   2. Gizli üyeler (private members)
#   3. Yarı-gizli üyeler (semi-private members).
# Aşağıdaki gibi kodlarımızı yazalım şimdi:
class Sınıf():
    sınıfNiteliği=[]
    def __init__(self,parametre):
        self.parametre=parametre
        self.örnekNiteliği=[]
    def örnek_metodu(self):
        self.örnekNiteliği.append("Örnek Niteliği")
        self.örnek_metodu_değeri=1
    @classmethod
    def sınıf_metodu(cls):
        cls.sınıfNiteliği.append("Sınıf Niteliği")
        cls.sınıf_metodu_değeri=2
    @staticmethod
    def statik_metod():
        print("Statik Metod")
        statik_metodu_değeri=3
# 1. Aleni üyeler-------------------------
# Eger bir sınıf üyesi dısarıya açıksa, yani bu üyeye sınıf dısından normal
# yöntemlerle erisilebiliyorsa bu tür üyelere ‘aleni üyeler’ adı verilir.
dir(Sınıf()) # yazdığımızda veya
obj=Sınıf("argüman")
dir(obj) # yazdığımızda, bu komutun çıktısında görünen ve normal yollardan
# erisebildigimiz bütün bu ögeler birer aleni üyedir.
# 'parametre'
# 'statik_metod'
# 'sınıfNiteliği'
# 'sınıf_metodu'
# 'örnekNiteliği'
# 'örnek_metodu'
#%%
#2. Gizli Üyeler------------------------------
# Bazı durumlarda, yazdıgınız bir sınıftaki bütün sınıf üyelerinin dısarıya
# açık olmasını istemeyebilirsiniz.
# Eger kodlarınızda, sınıfın yalnızca iç isleyisini ilgilendiren, bu yüzden de
# dısarıdan erisilmesine gerek olmadıgını veya erisilirse problem çıkacagını
# düsündügünüz birtakım ögeler varsa bunları dısarıya kapatarak bir ‘gizli üye’
# haline getirmek isteyebilirsiniz.
# Gizli üyelere, normal yöntemleri kullanarak sınıf dısından erisemeyiz.
# Ama bu üyelere sınıf içinden rahatlıkla erisebiliriz.
class Sınıf():
    aleniÜye="Ben Aleni Üyeyim."
    __gizliÜye="Ben Gizli Üyeyim."
    __gizliÜye2_="Ben de Gizli Üyeyim."
    def örnek_metodu(self):
        print(self.aleniÜye)
        print(self.__gizliÜye) # Sınıf içinden gizli üyeye erişim
        print(self.__gizliÜye2_) # Sınıf içinden gizli üyeye erişim
# Burada __gizliÜye adlı bir gizli sınıf niteligi tanımladık.
# Bu degiskenin yalnızca bas tarafında iki adet alt çizgi olduguna dikkat edin.
# Iste Python’da bas tarafında yukarıdaki gibi iki adet alt çizgi olan,
# ancak uç tarafında alt çizgi bulunmayan veya yalnızca tek bir alt çizgi
# bulunan bütün ögeler birer gizli üyedir.
obj=Sınıf()
obj.aleniÜye
obj.__gizliÜye
obj.__gizliÜye2_
# Gizli üyeye sınıf içinden örnek metodu ile erişebiliriz. Böylece örnek
# metodunda tanımlanan faaliyetleri dahilinde gizli üyeye dışardan erişebiliriz.
obj.örnek_metodu()
# Peki ama niçin gizli üye tanımlarız?
# Otobüs firması örneğinde yolcu adlarını ve TCKN'larını burada tutmak
# isteyebiliriz.
# Bir gizli üye sınıf niteliği olduğu gibi örnek niteliği de olabilir. Aşağıda
# sınıf niteliği şeklinde.
class ABCOtobüs():
    __adı=[]
    __soyadı=[]
    __TCKN=[]
    def yolcu_kayıt(self,Adı,Soyadı,TCKimlik):
        self.__adı.append(Adı)
        self.__soyadı.append(Soyadı)
        self.__TCKN.append(TCKimlik)
    def yolcu_listele(self):
        for i in range(0,len(self.__adı)):
            yaz=self.__adı[i][0]+"*"*3+" "+self.__soyadı[i][0]+"*"*3+" "+self.__TCKN[i][0:2]+"*"*5
            print(yaz)
yolcu1=ABCOtobüs()
yolcu1.yolcu_kayıt("Uğur","Özcan","56782341234")
yolcu1.__adı
yolcu1.__soyadı
yolcu1.__TCKN
yolcu2=ABCOtobüs()
yolcu2.yolcu_kayıt("Ali","Can","34565623445")
yolcu2=ABCOtobüs()
yolcu2.yolcu_kayıt("Ahmet","Öz","89656789453")
yolcu1.yolcu_listele()
# Sınıf nitelikleri ve örnek nitelikleri gizli üye olabiliyorsa sınıf metotları
# ve örnek metotları da gizli üye olabilir.
class Calisan():
    personel_listesi=[]
    def __init__(self, AdSoyad):
        self.AdSoyad=AdSoyad
        self.personel_ekle()
    def personel_ekle(self):
        self.personel_listesi.append(self.AdSoyad)
    @classmethod
    def personel_listele(cls):
        print(cls.personel_listesi)
personel_1=Calisan("Ugur Ozcan") # personel eklendi problem yok.
personel_1.personel_listele()
personel_1.personel_ekle() # aynı personel bir daha eklendi, problem var.
personel_1.personel_listele()
# O halde personel_ekle() örnek metodunu dışarıya kapatmamız gerekiyor.
# Hatta personel_listesini de kapatalım.
class Calisan():
    __personel_listesi=[]
    def __init__(self, AdSoyad):
        self.AdSoyad=AdSoyad
        self.__personel_ekle()
    def __personel_ekle(self):
        self.__personel_listesi.append(self.AdSoyad)
    @classmethod
    def personel_listele(cls):
        for i in range(0,len(cls.__personel_listesi)):
            print(cls.__personel_listesi[i][0]+"*"*5)
personel_1=Calisan("Ugur Ozcan") # personel eklendi problem yok.
personel_1.personel_listele()
personel_1.personel_ekle() # aynı personel bir daha eklenemedi, problem yok.
personel_1.personel_listele()
# Yukarıdaki örnekler, bazı durumlarda veri gizlemenin epey isimize
# yarayabilecegini bariz bir biçimde gösteriyor.
# Ayrıca yukarıdaki örnekte hemen dikkatinizi çeken birşey daha olmalı.
personel_1.AdSoyad
# Gördüğünüz gibi AdSoyad verisine ulaştık, hani gizliydi!
# Örnek nitelikleri de gizli üye yapılabilir.
# Şimdi bunları da dışarıya kapatalım.
class Calisan():
    __personel_listesi=[]
    def __init__(self, AdSoyad):
        self.__AdSoyad=AdSoyad # Örnek niteliği gizli üye oldu.
        self.__personel_ekle()
    def __personel_ekle(self):
        self.__personel_listesi.append(self.__AdSoyad) #Burayı da değiştirdik.
    @classmethod
    def personel_listele(cls):
        for i in range(0,len(cls.__personel_listesi)):
            print(cls.__personel_listesi[i][0]+"*"*5)
personel_1=Calisan("Ugur Ozcan")
personel_1.personel_listele()
personel_1.__AdSoyad # Artık örnek niteliğine erişemiyoruz.
dir(personel_1) # Gizli üyeler listelenmiyor.
#%%
# Not: İsim Bulandırma---------------------
# Python’da ‘gizli’ olarak adlandırdıgımız ögeler aslında o kadar da gizli degildir.
# Python, kodlar içinde gizli bir üye ile karsılastıgında özel bir
# ‘isim bulandırma’ (name mangling) islemi gerçeklestirir ve ilgili gizli
# üyenin görünüsünü degistirir.
# Python, siz bir sınıf üyesini gizli üye seklinde tanımladıgınızda,
# bu öge üzerinde su islemleri gerçeklestirir:
#-Öncelikle degiskenin bas tarafına bir alt çizgi ekler: _
#-Daha sonra, bu alt çizginin sag tarafına bu gizli üyeyi barındıran sınıfın
# adını ilistirir: _SınıfAdı
#-Son olarak da gizli üyeyi sınıf adının sag tarafına yapıstırır:
# _SınıfAdı__gizliÜye
personel_1._Calisan__AdSoyad
personel_1._Calisan__personel_listesi
personel_1._Calisan__personel_ekle()
personel_1.personel_listele()
# Gördüğünüz gibi hepsine erişebildik.
# Yalnız buraya söyle bir not düselim: Her ne kadar Python bize gizli üyelere
# erisme imkanı sunsa da, baskasının yazdıgı kodları kullanırken, o kodlardaki
# gizli üyelere erismeye çalısmamak çogu zaman iyi bir fikirdir. Nihayetinde
# eger bir programcı, bir sınıf üyesini gizlemisse bunun bir nedeni vardır.
# Python her ne kadar nitelikleri gizlememiz için bize özel bir mekanizma
# sunmus olsa da bu nitelige erismemizi tamamen engellemiyor, ancak ilgili
# sınıfı yazan kisinin niyetine saygı gösterecegimizi varsayıyor.
#%%
# 3.Yarı-gizli Üyeler
# Yarı-gizli üyeler, herhangi bir özel mekanizma aracılıgıyla degil de yalnızca
# Python topluluğu içi gelenekler tarafından korunan niteliklerdir.
# Herhangi bir üyeyi yarı-gizli olarak isaretlemek için yapmamız gereken tek
# sey, basına bir adet alt çizgi yerlestirmektir.
class Sınıf():
    _yarıgizliÜye="Ben Yarı-Gizli Üyeyim"
obj=Sınıf()
obj._yarıgizliÜye
dir(obj) # Yarı-gizli üyeler listelenir.
# Buradaki _yarıgizliÜye adlı nitelige sınıf içinden veya dısından erismemizi
# engelleyen veya zorlastıran hiçbir mekanizma bulunmaz.
# Ama biz bir sınıf içinde tek alt çizgi ile baslayan bir öge gördügümüzde,
# bunun sınıfın iç isleyisine iliskin bir ayrıntı oldugunu, sınıf dısından bu
# ögeyi degistirmeye kalkısmamamız gerektigini anlarız.
#%%
# -----------------@property Bezeyicisi----------------
# Aşağıdaki gibi bir kod yazalım.
class Calisan():
    personel_listesi=[]
    def __init__(self, AdıSoyadı):
        self.AdıSoyadı=AdıSoyadı
        self.personel_ekle()
    def personel_ekle(self):
        self.personel_listesi.append(self.AdıSoyadı)
    @classmethod
    def personel_listele(cls):
        for i in cls.personel_listesi:
            print(i)
pers_1=Calisan("Ugur Ozcan")
pers_2=Calisan("Ali Can")
pers_3=Calisan("Mehmet Oz")
pers_1.personel_listele()
pers_1.AdıSoyadı
pers_1.AdıSoyadı="Ahmet Canoz"
pers_1.AdıSoyadı
pers_1.personel_listele()
# Gördüğünüz gibi pers_1 adı soyadı değişti ancak personel_listesi değişmedi.
# Bunun için, yarı-gizli üye ile birlikte işlem yapacağız ve
# bezeyici tanımlamasında Türkçe karakterlere dikkat edeceğiz;
class Calisan():
    personel_listesi=[]
    def __init__(self, AdıSoyadı):
        self._AdıSoyadı=AdıSoyadı
        self.personel_ekle()
    def personel_ekle(self):
        self.personel_listesi.append(self._AdıSoyadı)
    @classmethod
    def personel_listele(cls):
        for i in cls.personel_listesi:
            print(i)
    @property
    def AdiSoyadi(self):
        return self._AdıSoyadı
    @AdiSoyadi.setter
    def AdiSoyadi(self,yeni_isim):
        indeks=self.personel_listesi.index(self.AdiSoyadi)
        self.personel_listesi[indeks]=yeni_isim
        self._AdıSoyadı=yeni_isim
pers_1=Calisan("Ugur Ozcan")
pers_2=Calisan("Ali Can")
pers_3=Calisan("Mehmet Oz")
pers_1.personel_listele()
pers_1.AdiSoyadi # Bir fonksiyonu nitelik gibi kullanıyoruz burada
pers_1.AdiSoyadi="Ahmet Canoz"
pers_1.AdiSoyadi
pers_1.personel_listele()
pers_2.AdiSoyadi
pers_2.AdiSoyadi="Kemal Candan"
pers_2.AdiSoyadi
pers_1.personel_listele()
# Gördügünüz gibi, öncelikle self.AdıSoyadı adlı niteligi, basına bir alt çizgi
# getirerek normal erisime kapatmak istedigimizi belirttik.
# Bu kodları görenler, sayı niteliginin yarı-gizli bir üye oldugunu anlayıp
# ona göre davranacak.
# Daha sonra da AdiSoyadi() fonksiyonumuzu tanımlıyoruz.
# Bu fonksiyonu @property ile bezedigimiz için, fonksiyon bir örnek nitelige
# dönüstü ve _AdıSoyadı degiskenini salt okunur hale getirdi.
# Eger amacınız degiskeni sadece salt okunur hale getirmek degilse @property
# ile bezedigimiz fonksiyon için bir .setter parametresi tanımlarız.
# Böylece _AdıSoyadı degiskenine AdiSoyadi adı ile normal bir sekilde erisip
# istedigimiz degisikligi yapabiliyoruz.
# Eğer bunları silmek istersek .deleter adlı özel bir @property bezeyicisi
# kullanırız;
class Calisan():
    personel_listesi=[]
    def __init__(self, AdıSoyadı):
        self._AdıSoyadı=AdıSoyadı
        self.personel_ekle()
    def personel_ekle(self):
        self.personel_listesi.append(self._AdıSoyadı)
    @classmethod
    def personel_listele(cls):
        for i in cls.personel_listesi:
            print(i)
    @property
    def AdiSoyadi(self):
        return self._AdıSoyadı
    @AdiSoyadi.setter
    def AdiSoyadi(self,yeni_isim):
        indeks=self.personel_listesi.index(self.AdiSoyadi)
        self.personel_listesi[indeks]=yeni_isim
        self._AdıSoyadı=yeni_isim
    @AdiSoyadi.deleter
    def AdiSoyadi(self):
        self.personel_listesi.remove(self.AdiSoyadi)
        del self._AdıSoyadı #Örnek niteliğini sildik
pers_1=Calisan("Ugur Ozcan")
pers_2=Calisan("Ali Can")
pers_3=Calisan("Mehmet Oz")
pers_1.personel_listele()
pers_1.AdiSoyadi
pers_1.AdiSoyadi="Ahmet Canoz"
pers_1.AdiSoyadi
pers_1.personel_listele()
del pers_1.AdiSoyadi # Artık silindi, en baştan tanımlama yapılması gerekir.
pers_1=Calisan("Ayşe Yenice")
pers_1.personel_listele()
# Gördügünüz gibi, @property bezeyicisini kullanırken üç ayrı metot
# tanımlıyoruz:
# a) Ilgili nitelige nasıl ulasacagımızı gösteren bir metot:
    # Bu metodu @property ile beziyoruz.
# b) Ilgili niteligi nasıl ayarlayacagımızı gösteren bir metot:
    # Bu metodu @metot_adı.setter seklinde beziyoruz.
# c) Ilgili niteligi nasıl silecegimizi gösteren bir metot:
    # Bu metodu @metot_adı.deleter seklinde beziyoruz.
#%% Özet
class Sinif(): #Ben Bir Sınıfım
    sinifNiteligi="Ben Sınıf Niteliğiyim."
    __sinNitGizliUye="Ben Sınıf Niteliği Gizli Üyesiyim."
    _sinNitYariGizliUye="Ben Sınıf Niteliği Yarı Gizli Üyesiyim"
    def __init__(self,params,__gizliParams,yariGizli): #Ben sınıf yüklendiğinde yapılacakları yaparım
        self.params=params #Ben örnek parametresiyim
        self.__gizliParams=__gizliParams #Ben gizli örnek parametresiyim
        self._yariGizli=yariGizli #Ben yarı gizli parametreyim, iptal edildim, değiştiriliyorum
        self.ornekNiteligi="Ben Örnek Niteliğiyim"
        self.baslangicOrnekMetodu() #Ben sınıf yüklendiğinde tanımlı işimi yaparım
    def baslangicOrnekMetodu(self):
        print("Sınıf yüklendiğinde yapılacaklar yapılır")
    def ornekMetodu(self,insparams):
        insparams="Ben örnek metodu parametresiyim, sadece burada çalışırım"
        print(self.ornekNiteligi)
        print("Ben Örnek Metoduyum sınıf ve örnek nitelikleri ile çalışırım")
    def __gizliOrnekMetodu(self):
        print("Ben Gizli Örnek Metodyum")
    @classmethod
    def sinifMetodu(cls):
        print(cls.sınıfNiteliği)
        print("Ben sınıf metoduyum, sınıf nitelikleriyle çalışırım")
    @staticmethod
    def statikMetodu():
        print("Ben Statik Metodum bir şeye karışmam, sabitleri filan tutarım")
    @property
    def yariGizli(self): #Ben örnek metodunu örnek niteliğine dönüştürürüm
        return self._yariGizli
    @yariGizli.setter #Ben örnek niteliğinin yeniden ayarlarım ve değiştiririm
    def yariGizli(self,yeni_deger):
        self._yariGizli=yeni_deger
    @yariGizli.deleter #Ben örnek niteliğini silerim
    def yariGizli(self):
        del self._yariGizli




































