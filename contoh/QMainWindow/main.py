#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:07:38 2021

@author: indi@petra.ac.id
"""
import sys
from PyQt5 import QtWidgets
from scripts import smartParking

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainUI = smartParking()
    sys.exit(app.exec_())
