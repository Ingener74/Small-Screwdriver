# encoding: utf8
from SmallScrewdriver import BinPacking
from SmallScrewdriver.Shelf import BinShelf


# noinspection PyPep8Naming
class ShelfFirstFitBinPacking(BinPacking):
    def __init__(self, bin_size, images):
        BinPacking.__init__(self, bin_size=bin_size)

        # Отсеиваем изображения размер которых больше или равен размеру контейнера
        self.images = filter(lambda image: image.size.less(self.bin_size) == (True, True), images)

        # Ориентируем все изображения по вертикали
        def rotate(image):
            if image.crop.size.width > image.crop.size.height:
                image.rotated = True
            return image
        self.images = map(rotate, self.images)

        # Сортируем по высоте
        self.images = sorted(self.images,
                             key=lambda im: im.crop.size.width if im.rotated else im.crop.size.height,
                             reverse=True)

        self.__newBin(bin_size)

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
                bin = self.__newBin(bin_size)

                # ...
                if bin.addImage(i):
                    pass
                else:
                    #
                    raise SystemError(u'Какая та хуйня, сюда мы дойти не должны')

    def __newBin(self, bin_size):
        bin = BinShelf(bin_size)
        self.bins += [bin]
        return bin
