from PyQt5 import uic
dosya=open("anaSayfaUI.py","w",encoding="utf-8")
uic.compileUi("anaSayfa.ui",dosya)
dosya.close()