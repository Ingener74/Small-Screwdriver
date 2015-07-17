# encoding: utf8
from PySide.QtCore import Qt
from PySide.QtGui import QPen


class Rect(object):
    def __init__(self, origin, width, height, pen=QPen()):
        self.origin = origin
        self.width = width
        self.height = height
        self.pen = pen

    def draw(self, painter):
        painter.setPen(self.pen)
        painter.drawRect(self.origin.x, self.origin.y, self.width, self.height)

    def __str__(self):
        return '{}{}'.format(self.__class__.__name__, {key: str(value) for key, value in self.__dict__.iteritems()})