# encoding: utf8
from PySide.QtCore import (Qt, QSettings)
from PySide.QtGui import (QWidget, QFileDialog)

from ScreamingMercuryWindow import Ui_ScreamingMercury
from SmallScrewdriver import (SmallScrewdriverWidget)
from Progress import (Progress)

COMPANY = 'Venus.Games'
APPNAME = 'SmallScrewdriver'

SETTINGS_GEOMETRY = 'Geometry'
SETTINGS_SPLITTER1 = 'Splitter1'
SETTINGS_SPLITTER2 = 'Splitter2'
SETTINGS_SIZE = 'BinSize'
SETTINGS_METHOD = 'BinPackingMethod'

SETTINGS_VARIANT = 'Variant'
SETTINGS_HEURISTIC = 'Heuristic'
SETTINGS_SPLIT_RULE = 'SplitRule'


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

        bin_size = self.settings.value(SETTINGS_SIZE)
        self.binSizeComboBox.setCurrentIndex(0 if bin_size is None else int(bin_size))

        method = self.settings.value(SETTINGS_METHOD)
        self.methodTabWidget.setCurrentIndex(0 if method is None else int(method))

        fit_variant = self.settings.value(SETTINGS_VARIANT)
        self.fitVariantComboBox.setCurrentIndex(0 if fit_variant is None else int(fit_variant))

        heuristic = self.settings.value(SETTINGS_HEURISTIC)
        self.heuristicComboBox.setCurrentIndex(0 if heuristic is None else int(heuristic))

        split_rule = self.settings.value(SETTINGS_SPLIT_RULE)
        self.splitComboBox.setCurrentIndex(0 if split_rule is None else int(split_rule))

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
        self.settings.setValue(SETTINGS_GEOMETRY, self.saveGeometry())
        self.settings.setValue(SETTINGS_SPLITTER1, self.splitter.saveState())
        self.settings.setValue(SETTINGS_SPLITTER2, self.splitter_2.saveState())
        self.settings.setValue(SETTINGS_SIZE, self.binSizeComboBox.currentIndex())
        self.settings.setValue(SETTINGS_METHOD, self.methodTabWidget.currentIndex())

        self.settings.setValue(SETTINGS_VARIANT, self.fitVariantComboBox.currentIndex())
        self.settings.setValue(SETTINGS_HEURISTIC, self.heuristicComboBox.currentIndex())
        self.settings.setValue(SETTINGS_SPLIT_RULE, self.splitComboBox.currentIndex())