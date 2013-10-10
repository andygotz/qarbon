# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'propertyeditor.ui'
#
# Created: Thu Oct 10 13:02:36 2013
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

class Ui_propertyEditor(object):
    def setupUi(self, propertyEditor):
        propertyEditor.setObjectName(_fromUtf8("propertyEditor"))
        propertyEditor.resize(587, 655)
        self.gridLayout = QtGui.QGridLayout(propertyEditor)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.superClassNameLineEdit = QtGui.QLineEdit(propertyEditor)
        self.superClassNameLineEdit.setReadOnly(True)
        self.superClassNameLineEdit.setObjectName(_fromUtf8("superClassNameLineEdit"))
        self.gridLayout.addWidget(self.superClassNameLineEdit, 2, 1, 1, 2)
        self.classLabel = QtGui.QLabel(propertyEditor)
        self.classLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.classLabel.setObjectName(_fromUtf8("classLabel"))
        self.gridLayout.addWidget(self.classLabel, 0, 0, 1, 1)
        self.classNameLabel = QtGui.QLabel(propertyEditor)
        self.classNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.classNameLabel.setObjectName(_fromUtf8("classNameLabel"))
        self.gridLayout.addWidget(self.classNameLabel, 1, 0, 1, 1)
        self.superClassNameLabel = QtGui.QLabel(propertyEditor)
        self.superClassNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.superClassNameLabel.setObjectName(_fromUtf8("superClassNameLabel"))
        self.gridLayout.addWidget(self.superClassNameLabel, 2, 0, 1, 1)
        self.isWidgetLabel = QtGui.QLabel(propertyEditor)
        self.isWidgetLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.isWidgetLabel.setObjectName(_fromUtf8("isWidgetLabel"))
        self.gridLayout.addWidget(self.isWidgetLabel, 3, 0, 1, 1)
        self.isWidgetLineEdit = QtGui.QLineEdit(propertyEditor)
        self.isWidgetLineEdit.setReadOnly(True)
        self.isWidgetLineEdit.setObjectName(_fromUtf8("isWidgetLineEdit"))
        self.gridLayout.addWidget(self.isWidgetLineEdit, 3, 1, 1, 1)
        self.classNameLineEdit = QtGui.QLineEdit(propertyEditor)
        self.classNameLineEdit.setReadOnly(True)
        self.classNameLineEdit.setObjectName(_fromUtf8("classNameLineEdit"))
        self.gridLayout.addWidget(self.classNameLineEdit, 1, 1, 1, 2)
        self.focusButton = QtGui.QPushButton(propertyEditor)
        self.focusButton.setObjectName(_fromUtf8("focusButton"))
        self.gridLayout.addWidget(self.focusButton, 3, 2, 1, 1)
        self.classLineEdit = QtGui.QLineEdit(propertyEditor)
        self.classLineEdit.setReadOnly(True)
        self.classLineEdit.setObjectName(_fromUtf8("classLineEdit"))
        self.gridLayout.addWidget(self.classLineEdit, 0, 1, 1, 2)
        self.propertiesGroupBox = QtGui.QGroupBox(propertyEditor)
        self.propertiesGroupBox.setObjectName(_fromUtf8("propertiesGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.propertiesGroupBox)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.propertiesTreeWidget = QtGui.QTreeWidget(self.propertiesGroupBox)
        self.propertiesTreeWidget.setAlternatingRowColors(True)
        self.propertiesTreeWidget.setIndentation(15)
        self.propertiesTreeWidget.setObjectName(_fromUtf8("propertiesTreeWidget"))
        self.propertiesTreeWidget.header().setDefaultSectionSize(200)
        self.propertiesTreeWidget.header().setMinimumSectionSize(150)
        self.verticalLayout.addWidget(self.propertiesTreeWidget)
        self.gridLayout.addWidget(self.propertiesGroupBox, 4, 0, 1, 3)
        self.gridLayout.setColumnStretch(1, 1)

        self.retranslateUi(propertyEditor)
        QtCore.QMetaObject.connectSlotsByName(propertyEditor)

    def retranslateUi(self, propertyEditor):
        propertyEditor.setWindowTitle(_translate("propertyEditor", "Form", None))
        self.classLabel.setText(_translate("propertyEditor", "class:", None))
        self.classNameLabel.setText(_translate("propertyEditor", "class name:", None))
        self.superClassNameLabel.setText(_translate("propertyEditor", "super class name:", None))
        self.isWidgetLabel.setText(_translate("propertyEditor", "is widget?:", None))
        self.focusButton.setText(_translate("propertyEditor", "focus", None))
        self.propertiesGroupBox.setTitle(_translate("propertyEditor", "Properties", None))
        self.propertiesTreeWidget.headerItem().setText(0, _translate("propertyEditor", "Name", None))
        self.propertiesTreeWidget.headerItem().setText(1, _translate("propertyEditor", "Type", None))
        self.propertiesTreeWidget.headerItem().setText(2, _translate("propertyEditor", "Value", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    propertyEditor = QtGui.QWidget()
    ui = Ui_propertyEditor()
    ui.setupUi(propertyEditor)
    propertyEditor.show()
    sys.exit(app.exec_())

