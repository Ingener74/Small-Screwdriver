# encoding: utf8
from PySide.QtCore import Qt
from PySide.QtGui import QWidget

from ScreamingMercuryWindow import Ui_ScreamingMercury
from SmallScrewdriver import (SmallScrewdriverWidget, Size, ShelfNextFitBinPacking, GuillotineBinPacking,
                              ShelfFirstFitBinPacking)

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


class ScreamingMercury(QWidget, Ui_ScreamingMercury):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        # self.paintWidget = PaintWidget(self.scale, self)
        # self.horizontalLayout_3.insertWidget(1, self.paintWidget)
        # self.horizontalLayout_3.setStretch(0, 3)
        # self.horizontalLayout_3.setStretch(1, 6)
        # self.horizontalLayout_3.setStretch(2, 1)
        #
        # self.paintWidget.bins = [Bin(), Bin()]

        self.small_screwdriver = SmallScrewdriverWidget()
        self.work_layout.insertWidget(0, self.small_screwdriver)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


# class SmallScrewdriver(QWidget, Ui_SmallScrewdriver):
#     def __init__(self, parent=None):
#         QWidget.__init__(self, parent)
#         self.setupUi(self)
#
#         self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, COMPANY, APPNAME)
#         print self.settings.fileName()
#         self.restoreGeometry(self.settings.value(self.__class__.__name__))
#
#         if self.settings.value(SETTINGS_SCALE) is not None:
#             self.scaleSpinBox.setValue(float(self.settings.value(SETTINGS_SCALE)))
#
#         if self.settings.value(SETTINGS_SIZE) is not None:
#             self.binSizeComboBox.setCurrentIndex(int(self.settings.value(SETTINGS_SIZE)))
#
#         if self.settings.value(SETTINGS_METHOD) is not None:
#             self.methodComboBox.setCurrentIndex(int(self.settings.value(SETTINGS_METHOD)))
#
#         self.scaleSpinBox.valueChanged.connect(self.update)
#
#         self.paintWidget = PaintWidget(self.scaleSpinBox, self)
#         self.paintWidget.resize(400, 400)
#
#         self.verticalLayout.insertWidget(1, self.paintWidget)
#
#         self.go.clicked.connect(self.onGo)
#
#     def onGo(self):
#         directory = QFileDialog.getExistingDirectory()
#         # print directory
#         # if len(directory) > 0:
#         self.binPackingThread = BinPackingThread(directory,
#                                                  self.methodComboBox.currentIndex(),
#                                                  self.binSizeComboBox.currentIndex())
#         self.binPackingThread.updateBins.connect(self.paintWidget.redrawBins)
#         self.binPackingThread.start()
#
#     def keyPressEvent(self, e):
#         if e.key() == Qt.Key_Escape:
#             self.close()
#
#     def closeEvent(self, e):
#         self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, COMPANY, APPNAME)
#         self.settings.setValue(self.__class__.__name__, self.saveGeometry())
#         self.settings.setValue(SETTINGS_SCALE, self.scaleSpinBox.value())
#         self.settings.setValue(SETTINGS_SIZE, self.binSizeComboBox.currentIndex())
#         self.settings.setValue(SETTINGS_METHOD, self.methodComboBox.currentIndex())
