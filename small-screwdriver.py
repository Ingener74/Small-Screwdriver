# encoding: utf8

import sys
import json
from PySide.QtGui import QApplication, QPushButton


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toDict(self):
        return {'x': self.x, 'y': self.y}

    def __repr__(self):
        return json.dumps(self.toDict(), indent=4, separators=(',', ':'))

    def __str__(self):
        return self.__repr__()

class Rect(object):
    def __init__(self, origin, width, height):
        self.origin = origin
        self.width = width
        self.height = height

    def toDict(self):
        return {'origin': self.origin.toDict(), 'width': self.width, 'height': self.height}

    def __repr__(self):
        return json.dumps(self.toDict(), indent=4, separators=(',', ':'))

    def __str__(self):
        return self.__repr__()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    p1 = Point(10, 20)
    print p1

    r1 = Rect(p1, 100, 200)
    print r1

    button = QPushButton(u"Выход")
    button.setMinimumSize(200, 80)
    button.show()
    button.clicked.connect(app.quit)

    sys.exit(app.exec_())
