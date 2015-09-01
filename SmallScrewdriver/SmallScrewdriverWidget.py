# encoding: utf8
from PySide.QtCore import (QDir, QDirIterator, Signal)

from PySide.QtGui import (QWidget, QSizePolicy, QPainter, QTransform)

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
        self.bins = [Bin(), Bin()]
        self.scale = 1.0

        self.bin_packing_thread = BinPackingThread()
        self.bin_packing_thread.updateBins.connect(self.redraw_bins)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setWorldTransform(QTransform().scale(self.scale, self.scale))

        x = 0
        for b in self.bins:
            b.draw(painter, Point(x, 0))
            x += b.size.width + 5

    def redraw_bins(self, bins):
        self.bins = bins
        self.update()

    def set_directory(self, directory):
        self.directory = directory

        folder = QDir(path=self.directory)
        folder.setNameFilters(['*.png'])
        folder.setFilter(QDir.Files or QDir.NoDotAndDotDot)

        dit = QDirIterator(folder, flags=QDirIterator.Subdirectories, filters=QDir.Files)

        while dit.hasNext():
            im = folder.relativeFilePath(dit.next())
            self.images.append(im)

        self.bin_packing_thread.set_directory(self.directory)
        self.bin_packing_thread.set_images(self.images)

        self.images_changed.emit(self.images)

    def remove_image(self, index):
        del self.images[index]
        self.images_changed.emit(self.images)

    def start_bin_packing(self):
        self.bin_packing_thread.start()

    def bin_size_changed(self, index):
        self.bin_packing_thread.set_bin_size(index)

    def method_changed(self, index):
        self.bin_packing_thread.set_method(index)
