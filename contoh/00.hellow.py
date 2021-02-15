from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget

""" Contoh paling sederhana untuk hello world 
    Catatan: Tanpa QApplication, QWidget tidak bisa dipakai """
app = QApplication([])
QMessageBox.information(QWidget(),"Informasi","Hello World! Bagaimana kabar anda?")
