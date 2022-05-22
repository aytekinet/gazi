# -*- coding: utf-8 -*-
#%% adamAsmaca
import pyfiglet
import sys
import time
import os
import random
import datetime
liste=[]
deneme=0
seçilen=0
def banner():
    yazdır=pyfiglet.figlet_format("adam Asmaca")
    print(yazdır)
def giriş():
    global liste
    global ekran_çıktısı
    global seçilen
    banner()
    print()
    print("Süreniz 1 dakika...")
    print("1- İsim")
    print("2- Şehir")
    print("99- Çıkış")
    seçim=input("Seçimim: ")
    if seçim=="1":
        dosya=open("isim.txt","r",encoding="utf-8")
        liste=dosya.readlines()
        dosya.close()
        for i in range(0,len(liste)):
            liste[i]=liste[i].removesuffix("\n")
    elif seçim=="2":
        dosya=open("şehir.txt","r",encoding="utf-8")
        liste=dosya.readlines()
        dosya.close()
        liste=liste[0].split(" ")
    elif seçim=="99":
        banner()
        print("Oyundan çıkılıyor...")
        os.system("cls")
        banner()
        print("Lütfen bekleyiniz.")
        time.sleep(1)
        os.system("cls")
        banner()
        print("Lütfen bekleyiniz..")
        time.sleep(1)
        os.system("cls")
        banner()
        print("Lütfen bekleyiniz...")
        time.sleep(1)
        os.system("cls")
        banner()
        print("Lütfen bekleyiniz....")
        time.sleep(1)
        os.system("cls")
        sys.exit()
    else:
        giriş()
    rassal_sayı=random.randint(0, len(liste))
    seçilen=liste[rassal_sayı]
    ekran_çıktısı=[]
    for i in range(0,len(seçilen)):
        if i!=" ":
            ekran_çıktısı.append("_")
        else:
            ekran_çıktısı.append(" ")
def kontrol():
    global deneme
    if deneme==1:
        print(r"""
              O
              """)
    if deneme==2:
        print(r"""
              O
              |
              """)
    if deneme==3:
        print(r"""
              O
             /|
              """)
    if deneme==4:
        print(r"""
              O
             /|\
              """)
    if deneme==5:
        print(r"""
              O
             /|\
             / 
              """)
    if deneme==6:
        print(r"""
              O
             /|\
             / \
              """)
giriş()
a=datetime.datetime.now()
def çıkış():
    os.system("cls")
    print("Oyunu kaybettiniz...")
    print(seçilen)
    sys.exit()
def adam_asmaca():
    global seçilen
    global ekran_çıktısı
    global deneme
    b=datetime.datetime.now()
    if a.second<=b.second and a.minute==b.minute:
        t=b.second-a.second #geçen süre
    elif a.second>=b.second and a.minute<b.minute:
        t=(60-a.second)+b.second
    if 60-t<=0:
        çıkış()
    print("Kalan süreniz:",60-t)
    banner()
    #print("Oyun başladı...")
    print()
    print(*ekran_çıktısı)
    print()
    if "_" not in ekran_çıktısı:
        banner()
        print(*ekran_çıktısı)
        print()
        print("Tebrikler kazandınız...")
        karar=input("Devam etmek ister misiniz? E/h: ")
        if karar=="h":
            çıkış()
        else:
            deneme=0
            giriş()
            os.system("cls")
            adam_asmaca()
        
    seçim=input("Bir harf tahmin ediniz...: ")
    print()
    if seçim in seçilen:
        for i in range(0,len(seçilen)):
            if seçim==seçilen[i]:
                ekran_çıktısı[i]=seçim
        adam_asmaca()
    
    else:
        deneme=deneme+1
        kontrol()
        if deneme==6:
            çıkış()
        adam_asmaca()
adam_asmaca()                



