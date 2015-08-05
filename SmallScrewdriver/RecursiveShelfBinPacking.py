# encoding: utf8
from SmallScrewdriver import BinPacking, Bin, Shelf


class RecursiveShelfBinPacking(BinPacking):
    def __init__(self, bin_size, images):
        BinPacking.__init__(self, bin_size=bin_size)

        for i in images:
            if i.crop.size.width > i.crop.size.height:
                i.rotated = True

        self.images = sorted(images,
                             key=lambda im: im.crop.size.width if im.rotated else im.crop.size.height,
                             reverse=True)

        self.shelfs = []

        bin = Bin(bin_size)
        self.bins.append(bin)

        shelf = Shelf(max_size=bin.size)
        self.shelfs.append(shelf)

        for i in self.images:
            pass

