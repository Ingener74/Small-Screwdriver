# encoding: utf8
import sys
import random
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QWidget, QPainter, QSizePolicy, QColor, QPen
from SmallScrewdriver import Ui_SmallScrewdriver, Point, Rect


class PaintWidget(QWidget):
    def __init__(self, rects, bin_size, parent=None):
        QWidget.__init__(self, parent)

        pen = QPen()
        pen.setStyle(Qt.DashLine)
        self.bin = Rect(Point(0, 0), bin_size[0], bin_size[1], pen)

        self.rects = rects
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.begin(self)

        for rect in self.rects:
            rect.draw(painter)

        self.bin.draw(painter)

        painter.end()


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
        return Rect(Point(100. * random.random(), 100. * random.random()),
                    10 + 200. * random.random(), 10 + 200. * random.random(), pen)

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
