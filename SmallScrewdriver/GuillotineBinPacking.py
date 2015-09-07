# coding=utf-8
from SmallScrewdriver import BinPacking, Rect, Point
from Guillotine import BinGuillotine


# noinspection PyPep8Naming
class GuillotineBinPacking(BinPacking):
    def __init__(self, bin_size, images, *args, **kwargs):
        BinPacking.__init__(self, bin_size=bin_size)

        select_variant = kwargs['select_variant'] if 'select_variant' in kwargs else BinGuillotine.BEST_VARIANTS
        select_heuristic = kwargs['select_heuristic'] if 'select_heuristic' in kwargs else BinGuillotine.AREA_FIT
        split_rule = kwargs['split_rule'] if 'split_rule' in kwargs else Rect.RULE_SAS

        # Отсеиваем изображения которые больше размера контейнера
        self.images = filter(lambda image: image.size.less(self.bin_size) == (True, True), images)

        # Создаём первый контейнер
        self.__newContainer(select_heuristic, select_variant, split_rule)

        for i in self.images:
            for b in self.bins:
                if b.addImage(i):
                    break
            else:
                # Не в один из контеёнеров изображение не влезло, делаем ещё один контейнер
                bin = self.__newContainer(select_heuristic, select_variant, split_rule)
                if bin.addImage(i):
                    pass
                else:
                    raise SystemError(u'Какая та хуйня, сюда мы дойти не должны')

                # break

    def __newContainer(self, select_heuristic, select_variant, split_rule):
        bin = BinGuillotine(self.bin_size, Point(), select_variant=select_variant,
                            select_heuristic=select_heuristic, split_rule=split_rule)
        self.bins += [bin]
        return bin
