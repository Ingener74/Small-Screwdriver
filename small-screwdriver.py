# encoding: utf8
import sys
from PySide.QtGui import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)

    print 'test'

    sys.exit(app.exec_())