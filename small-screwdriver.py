# encoding: utf8
import sys
import random

from PySide.QtCore import Qt, Signal, QThread, QDirIterator, QDir, QSettings
from PySide.QtGui import QApplication, QWidget, QPainter, QSizePolicy, QFileDialog, QTransform

from SmallScrewdriver import Ui_SmallScrewdriver, Point, Rect, Size, Bin, BPImage
from SmallScrewdriver.BinPacking import BinPacking


COMPANY = 'Venus.Games'
APPNAME = 'SmallScrewdriver'


class BinPackingThread(QThread):
    updateBins = Signal(Rect)

    def __init__(self, d, bins):
        QThread.__init__(self)
        self.directory = d
        self.bins = bins

    def run(self):

        d = QDir(path=self.directory)
        d.setNameFilters('*.png')
        d.setFilter(QDir.Files or QDir.NoDotAndDotDot)

        d = QDirIterator(d)

        input_images = []

        while d.hasNext():
            input_images.append(BPImage(d.next()))

        input_images = sorted(input_images, key=lambda image: image.crop_region.size.width, reverse=True)

        # for i in input_images:
        #     self.bins[0].append(i)
        #     self.updateBins.emit(self.bins)
        # self.bins.append()

        BinPacking(self.bins[0], input_images)

        for i in input_images:
            self.bins[1].append(i)

        self.updateBins.emit(self.bins)

        print u'Я закончил'


# noinspection PyPep8Naming
class PaintWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.bins = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setWorldTransform(QTransform().scale(0.2, 0.2))

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

        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, COMPANY, APPNAME)
        self.restoreGeometry(self.settings.value(self.__class__.__name__))

        self.paintWidget = PaintWidget(self)
        self.paintWidget.resize(400, 400)

        self.verticalLayout.insertWidget(1, self.paintWidget)

        self.go.clicked.connect(self.onGo)

    def onGo(self):
        directory = QFileDialog.getExistingDirectory()
        self.binPackingThread = BinPackingThread(directory, [
            Bin(Size(2048, 2048)),
            Bin(Size(1024, 1024), Point(2048, 0))
        ])
        self.binPackingThread.updateBins.connect(self.paintWidget.redrawBins)
        self.binPackingThread.start()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, e):
        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, COMPANY, APPNAME)
        self.settings.setValue(self.__class__.__name__, self.saveGeometry())



if __name__ == '__main__':
    # noinspection PyTypeChecker,PyCallByClass
    QApplication.setStyle(u'plastique')
    app = QApplication(sys.argv)

    random.seed()

    smallScrewdriver = SmallScrewdriver()
    smallScrewdriver.show()

    sys.exit(app.exec_())
