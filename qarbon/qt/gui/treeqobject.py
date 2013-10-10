# -*- coding: utf-8 -*-

##############################################################################
##
## This file is part of qarbon
##
## http://www.qarbon.org/
##
## Copyright 2013 European Synchrotron Radiation Facility, Grenoble, France
##
## qarbon is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## qarbon is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with qarbon.  If not, see <http://www.gnu.org/licenses/>.
##
##############################################################################

"""A tree widget which represents QObject hierarchy (used for development \
purposes)"""

__all__ = ["QObjectRepresentation", "getQObjectTree", "getQObjectTreeStr",
           "TreeQObjectInfoModel", "TreeQObjectWidget"]

__docformat__ = 'restructuredtext'

import logging
import weakref

from qarbon.external.enum import Enum
from qarbon.external.qt import QtCore, QtGui

from qarbon.qt.gui.icon import getIcon
from qarbon.qt.gui.application import getApplication
from qarbon.qt.gui.basetree import BaseTreeWidget
from qarbon.qt.gui.basemodel import BaseModel, BaseTreeItem


class QObjectRepresentation(Enum):
    "possible displays of a QObject"
    ClassName, ObjectName, FullName = range(3)


QR = QObjectRepresentation

__DEFAULT_FILTER_CLASSES = QtCore.QPropertyAnimation, QtGui.QPanGesture


def _filter(qobject):
    # Filter
    if isinstance(qobject, __DEFAULT_FILTER_CLASSES):
        return
    return qobject


def _buildQObjectsAsDict(qobject, container, ffilter=_filter):

    container[qobject] = childs = {}
    for child in qobject.children():
        # Filter
        if not ffilter(child) is None:
            _buildQObjectsAsDict(child, childs, ffilter=ffilter)


def getQObjectTreeAsDict(qobject=None, ffilter=_filter):

    if qobject is None:
        app = getApplication()
        qobjects = [app] + app.topLevelWidgets()
    else:
        qobjects = [qobject]

    tree = {}
    for qobject in qobjects:
        if not ffilter(qobject) is None:
            _buildQObjectsAsDict(qobject, tree, ffilter=ffilter)

    return tree


def _buildQObjectsAsList(qobject, container, ffilter=_filter):

    children = qobject.children()
    node = qobject, []
    container.append(node)
    for child in children:
        if not ffilter(child) is None:
            _buildQObjectsAsList(child, node[1], ffilter=ffilter)


def getQObjectTreeAsList(qobject=None, ffilter=_filter):

    if qobject is None:
        app = getApplication()
        qobjects = [app] + app.topLevelWidgets()
    else:
        qobjects = [qobject]

    tree = []
    for qobject in qobjects:
        if not ffilter(qobject) is None:
            _buildQObjectsAsList(qobject, tree, ffilter=ffilter)

    return tree

getQObjectTree = getQObjectTreeAsList


def _getQObjectStr(qobject, representation):
    if qobject is None:
        return 'Null'

    if representation == QObjectRepresentation.ClassName:
        return qobject.__class__.__name__

    try:
        objectName = qobject.objectName()
    except RuntimeError:
        logging.error("error accessing object %s", qobject)
        logging.debug("details: ", exc_info=1)
        if representation == QObjectRepresentation.ClassName:
            return qobject.__class__.__name__
        else:
            return "> ERROR! <"

    if representation == QObjectRepresentation.ObjectName:
        return objectName
    elif representation == QObjectRepresentation.FullName:
        className = qobject.metaObject().className()
        return '{0}("{1}")'.format(className, objectName)
    return str(qobject)


def _buildQObjectStr(node, str_tree,
                       representation=QObjectRepresentation.ClassName,
                       ffilter=_filter):

    qobject, children = node
    str_node = _getQObjectStr(qobject, representation)
    str_children = []
    if len(children):
        str_tree.append((str_node, str_children))
        for child in children:
            if ffilter(child):
                _buildQObjectStr(child, str_children,
                                   representation=representation,
                                   ffilter=ffilter)
    else:
        str_tree.append(str_node)


def getQObjectTreeStr(qobject=None,
                         representation=QObjectRepresentation.ClassName,
                         ffilter=_filter):

    tree, str_tree = getQObjectTree(qobject=qobject, ffilter=ffilter), []
    for e in tree:
        _buildQObjectStr(e, str_tree, representation=representation,
                           ffilter=ffilter)
    return str_tree


def _getWidgetLayout(widget):
    if not isinstance(widget, QtGui.QWidget):
        return
    parent = widget.parent()
    if parent is None or not isinstance(parent, QtGui.QWidget):
        return
    layout = parent.layout()
    if layout.indexOf(widget) < 0:
        return
    return layout


