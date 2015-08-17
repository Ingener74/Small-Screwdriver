# coding=utf-8
import sys
import random

from PySide.QtCore import (Qt,
                           Signal,
                           QThread,
                           QDirIterator,
                           QDir,
                           QSettings)
from PySide.QtGui import (QApplication,
                          QWidget,
                          QPainter,
                          QSizePolicy,
                          QFileDialog,
                          QTransform)

from ScreamingMercury import (Ui_SmallScrewdriver,
                              Ui_SmallScrewdriverMain)
from SmallScrewdriver import (Point,
                              Rect,
                              Size,
                              Image,
                              ShelfNextFitBinPacking,
                              ShelfFirstFitBinPacking,
                              GuillotineBinPacking,
                              Bin)

COMPANY = 'Venus.Games'
APPNAME = 'SmallScrewdriver'

SETTINGS_SCALE = 'RenderScale'
SETTINGS_SIZE = 'BinSize'
SETTINGS_METHOD = 'BinPackingMethod'

SIZES = (Size(256, 256),
         Size(512, 512),
         Size(1024, 1024),
         Size(2048, 2048),
         Size(4096, 4096),
         Size(8192, 8192))

METHODS = (ShelfNextFitBinPacking,
           ShelfFirstFitBinPacking,
           GuillotineBinPacking)


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

        x = 0
        for b in self.bins:
            b.draw(painter, Point(x, 0))
            x += b.size.width + 5

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

        if self.settings.value(SETTINGS_SIZE) is not None:
            self.binSizeComboBox.setCurrentIndex(int(self.settings.value(SETTINGS_SIZE)))

        if self.settings.value(SETTINGS_METHOD) is not None:
            self.methodComboBox.setCurrentIndex(int(self.settings.value(SETTINGS_METHOD)))

        self.scaleSpinBox.valueChanged.connect(self.update)

        self.paintWidget = PaintWidget(self.scaleSpinBox, self)
        self.paintWidget.resize(400, 400)

        self.verticalLayout.insertWidget(1, self.paintWidget)

        self.go.clicked.connect(self.onGo)

    def onGo(self):
        directory = QFileDialog.getExistingDirectory()
        # print directory
        # if len(directory) > 0:
        self.binPackingThread = BinPackingThread(directory,
                                                 self.methodComboBox.currentIndex(),
                                                 self.binSizeComboBox.currentIndex())
        self.binPackingThread.updateBins.connect(self.paintWidget.redrawBins)
        self.binPackingThread.start()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, e):
        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, COMPANY, APPNAME)
        self.settings.setValue(self.__class__.__name__, self.saveGeometry())
        self.settings.setValue(SETTINGS_SCALE, self.scaleSpinBox.value())
        self.settings.setValue(SETTINGS_SIZE, self.binSizeComboBox.currentIndex())
        self.settings.setValue(SETTINGS_METHOD, self.methodComboBox.currentIndex())


class SmallScrewdriverMain(QWidget, Ui_SmallScrewdriverMain):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.paintWidget = PaintWidget(self.scale, self)
        self.horizontalLayout_3.insertWidget(1, self.paintWidget)
        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 6)
        self.horizontalLayout_3.setStretch(2, 1)

        self.paintWidget.bins = [Bin(), Bin()]

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

    # ssm = SmallScrewdriverMain()
    # ssm.show()

    sys.exit(app.exec_())
