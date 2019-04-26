from choosedialog_ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from decision_tree import *
import csv


class ChooseDialog(QDialog):
    def __init__(self, db):
        self.db = db
        self.dataSet = []
        self.decision_tree = {}
        self.accuracy = 0
        self.labels = []
        QDialog.__init__(self)
        self.child = Ui_Dialog()
        self.child.setupUi(self)
        self.child.next.clicked.connect(self.cal_tree)
        self.child.next.clicked.connect(self.save_data_to_csv)
        self.child.next.clicked.connect(self.data_mining)
        self.child.next.clicked.connect(self.test_tree)
        self.child.next.clicked.connect(self.clear_data)

    def cal_tree(self):
        print("cal_tree")

    def save_data_to_csv(self):
        # judge whether to clean data
        if self.child.yes_clean.isChecked():
            print("clean data")
            clean_flag = "_clean"
        else:
            print("don't clean data")
            clean_flag = ""

        # create the view needed for data processing
        cur = self.db.cursor()
        sql = "create view calc_decision_tree as\
                select \
                business{0}.stars               as b_average_stars,\
                business{0}.review_count        as b_review_count,\
                user{0}.average_stars           as u_average_stars,\
                user{0}.review_count            as u_review_count,\
                user{0}.fans                    as u_fans,\
                review{0}.stars                 as u_b_stars\
                from business{0}\
                inner join review{0} using (business_id)\
                inner join user{0} using (user_id);".format(clean_flag)
        cur.execute(sql)
        self.db.commit()

        # save data into list
        print("data saving start")

        self.labels = ['b_average_stars', 'b_review_count', 'u_average_stars', 'u_review_count',
                       'u_fans']
        labels_str = ""
        for l in self.labels:
            labels_str += ","+l
        sql = 'select %s from calc_decision_tree;'% (labels_str[1:] + ', u_b_stars')
        print(sql)
        cur.execute(sql)
        self.db.commit()

        while True:
            row = cur.fetchone()  # 获取下一个查询结果集为一个对象
            if not row:
                break
            self.dataSet.append(list(row))

        print("data saving end")

        # drop the view
        sql = "drop view calc_decision_tree;"
        cur.execute(sql)
        self.db.commit()
        if cur:
            cur.close()

    def data_mining(self):
        half_length = int(len(self.dataSet) * 1 / 2)
        train_dataSet = self.dataSet[:half_length]
        dataSet, labels, labels_full = createDataSet(train_dataSet, self.labels)
        # chooseBestFeatureToSplit(dataSet, labels)
        self.decision_tree = createTree(dataSet, labels)
        print(self.decision_tree)

    def test_tree(self):
        half_length = int(len(self.dataSet) * 1 / 2)
        test_dataSet = self.dataSet[half_length + 1:]

        for d in test_dataSet:
            child = self.decision_tree
            feature_dic = {}
            for i in range(0,len(self.labels)):
                feature_dic[self.labels[i]] = d[i]

            while isinstance(child, dict):
                key = list(child.keys())[0]
                feature = key.split(' ')[0]
                if feature_dic[feature] < float(key.split(' ')[2]):
                    child = child[key]['yes']
                else:
                    child = child[key]['no']
            if int(child) == int(d[-1]):
                self.accuracy += 1
        self.accuracy = self.accuracy / len(test_dataSet)
        print(self.accuracy)

    def clear_data(self):
        self.dataSet = []
        self.decision_tree = {}
        self.accuracy = 0
