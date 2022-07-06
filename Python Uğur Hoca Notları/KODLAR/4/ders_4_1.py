# -*- coding: utf-8 -*-
# 1- Üç bardak içinden doğru olanı 
# bulma oyunu yazınız.
import random
sayı=random.randint(1, 3)
if sayı==1:
    bardak1="X"
    bardak2="O"
    bardak3="O"
elif sayı==2:
    bardak2="X"
    bardak1="O"
    bardak3="O"
else:
    bardak3="X"
    bardak1="O"
    bardak2="O"
tahmin=int(input("Tahmininiz: "))
if tahmin==sayı:
#    print("{} {} {}".format(bardak1,bardak2,bardak3))
    print(f"{bardak1} {bardak2} {bardak3}")
#    print("{0} {1} {2}".format(bardak1,bardak2,bardak3))
    
    print("Doğru bildiniz!!")
else:
    print("{} {} {}".format(bardak1,bardak2,bardak3))
    print("Yanlış tahmin, kaybettiniz!!!")
#%%
# 2- A ve B isimli takımların basketbol maçında aldıkları sayılar şöyledir;
'''
A takımı;
3 puanlık atış sayısı 4-15 arasında rastgele bir sayıdır.
2 puanlık atış sayısı 2-19  arasında rastgele bir sayıdır.
1 puanlık atış sayısı 10-30 arasında rastgele bir sayıdır.

B takımı;
3 puanlık atış sayısı 1-20 arasında rastgele bir sayıdır.
2 puanlık atış sayısı 4-14  arasında rastgele bir sayıdır.
1 puanlık atış sayısı 15-25 arasında rastgele bir sayıdır.
'''
import random
puan3A=random.randint(4, 15)*3
puan2A=random.randint(2, 19)*2
puan1A=random.randint(10, 30)
puan3B=random.randint(1, 20)*3
puan2B=random.randint(4, 14)*2
puan1B=random.randint(15, 25)
puanA=puan3A+puan2A+puan1A
puanB=puan3B+puan2B+puan1B
if puanA>puanB:
    print("A takımı kazandı...","A: ",puanA,"B: ",puanB)
elif puanA<puanB:
    print("B takımı kazandı...","A: ",puanA,"B: ",puanB)
else:
    print("Maç berabere bitti...","A: ",puanA,"B: ",puanB)
#%%
'''
3- Telefonunuza gelen bir çağrının dolandırıcı olup olmadığını son dört hanesine anladığınızı varsayalım. Eğer numaranın son dört hanesinin;

İlk hanesi 2’den küçük veya 7’den büyükse
Son hanesi 4’den küçük veya 9 ise
İkinci ve üçüncü haneler eşit ise
Gelen telefon dolandırıcıdır.

'''
import random
gelenArama=random.randint(1000000000, 9999999999)
#gelenArama=1234561003
type(gelenArama)
sonDort=str(gelenArama)
sonDort
type(sonDort)
sonDort=sonDort[-4:]  
#sonDort=sonDort[6:]  
type(sonDort)
sonDort
if int(sonDort[0])<2 or int(sonDort[0])>7:
    if int(sonDort[-1])<4 or int(sonDort[-1])==9:
        if int(sonDort[1])==int(sonDort[2]):
            print("0"+str(gelenArama))
            print("Sakın telefonu açma...")
else:
    print("0"+str(gelenArama))
    print("Telefonu açabilirsin...")
#%%
'''
A-  Here are the three burger choices:
1 – Cheeseburger (461 Calories)
2 – Fish Burger (431 Calories)
3 – Veggie Burger (420 Calories)
4 – no burger

B-  Here are the three side order choices:
1 – Fries (100 Calories)
2 – Baked Potato (57 Calories)
3 – Chef Salad (70 Calories)
4 – no side order

C-  Here are the three drink choices:
1 – Soft Drink (130 Calories)
2 – Orange Juice (160 Calories)
3 – Milk (118 Calories)
4 – no drink

D- Here are the three dessert choices:
1 – Apple Pie (167 Calories)
2 – Sundae (266 Calories)
3 – Fruit Cup (75 Calories)
4 – no dessert

'''

sipariş=input("Sipariş girişi A-1,B-3,C-1,D-4: ")
A=int(sipariş[2])
B=int(sipariş[6])
C=int(sipariş[10])
D=int(sipariş[14])
tK=0
if A==1:
  tK+=461
elif A==2:
  tK+=431
elif A==3:
  tK+=420
else:
    tK+=0

if B==1:
  tK+=100
elif B==2:
  tK+=57
elif B==3:
  tK+=70
else:
    tK+=0    

if C==1:
  tK+=130
elif C==2:
  tK+=160
elif C==3:
  tK+=118
else:
    tK+=0

if D==1:
  tK+=167
elif D==2:
  tK+=266
elif D==3:
  tK+=75
else:
    tK+=0

print("Toplam kaloriniz: ", tK)
#%%
import datetime
bugün=datetime.datetime.today()
bugün
type(bugün)
bugün=str(bugün)
bugün
ay=bugün[5:7]
gün=bugün[8:10]
ay
gün
ay=int(ay)
gün=int(gün)
dgunu=int(input("Gün:  "))
day=int(input("Ay:  "))
if day>ay:
    print("Acaba ne hediye alınacak")
elif day<ay:
    print("Hediyeler seneye kaldı")
