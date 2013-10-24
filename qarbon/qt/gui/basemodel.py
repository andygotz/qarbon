# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
# ----------------------------------------------------------------------------
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""A base model and a base tree item."""

__all__ = ["BaseTreeItem", "BaseModel", "BaseProxyModel"]

from qarbon.external.qt import QtCore, QtGui


class BaseTreeItem(object):
    """A generic node"""

    DisplayFunc = str

    def __init__(self, model, data, parent=None):
        self._model = model
        self._itemData = data
        self._parentItem = parent
        self._childItems = []
        self._depth = self._calcDepth()

    def itemData(self):
        """The internal itemData object

        :return: (object) object holding the data of this item
        """
        return self._itemData

    def depth(self):
        """Depth of the node in the hierarchy

        :return: (int) the node depth
        """
        return self._depth

    def appendChild(self, child):
        """Adds a new child node

        :param child: (BaseTreeItem) child to be added
        """
        self._childItems.append(child)

    def child(self, row):
        """Returns the child in the given row

        :return: (BaseTreeItem) the child node for the given row"""
        return self._childItems[row]

    def childCount(self):
        """Returns the number of childs for this node

        :return: (int) number of childs for this node
        """
        return len(self._childItems)

    def hasChildren(self):
        return len(self._childItems) > 0

    def data(self, index):
        """Returns the data of this node for the given index

        :return: (object) the data for the given index
        """
        return self._itemData[index.column()]

    def icon(self, index):
        return None

    def toolTip(self, index):
        return self.data(index)

    def setData(self, index, data):
        """Sets the node data

        :param data: (object) the data to be associated with this node
        """
        self._itemData = data

    def parent(self):
        """Returns the parent node or None if no parent exists

        :return: (BaseTreeItem) the parent node
        """
        return self._parentItem

    def row(self):
        """Returns the row for this node

        :return: (int) row number for this node
        """
        if self._parentItem is None:
            return 0
        return self._parentItem._childItems.index(self)

    def _calcDepth(self):
        d = 0
        n = self.parent()
        while n is not None:
            n = n.parent()
            d += 1
        return d

    def display(self):
        """Returns the display string for this node

        :return: (str) the node's display string"""
        if not hasattr(self, "_display"):
            if self._itemData is None:
                return None
            self._display = self.DisplayFunc(self._itemData)
        return self._display

    def mimeData(self, index):
        return self.data(index)

    def role(self):
        """Returns the prefered role for the item.
        This implementation returns string *Unknown*

        This method should be able to return any kind of python object as long
        as the model that is used is compatible.

        :return: the role in form of element type"""
        return "Unknown"

    def __str__(self):
        return self.display()


