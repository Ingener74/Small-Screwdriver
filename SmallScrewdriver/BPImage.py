# encoding: utf8
from PySide.QtCore import QPoint

from PySide.QtGui import QImage, QColor, QPixmap
from PIL import Image
from SmallScrewdriver import Rect, Size, Point
from SillyCrossbow import crop_image3


# noinspection PyPep8Naming
class BPImage(Rect):
    def __init__(self, filename):
        self.filename = filename

        image = Image.open(self.filename)
        Rect.__init__(self, Point(), Size(image.width, image.height))

        self.crop_region = Rect()
        self.image, \
            self.crop_region.origin.x, \
            self.crop_region.origin.y, \
            self.crop_region.size.width, \
            self.crop_region.size.height = crop_image3(image, 50)

    def area(self):
        return self.crop_region.area()

    def draw(self, painter, offset):
        painter.drawImage(QPoint(self.origin.x + offset.x,
                                  self.origin.y + offset.y), self.image)
        self.crop_region.draw(painter, offset)
        # Rect.draw(self, painter, offset)

    def __str__(self):
        print '{}({}, {})'.format(self.__class__.__name__, self.filename, self.image)

    def __repr__(self):
        return self.__str__()
