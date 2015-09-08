# coding=utf-8
from SmallScrewdriver import BinPacking, Rect, Point
from Guillotine import BinGuillotine


# noinspection PyPep8Naming
class GuillotineBinPacking(BinPacking):
    def __init__(self, bin_size, images, *args, **kwargs):

        # Отсеиваем изображения которые больше размера контейнера
        images = filter(lambda image: image.size.less(bin_size) == (True, True), images)

        BinPacking.__init__(self, bin_size=bin_size, images=images, *args, **kwargs)

    def _newBin(self, *args, **kwargs):
        bin = BinGuillotine(self.bin_size, Point(), *args, **kwargs)
        self.bins += [bin]
        return bin
