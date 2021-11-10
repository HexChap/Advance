import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QGraphicsDropShadowEffect, QWidget
from PyQt5.Qt import QMainWindow
from PyQt5 import QtCore

from gui_utils import set_move_window
from ui_functions import *
from main_window import Ui_MainWindow
from functools import partial


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        init_functional(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    set_move_window(window)
    window.show()
    sys.exit(app.exec_())
