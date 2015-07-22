# encoding: utf8
import copy
from PySide.QtCore import Qt
from PySide.QtGui import QPen
from Size import Size
from Point import Point
from Rect import Rect


# noinspection PyPep8Naming
class Bin(object):
    def __init__(self, size=Size(256, 256), origin=Point(0, 0)):
        self.origin = origin
        self.size = size
        self.rects = []

    def append(self, rect):
        area = rect.area()
        for r in self.rects:
            area += r.area()

        if area <= self.size.area():
            self.rects.append(rect)
            return True
        else:
            return False

    def fillLevel(self):
        area = 0.0
        for r in self.rects:
            area += r.area()
        return area / float(self.size.area())

    def draw(self, painter):
        pen = QPen()
        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawRect(self.origin.x, self.origin.y, self.size.width, self.size.height)

        for rect in self.rects:
            Rect(rect.origin + self.origin, rect.size, rect.pen).draw(painter=painter)

    def __str__(self):
        return '{}({}, {}, {})'.format(self.__class__.__name__, self.origin, self.size, self.rects)

    def __repr__(self):
        return self.__str__()
