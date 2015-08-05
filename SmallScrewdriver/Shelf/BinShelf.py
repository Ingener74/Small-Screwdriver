# encoding: utf8
from SmallScrewdriver import Bin, Size, Point, DEFAULT_BIN_SIZE
from SmallScrewdriver.Shelf import Shelf


class BinShelf(Bin):
    def __init__(self, size=DEFAULT_BIN_SIZE, origin=Point()):
        Bin.__init__(self, size=size, origin=origin)

        self.shelfs = [Shelf(self.size)]

    def addImage(self, image):
        for s in self.shelfs:
            if s.addImage(image):
                Bin.addImage(self, image)
                return True
        else:
            max_size = Size(self.size.width, self.size.height - (s.origin.y + s.size.height))
            origin = Point(0, s.origin.y + s.size.height)
            shelf = Shelf(max_size, origin)
            self.shelfs.append(shelf)

            if shelf.addImage(image):
                Bin.addImage(self, image)
                return True
            else:
                return False
