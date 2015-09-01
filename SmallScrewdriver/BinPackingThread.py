# encoding: utf8
from PySide.QtCore import (QThread, Signal)

from SmallScrewdriver import (Rect, Image, ShelfNextFitBinPacking, ShelfFirstFitBinPacking, GuillotineBinPacking, Size)

__author__ = 'pavel'


class BinPackingThread(QThread):
    METHODS = (ShelfNextFitBinPacking,
               ShelfFirstFitBinPacking,
               GuillotineBinPacking)

    SIZES = (Size(256, 256),
             Size(512, 512),
             Size(1024, 1024),
             Size(2048, 2048),
             Size(4096, 4096),
             Size(8192, 8192))

    updateBins = Signal(Rect)

    def __init__(self):
        QThread.__init__(self)

        self.directory = None
        self.images = []

        self.bins = []

        self.method = None
        self.bin_size = None

    def set_directory(self, directory):
        self.directory = directory

    def set_images(self, images):
        self.images = images

    def set_method(self, index):
        self.method = BinPackingThread.METHODS[index]

    def set_bin_size(self, index):
        self.bin_size = BinPackingThread.SIZES[index]

    def run(self):
        if not self.directory and not len(self.images) and not self.method and not self.bin_size:
            return
        bin_packing = self.method(self.bin_size, [Image(self.directory, image) for image in self.images])
        bin_packing.save_atlases(self.directory)

        self.updateBins.emit(bin_packing.bins)
