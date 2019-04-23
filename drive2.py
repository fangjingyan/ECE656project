from mainwindow import *
from choosedialog import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys

class MainWindow(QMainWindow):
    #### switch_window can be used to transfer data ####
    #### https://gist.github.com/MalloyDelacroix/2c509d6bcad35c7e35b1851dfc32d161 ####
    # switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        # self.main_ui.nextbtn.clicked.connect(self.next_clicked)

    # def next_clicked(self):
    #     self.switch_window.emit()

class ChooseDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Dialog()
        self.child.setupUi(self)


class Controller:
    def __init__(self):
        pass

    def show_mian_window(self):
        self.main_window = MainWindow()
        # self.main_window.switch_window.connect(self.show_choose_dialog)
        self.main_window.main_ui.nextbtn.clicked.connect(self.show_choose_dialog)
        self.main_window.show()

    def show_choose_dialog(self):
        self.choose_dialog = ChooseDialog()
        self.main_window.close()
        self.choose_dialog.child.restart.clicked.connect(self.restart)
        self.choose_dialog.show()

    def restart(self):
        self.choose_dialog.close()
        self.show_mian_window()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_mian_window()
    sys.exit(app.exec_())
