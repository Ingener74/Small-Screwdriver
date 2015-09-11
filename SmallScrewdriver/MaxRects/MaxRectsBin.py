# coding: utf-8
from SmallScrewdriver import Bin, DEFAULT_BIN_SIZE, Point


class MaxRectsBin(Bin):
    def __init__(self):
        Bin.__init__(self, size=DEFAULT_BIN_SIZE, origin=Point())

    def addImage(self, image):
        return False

