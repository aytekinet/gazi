# -*- coding: utf-8 -*-
#--------Miras Alma---------
# Miras alma, nesne tabanlı programlamanın en önemli konularından birisidir.
# Nesne tabanlı programlamayı faydalı bir programlama yaklasımı haline getiren
# özelliklerin basında miras alma gelir.
# Python programlama dilinin temel felsefesi, bir kez yazılan kodları en
# verimli sekilde tekrar tekrar kullanabilmeye dayanır. ‘miras alma’ kavramı da
# kodların tekrar tekrar kullanılabilmesi felsefesine katkı sunan bir özelliktir.

class İşçi():
    def __init__(self,adıSoyadı,departman,maaş):
        self.adıSoyadı=adıSoyadı
        self.departman=departman
        self.maaş=maaş
    def yazdır(self):
        print("Adı Soyadı: "+self.adıSoyadı,"Departmanı: "+self.departman,"Maaş: "+str(self.maaş),sep="\n")
        print()

class Yönetici():
    def __init__(self,adıSoyadı,departman,maaş):
        self.adıSoyadı=adıSoyadı
        self.departman=departman
        self.maaş=maaş
    def yazdır(self):
        print("Adı Soyadı: "+self.adıSoyadı,"Departmanı: "+self.departman,"Maaş: "+str(self.maaş),sep="\n")
        print()

# Burada isçi ve yöneticinin her biri için ayrı bir sınıf tanımladık. Her
# sınıfın adı soyadı, departmanı ve maaş bilgisi var.

işçi1=İşçi("Uğur Özcan","Üretim",3500)
işçi1.yazdır()
yönetici1=Yönetici("Ali Can","Üretim",7000)
yönetici1.yazdır()

# Yukarıdaki kodları inceledigimizde, aynı kodların sürekli tekrarlandıgını
# görüyoruz. Aynı nitelik ve metotları her sınıf için yeniden tanımlıyoruz.
# Bu durumun Python’ın mantalitesine aykırıdır.
#%%
#---------------Taban Sınıflar-------------------
# Şimdi aşağıdaki kodları yazalım ve bütün sınıflarda ortak olan bu nitelik ve
# metotları tek bir sınıf altında toplayalım.

class Personel():
    def __init__(self,adıSoyadı,departman,maaş):
        self.adıSoyadı=adıSoyadı
        self.departman=departman
        self.maaş=maaş
    def yazdır(self):
        print("Adı Soyadı: "+self.adıSoyadı,"Departmanı: "+self.departman,"Maaş: "+str(self.maaş),sep="\n")
        print()

# Iste burada Personel() adlı sınıf, bir ‘taban sınıf’ olarak adlandırılır.
# Taban sınıf denen sey, birkaç farklı sınıfta ortak olan nitelik ve metotları
# barındıran bir sınıf türüdür. Ingilizcede "base class" olarak adlandırılan
# taban sınıflar, ayrıca üst sınıf (super class) veya ebeveyn sınıf (parent
# class) olarak da adlandırılır.
#%%
#---------------Alt Sınıflar-----------------
# Bir taban sınıftan türeyen bütün sınıflar, o taban sınıfın alt sınıflarıdır (subclass).
# Alt sınıflar, kendilerinden türedikleri taban sınıfların metot ve niteliklerini
# miras yoluyla devralır.
# Şimdi tanımladıgımız Personel() adlı taban sınıftan alt sınıflar türetelim:

class İşçi(Personel):
    pass

class Yönetici(Personel):
    pass

işçi1=İşçi("Uğur Özcan","Üretim",3500)
işçi1.yazdır()
yönetici1=Yönetici("Ali Can","Üretim",7000)
yönetici1.yazdır()

# Burada İşçi() ve Yönetici() sınıflarını tanımlarken, bu sınıfların
# parantezleri içine Personel sınıfının adını yazdıgımıza dikkat edin.
# Iste bu sekilde bir sınıfın parantezleri içinde baska bir sınıfın adını
# belirtirsek, o sınıf, parantez içinde belirttigimiz sınıfın bir alt sınıfı olmus olur.
# Bu sayede Personel() sınıfında tanımlanan bütün nitelik ve metotlara İşçi()
# ve Yönetici() sınıflarından da erisebiliyoruz.
# Iste bu mekanizmaya miras alma (inheritance) adı verilir.
#%%
#--------------Miras Alma Türleri--------------------
# Miras alma mekanizmasının isleyisi bakımından üç türden söz edebiliriz:
# 1. Miras alınan sınıfın bütün nitelik ve metotları alt sınıfa oldugu gibi devredilir.
# 2. Miras alınan sınıfın nitelik ve metotlarına ek olarak yeni nitelik ve metotlar alt sınıfta tanımlanır.
# 3. Miras alınan sınıfın bazı nitelik ve metotları alt sınıfta degisiklige ugratılır.
# Birincisini az önce yaptık. Yukarıdaki kodlarda Personel() sınıfının özellikleri
# olduğu gibi İşçi() ve Yönetici() sınıflarına devredildi.
# İkinci durum ile ilgili örneğin İşçi() sınıfına ek bir sınıf niteliği
# koyalım.

