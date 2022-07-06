# -*- coding: utf-8 -*-
#%%
class Personel(): #sınıf tanımlaması
    personel=[] # sınıf niteliği
    def __init__(self,isim): # başlangıç örnek metodu
        self.isim=isim #örnek niteliği
        self.birimi="" #örnek niteliği
        self.ekle()
    def ekle(self): #örnek metodu
        self.personel.append(self.isim)
    def listele(self): #örnek metodu
        for i in self.personel:
            print(i)

personel1=Personel("Ali")
personel2=Personel("Ahmet")
personel1.listele()
personel2.listele()
Personel("Ugur").listele()
Personel.listele() #çalışmıyor


#%%
class Personel(): #sınıf tanımlaması
    personel=[] # sınıf niteliği
    def __init__(self,isim): # başlangıç örnek metodu
        self.isim=isim #örnek niteliği
        self.birimi="" #örnek niteliği
        self.ekle()
    def ekle(self): #örnek metodu
        self.personel.append(self.isim)
    @classmethod
    def listele(cls): #sınıf metodu
        for i in cls.personel:
            print(i)
        
personel1=Personel("Ali")
personel2=Personel("Ahmet")
personel1.listele()
personel2.listele()
Personel("Ugur").listele()
Personel.listele() #şimdi çalışıyor
#neden @classmethod
# 1- Tertip düzen
# 2- 42.satırı çalıştırma isteği
#%% @staticmethod
# sınıf veya örnek nitelikleri ile etkilesime
# girmeyen ve sınıf içinde olmasını istediğimiz metodlar
class Personel(): #sınıf tanımlaması
    personel=[] # sınıf niteliği
    def __init__(self,isim): # başlangıç örnek metodu
        self.isim=isim #örnek niteliği
        self.birimi="" #örnek niteliği
        self.ekle()
    def ekle(self): #örnek metodu
        self.personel.append(self.isim)
    @classmethod
    def listele(cls): #sınıf metodu
        for i in cls.personel:
            print(i)
    @staticmethod
    def pi_sayısı():
        return 22/7
    @staticmethod
    def zam_hesaplama(maas_gir):
        return 1.4*int(maas_gir)
    
pers1=Personel("Ali")
pers1.zam_hesaplama("10000")
pers1.pi_sayısı()
pers3=pers1
pers3.zam_hesaplama("20000")
pers3.listele()
pers3.isim
pers3.ekle()
pers4=pers3("Hakan")
dir(pers3)


#%% özet
class Sinif(object):
    sınıf_niteliği="Ben bir sınıf niteliğiyim"
    def __init__(self,param1,param2):#"Ben başlangıç örnek metodu"
        self.örnek_niteliği="Ben bir örnek niteliğiyim"
    def örnek_metodu(self):
        pass
    @classmethod
    def sınıf_metodu(cls):
        pass
    @staticmethod
    def statik_metodu():
        pass
#%%
class Hesaplama():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def topla(self):
        return self.a+self.b
#1- Fonksiyona arguman olmak
print(Hesaplama(2,3).topla())
#2- Fonksiyondan değer döndürmeli
def Fonksiyon():
    return Hesaplama(2,3).topla()
Fonksiyon()
#3-Değişkene atanma
değişken=Hesaplama(2,3).topla()
print(değişken)
#%% Üye türleri
class Otobus():
    yolcu_isim=[]
    yolcu_TC=[]
    def __init__(self,isim,TC):
        self.isim=isim
        self.TC=TC
        self.ekle()
    def ekle(self):
        self.yolcu_isim.append(self.isim)
        self.yolcu_TC.append(self.TC)
    @classmethod
    def listele(cls):
        for i in range(0,len(cls.yolcu_TC)):
            print(cls.yolcu_isim[i],cls.yolcu_TC[i])

#1-Aleni üyeler
dir(Otobus)
yolcu1=Otobus("Ali", "123456")
yolcu2=Otobus("Ahmet", "654321")
yolcu1.yolcu_TC
yolcu1.listele()
#%%2-Gizli üyeler
# __gizli
# __gizli_
class Otobus():
    __yolcu_isim=[]
    __yolcu_TC_=[]
    def __init__(self,isim,TC):
        self.__isim=isim
        self.__TC=TC
        self.__ekle()
    def __ekle(self):
        self.__yolcu_isim.append(self.__isim)
        self.__yolcu_TC_.append(self.__TC)
    @classmethod
    def __listele(cls):
        for i in range(0,len(cls.__yolcu_TC)):
            print(cls.__yolcu_isim[i],cls.__yolcu_TC_[i])
    @classmethod
    def yolcu_say(cls):
        print(len(cls.__yolcu_isim))



