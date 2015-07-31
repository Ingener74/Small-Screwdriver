# encoding: utf8
import copy
import sys
import random

from PySide.QtCore import Qt, Signal, QThread, QDirIterator, QDir
from PySide.QtGui import QApplication, QWidget, QPainter, QSizePolicy, QFileDialog

from SmallScrewdriver import Ui_SmallScrewdriver, Point, Rect, Size, Bin, BPImage


class BinPackingThread(QThread):
    updateBins = Signal(Rect)

    def __init__(self, d, bins):
        QThread.__init__(self)

        d = QDir(path=d)
        d.setNameFilters('*.png')
        d.setFilter(QDir.Files or QDir.NoDotAndDotDot)

        d = QDirIterator(d)

        self.input_images = []

        while d.hasNext():
            self.input_images.append(BPImage(d.next()))

        self.bins = bins

        for i in self.input_images:
            self.bins[0].append(i)

        self.updateBins.emit(copy.copy(self.bins))

    def run(self):
        while True:
            self.updateBins.emit(copy.copy(self.bins))
            self.sleep(1)


# noinspection PyPep8Naming
class PaintWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.bins = []

    def paintEvent(self, event):
        painter = QPainter(self)

        for b in self.bins:
            b.draw(painter)

    def redrawBins(self, bins):
        self.bins = bins
        self.update()


# noinspection PyPep8Naming,PyAttributeOutsideInit
class SmallScrewdriver(QWidget, Ui_SmallScrewdriver):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.paintWidget = PaintWidget(self)
        self.paintWidget.resize(400, 400)

        self.verticalLayout.insertWidget(1, self.paintWidget)

        self.go.clicked.connect(self.onGo)

    def onGo(self):
        directory = QFileDialog.getExistingDirectory()
        self.binPackingThread = BinPackingThread(directory, [
            Bin(Size(512, 512)),
            Bin(Size(256, 256), Point(514, 0))
        ])
        self.binPackingThread.updateBins.connect(self.paintWidget.redrawBins)
        self.binPackingThread.start()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    # noinspection PyTypeChecker,PyCallByClass
    QApplication.setStyle(u'plastique')
    app = QApplication(sys.argv)

    random.seed()

    smallScrewdriver = SmallScrewdriver()
    smallScrewdriver.show()

    sys.exit(app.exec_())
