import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import time

class MainWidget(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("mywidget.ui", self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.getTime)
        self.timer.setInterval(1000)
        self.timer.start()

    def getTime(self):
        sekarang = time.localtime()
        detik = "%02d" % sekarang.tm_sec
        menit = "%02d" % sekarang.tm_min
        jam = "%02d" % sekarang.tm_hour
        tgl = "%02d/%02d/%02d" % (sekarang.tm_mday, sekarang.tm_mon, sekarang.tm_year)
        self.detik.display(detik)
        self.menit.display(menit)
        self.jam.display(jam)
        print(f"Hari ini tanggal: {tgl}")
        
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    app.exec_()
