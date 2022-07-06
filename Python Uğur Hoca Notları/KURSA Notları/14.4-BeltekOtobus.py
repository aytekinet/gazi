# -*- coding: utf-8 -*-
# Otobüs Firması
# Nesneleri sefer sayısı olarak tanımlayacağız.
class Beltek(): # Otobüs firması
    #seferler=[]
    def __init__(self,nereden,nereye,süre,kapasite):
        self._nereden=nereden
        self.nereye=nereye
        self.süre=süre
        self.kapasite=kapasite
        self.yolcu_sayısı=0
        self.koltuk=[i for i in range(1,self.kapasite+1)]
        self.__yolcuAdı=[]
        self.__yolcuSoyadı=[]
        self.__TCKN=[]
        self.__koltukNo=[]
        self.sefer=[]
        self.sefer_ekle()
    def bilet_satış(self,adı,soyadı,TCKNo,koltuk_no):
        if koltuk_no not in self.koltuk:
            print("Koltuk Doludur. Başka Seçiniz...")
        else:
            self.yolcu_sayısı+=1
            self.sefer[0][4]=self.yolcu_sayısı
            self.koltuk.remove(koltuk_no)
            self.__yolcuAdı.append(adı)
            self.__yolcuSoyadı.append(soyadı)
            self.__TCKN.append(TCKNo)
            self.__koltukNo.append(koltuk_no)
    def bilet_iptal(self,koltuknum):        
        indeks=self.__koltukNo.index(koltuknum)
        self.__yolcuAdı.pop(indeks)
        self.__yolcuSoyadı.pop(indeks)
        self.__TCKN.pop(indeks)
        self.__koltukNo.remove(koltuknum)
        self.koltuk.insert(koltuknum-1,koltuknum)
        self.yolcu_sayısı-=1
        self.sefer[0][4]=self.yolcu_sayısı
    def yolcu_listele(self):
        for i in range(0,len(self.__TCKN)):
            print(str(self.__yolcuAdı[i])+" "+str(self.__yolcuSoyadı[i])+" "+str(self.__TCKN[i])+" "+str(self.__koltukNo[i]))
    def sefer_ekle(self):
        self.sefer.append([self._nereden,self.nereye,self.süre,self.kapasite,self.yolcu_sayısı])
    #@classmethod
    def sefer_listele(self):
        print(self.sefer)
    def boş_koltuklar(self):
        print(self.koltuk)
    @property
    def neredenn(self):
        return self._nereden
    @neredenn.setter
    def neredenn(self,yeni_nereden):
        self._nereden=yeni_nereden
        self.sefer[0][0]=yeni_nereden
    @neredenn.deleter
    def neredenn(self):
        self.sefer[0][0]=""
        del self._nereden

    
    
#dir(Beltek)        
SS01=Beltek("Ankara","İzmir","6 saat",50)        
SS01.sefer_listele()  
SS01.neredenn="İstanbul"
del SS01.neredenn

              
SS01.yolcu_listele()            
SS01.bilet_satış("Uğur","Özcan","78569874211",40)            
SS01.sefer_listele()                
SS01.yolcu_listele()            
SS01.bilet_satış("Ali","Can","11223334455",2)            
SS01.boş_koltuklar()            
SS01.bilet_iptal(40)            
SS01._Beltek__yolcuAdı
#%%
class Sınıf(): # Ben bir sınıfım
    sınıfNiteliği=[] #Ben sınıf niteliğiyim
    __gizliÜye=[] #Ben gizli üye
    __gizliÜye_=[] #Ben de gizli üye
    _yarıGizli=[]#ben yarı gizli üyeyim
    def __init__(self,params,__gizliParams,yarıGizliparams,tanımlıParam=0): #Ben sınıf bir nesneye atabndığında yapılacakları otomatik yaparım
        print("Yapılacaklar")
        self.örnekNiteliği=[] #ben tanımlı örnek niteliği
        self.params=params#ben kullanıcı tanımlı örnek niteliği
        self.__gizliParams=__gizliParams #ben gizli parametreyim
        self._yarıGizliparams=yarıGizliparams #ben yarı gizli parametre
        self.örnekMetodu() #Ben başlangıçta çalışmak için burada çağrıldım
    def örnekMetodu(self,örnekParams=0): #ben örnek metoduyum
        örnekParams=1 #ben örnek metodu parametresi sadece burada tanımlıyım
        print("örnek metodu işlevleri")
    def __gizliÖrnekMetodu(self):
        print("gizli yapılacak işler")
    @classmethod
    def sınıfMetodu(cls): #ben sınıf metodu cls ile çalışırım, sınıf niteliklerini değiştiririm
        print(cls.sınıfNiteliği)
    @staticmethod
    def statikMetodu(): # bir şeye karışmam sadece yapılması gerekeni yaparım
        return 22/7
    @property # ben bir örnek metodunu örnek niteliğine dönüştürüm
    def örnekNite(self):
        return self._yarıGizliparams
    @örnekNite.setter #ben örnek niteliğinde tanımlanan değişiklikleri yaparım
    def örnekNite(self):
        print("dönüşüm işlemleri")
    @örnekNite.deleter #örnek niteliği silerim
    def örnekNite(self):
        del self._yarıGizliparams
















