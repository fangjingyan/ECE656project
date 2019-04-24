import sys

import pymysql
from PyQt5 import QtWidgets

from ChooseDialog import *
from MainWindow import *


class Controller:
    def __init__(self, db):
        self.db = db
        self.main_window = MainWindow()
        self.choose_dialog = ChooseDialog(db)

    def show_mian_window(self):
        # self.main_window.switch_window.connect(self.show_choose_dialog)
        self.main_window.main_ui.nextbtn.clicked.connect(self.show_choose_dialog)
        self.main_window.show()

    def show_choose_dialog(self):
        # set user and business
        self.main_window.close()
        self.choose_dialog.child.restart.clicked.connect(self.choose_dialog_return)
        self.choose_dialog.show()

    def choose_dialog_return(self):
        self.choose_dialog.close()
        self.show_mian_window()


def open_ui(db):
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller(db)
    controller.show_mian_window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    db = pymysql.connect("ece651db.cyepucyw4sld.us-east-2.rds.amazonaws.com", "hdong", "donghao0",
                         "yelp")
    open_ui(db)
    db.close()
