# encoding: utf8
from SmallScrewdriver import Bin, DEFAULT_BIN_SIZE, Point
from Shelf import Shelf


class BinNextFitShelf(Bin):
    def __init__(self, bin_size=DEFAULT_BIN_SIZE, origin=Point(), *args, **kwargs):
        Bin.__init__(self, size=bin_size, origin=origin)

        self.shelfs = [Shelf(self.bin_size)]

    def addImage(self, image):
        pass
