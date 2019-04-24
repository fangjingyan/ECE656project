from choosedialog_ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog


class ChooseDialog(QDialog):
    def __init__(self, db):
        self.db = db
        QDialog.__init__(self)
        self.child = Ui_Dialog()
        self.child.setupUi(self)
        self.child.next.clicked.connect(self.clear_selected)
        self.child.next.clicked.connect(self.set_selected_attr)
        self.child.next.clicked.connect(self.cal_tree)
        self.selected_attributes = []
        self.selected_tables = []

    def set_selected_attr(self):
        check_flag = False

        for checkbox in self.child.business_checkboxes:
            if checkbox.isChecked():
                check_flag = True
                self.selected_attributes.append("business."+checkbox.text())
        if check_flag:
            check_flag = False
            self.selected_tables.append("business")

        for checkbox in self.child.business_categories_checkboxes:
            if checkbox.isChecked():
                check_flag = True
                self.selected_attributes.append("business_categories."+checkbox.text())
        if check_flag:
            check_flag = False
            self.selected_tables.append("business_categories")

        for checkbox in self.child.review_checkboxes:
            if checkbox.isChecked():
                check_flag = True
                self.selected_attributes.append("review."+checkbox.text())
        if check_flag:
            check_flag = False
            self.selected_tables.append("review")

        for checkbox in self.child.tip_checkboxes:
            if checkbox.isChecked():
                check_flag = True
                self.selected_attributes.append("tip."+checkbox.text())
        if check_flag:
            check_flag = False
            self.selected_tables.append("tip")

        for checkbox in self.child.user_checkboxes:
            if checkbox.isChecked():
                check_flag = True
                self.selected_attributes.append("user."+checkbox.text())
        if check_flag:
            check_flag = False
            self.selected_tables.append("user")

        for checkbox in self.child.user_elite_checkboxes:
            if checkbox.isChecked():
                check_flag = True
                self.selected_attributes.append("user_elite."+checkbox.text())
        if check_flag:
            check_flag = False
            self.selected_tables.append("user_elite")

        for checkbox in self.child.user_friends_checkboxes:
            if checkbox.isChecked():
                check_flag = True
                self.selected_attributes.append("user_friends."+checkbox.text())
        if check_flag:
            check_flag = False
            self.selected_tables.append("user_friends")

        print(self.selected_attributes)
        print(self.selected_tables)

    def clear_selected(self):
        self.selected_tables = []
        self.selected_attributes =[]

    def cal_tree(self):
        if self.child.yes_clean.isChecked():
            self.clean_data()

    def clean_data(self):
        print("clean data")
        cursor = self.db.cursor()
        cursor.execute("select * from yelp.user where name = 'test' limit 1")
        data = cursor.fetchone()
