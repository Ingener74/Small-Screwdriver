# encoding: utf8
from PySide.QtCore import QPoint

from PIL import Image
from SmallScrewdriver import Rect, Size, Point
from SillyCrossbow import crop_image3


# noinspection PyPep8Naming
class BPImage(Rect):
    """
    self.origin        - показывает положение в атласе
    self.size          - оригинальный размер изображения
    self.crop_region   - область изображения взятого из оригинала после обрезания прозрачных краёв
    """

    def __init__(self, filename):
        self.filename = filename

        image = Image.open(self.filename)
        Rect.__init__(self, Point(), Size(image.width, image.height))

        self.image, x, y, width, height = crop_image3(image, 50)
        self.crop_region = Rect(Point(x, y), Size(width, height))

    def area(self):
        return self.crop_region.area()

    def draw(self, painter, offset):
        painter.drawImage(QPoint(self.origin.x + offset.x,
                                 self.origin.y + offset.y), self.image)
        # Rect(self.origin, self.crop_region.size).draw(painter, offset)

    def __str__(self):
        return '{}({file}, {crop}, {origin}, {size})'.format(self.__class__.__name__,
                                                             file=self.filename,
                                                             crop=self.crop_region,
                                                             origin=self.origin,
                                                             size=self.size)

    def __repr__(self):
        return self.__str__()
