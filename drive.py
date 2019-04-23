from mainwindow import *
from choosedialog import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys


class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        # 想在这里定按钮中的功能
        # self.main_ui.nextbtn.clicked.connect(self.nextChoose())

    # def nextChoose(self):
        # self.hide()
        # self.dialog = Ui_Dialog()
        # self.dialog.show()


class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Dialog()
        self.child.setupUi(self)
        # self.child.restart.clicked.connect(self.returnMain())

    # def returnMain(self):
    #     self.hide()
    #     self.mainwindow = Ui_MainWindow()
    #     self.mainwindow.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = parentWindow()
    child = childWindow()

    # use button to connect
    btn = window.main_ui.nextbtn
    btn.clicked.connect(child.show)

    # display
    window.show()
    sys.exit(app.exec_())
