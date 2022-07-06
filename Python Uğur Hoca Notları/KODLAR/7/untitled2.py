# -*- coding: utf-8 -*-
seçilen="ankara"
ekran_çıktısı=[]
for i in range(0,len(seçilen)):
    ekran_çıktısı.append("_")
print(*ekran_çıktısı)
print(*seçilen)
seçim="a"
if seçim in seçilen:
    print("bildiniz")
else:
    print("bilemediniz")
from datetime import datetime
a=datetime.now()
type(a)
type(a.second)
print(a.minute)
a





#%%