class İşçi(Personel):
    üretimBirimi="Montaj hattı"

işçi1=İşçi("Uğur Özcan","Üretim",3500)
işçi1.yazdır()
işçi1.üretimBirimi

# Burada İşçi() sınıfına üretimBirimi adlı bir sınıf niteligi eklemis olduk.
# Dolayısıyla İşçi() sınıfı, Personel() adlı taban sınıftan miras alınan bütün
# nitelik ve metotlarla birlikte bir de üretimBirimi niteligine sahip olmus oldu.
# Elbette, bu niteligi Yönetici() alt sınıfında tanımlamadıgımız için bu
# nitelik yalnızca İşçi() sınıfına özgüdür.
# Aynı sekilde, bir taban sınıftan türeyen bir alt sınıfa yeni bir sınıf metodu,
# örnek metodu veya statik metot da ekleyebiliriz. Bakınız örnek niteliği demedim.

class İşçi(Personel):
    üretimBirimi="Montaj hattı"
    def örnek_metodu(self):
        print("Örnek metodu")
    @classmethod
    def sınıf_metodu(cls):
        print("Sınıf metodu")
    @staticmethod
    def statik_metodu():
        print("Statik metodu")

işçi1=İşçi("Uğur Özcan","Üretim",3500)
işçi1.yazdır()
işçi1.üretimBirimi
işçi1.örnek_metodu()
işçi1.sınıf_metodu()
işçi1.statik_metodu()

# Dikkat etmemiz gereken bir baska kural sudur: Eger alt sınıfa eklenen herhangi
# bir nitelik veya metot taban sınıfta zaten varsa, alt sınıfa eklenen nitelik
# ve metotlar taban sınıftaki metot ve niteliklerin yerine geçer.

class İşçi(Personel):
    def yazdır(self):
        print("Ben alt sınıfın örnek niteliğiyim, alt sınıfta benim sözüm geçer.")
işçi1=İşçi("Uğur Özcan","Üretim",3500)
işçi1.yazdır()

# Eğer yeni bir örnek niteliği tanımlamak istersek ki biliyorsunuz __init__
# kullanmamız gerekecek.

class İşçi(Personel):
    def __init__(self):
        self.işeGiriş="01/01/2021"
işçi1=İşçi("Uğur Özcan","Üretim",3500)
işçi1.yazdır()

# Gördüğünüz gibi hata verdi. Çünkü alt sınıfın __init__ metodu taban sınıfın
# __init__ metodunun yerine geçti ve bütün örnek niteliklerini kaybettik.
# Belki problemi aşağıdaki gibi çözebiliriz.

class İşçi(Personel):
    def __init__(self,adıSoyadı,departman,maaş):
        self.adıSoyadı=adıSoyadı
        self.departman=departman
        self.maaş=maaş
        self.işeGiriş="01/01/2021"
işçi1=İşçi("Uğur Özcan","Üretim",3500)
işçi1.yazdır()
işçi1.işeGiriş

# Bu yaklaşım hiç pratik olmadı, çünkü kod tekrarı yapıyoruz.
#%%
#--------super() fonksiyonu---------------
# Miras alınan üst sınıfa atıfta bulunan super() fonksiyonu, miras aldıgımız
# bir üst sınıfın nitelik ve metotları üzerinde degisiklik yaparken, mevcut
# özellikleri de muhafaza edebilmemizi saglar.

class İşçi(Personel):
    def __init__(self,adıSoyadı,departman,maaş):
        super().__init__(adıSoyadı,departman,maaş)
        self.işeGiriş="01/01/2021"

işçi1=İşçi("Uğur Özcan","Üretim",3500)
işçi1.yazdır()
işçi1.işeGiriş

