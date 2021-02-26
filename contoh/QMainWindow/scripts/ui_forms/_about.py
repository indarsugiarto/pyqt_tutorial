# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutForm(object):
    def setupUi(self, AboutForm):
        AboutForm.setObjectName("AboutForm")
        AboutForm.resize(450, 360)
        AboutForm.setMinimumSize(QtCore.QSize(450, 360))
        AboutForm.setMaximumSize(QtCore.QSize(450, 360))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutForm.setWindowIcon(icon)
        self.textEdit = QtWidgets.QTextEdit(AboutForm)
        self.textEdit.setGeometry(QtCore.QRect(0, 250, 450, 111))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(AboutForm)
        self.label.setGeometry(QtCore.QRect(130, 10, 181, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icon/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AboutForm)
        self.label_2.setGeometry(QtCore.QRect(30, 200, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(AboutForm)
        QtCore.QMetaObject.connectSlotsByName(AboutForm)

    def retranslateUi(self, AboutForm):
        _translate = QtCore.QCoreApplication.translate
        AboutForm.setWindowTitle(_translate("AboutForm", "Tentang Kami"))
        self.textEdit.setHtml(_translate("AboutForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Sistem parkir berdasarkan konsep IoT (</span><span style=\" font-size:12pt; font-style:italic;\">Internet of Things</span><span style=\" font-size:12pt;\">) dan AI (</span><span style=\" font-size:12pt; font-style:italic;\">Artificial Intelligence</span><span style=\" font-size:12pt;\">) yang mendukung pengembangan </span><span style=\" font-size:12pt; font-weight:600;\">Smart City</span><span style=\" font-size:12pt;\">.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Kontak kami: cs@smartparking.co.id</span></p></body></html>"))
        self.label_2.setText(_translate("AboutForm", "Smart Parking System"))

from . import form_src_rc
