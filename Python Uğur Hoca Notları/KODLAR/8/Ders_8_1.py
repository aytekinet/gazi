# -*- coding: utf-8 -*-
#%% Nesne Tabanlı Programlama
#%%
sesli_harfler="aeıioöuü"
kelime=input("Bir kelime giriniz: ")
sayac=0
for i in kelime:
    if i in sesli_harfler:
        sayac=sayac+1
print()
print(f"{kelime} kelimesinde {sayac} tane sesli harf var...")
#%%
def giriş():
    kelime=input("Bir kelime giriniz: ")
    return kelime
def sesli(harf):
    sesli_harfler="aeıioöuü"
    return harf in sesli_harfler
def sesli_say(kelime):
    sayac=0
    for i in kelime:
        if sesli(i):
            sayac=sayac+1
    return sayac
def yazdır():
    kelime=giriş()
    print()
    print(f"{kelime} kelimesinde {sesli_say(kelime)} tane sesli harf var...")

if __name__=="__main__":
    yazdır()    
#%%
import deneme1    
dir(deneme1)    
deneme1.yazdır()    
import math
math.pi
from math import *
pow(2,3)
#%%
class Sesliler():
    def __init__(self):
        self.sesli_harfler="aeıioöuü"
        self.sayac=0
    def giriş(self):
        self.kelime=input("Bir kelime giriniz: ")
        return self.kelime
    def sesli(self,harf):
        return harf in self.sesli_harfler
    def sesli_say(self,kelime):
        for i in self.kelime:
            if self.sesli(i):
                self.sayac=self.sayac+1
        return self.sayac
    def yazdır(self):
        self.kelime=self.giriş()
        print()
        print(f"{self.kelime} kelimesinde {self.sesli_say(self.kelime)} tane sesli harf var...")
if __name__=="__main__":
    Sesliler().yazdır()
#%% Sınıflar
class Sınıf:
    pass
class Sınıf(): #en fazla kullanılan
    pass
class Sınıf(object):
    pass
#%%
class Sınıf():
    sınıf_liste=["Sınıf Niteliği"]
    sınıf_string="ankara"
    #print(sınıf_liste)
    #print(sınıf_string)
    
Sınıf.sınıf_liste    #sınıf niteliği çağırma
Sınıf.sınıf_string

def sınıf_fonk():
    fonk_liste=["Fonksiyon listesi"]
    fonk_string="Fonksiyon string"
    print(fonk_liste)
    print(fonk_string)
    
sınıf_fonk()
#%% Örneklendirme, instance
class Bitkiler():
    bitki_türü=[] #mutable (liste, sözlük, küme)
    bitki_adı="" #immutable (string, tupe, frozen sets, int, float, bool)
    bitki_rengi="" #immutable
    
elma=Bitkiler() #örneklendirme
kiraz=Bitkiler()
muz=Bitkiler()
patlıcan=Bitkiler()

elma.bitki_türü.append("Meyve")
elma.bitki_türü
elma.bitki_adı="ELMA"
elma.bitki_rengi="KIRMIZI"
elma.bitki_adı
elma.bitki_rengi
muz.bitki_adı="MUZ"
muz.bitki_rengi="SARI"
muz.bitki_türü
muz.bitki_rengi
kiraz.bitki_türü
kiraz.bitki_adı
kiraz.bitki_rengi
patlıcan.bitki_türü
#%%
class Rehber():
    adı_soyadı=""
    telefon=""

örnek1=Rehber()
örnek1.adı_soyadı="Uğur Özcan"
örnek1.telefon="03122023233"
örnek2=Rehber()
dir(örnek2)
örnek2.adı_soyadı="Ali Can"
örnek2.telefon="03122021122"

örnek2.adı_soyadı
örnek1.adı_soyadı
örnek2.telefon
örnek1.telefon
#%%
class Kutuphane():
    butun_kitaplarım=[]
    birinci_kitaplarım=tupple()
    ikinci_kitaplarım=tupple()


birinci=Kutuphane()
ikinci=Kutuphane()
#%%
class Personel(): #sınıf adı
    personel_listesi=[] #sınıf niteliği
    print("Tanımlama Aşamasında Çalışır")
    def __init__(self,adı_soyadı,maası,birimi): #başlangıç örnek metodu
        self.adı_soyadı=adı_soyadı #örnek niteliği
        self.maası=maası
        self.birimi=birimi
        self.yetenek=[]
        self.personel_listele()
    def personel_listele(self): #örnek metodu
        print("Örneklendirme aşamasında çalışır")    
    #for i in self.personel_listesi:
        #    print(i)
        
#%%
class Araçlarım():
    araç_listesi=[]
    def __init__(self):
        self.araç_türü:""
        self.araç_türü_listesi=[]

honda=Araçlarım()
honda.araç_listesi.append("Honda")
honda.araç_türü="Binek"
honda.araç_türü_listesi.append("CRV")
mazda=Araçlarım()
mazda.araç_türü="Station"
mazda.araç_türü_listesi.append("M")
mazda.araç_listesi

