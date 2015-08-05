# encoding: utf8
from SmallScrewdriver import Bin, DEFAULT_BIN_SIZE, Point


class BinGuillotine(Bin):
    def __init__(self, size=DEFAULT_BIN_SIZE, origin=Point()):
        Bin.__init__(self, size=size, origin=origin)

    def addImage(self, image):
        return False