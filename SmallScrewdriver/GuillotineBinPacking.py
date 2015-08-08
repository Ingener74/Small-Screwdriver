# coding=utf-8
from SmallScrewdriver import BinPacking
from Guillotine import BinGuillotine


class GuillotineBinPacking(BinPacking):
    def __init__(self, bin_size, images, selection_heuristic=BinGuillotine):
        BinPacking.__init__(self, bin_size=bin_size)

        self.selection_heuristic = selection_heuristic
        self.images = []

        # Bыкидываем все изображения размер которых больше или равен размеру контейнера
        for i in images:
            if i.crop.size < self.bin_size:
                self.images.append(i)

        # ориентировать все изображения по вертикали
        for i in self.images:
            if i.crop.size.width > i.crop.size.height:
                i.rotated = True

        # сортировать по высоте
        self.images = sorted(self.images,
                             key=lambda im: im.crop.size.width if im.rotated else im.crop.size.height,
                             reverse=True)

        for i in self.images:
            print i