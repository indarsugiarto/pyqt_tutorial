"""
------------------------------------------------
Bagian ini berhubungan dengan tampilan About Me
------------------------------------------------
"""
from PyQt5 import QtWidgets
from .ui_forms import Ui_AboutForm

class about(QtWidgets.QWidget, Ui_AboutForm):
    def __init__(self, parent=None):
        super(about,self).__init__(parent)
        self.setupUi(self)

