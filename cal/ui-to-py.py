from PyQt5 import uic 

dosya=open("cal.py","w", encoding="utf-8")
uic.compileUi("cal_ui.ui", dosya)
dosya.close()