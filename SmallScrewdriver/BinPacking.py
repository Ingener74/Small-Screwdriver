# encoding: utf8
from SmallScrewdriver import DEFAULT_BIN_SIZE, Point
from abc import abstractmethod


class BinPackingProgress(object):
    def __init__(self):
        pass

    def packing_progress(self, percent):
        pass

    def saving_progress(self, percent):
        pass

    def verify_progress(self, percent):
        pass


# noinspection PyPep8Naming,PyShadowingBuiltins
class BinPacking(object):

    bin_packing_progress = BinPackingProgress()

    def __init__(self, bin_size=DEFAULT_BIN_SIZE, images=None, bin_parameters=None):
        self.bins = []

        # Первый контейнер
        self._newBin(size=bin_size, origin=Point(), bin_parameters=bin_parameters)

        images = [] if images is None else images

        # Проходим по всем изображениям ...
        for index, image in enumerate(images):

            # ... и по всем контейнерам ...
            for bin in self.bins:

                # ... пробуем поместить изображение в контейнер ...
                if bin.addImage(image):
                    BinPacking.bin_packing_progress.packing_progress(100 * index / len(images))

                    # ... если получилось, идём к следующему изображению ...
                    break
            else:
                # ... если не в один контейнер, поместить не получилось, создаём новый ...
                bin = self._newBin(size=bin_size, origin=Point(), bin_parameters=bin_parameters)

                # ... и пробуем поместить в него ...
                if bin.addImage(image):
                    BinPacking.bin_packing_progress.packing_progress(100 * index / len(images))
                else:
                    # ... и если не получается значит произошла ...
                    raise SystemError(u'Какая та хуйня')

        BinPacking.bin_packing_progress.packing_progress(100)

    def saveAtlases(self, directory):
        for i, b in enumerate(self.bins):
            BinPacking.bin_packing_progress.saving_progress(100 * i / len(self.bins))
            b.save(directory + 'atlas' + str(i))

        BinPacking.bin_packing_progress.saving_progress(100)

    @abstractmethod
    def _newBin(self, size, origin, bin_parameters):
        raise NotImplementedError
