# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Pavel/workspace/Small-Screwdriver/ScreamingMercury/ScreamingMercuryWindow.ui'
#
# Created: Sun Sep 06 13:46:04 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ScreamingMercury(object):
    def setupUi(self, ScreamingMercury):
        ScreamingMercury.setObjectName("ScreamingMercury")
        ScreamingMercury.resize(1443, 1009)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main/screwdriver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ScreamingMercury.setWindowIcon(icon)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(ScreamingMercury)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.splitter_2 = QtGui.QSplitter(ScreamingMercury)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.groupBox_2 = QtGui.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imageList = QtGui.QListWidget(self.groupBox_2)
        self.imageList.setObjectName("imageList")
        self.verticalLayout.addWidget(self.imageList)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addDirectory = QtGui.QPushButton(self.groupBox_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/main/list_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addDirectory.setIcon(icon1)
        self.addDirectory.setIconSize(QtCore.QSize(24, 24))
        self.addDirectory.setObjectName("addDirectory")
        self.horizontalLayout.addWidget(self.addDirectory)
        self.removeImage = QtGui.QPushButton(self.groupBox_2)
        self.removeImage.setWhatsThis("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/main/trash_green_full.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeImage.setIcon(icon2)
        self.removeImage.setIconSize(QtCore.QSize(24, 24))
        self.removeImage.setShortcut("")
        self.removeImage.setObjectName("removeImage")
        self.horizontalLayout.addWidget(self.removeImage)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.binSizeComboBox = QtGui.QComboBox(self.groupBox)
        self.binSizeComboBox.setObjectName("binSizeComboBox")
        self.binSizeComboBox.addItem("")
        self.binSizeComboBox.addItem("")
        self.binSizeComboBox.addItem("")
        self.binSizeComboBox.addItem("")
        self.binSizeComboBox.addItem("")
        self.binSizeComboBox.addItem("")
        self.verticalLayout_2.addWidget(self.binSizeComboBox)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.methodTabWidget = QtGui.QTabWidget(self.layoutWidget)
        self.methodTabWidget.setObjectName("methodTabWidget")
        self.tabShelfNextFit = QtGui.QWidget()
        self.tabShelfNextFit.setObjectName("tabShelfNextFit")
        self.methodTabWidget.addTab(self.tabShelfNextFit, "")
        self.tabShelfFirstFit = QtGui.QWidget()
        self.tabShelfFirstFit.setObjectName("tabShelfFirstFit")
        self.methodTabWidget.addTab(self.tabShelfFirstFit, "")
        self.tabGuillotine = QtGui.QWidget()
        self.tabGuillotine.setObjectName("tabGuillotine")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabGuillotine)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_3 = QtGui.QGroupBox(self.tabGuillotine)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.fitVariantComboBox = QtGui.QComboBox(self.groupBox_3)
        self.fitVariantComboBox.setObjectName("fitVariantComboBox")
        self.fitVariantComboBox.addItem("")
        self.fitVariantComboBox.addItem("")
        self.verticalLayout_6.addWidget(self.fitVariantComboBox)
        self.heuristicComboBox = QtGui.QComboBox(self.groupBox_3)
        self.heuristicComboBox.setObjectName("heuristicComboBox")
        self.heuristicComboBox.addItem("")
        self.heuristicComboBox.addItem("")
        self.heuristicComboBox.addItem("")
        self.verticalLayout_6.addWidget(self.heuristicComboBox)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.tabGuillotine)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitComboBox = QtGui.QComboBox(self.groupBox_4)
        self.splitComboBox.setObjectName("splitComboBox")
        self.splitComboBox.addItem("")
        self.splitComboBox.addItem("")
        self.splitComboBox.addItem("")
        self.splitComboBox.addItem("")
        self.splitComboBox.addItem("")
        self.splitComboBox.addItem("")
        self.verticalLayout_5.addWidget(self.splitComboBox)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        spacerItem = QtGui.QSpacerItem(20, 197, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.methodTabWidget.addTab(self.tabGuillotine, "")
        self.tabMaxRects = QtGui.QWidget()
        self.tabMaxRects.setObjectName("tabMaxRects")
        self.methodTabWidget.addTab(self.tabMaxRects, "")
        self.verticalLayout_3.addWidget(self.methodTabWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.startPushButton = QtGui.QPushButton(self.layoutWidget)
        self.startPushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/main/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startPushButton.setIcon(icon3)
        self.startPushButton.setIconSize(QtCore.QSize(128, 128))
        self.startPushButton.setObjectName("startPushButton")
        self.horizontalLayout_2.addWidget(self.startPushButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.layoutWidget1 = QtGui.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.work_layout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.work_layout.setContentsMargins(0, 0, 0, 0)
        self.work_layout.setObjectName("work_layout")
        self.horizontalLayout_3.addWidget(self.splitter_2)

        self.retranslateUi(ScreamingMercury)
        self.methodTabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(ScreamingMercury)

    def retranslateUi(self, ScreamingMercury):
        ScreamingMercury.setWindowTitle(QtGui.QApplication.translate("ScreamingMercury", "Кричащая ртуть - упаковщик текстур", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ScreamingMercury", "Изображения", None, QtGui.QApplication.UnicodeUTF8))
        self.addDirectory.setToolTip(QtGui.QApplication.translate("ScreamingMercury", "Добавить папку с изображениями", None, QtGui.QApplication.UnicodeUTF8))
        self.addDirectory.setText(QtGui.QApplication.translate("ScreamingMercury", "Добавить", None, QtGui.QApplication.UnicodeUTF8))
        self.removeImage.setToolTip(QtGui.QApplication.translate("ScreamingMercury", "Убрать выделенное изображение", None, QtGui.QApplication.UnicodeUTF8))
        self.removeImage.setText(QtGui.QApplication.translate("ScreamingMercury", "Убрать", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ScreamingMercury", "Максимальный размер атласов", None, QtGui.QApplication.UnicodeUTF8))
        self.binSizeComboBox.setItemText(0, QtGui.QApplication.translate("ScreamingMercury", "256 x 256", None, QtGui.QApplication.UnicodeUTF8))
        self.binSizeComboBox.setItemText(1, QtGui.QApplication.translate("ScreamingMercury", "512 x 512", None, QtGui.QApplication.UnicodeUTF8))
        self.binSizeComboBox.setItemText(2, QtGui.QApplication.translate("ScreamingMercury", "1024 x 1024", None, QtGui.QApplication.UnicodeUTF8))
        self.binSizeComboBox.setItemText(3, QtGui.QApplication.translate("ScreamingMercury", "2048 x 2048", None, QtGui.QApplication.UnicodeUTF8))
        self.binSizeComboBox.setItemText(4, QtGui.QApplication.translate("ScreamingMercury", "4096 x 4096", None, QtGui.QApplication.UnicodeUTF8))
        self.binSizeComboBox.setItemText(5, QtGui.QApplication.translate("ScreamingMercury", "8192 x 8192", None, QtGui.QApplication.UnicodeUTF8))
        self.methodTabWidget.setTabText(self.methodTabWidget.indexOf(self.tabShelfNextFit), QtGui.QApplication.translate("ScreamingMercury", "Shelf Next Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.methodTabWidget.setTabText(self.methodTabWidget.indexOf(self.tabShelfFirstFit), QtGui.QApplication.translate("ScreamingMercury", "Shelf First Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ScreamingMercury", "Эвристика выбора", None, QtGui.QApplication.UnicodeUTF8))
        self.fitVariantComboBox.setItemText(0, QtGui.QApplication.translate("ScreamingMercury", "Best Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.fitVariantComboBox.setItemText(1, QtGui.QApplication.translate("ScreamingMercury", "Worst Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.heuristicComboBox.setItemText(0, QtGui.QApplication.translate("ScreamingMercury", "Best/Worst Area Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.heuristicComboBox.setItemText(1, QtGui.QApplication.translate("ScreamingMercury", "Best/Worst Short Side Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.heuristicComboBox.setItemText(2, QtGui.QApplication.translate("ScreamingMercury", "Best/Worst Long Side Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("ScreamingMercury", "Правило разделения", None, QtGui.QApplication.UnicodeUTF8))
        self.splitComboBox.setItemText(0, QtGui.QApplication.translate("ScreamingMercury", "Shorter Axis Split", None, QtGui.QApplication.UnicodeUTF8))
        self.splitComboBox.setItemText(1, QtGui.QApplication.translate("ScreamingMercury", "Longer Axis Split", None, QtGui.QApplication.UnicodeUTF8))
        self.splitComboBox.setItemText(2, QtGui.QApplication.translate("ScreamingMercury", "Shorter Leftover Axis Split", None, QtGui.QApplication.UnicodeUTF8))
        self.splitComboBox.setItemText(3, QtGui.QApplication.translate("ScreamingMercury", "Longer Leftover Axis Split", None, QtGui.QApplication.UnicodeUTF8))
        self.splitComboBox.setItemText(4, QtGui.QApplication.translate("ScreamingMercury", "Max Area Split", None, QtGui.QApplication.UnicodeUTF8))
        self.splitComboBox.setItemText(5, QtGui.QApplication.translate("ScreamingMercury", "Min Area Split", None, QtGui.QApplication.UnicodeUTF8))
        self.methodTabWidget.setTabText(self.methodTabWidget.indexOf(self.tabGuillotine), QtGui.QApplication.translate("ScreamingMercury", "Guillotine", None, QtGui.QApplication.UnicodeUTF8))
        self.methodTabWidget.setTabText(self.methodTabWidget.indexOf(self.tabMaxRects), QtGui.QApplication.translate("ScreamingMercury", "Max Rects", None, QtGui.QApplication.UnicodeUTF8))
        self.startPushButton.setToolTip(QtGui.QApplication.translate("ScreamingMercury", "Поехали!", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc