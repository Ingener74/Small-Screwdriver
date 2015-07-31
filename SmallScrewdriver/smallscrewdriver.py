# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SmallScrewdriver/smallscrewdriver.ui'
#
# Created: Fri Jul 31 19:31:25 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SmallScrewdriver(object):
    def setupUi(self, SmallScrewdriver):
        SmallScrewdriver.setObjectName("SmallScrewdriver")
        SmallScrewdriver.resize(948, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main/screwdriver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SmallScrewdriver.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(SmallScrewdriver)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtGui.QGroupBox(SmallScrewdriver)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.go = QtGui.QPushButton(self.groupBox)
        self.go.setIcon(icon)
        self.go.setIconSize(QtCore.QSize(32, 32))
        self.go.setObjectName("go")
        self.horizontalLayout_2.addWidget(self.go)
        spacerItem = QtGui.QSpacerItem(709, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(SmallScrewdriver)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scaleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.scaleSpinBox.setMinimum(0.05)
        self.scaleSpinBox.setMaximum(10.0)
        self.scaleSpinBox.setSingleStep(0.02)
        self.scaleSpinBox.setProperty("value", 1.0)
        self.scaleSpinBox.setObjectName("scaleSpinBox")
        self.horizontalLayout.addWidget(self.scaleSpinBox)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(SmallScrewdriver)
        QtCore.QMetaObject.connectSlotsByName(SmallScrewdriver)

    def retranslateUi(self, SmallScrewdriver):
        SmallScrewdriver.setWindowTitle(QtGui.QApplication.translate("SmallScrewdriver", "Упаковщик текстур", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SmallScrewdriver", "Кнопачки", None, QtGui.QApplication.UnicodeUTF8))
        self.go.setText(QtGui.QApplication.translate("SmallScrewdriver", "Поехали!", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("SmallScrewdriver", "Масштаб", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
