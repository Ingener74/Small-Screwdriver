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

        print len(images)
        # Отсеиваем изображения которые больше размера контейнера
        self.images = filter(lambda image: image.size.less(self.bin_size) == (True, True), images)
        print len(self.images)

        # Создаём первый контейнер
        self.__newContainer(select_heuristic, select_variant, split_rule)

        for i in self.images:
            for b in self.bins:
                print u'Помещаем изображение ', i
                if b.addImage(i):
                    self.images.remove(i)
                    break
                else:
                    print u'Изображение не вошло'
            else:
                print u'Новый контейнер'
                # Не в один из контеёнеров изображение не влезло, делаем ещё один контейнер
                self.__newContainer(select_heuristic, select_variant, split_rule)

            # break

    def __newContainer(self, select_heuristic, select_variant, split_rule):
        self.bins += [BinGuillotine(self.bin_size,
                                    Point(),
                                    select_variant=select_variant,
                                    select_heuristic=select_heuristic,
                                    split_rule=split_rule)]