# -*- coding: utf-8 -*-
#pip install pyfiglet
import random
import pyfiglet
import os
import sys
import time
print(pyfiglet.figlet_format("Bulmaca"))
print()
print("Oyuna Hoşgeldiniz.".rjust(45," "))
print()
print("1-Oyuna başla")
print("99-Oyundan çık")
print()
os.system("cls")
rekor=100
while True:
    print(pyfiglet.figlet_format("Bulmaca"))
    print()
    print("Oyuna Hoşgeldiniz.".rjust(45," "))
    print()
    print("1-Oyuna başla")
    print("99-Oyundan çık")
    print()
    seçim=input("Seçiminiz: ")
    print()
    if seçim=="1":
        os.system("cls")
        print("Oyun yükleniyor.")
        time.sleep(1)
        os.system("cls")
        print("Oyun yükleniyor..")
        time.sleep(1)
        os.system("cls")
        print("Oyun yükleniyor...")
        time.sleep(1)
        os.system("cls")
        print("Oyun yükleniyor....")
        time.sleep(1)
        os.system("cls")
        print("Oyun yükleniyor.....")
        time.sleep(3)
        print("Oyun başladı...")
        time.sleep(2)
        os.system("cls")
        print(pyfiglet.figlet_format("Bulmaca"))
        print()
        print("Oyuna Başladınız.".rjust(45," "))
        print()
        print()
        sayı=random.randint(0, 100)
        tahmin_sayısı=1
        print("Son rekor: ",rekor)
        while True:
            tahmin=input("Tahmininiz: ")
            if tahmin=="q":
                print("Oyundan çıkılıyor...")
                time.sleep(2)
                sys.exit()
            elif int(tahmin)>sayı:
                print("Daha küçük bir sayı söyle")
            elif int(tahmin)<sayı:
                print("Daha büyük sayı söyle")
            else:
                print("Tebrikler...")
                print(tahmin_sayısı,"defa tahmin yaptınız")
                if rekor>tahmin_sayısı:
                    rekor=tahmin_sayısı
                break
            tahmin_sayısı=tahmin_sayısı+1
        karar=input("Tekrar Oynamak İster misiniz:e/h ")
        if karar=="h":
            break
        os.system("cls")
    elif seçim=="99":
        sys.exit()
    else:
        print("Seçiminizi tekrar yapınız...")
        os.system("cls")


