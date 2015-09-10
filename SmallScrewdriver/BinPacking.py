# encoding: utf8
from PySide.QtCore import Signal
from SmallScrewdriver import DEFAULT_BIN_SIZE
from abc import abstractmethod


# noinspection PyPep8Naming,PyShadowingBuiltins
class BinPacking(object):

    def __init__(self, *args, **kwargs):
        self.bins = []
        self.bin_size = args[0] if len(args) > 0 else kwargs['bin_size'] if 'bin_size' in kwargs else DEFAULT_BIN_SIZE

        images = args[1] if len(args) > 1 else kwargs['images'] if 'images' in kwargs else []
        del kwargs['images']

        on_progress = kwargs['on_progress'] if 'on_progress' in kwargs else None
        del kwargs['on_progress']

        # Первый контейнер
        self._newBin(*args, **kwargs)

        # Проходим по всем изображениям ...
        for index, image in enumerate(images):

            # ... и по всем контейнерам ...
            for bin in self.bins:

                # ... пробуем поместить изображение в контейнер ...
                if bin.addImage(image):

                    if on_progress:
                        on_progress(int(100.0 * index / float(len(images))))

                    # ... если получилось, идём к следующему изображению ...
                    break
            else:
                # ... если не в один контейнер, поместить не получилось, создаём новый ...
                bin = self._newBin(*args, **kwargs)

                # ... и пробуем поместить в него ...
                if bin.addImage(image):
                    if on_progress:
                        on_progress(int(100.0 * index / float(len(images))))
                else:
                    # ... и если не получается значит произошла ...
                    raise SystemError(u'Какая та хуйня')

        if on_progress:
            on_progress(100)

    def saveAtlases(self, directory):
        for i, b in enumerate(self.bins):
            b.save(directory + '/atlas' + str(i))

    @abstractmethod
    def _newBin(self, *args, **kwargs):
        raise NotImplementedError
