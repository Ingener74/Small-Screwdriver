# coding=utf-8
from SmallScrewdriver import BinPacking, Rect, Point
from SmallScrewdriver.Guillotine import BinGuillotine


# noinspection PyPep8Naming,PyShadowingBuiltins
class GuillotineBinPacking(BinPacking):
    def __init__(self, bin_size, images, *args, **kwargs):

        # Отсеиваем изображения которые больше размера контейнера
        images = filter(lambda image: image.size.less(bin_size) == (True, True), images)

        BinPacking.__init__(self, bin_size=bin_size, images=images, *args, **kwargs)

    def _newBin(self, *args, **kwargs):
        self.bins.append(BinGuillotine(self.bin_size, Point(), *args, **kwargs))
        return self.bins[-1]