def getQObjectIcon(qo):
    if isinstance(qo, QtGui.QWidget):
        name = "widget"
        if isinstance(qo, QtGui.QLabel):
            name = "label"
        elif isinstance(qo, QtGui.QComboBox):
            name = "combobox"
        elif isinstance(qo, QtGui.QDoubleSpinBox):
            name = "doublespinbox"
        elif isinstance(qo, QtGui.QDateEdit):
            name = "dateedit"
        elif isinstance(qo, QtGui.QTimeEdit):
            name = "timeedit"
        elif isinstance(qo, QtGui.QDateTimeEdit):
            name = "datetimeedit"
        elif isinstance(qo, QtGui.QLineEdit):
            name = "linedit"
        elif isinstance(qo, QtGui.QPlainTextEdit):
            name = "plaintextedit"
        elif isinstance(qo, QtGui.QTextEdit):
            name = "textedit"
        elif isinstance(qo, QtGui.QTabWidget):
            name = "tabwidget"
        elif isinstance(qo, QtGui.QRadioButton):
            name = "radiobutton"
        elif isinstance(qo, QtGui.QPushButton):
            name = "pushbutton"
        elif isinstance(qo, QtGui.QToolButton):
            name = "toolbutton"
        elif isinstance(qo, QtGui.QCheckBox):
            name = "checkbox"
        elif isinstance(qo, QtGui.QToolBox):
            name = "toolbox"
        elif isinstance(qo, QtGui.QTreeView):
            name = "tree"
        elif isinstance(qo, QtGui.QTableView):
            name = "table"
        elif isinstance(qo, QtGui.QListView):
            name = "listbox"
        elif isinstance(qo, QtGui.QStackedWidget):
            name = "widgetstack"
        elif isinstance(qo, QtGui.QDockWidget):
            name = "dockwidget"
        elif isinstance(qo, QtGui.QDockWidget):
            name = "dockwidget"
        elif isinstance(qo, QtGui.QCalendarWidget):
            name = "calendarwidget"
        elif isinstance(qo, QtGui.QDialogButtonBox):
            name = "dialogbuttonbox"
        elif isinstance(qo, QtGui.QFrame):
            name = "frame"
        elif isinstance(qo, QtGui.QAbstractSpinBox):
            name = "spinbox"
        elif isinstance(qo, QtGui.QAbstractButton):
            name = "pushbutton"
        elif isinstance(qo, QtGui.QAbstractSlider):
            name = "hslider"
        return getIcon(":/designer/" + name + ".png")
    elif isinstance(qo, QtGui.QLayout):
        name = "editform"
        if isinstance(qo, QtGui.QVBoxLayout):
            name = "editvlayout"
        elif isinstance(qo, QtGui.QHBoxLayout):
            name = "edithlayout"
        elif isinstance(qo, QtGui.QGridLayout):
            name = "editgrid"
        elif isinstance(qo, QtGui.QFormLayout):
            name = "editform"
    elif isinstance(qo, QtCore.QCoreApplication):
        return getIcon("applications-development")
    return getIcon("emblem-system")


class TreeQObjecttInfoItem(BaseTreeItem):

    def __init__(self, model, data, parent=None):
        BaseTreeItem.__init__(self, model, data, parent=parent)
        if data is not None:
            self.qobject = weakref.ref(data)
            dat = (_getQObjectStr(data, QR.ClassName),
                   _getQObjectStr(data, QR.ObjectName))
            self.setData(0, dat)
        self.__toolTip = _getQObjectStr(data, QR.FullName)
        self.__icon = getQObjectIcon(data)

    def toolTip(self, index):
        return self.__toolTip

    def icon(self, index):
        if index.column() == 0:
            return self.__icon


class TreeQObjectInfoModel(BaseModel):

    ColumnNames = "Class", "Object name"
    ColumnRoles = (QR.ClassName,), QR.ObjectName

    def __init__(self, parent=None, data=None):
        BaseModel.__init__(self, parent=parent, data=data)

    def role(self, column, depth=0):
        if column == 0:
            return self.ColumnRoles[column][0]
        return self.ColumnRoles[column]

    def roleIcon(self, taurus_role):
        return QtGui.QIcon()

    def roleSize(self, taurus_role):
        return QtCore.QSize(300, 70)

    def roleToolTip(self, role):
        return "widget information"

    @staticmethod
    def _build_qobject_item(model, parent, node):
        qobject, children = node
        item = TreeQObjecttInfoItem(model, qobject, parent)
        parent.appendChild(item)
        for child in children:
            TreeQObjectInfoModel._build_qobject_item(model, item, child)

    def setupModelData(self, qobject):
        if qobject is None:
            return
        data = getQObjectTree(qobject=qobject)
        rootItem = self._rootItem
        for node in data:
            TreeQObjectInfoModel._build_qobject_item(self, rootItem, node)


class TreeQObjectWidget(BaseTreeWidget):
    """A tree representation of the selected QObject childs"""

    KnownPerspectives = {
        "Default": {
            "label":   "Default perspecive",
            "tooltip": "QObject tree view",
            "icon":    "",
            "model":   [TreeQObjectInfoModel],
        },
    }

    DftPerspective = "Default"

    def __init__(self, parent=None, with_navigation_bar=True,
                 with_filter_widget=True, perspective=None, proxy=None,
                 qobject=None):
        BaseTreeWidget.__init__(self, parent,
                                with_navigation_bar=with_navigation_bar,
                                with_filter_widget=with_filter_widget,
                                perspective=perspective, proxy=proxy)
        qmodel = self.getQModel()
        #getQObjectTree(qobject=qobject)
        qmodel.setDataSource(qobject)


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
    app = getApplication()

    w = buildGUI()
    w.show()
    inspector = TreeQObjectWidget(qobject=w)
    inspector.setAttribute(QtCore.Qt.WA_QuitOnClose, False)
    inspector.show()
    app.exec_()

if __name__ == "__main__":
    main()
