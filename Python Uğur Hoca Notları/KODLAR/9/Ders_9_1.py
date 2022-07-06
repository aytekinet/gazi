# -*- coding: utf-8 -*-
#%%
class Kutuphane(): #üst, taban, ebeveyn sınıf
    butun_kitaplar=[]
    def __init__(self,adı,yazarı):
        self.adı=adı
        self.yazarı=yazarı
        self.butun_kitaplar.append([self.adı,self.yazarı])
    def listele(self):
        for i in self.butun_kitaplar:
            print(i)

#%%
class Kutuphane_Solon(Kutuphane):
    pass
class Kutuphane_Oda(Kutuphane):
    pass

ks1=Kutuphane_Solon("1984", "George Orwell")
ks2=Kutuphane_Solon("Hayvan Çiftliği", "George Orwell")    

ko1=Kutuphane_Oda("Cehennem", "Dan Brown")
ko2=Kutuphane_Oda("Dijital Kale", "Dan Brown")
ko3=Kutuphane_Oda("Melekler ve Şeytanlar", "Dan Brown")


ks2.butun_kitaplar        
#%%
class Ders():
    def __init__(self):
        self.sınıf_listesi=[]
    def ekle(self,adı,notu):
        self.adı=adı
        self.notu=notu
        self.sınıf_listesi.append([self.adı,self.notu])
    def listele(self):
        for i in self.sınıf_listesi:
            print(i)
#bütünüyle miras alma
class Fizik(Ders):
    pass
class Kimya(Ders):
    pass
#%% ekleme ile miras alma, değişiklik de var
class Ders():
    def __init__(self):
        self.sınıf_listesi=[]
    def ekle(self,adı,notu):
        self.adı=adı
        self.notu=notu
        self.sınıf_listesi.append([self.adı,self.notu])
    def listele(self):
        for i in self.sınıf_listesi:
            print(i)

class Fizik(Ders):
    import statistics
    def __init__(self):
        super().__init__()
        self.memleketi=[]
    def ortalama(self): #örnek metodu ekledik
        notlar=[int(self.sınıf_listesi[i][1]) 
                for i in range(0,len(self.sınıf_listesi))]
        print(self.statistics.mean(notlar))
    def ekle(self): #taban sınıfın aynı isimli metodu iptal olur
        self.adı=input("adı: ")
        self.soyadı=input("Soyadı: ")
        self.notu=input("Notu: ")
        self.sınıf_listesi.append([self.adı,self.soyadı,self.notu])



class Kimya(Ders):
    def sınıf_birincisi(self):
        sözlük={self.sınıf_listesi[i][0]:
                int(self.sınıf_listesi[i][1])
                for i in range(0,len(self.sınıf_listesi))}
        birinci=max(sözlük.values())
        birinciler=""
        for i,j in sözlük.items():
            if j==birinci:
                birinciler+=i+","
        print(birinciler)


fizik1=Fizik()
fizik1.ekle()
fizik1.ekle("ayşe","1")
fizik1.listele()
fizik1.ortalama()
kimya1=Kimya()
kimya1.ekle("ahmet","87")
kimya1.ekle("ali","75")
kimya1.ekle("ayşe","87")
kimya1.ekle("aysun","77")
kimya1.sınıf_birincisi()
#%%
class Yazılımcı(): #taban sınıf
    bütün_yazılımcılar=[]    
    def __init__(self,adı,soyadı,dil,tecrübe):
        self.adı=adı
        self.soyadı=soyadı
        self.dil=dil
        self.tecrübe=tecrübe
        self.yazılımcı=[]
        self.ekle()
    def ekle(self):
        self.yazılımcı.append([self.adı,self.soyadı,self.dil,self.tecrübe])
        self.bütün_yazılımcılar.append([self.adı,self.soyadı,self.dil,self.tecrübe])
    def listele(self):
        for i in self.yazılımcı:
            print(i)
    @classmethod
    def bütün_listele(cls):
        for i in cls.bütün_yazılımcılar:
            print(i)
    @staticmethod
    def sabit_katsayı():
        return 1.5
    

class Python(Yazılımcı):
    __TC_list_=[]
    def __init__(self,adı,soyadı,dil,tecrübe,TC):
        dil="Python"        
        super().__init__(adı,soyadı,dil,tecrübe)
        self.TC=TC
        self.__TC_list_.append(self.TC)



p1=Python("ali","can","dshfkjhdskjhfk","4","1212131")
p1.listele()
p1.dil
p1.bütün_listele()
p1.__TC_list_
#%%
class Topla():
    def __init__(self,a,b):
        print(a+b)
class Toplamak():
    def __init__(self,a,b):
        print(a**2+b**2)

class Hesap(Toplamak,Topla):
    def __init__(self,*args):
        Topla.__init__(self,*args)
örnek=Hesap(2,3)

#%%
class HesapMakinesi():
    def topla(self,a,b):
        return a+b
    def çıkar(self,a,b):
        return a-b
    def çarp(self,a,b):
        return a*b

class Calculator():
    def topla(self,a,b):
        return a**2+b**3
    def çıkar(self,a,b):
        return a**5-b**2
    def çarp(self,a,b):
        return a*b/4

class HM(HesapMakinesi,Calculator):
    def topla(self,a,b):
        self.a=a 
        self.b=b
        print(Calculator().topla(self.a,self.b))
    def çıkar(self,a,b):
        self.a=a
        self.b=b
        print(HesapMakinesi().çıkar(self.a,self.b))
    def çarp(self,a,b):
        return a/b

hesap1=HM()
hesap1.topla(2,3)
hesap1.çıkar(2,3)
hesap1.çarp(2,3)


























