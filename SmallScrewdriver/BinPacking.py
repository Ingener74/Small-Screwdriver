# encoding: utf8
import sys
import math

from SmallScrewdriver import Size, Point


# noinspection PyPep8Naming
class BinPacking(object):
    def __init__(self, bin, images):
        self.bin = bin

        print 'Before sort'
        for i in images:
            print i

        self.images = sorted(images, key=lambda image: image.crop_region.size.width, reverse=True)

        print 'After sort'
        for i in self.images:
            print i

        self.current_shelf_size = Size()
        self.current_shelf_pos = Point()n
        for i in images:
            # Если на текущеё полке есть место
            if self.bin.size.width - self.current_shelf_size.width >= i.crop_region.size.width:

                # Добавляем изображение в ящик
                self.add_image_to_shelf(i)

            # Если на текущёй полке места нет ...
            else:
                # тогда вставляем ещё одну полку если для неё есть место
                if self.bin.size.height - self.current_shelf_pos.y > i.crop_region.size.height:
                    self.current_shelf_pos.y += self.current_shelf_size.height
                    self.current_shelf_pos.x = 0
                    self.current_shelf_size = Size()

                    self.add_image_to_shelf(i)
                # Если места нет ...
                else:
                    # ... тогда заканчиваем
                    break

        for i in self.bin.images:
            images.remove(i)

        # print 'packing end'

    def add_image_to_shelf(self, image):
        self.current_shelf_size.width += image.crop_region.size.width

        if self.current_shelf_size.height < image.crop_region.size.height:
            self.current_shelf_size.height = image.crop_region.size.height

        image.origin.x = self.current_shelf_pos.x
        image.origin.y = self.current_shelf_pos.y

        self.current_shelf_pos.x += image.crop_region.size.width

        self.bin.append(image)