mazda.araç_türü_listesi
ford=Araçlarım()
ford.araç_listesi
ford.araç_türü_listesi
#%%
class Personel():
    personel_listesi=[]
    def __init__(self,adı_soyadı,görev,birim):
        self.adı_soyadı=adı_soyadı
        self.görev=görev
        self.birim=birim
        self.personel_ekle()
    def personel_ekle(self):
        self.personel_listesi.append(self.adı_soyadı)
    def personel_listele(self):
        for i in self.personel_listesi:
            print(i)
    
pers1=Personel("Ugur Özcan","Mühendis")
pers1.personel_listele()
pers2=Personel("Ali Can","İşçi")
pers3=Personel("Ahmet Çalışkan","Müdür")
pers4=Personel("Ayça Solmaz","Sekreter")
pers3.personel_listele()
pers3.görev
pers3.adı_soyadı
pers2.adı_soyadı
pers1.birim="Üretim"
pers2.birim
pers1.birim
pers2.birim="Dağıtım"
#%%
class HesapMakinası():
    def topla(self,a,b):
        return a+b
    def çıkar(self,a,b):
        return a-b
    def çarp(self,a,b):
        return a*b

hesap1=HesapMakinası()
print(hesap1.topla(3,5))
print(hesap1.çıkar(3,5))
print(HesapMakinası().topla(6,8))
#%%
class HesapMakinası():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def topla_üs(self,c):
        return (self.a+self.b)**c
    def çıkar(self):
        return self.a-self.b
    def çarp(self):
        return self.a*self.b

hesap2=HesapMakinası(3,5)
hesap2.topla_üs(2)
hesap2.çarp()
hesap2.çıkar()
#%%
class TelefonRehberi():
    rehber=[]
    def __init__(self,adı_soyadı,telefonu):
        self.adı_soyadı=adı_soyadı
        self.telefonu=telefonu
        self.rehber.append([self.adı_soyadı,self.telefonu])
    def rehber_listele(self):
        for i in self.rehber:
            print("Adı Soyadı:",i[0],"Telefonu:",i[1])
ekle=TelefonRehberi("Uğur Özcan","00000000")        
ekle.rehber_listele()        
TelefonRehberi("Ahmet Can","45454").rehber_listele()
#%% #Öğrenci ders bazında not ekleme
    #Öğrenci silme
    #Öğrenci ders bazında not güncelleme
    #öğrenci bazında not görüntüleme
    #öğrenci isimlerini toplu görüntüleme
    #ders bazında öğrenci ve notu görüntüleme
class Notlar():
    öğrenci_listesi=[]
    not_listesi=[]
    def __init__(self,adı,ders,notu):
        self.adı=adı
        self.ders=ders
        self.notu=notu
        self.öğrenci_ekle()
        self.ders_not_ekle()
    def öğrenci_ekle(self):
        self.öğrenci_listesi.append(self.adı)
    def ders_not_ekle(self):
        self.not_listesi.append([self.adı,self.ders,self.notu])
    def öğrenci_silme(self,öğrenci_sil):
        self.öğrenci_listesi.remove(öğrenci_sil)
        for i in range(0,len(self.not_listesi)):
            if öğrenci_sil==self.not_listesi[i][0]:
                self.not_listesi.pop(i)
    def öğrenci_not_güncelle(self,a_adı,a_ders,yeni_not):
        for i in range(0,len(self.not_listesi)):
            if a_adı==self.not_listesi[i][0] and a_ders==self.not_listesi[i][1]:
                self.not_listesi[i][2]=yeni_not
                break
    def öğrenci_not_listele(self,b_adı):
        for i in range(0,len(self.not_listesi)):
            if b_adı==self.not_listesi[i][0]:
                print(self.not_listesi[i][1],self.not_listesi[i][2])
    def öğrenci_listele(self):
        for i in self.öğrenci_listesi:
            print(i)
    def ders_not_listele(self,b_ders):
        for i in range(0,len(self.not_listesi)):
            if b_ders==self.not_listesi[i][1]:
                print(self.not_listesi[i][0],self.not_listesi[i][2])

örnek1=Notlar("ali","kimya","95")

örnek1.ders_not_listele("fizik")
örnek1.not_listesi
örnek1.öğrenci_not_güncelle("ugur", "fizik", "100")
#%%
#1-100 sayı tahmini oyunu
class SayıTahmin():
    def __init__(self):
        print("Oyuna Hoşgeldiniz...")
        self.tahminim=0 #örnek niteliği
    def rastgele(self): #örnek metodu
        import random
        self.sayı=random.randint(1,100)
    def tahmin(self):#örnek metodu
        tahmin=int(input("Sayı giriniz: "))
        return tahmin
    def kontrol(self,benim_tahminim):#örnek metodu
        if benim_tahminim>self.sayı:
            print("Aşağı")
        elif benim_tahminim<self.sayı:
            print("Yukarı")
        else:
            print("Tebrikler")
    def oyna(self):
        self.rastgele()
        while self.sayı!=self.tahminim:
            self.tahminim=self.tahmin()
            self.kontrol(self.tahminim)
        karar=input("Tekrar Oynamak İster misiniz?: E/h")
        if karar!="h":
            self.oyna()

oyun1=SayıTahmin()
oyun1.oyna()    
    
    
    
    
    
    





