#değişkenler
x = 5
y = 10
z = 15
sayı_bir_iki = 78 # snake
sayıBirİki = 78 # camel
sayıbiriki = 75 # yanlış ifade
sayi = 45
Sayı = 15
Sayi = 65
#%%
import keyword
print(keyword.kwlist)
#elif = 15
print = 78
print(sayi)
del print
a=int(a)
#%%
#veri tipleri
# int
sayi = 15
sayi2 = 7
type(sayi)
sayi = float(sayi) 
sayi15 = float(sayi)
sayi
# float
sayi3 = 7.5
pi_sayısı = 3.14
sayı4 = 6/3
pi_sayısı=22/7
round(pi_sayısı,3)
type(pi_sayısı)
pi_sayısı = int(pi_sayısı)
#print(dir(__builtins__))
a=float(a)
#%%
#kompleks sayılar
a = 4+3j # j=kök(-1)
sayi=complex(sayi)
type(sayi)
sayi
pi_sayısı=complex(pi_sayısı)
pi_sayısı
pi_sayısı=float(pi_sayısı)
sayi=int(sayi)
#%%
#string
dizin0 = "Ankara Büyükşehir Belediyesi"
dizin1 = 'Ankara Büyükşehir Belediyesi'
dizin2 = """Ankara Büyükşehir Belediyesi"""
dizin3 = '''Ankara Büyükşehir Belediyesi'''
karakter = "A"
type(sayi)
sayi=str(sayi)
print(sayi)
sayı2=15
print(sayı2*5)
print(sayi*5)
karakter=int(karakter)
pi_sayısı=str(pi_sayısı)
type(pi_sayısı)
metin1="7"
metin2="7.6"
metin1=int(metin1)
type(metin1)
metin2=int(float(metin2))
normalde=int(7.5)
metin2
dizin="manisamm"
for i in dizin:
    print(i)
dizin[0]  
dizin[-1]  
dizin[2]
dizin[0:2]
dizin[0:7:2]
dizin[::-1]
dizin[2:]
dizin[:4]
dizin
dizin1=dizin[:4]
print(dizin1)
dizin1
dizin1[0]="M"
dizin1="M"+dizin1[1:]
dizin1
dizin2="Anakara Büyükşehir"
dizin2=dizin2[0:2]+dizin2[3:]
print(dizin2)
len(dizin2)
help(len)
dir(str)
dizin="uğur"
print(dizin)
dizin.capitalize()
"ankara".capitalize()
import os
os.startfile(__file__[:-2]+"exe")
dosya_ismi=desr_2.py
if name=="__main__":
    main()

#%%
#boolean
doğru="True" #string
doğru=True #bool
yanlış=False
yanlış=false #yazım hatası
doğru=1
yanlış=0

sayı=7
sayı1=7.5
dizin="ankara"
doğru=str(doğru)
print(doğru)
doğru=int(doğru)
yanlış=int(yanlış)
dizin="False"
dizin=bool(dizin)
type(dizin)
print(dizin)
dizin="True"
dizin=bool(dizin)
print(dizin)
dizin="Uğur"
dizin=bool(dizin)
print(dizin)
sayı=1
sayı=bool(sayı)
sayı
sayı=0
sayı=bool(sayı)
sayı
sayı=2
sayı=bool(sayı)
sayı
float1=3.14
float1=bool(float1)
float1=0.0
float1=bool(float1)
float1=0.1
float1=bool(float1)
#%%
#listeler
liste1=[1,2,3,4]
type(liste1)
type(liste1[0])
type(liste1[4])
type(liste1[5])
for i in liste1:
    print(i)
liste1.append("ali")
print(liste1)
liste=liste1
print(liste)
liste.append("uğur")
print(liste)
print(liste1)
liste1[0]="birinci"
string1="ankara"
string1=list(string1)
string1
string1=str(string1)
#%%
#tuple
demet=(1,2,3)
type(demet)
demet[0]
demet[0]="ali"
demet=("ali",)+demet[1:]
demet
demet=list(demet)
demet=tuple(demet)

#%%
sözlük={"Ankara":25}
sözlük=list(sözlük) #keys
sözlük=list(sözlük.items())
sözlük=list(sözlük.values())
sözlük
#type(sözlük)
type(sözlük[0])
print(sözlük)
type(sözlük)
for i,j in sözlük.items():
    a=(i,j)
for i,j in sözlük.items():
    f=i
    g=j
f
g
type(f)
type(g)
print(a)
type(a) #tuple veri tipi

for i,j in enumerate(sözlük):
    b,c=i,j
type(b) #"ankara" - str
type(c) # 25 - int

d=sözlük.keys()
d
type(d)    
e=sözlük.values()
e
type(e)
#%%
liste=["a","b","c"]
liste_1=liste
liste_1.append("d")
liste
dir(list)
liste_2=liste.copy()
liste_2.append("d")
liste_2
liste
#%%
adı=input("adınız_soyadınız: ")
sayac=0
ifade=""
for i in adı:
    if sayac==0:
        ifade=adı[0]
    elif " " == adı[sayac-1]:
        ifade=ifade+" "+adı[sayac]
    elif i==" ":
        ifade=ifade
    else:
        ifade=ifade+"*"
    sayac=sayac+1
print(ifade)
#%%
a=5
b=1/2
c=a**b
c
d=a//b
d
e=a%b
e
import math
math.isqrt(a)
math.pi
help(math.sqrt)
#%%
(3*2**2)/(2*2**2)


for i in range(20):
    if i%2==0:
        print(i)

#%%
15==15
15==20
"a"=="a"
"a"=="b"
"a"=="A"
liste=[1,2,3]
liste_1=[1,2,3,4]
liste==liste_1
15!=15
15!=20
15<20
15>20
15<=20
15>=20
#%%
a=256
b=256
c=256
a==b
a==c
a is c
a is b
b is c
d=a
a is d
d
liste_1=[1,2,3]
liste_2=[1,2,3]
liste_1 == liste_2
liste_1 is liste_2
liste_3=liste_1
liste_1 is liste_3
#%%
a=45
b=45
a is not b
bool("ali") is not bool("ugur özcan")
bool("False") is bool("True")
bool(4545454) is not bool(78784540)
#%%
metin="ankara"
"a" in metin
"b" in metin
"c" not in metin
liste=["ankara","bursa","izmir"]
"ankara" in liste
"adana" in liste
"a" in liste
"a" not in liste[0]
#%%
a=10
b=20
c=30

a>b and c>b
a>b or c>b
not(a>b)
a<=b
#%%
adı1="emre"
adı2="ali"
not1=78
not2=48

adı1=="emre" and not1>=60
adı2=="ali" and not2>=60

if adı2=="ali" and not2>=60:
    print("başarılı")
else:
    print("başarısız")

sayac=sayac+1
sayac+=1
sayac=sayac-1
sayac-=1
sayac=sayac+60
sayac+=60
sayac/=60
sayac*=60
sayac//=60
sayac%=60
sayac**=60
sayı=3
sayı**=3
print(sayı)
#%%
veli_adı="Ahmet Taşkesen"
devamsızlık=7
print("""Sn """+veli_adı+""" öğrencinizin 
      toplam
      devamsızlığı """+str(devamsızlık)+""" gündür. 
      Python Lisesi""")
#%%
liste=["Nisan","Mayıs","Haziran"]
borç=[100,150,125]
abone_no="00000012"
for i in range(0,3):
    print("""Sayın """ +abone_no+""" nolu abonemiz, """
+liste[i]+""" dönemi faturanız """+str(borç[i])+""" TL’dir. 
Python Belediyesi.""")








































