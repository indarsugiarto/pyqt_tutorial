import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTimer
from PyQt5 import uic
import os
import pathlib
import time

from .ui_forms import Ui_MainWindow
from .dashboard import dashboard
from .about import about

class smartParking(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(smartParking,self).__init__(parent)

        self.setupUi(self)
        self.setCentralWidget(self.mdiArea)

        self.timer = QTimer()
        self.timer.timeout.connect(self.getTime)
        self.timer.setInterval(1000)
        self.timer.start()

        self.dashboardActive = False

        self.pbMon.clicked.connect(self.showDashboard)
        self.action_Monitor.triggered.connect(self.showDashboard)
        self.action_About.triggered.connect(self.showAbout)
        
        self.login()
        self.show()

    def login(self):
        """ Seharusnya ada mekanisme untuk login. Sementara di bypass dulu.  """
        self.opStatus = QtWidgets.QLabel("Operator: Indar")
        self.sepStatus = QtWidgets.QLabel("|")
        self.netStatus = QtWidgets.QLabel("Server Polda Jatim Connected")
        self.statusBar().addWidget(self.netStatus)
        self.statusBar().addWidget(self.sepStatus)
        self.statusBar().addWidget(self.opStatus)

    def dashboardClosed(self):
        self.dashboardActive = False

    def showDashboard(self):
        if self.dashboardActive is True:
            return
        else:
            self.dashboardActive = True
        self.dash = dashboard(self)
        self.dash.tutup.connect(self.dashboardClosed)
        self.subDash = QtWidgets.QMdiSubWindow(self.mdiArea)
        self.subDash.setWidget(self.dash)
        self.mdiArea.addSubWindow(self.subDash)
        self.subDash.show()

    def showAbout(self):
        self.me = about()
        self.me.setWindowModality(QtCore.Qt.ApplicationModal)
        self.me.show()

    def getTime(self):
        sekarang = time.localtime()
        detik = "%02d" % sekarang.tm_sec
        menit = "%02d" % sekarang.tm_min
        jam = "%02d" % sekarang.tm_hour
        tgl = "%02d/%02d/%02d" % (sekarang.tm_mday, sekarang.tm_mon, sekarang.tm_year)
        self.lcdDetik.display(detik)
        self.lcdMenit.display(menit)
        self.lcdJam.display(jam)
        self.tanggal.setText(tgl)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F12:
            self.showAbout()
        elif event.key() == QtCore.Qt.Key_F2:
            self.showDashboard()
        
