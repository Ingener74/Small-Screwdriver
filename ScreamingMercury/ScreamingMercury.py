# encoding: utf8
from PySide.QtCore import (Qt, QSettings)
from PySide.QtGui import (QWidget, QFileDialog)

from ScreamingMercuryWindow import (Ui_ScreamingMercury)
from SmallScrewdriver import (SmallScrewdriverWidget)
from Settings import (Settings)
from Progress import (Progress)

COMPANY = 'Venus.Games'
APPNAME = 'ScreamingMercury'

SETTINGS_GEOMETRY = 'Geometry'
SETTINGS_SPLITTER1 = 'Splitter1'
SETTINGS_SPLITTER2 = 'Splitter2'
SETTINGS_SIZE = 'BinSize'
SETTINGS_METHOD = 'BinPackingMethod'

SETTINGS_FIRST_FIT_VARIANT = 'FirstFitVariant'
SETTINGS_FIRST_FIT_HEURISTIC = 'FirstFitHeuristic'

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

        self.progress_window = Progress()
        self.settings_window = Settings()

        self.addDirectory.clicked.connect(self.onAddDirectory)
        self.removeImage.clicked.connect(self.onRemoveImages)
        self.startPushButton.clicked.connect(self.onStart)
        self.methodTabWidget.currentChanged.connect(self.small_screwdriver.methodChanged)
        self.binSizeComboBox.currentIndexChanged.connect(self.small_screwdriver.binSizeChanged)

        self.settingsPushButton.clicked.connect(self.settings_window.show)

        self.small_screwdriver.images_changed.connect(self.updateImages)

        self.small_screwdriver.bin_packing_thread.bin_packing_available.connect(self.startPushButton.setEnabled)
        self.small_screwdriver.bin_packing_thread.on_end.connect(self.startPushButton.setEnabled)
        self.small_screwdriver.bin_packing_thread.on_end.connect(self.progress_window.setHidden)
        self.small_screwdriver.bin_packing_thread.packing_progress.connect(
            self.progress_window.binPackingProgressBar.setValue)
        self.small_screwdriver.bin_packing_thread.saving_progress.connect(
            self.progress_window.savingProgressBar.setValue)

        self.startPushButton.setEnabled(self.small_screwdriver.bin_packing_thread.binPackingAvailable())

        # Настройки
        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, COMPANY, APPNAME)

        # Востанавливаем ...
        # ... геометрию окна
        self.restoreGeometry(self.settings.value(SETTINGS_GEOMETRY))
        self.splitter.restoreState(self.settings.value(SETTINGS_SPLITTER1))
        self.splitter_2.restoreState(self.settings.value(SETTINGS_SPLITTER2))

        # ... размер контейнера
        self.binSizeComboBox.setCurrentIndex(int(self.settings.value(SETTINGS_SIZE, defaultValue=0)))

        # ... метод упаковки
        self.methodTabWidget.setCurrentIndex(int(self.settings.value(SETTINGS_METHOD, defaultValue=0)))

        # ... вариант упоковки от лучшего варианта или от худшего
        self.firstFitShelfVariantComboBox.setCurrentIndex(int(self.settings.value(SETTINGS_FIRST_FIT_VARIANT,
                                                                                  defaultValue=0)))
        # ... эвристику упаковки
        self.firstFitShelfHeuristicComboBox.setCurrentIndex(int(self.settings.value(SETTINGS_FIRST_FIT_HEURISTIC,
                                                                                    defaultValue=0)))

        # ... вариант для гильотины
        self.guillotineVariantComboBox.setCurrentIndex(int(self.settings.value(SETTINGS_VARIANT, defaultValue=0)))
        # ... эвристику для гильотины
        self.guillotineHeuristicComboBox.setCurrentIndex(int(self.settings.value(SETTINGS_HEURISTIC, defaultValue=0)))

        # ... правило разделения гильотиной
        self.splitComboBox.setCurrentIndex(int(self.settings.value(SETTINGS_SPLIT_RULE, defaultValue=0)))

        # ... масштаб отрисовки
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
        self.progress_window.show()

    def updateImages(self, images):
        self.imageList.clear()
        self.imageList.addItems(images)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, e):
        self.progress_window.close()
        self.settings.setValue(SETTINGS_GEOMETRY, self.saveGeometry())
        self.settings.setValue(SETTINGS_SPLITTER1, self.splitter.saveState())
        self.settings.setValue(SETTINGS_SPLITTER2, self.splitter_2.saveState())
        self.settings.setValue(SETTINGS_SIZE, self.binSizeComboBox.currentIndex())

        self.settings.setValue(SETTINGS_METHOD, self.methodTabWidget.currentIndex())

        self.settings.setValue(SETTINGS_FIRST_FIT_VARIANT, self.firstFitShelfVariantComboBox.currentIndex())
        self.settings.setValue(SETTINGS_FIRST_FIT_HEURISTIC, self.firstFitShelfHeuristicComboBox.currentIndex())

        self.settings.setValue(SETTINGS_VARIANT, self.guillotineVariantComboBox.currentIndex())
        self.settings.setValue(SETTINGS_HEURISTIC, self.guillotineHeuristicComboBox.currentIndex())
        self.settings.setValue(SETTINGS_SPLIT_RULE, self.splitComboBox.currentIndex())

        self.settings.setValue(SETTINGS_DRAW_SCALE, self.small_screwdriver.scale)
