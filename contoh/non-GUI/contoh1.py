#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:07:38 2021

Contoh sederhana bagaimana menggunakan PyQt5 untuk
aplikasi non-GUI. Kuncinya adalah pada penggunaan
QtCore.QCoreApplication() dan bukannya QApplication()

@author: indi@petra.ac.id
"""

from PyQt5 import QtCore
import time

class Hello(QtCore.QObject):
    def __init__(self):
        super(Hello, self).__init__()
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
