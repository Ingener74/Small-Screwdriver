# encoding: utf8
from PySide.QtGui import QImage
from PIL import Image
from SmallScrewdriver import Rect, Size, Point
from SillyCrossbow import crop_image


# noinspection PyPep8Naming
class BPImage(Rect):
    def __init__(self, filename):
        self.filename = filename

        image = Image.open(self.filename)
        Rect.__init__(self, Point(), Size(image.width, image.height))

        self.crop_region = Rect()
        image, \
            self.crop_region.origin.x, \
            self.crop_region.origin.y, \
            self.crop_region.size.width, \
            self.crop_region.size.height = crop_image(image, 50)

        self.image = QImage(image.tostring(), image.width, image.height, QImage.Format_ARGB32)

    def __str__(self):
        print '{}({}, {})'.format(self.__class__.__name__, self.filename, self.image)

    def __repr__(self):
        return self.__str__()
