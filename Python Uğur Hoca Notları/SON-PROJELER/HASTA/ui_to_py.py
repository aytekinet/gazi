from PyQt5 import uic
dosya=open("hastaUI.py","w",encoding="utf-8")
uic.compileUi("hastaUI.ui",dosya)
dosya.close()