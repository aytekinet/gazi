# -*- coding: utf-8 -*-
# İstisna yakalama
sayı=input("Bir sayı giriniz: ")
işlem=int(sayı)**2
print(işlem)
# Error
prit("ankara")
for i in range(0,10)
    print(i)
#%% bug
sayı1=input("sayı 1: ")
sayı2=input("sayı 2: ")
print(int(sayı1)+int(sayı2))
#%% exceptions
# ValueError:
# ZeroDivisionError:
while True:
    sayı1=input("Sayı 1: ")
    sayı2=input("Sayı 2: ")
    try:
        sayı1=int(sayı1)# ValueError:
        sayı2=int(sayı2)# ValueError:
        print(sayı1/sayı2)# ZeroDivisionError:
        break
    except ValueError:
        print("Sayı değeri giriniz...")
    except ZeroDivisionError:
        print("Sıfıra bölme hatası...")
#%%
while True:
    sayı1=input("Sayı 1: ")
    sayı2=input("Sayı 2: ")
    try:
        sayı1=int(sayı1)# ValueError:
        sayı2=int(sayı2)# ValueError:
        print(sayı1/sayı2)# ZeroDivisionError:
        break
    except (ValueError, ZeroDivisionError):
        print("Bir hata ile karşılaşıldı...")
#%%
while True:
    sayı1=input("Sayı 1: ")
    sayı2=input("Sayı 2: ")
    try:
        sayı1=int(sayı1)# ValueError:
        sayı2=int(sayı2)# ValueError:
        print(sayı1/sayı2)# ZeroDivisionError:
        break
    except:
        print("Bir hata ile karşılaşıldı...")
#%%
while True:
    sayı1=input("Sayı 1: ")
    sayı2=input("Sayı 2: ")
    try:
        sayı1=int(sayı1)# ValueError:
        sayı2=int(sayı2)# ValueError:
        print(sayı1/sayı2)# ZeroDivisionError:
        break
    except ValueError as hata1:
        print(hata1)
        print("Sayı değeri giriniz...")
    except ZeroDivisionError as hata2:
        print(hata2)
        print("Sıfıra bölme hatası...")
#%%
while True:
    sayı1=input("Sayı 1: ")
    sayı2=input("Sayı 2: ")
    try:
        sayı1=int(sayı1)# ValueError:
        sayı2=int(sayı2)# ValueError:
    except ValueError as hata1:
        print(hata1)
        print("Sayı değeri giriniz...")
    else:
        try:
            print(sayı1/sayı2)# ZeroDivisionError:
            break
        except ZeroDivisionError as hata2:
            print(hata2)
            print("Sıfıra bölme hatası...")
#%%
try:
    dosya=open("deneme.txt","w")
    dosya.write("Merhaba")
except IOError:
    print("Yapılacak işler...")
finally:
    dosya.close()
#%%
for i in range(0,50):
    if i==20:
        raise Exception("Program çöktü...")
#%%
while True:
    sayı1=input("Sayı 1: ")
    sayı2=input("Sayı 2: ")
    try:
        sayı1=int(sayı1)# ValueError:
        sayı2=int(sayı2)# ValueError:
        print(sayı1/sayı2)# ZeroDivisionError:
        break
    except ValueError:
        print("Sayı değeri giriniz...")
        raise
    except ZeroDivisionError:
        print("Sıfıra bölme hatası...")
        raise
#%%
for i in range(0,50):
    if i==20:
        raise TypeError("Program çöktü...")

#%%
sayı=[]
for i in range(0,3):
    sayı1=input("Bir sayı giriniz: ")
    sayı.append(sayı1)
try:
    toplam=0
    for i in range(0,3):
        sayı[i]=int(sayı[i])
        toplam=toplam+sayı[i]
    print(toplam)
except ValueError as hata:
    print(hata)
    print("Karakter girilmiş...")  
except:
    print("Beklenmeyen bir hata ile karşılaşıldı...")
finally:
    print(sayı)
