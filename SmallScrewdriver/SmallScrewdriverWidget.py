# encoding: utf8
import math

from PySide.QtCore import (QDir, QDirIterator, Signal, QThread)
from PySide.QtGui import (QWidget, QSizePolicy, QPainter, QTransform)

import re
from SmallScrewdriver import (Point, Size, Rect, Image, GuillotineBinPacking, MaxRectsBinPacking,
                              ShelfNextFitBinPacking, ShelfFirstFitBinPacking)


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

    packing_progress = Signal(int)
    saving_progress = Signal(int)
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

        self.packing_progress.emit(0)
        self.saving_progress.emit(0)

        bin_packing = self.method(self.bin_size, [Image(self.directory, image) for image in self.images],
                                  packingProgress=self.packingProgress, savingProgress=self.savingProgress)
        bin_packing.saveAtlases(self.directory)

        self.update_bins.emit(bin_packing.bins)
        self.on_end.emit(True)

    def packingProgress(self, progress):
        self.packing_progress.emit(progress)

    def savingProgress(self, progress):
        self.saving_progress.emit(progress)


# noinspection PyPep8Naming
class SmallScrewdriverWidget(QWidget):
    """
    Виджет для
    """
    images_changed = Signal(object)

    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.directory = None
        self.images = []
        self.bins = []
        self.scale = 1.0

        self.bin_packing_thread = BinPackingThread()
        self.bin_packing_thread.update_bins.connect(self.redrawBins)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setWorldTransform(QTransform().scale(self.scale, self.scale))

        for i, b in enumerate(self.bins):
            side = int(math.floor(math.log(len(self.bins), 2)))

            x = (i % side) * (b.size.width + 10) if side else 10
            y = (i / side) * (b.size.height + 10) if side else 10

            b.draw(painter, Point(x, y))

    def wheelEvent(self, *args, **kwargs):
        self.scale += args[0].delta() / 2400.0
        self.update()

    def redrawBins(self, bins):
        self.bins = bins
        self.update()

    def setDirectory(self, directory):
        self.directory = directory

        folder = QDir(path=self.directory)
        folder.setNameFilters(['*.png'])
        folder.setFilter(QDir.Files or QDir.NoDotAndDotDot)

        dit = QDirIterator(folder, flags=QDirIterator.Subdirectories, filters=QDir.Files)

        while dit.hasNext():
            im = folder.relativeFilePath(dit.next())
            if not re.search("atlas", im):
                self.images.append(im)

        self.bin_packing_thread.setDirectory(self.directory)
        self.bin_packing_thread.setImages(self.images)

        self.images_changed.emit(self.images)

    def removeImage(self, index):
        del self.images[index]
        self.images_changed.emit(self.images)

    def startBinPacking(self):
        self.bin_packing_thread.start()

    def binSizeChanged(self, index):
        self.bin_packing_thread.setBinSize(index)

    def methodChanged(self, index):
        self.bin_packing_thread.setMethod(index)
