from resultDialog_ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog


class ResultDialog(QDialog):
    def __init__(self, db):
        self.db = db
        QDialog.__init__(self)
        self.child = Ui_Dialog()
        self.child.setupUi(self)
