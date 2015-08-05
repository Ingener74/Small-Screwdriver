# encoding: utf8
import sys

from PySide.QtCore import Qt

from PySide.QtGui import QApplication, QWidget, QPainter, QImage, QTransform
from SillyCrossbow import crop_image_from_file


class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.image1 = QImage('resources/fire.png')
        self.image2 = crop_image_from_file(QImage('resources/start.png'), 50)[0]

    def paintEvent(self, *args, **kwargs):
        painter = QPainter(self)

        painter.setTransform(QTransform().scale(0.3, 0.3))

        painter.drawImage(0, 0, self.image1)

        painter.setTransform(QTransform().scale(0.3, 0.3).translate(self.image2.height(), 0).rotate(90, Qt.ZAxis))
        painter.drawImage(0, 0, self.image2)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Widget()
    w.show()

    sys.exit(app.exec_())
