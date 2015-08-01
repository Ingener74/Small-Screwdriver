from abc import ABCMeta, abstractmethod

__author__ = 'Pavel'


class BinPacking(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def saveAtlases(self, directory):
        pass