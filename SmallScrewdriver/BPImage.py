# encoding: utf8
import sys
from PIL import Image
from PySide.QtGui import QImage, QColor
from SmallScrewdriver import Rect, Size, Point


# noinspection PyPep8Naming
class BPImage(Rect):
    def __init__(self, filename):
        self.filename = filename

        image = Image.open(self.filename)

        self.image = BPImage.convertPil2QImage(image)

        Rect.__init__(self, Point(0, 0), Size(self.image.width(), self.image.height()))

        self.crop_region = Rect(self.origin, self.size)

    # TODO Very slow
    @staticmethod
    def cropImage(image, alphaThreshold):

        x1 = sys.maxint
        y1 = sys.maxint
        x2 = 0
        y2 = 0

        rect = image.rect()
        print rect

        print image.format()

        for x in xrange(image.width()):
            for y in xrange(image.height()):

                pixel = image.pixel(x, y)
                color = QColor(pixel)

                print color

        croped_image = image.copy(rect)
        print croped_image

        return croped_image

    # TODO Very slow
    @staticmethod
    def convertPil2QImage(pil):

        if pil.mode == 'RGB':
            pil = pil.convert('RGBA')

        qimage = QImage(pil.width, pil.height, QImage.Format_ARGB32)

        for x in xrange(0, pil.width):
            for y in xrange(0, pil.height):
                color = pil.getpixel((x, y))
                qimage.setPixel(x, y, QColor(color[0], color[1], color[2], color[3]).rgba())

        return qimage

    def __str__(self):
        print '{}({}, {})'.format(self.__class__.__name__, self.filename, self.image)

    def __repr__(self):
        return self.__str__()
