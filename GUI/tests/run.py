import sys

from PyQt5.QtWidgets import QApplication

from ui import Test


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