#%%
#demetler...
#string+list
()
print ("yazdır","yazdır")
print("yazdır","yazdır")
("yazdır","yazdır") #tuple, python2
yazdır, yazdır # normal yazdırma işlemi, python3
#%%
demet=()
type(demet)
demet=tuple()
type(demet)
demet=(13,)
type(demet)
demet=tuple(13) #tanımlanamaz
demet=tuple(True) #tanımlanamaz
demet=tuple(1.3) #tanımlanamaz
demet=tuple([13]) #tanımlanabilir
demet=tuple((13,)) #tanımlanabilir
demet=tuple("abcdefg") #tanımlanabilir
demet
type(demet)
demet=13,
type(demet)
#%%
demet=([1,2,3,4,5],)
demet
type(demet)
demet1=tuple([1,2,3,4,5])
demet1
type(demet1)
demet=(1,2,3,4,5)
demet
type(demet)
demet=("ali",12,1.23,True,[1,2,3],(1,2,3))
demet
demet[0]
demet[1]
demet[-1]
demet[::-1]
demet[0][-1]
demet[0]="veli"
demet=list(demet)
demet[0]="veli"
demet=tuple(demet)
demet
demet=("ali",)+demet[1:]
demet
demet=demet+(["a","b"],)
demet
for i in demet:
    print(i)
dir(tuple)
demet.count("ali")
demet.index("ali")
#%%
#Sözlükler
sözlük={}
type(sözlük)
sözlük=dict()
type(sözlük)
#%%
sözlük={"defter":"notebook",
        "kalem":"pencil",
        "silgi":"eraser",
        "masa":"table"}
len(sözlük)
sözlük["defter"]
sözlük[0]
sözlük["masa"]
sözlük["pencere"]
sözlük["pencil"]
sözlük["pencere"]="window"
print(sözlük)
#%%
"""
,
,
,
,
,
,
,
,
,
,

"""
#%%
"""
mutable: list,dict,set
immutable: str,int,float,bool,tuple,frozen sets
"""
#%%
#'clear'
sözlük
sözlük.clear()
sözlük
del sözlük
sözlük
#%%
#'copy'
sözlük1={"ali":78}
sözlük2={"ahmet":32}
sözlük1=sözlük2
sözlük1
sözlük2
sözlük1["ali"]=78
sözlük1
sözlük2
sözlük1=sözlük2.copy()
sözlük1
sözlük1["ayşe"]=98
sözlük1
sözlük2
#%%
#'fromkeys'
liste=["ankara","bursa","izmir"]
sözlük=dict.fromkeys(liste,"Şehir")
print(sözlük)
#%%
#'get'
sözlük["ankara"]
sözlük["istanbul"]
sözlük.get("istanbul","Bu kelime sözlükte yok.")
sözlük.get("bursa")
sözlük
#%%
#'items'
sözlük={"ali":78,"ahmet":45,"ayşe":99}
print(sözlük)
for i,j in sözlük.items():
    print(i)
    print(j)
print(sözlük.items())
type(sözlük.items())
type(sözlük)
#'keys'
for i in sözlük.keys():
    print(i)
print(list(sözlük.keys()))
type(list(sözlük.keys()))
#'values'
for j in sözlük.values():
    print(j)
print(list(sözlük.values()))
type(sözlük.values())
#%%
#'pop'
sözlük
sözlük.pop("ali")
sözlük
sözlük.pop("yasin")
#'popitem'
sözlük
sözlük["ali"]=78
sözlük["yasin"]=55
sözlük
sözlük.popitem()
#%%
#'setdefault'
sözlük
sözlük.setdefault("ali",98)
sözlük
sözlük["ali"]=98
sözlük.setdefault("ugur",100)
sözlük
#%%
#'update'
sözlük
yeni_sözlük={"ali":98,
             "ahmet":20,
             "hande":45,
             "hasan":96}
