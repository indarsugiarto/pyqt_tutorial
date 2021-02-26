#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:07:38 2021

Contoh program ini menunjukkan bagaimana bekerja dengan
mekanisme multi-threading yang benar. Meskipun Qt memiliki
QThread, tetapi disarankan untuk tidak melakukan inheritance
langsung terhadap QThread ini.

@author: indi@petra.ac.id
"""

from PyQt5 import QtCore
import time

class mainCtrl(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    running = False

    def __init__(self):
        super(mainCtrl, self).__init__()

    def run(self):
        self.running = True
        while self.running:
            QtCore.QCoreApplication.processEvents()
            time.sleep(1)

    def stop(self):
        self.running = False
        self.finished.emit()
        
class Hello(QtCore.QObject):
    def __init__(self):
        super(Hello, self).__init__()
        self.mainCtrl = mainCtrl()
        self.thread = QtCore.QThread()
        self.mainCtrl.moveToThread(self.thread)
        self.thread.started.connect(self.mainCtrl.run)       
        self.mainCtrl.finished.connect(self.thread.quit)
        self.mainCtrl.finished.connect(self.mainCtrl.deleteLater)           
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.say)
        self.timer.start(1000)
        self.i = 0
        
    def say(self):
        self.i += 1
        print("[AWAS] Ini warning ke-%d"%self.i)
        if self.i > 5:
            print("[DONE] Selesai sudah!")
            QtCore.QCoreApplication.instance().quit()

if __name__ == "__main__":
    import sys
    app = QtCore.QCoreApplication(sys.argv)
    hello = Hello()
    sys.exit(app.exec_())
