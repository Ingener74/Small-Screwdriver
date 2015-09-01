# encoding: utf8
from PySide.QtCore import QThread, Signal, QDir, QDirIterator
from SmallScrewdriver import Rect, Image

__author__ = 'pavel'


class BinPackingThread(QThread):
    updateBins = Signal(Rect)

    def __init__(self, d, method, bin_size):
        QThread.__init__(self)
        self.directory = d
        self.bins = []

        self.method = method
        self.bin_size = bin_size

    def run(self):
        print 'work directory ', self.directory

        d = QDir(path=self.directory)
        d.setNameFilters(['*.png'])
        d.setFilter(QDir.Files or QDir.NoDotAndDotDot)

        dit = QDirIterator(d, flags=QDirIterator.Subdirectories, filters=QDir.Files)

        input_images = []

        while dit.hasNext():
            im = dit.next()
            print d.relativeFilePath(im)
            input_images.append(Image(im))

        bin_packing = METHODS[self.method](SIZES[self.bin_size], input_images)
        bin_packing.save_atlases(self.directory)

        self.updateBins.emit(bin_packing.bins)