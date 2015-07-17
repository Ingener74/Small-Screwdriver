# encoding: utf8
import sys
import random
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QWidget, QPainter, QSizePolicy, QColor
from SmallScrewdriver import Ui_SmallScrewdriver, Point, Rect


class PaintWidget(QWidget):
    def __init__(self, rects, parent=None):
        QWidget.__init__(self, parent)

        self.rects = rects
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.begin(self)

        for rect in self.rects:
            rect.draw(painter)

        painter.end()


# noinspection PyPep8Naming
class SmallScrewdriver(QWidget, Ui_SmallScrewdriver):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.rects = [self.randomRect() for i in xrange(0, 20)]

        self.paintWidget = PaintWidget(self.rects, self)
        self.paintWidget.resize(400, 400)

        self.verticalLayout.insertWidget(1, self.paintWidget)

    @staticmethod
    def randomRect():
        return Rect(Point(100. * random.random(), 100. * random.random()),
                    10 + 200. * random.random(), 10 + 200. * random.random(),
                    QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

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
