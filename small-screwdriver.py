# encoding: utf8
from copy import copy
import sys
import random

from PySide.QtCore import Qt, Signal, QThread, QDirIterator, QDir, QSettings
from PySide.QtGui import QApplication, QWidget, QPainter, QSizePolicy, QFileDialog, QTransform, QImage

from SmallScrewdriver import Ui_SmallScrewdriver, Point, Rect, Size, Bin, BPImage
from SmallScrewdriver.BinPacking import BinPacking

COMPANY = 'Venus.Games'
APPNAME = 'SmallScrewdriver'

SETTINGS_SCALE = 'RenderScale'


class BinPackingThread(QThread):
    updateBins = Signal(Rect)

    def __init__(self, d):
        QThread.__init__(self)
        self.directory = d
        self.bins = []

    def run(self):

        d = QDir(path=self.directory)
        d.setNameFilters(['*.png'])
        d.setFilter(QDir.Files or QDir.NoDotAndDotDot)

        d = QDirIterator(d)

        input_images = []

        while d.hasNext():
            input_images.append(BPImage(d.next()))

        atlas_counter = 0

        while len(input_images) > 0:
            bin = Bin(Size(2048, 2048))
            BinPacking(bin, input_images)
            bin.save('atlas' + str(atlas_counter))
            atlas_counter += 1

            self.bins.append(bin)

        bin_x = 0
        for b in self.bins:
            b.origin = Point(bin_x, 0)
            bin_x += b.size.width + 5

        self.updateBins.emit(self.bins)

        print u'Я закончил'


# noinspection PyPep8Naming
class PaintWidget(QWidget):
    def __init__(self, scaleSpinBox, parent=None):
        QWidget.__init__(self, parent)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.bins = []

        self.scaleSpinBox = scaleSpinBox

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setWorldTransform(QTransform().scale(self.scaleSpinBox.value(), self.scaleSpinBox.value()))

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
        print self.settings.fileName()
        self.restoreGeometry(self.settings.value(self.__class__.__name__))
        if self.settings.value(SETTINGS_SCALE) is not None:
            self.scaleSpinBox.setValue(float(self.settings.value(SETTINGS_SCALE)))

        self.scaleSpinBox.valueChanged.connect(self.update)

        self.paintWidget = PaintWidget(self.scaleSpinBox, self)
        self.paintWidget.resize(400, 400)

        self.verticalLayout.insertWidget(1, self.paintWidget)

        self.go.clicked.connect(self.onGo)

    def onGo(self):
        directory = QFileDialog.getExistingDirectory()
        self.binPackingThread = BinPackingThread(directory)
        self.binPackingThread.updateBins.connect(self.paintWidget.redrawBins)
        self.binPackingThread.start()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, e):
        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, COMPANY, APPNAME)
        self.settings.setValue(self.__class__.__name__, self.saveGeometry())
        self.settings.setValue(SETTINGS_SCALE, self.scaleSpinBox.value())


if __name__ == '__main__':
    # noinspection PyTypeChecker,PyCallByClass
    QApplication.setStyle(u'plastique')
    app = QApplication(sys.argv)

    random.seed()

    smallScrewdriver = SmallScrewdriver()
    smallScrewdriver.show()

    sys.exit(app.exec_())
