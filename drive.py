import sys

import pymysql

from ChooseDialog import *
from MainWindow import *
from ResultDialog import *


class Controller:
    def __init__(self, db):
        self.db = db
        self.main_window = MainWindow()



    def show_main_window(self):
        self.main_window.switch_window.connect(self.show_choose_dialog)
        # self.main_window.main_ui.nextbtn.clicked.connect(self.show_choose_dialog)
        self.main_window.show()

    def show_choose_dialog(self, text):
        def choose_dialog_return():
            self.choose_dialog.close()
            self.show_main_window()
        self.choose_dialog = ChooseDialog(db, text)
        self.main_window.close()
        self.choose_dialog.child.restart.clicked.connect(choose_dialog_return)
        # self.choose_dialog.child.next.clicked.connect(self.show_result_dialog)
        self.choose_dialog.switch_window.connect(self.show_result_dialog)
        self.choose_dialog.show()

    def show_result_dialog(self, text):
        def result_dialog_return():
            self.result_dialog.close()
            self.show_main_window()
        self.result_dialog = ResultDialog(db, text)
        self.choose_dialog.close()
        self.result_dialog.child.reselectPushButton.clicked.connect(result_dialog_return)
        self.result_dialog.child.close.clicked.connect(self.result_dialog.close)
        self.result_dialog.show()


def open_ui(db):
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller(db)
    controller.show_main_window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    # db = pymysql.connect("ece651db.cyepucyw4sld.us-east-2.rds.amazonaws.com", "hdong", "donghao0",
    #     #                          "yelp")
    db = pymysql.connect("localhost","hdong","dddd","Yelp")
    open_ui(db)
    db.close()
