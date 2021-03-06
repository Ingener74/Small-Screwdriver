# encoding: utf8
from SmallScrewdriver import (Bin, Point, Size)
from Shelf import (Shelf)


# noinspection PyPep8Naming
class ShelfBin(Bin):
    def __init__(self, size, bin_parameters=None):
        Bin.__init__(self, size, bin_parameters)

        self.shelfs = [Shelf(self.size)]

    def _newShelf(self):
        shelf = self.shelfs[-1]
        new_y = shelf.origin.y + shelf.size.height
        max_size = Size(self.size.width, self.size.height - new_y)

        # ... создаём новую полку ...
        shelf = Shelf(max_size, Point(0, new_y))

        # ... добавляем её к полками ...
        self.shelfs.append(shelf)

        return shelf
