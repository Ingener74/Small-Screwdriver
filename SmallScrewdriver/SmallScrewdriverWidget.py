# encoding: utf8
from PySide.QtGui import (QWidget, QSizePolicy, QPainter, QTransform)

from SmallScrewdriver import (Bin, Point)


class SmallScrewdriverWidget(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.bins = [Bin(), Bin()]

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


# class PaintWidget(QWidget):
#     def __init__(self, scaleSpinBox, parent=None):
#         QWidget.__init__(self, parent)
#         self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
#
#         self.bins = []
#
#         self.scaleSpinBox = scaleSpinBox

