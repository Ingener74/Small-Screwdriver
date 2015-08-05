# encoding: utf8
from SmallScrewdriver import Bin


class BinShelf(Bin):
    def __init__(self, size, origin):
        Bin.__init__(self, size=size, origin=origin)

    def addImage(self, image):
        pass

