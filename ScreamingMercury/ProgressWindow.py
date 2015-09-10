# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScreamingMercury/ProgressWindow.ui'
#
# Created: Thu Sep 10 16:56:51 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ProgressWindow(object):
    def setupUi(self, ProgressWindow):
        ProgressWindow.setObjectName("ProgressWindow")
        ProgressWindow.resize(476, 146)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main/screwdriver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ProgressWindow.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ProgressWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtGui.QGroupBox(ProgressWindow)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.binPackingProgressBar = QtGui.QProgressBar(self.groupBox)
        self.binPackingProgressBar.setProperty("value", 24)
        self.binPackingProgressBar.setObjectName("binPackingProgressBar")
        self.verticalLayout.addWidget(self.binPackingProgressBar)
        self.verticalLayout_2.addWidget(self.groupBox)
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
        self.groupBox.setTitle(QtGui.QApplication.translate("ProgressWindow", "Упаковка", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ProgressWindow", "Сохранение", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
