# encoding: utf8
import json
from PySide.QtCore import (QPoint, Qt, QDir, QFile, QFileInfo)
from PySide.QtGui import (QImage, QTransform)

from SmallScrewdriver import (Rect, Size, Point)
from SillyCrossbow import (crop_image)


# noinspection PyPep8Naming,PyUnusedLocal
class Image(Rect):
    """
    self.origin - показывает положение в атласе
    self.size   - оригинальный размер изображения
    self.crop   - область изображения взятого из оригинала после обрезания прозрачных краёв
    """

    BorderPadding = 1
    CropThreshold = 10

    def __init__(self, directory, filename):
        self.directory = directory
        self.filename = filename

        image = QImage(self.directory + QDir.separator() + self.filename)

        Rect.__init__(self, Point(), Size(image.width(), image.height()))

        cropped_image, x, y, width, height = self.__getCrop(image)

        self.crop = Rect(Point(x, y), Size(width, height))

        self.rotated = False

    def area(self):
        return self.crop.area()

    def draw(self, painter, offset=Point()):
        cropped_image, x, y, width, height = self.__getCrop()

        origin_offset = QPoint(self.origin.x + offset.x, self.origin.y + offset.y)

        if self.rotated:
            old_transform = QTransform(painter.transform())
            painter.setTransform(painter.transform().translate(origin_offset.x() + self.crop.size.height,
                                                               origin_offset.y()).rotate(90, Qt.ZAxis))
            painter.drawImage(0, 0, cropped_image)
            painter.setTransform(old_transform)
        else:
            painter.drawImage(origin_offset, cropped_image)
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
            'crop': {
                'origin': {
                    'x': self.crop.origin.x,
                    'y': self.crop.origin.y
                },
                'size': {
                    'width': self.crop.size.width,
                    'height': self.crop.size.height
                }
            },
            'rotated': self.rotated,
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

    def __getCrop(self, image=None):
        if self.__hasCrop():
            cropped_image, crop_info = self.__loadCrop()
            x, y, width, height = crop_info['x'], crop_info['y'], crop_info['width'], crop_info['height']
        else:
            if not image:
                raise RuntimeError('Image is none')
            cropped_image, x, y, width, height = crop_image(image, Image.CropThreshold)
            self.__saveCrop(cropped_image, x, y, width, height)
        return cropped_image, x, y, width, height

    def __getFileNameWoExt(self):
        image = QFileInfo(self.directory + QDir.separator() + self.filename)
        return image.absoluteDir().absolutePath() + QDir.separator() + image.baseName()

    def __hasCrop(self):
        name_wo_ext = self.__getFileNameWoExt()
        crop_info_exists = QFileInfo(name_wo_ext + '.json').exists()
        crop_image_exists = QFileInfo(name_wo_ext + '.crop').exists()
        exists = crop_info_exists and crop_image_exists
        return exists

    def __saveCrop(self, image, x, y, width, height):
        image.save(self.__getFileNameWoExt() + '.crop', 'PNG')
        with open(self.__getFileNameWoExt() + '.json', 'w') as f:
            json.dump({
                'x': x,
                'y': y,
                'width': width,
                'height': height
            }, fp=f)

    def __loadCrop(self):
        name_wo_ext = self.__getFileNameWoExt()
        json_data = open(name_wo_ext + '.json').read()
        image = QImage()
        image.load(name_wo_ext + '.crop', 'PNG')
        return image, json.loads(json_data)
