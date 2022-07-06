# mouse pozisyonunu bulmak için;
# cmd üzerinden sırasıyla;
# import pyautogui
# pyautogui.displayMousePosition()
# buradan x ve y koordinatları anlık okunabilir...

import pyautogui as pa # kütüphane çağır
import random # kütüphane çağır
pa.click(1809,15,duration=1) #spyderı kapat
pa.click(765,1056,duration=1) # başlatı aç
pa.click(910,633,duration=1) # not defteri aç

pa.write("Merhaba Python", interval=0.5) # yazıyı yaz
pa.click(1507,161,duration=1) # not defrerini kapat
for i in range(0,10): # 10 adet döngü için
    X=random.randint(0,1920) # x i rastgele belirle
    Y=random.randint(0,1080) # y i rastgele belirle
    pa.doubleClick(X,Y,duration=0.2) # bu koordinatlara çift klikleme yap
