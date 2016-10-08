# encoding: utf8
import math
import re

from PySide.QtCore import (Qt, QSettings, QDir, QDirIterator, Signal, QThread)
from PySide.QtGui import (QWidget, QFileDialog, QSizePolicy, QPainter, QTransform)

from SmallScrewdriver import (Point, Size, Rect, Image, GuillotineBinPacking, MaxRectsBinPacking,
                              NextFitShelfBinPacking, FirstFitShelfBinPacking, GuillotineBin, FirstFitShelfBin,
                              Bin, JupiterExporter, PListExporter,
                              BinPacking, BinPackingProgress)
from ScreamingMercuryWindow import (Ui_ScreamingMercury)
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

SETTINGS_OUTPUT_FORMAT = 'OutputFormat'

SETTINGS_DIRECTORY = 'InputDirectory'


EXPORTERS = (
    JupiterExporter,
    PListExporter
)


# noinspection PyPep8Naming
class BinPackingThread(QThread, BinPackingProgress):
    """
    Поток обработки изображений вне GUI потока
    """
    METHODS = (
        {
            'name': 'next_fit_shelf',
            'type': NextFitShelfBinPacking
        }, {
            'name': 'first_fit_shelf',
            'type': FirstFitShelfBinPacking
        }, {
            'name': 'guillotine',
            'type': GuillotineBinPacking
        }, {
            'name': 'max_rects',
            'type': MaxRectsBinPacking
        }
    )

    SIZES = (
        Size(256, 256),
        Size(512, 512),
        Size(1024, 1024),
        Size(2048, 2048),
        Size(4096, 4096),
        Size(8192, 8192)
    )

    bin_packing_available = Signal(bool)
    update_bins = Signal(Rect)

    prepare_progress_signal = Signal(int)
    packing_progress_signal = Signal(int)
    saving_progress_signal = Signal(int)
    verify_progress_signal = Signal(int)
    on_end = Signal(bool)

    def __init__(self):
        QThread.__init__(self)

        Bin.exporter = JupiterExporter()
        BinPacking.bin_packing_progress = self

        self.directory = None
        self.images = []

        self.method = BinPackingThread.METHODS[0]
        self.bin_size = BinPackingThread.SIZES[0]

        self.bin_parameter = {
            'next_fit_shelf': {
            },
            'first_fit_shelf': {
                'selection_variant': FirstFitShelfBin.BEST_VARIANTS,
                'selection_heuristic': FirstFitShelfBin.SHORT_SIDE_FIT,
            },
            'guillotine': {
                'selection_variant': GuillotineBin.BEST_VARIANTS,
                'selection_heuristic': GuillotineBin.SHORT_SIDE_FIT,
                'split_rule': Rect.RULE_SAS
            },
            'max_rects': {
            }
        }

    def setDirectory(self, directory):
        self.directory = directory
        self.bin_packing_available.emit(self.binPackingAvailable())

    def binPackingAvailable(self):
        return len(self.images) and self.directory is not None

    def setImages(self, images):
        self.images = images
        self.bin_packing_available.emit(self.binPackingAvailable())

    def setMethod(self, index):
        self.method = BinPackingThread.METHODS[index]

    def setBinSize(self, index):
        self.bin_size = BinPackingThread.SIZES[index]

    @staticmethod
    def set_exporter(index):
        Bin.exporter = EXPORTERS[index]()

    def run(self):
        if not self.directory or not len(self.images):
            return

        self.prepare_progress_signal.emit(0)
        self.packing_progress_signal.emit(0)
        self.verify_progress_signal.emit(0)
        self.saving_progress_signal.emit(0)

        images = []
        for i, image in enumerate(self.images):
            self.prepare_progress_signal.emit(int(100 * float(i) / float(len(self.images))))
            images.append(Image(self.directory, image))

        bin_packing = self.method['type'](self.bin_size,
                                          images,
                                          bin_parameters=self.bin_parameter[self.method['name']])
        bin_packing.saveAtlases(self.directory + QDir.separator())

        self.update_bins.emit(bin_packing.bins)
        self.on_end.emit(True)

    def packing_progress(self, percent):
        self.packing_progress_signal.emit(percent)

    def saving_progress(self, percent):
        self.saving_progress_signal.emit(percent)

    def verify_progress(self, percent):
        pass


