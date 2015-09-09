# encoding: utf8
from SmallScrewdriver import BinPacking
from SmallScrewdriver.Shelf import BinFirstFitShelf


# noinspection PyPep8Naming,PyShadowingBuiltins
class ShelfFirstFitBinPacking(BinPacking):
    def __init__(self, bin_size, images, *args, **kwargs):

        # Отсеиваем изображения размер которых больше или равен размеру контейнера
        images = filter(lambda image: image.size.less(bin_size) == (True, True), images)

        # Ориентируем все изображения по вертикали
        def rotate(image):
            if image.crop.size.width > image.crop.size.height:
                image.rotated = True
            return image
        images = map(rotate, images)

        # Сортируем по высоте
        images = sorted(images,
                        key=lambda im: im.crop.size.width if im.rotated else im.crop.size.height,
                        reverse=True)

        BinPacking.__init__(self, bin_size=bin_size, images=images, *args, **kwargs)

    def _newBin(self, *args, **kwargs):
        size = kwargs['bin_size']
        del kwargs['bin_size']
        self.bins.append(BinFirstFitShelf(size=size, *args, **kwargs))
        return self.bins[-1]
