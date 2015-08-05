# encoding: utf8
from SmallScrewdriver import BinPacking
from SmallScrewdriver.Shelf import BinShelf


class RecursiveShelfBinPacking(BinPacking):
    def __init__(self, bin_size, images):
        BinPacking.__init__(self, bin_size=bin_size)

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

        bin = BinShelf(bin_size)
        self.bins.append(bin)

        # Проходим по всем изображениям ...
        for i in self.images:
            # ... и по всем контейнерам ...
            for b in self.bins:

                # ... пробуем вставить изображение в контейнер ...
                if b.addImage(i):
                    # ... если получилось, идём к следующему изображению ...
                    break
            else:
                # ... если не получилось вставить не в однин контейнер, создаём новый ...
                bin = BinShelf(bin_size)
                self.bins.append(bin)

                # ...
                if bin.addImage(i):
                    pass
                else:
                    #
                    raise SystemError(u'Какая та хуйня, сюда мы дойти не должны')
