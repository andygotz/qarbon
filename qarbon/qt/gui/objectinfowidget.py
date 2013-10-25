# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
#
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""A widget which displays/edits information about a QObject.

Example::

    from qarbon.external.qt import QtCore, QtGui
    from qarbon.qt.gui.application import Application
    from qarbon.qt.gui.qobjectinfowidget import ObjectInfoWidget

    app = Application()

    # mw will be the QObject to be "seen"
    mw = QtGui.QMainWindow()
    mw.setObjectName("main window")
    w = QtGui.QWidget()
    w.setObjectName("central widget")
    mw.setCentralWidget(w)
    l = QtGui.QVBoxLayout()
    w.setLayout(l)
    l1 = QtGui.QLabel("H1")
    l1.setObjectName("label 1")
    l.addWidget(l1)
    l2 = QtGui.QLabel("H2")
    l2.setObjectName("label 2")
    l.addWidget(l2)
    mw.show()

    inspector = ObjectInfoWidget(qobject=mw)
    inspector.setAttribute(QtCore.Qt.WA_QuitOnClose, False)
    inspector.show()
    app.exec_()"""

__all__ = ["ObjectInfoWidget"]

from qarbon.external.qt import QtCore, QtGui
from qarbon.qt.gui.icon import Icon
from qarbon.qt.gui.propertyeditor import PropertyEditor
from qarbon.qt.gui.treeqobject import TreeQObjectWidget


class ObjectInfoWidget(QtGui.QWidget):
    """A widget which displays/edits information about a QObject."""

    def __init__(self, parent=None, qobject=None):
        super(ObjectInfoWidget, self).__init__(parent)
        self.setWindowIcon(Icon("applications-development"))
        self.setWindowTitle("QObject Inspector")
        layout = QtGui.QHBoxLayout()
        self.setLayout(layout)
        layout.setSpacing(0)
        layout.setMargin(0)
        self.__splitter = splitter = QtGui.QSplitter(QtCore.Qt.Horizontal,
                                                     self)
        layout.addWidget(splitter)

        self.__form = form = PropertyEditor(parent=splitter, qobject=qobject)
        self.__tree = tree = TreeQObjectWidget(parent=splitter,
                                               qobject=qobject)
        splitter.addWidget(tree)
        splitter.addWidget(form)

        treeSelectionModel = tree.viewWidget().selectionModel()
        QtCore.QObject.connect(treeSelectionModel,
            QtCore.SIGNAL("selectionChanged(QItemSelection, QItemSelection)"),
            self.__onSelectionChanged)

    def __onSelectionChanged(self, selected, deselected):
        indexes = selected.indexes()
        if len(indexes):
            index = indexes[0]
            qobject = index.internalPointer().qobject()
        else:
            qobject = None
        self.__form.setQObject(qobject)

    def setQObject(self, qobject):
        self.__tree.getBaseQModel().setDataSource(qobject)
        self.__form.setQObject(qobject)


def buildGUI():
    mw = QtGui.QMainWindow()
    mw.setObjectName("main window")
    w = QtGui.QWidget()
    w.setObjectName("central widget")
    mw.setCentralWidget(w)
    l = QtGui.QVBoxLayout()
    w.setLayout(l)
    l1 = QtGui.QLabel("H1")
    l1.setObjectName("label 1")
    l.addWidget(l1)
    l2 = QtGui.QLabel("H2")
    l2.setObjectName("label 2")
    l.addWidget(l2)
    mw.show()
    return mw


def main():
    from qarbon.qt.gui.application import Application
    app = Application()
    w = buildGUI()
    w.show()
    inspector = ObjectInfoWidget(qobject=w)
    inspector.setAttribute(QtCore.Qt.WA_QuitOnClose, False)
    inspector.show()
    app.exec_()

if __name__ == "__main__":
    main()
