# encoding: utf8
from SmallScrewdriver import BinPacking, Bin, Shelf, Size, Point


class RecursiveShelfBinPacking(BinPacking):
    def __init__(self, bin_size, images):
        BinPacking.__init__(self, bin_size=bin_size)

        self.images = []
        for i in images:
            if i.crop.size < self.bin_size:
                self.images.append(i)

        for i in self.images:
            if i.crop.size.width > i.crop.size.height:
                i.rotated = True

        # TODO выкинуть все изображения размер которых больше размера контейнера
        self.images = sorted(self.images,
                             key=lambda im: im.crop.size.width if im.rotated else im.crop.size.height,
                             reverse=True)

        self.shelfs = []

        bin = Bin(bin_size)
        self.bins.append(bin)

        shelf = Shelf(max_size=bin.size)
        self.shelfs.append(shelf)

        # Проходим по всем изображениям ...
        for i in self.images:
            # ... и по всем полкам ...
            for s in self.shelfs:

                # ... пробуем вставить изображение в полку ...
                if s.addImage(i):
                    # ... если получилось, идём к следующему изображению ...
                    bin.append(i)
                    break
                else:
                    # ... если не получилось, создаём новую полку ...
                    max_size = Size(bin.size.width, bin.size.height - (shelf.origin.y + shelf.size.height))
                    origin = Point(0, shelf.origin.y + shelf.size.height)
                    shelf = Shelf(max_size=max_size, origin=origin)

                    self.shelfs.append(shelf)

                    # ... пробуем вставить изображение в новую полку ...
                    if shelf.addImage(i):
                        # ... если получилось, идём к следующему изображению ...
                        bin.append(i)
                        break
                    else:
                        # ... если нет, создаём новый контейнер и полку

                        bin = Bin(bin_size)
                        self.bins.append(bin)

                        shelf = Shelf(max_size=bin.size)
                        self.shelfs.append(shelf)

                        # ... пробуем вставить изображение в новый контейнер на новой полке
                        if shelf.addImage(i):
                            bin.append(i)
                            break
                        else:
                            raise SystemError(u'Какая та хуйня, сюда мы дойти не должны')

        for i, b in enumerate(self.bins):
            b.origin = Point(i * self.bin_size.width + i*5 + 5, 0)

        for b in self.bins:
            print 'fill level ', b.fillLevel()
