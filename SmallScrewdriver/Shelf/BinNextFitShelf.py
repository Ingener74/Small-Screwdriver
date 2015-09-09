# encoding: utf8
from SmallScrewdriver import Bin, DEFAULT_BIN_SIZE, Point, Size
from Shelf import Shelf


class BinNextFitShelf(Bin):
    def __init__(self, bin_size=DEFAULT_BIN_SIZE, origin=Point(), *args, **kwargs):
        Bin.__init__(self, size=bin_size, origin=origin)

        self.shelfs = [Shelf(bin_size)]

    def addImage(self, image):
        last_shelf = self.shelfs[-1]
        if last_shelf.addImage(image):
            return Bin.addImage(self, image)
        else:
            max_size = Size(self.size.width, self.size.height - (last_shelf.origin.y + last_shelf.size.height))

            # ... создаём новую полку ...
            shelf = Shelf(max_size, Point(0, last_shelf.origin.y + last_shelf.size.height))

            # ... добавляем её к полками ...
            self.shelfs.append(shelf)

            return Bin.addImage(self, image) if last_shelf.addImage(image) else False
