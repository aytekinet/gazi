# -*- coding: utf-8 -*-
#%%
for i in range(0,7): #1.yol
    if i==3 or i==6:
        continue
    print(i)

sayac=-1 #2.yol
while sayac<6:
    sayac=sayac+1
    if sayac==3 or sayac==6:
        continue
    print(sayac)
#%%
x,y=0,1
while y<=100:
    print(y, end=",")
    x,y=y,x+y
#%%
satır=int(input("Satır: "))
sutun=int(input("Sutun: "))
matris=[]
for _ in range(0,satır):
    matris.append([])
#print(matris)
for i in range(0,satır):
    for j in range(0,sutun):
        matris[i].append(i*j)
print(matris)
#%%
alfabe="a b c ç d e f g ğ h i ı j k l m n o ö p r s ş t u ü v y z"
ALFABE="A B C Ç D E F G Ğ H İ I J K L M N O Ö P R S Ş T U Ü V Y Z"
rakam="0123456789"
karakter="$#@"
'''
Doğrulama:
[a-z] arasında en az 1 harf ve [A-Z] arasında 1 harf.
[0-9] arasında en az 1 sayı.
[$#@]'dan en az 1 karakter.
Minimum uzunluk 6 karakter.
Maksimum uzunluk 16 karakter.
'''
a=0
b=0
c=0
d=0
e=0
while True: #Aa1@454545
    parola=input("Parolanız: ")
    for i in parola:
        if i in alfabe:
            a=1
        if i in ALFABE:
            b=1
        if i in rakam:
            c=1
        if i in karakter:
            d=1
        if len(parola)>=6 and len(parola)<=16:
            e=1
    if a==1 and b==1 and c==1 and d==1 and e==1:
        print("Parola geçerlidir...")
        break
#%%
import random
adet=int(input("Sayı sayısı: "))
liste=[]
for _ in range(0,adet):
    liste.append(random.randint(0, 50))
#print(liste)
maks=-1
mod=[]
for i in liste:
    if maks<=liste.count(i) and liste.count(i)!=1:
        maks=liste.count(i)
        if i not in mod:
            mod.append(i)
liste.sort()
if len(liste)%2==0:
    a=len(liste)/2
    b=a+1
    medyan=(liste[int(a)-1]+liste[int(b)-1])/2
else:
    a=(len(liste)+1)/2
    medyan=liste[int(a)-1]
print(liste)
print("Mod:",mod, "Tekrar sayısı:",maks)
print("Medyan:",medyan)
#%%
n=int(input("Uzunluk: "))
for i in range(n,0,-1):
    print()
    for j in range(i,0,-1):
        print(j,end=" ")
        
#%%
liste=[1,2,3,3,3,3,4,5]
unique_liste=[]
for i in liste:
    if i not in unique_liste:
        unique_liste.append(i)
print(unique_liste)        
#%%
# bir listede ardışık tekrar eden sayıları en az yer değiştirmeyle bulma
import random

def ekle(i):
    a=random.randint(0, len(liste)-1)
    b=liste[a]
    liste.pop(a)
    liste.insert(i,b)
    

def kontrol(liste):
    global sayac
    for i in range(1,len(liste)):
        if liste[i]==liste[i-1]:
            ekle(i)
            sayac=sayac+1
            kontrol(liste)    

liste=[1,1,2,3,3,3,4,5,6,7]
enaz=10000
for j in range(0,100):
    sayac=0
    kontrol(liste)
    if enaz>sayac and sayac!=0:
        enaz=sayac
        çözüm=liste.copy()
print(enaz)
print(çözüm)    
#%%
sayı=int(input("Sayı: "))
bölenler=[]
for i in range(1,int(sayı/2)+1):
    if sayı%i==0:
        bölenler.append(i)
toplam=0
for i in bölenler:
    toplam=toplam+i
if toplam==sayı:
    print(bölenler)
    print("Mükemmel sayıdır")
else:
    print(bölenler)
    print("Mükemmel sayı değildir")
#%%
kelime=input("Kelime: ")
if kelime[::-1]==kelime:
    print("Evet")
else:
    print("Hayır")
#%%
kelime=input("Kelime: ")
eski=list(kelime)
kelime=list(kelime)
type(kelime)
kelime.reverse()
if kelime==eski:
    print("Evet")
else:
    print("Hayır")

#%%
liste=[1,1,2,3]
liste=set(liste)
liste=list(liste)
liste
dir(set)
#%%
alphabet="a b c ç d e f g ğ h i ı j k l m n o ö p r s ş t u ü v y z"
alphabet=alphabet.replace(" ", "")
alphabet
#kelime="abcçdefgğhiıjklmnoöprsştuüvyz"
kelime="Pijamalı hasta yağız şoföre çabucak güvendi"
sonuc=1
for i in alphabet:
    if i not in kelime:
        sonuc=0    
if sonuc==0:
    print("Hayır")
else:
    print("Evet")
#%%
def test(a):
    def add(b):
        nonlocal a
        a += 1
        return a+b
    return add



func= test(10)
print(func(10))





    
    





