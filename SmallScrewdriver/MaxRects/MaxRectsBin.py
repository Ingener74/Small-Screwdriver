# coding: utf-8
from SmallScrewdriver import Bin, DEFAULT_BIN_SIZE, Point


class MaxRectsBin(Bin):
    def __init__(self, size=DEFAULT_BIN_SIZE, origin=Point(), bin_parameters=None):
        Bin.__init__(size=size, origin=origin, bin_parameters=bin_parameters)

    def addImage(self, image):
        return False

