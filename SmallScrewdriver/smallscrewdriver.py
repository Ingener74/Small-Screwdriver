# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smallscrewdriver.ui'
#
# Created: Fri Jul 17 10:02:22 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SmallScrewdriver(object):
    def setupUi(self, SmallScrewdriver):
        SmallScrewdriver.setObjectName("SmallScrewdriver")
        SmallScrewdriver.resize(655, 644)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main/screwdriver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SmallScrewdriver.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(SmallScrewdriver)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(SmallScrewdriver)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.go = QtGui.QPushButton(self.groupBox)
        self.go.setIcon(icon)
        self.go.setIconSize(QtCore.QSize(32, 32))
        self.go.setObjectName("go")
        self.horizontalLayout.addWidget(self.go)
        spacerItem = QtGui.QSpacerItem(709, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(SmallScrewdriver)
        QtCore.QMetaObject.connectSlotsByName(SmallScrewdriver)

    def retranslateUi(self, SmallScrewdriver):
        SmallScrewdriver.setWindowTitle(QtGui.QApplication.translate("SmallScrewdriver", "Упаковщик текстур", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SmallScrewdriver", "Кнопачки", None, QtGui.QApplication.UnicodeUTF8))
        self.go.setText(QtGui.QApplication.translate("SmallScrewdriver", "Поехали!", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
