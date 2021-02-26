"""
------------------------------------------------
Bagian ini berhubungan dengan tampilan dashboard
------------------------------------------------
"""
from PyQt5 import QtWidgets, QtGui, QtCore
from .ui_forms import Ui_MonitorForm

class dashboard(QtWidgets.QWidget, Ui_MonitorForm):
    tutup = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(dashboard,self).__init__(parent)
        self.setupUi(self)
        self.pbTest.clicked.connect(self.pbTestClicked)

    def pbTestClicked(self):
        """ Hanya untuk testing, misal untuk mengambil gambar """
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Buka file gambar', './', "Image files (*.jpg *.png)")
        dbgstr = "File gambar: {}".format(fname[0])
        self.dbgConsole.appendPlainText(dbgstr)
        pixmap = QtGui.QPixmap(fname[0])
        self.cam.setPixmap(pixmap)
        
    def closeEvent(self, event):
        self.tutup.emit()
        event.accept()

