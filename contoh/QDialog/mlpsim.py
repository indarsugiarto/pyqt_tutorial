# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mlpsim.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MLPsim(object):
    def setupUi(self, MLPsim):
        MLPsim.setObjectName("MLPsim")
        MLPsim.resize(150, 200)
        MLPsim.setMinimumSize(QtCore.QSize(150, 200))
        MLPsim.setMaximumSize(QtCore.QSize(150, 200))
        self.pbOpen = QtWidgets.QPushButton(MLPsim)
        self.pbOpen.setGeometry(QtCore.QRect(20, 20, 104, 23))
        self.pbOpen.setObjectName("pbOpen")
        self.pbSim = QtWidgets.QPushButton(MLPsim)
        self.pbSim.setGeometry(QtCore.QRect(20, 60, 104, 23))
        self.pbSim.setObjectName("pbSim")
        self.pbSave = QtWidgets.QPushButton(MLPsim)
        self.pbSave.setGeometry(QtCore.QRect(20, 100, 104, 23))
        self.pbSave.setObjectName("pbSave")
        self.pbConfig = QtWidgets.QPushButton(MLPsim)
        self.pbConfig.setGeometry(QtCore.QRect(20, 140, 104, 23))
        self.pbConfig.setObjectName("pbConfig")

        self.retranslateUi(MLPsim)
        QtCore.QMetaObject.connectSlotsByName(MLPsim)

    def retranslateUi(self, MLPsim):
        _translate = QtCore.QCoreApplication.translate
        MLPsim.setWindowTitle(_translate("MLPsim", "Regresi dengan Multilayer Perceptron"))
        self.pbOpen.setText(_translate("MLPsim", "Buka Data"))
        self.pbSim.setText(_translate("MLPsim", "Simulasi"))
        self.pbSave.setText(_translate("MLPsim", "Simpan"))
        self.pbConfig.setText(_translate("MLPsim", "Konfigurasi MLP"))

