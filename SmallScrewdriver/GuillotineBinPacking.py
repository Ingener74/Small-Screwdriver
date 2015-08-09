# coding=utf-8
from SmallScrewdriver import BinPacking, Rect, Point
from Guillotine import BinGuillotine


class GuillotineBinPacking(BinPacking):
    def __init__(self, bin_size, images, *args, **kwargs):
        BinPacking.__init__(self, bin_size=bin_size)

        self.selection_heuristic = kwargs.get('selection_heuristic', BinGuillotine.BAF)
        self.split_rule = kwargs.get('split_rule', Rect.RULE_SAS)
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

        bin = BinGuillotine(self.bin_size, Point(), self.selection_heuristic, self.split_rule)

        for i in self.images:
            for b in self.bins:

                if b.addImage(i):
                    pass
                else:
                    pass