# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScreamingMercury/ProgressWindow.ui'
#
# Created: Tue Sep  8 09:24:57 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ProgressWindow(object):
    def setupUi(self, ProgressWindow):
        ProgressWindow.setObjectName("ProgressWindow")
        ProgressWindow.resize(471, 79)
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

        self.retranslateUi(ProgressWindow)
        QtCore.QMetaObject.connectSlotsByName(ProgressWindow)

    def retranslateUi(self, ProgressWindow):
        ProgressWindow.setWindowTitle(QtGui.QApplication.translate("ProgressWindow", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ProgressWindow", "Упаковка", None, QtGui.QApplication.UnicodeUTF8))

