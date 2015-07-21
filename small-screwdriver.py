# encoding: utf8

import sys
import random
from PySide.QtCore import Qt, Signal, Slot, QThread, QTimer, QMutex
from PySide.QtGui import QApplication, QWidget, QPainter, QSizePolicy, QColor, QPen
from SmallScrewdriver import Ui_SmallScrewdriver, Point, Rect
from SmallScrewdriver.Size import Size


class BinPackingThread(QThread):
    def __init__(self):
        self.bins = []
        self.input_rects = []

        self.output_mutex = QMutex()
        self.output_rects = []

        pass

    def run(self):
        while True:

            self.output_mutex.lock()

            if len(self.output_rects) > 0:
                self.output_rects.remove(0)
            else:
                self.output_rects.append(Rect(Point(10, 10), Size(100, 100)))

            self.output_mutex.unlock()

            self.sleep(1)


# noinspection PyPep8Naming
class PaintWidget(QWidget):
    def __init__(self, rects, bin_size, parent=None):
        QWidget.__init__(self, parent)

        pen = QPen()
        pen.setStyle(Qt.DashLine)
        self.bin = Rect(Point(0, 0), pen)

        self.rects = rects
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.redrawTimer = QTimer()
        self.redrawTimer.timeout.connect(self.onTimeout)
        self.redrawTimer.start(10)

        self.binPackingThread = BinPackingThread()

    def paintEvent(self, event):
        painter = QPainter(self)

        for rect in self.rects:
            rect.draw(painter)

        self.bin.draw(painter)

    def onTimeout(self, rects):
        self.binPackingThread.output_mutex.lock()

        del self.rects[:]
        self.rects = list(self.binPackingThread.output_rects)

        self.binPackingThread.output_mutex.unlock()

        self.update()


# noinspection PyPep8Naming
class SmallScrewdriver(QWidget, Ui_SmallScrewdriver):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.rects = [self.randomRect() for i in xrange(0, 20)]

        self.paintWidget = PaintWidget(self.rects, (512, 512), self)
        self.paintWidget.resize(400, 400)

        self.verticalLayout.insertWidget(1, self.paintWidget)

        self.go.clicked.connect(self.onGo)

    def onGo(self):
        print u'Поехали'

    @staticmethod
    def randomRect():
        pen = QPen()
        pen.setColor(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        return Rect(Point(100. * random.random(), 100. * random.random()), pen)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    test = {'Point': {'x': 10, 'y': 20},
            'width': 100,
            'height': 100
            }
    print test

    print Point(10, 10)

    raise SystemExit

    # noinspection PyTypeChecker,PyCallByClass
    QApplication.setStyle(u'plastique')
    app = QApplication(sys.argv)

    random.seed()

    smallScrewdriver = SmallScrewdriver()
    smallScrewdriver.show()

    sys.exit(app.exec_())
