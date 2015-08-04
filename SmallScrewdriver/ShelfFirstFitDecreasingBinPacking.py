# encoding: utf8

from SmallScrewdriver import Size, Point, BinPacking, Bin, Shelf


# noinspection PyPep8Naming
class ShelfFirstFitDecreasingBinPacking(BinPacking):
    def __init__(self, binSize, images):

        self.binSize = binSize

        self.bins = []

        self.shelfs = []

        self.images = sorted(images, key=lambda image: image.crop_region.size.width, reverse=True)

        self.current_shelf_size = Size()
        self.current_shelf_pos = Point()

        bin = Bin(self.binSize)
        self.bins.append(bin)

        shelf = Shelf(bin.size)
        self.shelfs.append(shelf)

        for i in self.images:

            # Добавляем изображение на полку
            if shelf.addImage(i):
                bin.append(i)
            else:
                # ... если не можем, добавляем новую полку...
                shelf = Shelf(Size(bin.size.width, bin.size.height - (shelf.origin.y + shelf.size.height)),
                              shelf.origin + Point(0, shelf.size.height))
                self.shelfs.append(shelf)

                # ... пробуем добавить изображение на новую полку ...
                if shelf.addImage(i):
                    bin.append(i)
                else:
                    # ... если даже в новую полку мы добавить не можем, добавляем новый контейнер
                    bin = Bin(self.binSize)
                    self.bins.append(bin)

                    # bin =


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

    def __new_bin(self):
        bin = Bin(self.binSize)
        self.bins.append(bin)

        shelf = Shelf(bin.size)
        self.shelfs.append(shelf)

    def __new_shelf(self, shelf):
        shelf = Shelf(Size(bin.size.width, bin.size.height - (shelf.origin.y + shelf.size.height)),
                      shelf.origin + Point(0, shelf.size.height))
        self.shelfs.append(shelf)

    def saveAtlases(self, directory):
        pass
