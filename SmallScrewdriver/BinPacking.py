# encoding: utf8
from abc import abstractmethod

from SmallScrewdriver import (Point)


class BinPackingProgress(object):
    def __init__(self):
        pass

    def prepare_progress(self, progress_in_percent):
        pass

    def packing_progress(self, percent):
        pass

    def saving_progress(self, percent):
        pass

    def verify_progress(self, percent):
        pass


# noinspection PyPep8Naming,PyShadowingBuiltins
class BinPacking(object):

    def __init__(self, bin_size, images, bin_parameters, progress):
        self.bins = []

        self.progress = progress

        # Первый контейнер
        self._newBin(bin_size, bin_parameters)

        images = [] if images is None else images

        # Проходим по всем изображениям ...
        for index, image in enumerate(images):

            # ... и по всем контейнерам ...
            for bin in self.bins:

                # ... пробуем поместить изображение в контейнер ...
                if bin.addImage(image):
                    self.progress.packing_progress(100 * index / len(images))

                    # ... если получилось, идём к следующему изображению ...
                    break
            else:
                # ... если не в один контейнер, поместить не получилось, создаём новый ...
                bin = self._newBin(bin_size, bin_parameters)

                # ... и пробуем поместить в него ...
                if bin.addImage(image):
                    self.progress.packing_progress(100 * index / len(images))
                else:
                    # ... и если не получается значит произошла ...
                    raise SystemError(u'Какая та хуйня')

        self.progress.packing_progress(100)

    def saveAtlases(self, directory):
        for i, b in enumerate(self.bins):
            self.progress.saving_progress(100 * i / len(self.bins))
            b.save(directory + 'atlas' + str(i))

            self.progress.saving_progress(100)

    @abstractmethod
    def _newBin(self, size, bin_parameters):
        raise NotImplementedError
