# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\prj\Small-Screwdriver\ScreamingMercury\ProgressWindow.ui'
#
# Created: Thu Oct 06 21:07:22 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ProgressWindow(object):
    def setupUi(self, ProgressWindow):
        ProgressWindow.setObjectName("ProgressWindow")
        ProgressWindow.resize(133, 289)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main/images/screwdriver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ProgressWindow.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ProgressWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.prepareGroupBox = QtGui.QGroupBox(ProgressWindow)
        self.prepareGroupBox.setObjectName("prepareGroupBox")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.prepareGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.prepareProgressBar = QtGui.QProgressBar(self.prepareGroupBox)
        self.prepareProgressBar.setProperty("value", 24)
        self.prepareProgressBar.setObjectName("prepareProgressBar")
        self.verticalLayout_5.addWidget(self.prepareProgressBar)
        self.verticalLayout_2.addWidget(self.prepareGroupBox)
        self.groupBox = QtGui.QGroupBox(ProgressWindow)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.binPackingProgressBar = QtGui.QProgressBar(self.groupBox)
        self.binPackingProgressBar.setProperty("value", 24)
        self.binPackingProgressBar.setObjectName("binPackingProgressBar")
        self.verticalLayout.addWidget(self.binPackingProgressBar)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(ProgressWindow)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verificationProgressBar = QtGui.QProgressBar(self.groupBox_3)
        self.verificationProgressBar.setProperty("value", 24)
        self.verificationProgressBar.setObjectName("verificationProgressBar")
        self.verticalLayout_4.addWidget(self.verificationProgressBar)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(ProgressWindow)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.savingProgressBar = QtGui.QProgressBar(self.groupBox_2)
        self.savingProgressBar.setProperty("value", 24)
        self.savingProgressBar.setObjectName("savingProgressBar")
        self.verticalLayout_3.addWidget(self.savingProgressBar)
        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.retranslateUi(ProgressWindow)
        QtCore.QMetaObject.connectSlotsByName(ProgressWindow)

    def retranslateUi(self, ProgressWindow):
        ProgressWindow.setWindowTitle(QtGui.QApplication.translate("ProgressWindow", "Прогресс упаковки", None, QtGui.QApplication.UnicodeUTF8))
        self.prepareGroupBox.setTitle(QtGui.QApplication.translate("ProgressWindow", "Подготовка", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ProgressWindow", "Упаковка", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ProgressWindow", "Верификация", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ProgressWindow", "Сохранение", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
