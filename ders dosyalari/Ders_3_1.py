# -*- coding: utf-8 -*-
#%%
if koşul:
    yapılacakları
if blogu sona erdi



#%%
kullanıcıGırısı=input("Değer giriniz: ")
if kullanıcıGırısı=="a":
    print("Şart 1 sağlandı...")
if kullanıcıGırısı=="1":
    print("Şart 2 sağlandı...")
print("Program çalışmaya devam ediyor...")
#%%
user=input("Kullanıcı adı: ")
password=input("Parolanız nedir: ")
print(user=="admin" and password=="12345")
#%%
yaş=input("Yaşınız: ")
if int(yaş)>=18:
    print("Oy kullanabilirsiniz...")
#%%
yaş=int(input("Yaşınız: "))
if yaş>=18:
    print("Oy kullanabilirsiniz...")
#%%
password=input("Parolanız: ")
#input bize str değer verir.
a="ali"
b="23"
b
type(b)
c=int(a)
d=int(b)
d
type(d)
print(d)
print(d/5)
type(d/5)


e="7.5"
f=float(e)
f
f/2
g=int(f)
g
g/8

#%%
user=input("kullanıcı: ")
password=input("parola: ")
kullanıcı="admin"
parola="1234"
if user==kullanıcı and password==parola:
    print("Giriş Başarılı...")
""
''
[]
{}
(kullanıcı,)

#%%
abc=60
if abc>90:
    print("90'dan büyük")
    if abc%5==0:
        print("5'e de bölünüyor")
        if abc//8==12:
            print("bölümü de 12")
        print("3. iften çıktık")
    print("2. if")
print("1. if")
#%%
user=input("kullanıcı: ")
password=input("parola: ")
kullanıcı="admin"
parola="1234"
if user==kullanıcı:
    if password==parola:
        print("Giriş Başarılı...")
#%%
if koşul:
    true yapılacaklar
else:
    false yapılacaklar
#%%
#sayı=100
#sayı=90
#sayı="ali"
#sayı=[1234,12345]
if sayı>=100:
    print("sayı 100'den büyük-eşit")
else:
    print("diğer durumlar...")
#%%
sayı=78 
if sayı%2==0:
    print("çift")
else:
    print("tek")
#%%
sinavPuanı=98
'''
sinavPuani >= 85 ise 'Pek iyi'
70 <= sinavPuani < 85 ise 'İyi'
55 <= sinavPuani < 70 ise 'Orta'
45 <= sinavPuani < 55 ise 'Geçer'
0 <= sinavPuani < 45 ise 'Kaldı'
'''
if sinavPuanı>=85:
    print("Pekiyi")
elif sinavPuanı>=70:
    print("İyi")
elif sinavPuanı>=55:
    print("Orta")
elif sinavPuanı>=45:
    print("Geçer")
else:
    print("Kaldı")
    
#%%
sayı=int(input("Sayı: "))
'''
if sayı>0:
    print("Pozitif")
elif sayı<0:
    print("Negatif")
else:
    print("Sıfırdır")
'''
if sayı>=0:
    print("Pozitif")
else:
    print("Negatif")

#%%
'''
Kitle Endeksi (KE) < 18.5 ise Zayıf,
18.5 < (KE) <=25 ise Normal,
25 < (KE) <= 30 ise Kilolu, 
(KE) > 30 ise birey obez sınıfına girmektedir.
'''
boy=float(input("Boy (metre): "))
kilo=int(input("Kilo (kg): "))
KE=kilo/boy**2
if KE>30:
    print("Obez")
elif KE>25:
    print("Kilolu")
elif KE>18.5:
    print("Normal")
else:
    print("Zayıf")
#%%
a=int(input("Kenar 1: "))
b=int(input("Kenar 2: "))
c=int(input("Kenar 3: "))

if a==b and b==c:
    print("Eşkenar Üçgen")
elif a==b or a==c or b==c:
    print("ikizkenar üçgen")
else:
    print("Çeşitkenar")

#%%birinci yol
a=int(input("Sayı 1: "))
b=int(input("Sayı 2: "))
c=int(input("Sayı 3: "))

if (a>b and a<c) or (a<b and a>c):
    print(a)
elif (b>a and b<c) or (b<a and b>c):
    print(b)
else:
    print(c)

#%% ikinci yol
a=int(input("Sayı 1: "))
b=int(input("Sayı 2: "))
c=int(input("Sayı 3: "))

if a>b>c or c>b>a:
    print(b)
elif b>a>c or c>a>b:
    print(a)
else:
    print(c)




