sözlük.update(yeni_sözlük)
sözlük
#%%
stok={"elma":6,"armut":15,"erik":20}
bugun={"elma":14,"kiraz":30,"armut":0}
stok.update(bugun)
stok
stok.pop("armut")
#%%
personel={"Uğur":
          {"Birim":"Üretim",
           "Yaş":43,
           "Memleket":"Kırşehir"},
          "Ayşe":
              {"Birim":"Satış",
               "Yaş":30,
               "Memleket":"Ankara"}}
personel["Uğur"]["Birim"]
#%%anahtar için
sözlük={"ali":45}#tanımlanabilir
sözlük={12:45}#tanımlanabilir
sözlük={(1,2,3):45}#tanımlanabilir
sözlük={[1,2,3]:45}#tanımlanamaz
sözlük={{"a":1}:45}#tanımlanamaz
sözlük={{1,2,3}:45}#tanımlanamaz
sözlük={frozenset((1,2,3)):45}#tanımlanabilir
sözlük={True:45}#tanımlanabilir
sözlük
#değer için; hepsi kullanılabilir
sözlük={True:"Uğur",False:"Özcan"}
sözlük[False]
sözlük[True]
#%%Set
küme={}
type(küme)
küme=set()
type(küme)
küme={1,1,1,2,2,3,3,3,3,3,4}
print(küme)
küme={1,1.2,"ali",True,(1,2,3)}
liste=[1,2,3,4,4,4,5]
küme=set(liste)
küme
küme=set("abcdefg")
küme
küme={1,2,(3,4)}
küme
küme=set("abcdefg")
print(küme)
küme[0]
küme1={1,2}
küme2={3,4}
küme=küme1+küme2
#%%
"""
,
 ,
,
,
,
 ,
 ,
 ,

 ,
,

 ,
 
"""
#%%  'add'
küme={1,2,3}
küme=küme+{4}
küme.add(4)
küme
küme.add(3)
küme
küme.add((5,6,7))
küme
küme.add([8,9,10])
küme.add("ali")
küme
küme1=set()
küme1.add("ahmet")
küme1
#%% 'clear'
küme
küme.clear()
küme
del küme
#%% 'discard', 'remove'
küme={1,2,3}
küme
küme.discard(1)
küme
küme.discard(2)
küme
küme.discard(3)
küme
küme.discard(4)
küme={1,2,3}
küme
küme.remove(2)
küme
küme.remove(4)
#%%  'copy'
küme1={1,2,3}
küme2=küme1
küme2.add(4)
küme1
küme3=küme1.copy()
küme3.add(6)
küme1
küme3
#%%  'difference'
A={1,2,3,4}
B={3,4,5,6}
A.difference(B)
B.difference(A)
A-B
B-A
A
B
C=A-B
C
type(C)
# 'difference_update'
A={1,2,3,4}
B={3,4,5,6}
A.difference_update(B) # A=A-B
A
B.difference_update(A) # B=B-A
B
#%% 'intersection'
A={1,2,3,4}
B={3,4,5,6}
C=A.intersection(B)
B.intersection(A)
C=set()
bool(A.intersection(B))
bool(C)
A&B
B&A
C=A&B


#%%
alfabe="a b c ç d e f g ğ h i ı j k l m n o ö p r s ş t u ü v y z"
ALFABE="A B C Ç D E F G Ğ H İ I J K L M N O Ö P R S Ş T U Ü V Y Z"
rakam="0123456789"
karakter="$#@"
alfabe=set(alfabe)
ALFABE=set(ALFABE)
rakam=set(rakam)
karakter=set(karakter)

'''
Doğrulama:
[a-z] arasında en az 1 harf ve [A-Z] arasında 1 harf.
[0-9] arasında en az 1 sayı.
[$#@]'dan en az 1 karakter.
Minimum uzunluk 6 karakter.
Maksimum uzunluk 16 karakter.
'''
while True:
    parola=input("Parola: ")
    uzunluk=len(parola)
    parola=set(parola)
    if parola&alfabe and parola&ALFABE and parola.intersection(karakter) and parola.intersection(rakam) and uzunluk>6 and uzunluk<16:
        print("Parola geçerli...")
        break
    print("Geçersiz parola, tekrar deneyiniz...")

