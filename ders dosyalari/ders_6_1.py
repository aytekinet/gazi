# -*- coding: utf-8 -*-
#%% Fonksiyonlar
dizin="abcdefg"
len(dizin)

sayac=0
for _ in dizin:
    sayac+=1
print(sayac)
#%%
# fonksiyonun tanımlama aşaması
def uzunluk(dizin: str)-> int:
    '''
    Bu fonksiyon bir karakter dizisinin
    uzunluğunu verir. 
                     Beltek Kursları...
    '''
    sayac=0
    for _ in dizin:
        sayac=sayac+1
    print("Verilen ifadenin uzunluğu:",sayac)
#fonksiyonun çağrılma aşaması
uzunluk("abcdefgh")
yeni_dizin="uğur özcan"
uzunluk(yeni_dizin)
#%%
#değer döndermeyen fonksiyonlar
liste=[5,4,7,9,1]
def carpim(seri: "liste içinde int veya float")-> "int veya float":
    sonuc=1
    for i in seri:
        sonuc=sonuc*i
    print(sonuc)

print(carpim([6,7]))
sonuc=carpim([6,5])
print(sonuc**2)

#%%değer dönderen fonksiyonlar
def carpim(seri: "liste içinde int veya float")-> "int veya float":
    sonuc=1
    for i in seri:
        sonuc=sonuc*i
    return sonuc

print(carpim([5,4]))
sonuc=carpim([6,5])
print(sonuc**3)
#%%
def hipotenus(x,y):
    sonuc=(x**2+y**2)**(1/2)
    return sonuc
print(hipotenus(3, 4))
#%%
def hipotenus(x,y):
    return (x**2+y**2)**(1/2)
print(hipotenus(3, 4))
#%%
def hipotenus(x,y):
    return ("Bir kenarı", x), ("Diğer kenarı", y), ("Hipotenüsü",(x**2+y**2)**(1/2))
print(hipotenus(3, 4))
#%%
def split(seri,oran):
    uzunluk=len(seri[0])
    bölme_noktası=int(uzunluk*oran)
    X_train=seri[0][0:bölme_noktası]
    X_test=seri[0][bölme_noktası:]
    y_train=seri[1][0:bölme_noktası]
    y_test=seri[1][bölme_noktası:]
    return y_train,y_test,X_train,X_test

liste=[[1,2,3,4,5,6,7,8,9,10],[10,9,8,7,6,5,4,3,2,1]]
c,d,a,b=split(liste,0.7)
print(X_train)

def değer(x,y):
    sonuc="ilk değer "+str(x)+"ikinci değer "+str(y)
    return sonuc,"adana"
print(değer(1,2))
a=değer(1,2)
print(a)   
#%%
def adı_soyadı(adı,soyadı):
    return adı,soyadı

adı,soyadı=adı_soyadı("uğur", "özcan")
print(adım.upper()+" "+soyadım.upper())
#%%
listem=[]
def telefon_rehberi(adı,soyadı,telefon):
    listem.append([adı,soyadı,telefon])
print(listem)    

telefon_rehberi("ahmet", "öz", 3122027878)    
telefon_rehberi(telefon="03122025544",adı="ali",soyadı="can")    
#%% 
def alan_hesapla(r,pi=3.14):
    return pi*r**2
alan_hesapla(5)
alan_hesapla(5,3)
alan_hesapla(8)
#%%
def topla(*args):
    toplama=0
    for i in args:
        toplama=toplama+i
    return toplama
topla(2)
topla(3,2,5)
topla(5,4,7,8,9,6,6)
#%%
def kayıt(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
kayıt(adı="uğur",soyadı="özcan",telefonu="03122223344",adres="ankara",meslek="mühendis")
kayıt(öğrenci_adı="ali",soyadı="can",notu="100")
#%%
def yazdır(*args,**kwargs):
    return print("# ",*args,**kwargs)

yazdır("ugur")
yazdır(*"ugur")
yazdır(*"ugur",sep=",")
yazdır(*"özcan",sep=",")
#%%
sayı=5
carpım=1
for i in range(1,sayı+1):
    carpım=carpım*i
print(carpım)
#%%
def faktoriyel(sayı):
    carpım=1
    for i in range(1,sayı+1):
        carpım*=i
    return carpım
faktoriyel(5)
#%%
def faktoriyel(sayı):
    if sayı==1:
        return 1
    else:
        return sayı*faktoriyel(sayı-1)
faktoriyel(5)
#%%
x=6
y=9
def hipotenüs(x,y):
    return (x**2+y**2)**(1/2)

hipotenüs(x, y)

hipotenüs=lambda x,y:(x**2+y**2)**(1/2)
carpma= lambda x,y:x*y
print((lambda x: x**2) (25))



carpma(5,8)
hipotenüs(3, 4)
from functools import reduce
faktoriyel=reduce(lambda x,y:x*y, [1,2,3,4,5])
print(faktoriyel)

def sayı(sayı1,sayı2):
    return (sayı1+sayı2)
sonuc=reduce(sayı,[5,1,2,3])
print(sonuc)
#%%
liste=[5,4,7,8,9,8,7,4,3,2]
def küçük(sayı):
    return sayı>5
küçük(30)
sonuc=filter(küçük,liste)
print(*sonuc)
#%% map
def yazdır(isim):
    return "Sayın "+isim+" hoşgeldiniz\n"
yazdır("ugur")

liste=["ali","ayşe","veli"]
sonuc=map(yazdır,liste)
print(*sonuc,sep="")

#%%
def toplama(sayı):
    if sayı==0:
        return 0
    else:
        return sayı+toplama(sayı-1)
toplama(5)



#sayı=5
5+toplama(4)
#toplama(4)
5+4+toplama(3)
#toplama(3)
5+4+3+toplama(2)
...
5+4+3+2+1+toplama(0)
5+4+3+2+1+0
#%%
liste=[]
def kayıt(adı,soyadı):
    liste.append([adı,soyadı])

kayıt("ugur","özcan")
print(liste)
kayıt(input("adınız: "),input("soyadınız: "))
#%%
x=1 #global değişken
def hesapla(sayı):
    global x
    x=x+sayı #local değişken
    return x

print(x)
print(hesapla(16))
#%%
from hesap_makinesi import topla,çıkar
print(topla(5,6))
print(çıkar(8,4))

import hesap_makinesi
print(hesap_makinesi.böl(5,6))
print(hesap_makinesi.çarp(8,4))

from hesap_makinesi import *
print(böl(5,6))
print(çarp(8,4))

#%%
#eval()
#exec()

işlem="5+4-9/(9*1)"
print(işlem)
sonuc=eval(işlem)
print(sonuc)
#%%
hesap=input("İşleminiz: ")
print(eval(hesap))
eval()
#%%
hesaplama='''
giriş=int(input("Sayı: "))
topla=0
for i in range(0,giriş+1):
    topla+=i
print(topla)
'''
exec(hesaplama)

for i in range(10,-1,-2):
    print(i)

#%%
dizin="abcdefg"
uzunluk=len(dizin)
for i in range(0,uzunluk):
    print(i,dizin[i])

for i in dizin:
    print(i)
#%%
liste=[["a","b"],["c","d"]]
liste[-1][-1]
liste[1][1]

liste=[i for i in range(0,17)]
liste[16:0:-5]
#%%
liste=[i for i in range(0,16)]
liste
liste2=liste[4]
liste2























    