# encoding: utf8
from SmallScrewdriver import Bin, DEFAULT_BIN_SIZE, Point


class BinGuillotine(Bin):

    """
    Free selection heuristics
    """
    BAF = 0
    BSSF = 1
    BLSF = 2
    WAF = 3
    WSSF = 4
    WLSF = 5

    def __init__(self, size=DEFAULT_BIN_SIZE, origin=Point()):
        Bin.__init__(self, size=size, origin=origin)

        self.splits = []

    def addImage(self, image):
        return False