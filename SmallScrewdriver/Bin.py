# encoding: utf8
import json

from PySide.QtCore import Qt
from PySide.QtGui import (QPen, QImage, QPainter)

import os
from SmallScrewdriver import Size, Point

DEFAULT_BIN_SIZE = Size(256, 256)


# noinspection PyPep8Naming
class Bin(object):
    def __init__(self, size=DEFAULT_BIN_SIZE, origin=Point(0, 0), bin_parameters=None):
        self.origin = origin
        self.size = size
        self.bin_parameters = bin_parameters
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
        # Создаём изображение для контейнера
        image = QImage(self.size.width, self.size.height, QImage.Format_ARGB32)

        # Рисуем контейнер в изображение
        painter = QPainter(image)
        self.draw(painter, Point())

        bin_file_name = binName + '.png'

        # Если изображение для контейнера существует, удаляем
        if os.path.exists(bin_file_name):
            os.remove(bin_file_name)

        # Сохраняем изображение контейнера
        image.save(bin_file_name)
        painter.end()

        # Собираем json файл для контейнера
        json_images = []
        for i in self.images:
            json_images.append(i.toJson())

        # Сохраняем json файл для контейнера
        with open(binName + '.json', mode='w') as outfile:
            json.dump(obj=json_images, fp=outfile, separators=(',', ':'), indent=4)

    def __str__(self):
        return '{}({}, {}, {})'.format(self.__class__.__name__, self.origin, self.size, self.images)

    def __repr__(self):
        return self.__str__()
