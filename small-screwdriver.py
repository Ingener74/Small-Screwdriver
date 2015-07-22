# encoding: utf8
import copy

import sys
import random
from PySide.QtCore import Qt, Signal, Slot, QThread, QTimer, QMutex
from PySide.QtGui import QApplication, QWidget, QPainter, QSizePolicy, QColor, QPen
from SmallScrewdriver import Ui_SmallScrewdriver, Point, Rect, Size, Bin


class BinPackingThread(QThread):
    updateBins = Signal(Rect)

    def __init__(self, bins):
        QThread.__init__(self)

        self.input_images = []

        self.bins = bins

        for b in self.bins:
            b.append(Rect.random())
            b.append(Rect.random())
            b.append(Rect.random())

        print 'BinPackingThread'
        print self.bins

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

        self.binPackingThread = BinPackingThread(
            [
                Bin(Size(512, 512)),
                Bin(Size(256, 256), Point(514, 0))
            ])
        self.binPackingThread.updateBins.connect(self.redrawBins)
        self.binPackingThread.start()

    def paintEvent(self, event):
        painter = QPainter(self)

        for b in self.bins:
            b.draw(painter)

    def redrawBins(self, bins):
        self.bins = bins

        print 'redraw bins', self.bins

        self.update()


# noinspection PyPep8Naming
class SmallScrewdriver(QWidget, Ui_SmallScrewdriver):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.paintWidget = PaintWidget(self)
        self.paintWidget.resize(400, 400)

        self.verticalLayout.insertWidget(1, self.paintWidget)

        self.go.clicked.connect(self.onGo)

    def onGo(self):
        print u'Поехали'

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
