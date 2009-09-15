# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'python/litprojects/trunk/seriesManager/gui/seriesManagerMain.ui'
#
# Created: Tue Sep 15 22:04:28 2009
#      by: PyQt4 UI code generator 4.5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 59)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.serieName = QtGui.QLineEdit(self.centralwidget)
        self.serieName.setGeometry(QtCore.QRect(0, 0, 241, 24))
        self.serieName.setObjectName("serieName")
        self.serieN = QtGui.QSpinBox(self.centralwidget)
        self.serieN.setGeometry(QtCore.QRect(250, 0, 54, 25))
        self.serieN.setMinimum(1)
        self.serieN.setObjectName("serieN")
        self.episodioN = QtGui.QSpinBox(self.centralwidget)
        self.episodioN.setGeometry(QtCore.QRect(310, 0, 54, 25))
        self.episodioN.setMinimum(1)
        self.episodioN.setObjectName("episodioN")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 30, 111, 24))
        self.pushButton.setObjectName("pushButton")
        self.estensione = QtGui.QLineEdit(self.centralwidget)
        self.estensione.setGeometry(QtCore.QRect(370, 0, 61, 25))
        self.estensione.setObjectName("estensione")
        self.azione = QtGui.QComboBox(self.centralwidget)
        self.azione.setGeometry(QtCore.QRect(0, 30, 111, 24))
        self.azione.setObjectName("azione")
        self.azione.addItem(QtCore.QString())
        self.azione.addItem(QtCore.QString())
        self.path = QtGui.QLineEdit(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(120, 30, 121, 25))
        self.path.setObjectName("path")
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 30, 61, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("pressed()"), MainWindow.close)
        QtCore.QObject.connect(self.azione, QtCore.SIGNAL("currentIndexChanged(QString)"), self.path.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.serieName, self.serieN)
        MainWindow.setTabOrder(self.serieN, self.episodioN)
        MainWindow.setTabOrder(self.episodioN, self.estensione)
        MainWindow.setTabOrder(self.estensione, self.azione)
        MainWindow.setTabOrder(self.azione, self.path)
        MainWindow.setTabOrder(self.path, self.pushButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "GO", None, QtGui.QApplication.UnicodeUTF8))
        self.estensione.setText(QtGui.QApplication.translate("MainWindow", "avi", None, QtGui.QApplication.UnicodeUTF8))
        self.azione.setItemText(0, QtGui.QApplication.translate("MainWindow", "copy", None, QtGui.QApplication.UnicodeUTF8))
        self.azione.setItemText(1, QtGui.QApplication.translate("MainWindow", "vlc", None, QtGui.QApplication.UnicodeUTF8))
        self.path.setText(QtGui.QApplication.translate("MainWindow", "/media/ILICH", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))

