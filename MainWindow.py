from mainwindow_ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog


class MainWindow(QMainWindow):
    # switch_window can be used to transfer data
    switch_window = QtCore.pyqtSignal(list)

    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.user = ""
        self.business = ""
        self.main_ui.nextbtn.clicked.connect(self.set_selected_user_business)
        self.main_ui.nextbtn.clicked.connect(self.emit_signals)


    def set_selected_user_business(self):
        self.user = self.main_ui.user_box.toPlainText()
        self.business = self.main_ui.business_box.toPlainText()

    def emit_signals(self):
        self.switch_window.emit([self.user,self.business])

