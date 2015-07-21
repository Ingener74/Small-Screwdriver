# encoding: utf8
from PySide.QtGui import QPen


class Rect(object):
    def __init__(self, origin, size, pen=QPen()):
        self.origin = origin
        self.size = size
        self.pen = pen

    def draw(self, painter):
        painter.setPen(self.pen)
        painter.drawRect(self.origin.x, self.origin.y, self.size.width, self.size.height)

    def __str__(self):
        return '{}({}, {})'.format(self.__class__.__name__, str(self.origin), str(self.size))