yolcu1=Otobus("Ali", "123456")
yolcu2=Otobus("Ahmet", "654321")
yolcu1.__yolcu_TC_
yolcu1.__listele()
yolcu1.yolcu_say()
yolcu1._Otobus__yolcu_TC_
#%% Yarı-gizli
# _yarıGizli
class Otobus():
    _yolcu_isim=[]
    _yolcu_TC=[]
    def __init__(self,isim,TC):
        self.isim=isim
        self.TC=TC
        self.ekle()
    def ekle(self):
        self._yolcu_isim.append(self.isim)
        self._yolcu_TC.append(self.TC)
    @classmethod
    def listele(cls):
        for i in range(0,len(cls._yolcu_TC)):
            print(cls._yolcu_isim[i],cls._yolcu_TC[i])

yolcu1=Otobus("Ali", "111111")
yolcu1._yolcu_TC
#%% @property
#salt okunur
class Otobus():
    yolcu_isim=[]
    yolcu_TC=[]
    def __init__(self,isim,TC):
        self.isim=isim
        self._TC=TC
        self.ekle()
    def ekle(self):
        self.yolcu_isim.append(self.isim)
        self.yolcu_TC.append(self._TC)
    @classmethod
    def listele(cls):
        for i in range(0,len(cls.yolcu_TC)):
            print(cls.yolcu_isim[i],cls.yolcu_TC[i])
    @property
    def TC(self):
        return self._TC
   
yolcu1=Otobus("Ali","1121212")
yolcu1._TC
yolcu1.TC
yolcu1.TC="121212121"
yolcu1._TC="45454545"
#%% değiştirme
class Otobus():
    yolcu_isim=[]
    yolcu_TC=[]
    def __init__(self,isim,TC):
        self.isim=isim
        self.TC=TC
        self.ekle()
    def ekle(self):
        self.yolcu_isim.append(self.isim)
        self.yolcu_TC.append(self.TC)
    @classmethod
    def listele(cls):
        for i in range(0,len(cls.yolcu_TC)):
            print(cls.yolcu_isim[i],cls.yolcu_TC[i])
    def TC_değiştir(self,yeni_TC):
        indeks=self.yolcu_TC.index(self.TC)
        self.yolcu_TC[indeks]=yeni_TC
        self.TC=yeni_TC
yolcu1=Otobus("Ali","1121212")
yolcu1.TC
yolcu1.TC_değiştir("00000000")
yolcu1.yolcu_TC
#%%
class Otobus():
    yolcu_isim=[]
    yolcu_TC=[]
    def __init__(self,isim,TC):
        self.isim=isim
        self._TC=TC
        self.ekle()
    def ekle(self):
        self.yolcu_isim.append(self.isim)
        self.yolcu_TC.append(self._TC)
    @classmethod
    def listele(cls):
        for i in range(0,len(cls.yolcu_TC)):
            print(cls.yolcu_isim[i],cls.yolcu_TC[i])
    @property
    def TC(self):
        return self._TC
    @TC.setter
    def TC(self,yeni_TC):
        indeks=self.yolcu_TC.index(self._TC)
        self.yolcu_TC[indeks]=yeni_TC
        self._TC=yeni_TC

yolcu1=Otobus("Ali","1121212")
yolcu1.TC
yolcu1.yolcu_TC
yolcu1.TC="00000000000111"
#%% yerine kullanma, güncelleme
class Hesaplama():
    def __init__(self,data):
        self._data=data
        self.yazdır()
    def yazdır(self):
        print(self._data)
    @property
    def veri(self):
        return self._data
    @veri.setter
    def veri(self,yeni):
        self._data=yeni
hesap1=Hesaplama(11)
hesap1.veri
hesap1.veri=144
#%% @deleter
class Otobus():
    yolcu_isim=[]
    yolcu_TC=[]
    def __init__(self,isim,TC):
        self._isim=isim
        self._TC=TC
        self.ekle()
    def ekle(self):
        self.yolcu_isim.append(self._isim)
        self.yolcu_TC.append(self._TC)
    @classmethod
    def listele(cls):
        for i in range(0,len(cls.yolcu_TC)):
            print(cls.yolcu_isim[i],cls.yolcu_TC[i])
    @property
    def TC(self):
        return self._TC
    @TC.setter
    def TC(self,yeni_TC):
        indeks=self.yolcu_TC.index(self._TC)
        self.yolcu_TC[indeks]=yeni_TC
        self._TC=yeni_TC
    @TC.deleter
    def TC(self):
        self.yolcu_TC.remove(self._TC)
        del self._TC
    @property
    def isim(self):
        return self._isim
    @isim.deleter
    def isim(self):
        self.yolcu_isim.remove(self._isim)
        del self._isim


yolcu1=Otobus("Ali","1121212")
yolcu2=Otobus("Ahmet","3232323")
yolcu1.TC
yolcu1.yolcu_TC
del yolcu1.TC
yolcu1.isim
yolcu1.yolcu_isim
del yolcu1.isim
