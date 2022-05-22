# -*- coding: utf-8 -*-
# birinci yol
liste=[4,1,5,7,6,9,3,2,8]
print(liste)
for _ in range(0,len(liste)):
    for i in range(0,len(liste)-1):
        if liste[i]>liste[i+1]:
            liste[i],liste[i+1]=liste[i+1],liste[i]
    print(liste)        
#print(liste)            
#%% ikinci yol
liste=[4,1,5,7,6,9,3,2,8]
küçük=[]
uzunluk=len(liste)
for _ in range(0,uzunluk):
    minimum=10
    for j in range(0,len(liste)):
        if minimum>liste[j]:
            minimum=liste[j]
    küçük.append(minimum)
    liste.remove(minimum)
print(küçük)

            
            