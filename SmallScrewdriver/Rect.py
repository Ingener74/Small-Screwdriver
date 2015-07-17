# encoding: utf8
from PySide.QtCore import Qt
from PySide.QtGui import QPen


class Rect(object):
    def __init__(self, origin, width, height, color=Qt.red):
        self.origin = origin
        self.width = width
        self.height = height
        self.color = color

    def draw(self, painter):
        pen = QPen()
        pen.setColor(self.color)
        painter.setPen(pen)
        painter.drawRect(self.origin.x, self.origin.y, self.width, self.height)

    def __str__(self):
        return '{}{}'.format(self.__class__.__name__, {key: str(value) for key, value in self.__dict__.iteritems()})