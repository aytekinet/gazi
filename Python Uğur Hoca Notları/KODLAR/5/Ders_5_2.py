# -*- coding: utf-8 -*-
# Döngüler
#%% while
sayac=0
while sayac<6:
    print(sayac)
    sayac=sayac+1
print("Döngü sonlandı")

sayac1=0
while True:
    print(sayac1)
    sayac1=sayac1+1
    if sayac1>=6:
        break
#%%
sayac=1
while sayac<=100:
    if sayac%2==0:
        print(sayac,end=",")
    sayac=sayac+1
#%%
sayac=0
toplam=0
while sayac<100:
    sayac=sayac+1
    toplam=toplam+sayac
print(toplam)
#%%
alışveriş=[]
while True:
    sepet=input("ürün: ")
    if sepet=="q":
        break
    alışveriş.append(sepet)
print(alışveriş)
#%% Sayı Bulmaca
import random
sayı=random.randint(0, 100)
tahmin_sayısı=1
while True:
    tahmin=int(input("Tahmininiz: "))
    if tahmin>sayı:
        print("Daha küçük bir sayı söyle")
    elif tahmin<sayı:
        print("Daha büyük sayı söyle")
    else:
        print("Tebrikler...")
        print(tahmin_sayısı,"defa tahmin yaptınız")
        break
    tahmin_sayısı=tahmin_sayısı+1
#%%
import pyfiglet
a=pyfiglet.figlet_format("Merhaba")
print(a)
print(pyfiglet.FigletFont.getFonts())
#%%
sayı=int(input("Faktöriyeli alınacak sayı: "))
sayac=1
faktoriyel=1
while sayac<=sayı:
    faktoriyel=faktoriyel*sayac
    sayac=sayac+1
print(faktoriyel)
#%%
kelime="python programlama"
for i in kelime:
    print(i)   
#%%
kelime="python programlama"
sayac=0
while sayac<len(kelime): 
    print(kelime[sayac])
    sayac=sayac+1
    
#%%
liste=["elma","armut","muz"]
for i in liste:
    for j in i:
        print(j)
#%%
yazi='''Python üst düzey basit sözdizimine
 sahip, öğrenmesi oldukça kolay, 
 modülerliği, okunabilirliği destekleyen, 
 platform bağımsız nesne yönelimli 
 yorumlanabilir bir script dilidir.'''
harf="s"
#print(yazi.count(harf))
sayac=0
for i in yazi:
    if i==harf:
        sayac=sayac+1
print(harf,":",sayac)


yazı_liste=yazi
yazı_liste=yazı_liste.replace(".","")
yazı_liste=yazı_liste.replace(",","")
yazı_liste=yazı_liste.replace("\n","")
yazı_liste=yazı_liste.split(" ")
yazı_liste.remove('')
yazı_liste
aranan="bir"
sayac1=0
#len(yazı_liste)
for j in yazı_liste:
    sayac1=sayac1+1
print(sayac1)

#%%
liste1=[1,2,3,4,5]
liste2=[]
for i in liste1:
    liste2.append(i**2)
print(liste2)
#%%
#iterable
str()
list()
tuple()
set()
dict()
#non iterable
int()
float()
complex()

sayı="102547"
for i in sayı:
    print(i)
#%%
print(*range(0,10,2))
print(*range(10,-1,-1))
print(*range(1,11))
print(abs(-5))

for i in range(1,11,1):
    print(i)


for i in range(10,0,-1):
    print(i)
    
kelime="python"
for i in kelime:
    print(i)
kelime="python"
for i in range(len(kelime)-1,-1,-1):
    print(kelime[i])
#%%
liste=[4,5,7,1,5,6]
a=sum(liste)/len(liste)
a
import statistics
b=statistics.mean(liste)
b
sayac=0
for i in liste:
    sayac=sayac+i
ortalama=sayac/len(liste)
print(ortalama)
#%% 3'ün katları
for i in liste:
    if i%3==0:
        print(i)
#%%
liste = [[3,4],[7,8],[10,11],[14,15]]
for i in liste:
    for j in i:
        print(j)

#%%
toplam=0
for i in range(0,21):
    toplam=toplam+i
print(toplam)
#%%
for i in range(20,-1,-1):
    print(i)
#%%
for i in range(0,101,5):
    print(i)

for i in range(0,101):
    if i%5==0:
        print(i)
#%%
# break, continue, pass

for i in range(1,11):
    if i==5:
        break
    print(i)

for i in range(1,11):
    if i==5:
        continue
    print(i)

for i in range(1,11):
    continue
    print(i)

for i in range(1,11):
    if i==5:
        pass
    print(i)
#%%
i=1
while i<4:
    j=1
    while j<4:
        print("i: {} j: {} ".format(i,j))
        j=j+1
    i=i+1
#%% asal sayı
sayı=int(input("Sayı: "))
sayac=2
while sayac<sayı:
    if sayı%sayac==0:
        print("Asal değil")
        break
    if sayac==sayı-1:
        print("Asal sayıdır")
    sayac=sayac+1
#%%
'''
    *
   ***
  *****
 ******* 
*********
'''
sayı=int(input("Katman sayısı: "))
for i in range(1,sayı+1):
    yazdır=(2*i-1)*"*"
    print(yazdır.center(5*sayı-1," "))
#%%
#ikinci yol
sayı=int(input("Katman sayısı: "))
for i in range(1,sayı+1):
    yazdır=(sayı-i)*" "+(2*i-1)*"*"
    print(yazdır)
for i in range(1,6):
    yazdır=(sayı-2)*" "+3*"*"
    print(yazdır)
#%%
liste=[5,8,7,4,8,9,4,6,1]
#max(liste)
#min(liste)
en_büyük=0
en_küçük=100
for i in liste:
    if en_büyük<i:
        en_büyük=i
    if en_küçük>i:
        en_küçük=i
print(en_küçük)
print(en_büyük)
#%%
liste=[]
for i in range(1500,2701):
    if i%5==0: 
        if i%7==0:
            liste.append(i)
print(liste)
#%%
import random
sayı=random.randint(1, 9)
while True:
    tahmin=int(input("Tahmin: "))
    if tahmin>sayı:
        print("Azalt")
    elif tahmin<sayı:
        print("Arttır")
    else:
        print("Tebrikler")
        break
#%%
sayılar=[i for i in range(1,10)]
çift_sayısı=0
tek_sayısı=0
for i in sayılar:
    if i%2==0:
        çift_sayısı+=1
    else:
        tek_sayısı+=1
print(çift_sayısı)
print(tek_sayısı)
#%%
işlem=input("İşleminiz: ")
sonuc=eval(işlem)
print(sonuc)




#%%
işlem=input("işleminiz: ")
karakterler="+/*-"
liste=[]
asd=""
sayac=0
for i in işlem:
    sayac+=1
    if i not in karakterler:
        asd=asd+i
    else:
        liste.append(asd)
        liste.append(i)
        asd=""
    if sayac==len(işlem):
        liste.append(asd)

sayac=0
sayı1=0
sayı2=0
sonuc=0
for i in liste:
    if sayac%2==0:
        sayı1=int[i]
    else:
        















