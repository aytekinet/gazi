# -*- coding: utf-8 -*-
liste=[["ali","78"],["veli","99"],["ayşe","99"]]
sözlük={liste[i][0]:int(liste[i][1]) 
        for i in range(0,len(liste))}
sözlük
birinci=max(sözlük.values())
birinciler=""
for i,j in sözlük.items():
    if j==birinci:
        birinciler=birinciler+i+","
print(birinciler)
#%%
sözlük={"elma":"apple","muz":"banana"}
sözlük.keys()
sözlük.values()
sözlük.items()
len(sözlük)
#%%
class Hesaplama():
    def topla(self):
        self.a=int(input("a: "))
        self.b=int(input("b: "))
        print(self.a+self.b)
    def çıkar(self):
        print(self.a-self.b)

hesap1=Hesaplama()
hesap1.topla()
hesap1.çıkar()
#%%
sayı=1.4578787
print(round(sayı,2))
sayı1=1245457815454
print(round(sayı1,-5))
#%%
class Deneme():
    sınıf="sınıf tanımlama aşamasında çalışır"
    print(sınıf)
    def __init__(self):
        print("Örneklendirmede çalışır")
örnek=Deneme()
#%%
def Fonk(a,b,c):
    return sum([a,b,c])
print(Fonk(1,2,3))

def fonk(*args):
    return sum(args)
print(fonk(1,2,3,4,5,8,9))

#%%

def fonk(*args,**kwargs):
    for i,j in kwargs.items():
        print(i)
        print(j)
    print(sum(kwargs.values()))
    
print(fonk(a=1,b=4,c=7))
#print(fonk(1,2,3,4,5,8,9))



















