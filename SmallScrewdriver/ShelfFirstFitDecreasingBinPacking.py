# encoding: utf8

from SmallScrewdriver import Size, Point, BinPacking, Bin, Shelf


# noinspection PyPep8Naming
class ShelfFirstFitDecreasingBinPacking(BinPacking):
    def __init__(self, bin_size, images):
        BinPacking.__init__(self, bin_size=bin_size)

        self.shelfs = []

        # TODO выкинуть все изображения размер которых больше размера контейнера
        self.images = sorted(images, key=lambda image: image.crop.size.width, reverse=True)

        bin = Bin(self.bin_size)
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
                    bin = Bin(self.bin_size)
                    self.bins.append(bin)

                    shelf = Shelf(bin.size)
                    self.shelfs.append(shelf)

        for i, b in enumerate(self.bins):
            b.origin = Point(i * self.bin_size.width + i*5 + 5, 0)

        for b in self.bins:
            print 'fill level ', b.fillLevel()