elif day==ay:
    if dgunu>gün:
        print("Acaba ne hediye alınacak")
    elif dgunu<gün:
        print("Hediyeler seneye kaldı")
    else:
        print("Bugün doğum günün")
#%%
'''
6- En fazla 255 karakterden oluşan bir kullanıcı ifadesinde, kullanıcının mutlu veya mutsuz olduğunu belirlemek istiyoruz. Bunun için emojileri sayacağız.
mutlu
:-) 
mutsuz
:-(
Mutlu sayısı fazla ise «kullanıcı bugün iyi halde»
Mutsuz sayısı fazla ise «kullanıcı bugün kötü»
İkisi eşit ise «kullanıcının sinirleri bozuk»
Hiç ifade yoksa «kullanıcı belirsiz»
'''

ifade="Bugün günlerden Cumartesi :-), hava çok soğuk :-( çocukların ne hali ne olacak :-(  Bugün günlerden Cumartesi :-), hava çok soğuk :-( çocukların ne hali ne olacak :-(  Bugün günlerden Cumartesi :-), hava çok soğuk :-( çocukların ne hali ne olacak :-(  Bugün günlerden Cumartesi :-), hava çok soğuk :-( çocukların ne hali ne olacak :-(  Bugün günlerden Cumartesi :-), hava çok soğuk :-( çocukların ne hali ne olacak :-(  Bugün günlerden Cumartesi :-), hava çok soğuk :-( çocukların ne hali ne olacak :-( "
uzunluk=len(ifade)
uzunluk
dir(ifade)
help(str.count)
if uzunluk>255:
    print("karakter limiti aşıldı...")
mutlu=ifade.count(":-)")
print(mutlu)
mutsuz=ifade.count(":-(")
print(mutsuz)
#%%

string="ankara"
for i in string:
    if i == "a":
        print(i)
string[1:4]
string[0]
string.capitalize()
string
string=string.capitalize()
string
dir(__builtins__)
sayı=12456
type(sayı)
sayı=sayı.capitalize()
dir(int)
dir(str)
dir(list)
liste=[1,2,3,4,5]
toplam=sum(liste)
toplam
topla=sum((1,2,3,4,5))
topla
sayı=9

import math
dir(math)
işlem=(5*8+4**7)/5
karekök=math.sqrt(işlem)
karekök

9.sqrt() #bu olmaz

ifade="ankara"
ifade.capitalize()
"ankara".capitalize()
#%%
# replace
ifade="ankara"
ifade=ifade.replace("a", "e")
ifade
ifade="ankara"
ifade=ifade.replace("a", "e")
ifade
help(str.replace)
#%%
ifade="Bugün günlerden Cumartesi :-), hava çok soğuk :-( çocukların ne hali ne olacak :-(  Bugün günlerden Cumartesi :-), hava çok soğuk :-( çocukların ne hali ne olacak :-(  Bugün günlerden Cumartesi :-), hava çok soğuk :-( çocukların ne hali ne olacak :-(  Bugün günlerden Cumartesi :-), hava çok soğuk :-( çocukların ne hali ne olacak :-(  Bugün günlerden Cumartesi :-), hava çok soğuk :-( çocukların ne hali ne olacak :-(  Bugün günlerden Cumartesi :-), hava çok soğuk :-( çocukların ne hali ne olacak :-( "
ifade=ifade.split()
ifade
ifade=set(ifade)
ifade
for i in ifade:
    print(i,end="--")

ifade=ifade.split("Cumartesi")
print(ifade)
#%%
dizin="""Ankara
İstanbul
Bursa
İzmir"""
dizin.splitlines()

dizin2="Elma\nArmut\nMuz"
dizin2.splitlines()
#%%
sehir="AMASYA"
sehir.lower()
sehir="MUĞLA"
sehir.lower()
sehir="DİYARBAKIR"
from unicode_tr import *
sehir=unicode_tr(sehir)
sehir.lower()

sehir="amasya"
sehir.upper()
sehir="muğla"
sehir.upper()
sehir="izmir"
sehir.upper()
sehir="çankırı"
sehir.upper()
sehir.islower()

if sehir.islower():
    print(sehir.upper())

if sehir.isupper():
    print(sehir.lower())
#%%
dosya="deneme.txt"
dosya.endswith(".txt")
dosya.endswith("t")
dosya.startswith("d")
dosya.startswith("e")
#%%
adı="uğur özcan kırşehir"
adı.title()
adı.capitalize()
#%%
kelime="AnkaRA"
kelime.swapcase()
#%%
ifade="                 ankara          "
ifade.strip()
#%%
sehir="ankara"
sehir=list(sehir)
print(sehir)
sehir="/".join(sehir)
print(sehir)
liste=["ankara","izmir","bursa"]
liste=", ".join(liste)
print(liste)
#%%
adı="MahMut"
adı.index("m")
adı.rindex("m")
adı.find("m")
adı.rfind("m")
#%%
dizin="istanbul"
dizin.partition("an")
dizin.rpartition("an")
dizin.split("an")
#%%
dizin="ankara\tistanbul"
print(dizin)
dizin.expandtabs(12)
#%%
q_klavye="qwertyuıopğüasdfghjklşi,zxcvbnmöç."
f_klavye="--*!uıopğüasdfghjklşi,zxcvbnmöç.qw"

#f_klavye="fgğıodrnhpqwuieaütkmlyşxjövcçzsb.,"

cevir=str.maketrans(q_klavye,f_klavye)
ifade="artık ders bitsede gitsek"
ifade.translate(cevir)














