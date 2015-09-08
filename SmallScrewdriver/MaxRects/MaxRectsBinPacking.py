# encoding: utf8
from SmallScrewdriver import BinPacking


class MaxRectsBinPacking(BinPacking):
    def __init__(self, *args, **kwargs):
        BinPacking.__init__(self, bin_size=kwargs['bin_size'])
