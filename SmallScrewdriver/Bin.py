# encoding: utf8
import json

from PySide.QtCore import Qt
from PySide.QtGui import (QPen, QImage, QPainter)

from SmallScrewdriver import Size, Point


DEFAULT_BIN_SIZE = Size(256, 256)


# noinspection PyPep8Naming
class Bin(object):
    def __init__(self, size=DEFAULT_BIN_SIZE, origin=Point(0, 0), *args, **kwargs):
        self.origin = origin
        self.size = size
        self.images = []

    def addImage(self, image):
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

    def draw(self, painter, offset):
        pen = QPen()
        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        # painter.drawRect(self.origin.x, self.origin.y, self.size.width, self.size.height)
        painter.drawRect(offset.x, offset.y, self.size.width, self.size.height)

        for image in self.images:
            # Rect(rect.origin + self.origin, rect.size, rect.pen).draw(painter=painter)
            # image.draw(painter=painter, offset=self.origin)
            image.draw(painter=painter, offset=offset)

    def save(self, binName):
        image = QImage(self.size.width, self.size.height, QImage.Format_ARGB32)
        painter = QPainter(image)
        self.draw(painter, Point())
        image.save(binName + '.png')
        painter.end()

        json_images = []
        for i in self.images:
            json_images.append(i.toJson())

        with open(binName + '.json', mode='w') as outfile:
            json.dump(obj=json_images, fp=outfile, separators=(',', ':'), indent=4)

    def __str__(self):
        return '{}({}, {}, {})'.format(self.__class__.__name__, self.origin, self.size, self.images)

    def __repr__(self):
        return self.__str__()
