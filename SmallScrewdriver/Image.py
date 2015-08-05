# encoding: utf8
from PySide.QtCore import QPoint
from PySide.QtGui import QImage

from SmallScrewdriver import Rect, Size, Point
from SillyCrossbow import crop_image


# noinspection PyPep8Naming,PyUnusedLocal
class Image(Rect):
    """
    self.origin        - показывает положение в атласе
    self.size          - оригинальный размер изображения
    self.crop   - область изображения взятого из оригинала после обрезания прозрачных краёв
    """

    def __init__(self, filename):
        self.filename = filename

        image = QImage(self.filename)

        Rect.__init__(self, Point(), Size(image.width(), image.height()))

        self.image, x, y, width, height = crop_image(image, 50)
        self.crop = Rect(Point(x, y), Size(width, height))

        self.rotated = False

    def area(self):
        return self.crop.area()

    def draw(self, painter, offset):
        painter.drawImage(QPoint(self.origin.x + offset.x,
                                 self.origin.y + offset.y), self.image)
        # Rect(self.origin, self.crop.size).draw(painter, offset)

    def toJson(self):
        return {
            'offset': {
                'x': self.origin.x,
                'y': self.origin.y
            },
            'original_size': {
                'width': self.size.width,
                'height': self.size.height
            },
            'cropped_image': {
                'origin': {
                    'x': self.crop.origin.x,
                    'y': self.crop.origin.y
                },
                'size': {
                    'width': self.crop.size.width,
                    'height': self.crop.size.height
                }
            },
            'filename': self.filename
        }

    # noinspection PyUnreachableCode
    def __str__(self):
        return '{klass}({file}, {origin}, {size}, {crop}, {rotated})'.format(klass=self.__class__.__name__,
                                                                             file=self.filename,
                                                                             crop=self.crop,
                                                                             origin=self.origin,
                                                                             size=self.size,
                                                                             rotated=self.rotated)

    def __repr__(self):
        return self.__str__()
