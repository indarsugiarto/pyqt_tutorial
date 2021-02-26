#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:07:38 2021

@author: indi
"""
from sklearn.neural_network import MLPRegressor  
import numpy as np
import math

from PyQt5 import QtWidgets, QtGui
from mlpsim import Ui_MLPsim
import sys

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)
    def save(self,fname):
        self.fig.savefig(fname)
        
        
class paramDlg(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(paramDlg,self).__init__(parent)
        flo = QtWidgets.QFormLayout()
        self.nLayer = QtWidgets.QLineEdit(self)
        self.nLayer.setText("3")
        self.nLayer.setValidator(QtGui.QIntValidator())
        flo.addRow("Jumlah layer", self.nLayer)
        self.nNeuron = QtWidgets.QLineEdit(self)
        self.nNeuron.setText("20")
        self.nNeuron.setValidator(QtGui.QIntValidator())
        flo.addRow("Jumlah neuron", self.nNeuron)
        self.nIter = QtWidgets.QLineEdit(self)
        self.nIter.setText("10000")
        self.nIter.setValidator(QtGui.QIntValidator())
        flo.addRow("Iterasi maximum", self.nIter)

        hLayout = QtWidgets.QHBoxLayout()
        self.pbSimpan = QtWidgets.QPushButton("Simpan")
        self.pbSimpan.clicked.connect(self.pbSimpanClicked)
        self.pbBatal = QtWidgets.QPushButton("Batal")
        self.pbBatal.clicked.connect(self.pbBatalClicked)
        hLayout.addWidget(self.pbSimpan)
        hLayout.addSpacing(10)
        hLayout.addWidget(self.pbBatal)

        vLayout = QtWidgets.QVBoxLayout(self)
        vLayout.addLayout(flo)
        vLayout.addSpacing(10)
        vLayout.addLayout(hLayout)
        self.setLayout(vLayout)
        self.setWindowTitle("Setting Parameter MLP")
        #self.signalslot()
        self.setModal(True)
        self.show()
       
    def signalslot(self):
        self.pbReset.clicked.connect(self.Reset)
        self.pbShutdown.clicked.connect(self.Shutdown)
        
    def pbSimpanClicked(self):
        """ 
        Jika tombol Cancel ditekan, tidak perlu melakukan apa-apa
        """
        nLayer = int(self.nLayer.text())
        nNeuron = int(self.nNeuron.text())
        nIter = int(self.nIter.text())
        self.param = (nLayer, nNeuron, nIter)
        self.accept()

    def pbBatalClicked(self):
        """ 
        Jika tombol Cancel ditekan, tidak perlu melakukan apa-apa
        """
        self.reject()

class wxSim(QtWidgets.QWidget, Ui_MLPsim):
    def __init__(self, parent=None):
        super(wxSim,self).__init__(parent)
        self.setupUi(self)

        self.dataFile = None
        self.mlpParam = None
        
        """ Lalu tentukan koneksi signal-slot """
        self.pbOpen.clicked.connect(self.pbOpenClicked)
        self.pbSim.clicked.connect(self.pbSimClicked)
        self.pbSim.setEnabled(False)
        self.pbSave.clicked.connect(self.pbSaveClicked)
        self.pbSave.setEnabled(False)
        self.pbConfig.clicked.connect(self.pbConfigClicked)

    def pbOpenClicked(self):
        fname, _filter = QtWidgets.QFileDialog.getOpenFileName(self, "Buka File Data", "", "Data file (*.csv)")
        if fname != '':
            self.dataFile = fname
            
    def pbSimClicked(self):
        if self.dataFile is None or self.mlpParam is None:
            return
        szLayer = tuple([self.mlpParam[1] for _ in range(self.mlpParam[0])])
        mlp = MLPRegressor(hidden_layer_sizes=szLayer, activation='tanh', solver='sgd', max_iter= self.mlpParam[2])
        data = np.loadtxt(self.dataFile, delimiter=",")
        X = np.array([[x] for x in data[:,0]])
        y = np.array([[x] for x in data[:,1]])
        mlp.fit(X,y.ravel())
        a = math.floor(min(min(X)))
        b = math.ceil(max(max(X)))
        X_test = [[i] for i in np.linspace(a,b,len(X))]
        y_test = mlp.predict(X_test)
        
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.sc.axes.plot(X, y, "g.")
        self.sc.axes.plot(X_test, y_test, "c-", linewidth=2)

        toolbar = NavigationToolbar(self.sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.sc)

        self.plotter = QtWidgets.QDialog()
        self.plotter.setLayout(layout)
        self.plotter.show()
        self.pbSave.setEnabled(True)


    def pbSaveClicked(self):
        fname, _filter = QtWidgets.QFileDialog.getSaveFileName(self, "Simpan Grafik", "", "Image file (*.png)")
        if fname != '':
            if fname.find('.png') == -1:
                fname = fname + '.png'
            self.sc.save(fname)
            self.plotter.close()
        
    def pbConfigClicked(self):
        getParam = paramDlg(self)
        if getParam.exec_() == QtWidgets.QDialog.Accepted:
            self.mlpParam = getParam.param
            self.pbSim.setEnabled(True)
            


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = wxSim()
    widget.show()
    app.exec_()
    