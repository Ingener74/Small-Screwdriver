# encoding: utf8
from SmallScrewdriver import BinPacking, DEFAULT_BIN_SIZE
from MaxRectsBin import MaxRectsBin


class MaxRectsBinPacking(BinPacking):
    def __init__(self, bin_size=DEFAULT_BIN_SIZE, images=None, bin_parameters=None):

        # Оставляем только изображения входящие по размеру в контейнер
        images = filter(lambda image: image.crop.size.less(bin_size) == (True, True), images)

        BinPacking.__init__(self,
                            bin_size=bin_size,
                            images=images,
                            bin_parameters=bin_parameters)

    def _newBin(self, size, bin_parameters):
        self.bins.append(MaxRectsBin(size, bin_parameters))
        return self.bins[-1]
