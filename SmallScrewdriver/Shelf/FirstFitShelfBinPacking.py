# encoding: utf8
from SmallScrewdriver import BinPacking, DEFAULT_BIN_SIZE
from SmallScrewdriver.Shelf import FirstFitShelfBin


# noinspection PyPep8Naming,PyShadowingBuiltins
class FirstFitShelfBinPacking(BinPacking):
    def __init__(self, bin_size, images, bin_parameters, progress):
        # Отсеиваем изображения размер которых больше или равен размеру контейнера
        images = filter(lambda image: image.crop.size.less(bin_size) == (True, True), images)

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

        BinPacking.__init__(self, bin_size, images, bin_parameters, progress)

    def _newBin(self, size, bin_parameters):
        self.bins.append(FirstFitShelfBin(size))
        return self.bins[-1]
