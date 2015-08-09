# coding=utf-8
from SmallScrewdriver import Bin, DEFAULT_BIN_SIZE, Point, Rect


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

    def __init__(self, size=DEFAULT_BIN_SIZE, origin=Point(), selection_heuristic=BAF,
                 split_rule=Rect.RULE_SAS):
        Bin.__init__(self, size=size, origin=origin)

        self.selection_heuristic = selection_heuristic
        self.split_rule = split_rule
        self.splits = []

    def addImage(self, image):
        return False