class BaseModel(QtCore.QAbstractItemModel):
    """The base class for all Qt models."""

    ColumnNames = ()
    ColumnRoles = (),

    DftFont = QtGui.QFont("Mono", 8)

    def __init__(self, parent=None, data=None):
        QtCore.QAbstractItemModel.__init__(self, parent)
        # if qt < 4.6, beginResetModel and endResetModel don't exist. In this
        # case we set beginResetModel to be an empty function and endResetModel
        # to be reset.
        if not hasattr(QtCore.QAbstractItemModel, "beginResetModel"):
            self.beginResetModel = lambda: None
            self.endResetModel = self.reset
        self._data_src = None
        self._rootItem = None
        self._filters = []
        self._selectables = [self.ColumnRoles[0][-1]]
        self.setDataSource(data)

    def __getattr__(self, name):
        return getattr(self.dataSource(), name)

    def createNewRootItem(self):
        return BaseTreeItem(self, self.ColumnNames)

    def refresh(self, refresh_source=False):
        self.beginResetModel()
        self._rootItem = self.createNewRootItem()
        self.setupModelData(self.dataSource())
        self.endResetModel()

    def setupModelData(self, data):
        raise NotImplementedError("setupModelData must be implemented "
                                  "in %s" % self.__class__.__name__)

    def roleIcon(self, role):
        raise NotImplementedError("roleIcon must be implemented "
                                  "in %s" % self.__class__.__name__)

    def roleSize(self, role):
        raise NotImplementedError("roleSize must be implemented "
                                  "in %s" % self.__class__.__name__)

    def roleToolTip(self, role):
        raise NotImplementedError("roleToolTip must be implemented "
                                  "in %s" % self.__class__.__name__)

    def setDataSource(self, data_src):
        self._data_src = data_src
        self.refresh()

    def dataSource(self):
        return self._data_src

    def setSelectables(self, seq_elem_types):
        self._selectables = seq_elem_types

    def selectables(self):
        return self._selectables

    def role(self, column, depth=0):
        cr = self.ColumnRoles
        if column == 0:
            return cr[0][depth]
        return self.ColumnRoles[column]

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self.ColumnRoles)

    def columnIcon(self, column):
        return self.roleIcon(self.role(column))

    def columnToolTip(self, column):
        return self.roleToolTip(self.role(column))

    def columnSize(self, column):
        role = self.role(column)
        s = self.roleSize(role)
        return s

    def pyData(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None

        item = index.internalPointer()

        ret = None
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            ret = item.data(index)
#        elif role == Qt.Qt.CheckStateRole:
#            data = item.data(index)
#            if type(data) != bool:
#                data = str(data).lower() == 'true'
#            ret = Qt.Qt.Unchecked
#            if data == True:
#                ret = Qt.Qt.Checked
        elif role == QtCore.Qt.DecorationRole:
            ret = item.icon(index)
        elif role == QtCore.Qt.ToolTipRole:
            ret = item.toolTip(index)
        #elif role == Qt.Qt.SizeHintRole:
        #    ret = self.columnSize(column)
        elif role == QtCore.Qt.FontRole:
            ret = self.DftFont
        elif role == QtCore.Qt.UserRole:
            ret = item
        return ret

    def data(self, index, role=QtCore.Qt.DisplayRole):
        ret = self.pyData(index, role)
        return ret

    def _setData(self, index, pyobj, role=QtCore.Qt.EditRole):
        item = index.internalPointer()
        item.setData(index, pyobj)
        return True

    def flags(self, index):
        if not index.isValid():
            return 0

        ret = QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsDragEnabled

        item = index.internalPointer()
        column, depth = index.column(), item.depth()
        qrole = self.role(column, depth)

        if qrole in self.selectables():
            ret |= QtCore.Qt.ItemIsSelectable
        return ret

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        ret = None
        if orientation == QtCore.Qt.Horizontal:
            if role == QtCore.Qt.TextAlignmentRole:
                ret = int(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            elif role == QtCore.Qt.DisplayRole:
                ret = self.ColumnNames[section]
            elif role == QtCore.Qt.SizeHintRole:
                ret = QtCore.QSize(self.columnSize(section))
                ret.setHeight(24)
            elif role == QtCore.Qt.ToolTipRole:
                ret = self.columnToolTip(section)
            elif role == QtCore.Qt.DecorationRole:
                ret = self.columnIcon(section)

        return ret

    def index(self, row, column, parent=QtCore.QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()
        if not parent.isValid():
            parentItem = self._rootItem
        else:
            parentItem = parent.internalPointer()
        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        return QtCore.QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QtCore.QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem is None or parentItem == self._rootItem:
            return QtCore.QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parentItem = self._rootItem
        else:
            parentItem = parent.internalPointer()
        if parentItem is None:
            return 0
        return parentItem.childCount()

    def hasChildren(self, parent=QtCore.QModelIndex()):
        if parent.column() > 0:
            return 0
        if not parent.isValid():
            parentItem = self._rootItem
        else:
            parentItem = parent.internalPointer()

        if parentItem is None:
            return False
        return parentItem.hasChildren()


class BaseProxyModel(QtGui.QSortFilterProxyModel):
    """A base Qt filter & sort model"""

    def __init__(self, parent=None):
        QtGui.QSortFilterProxyModel.__init__(self, parent)

        # filter configuration
        self.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.setFilterKeyColumn(0)
        self.setFilterRole(QtCore.Qt.DisplayRole)

        # sort configuration
        self.setSortCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.setSortRole(QtCore.Qt.DisplayRole)

        # general configuration
        self.sort(0, QtCore.Qt.AscendingOrder)

    def __getattr__(self, name):
        return getattr(self.sourceModel(), name)
