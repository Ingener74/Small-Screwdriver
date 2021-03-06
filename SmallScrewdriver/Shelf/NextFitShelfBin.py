# encoding: utf8
from SmallScrewdriver import Bin, DEFAULT_BIN_SIZE, Point
from ShelfBin import ShelfBin


class NextFitShelfBin(ShelfBin):
    def __init__(self, size, bin_parameters=None):
        ShelfBin.__init__(self, size, bin_parameters)

    def addImage(self, image):
        return \
            Bin.addImage(self, image) if self.shelfs[-1].addImage(image) else \
            Bin.addImage(self, image) if self._newShelf().addImage(image) else \
            False
