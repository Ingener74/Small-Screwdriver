# encoding: utf8
from PySide.QtCore import (QThread, Signal)

from SmallScrewdriver import (Rect, Image, GuillotineBinPacking, Size)
from SmallScrewdriver.MaxRects import MaxRectsBinPacking
from SmallScrewdriver.Shelf.ShelfFirstFitBinPacking import ShelfFirstFitBinPacking
from SmallScrewdriver.Shelf.ShelfNextFitBinPacking import ShelfNextFitBinPacking


# noinspection PyPep8Naming
class BinPackingThread(QThread):
    METHODS = (ShelfNextFitBinPacking,
               ShelfFirstFitBinPacking,
               GuillotineBinPacking,
               MaxRectsBinPacking)

    SIZES = (Size(256, 256),
             Size(512, 512),
             Size(1024, 1024),
             Size(2048, 2048),
             Size(4096, 4096),
             Size(8192, 8192))

    bin_packing_available = Signal(bool)
    update_bins = Signal(Rect)

    on_end = Signal(bool)

    def __init__(self):
        QThread.__init__(self)

        self.directory = None
        self.images = []

        self.method = BinPackingThread.METHODS[0]
        self.bin_size = BinPackingThread.SIZES[0]

    def setDirectory(self, directory):
        self.directory = directory
        self.bin_packing_available.emit(self.binPackingAvailable())

    def binPackingAvailable(self):
        return len(self.images) and self.directory is not None

    def setImages(self, images):
        self.images = images
        self.bin_packing_available.emit(self.binPackingAvailable())

    def setMethod(self, index):
        self.method = BinPackingThread.METHODS[index]

    def setBinSize(self, index):
        self.bin_size = BinPackingThread.SIZES[index]

    def run(self):
        if not self.directory or not len(self.images):
            return

        bin_packing = self.method(self.bin_size, [Image(self.directory, image) for image in self.images])
        bin_packing.saveAtlases(self.directory)

        self.update_bins.emit(bin_packing.bins)
        self.on_end.emit(True)
