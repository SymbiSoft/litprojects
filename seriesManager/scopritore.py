# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'python/litprojects/trunk/seriesManager/gui/seriesManagerMain.ui'
#
# Created: Sat Sep 19 15:41:25 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 74)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.serieName = QtGui.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serieName.sizePolicy().hasHeightForWidth())
        self.serieName.setSizePolicy(sizePolicy)
        self.serieName.setMinimumSize(QtCore.QSize(230, 0))
        self.serieName.setObjectName("serieName")
        self.gridLayout.addWidget(self.serieName, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.azione = QtGui.QComboBox(self.gridLayoutWidget)
        self.azione.setObjectName("azione")
        self.azione.addItem(QtCore.QString())
        self.azione.addItem(QtCore.QString())
        self.horizontalLayout_2.addWidget(self.azione)
        self.path = QtGui.QLineEdit(self.gridLayoutWidget)
        self.path.setObjectName("path")
        self.horizontalLayout_2.addWidget(self.path)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.serieN = QtGui.QSpinBox(self.gridLayoutWidget)
        self.serieN.setMinimum(1)
        self.serieN.setObjectName("serieN")
        self.horizontalLayout.addWidget(self.serieN)
        self.episodioN = QtGui.QSpinBox(self.gridLayoutWidget)
        self.episodioN.setMinimum(1)
        self.episodioN.setObjectName("episodioN")
        self.horizontalLayout.addWidget(self.episodioN)
        self.estensione = QtGui.QLineEdit(self.gridLayoutWidget)
        self.estensione.setObjectName("estensione")
        self.horizontalLayout.addWidget(self.estensione)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.serieName, self.serieN)
        MainWindow.setTabOrder(self.serieN, self.episodioN)
        MainWindow.setTabOrder(self.episodioN, self.estensione)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Scopritore", None, QtGui.QApplication.UnicodeUTF8))
        self.azione.setItemText(0, QtGui.QApplication.translate("MainWindow", "copy", None, QtGui.QApplication.UnicodeUTF8))
        self.azione.setItemText(1, QtGui.QApplication.translate("MainWindow", "vlc", None, QtGui.QApplication.UnicodeUTF8))
        self.path.setText(QtGui.QApplication.translate("MainWindow", "/media/ILICH", None, QtGui.QApplication.UnicodeUTF8))
        self.estensione.setText(QtGui.QApplication.translate("MainWindow", "avi", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "GO", None, QtGui.QApplication.UnicodeUTF8))