# super() fonksiyonu, miras alınan üst sınıfın __init__() metodu içindeki
# kodların, miras alan alt sınıfın __init__() metodu içine aktarılmasını saglıyor.
# Böylece hem taban sınıfın örnek niteliklerini korumus, hem de yeni bir örnek
# nitelik ekleme imkanı elde etmis oluyoruz.
# Bunu şöyle de yazabilirdik;

class İşçi(Personel):
    def __init__(self,adıSoyadı,departman,maaş):
        Personel.__init__(self,adıSoyadı,departman,maaş) # self'e dikkat edelim.
        self.işeGiriş="01/01/2021"

işçi1=İşçi("Uğur Özcan","Üretim",3500)
işçi1.yazdır()
işçi1.işeGiriş

# Uzun uzun örnek niteliklerini yazmamak için aynı işi aşağıdaki gibi de yapabiliriz.

class İşçi(Personel):
    def __init__(self,*args):
        super().__init__(*args)
        self.işeGiriş="01/01/2021"

işçi1=İşçi("Uğur Özcan","Üretim",3500)
işçi1.yazdır()
işçi1.işeGiriş

# Bildiginiz gibi, *args bir fonksiyonun bütün konumlu (positional) argümanlarını,
# parametrelerin parantez içinde geçtigi sırayı dikkate alarak bir demet içinde
# toplar. Iste yukarıda da bu özellikten faydalanıyoruz. Eger taban sınıfta
# isimli (keyword) argümanlar da olsaydı, o zaman **kwargs kullanırdık. Ama
# kodları aşağıdaki gibi de yazabiliriz.

