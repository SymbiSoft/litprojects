# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'python/litprojects/trunk/seriesManager/gui/seriesManagerMain.ui'
#
# Created: Wed Sep 16 20:53:59 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(374, 71)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../immagini/rarr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.serieName = QtGui.QLineEdit(self.centralwidget)
        self.serieName.setGeometry(QtCore.QRect(10, 10, 181, 24))
        self.serieName.setObjectName("serieName")
        self.serieN = QtGui.QSpinBox(self.centralwidget)
        self.serieN.setGeometry(QtCore.QRect(190, 10, 54, 25))
        self.serieN.setMinimum(1)
        self.serieN.setObjectName("serieN")
        self.episodioN = QtGui.QSpinBox(self.centralwidget)
        self.episodioN.setGeometry(QtCore.QRect(250, 10, 54, 25))
        self.episodioN.setMinimum(1)
        self.episodioN.setObjectName("episodioN")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 40, 181, 24))
        self.pushButton.setObjectName("pushButton")
        self.azione = QtGui.QComboBox(self.centralwidget)
        self.azione.setGeometry(QtCore.QRect(10, 40, 81, 24))
        self.azione.setObjectName("azione")
        self.azione.addItem(QtCore.QString())
        self.azione.addItem(QtCore.QString())
        self.path = QtGui.QLineEdit(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(90, 40, 101, 25))
        self.path.setObjectName("path")
        self.estensione = QtGui.QLineEdit(self.centralwidget)
        self.estensione.setGeometry(QtCore.QRect(310, 10, 61, 25))
        self.estensione.setObjectName("estensione")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.azione, QtCore.SIGNAL("currentIndexChanged(QString)"), self.path.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.serieName, self.serieN)
        MainWindow.setTabOrder(self.serieN, self.episodioN)
        MainWindow.setTabOrder(self.episodioN, self.estensione)
        MainWindow.setTabOrder(self.estensione, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.azione)
        MainWindow.setTabOrder(self.azione, self.path)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Scopritore", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "GO", None, QtGui.QApplication.UnicodeUTF8))
        self.azione.setItemText(0, QtGui.QApplication.translate("MainWindow", "copy", None, QtGui.QApplication.UnicodeUTF8))
        self.azione.setItemText(1, QtGui.QApplication.translate("MainWindow", "vlc", None, QtGui.QApplication.UnicodeUTF8))
        self.path.setText(QtGui.QApplication.translate("MainWindow", "/media/ILICH", None, QtGui.QApplication.UnicodeUTF8))
        self.estensione.setText(QtGui.QApplication.translate("MainWindow", "avi", None, QtGui.QApplication.UnicodeUTF8))

