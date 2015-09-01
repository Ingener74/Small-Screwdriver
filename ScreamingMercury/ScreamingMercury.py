# encoding: utf8
from PySide.QtCore import (Qt, QSettings)
from PySide.QtGui import (QWidget, QFileDialog)

from ScreamingMercuryWindow import Ui_ScreamingMercury
from SmallScrewdriver import (SmallScrewdriverWidget)

COMPANY = 'Venus.Games'
APPNAME = 'SmallScrewdriver'

SETTINGS_GEOMETRY = 'Geometry'
SETTINGS_SPLITTER1 = 'Splitter1'
SETTINGS_SPLITTER2 = 'Splitter2'
SETTINGS_SIZE = 'BinSize'
SETTINGS_METHOD = 'BinPackingMethod'


class ScreamingMercury(QWidget, Ui_ScreamingMercury):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.small_screwdriver = SmallScrewdriverWidget()
        self.work_layout.insertWidget(0, self.small_screwdriver)

        self.addDirectory.clicked.connect(self.on_add_directory)
        self.removeImage.clicked.connect(self.on_remove_images)
        self.startPushButton.clicked.connect(self.on_start)
        self.methodTabWidget.currentChanged.connect(self.small_screwdriver.method_changed)
        self.binSizeComboBox.currentIndexChanged.connect(self.small_screwdriver.bin_size_changed)

        self.small_screwdriver.images_changed.connect(self.update_images)

        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, COMPANY, APPNAME)
        self.restoreGeometry(self.settings.value(SETTINGS_GEOMETRY))
        self.splitter.restoreState(self.settings.value(SETTINGS_SPLITTER1))
        self.splitter_2.restoreState(self.settings.value(SETTINGS_SPLITTER2))
        self.binSizeComboBox.setCurrentIndex(int(self.settings.value(SETTINGS_SIZE)))
        self.methodTabWidget.setCurrentIndex(int(self.settings.value(SETTINGS_METHOD)))

    def on_add_directory(self):
        directory = QFileDialog.getExistingDirectory()
        if directory != u'':
            self.small_screwdriver.set_directory(directory)

    def on_remove_images(self):
        row = self.imageList.currentRow()
        self.small_screwdriver.remove_image(row)
        self.imageList.setCurrentRow(row)

    def on_start(self):
        self.small_screwdriver.start_bin_packing()

    def update_images(self, images):
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
