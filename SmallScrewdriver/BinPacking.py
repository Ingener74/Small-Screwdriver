# encoding: utf8

from SmallScrewdriver import Size, Point


# noinspection PyPep8Naming
class BinPacking(object):
    def __init__(self, bin, images):
        self.bin = bin

        self.images = sorted(images, key=lambda image: image.crop_region.size.width, reverse=True)

        self.current_shelf_size = Size()
        self.current_shelf_pos = Point()
        for i in self.images:
            # Если на текущеё полке есть место
            if self.bin.size.width - self.current_shelf_size.width >= i.crop_region.size.width:

                # Добавляем изображение в ящик
                self.addImage2Shelf(i)

            # Если на текущёй полке места нет ...
            else:
                # тогда вставляем ещё одну полку если для неё есть место
                if self.bin.size.height - self.current_shelf_pos.y > i.crop_region.size.height:
                    self.current_shelf_pos.y += self.current_shelf_size.height
                    self.current_shelf_pos.x = 0
                    self.current_shelf_size = Size()

                    self.addImage2Shelf(i)
                # Если места нет ...
                else:
                    # ... тогда заканчиваем
                    break

        for i in self.bin.images:
            images.remove(i)

    def addImage2Shelf(self, image):
        self.current_shelf_size.width += image.crop_region.size.width

        if self.current_shelf_size.height < image.crop_region.size.height:
            self.current_shelf_size.height = image.crop_region.size.height

        image.origin.x = self.current_shelf_pos.x
        image.origin.y = self.current_shelf_pos.y

        self.current_shelf_pos.x += image.crop_region.size.width

        self.bin.append(image)

    def saveAtlases(self, directory):
        pass