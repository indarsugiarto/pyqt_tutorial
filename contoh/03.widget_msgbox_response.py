import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QVBoxLayout, QPushButton

class App(QWidget):

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setWindowTitle('Contoh respon QDialog dengan QMessageBox')
        layout = QVBoxLayout(self)
        self.btn = QPushButton("Survey")
        self.btn.clicked.connect(self.btn_ditekan)
        layout.addWidget(self.btn)
        self.show()

    def btn_ditekan(self):
        jawab = QMessageBox.question(self, 'Pertanyaan', "Bagaimana kabarnya hari ini, baik?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if jawab==QMessageBox.Yes:
            QMessageBox.information(self,"Well...","OK!")
        else:
            QMessageBox.information(self,"Well....","Aww!")
        self.show()
        
if __name__ == '__main__':
    app = QApplication([])
    widget = App()
    """ Letakkan di tengah-tengah layar monitor """
    szScreen = app.primaryScreen().geometry().getRect()
    szApp = widget.geometry().getRect()
    widget.setGeometry((szScreen[2]//2)-(szApp[2]//2),(szScreen[3]//2)-(szApp[3]//2),0,0)
    sys.exit(app.exec_())  
