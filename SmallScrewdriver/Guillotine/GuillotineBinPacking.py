# coding=utf-8
from SmallScrewdriver import (BinPacking, DEFAULT_BIN_SIZE)
from SmallScrewdriver.Guillotine import (GuillotineBin)


# noinspection PyPep8Naming,PyShadowingBuiltins
class GuillotineBinPacking(BinPacking):
    def __init__(self, bin_size, images, bin_parameters, progress):

        # Отсеиваем изображения которые больше размера контейнера
        images = filter(lambda image: image.crop.size.less(bin_size) == (True, True), images)

        # TODO Сортировка изображений по (высоте, ширине, площади и прочей хуйне)

        BinPacking.__init__(self, bin_size, images, bin_parameters, progress)

    def _newBin(self, size, bin_parameters):
        self.bins.append(GuillotineBin(size, bin_parameters))
        return self.bins[-1]
