import sys
from PyQt4 import QtCore, QtGui
from scopritore import Ui_MainWindow
import sc

class Scopritore(QtGui.QMainWindow):
    def __init__(self, parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.azione, QtCore.SIGNAL("currentIndexChanged(QString)"), self.disablePath)
		QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.scopri)
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.geometry()
		self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

		
        
    def disablePath(self,text):
        if text=='vlc':
            self.ui.path.setDisabled(True)
        else:
            self.ui.path.setDisabled(False)

    def scopri(self):
        if not self.ui.serieName.displayText():
            QtGui.QMessageBox.warning(self, 'Avviso',"Nome serie mancante")
        else:
            serie = self.ui.serieName.displayText()
            S = self.ui.serieN.text()
            E = self.ui.episodioN.text()
            formato = self.ui.estensione.displayText()
            r=sc.make_pattern(serie,S,E,formato)
            l=[i for i in sc.find(r,sc.TOR)]
            if  len(l)==0:
                QtGui.QMessageBox.warning(self, 'Avviso',"Nessun file video trovato %s %s %s %s" % (serie,S,E,formato))
                
            else:
                if len(l)==1:
                    video=l[0]
                else:
                    video, ok = QtGui.QInputDialog.getItem(None, 'Input Dialog', 'Scegli video',l)
                if video:
                    QtGui.QMessageBox.warning(self, 'Avviso',"Trovato "+video)
            
            
            


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Scopritore()
    myapp.show()
    sys.exit(app.exec_())
