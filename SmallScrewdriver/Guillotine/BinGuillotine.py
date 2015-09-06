# coding=utf-8

from SmallScrewdriver import Bin, DEFAULT_BIN_SIZE, Point, Rect


class BinGuillotine(Bin):
    """
    Контейнер для метода гильотины
    """

    BEST_VARIANTS = 0
    WORST_VARIANTS = 1

    AREA_FIT = 0
    SHORT_SIDE_FIT = 1
    LONG_SIDE_FIT = 2

    def __init__(self, size=DEFAULT_BIN_SIZE, origin=Point(), *args, **kwargs):
        Bin.__init__(self, size=size, origin=origin)

        self.select_variant = kwargs['select_variant'] if 'select_variant' in kwargs else BinGuillotine.BEST_VARIANTS
        self.select_heuristic = kwargs['select_heuristic'] if 'select_heuristic' in kwargs else BinGuillotine.AREA_FIT
        self.split_rule = kwargs['split_rule'] if 'split_rule' in kwargs else Rect.RULE_SAS

        self.splits = [Rect(size=self.size)]

    def addImage(self, image):

        af = lambda x: x.area()
        ssf = lambda x: min(x.width() - image.size.width(), x.height() - image.size.height())
        lsf = lambda x: max(x.width() - image.size.width(), x.height() - image.size.height())

        # foo1 = filter([af, ssf, lsf][self.select_heuristic], self.splits)

        foo2 = sorted(self.splits, key=[af, ssf, lsf][self.select_heuristic], reverse=bool(self.select_variant))

        for rect in foo2:
            s, rs1, rs2, rotate = rect.split(image.crop, self.split_rule)

            if s > 0:
                image.origin = rect.origin
                image.rotated = rotate
                if s == 2:
                    self.splits.remove(rect)
                    self.splits += [rs1, rs2]
                    return Bin.addImage(self, image)
                elif s == 1:
                    self.splits.remove(rect)
                    self.splits += [rs1]
                    return Bin.addImage(self, image)
                else:
                    raise RuntimeError(u'Что то странное')
