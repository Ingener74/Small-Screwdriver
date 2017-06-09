# encoding: utf8

from SmallScrewdriver import BinPacking, DEFAULT_BIN_SIZE
from SmallScrewdriver.Shelf import NextFitShelfBin


# noinspection PyPep8Naming
class NextFitShelfBinPacking(BinPacking):
    def __init__(self, bin_size, images, bin_parameters, progress):
        # TODO выкинуть все изображения размер которых больше размера контейнера
        self.images = sorted(images, key=lambda image: image.crop.size.width, reverse=True)

        BinPacking.__init__(self, bin_size, images, bin_parameters, progress)

    def _newBin(self, size, bin_parameters):
        self.bins.append(NextFitShelfBin(size, bin_parameters))
        return self.bins[-1]
