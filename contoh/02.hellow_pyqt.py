import sys
from PyQt5.QtWidgets import QMessageBox, QDialog, QApplication, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QWidget

""" Variasi hello world dengan PyQt """

class Form(QDialog):
   def __init__(self, parent=None):
      super(Form, self).__init__(parent)
      layout = QVBoxLayout(self)
      self.btn = QPushButton("Tekan aku!")
      self.btn.clicked.connect(self.btn_ditekan)
      layout.addWidget(self.btn)
      self.setWindowTitle("Contoh demo dengan button")

   def btn_ditekan(self):
      QMessageBox.information(QWidget(),"Informasi","Hello World! Bagaimana kabar anda?")			
def main():
   app = QApplication(sys.argv)
   ex = Form()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
