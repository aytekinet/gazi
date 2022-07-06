# -*- coding: utf-8 -*-
#listeler
#%%
#boş liste tanımlamaları
liste=[]
liste1=list()
#liste nedir?
liste=[12,5.5,45j,True,[1,2,3],"Ali","k"]
liste1=[45,78,96]
liste3=liste[0]+liste1[1]
liste3=liste[0:1]+liste1[1:2]
liste4=liste[5]+liste[6]
liste3

liste=[i for i in range(0,16)]
liste
len(liste)
liste[0:16:3]
liste[16:0:-3]

len(liste)
liste[0]
liste[-1]
liste[6]
liste[2:4] #2 ve 3'ü verir
liste[::] #hepsi
liste[::2] #2 step ile
liste[::-1] #ters sıralama
liste[-1:-1:-1] 
liste1=liste[0]+liste[2]
liste1
liste2=liste[4]
liste2[1]
liste[4][1]
liste=[[[1,2],3],[4,5,6],[7,8,9]]
liste[0][2]
liste[2][2]
liste[0][0][1]
x,y
x1-x2
x1,x2,x3
x(1,2,3)
#%%
# 'append'
liste=["muz","elma","kiraz"]
liste
eklenecek1="vişne"
eklenecek2="karpuz"
eklenecek3=[1,2,3,4,5,6,7,8,9,90]
eklenecek4=("kavun","karpuz")
liste.append(eklenecek3)
liste
liste[0]
liste[1]
liste[2]
liste[3]
liste[3]
liste[4]

liste=liste+[eklenecek4]
liste

eklenecek4
a1=[eklenecek4]
a1
a2=list(eklenecek4)
a2
liste=[1,2,35,6]+["ali","veli","ahmet"]
liste

il="ankara"
il=il.upper()
il
#%%
# 'extend'
liste1=[1,2,3]
liste2=[4,5,6]
liste1.extend(liste2)
liste1
liste2
liste1=liste1+liste2
liste1=liste2+liste1
liste2.extend(liste1)
meyve=["muz","kiraz"]
eklenecek=["armut","kayısı","erik"]
meyve.extend(eklenecek)
meyve
liste1.append(liste2)
liste1
#%%
# 'insert'
liste=["ankara","izmir"]
ekle="istanbul"
liste.insert(0,ekle)
liste
liste.insert(1,"bursa")
liste
ekle1=["adana","antalya"]
liste.insert(2,ekle1)
liste
sehir=["ankara","izmir"]
ekle=["adana","antalya"]
sehir=sehir[0:1]+ekle[:]+sehir[1:2]
sehir

sehir.insert(1,ekle)
sehir
#%%
#'clear', "pop", "remove", "del"
sehir=["ankara","izmir"]
sehir.clear()
sehir
sehir.pop(0)
sehir.remove("izmir")
sayılar=[1,2,35]
sayılar.remove(35)
sayılar

del sehir
del sehir[0]
sehir
#%% "copy"
liste1=[1,2,3]
liste2=liste1 #nesnenin kendisi kopyalanır
liste2.append(4)
liste2
liste1

liste1=[1,2,3,4,5,6,7,8,9]
liste2=liste1
liste2[2],liste2[5]=liste2[5],liste2[2]
liste2
liste1
#bu problemi aşmanın üç yolu
liste1=[1,2,3]
#değer kopyalanır
liste2=liste1.copy() # 1. yol
liste2=list(liste1) # 2. yol
liste2=liste1[:] # 3. yol
liste2
liste2.append(4)
liste2
liste1
#%%  'index',
liste=list("abcdefgheeeee")
liste
indeks=liste.index("e")
indeks
liste.pop(indeks)
liste
liste.remove("e")
liste
#%%  'count',
liste=list("abcdefgheeeee")
liste.count("e")
meyve=["muz","kiraz","armut","kayısı","erik"]
meyve.count("muz")
#%%  'reverse', 'sort'
liste=[4,8,1,87,9,44]
liste.sort()
liste.reverse()
liste
liste=["a","e","z","r","b"]
liste.sort()
liste
liste=["ç","ğ","ş","a","e","z","r","b"]
liste.reverse()
liste[::-1]
liste
liste.sort()
liste
liste=[[1,3,2],"b","a","c"]
liste[0].sort()
liste[1:].sort()
liste
#%% sorgulamalar
meyve=["muz","elma"]
if "kiraz" not in meyve:
    print("evet yok...")
else:
    print("hayır var...")
#%%
liste1=[1,2]
liste2=[2,4]
liste3=liste1+liste2
liste3
liste4=[liste1,liste2]
liste4
#%%
help(list.sort)
list.sort.__doc__

library list
sort()

library liste
sortt()

sayı=-8
sayı=abs(sayı)
sayı
help(abs)
abs.__doc__
import math
dir(math)


pow(2,3)
help(pow)
pow.__doc__

help(math.pow)
math.pow.__doc__
#%%
liste=[1,2,3,4,5]
liste
liste[0]=100
liste
liste[0]="ali"
liste
liste[0:3]=[450,550,650]
liste[0:5]=[450,550,650]
liste=[450,550,650]
liste
#%%
dizin="istanbul"
çıktı=dizin.split("a")
type(çıktı)
çıktı[0]
çıktı[1]
dizin="bembeyaz"
dizin.split("be")
dizin.rsplit("be")
dizin="izmir"
dizin.split("i")
dizin.rsplit("i")
#%%
"""
Harfler adıyla bir liste oluşturup 
içine ‘a’, ‘e’, ‘i’, ‘o’, ‘ı’, ‘u’ 
elemanları kaydediniz. 
Bu listede i ve p harflerinin 
sayısını ekrana yazdırınız.
"""
harfler=list("aeiioöuü")
harfler.count("i")
harfler.count("p")
#%%
"""Liste1, liste2, liste3 
ve liste4 adında dört adet 
liste oluşturup aynı satırda 
olacak şekilde tanımlayıp, 
her bir listeye birer adet 
eleman girip listeleyiniz.
"""
liste1=[]
liste2=[]
liste3=[]
liste4=[]
liste=[liste1,liste2,liste3,liste4]
liste
liste[0].append(1)
liste[0].append(2)
liste[1].append(3)
liste[2].append(4)
liste[2].append(5)
liste[3].append(6)
liste
#%%
liste1,liste2,liste3,liste4=[[1],[2],[3],[4]]
liste1
type(liste1)

#%%
liste = [1, 2, 3, 4, 5, 6, 7]
liste[1:3]+liste[5:6]
#%%
liste = ['bir','iki','dört']
print(liste)
liste.insert(2,"üç")
liste
liste.insert(4,"beş")
#%%
liste=["birinci veri", "ikinci veri", "üçüncü veri ", "dördüncü veri","beşinci veri"]
liste[0]
liste[-1]
len(liste)
liste[4]
liste[5]
liste[len(liste)-1]

dizin=liste[0]+"\n\n"+liste[-1]
print(dizin)
#%% bytes
sayı=63
bytes([97])

ord("a")
hex(97)
bin(97)
oct(97)

