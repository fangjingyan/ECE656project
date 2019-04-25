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
        select_table_flag = False
        clean_flag = ""
        if self.child.yes_clean.isChecked():
            self.clean_data()
            clean_flag = "_clean"

        for checkbox in self.child.business_checkboxes:
            if checkbox.isChecked():
                select_table_flag = True
                self.selected_attributes.append("business"+clean_flag+"."+checkbox.text())
        if select_table_flag:
            select_table_flag = False
            self.selected_tables.append("business"+clean_flag)

        for checkbox in self.child.business_categories_checkboxes:
            if checkbox.isChecked():
                select_table_flag = True
                self.selected_attributes.append("business_categories"+clean_flag+"."+checkbox.text())
        if select_table_flag:
            select_table_flag = False
            self.selected_tables.append("business_categories"+clean_flag)

        for checkbox in self.child.review_checkboxes:
            if checkbox.isChecked():
                select_table_flag = True
                self.selected_attributes.append("review"+clean_flag+"."+checkbox.text())
        if select_table_flag:
            select_table_flag = False
            self.selected_tables.append("review"+clean_flag)

        for checkbox in self.child.tip_checkboxes:
            if checkbox.isChecked():
                select_table_flag = True
                self.selected_attributes.append("tip"+clean_flag+"."+checkbox.text())
        if select_table_flag:
            select_table_flag = False
            self.selected_tables.append("tip"+clean_flag)

        for checkbox in self.child.user_checkboxes:
            if checkbox.isChecked():
                select_table_flag = True
                self.selected_attributes.append("user"+clean_flag+"."+checkbox.text())
        if select_table_flag:
            select_table_flag = False
            self.selected_tables.append("user"+clean_flag)

        for checkbox in self.child.user_elite_checkboxes:
            if checkbox.isChecked():
                select_table_flag = True
                self.selected_attributes.append("user_elite"+clean_flag+"."+checkbox.text())
        if select_table_flag:
            select_table_flag = False
            self.selected_tables.append("user_elite"+clean_flag)

        print(self.selected_attributes)
        print(self.selected_tables)

    def clear_selected(self):
        self.selected_tables = []
        self.selected_attributes =[]

    def cal_tree(self):
        print("cal_tree")

    def clean_data(self):
        print("clean data")
        cursor = self.db.cursor()
        cursor.execute("select * from yelp.user where name = 'test' limit 1")
        data = cursor.fetchone()
