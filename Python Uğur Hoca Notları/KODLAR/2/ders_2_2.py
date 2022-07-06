# -*- coding: utf-8 -*-
#%%
ise_gidis=3.5
eve_gelis=3
ay_gun_sayısı=22
yıl_ay_sayısı=12
aylık=(ise_gidis+eve_gelis)*ay_gun_sayısı
print("Aylık yol masrafınız: "+str(aylık))
print("Yıllık yol masrafınız: "+str(aylık*12))
#%%
import math
r=float(input("Yarıçapı giriniz: "))
alan=round(math.pi*r**2,3)
print("Dairenin alanı: "+str(alan))
#%%
mart_m3=346
mart_fatura_tl=273.87
birim_fiyat=mart_fatura_tl/mart_m3
günlük_sarfiyat_tl=mart_fatura_tl/31
print("Nisan fatura: "+str(round(günlük_sarfiyat_tl*30,3)))
print("Şubat fatura: "+str(round(günlük_sarfiyat_tl*28,3)))
#%%
osman = "Araştırma Geliştirme Müdürü"
mehmet = "Proje Sorumlusu"
osman,mehmet=mehmet,osman
#%%
# print()
print("Uğur Özcan")
adı_soyadı="Ali Can"
print(adı_soyadı)
print("Ali","Ahmet","Veli","Ayşe","Uğur")
print("Ali","Ahmet","Veli","Ayşe","Uğur",sep=" Özcan ")


print("Ali"+"Ahmet"+"Veli"+"Ayşe")

print("Bir ifade yazıyor...", end="son kısmı")
print("Bir ifade yazıyor...", end="\nson kısmı")
print("Ali","Ahmet","Veli","Ayşe","Uğur",end="\nson kısmı")
print("Ali",end="///***")
print("Ahmet",end="---??")
print("Mehmet")

dosya=open("deneme.txt","w",encoding="utf-8")
print("Bu çok daha yeni bir yazdırma işlemidir...",file=dosya)
dosya.close()
#import os
#os.startfile("deneme.txt")
#os.system("taskkill /f /im notepad.exe")

dosya=open("deneme.txt","w",encoding="utf-8")
print("Ankara",flush=True, file=dosya)
print("Bursa",flush=True, file=dosya)
print("İstanbul",flush=True, file=dosya)
dosya.close()
os.system("del deneme.txt")
#%%
print("yazdır") #bununla aşağıdaki aynı şey
import sys
print("yazdır",sep=" ", end="\n", file=sys.stdout, flush=False)
#%%
print("C:\\Windows\\System32\\ayna.exe")

print(*"İstanbul") #aşağıdaki kod ile aynıdır
print("İ","s","t","a","n","b","u","l")
print(*"TBMM",sep=".")
#%%
a=5
b=9
c=7
toplam=a+b+c
print(a,b,"ve",c,"'nin toplamı",toplam,"'dır.") #birinci yol
print("{}, {} ve {}'nin toplamı {}'dir.".format(a,b,c,toplam)) #ikinci yol
print("{1}, {2} ve {0}'nin toplamı {3}'dir.".format(a,b,c,toplam))
print(f"{a}, {b} ve {c}'nin toplamı {toplam}'dir.") #üçüncü yol
#%%
x=3
y=4
hipotenüs=(x**2+y**2)**(1/2)
print("""bir kenarı 3 diğer kenarı 4 olan
      üçgenin hipotenüsü 5'dir.""")
#%%
# input()
x=float(input("Bir kenarı giriniz: "))
y=float(input("Diğer kenarı giriniz: "))
h=(x**2+y**2)**(1/2)
print(f"{x}, {y}'nin hipotenüsü {h}'dır.")






























#%%