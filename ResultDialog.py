from resultDialog_ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog


class ResultDialog(QDialog):
    def __init__(self, db, accu_stars_list):
        self.db = db
        QDialog.__init__(self)
        self.child = Ui_Dialog()
        self.child.setupUi(self)
        self.child.close.clicked.connect(self.closeDB)
        self.child.accuracy.setText(str(accu_stars_list[0]))
        self.child.predicting_stars.setText(str(accu_stars_list[1]))
        print(accu_stars_list)

    def closeDB(self):
        if self.db:
            self.db.close()
