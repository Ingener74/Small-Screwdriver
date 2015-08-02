# encoding: utf8

from SmallScrewdriver import Rect, Point, Size


# noinspection PyPep8Naming
class Shelf(Rect):
    def __init__(self, maxSize, origin):
        Rect.__init__(self, origin, Size())
        self.maxSize = maxSize
        self.images = []

    def addImage(self, image):
        """
        Добавить изображение на полку
        :param image: добавляемое изображение
        :return: True если изображение может быть добавлено
                 False если не может
        """
        freeSize = Size(self.maxSize.width - self.size.width, self.maxSize.height)
        if freeSize >= image.crop_region.size:

            image.origin = Point(self.size.width, origin)
            self.images.append(image)

            self.size.width += image.crop_region.size.width
            if image.crop_region.size.height > self.size.height:
                self.size.height += image.crop_region.size.height
            return True
        else:
            return False

