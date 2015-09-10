# encoding: utf8
from PySide.QtCore import (Qt, QSettings)
from PySide.QtGui import (QWidget, QFileDialog)

from ScreamingMercuryWindow import Ui_ScreamingMercury
from SmallScrewdriver import (SmallScrewdriverWidget)
from Progress import (Progress)

COMPANY = 'Venus.Games'
APPNAME = 'ScreamingMercury'

SETTINGS_GEOMETRY = 'Geometry'
SETTINGS_SPLITTER1 = 'Splitter1'
SETTINGS_SPLITTER2 = 'Splitter2'
SETTINGS_SIZE = 'BinSize'
SETTINGS_METHOD = 'BinPackingMethod'

SETTINGS_VARIANT = 'Variant'
SETTINGS_HEURISTIC = 'Heuristic'
SETTINGS_SPLIT_RULE = 'SplitRule'

SETTINGS_DRAW_SCALE = 'DrawScale'


# noinspection PyPep8Naming
class ScreamingMercury(QWidget, Ui_ScreamingMercury):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.small_screwdriver = SmallScrewdriverWidget()
        self.work_layout.insertWidget(0, self.small_screwdriver)

        self.progress = Progress()

        self.addDirectory.clicked.connect(self.onAddDirectory)
        self.removeImage.clicked.connect(self.onRemoveImages)
        self.startPushButton.clicked.connect(self.onStart)
        self.methodTabWidget.currentChanged.connect(self.small_screwdriver.methodChanged)
        self.binSizeComboBox.currentIndexChanged.connect(self.small_screwdriver.binSizeChanged)

        self.small_screwdriver.images_changed.connect(self.updateImages)

        self.small_screwdriver.bin_packing_thread.bin_packing_available.connect(self.startPushButton.setEnabled)
        self.small_screwdriver.bin_packing_thread.on_end.connect(self.startPushButton.setEnabled)
        self.small_screwdriver.bin_packing_thread.on_end.connect(self.progress.setHidden)
        self.small_screwdriver.bin_packing_thread.on_progress.connect(self.progress.binPackingProgressBar.setValue)

        self.startPushButton.setEnabled(self.small_screwdriver.bin_packing_thread.binPackingAvailable())

        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, COMPANY, APPNAME)
        self.restoreGeometry(self.settings.value(SETTINGS_GEOMETRY))
        self.splitter.restoreState(self.settings.value(SETTINGS_SPLITTER1))
        self.splitter_2.restoreState(self.settings.value(SETTINGS_SPLITTER2))

        self.binSizeComboBox.setCurrentIndex(int(self.settings.value(SETTINGS_SIZE, defaultValue=0)))
        self.methodTabWidget.setCurrentIndex(int(self.settings.value(SETTINGS_METHOD, defaultValue=0)))
        self.fitVariantComboBox.setCurrentIndex(int(self.settings.value(SETTINGS_VARIANT, defaultValue=0)))
        self.heuristicComboBox.setCurrentIndex(int(self.settings.value(SETTINGS_HEURISTIC, defaultValue=0)))
        self.splitComboBox.setCurrentIndex(int(self.settings.value(SETTINGS_SPLIT_RULE, defaultValue=0)))
        self.small_screwdriver.scale = float(self.settings.value(SETTINGS_DRAW_SCALE, defaultValue=1.0))

    def onAddDirectory(self):
        directory = QFileDialog.getExistingDirectory()
        if directory != u'':
            self.small_screwdriver.setDirectory(directory)

    def onRemoveImages(self):
        row = self.imageList.currentRow()
        self.small_screwdriver.removeImage(row)
        self.imageList.setCurrentRow(row)

    def onStart(self):
        self.startPushButton.setEnabled(False)
        self.small_screwdriver.startBinPacking()
        self.progress.show()

    def updateImages(self, images):
        self.imageList.clear()
        self.imageList.addItems(images)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, e):
        self.progress.close()
        self.settings.setValue(SETTINGS_GEOMETRY, self.saveGeometry())
        self.settings.setValue(SETTINGS_SPLITTER1, self.splitter.saveState())
        self.settings.setValue(SETTINGS_SPLITTER2, self.splitter_2.saveState())
        self.settings.setValue(SETTINGS_SIZE, self.binSizeComboBox.currentIndex())
        self.settings.setValue(SETTINGS_METHOD, self.methodTabWidget.currentIndex())

        self.settings.setValue(SETTINGS_VARIANT, self.fitVariantComboBox.currentIndex())
        self.settings.setValue(SETTINGS_HEURISTIC, self.heuristicComboBox.currentIndex())
        self.settings.setValue(SETTINGS_SPLIT_RULE, self.splitComboBox.currentIndex())

        self.settings.setValue(SETTINGS_DRAW_SCALE, self.small_screwdriver.scale)
