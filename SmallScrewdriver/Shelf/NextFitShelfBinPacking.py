# encoding: utf8

from SmallScrewdriver import BinPacking
from SmallScrewdriver.Shelf import NextFitShelfBin


# noinspection PyPep8Naming
class NextFitShelfBinPacking(BinPacking):
    def __init__(self, bin_size, images, *args, **kwargs):
        # TODO выкинуть все изображения размер которых больше размера контейнера
        self.images = sorted(images, key=lambda image: image.crop.size.width, reverse=True)

        BinPacking.__init__(self, bin_size=bin_size, images=images, *args, **kwargs)

    def _newBin(self, *args, **kwargs):
        self.bins.append(NextFitShelfBin(*args, **kwargs))
        return self.bins[-1]
