# encoding: utf8
from PySide.QtCore import (QDir, QDirIterator, Signal)

from PySide.QtGui import (QWidget, QSizePolicy, QPainter, QTransform)
import math

from SmallScrewdriver import (Bin, Point)
from SmallScrewdriver.BinPackingThread import BinPackingThread


# noinspection PyPep8Naming
class SmallScrewdriverWidget(QWidget):
    images_changed = Signal(object)

    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.directory = None
        self.images = []
        # self.bins = [Bin(), Bin(), Bin(), Bin(), Bin(), Bin(), Bin(), Bin(), Bin()]
        self.bins = []
        self.scale = 1.0

        self.bin_packing_thread = BinPackingThread()
        self.bin_packing_thread.update_bins.connect(self.redrawBins)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setWorldTransform(QTransform().scale(self.scale, self.scale))

        for i, b in enumerate(self.bins):
            side = int(math.floor(math.log(len(self.bins), 2)))

            x = (i % side) * (b.size.width + 10) if side else 0
            y = (i / side) * (b.size.height + 10) if side else 0

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
