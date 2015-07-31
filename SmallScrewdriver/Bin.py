# encoding: utf8
from PySide.QtCore import Qt
from PySide.QtGui import QPen
from SmallScrewdriver import Size, Point, Rect


# noinspection PyPep8Naming
class Bin(object):
    def __init__(self, size=Size(256, 256), origin=Point(0, 0)):
        self.origin = origin
        self.size = size
        self.images = []

    def append(self, image):
        if image.area() > self.size.area():
            return False

        area = image.area()
        for r in self.images:
            area += r.area()
        area += image.area()

        if area <= self.size.area():
            self.images.append(image)
            return True
        else:
            return False

    def fillLevel(self):
        area = 0.0
        for r in self.images:
            area += r.area()
        return area / float(self.size.area())

    def draw(self, painter):
        pen = QPen()
        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawRect(self.origin.x, self.origin.y, self.size.width, self.size.height)

        for image in self.images:
            # Rect(rect.origin + self.origin, rect.size, rect.pen).draw(painter=painter)
            image.draw(painter=painter, offset=self.origin)

    def save(self, binName):
        pass

    def __str__(self):
        return '{}({}, {}, {})'.format(self.__class__.__name__, self.origin, self.size, self.images)

    def __repr__(self):
        return self.__str__()
