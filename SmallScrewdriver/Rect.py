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

    def draw(self, painter, offset=Point()):
        painter.setPen(self.pen)
        painter.drawRect(self.origin.x + offset.x, self.origin.y + offset.y, self.size.width, self.size.height)

    def split(self, rect, rule):
        """
        Разделить прямоугольник
        :param size:
        :return:
        """
        if max(self.size.width, self.size.height) <= min(rect.size.width, rect.size.height):
            return 0, Rect(), Rect()

        if self.size == rect.size:
            return 0, Rect(), Rect()

        if self.size.width == rect.size.width and self.size.height > rect.size.height:
            return 1, Rect(self.origin + Point(0, rect.size.height),
                           Size(self.size.width, self.size.height - rect.size.height)), Rect()

        if self.size.height == rect.size.height and self.size.width > rect.size.width:
            return 1, Rect(self.origin + Point(rect.size.width, 0),
                           Size(self.size.width - rect.size.width, self.size.height)), Rect()

        if max(rect.size.width, rect.size.height) < max(self.size.width, self.size.height) and \
                        min(rect.size.width, rect.size.height) < min(self.size.width, self.size.height):
            # тогда входит
            pass

        x1 = 0
        x2 = 0

        if rule is Rect.RULE_SAS or rule is Rect.RULE_LAS:
            x1 = self.size.width
            x2 = self.size.height
        elif rule is Rect.RULE_SLAS or rule is Rect.RULE_LLAS:
            x1 = self.size.width - rect.size.width
            x2 = self.size.height - rect.size.height
        elif rule is Rect.RULE_MAXAS or rule is Rect.RULE_MINAS:
            x1 = self.area()
            x2 = rect.area()

        if (rule is Rect.RULE_SAS or rule is Rect.RULE_SLAS or rule is Rect.RULE_MINAS) and x1 < x2:
            # Делим горизонтально
            r1 = Rect(self.origin + Point(rect.size.width, 0),
                      Size(self.size.width - rect.size.width, rect.size.height))

            r2 = Rect(self.origin + Point(0, rect.size.height),
                      Size(self.size.width, self.size.height - rect.size.height))
        else:
            # Делим вертикально
            r1 = Rect(self.origin + Point(rect.size.width, 0),
                      Size(self.size.width - rect.size.width, self.size.height))

            r2 = Rect(self.origin + Point(0, rect.size.height),
                      Size(rect.size.width, self.size.height - rect.size.height))

        return 2, r1, r2

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

    def randomColor(self):
        self.pen.setColor(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
