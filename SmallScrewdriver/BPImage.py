# encoding: utf8
from PySide.QtCore import QPoint

from PySide.QtGui import QImage, QColor, QPixmap
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
        cimage, \
            self.crop_region.origin.x, \
            self.crop_region.origin.y, \
            self.crop_region.size.width, \
            self.crop_region.size.height = crop_image(image, 50)

        # QImage(cimage.tostring(), cimage.width, cimage.height, QImage.Format_ARGB32)
        self.image = BPImage.convertPil2QImage(cimage)

    # TODO Very slow
    @staticmethod
    def convertPil2QImage(pil):

        if pil.mode == 'RGB':
            # pil = pil.convert('RGBA')
            raise RuntimeError('RGBA only')

        qimage = QImage(pil.width, pil.height, QImage.Format_ARGB32)

        for x in xrange(0, pil.width):
            for y in xrange(0, pil.height):
                color = pil.getpixel((x, y))
                qimage.setPixel(x, y, QColor(color[0], color[1], color[2], color[3]).rgba())

        return qimage

    def draw(self, painter):
        painter.drawPixmap(QPoint(self.crop_region.origin.x, self.crop_region.origin.y), QPixmap(self.image))
        self.crop_region.draw(painter)
        Rect.draw(self, painter)

    def __str__(self):
        print '{}({}, {})'.format(self.__class__.__name__, self.filename, self.image)

    def __repr__(self):
        return self.__str__()
