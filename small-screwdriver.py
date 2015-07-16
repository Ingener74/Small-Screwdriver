# encoding: utf8

import sys
from PySide.QtGui import QApplication, QPushButton


class Point(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    button = QPushButton(u"Выход")
    button.show()
    button.clicked.connect(app.quit)

    sys.exit(app.exec_())
