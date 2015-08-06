# encoding: utf8

import random
from PySide.QtGui import QPen, QColor
from Size import Size
from Point import Point


class Rect(object):
    """
    Split rules
    """
    RULE_SAS = 0
    RULE_LAS = 1
    RULE_SLAS = 2
    RULE_LLAS = 3
    RULE_MAXAS = 4
    RULE_MINAS = 5

    def __init__(self, origin=Point(), size=Size(), pen=QPen()):
        self.origin = origin
        self.size = size
        self.pen = pen

    def area(self):
        return self.size.area()

    def draw(self, painter, offset):
        painter.setPen(self.pen)
        painter.drawRect(self.origin.x + offset.x, self.origin.y + offset.y, self.size.width, self.size.height)

    def split(self, size, rule):
        """
        Разделить прямоугольник
        :param size:
        :return:
        """
        if size >= self.size:
            return False
        return False

    def __eq__(self, other):
        return self.origin == other.origin and self.size == other.size

    def __ne__(self, other):
        return self.origin != other.origin or self.size != other.size

    def __str__(self):
        return '{}({}, {})'.format(self.__class__.__name__, str(self.origin), str(self.size))

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def random():
        pen = QPen()
        pen.setColor(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        point = Point(100. * random.random(), 100. * random.random())
        size = Size(5 + 100. * random.random(), 5 + 100. * random.random())
        return Rect(point, size, pen)
