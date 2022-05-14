# -*- coding: utf-8 -*-
"""
Created on Sat May 14 13:47:07 2022

@author: Gazi TF
"""

#%%Fonksiyonlar

dizin="abcdefg"


sayac = 0
for _ in dizin:
    sayac+=1
print(sayac)

#%%

#fonksiyon tanımlaması 

def uzunluk(dizin: str) -> int:
    '''
    fonsiyonun açıklama kısmdır.
    bu fonksiyon bir karakter dizisinin uzunluğunu verir.
    
    '''
    sayac = 0
    for _ in dizin:
        sayac = sayac+1
    print("sonuç: ",sayac)

#fonksiyon çağırma

uzunluk("abcdfg")
yeni_dizin = "aytek"
uzunluk(yeni_dizin)

#%%

liste = [5,4,7,9,1]
sum(liste)

def carpim(seri : "liste içerisinde int veya float")-> "int veya float":
    sonuc = 1
    for i in seri:
        sonuc = sonuc * i
    print(sonuc)
    
carpim(liste)


#/%%

def hipotenus(x,y):
    return ("Bir kenarı",x), ("Bir kenarı ",y), ("Hipotenüs", x**y)
print(hipotenus(3, 4))

#%%

def deger(x,y):
    sonuc = "ilk değer:" + str(x) + "___"+"ikinci değer:"+str(y)
    return sonuc

print(deger(1,2))
a=deger(7,9)
print(a)


#%%

def adı_soyadı(adı,soyadı):
    return adı,soyadı 

adım,soyadım= adı_soyadı("aytekin", "tanrısever")
print(adım.upper()+" "+soyadım.upper())

#%%

def sayılar(a,b):
    return a,b

aDegiskeni,bDegiskeni = sayılar(5, 4)

print (round(aDegiskeni**bDegiskeni / 11))


#%%

def alan_hesapla(r,pi=3.14):
    return pi*r**2
alan_hesapla(5)

#%%

#fonksiyon örneği

def topla(*args):
    toplama = 0
    for i in args:
        toplama = toplama + i
    return toplama

topla(2)
topla(3,2,1)
topla(5,8,7,9,6)

#%%

def kayıt(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
        
kayıt(adı="aytekin", soyadı="tanrısever", telefon="0545456456", meslek="dev")
kayıt(ogrenci_adı="ali", soyad="lorem")

#%%
def yazdir(*args,**kwargs):
    return print("#",*args,**kwargs)
    
yazdir("aytekin")
yazdir(*"aytekin")
yazdir(*"aytekin",sep=",")    

#%%
sayi = 5
carp = 1
for i in range(1,sayi+1):
    carp=carp*i
print(carp)


#%%
def faktoriyel(sayi):
    carpim=1
    for i in range(1,sayi+1):
        carpim*=i
    return carpim
faktoriyel(5)

#%%

def faktoriyel(sayi):
    if sayi == 1:
        return 1
    else:
        return sayi*faktoriyel(sayi-1)
faktoriyel(5)

#%%

def toplama(sayi):
    if sayi == 0:
        return 0
    else:
        return sayi+toplama(sayi-1)

toplama(5)

#%%

liste = []
def kayit(adi,soyadi):
    liste.append([adi,soyadi])

kayit("lorem","loremm")
print(liste)
kayit(input("adınız: "), input("sayadınız: ") )


#%%

hipotenus = lambda x,y:(x**2+y**2)**(1/2)

hipotenus(3, 4)

#%%

def hipotenus(x,y):
    return (x**2+y**2)**(1/2)

#%%

#filter örnekte sadece 5'ten büyük sayıları listeler

liste = [5,7,8,3,2,7,9,0]

def küçük(sayı):
    return sayı > 5
küçük(30)
sonuc=filter(küçük, liste)
print(*sonuc)

#%% map

#%%
#başka dosyadan hesapmakinesi.py'den sadece topla ve çıkar fonksiyonlarını import ettik
from hesapmakinesi import topla, çıkar

print(topla(5,6))
print(çıkar(10,5))


#başka dosyadan hesapmakinesi.py'den tüm fonksiyonları import ettik

from hesapmakinesi import *

print(böl(10,2))
print(çarp(10,5))


#%%

#eval() #tek satırlık işlemler için uyhun
#exec() $çok satırlık işlemler için uygun 
#iki fonksiyonda string olarak çalışıyor.

işlem = "5+4-8/9*7"
print(işlem)

sonuc =eval(işlem)
print(sonuc)

#%% eval()

#burada kullanıcı input ile hesaplama yapabilir. 9+7+10/2*6 gibi 
hesap=input("İşleminiz: ")
print(eval(hesap))

#%% exec() ***
