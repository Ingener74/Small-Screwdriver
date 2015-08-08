# coding=utf-8
import sys

from PySide.QtCore import Qt, QSettings

from PySide.QtGui import QApplication, QWidget, QPainter, QImage, QTransform, QPen, QColor
from SillyCrossbow import crop_image_from_file
from SmallScrewdriver import Rect, Point, Size

COMPANY = 'Venus.Games'
APPNAME = 'SmallScrewdriver.test'


class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, COMPANY, APPNAME)
        self.restoreGeometry(self.settings.value(self.__class__.__name__))

        self.image1 = QImage('resources/fire.png')
        self.image2 = crop_image_from_file(QImage('resources/start.png'), 50)[0]

    def paintEvent(self, *args, **kwargs):
        painter = QPainter(self)

        # painter.setTransform(QTransform().scale(0.3, 0.3))
        #
        # painter.drawImage(0, 0, self.image1)
        #
        # painter.setTransform(QTransform().scale(0.3, 0.3).translate(self.image2.height(), 0).rotate(90, Qt.ZAxis))
        # painter.drawImage(0, 0, self.image2)

        r1 = Rect(Point(10, 10), Size(512, 512))
        r2 = Rect(Point(), Size(110, 75))
        r3 = Rect(Point(), Size(70, 95))
        r4 = Rect(Point(), Size(90, 55))
        r5 = Rect(Point(), Size(50, 35))

        r1.draw(painter)
        # r2.draw(painter)
        # r3.draw(painter)
        # r4.draw(painter)
        # r5.draw(painter)

        s, rs1, rs2 = r1.split(r2, Rect.RULE_SAS)
        if s:
            # rs1.randomColor()
            rs1.draw(painter)

            # rs2.randomColor()
            rs2.draw(painter)

            # r2.randomColor()
            # r2.draw(painter)

        s, rs3, rs4 = rs1.split(r3, Rect.RULE_SAS)
        if s:
            # rs3.randomColor()
            rs3.draw(painter)

            # rs4.randomColor()
            rs4.draw(painter)

            # r3.randomColor()
            # r3.draw(painter)

        s, rs5, rs6 = rs3.split(r4, Rect.RULE_SAS)
        if s:
            # rs5.randomColor()
            rs5.draw(painter)

            # rs6.randomColor()
            rs6.draw(painter)

            # r4.randomColor()
            # r4.draw(painter)

        s, rs7, rs8 = rs5.split(r5, Rect.RULE_SAS)
        if s:
            # rs7.randomColor()
            rs7.draw(painter)

            # rs8.randomColor()
            rs8.draw(painter)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, *args, **kwargs):
        self.settings.setValue(self.__class__.__name__, self.saveGeometry())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Widget()
    w.show()

    sys.exit(app.exec_())
