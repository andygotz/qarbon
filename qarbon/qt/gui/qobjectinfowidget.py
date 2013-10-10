#------------------------------------------------------------------------------
# This file is part of Framework4, a graphical toolkit to build beamline
# applications
#
# http://forge.epn-campus.eu/projects/framework4
#
# Copyright 2013
#           European Synchrotron Radiation Facility,
#           BP 220, Grenoble 38043, FRANCE
#
# Framework4 is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Framework is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Framework.  If not, see <http://www.gnu.org/licenses/>.
#------------------------------------------------------------------------------

"""A widget which displays/edits information about a QObject"""

__all__ = ["QObjectInfoWidget"]

__docformat__ = 'restructuredtext'

from qarbon.external.qt import QtCore, QtGui
from qarbon.qt.gui.icon import getIcon
from qarbon.qt.gui.propertyeditor import PropertyEditor
from qarbon.qt.gui.treeqobject import TreeQObjectWidget


class QObjectInfoWidget(QtGui.QWidget):

    def __init__(self, parent=None, qobject=None):
        super(QObjectInfoWidget, self).__init__(parent)
        self.setWindowIcon(getIcon("applications-development"))
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
    from qarbon.qt.gui.application import getApplication
    app = getApplication()
    w = buildGUI()
    w.show()
    inspector = QObjectInfoWidget(qobject=None)
    inspector.setAttribute(QtCore.Qt.WA_QuitOnClose, False)
    inspector.show()
    app.exec_()

if __name__ == "__main__":
    main()
