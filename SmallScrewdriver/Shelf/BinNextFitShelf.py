# encoding: utf8
from SmallScrewdriver import Bin, DEFAULT_BIN_SIZE, Point


class BinNextFitShelf(Bin):
    def __init__(self):
        Bin.__init__(self, DEFAULT_BIN_SIZE, Point())

    def addImage(self, image):
        pass


