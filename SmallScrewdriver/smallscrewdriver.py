# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SmallScrewdriver/smallscrewdriver.ui'
#
# Created: Wed Aug 05 23:03:42 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SmallScrewdriver(object):
    def setupUi(self, SmallScrewdriver):
        SmallScrewdriver.setObjectName("SmallScrewdriver")
        SmallScrewdriver.resize(1059, 868)
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
        self.methodGroupBox = QtGui.QGroupBox(SmallScrewdriver)
        self.methodGroupBox.setObjectName("methodGroupBox")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.methodGroupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.methodComboBox = QtGui.QComboBox(self.methodGroupBox)
        self.methodComboBox.setObjectName("methodComboBox")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.methodComboBox)
        self.horizontalLayout_3.addWidget(self.methodGroupBox)
        self.binSizeGroupBox = QtGui.QGroupBox(SmallScrewdriver)
        self.binSizeGroupBox.setObjectName("binSizeGroupBox")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.binSizeGroupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.binSizeComboBox = QtGui.QComboBox(self.binSizeGroupBox)
        self.binSizeComboBox.setObjectName("binSizeComboBox")
        self.binSizeComboBox.addItem("")
        self.binSizeComboBox.addItem("")
        self.binSizeComboBox.addItem("")
        self.binSizeComboBox.addItem("")
        self.binSizeComboBox.addItem("")
        self.binSizeComboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.binSizeComboBox)
        self.horizontalLayout_3.addWidget(self.binSizeGroupBox)
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
        self.methodGroupBox.setTitle(QtGui.QApplication.translate("SmallScrewdriver", "Метод", None, QtGui.QApplication.UnicodeUTF8))
        self.methodComboBox.setItemText(0, QtGui.QApplication.translate("SmallScrewdriver", "Shelf First Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.methodComboBox.setItemText(1, QtGui.QApplication.translate("SmallScrewdriver", "Recursive Shelf", None, QtGui.QApplication.UnicodeUTF8))
        self.binSizeGroupBox.setTitle(QtGui.QApplication.translate("SmallScrewdriver", "Размер атласов", None, QtGui.QApplication.UnicodeUTF8))
        self.binSizeComboBox.setItemText(0, QtGui.QApplication.translate("SmallScrewdriver", "256 x 256", None, QtGui.QApplication.UnicodeUTF8))
        self.binSizeComboBox.setItemText(1, QtGui.QApplication.translate("SmallScrewdriver", "512 x 512", None, QtGui.QApplication.UnicodeUTF8))
        self.binSizeComboBox.setItemText(2, QtGui.QApplication.translate("SmallScrewdriver", "1024 x 1024", None, QtGui.QApplication.UnicodeUTF8))
        self.binSizeComboBox.setItemText(3, QtGui.QApplication.translate("SmallScrewdriver", "2048 x 2048", None, QtGui.QApplication.UnicodeUTF8))
        self.binSizeComboBox.setItemText(4, QtGui.QApplication.translate("SmallScrewdriver", "4096 x 4096", None, QtGui.QApplication.UnicodeUTF8))
        self.binSizeComboBox.setItemText(5, QtGui.QApplication.translate("SmallScrewdriver", "8192 x 8192", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("SmallScrewdriver", "Масштаб", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
