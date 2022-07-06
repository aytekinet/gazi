# -*- coding: utf-8 -*-
class XOX():
    import random
    import sys
    import os
    import pyfiglet
    tht=[1,2,3,4,5,6,7,8,9]
    b_tht=[1,2,3,4,5,6,7,8,9]
    def __init__(self,adınız):
        self.oyuncu_X=adınız
        self.oyuncu_O="Bilgisayar"
        self.sıra="X"
        self.başla()
    def banner(self):
        print(self.pyfiglet.figlet_format("X O X"))
    def tahta(self):
        self.banner()
        print(""" 
              _{6}_|_{7}_|_{8}_
              _{3}_|_{4}_|_{5}_
               {0} | {1} | {2}
              """.format(self.tht[0],
                         self.tht[1],
                         self.tht[2],
                         self.tht[3],
                         self.tht[4],
                         self.tht[5],
                         self.tht[6],
                         self.tht[7],
                         self.tht[8]))
    def başla(self):
        if self.sıra=="X":
            print(f"{self.oyuncu_X} sıra sende")
            while True:
                self.tahta()
                seç=input("Seçimin: ")
                try:
                    seç=int(seç)
                    if seç not in self.b_tht:
                        raise TypeError()
                    self.tht[seç-1]="X"
                    self.b_tht.pop(self.b_tht.index(seç))
                    break
                except TypeError:
                    print("Orası oynandı veya 1-9 arası...")
                except:
                    print("Tekrar deneyiniz...")
        else:
            print(f"{self.oyuncu_O} sıra sende")
            indeks=self.random.randint(0, len(self.b_tht)-1)
            seç=self.b_tht[indeks]
            self.tht[seç-1]="O"
            self.b_tht.pop(indeks)
        self.kontrol()    

            
    
    def kontrol(self):
        if self.tht[0]==self.tht[1] and self.tht[1]==self.tht[2]:
            self.kazanan()
        elif self.tht[3]==self.tht[4] and self.tht[4]==self.tht[5]:
            self.kazanan()
        elif self.tht[6]==self.tht[7] and self.tht[7]==self.tht[8]:
            self.kazanan()
        elif self.tht[0]==self.tht[3] and self.tht[3]==self.tht[6]:
            self.kazanan()
        elif self.tht[1]==self.tht[4] and self.tht[4]==self.tht[7]:
            self.kazanan()
        elif self.tht[2]==self.tht[5] and self.tht[5]==self.tht[8]:
            self.kazanan()
        elif self.tht[0]==self.tht[4] and self.tht[4]==self.tht[8]:
            self.kazanan()
        elif self.tht[2]==self.tht[4] and self.tht[4]==self.tht[6]:
            self.kazanan()
        if self.b_tht==[]:
            self.berabere()
        
        if self.sıra=="X":
            self.sıra="O"
            self.os.system("cls")
        else:
            self.sıra="X"
            self.os.system("cls")
        self.başla()
    
    def kazanan(self):
        self.tahta()
        if self.sıra=="X":
            print(f"Tebrikler {self.oyuncu_X} kazandın")
        else:
            print(f"Malesef {self.oyuncu_O} kazandı")
        self.çıkış()
    def berabere(self):
        self.tahta()
        print("Berabere bitti...")
        self.çıkış()
    
    def çıkış(self):
        soru=input("Tekrar oynamak ister misin? E/h: ")
        if soru=="h":
            print("Oyun sona erdi...")
            self.sys.exit()
        else:
            self.tht=[1,2,3,4,5,6,7,8,9]
            self.b_tht=[1,2,3,4,5,6,7,8,9] 
            self.sıra="X"
            self.başla()
oyun1=XOX("Uğur")    
    
    
    
    