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

                    shelf = Shelf(bin.size)
                    self.shelfs.append(shelf)

    def saveAtlases(self, directory):
        for i, b in enumerate(self.bins):
            b.save(directory + '/atlas' + str(i))
