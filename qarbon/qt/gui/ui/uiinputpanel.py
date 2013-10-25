# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inputpanel.ui'
#
# Created: Fri Oct 25 17:10:53 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_InputPanel(object):
    def setupUi(self, InputPanel):
        InputPanel.setObjectName(_fromUtf8("InputPanel"))
        InputPanel.resize(549, 174)
        self.gridLayout = QtGui.QGridLayout(InputPanel)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonPanelWidget = QtGui.QWidget(InputPanel)
        self.buttonPanelWidget.setObjectName(_fromUtf8("buttonPanelWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.buttonPanelWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(self.buttonPanelWidget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.setStretch(0, 1)
        self.gridLayout.addWidget(self.buttonPanelWidget, 4, 0, 1, 2)
        self.iconTextLayout = QtGui.QHBoxLayout()
        self.iconTextLayout.setObjectName(_fromUtf8("iconTextLayout"))
        self.iconLabel = QtGui.QLabel(InputPanel)
        self.iconLabel.setObjectName(_fromUtf8("iconLabel"))
        self.iconTextLayout.addWidget(self.iconLabel)
        self.textLabel = QtGui.QLabel(InputPanel)
        self.textLabel.setObjectName(_fromUtf8("textLabel"))
        self.iconTextLayout.addWidget(self.textLabel)
        self.iconTextLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.iconTextLayout, 1, 0, 2, 2)
        self.inputPanel = QtGui.QWidget(InputPanel)
        self.inputPanel.setObjectName(_fromUtf8("inputPanel"))
        self.gridLayout.addWidget(self.inputPanel, 3, 0, 1, 2)
        self.gridLayout.setRowStretch(3, 1)

        self.retranslateUi(InputPanel)
        QtCore.QMetaObject.connectSlotsByName(InputPanel)

    def retranslateUi(self, InputPanel):
        InputPanel.setWindowTitle(_translate("InputPanel", "Form", None))
        self.iconLabel.setText(_translate("InputPanel", "iconLabel", None))
        self.textLabel.setText(_translate("InputPanel", "textLabel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    InputPanel = QtGui.QWidget()
    ui = Ui_InputPanel()
    ui.setupUi(InputPanel)
    InputPanel.show()
    sys.exit(app.exec_())