class İşçi(Personel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.işeGiriş="01/01/2021"

işçi1=İşçi("Uğur Özcan","Üretim",3500)
işçi1.yazdır()
işçi1.işeGiriş

# Not olarak, super() fonksiyonunu yalnızca __init__() fonksiyonu içinde
# kullanmak zorunda degiliz. Bu fonksiyonu diğer metodlar içinde de kullanabiliriz.
# Örneğin az önceki yazdır() örnek metodu gibi.

class İşçi(Personel):
    def yazdır(self):
        super().yazdır()
        print("""Ben alt sınıfın örnek niteliğiyim, alt sınıfta benim sözüm geçer,
              diyordum ki tam olarak öyle değilmiş.""")

işçi1=İşçi("Uğur Özcan","Üretim",3500)
işçi1.yazdır()
#%%
#------------------object sınıfı--------------------
# Sınıflar aşağıdaki gibi tanımlanabilir.

class Sınıf:
    pass

class Sınıf():
    pass

# Fakat bazı kodlarda aşağıdaki gibi tanımlanmış sınıflar göreceksiniz. Bu sınıflar
# Python 2'deki yeni sınıf kavramından geliyor. Python 3 ile ilgisi yok, fakat
# Python 3'te bu şekilde de sınıf tanımı yapılabilir.

class Sınıf(object):
    pass
#%%
#--------------Çoklu Miras Alma------------
# Python’da bir sınıf, aynı anda birden fazla sınıfı da miras alabilir.
# Bu mekanizmaya Python’da çoklu miras alma (multiple inheritance) denir.

class Toplama():
    def topla(self):
        return self.a+self.b

class Çıkarma():
    def çıkar(self):
        return self.a-self.b

class Çarpma():
    def çarp(self):
        return self.a*self.b

class Bölme():
    def böl(self):
        return self.a/self.b

class HesapMakinesi(Toplama,Çıkarma,Çarpma,Bölme):
    def __init__(self,a,b):
        self.a=a
        self.b=b

işlem1=HesapMakinesi(3,5)
işlem1.topla()
işlem1.çıkar()
işlem1.çarp()
işlem1.böl()

# Tek bir sınıfı miras aldıgınızda hangi kurallar geçerliyse, birden fazla
# sınıfı miras aldıgınızda da temel olarak aynı kurallar geçerlidir.
# Ancak çoklu miras almada birden fazla sınıf söz konusu oldugu için, miras
# alınan sınıfların da kendi aralarında veya baska sınıflarla nitelik ve/veya
# metot alısverisi yapması halinde ortaya çıkabilecek beklenmedik durumlara
# karsı dikkatli olmalısınız. Ayrıca çoklu miras alma islemi sırasında, aynı
# adı tasıyan metotlardan yalnızca birinin miras alınacagını da unutmayın.
# Miras alma listesinde hangi sınıf önde geliyorsa onun özellikleri miras alınacaktır.

class TabanSınıfBir():
    sınıfNiteliği="TabanSınıfBir'den gelen sınıfNiteliği"
    def __init__(self):
        self.örnekNiteliği="TabanSınıfBir'den gelen örnekNiteliği"
    def örnekMetodu(self):
        print("TabanSınıfBir'den gelen örnekMetodu")

class TabanSınıfİki():
    sınıfNiteliği="TabanSınıfİki'den gelen sınıfNiteliği"
    def __init__(self):
        self.örnekNiteliği="TabanSınıfİki'den gelen örnekNiteliği"
    def örnekMetodu(self):
        print("TabanSınıfİki'den gelen örnekMetodu")

class TabanSınıfÜç():
    sınıfNiteliği="TabanSınıfÜç'den gelen sınıfNiteliği"
    def __init__(self):
        self.örnekNiteliği="TabanSınıfÜç'den gelen örnekNiteliği"
    def örnekMetodu(self):
        print("TabanSınıfÜç'den gelen örnekMetodu")

class AltSınıf(TabanSınıfBir,TabanSınıfİki,TabanSınıfÜç):
    pass

obj=AltSınıf()
obj.sınıfNiteliği
obj.örnekNiteliği
obj.örnekMetodu()

# Veya bu önceliği kendiniz de belirleyebilirsiniz.

class AltSınıf(TabanSınıfBir,TabanSınıfİki,TabanSınıfÜç):
    sınıfNiteliği=TabanSınıfÜç.sınıfNiteliği #Dahil etme var burada aşağıdaki konu
    def __init__(self):
        TabanSınıfİki.__init__(self)
    def örnekMetodu(self):
        TabanSınıfÜç.örnekMetodu(self)

obj=AltSınıf()
obj.sınıfNiteliği
obj.örnekNiteliği
obj.örnekMetodu()
#%%
#-------------Dahil Etme-----------------
# Bir sınıftaki nitelik ve metotları baska bir sınıf içinde kullanmanın tek yolu
# ilgili sınıf veya sınıfları miras almak degildir. Hatta bazı durumlarda,
# miras alma iyi bir yöntem dahi olmayabilir. Özellikle birden fazla sınıfa ait
# nitelik ve metotlara ihtiyaç duydugumuzda, çoklu miras alma yöntemini
# kullanmak yerine, dahil etme (composition) denen yöntemi tercih edebiliriz.
# Miras alma ve dahil etme yöntemleri arasında tercih yaparken genel
# yaklasımımız su olacak: Eger yazdıgımız uygulama, bir baska sınıfın türevi
# ise, o sınıfı miras alacagız. Ama eger bir sınıf, yazdıgımız uygulamanın bir
# parçası ise o sınıfı uygulamamıza dahil edecegiz.

class TabanSınıfBir():
    sınıfNiteliği="TabanSınıfBir'den gelen sınıfNiteliği"
    def __init__(self):
        self.örnekNiteliği="TabanSınıfBir'den gelen örnekNiteliği"
    def örnekMetodu(self):
        return ("TabanSınıfBir'den gelen örnekMetodu")

class TabanSınıfİki():
    sınıfNiteliği="TabanSınıfİki'den gelen sınıfNiteliği"
    def __init__(self):
        self.örnekNiteliği="TabanSınıfİki'den gelen örnekNiteliği"
    def örnekMetodu(self):
        return ("TabanSınıfİki'den gelen örnekMetodu")

class TabanSınıfÜç():
    sınıfNiteliği="TabanSınıfÜç'den gelen sınıfNiteliği"
    def __init__(self):
        self.örnekNiteliği="TabanSınıfÜç'den gelen örnekNiteliği"
    def örnekMetodu(self):
        return ("TabanSınıfÜç'den gelen örnekMetodu")

class DahilEtmeSınıfı(): # Parantez içerisinde sınıf belirtmiyoruz.
    dahil1=TabanSınıfÜç.sınıfNiteliği
    def __init__(self):
        self.dahil2=TabanSınıfBir.__init__(self)
        self.dahil3=TabanSınıfİki.örnekMetodu(self)
        self.dahil4=TabanSınıfÜç.örnekMetodu(self)

obj=DahilEtmeSınıfı()
obj.dahil1
obj.dahil2
obj.örnekNiteliği
obj.dahil3
obj.dahil4
#%%
#----------------Taban Sınıf ve Alt Sınıflar Hiyerarşisi---------------

class TabanSınıf_0(): # Seviye 0
    s0_sınıfNiteliğiMutable=["s0_sınıfNiteliğiMutable"]
    s0_sınıfNiteliğiImmutable="s0_sınıfNiteliğiImmutabel"
    def __init__(self):
        self.s0_örnekNiteliğiMutable=["s0_örnekNiteliğiMutable"]
        self.s0_örnekNiteliğiImmutable="s0_örnekNiteliğiImmutabel"

class AltSınıf_01(TabanSınıf_0): # Seviye 1
    pass

obj=AltSınıf_01()
obj.s0_sınıfNiteliğiMutable
obj.s0_sınıfNiteliğiImmutable
obj.s0_örnekNiteliğiMutable
obj.s0_örnekNiteliğiImmutable

# Miras almayı tamamladık. Şimdi taban sınıf niteliklerini değiştirelim.

TabanSınıf_0().s0_sınıfNiteliğiMutable.append("tabanSınıfaYeniSınıfNiteliğiEklendi")
TabanSınıf_0().s0_sınıfNiteliğiImmutable="tabanSınıfınSınıfNiteliğiDeğiştirildi"
TabanSınıf_0().s0_örnekNiteliğiMutable.append("tabanSınıfaYeniÖrnekNiteliğiEklendi")
TabanSınıf_0().s0_örnekNiteliğiImmutable="tabanSınıfınÖrnekNiteliğiDeğiştirildi"

# Değişimleri yaptık, şimdi alt sınıf etkilenmiş mi kontrol edelim.

obj=AltSınıf_01()
obj.s0_sınıfNiteliğiMutable # Değişti
obj.s0_sınıfNiteliğiImmutable # Değişmedi
obj.s0_örnekNiteliğiMutable # Değişmedi
obj.s0_örnekNiteliğiImmutable # Değişmedi

# Gördüğünüz gibi sadece sınıf niteliklerinden mutable değişkenler etkileniyor.
# Çünkü taban sınıfın örneğini değiştiriyoruz.
# Şimdi burayı geçip sadece TabanSınıf_0() ve AltSınıf_01()'i ele alalım tekrar.
# Yeni bir alt sınıf tanımlıyorum, ama AltSınıf_01()'den miras alacak.

class AltSınıf_011(AltSınıf_01): # Seviye 3
    pass

obj=AltSınıf_011()
obj.s0_sınıfNiteliğiMutable
obj.s0_sınıfNiteliğiImmutable
obj.s0_örnekNiteliğiMutable
obj.s0_örnekNiteliğiImmutable

# Peki, AltSınıf_01()'in örnek niteliklerinden birini değiştirelim

class AltSınıf_01(TabanSınıf_0):
    def __init__(self):
        super().__init__()
        self.s0_örnekNiteliğiImmutable="s01_örnekNiteliğiImmutabel"

class AltSınıf_011(AltSınıf_01):
    pass

obj=AltSınıf_011()
obj.s0_sınıfNiteliğiMutable
obj.s0_sınıfNiteliğiImmutable
obj.s0_örnekNiteliğiMutable
obj.s0_örnekNiteliğiImmutable

# Gördüğünüz gibi sınıflar hiyerarşisinde bir alt sınıf hemen bir üst sınıfın
# özelliklerini alıyor.
# Not: Python’daki bütün sınıflar, eger baska bir sınıfı miras olarak
# almıyorlarsa, otomatik olarak object sınıfını miras alırlar.

class Sınıf():
    pass

class Sınıf:
    pass

class Sınıf(object):
    pass

# Sınıf tanımlamadan hatırlayacağınız üzere hepsi aynı işi yapar, ilk ikisinde
# otomatik olarak object sınıfı miras alınır.
#%%
# __str__
# Nesnenin okunabilir çıktısını vermede kullanılır

class İşçi():
    def __init__(self,adıSoyadı,departman,maaş):
        self.adıSoyadı=adıSoyadı
        self.departman=departman
        self.maaş=maaş

İşçi1=İşçi("Uğur Özcan","Üretim",4000)
print(İşçi1)

class İşçi():
    def __init__(self,adıSoyadı,departman,maaş):
        self.adıSoyadı=adıSoyadı
        self.departman=departman
        self.maaş=maaş
    def __str__(self):
        return "Adı Soyadı: "+self.adıSoyadı+" Departmanı: "+self.departman+" Maaş: "+str(self.maaş)

İşçi1=İşçi("Uğur Özcan","Üretim",4000)
print(İşçi1)