from mainwindow_ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog


class MainWindow(QMainWindow):
    #### switch_window can be used to transfer data ####
    #### https://gist.github.com/MalloyDelacroix/2c509d6bcad35c7e35b1851dfc32d161 ####
    # switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.user = ""
        self.business = ""
        self.main_ui.nextbtn.clicked.connect(self.set_selected_user_business)

    # def next_clicked(self):
    #     self.switch_window.emit()

    def set_selected_user_business(self):
        self.user = self.main_ui.user_box.toPlainText()
        self.business = self.main_ui.business_box.toPlainText()
