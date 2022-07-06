# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'otelUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1022, 655)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(590, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(590, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lstPansiyon = QtWidgets.QListWidget(self.centralwidget)
        self.lstPansiyon.setGeometry(QtCore.QRect(590, 60, 121, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lstPansiyon.setFont(font)
        self.lstPansiyon.setObjectName("lstPansiyon")
        item = QtWidgets.QListWidgetItem()
        self.lstPansiyon.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstPansiyon.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstPansiyon.addItem(item)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(630, 200, 101, 71))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.rdKadin = QtWidgets.QRadioButton(self.groupBox)
        self.rdKadin.setGeometry(QtCore.QRect(10, 11, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdKadin.setFont(font)
        self.rdKadin.setObjectName("rdKadin")
        self.rdErkek = QtWidgets.QRadioButton(self.groupBox)
        self.rdErkek.setGeometry(QtCore.QRect(10, 41, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdErkek.setFont(font)
        self.rdErkek.setObjectName("rdErkek")
        self.tblWKayitlar = QtWidgets.QTableWidget(self.centralwidget)
        self.tblWKayitlar.setGeometry(QtCore.QRect(10, 300, 1001, 261))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tblWKayitlar.setFont(font)
        self.tblWKayitlar.setRowCount(50)
        self.tblWKayitlar.setColumnCount(12)
        self.tblWKayitlar.setObjectName("tblWKayitlar")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 570, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lblMisafirSayisi = QtWidgets.QLabel(self.centralwidget)
        self.lblMisafirSayisi.setGeometry(QtCore.QRect(150, 570, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblMisafirSayisi.setFont(font)
        self.lblMisafirSayisi.setObjectName("lblMisafirSayisi")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 322, 262))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lneTC = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lneTC.setFont(font)
        self.lneTC.setObjectName("lneTC")
        self.horizontalLayout.addWidget(self.lneTC)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lneAdi = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lneAdi.setFont(font)
        self.lneAdi.setObjectName("lneAdi")
        self.horizontalLayout_2.addWidget(self.lneAdi)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lneSoyadi = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lneSoyadi.setFont(font)
        self.lneSoyadi.setObjectName("lneSoyadi")
        self.horizontalLayout_3.addWidget(self.lneSoyadi)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.cmbOdaTipi = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cmbOdaTipi.setFont(font)
        self.cmbOdaTipi.setObjectName("cmbOdaTipi")
        self.cmbOdaTipi.addItem("")
        self.cmbOdaTipi.addItem("")
        self.cmbOdaTipi.addItem("")
        self.horizontalLayout_4.addWidget(self.cmbOdaTipi)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.spnGunSayisi = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spnGunSayisi.setFont(font)
        self.spnGunSayisi.setMinimum(1)
        self.spnGunSayisi.setMaximum(100)
        self.spnGunSayisi.setSingleStep(1)
        self.spnGunSayisi.setProperty("value", 1)
        self.spnGunSayisi.setObjectName("spnGunSayisi")
        self.horizontalLayout_5.addWidget(self.spnGunSayisi)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.lblUcret = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblUcret.setFont(font)
        self.lblUcret.setObjectName("lblUcret")
        self.horizontalLayout_6.addWidget(self.lblUcret)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.spnCocukSayisi = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spnCocukSayisi.setFont(font)
        self.spnCocukSayisi.setMaximum(10)
        self.spnCocukSayisi.setObjectName("spnCocukSayisi")
        self.horizontalLayout_7.addWidget(self.spnCocukSayisi)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(790, 10, 95, 281))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnKaydet = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnKaydet.setObjectName("btnKaydet")
        self.verticalLayout_2.addWidget(self.btnKaydet)
        self.btnSil = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnSil.setObjectName("btnSil")
        self.verticalLayout_2.addWidget(self.btnSil)
        self.btnGuncelle = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnGuncelle.setObjectName("btnGuncelle")
        self.verticalLayout_2.addWidget(self.btnGuncelle)
        self.btnBul = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnBul.setObjectName("btnBul")
        self.verticalLayout_2.addWidget(self.btnBul)
        self.btnTemizle = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnTemizle.setObjectName("btnTemizle")
        self.verticalLayout_2.addWidget(self.btnTemizle)
        self.btnListele = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnListele.setObjectName("btnListele")
        self.verticalLayout_2.addWidget(self.btnListele)
        self.btnCikis = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnCikis.setObjectName("btnCikis")
        self.verticalLayout_2.addWidget(self.btnCikis)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(340, 20, 233, 32))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.dateGiris = QtWidgets.QDateEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateGiris.setFont(font)
        self.dateGiris.setObjectName("dateGiris")
        self.horizontalLayout_8.addWidget(self.dateGiris)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(340, 70, 235, 32))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.dateCikis = QtWidgets.QDateEdit(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateCikis.setFont(font)
        self.dateCikis.setObjectName("dateCikis")
        self.horizontalLayout_9.addWidget(self.dateCikis)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1022, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuHakkinda = QtWidgets.QAction(MainWindow)
        self.menuHakkinda.setObjectName("menuHakkinda")
        self.menuCikis = QtWidgets.QAction(MainWindow)
        self.menuCikis.setObjectName("menuCikis")
        self.menuMenu.addAction(self.menuHakkinda)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.menuCikis)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.cmbOdaTipi.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Pansiyon"))
        self.label_10.setText(_translate("MainWindow", "Cinsiyet"))
        __sortingEnabled = self.lstPansiyon.isSortingEnabled()
        self.lstPansiyon.setSortingEnabled(False)
        item = self.lstPansiyon.item(0)
        item.setText(_translate("MainWindow", "Yarım"))
        item = self.lstPansiyon.item(1)
        item.setText(_translate("MainWindow", "Tam"))
        item = self.lstPansiyon.item(2)
        item.setText(_translate("MainWindow", "Herşey Dahil"))
        self.lstPansiyon.setSortingEnabled(__sortingEnabled)
        self.rdKadin.setText(_translate("MainWindow", "Kadın"))
        self.rdErkek.setText(_translate("MainWindow", "Erkek"))
        self.label_12.setText(_translate("MainWindow", "Misafir Sayısı"))
        self.lblMisafirSayisi.setText(_translate("MainWindow", "Misafir Sayısı"))
        self.label.setText(_translate("MainWindow", "TC"))
        self.lneTC.setInputMask(_translate("MainWindow", "99999999999"))
        self.label_2.setText(_translate("MainWindow", "Adı"))
        self.label_3.setText(_translate("MainWindow", "Soyadı"))
        self.label_4.setText(_translate("MainWindow", "Oda Tipi"))
        self.cmbOdaTipi.setItemText(0, _translate("MainWindow", "Tek"))
        self.cmbOdaTipi.setItemText(1, _translate("MainWindow", "Çift"))
        self.cmbOdaTipi.setItemText(2, _translate("MainWindow", "Suit"))
        self.label_7.setText(_translate("MainWindow", "Gün Sayısı"))
        self.spnGunSayisi.setSuffix(_translate("MainWindow", " gün"))
        self.label_8.setText(_translate("MainWindow", "Ücret"))
        self.lblUcret.setText(_translate("MainWindow", "ücret"))
        self.label_9.setText(_translate("MainWindow", "Çocuk Sayısı"))
        self.btnKaydet.setText(_translate("MainWindow", "Kaydet"))
        self.btnSil.setText(_translate("MainWindow", "Sil"))
        self.btnGuncelle.setText(_translate("MainWindow", "Güncelle"))
        self.btnBul.setText(_translate("MainWindow", "Bul"))
        self.btnTemizle.setText(_translate("MainWindow", "Temizle"))
        self.btnListele.setText(_translate("MainWindow", "Listele"))
        self.btnCikis.setText(_translate("MainWindow", "Çıkış"))
        self.label_6.setText(_translate("MainWindow", "Giriş Tarihi"))
        self.label_11.setText(_translate("MainWindow", "Çıkış Tarihi"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuHakkinda.setText(_translate("MainWindow", "Hakkında"))
        self.menuCikis.setText(_translate("MainWindow", "Çıkış"))