# noinspection PyPep8Naming
class DrawBinsWidget(QWidget):
    """
    Виджет отрисовки контейнеров
    """

    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.bins = []
        self.scale = 1.0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setWorldTransform(QTransform().scale(self.scale, self.scale))

        for i, b in enumerate(self.bins):
            side = int(math.ceil(math.log(len(self.bins), 2)))

            x = (i % side) * (b.size.width + 10) if side else 10
            y = (i / side) * (b.size.height + 10) if side else 10

            b.draw(painter, Point(x, y))

    def wheelEvent(self, *args, **kwargs):
        self.scale += args[0].delta() / 4800.0
        self.update()

    def redrawBins(self, bins):
        self.bins = bins
        self.update()


# noinspection PyPep8Naming
class ScreamingMercury(QWidget, Ui_ScreamingMercury):
    def __init__(self, delegate, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.delegate = delegate

        self.small_screwdriver = DrawBinsWidget()
        self.work_layout.insertWidget(0, self.small_screwdriver)

        self.progress_window = Progress()
        self.settings_window = Settings()

        self.bin_packing_thread = BinPackingThread()

        self.addDirectory.clicked.connect(self.onAddDirectory)
        self.removeImage.clicked.connect(self.onRemoveImages)
        self.startPushButton.clicked.connect(self.onStart)
        self.methodTabWidget.currentChanged.connect(self.bin_packing_thread.setMethod)
        self.binSizeComboBox.currentIndexChanged.connect(self.bin_packing_thread.setBinSize)

        self.clearPushButton.clicked.connect(self.delegate.on_remove_all_images)

        self.settingsPushButton.clicked.connect(self.settings_window.show)

        # self.images_changed.connect(self.updateImages)

        self.bin_packing_thread.bin_packing_available.connect(self.startPushButton.setEnabled)
        self.bin_packing_thread.on_end.connect(self.startPushButton.setEnabled)
        self.bin_packing_thread.on_end.connect(self.progress_window.setHidden)
        self.bin_packing_thread.prepare_progress_signal.connect(self.progress_window.prepareProgressBar.setValue)
        self.bin_packing_thread.packing_progress_signal.connect(self.progress_window.binPackingProgressBar.setValue)
        self.bin_packing_thread.saving_progress_signal.connect(self.progress_window.savingProgressBar.setValue)


        self.startPushButton.setEnabled(self.bin_packing_thread.binPackingAvailable())

        self.directory = None
        self.images = []

        self.restoreSettings()

        if self.directory:
            self.harvestDirectory(self.directory)

        self.bin_packing_thread.update_bins.connect(self.small_screwdriver.redrawBins)

        self.outputFormatComboBox.currentIndexChanged.connect(BinPackingThread.set_exporter)
        BinPackingThread.set_exporter(self.outputFormatComboBox.currentIndex())

    def restoreSettings(self):
        # Настройки
        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, COMPANY, APPNAME)

        print self.settings.fileName()

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

        self.outputFormatComboBox.setCurrentIndex(int(self.settings.value(SETTINGS_OUTPUT_FORMAT, defaultValue=0)))

        self.directory = self.settings.value(SETTINGS_DIRECTORY, defaultValue=None)

    def onAddDirectory(self):
        directory = QFileDialog.getExistingDirectory(caption='Select image directory', dir=self.directory)
        if directory != u'':
            self.directory = directory

            self.harvestDirectory(self.directory)

    def resetDirectory(self):
        self.directory = None
        self.images = []
        self.bin_packing_thread.setDirectory(self.directory)
        self.bin_packing_thread.setImages(self.images)
        self.updateImages(self.images)

    def harvestDirectory(self, directory):
        folder = QDir(path=directory)
        folder.setNameFilters(['*.png'])
        folder.setFilter(QDir.Files or QDir.NoDotAndDotDot)
        dit = QDirIterator(folder, flags=QDirIterator.Subdirectories, filters=QDir.Files)
        while dit.hasNext():
            im = folder.relativeFilePath(dit.next())
            if not re.search('atlas', im):
                self.images.append(im)
        self.bin_packing_thread.setDirectory(self.directory)
        self.bin_packing_thread.setImages(self.images)
        self.updateImages(self.images)

    def onRemoveImages(self):
        row = self.imageList.currentRow()

        del self.images[row]
        self.updateImages(self.images)

        self.imageList.setCurrentRow(row)

    def onStart(self):
        self.startPushButton.setEnabled(False)
        self.bin_packing_thread.start()
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

        self.settings.setValue(SETTINGS_OUTPUT_FORMAT, self.outputFormatComboBox.currentIndex())

        self.settings.setValue(SETTINGS_DIRECTORY, self.directory)