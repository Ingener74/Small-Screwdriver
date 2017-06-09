# encoding: utf8

import os

from PySide.QtCore import Qt
from PySide.QtGui import (QPen, QImage, QPainter)

from Exporters import Exporter
from SmallScrewdriver import Size, Point, Rect

DEFAULT_BIN_SIZE = Size(256, 256)


# noinspection PyPep8Naming
class Bin(object):

    EXPORTER = 0

    DRAW_MODE_NORMAL = 0
    DRAW_MODE_DEBUG = 1
    DRAW_MODE_RELEASE = 2

    def __init__(self, size, bin_parameters=None):
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

    def draw(self, painter, offset, draw_mode=DRAW_MODE_NORMAL):

        if draw_mode != Bin.DRAW_MODE_RELEASE:
            # Рисуем контур контейнера
            pen = QPen()
            pen.setStyle(Qt.DashLine)
            painter.setPen(pen)
            # painter.drawRect(self.origin.x, self.origin.y, self.size.width, self.size.height)
            painter.drawRect(offset.x, offset.y, self.size.width, self.size.height)

        for image in self.images:
            # Rect(rect.origin + self.origin, rect.size, rect.pen).draw(painter=painter)
            # image.draw(painter=painter, offset=self.origin)
            image.draw(painter=painter, offset=offset)

    def save(self, bin_name):
        # Создаём изображение для контейнера
        image = QImage(self.size.width, self.size.height, QImage.Format_ARGB32)

        # Рисуем контейнер в изображение
        painter = QPainter(image)
        self.draw(painter, Point(), draw_mode=self.DRAW_MODE_RELEASE)

        bin_file_name = bin_name + '.png'

        # Если изображение для контейнера существует, удаляем
        if os.path.exists(bin_file_name):
            os.remove(bin_file_name)

        # Сохраняем изображение контейнера
        image.save(bin_file_name)
        painter.end()

        self.bin_parameters[Bin.EXPORTER]().export(bin_name, self.size, self.images)

    def __verify(self, image0, images):
        for image in images:
            if image.intersection(image0) != Rect():
                pass

        self.__verify(images[0], images[1:])

    def verify(self):
        """
        Верификация изображений в контейнере проверяем что изображения в контейнере не накладываются друг на друга
        :return:
        """
        self.__verify(self.images[0], self.images[1:])

    def __str__(self):
        return '{}({}, {})'.format(self.__class__.__name__, self.size, self.images)

    def __repr__(self):
        return self.__str__()