#%% 'issubset'
A={1,2,3,4}
B={3,4,5,6}
A.issubset(B)
B.issubset(A)
C={2,3}
C.issubset(A)
C.issubset(B)
#%%  'issuperset'
A={1,2,3,4}
B={3,4,5,6}
C={2,3}
A.issuperset(B)
A.issuperset(C)
#%% 'isdisjoint'
A={1,2,3,4}
B={3,4,5,6}
C={2,3}
D={7,8,9}
A.isdisjoint(B)
A.isdisjoint(C)
C.isdisjoint(A)
A.isdisjoint(D)
#%% 'intersection_update'
A={1,2,3,4}
B={3,4,5,6}
A.intersection_update(B)
A
#%% 'union'
A={1,2,3,4}
B={3,4,5,6}
A.union(B)
A
B
A|B
#'update'
A.update(B) #union_update
A
#%%  'pop',
A={1,2,3,4}
A.pop()
A
#%% 'symmetric_difference',
A={1,2,3,4}
B={3,4,5,6}
#(A/B)U(B/A)
A.symmetric_difference(B) 
#'symmetric_difference_update',
A.symmetric_difference_update(B)
A
#%%
Örnek_Sözlük = {0: 10, 1: 20}
Örnek_Sözlük[2]=30
Örnek_Sözlük
#%%
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic1.update(dic2)
dic1
dic1.update(dic3)
dic1
#%%
liste=[i for i in range(0,10)]
liste
n=int(input("n: "))
sözlük={i:i**2 for i in range(0,n+1)}
print(sözlük)

n=int(input("n: "))
sözlük={i:i**2 for i in range(0,n+1) if i<10}
print(sözlük)

sözlük={}
for i in range(0,n+1):
    if i<10:
        sözlük[i]=i**2
print(sözlük)    
#%%
A={"A":1,"B":2}
B={"C":3,"D":4}
C=A.copy()
C.update(B)
C
#%%
#list->set
#tuple->frozenset
A={1,2,3,4,5}
A.add(6)
A
A=frozenset(A)
A
type(A)
A.add(7)
B={4,5,6,7,8}
B=frozenset(B)
A-B
A&B
A|B
A.clear()
A=set(A)
B=set(B)
#%%dosya işlemleri
# w-> write
# r-> read, default
# a-> append
#r+ -> read and write
#write
dosya=open("deneme.txt","w")
dosya.write("İstanbul")
dosya.write("Ankara")
dosya.write("Çankırı")
dosya.close()


with open("deneme.txt") as dosya:
    #yapılacaklar
#%%
dosya=open("deneme.txt","w",encoding="utf-8")
dosya.write("İstanbul\n")
dosya.write("Ankara\n")
dosya.write("Çankırı\n")
dosya.close()
#%% read
dosya=open("deneme.txt","r",encoding="utf-8")
dosya.read()
dosya.tell()
dosya.seek(0)
dosya.seek(5)
dosya.seek(15)
dosya.readline()
dosya.readlines()
dosya.close()
#%% sona ekleme
dosya=open("deneme.txt","a",encoding="utf-8")
dosya.write("Kırşehir\n")
dosya.write("Kırıkkale\n")
dosya.close()
#%% başa ekleme
dosya=open("deneme.txt","r+",encoding="utf-8")
veri=dosya.read()
dosya.seek(0)#imleci başa alıyoruz...
dosya.write("Muğla\n"+veri)
dosya.close()
#%% ortaya ekleme
dosya=open("deneme.txt","r+",encoding="utf-8")
veri=dosya.readlines()
dosya.tell()
type(veri)
print(veri)
veri.insert(4,"İzmir\n")
dosya.seek(0)
dosya.writelines(veri)
dosya.close()


























