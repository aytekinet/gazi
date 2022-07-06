
#%% \ Ters Taksim
# \ kaçıs dizisi olası bir hatadan kaçmamızı saglar.
print('Bugün Ankara\'ya gidiyorum.')
print("Ahmet \"Ben geldim\" dedi.")    
print("Akşam oldu \
Hava karardı \
Yağmur yağıyor.")
#%% \n Satır Başı
#\n adlı kaçıs dizisi, bir alt satıra geçilmesini saglıyor.
print("Birinci satır \nikinci satır \nüçüncü satır")
başlık="Uğur Özcan"
print(başlık, "\n", len(başlık)*"-",sep="")
print("C:\nisan\masraf.txt")
print("C:\\nisan\\masraf.txt")
#%% \t Sekme-Tab
#\t adlı kaçıs dizisi, “abc” ifadesinden sonra sanki Tab (sekme) tusuna basılmıs gibi bir
#etki olusturarak “def” ifadesini saga dogru itiyor.
print("abc\tdef")
print("abc\t\tdef")
print(*"123456789", sep="\t")
print("C:\nisan\takvim.txt")
print("C:\\nisan\\takvim.txt")
#%% \a Zil Sesi
#!bip! benzeri bir zil sesi üretilmesini saglayabilir.
print("\a")
print("C:\nisan\aylar.txt")
print("C:\\nisan\\aylar.txt")
adı=input("adınız: \a")
#%% \r Aynı Satır Başı-insert
#Bu kaçıs dizisi, bir karakter dizisinde aynı satırın en basına dönülmesini saglar.
print("Öğreniyorum Python")
print("Öğreniyorum \rPython")
print("C:\nisan\ramazan.txt")
print("C:\\nisan\\ramazan.txt")
#%% \v Düşey Sekme-her işletim sisteminde çalışmıyor
#Eger \ isaretini ‘v’ harfiyle birlikte kullanırsak düsey sekme denen seyi elde ederiz.
#Yalnız bu \v adlı kaçıs dizisi her isletim sisteminde çalısmayabilir.
print("Düşey \vSekme")
print("C:\nisan\vergi.txt")
print("C:\\nisan\\vergi.txt")
#%% \b İmleç Kaydırma
#\b kaçıs dizisinin görevi, imleci o anki konumundan sola kaydırmaktır.
print("gazi.edu.\btr")
#%% \u Küçük Unicode
#UNICODE, karakterlerin, harflerin, sayıların ve bilgisayar ekranında gördügümüz
#öteki bütün isaretlerin her biri için tek ve benzersiz bir numaranın tanımlandıgı bir sistemdir.
#Bu sistemde, ‘kod konumu’ (code point ) adı verilen bu numaralar özel bir sekilde gösterilir.
print("Dosya Konumu: C:\users\Desktop\dosya.txt")
print("Dosya Konumu: C:\\users\\Desktop\\dosya.txt")
print("\u0131")
print("\u0061")
print("\u0055\u011F\u0075\u0072","\u00D6\u007A\u0063\u0061\u006E")
#%% \U Büyük Unicode
#Bu kaçıs dizisi \u adlı kaçıs dizisiyle hemen hemen aynı anlama gelir. 
#Bu kaçıs dizisi de, tıpkı \u gibi, UNICODE kod konumlarını temsil etmek için kullanılır.
#Ancak U ile gösterilen kod konumları u ile gösterilenlere göre biraz daha uzundur.
#burada \U kaçıs dizisinden sonra gelen kısım toplam 8 haneli bir sayıdan olusuyor.
print("Dosya Konumu: C:\Users\Desktop\dosya.txt")
print("Dosya Konumu: C:\\Users\\Desktop\\dosya.txt")
print("\U00000131")
print("\U00000061")
#%% \N Uzun Ad
#UNICODE sisteminde her karakterin tek ve benzersiz bir kod konumu oldugu gibi, tek ve
#benzersiz bir de uzun adı vardır.
#\u, \U ve \N kaçıs dizileri, UNICODE sistemi ile ilgili çalısmalar yapmak isteyen programcılar
#için Python programlama dilinin sundugu faydalı araçlardan yalnızca birkaçıdır.
import unicodedata
unicodedata.name("a")
unicodedata.name("A")
print("C:\Nisan")
print("C:\\Nisan")
#%% \x Onaltılı Karakter
#\x kaçıs dizisini kullanarak, onaltılı (hexadecimal ) sayma sistemindeki bir sayının karakter
#karsılıgını gösterebilirsiniz.
#Onaltılı sayma sistemindeki 41 sayısı ‘A’ har1ne karsılık gelir. Eger hangi karakterlerin
#hangi sayılara karsılık geldigini merak ediyorsanız http://www.ascii.cl/ adresindeki tabloyu
#inceleyebilirsiniz.
"\x41"
print("C:\Users\Ahmet\xp_dosyaları")
print("C:\\Users\\Ahmet\\xp_dosyaları")
#%% r Etkisizleştirme
#Aşağıdaki örnekte, \ isaretlerinin her birini çiftleyerek sorunun üstesinden geldik. 
#Ama bu sorunun üstesinden gelmenin çok daha basit ve pratik bir yolu var.
#Gördügünüz gibi, karakter dizisinin bas kısmının dıs tarafına bir adet r har1 yerlestirerek
#sorunun üstesinden geliyoruz. 
#Öteki kaçıs dizileri karakter dizisinin içinde yer alırken, bu kaçıs
#dizisi karakter dizisinin dısına yerlestiriliyor.
#Bu arada bu kaçıs dizisini, daha önce ögrendigimiz \r adlı kaçıs dizisi ile karıstırmamaya 
#dikkat ediyoruz.
print("Kurulum dizini: C:\aylar\nisan\toplam masraf")
print("Kurulum dizini: C:\\aylar\\nisan\\toplam masraf")
print(r"Kurulum dizini: C:\aylar\nisan\toplam masraf")
#%% Önemli Not: 
#Python’da karakter dizilerinin sonunda sadece çift sayıda \ isareti bulunabilir. Tek sayıda
#\ isareti kullanıldıgında karakter dizisini bitiren tırnak isareti etkisizlesecegi için çakısma
#sorunu ortaya çıkar. Bu etkisizlesmeyi, karakter dizisinin basına koydugunuz ‘r’ kaçıs dizisi
#de engelleyemez.
print("Kaçış dizisi: \") #hata verir
print(r"Kaçış dizisi: \") #hata verir
print("Kaçış dizisi: \ ") #hata vermez
print("Kaçış dizisi: \\") #hata vermez
#%% \f Sayfa Başı
#Bu kaçıs dizisinin görevi, bir sayfanın sona erip yeni bir sayfanın basladıgını göstermektir.
#Çok fazla kullanılmamaktadır. Eski yazıcıların sayfa başını anlaması için kullanılırdı.
#Bu kaçış dizisini görünce yazıcı yazmayı sonlandırıp, yeni sayfadan yazmaya başlar.
dosya=open("deneme.txt","w")
print("Sayfa Başı 1\fSayfa Başı 2",file=dosya)
dosya.close()







