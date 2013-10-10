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

"""Helper functions to handle icons and pixmaps"""

__all__ = ["getThemeIcon", "getThemePixmap",
           "getStandardIcon", "getStandardPixmap",
           "getQarbonIcon", "getQarbonPixmap",
           "getIcon", "getPixmap"]

import os

import qarbon
from qarbon.config import NAMESPACE
from qarbon.meta import State
from qarbon.util import isString
from qarbon.external.qt import QtGui
from qarbon.qt.gui.style import getStyle

__THEME_ICON_DIR = os.path.join(
                       os.path.dirname(os.path.abspath(qarbon.__file__)),
                       "resource", "icons", "theme")


def getThemeIcon(icon_name):
    """Returns a QIcon for the given theme icon name.

    Example::

        from qarbon.external.qt import QtGui
        from qarbon.qt.gui.icon import getThemeIcon

        app = QtGui.QApplication([])
        icon = getThemeIcon("folder-open")
        button = QtGui.QPushButton(icon, "Open folder")
        button.show()
        app.exec_()

    :param icon_name: icon name
    :type icon_name: str
    :return: the QIcon corresponding to the given theme name. If the theme icon
             doesn't exist it returns a Null icon
    :rtype: QtGui.QIcon
    """
    if QtGui.QIcon.hasThemeIcon(icon_name):
        return QtGui.QIcon.fromTheme(icon_name)

    icon_name = icon_name + os.path.extsep + "png"
    if os.path.isfile(os.path.join(__THEME_ICON_DIR, icon_name)):
        return QtGui.QIcon(NAMESPACE + ":/theme/" + icon_name)
    return QtGui.QIcon()


def getThemePixmap(pixmap_name, width, height=None, mode=QtGui.QIcon.Normal,
                   state=QtGui.QIcon.Off):
    """Returns a QPixmap for the given theme pixmap name.

    Example::

        from qarbon.external.qt import QtGui
        from qarbon.qt.gui.icon import getThemePixmap

        app = QtGui.QApplication([])
        pixmap = getThemePixmap("folder-open")
        label = QtGui.QLabel()
        label.setPixmap(pixmap)
        label.show()
        app.exec_()

    :param pixmap_name: pixmap name
    :type pixmap_name: str
    :param width: pixmap width
    :type width: int
    :param height: pixmap height [default: None meaning use given width]
    :type height: int
    :param mode: icon mode
    :type mode: QtGui.QIcon.Mode
    :param state: icon state
    :type state: QtGui.QIcon.State
    :return: the QPixmap corresponding to the given theme name. If the theme
             icon doesn't exist it returns a Null pixmap
    :rtype: QtGui.QPixmap
    """
    if height is None:
        height = width
    return getThemeIcon(pixmap_name).pixmap(width, height, mode, state)


def getStandardIcon(icon_id):
    """Returns a QIcon for the given icon ID (QtGui.QStyle.SP_*)

    Example::

        from qarbon.external.qt import QtGui
        from qarbon.qt.gui.icon import getStandardIcon

        app = QtGui.QApplication([])
        icon = getStandardIcon(QtGui.QStyle.SP_MessageBoxWarning)
        button = QtGui.QPushButton(icon, "Open hutch")
        button.show()
        app.exec_()

    :param icon_id: icon name
    :type icon_id: QtGui.QStyle.SP
    :return: the QIcon corresponding to the given id. If the standard ID
             doesn't exist it returns a Null icon
    :rtype: QtGui.QIcon
    """
    return getStyle().standardIcon(icon_id)


def getStandardPixmap(pixmap_id, width, height=None, mode=QtGui.QIcon.Normal,
                      state=QtGui.QIcon.Off):
    """Returns a QPixmap for the given icon ID (QtGui.QStyle.SP_*)

    Example::

        from qarbon.external.qt import QtGui
        from qarbon.qt.gui.icon import getStandardPixmap

        app = QtGui.QApplication([])
        icon = getStandardPixmap(QtGui.QStyle.SP_MessageBoxWarning)
        label = QtGui.QLabel()
        label.setPixmap(pixmap)
        label.show()
        app.exec_()

    :param pixmap_id: pixmap name
    :type pixmap_id: QtGui.QStyle.SP
    :param width: pixmap width
    :type width: int
    :param height: pixmap height [default: None meaning use given width]
    :type height: int
    :param mode: icon mode
    :type mode: QtGui.QIcon.Mode
    :param state: icon state
    :type state: QtGui.QIcon.State
    :return: the QPixmap corresponding to the given id. If the standard ID
             doesn't exist it returns a Null QPixmap
    :rtype: QtGui.QPixmap
    """
    if height is None:
        height = width
    return getStandardIcon(pixmap_id).pixmap(width, height, mode, state)


def getQarbonIcon(icon_name):
    """Returns a QIcon for the given qarbon icon name.

    Example::

        from qarbon.external.qt import QtGui
        from qarbon.qt.gui.icon import getQarbonIcon

        app = QtGui.QApplication([])
        icon = getQarbonIcon(":/controls/collapse.png")
        button = QtGui.QPushButton(icon, "Collapse")
        button.show()
        app.exec_()

    :param icon_name: icon name
    :type icon_name: str
    :return: the QIcon corresponding to the given qarbon name. If the icon
             doesn't exist it returns a Null icon
    :rtype: QtGui.QIcon
    """
    return QtGui.QIcon(NAMESPACE + icon_name)


def getQarbonPixmap(pixmap_name, width, height=None, mode=QtGui.QIcon.Normal,
                    state=QtGui.QIcon.Off):
    """Returns a QPixmap for the given pixmap name

    Example::

        from qarbon.external.qt import QtGui
        from qarbon.qt.gui.icon import getQarbonPixmap

        app = QtGui.QApplication([])
        icon = getQarbonPixmap(":/controls/collapse.png")
        label = QtGui.QLabel()
        label.setPixmap(pixmap)
        label.show()
        app.exec_()

    :param pixmap_name: pixmap name
    :type pixmap_name: str
    :param width: pixmap width
    :type width: int
    :param height: pixmap height [default: None meaning use given width]
    :type height: int
    :param mode: icon mode
    :type mode: QtGui.QIcon.Mode
    :param state: icon state
    :type state: QtGui.QIcon.State
    :return: the QPixmap corresponding to the given id. If the standard ID
             doesn't exist it returns a Null QPixmap
    :rtype: QtGui.QPixmap
    """
    if height is None:
        height = width
    return getQarbonIcon(pixmap_name).pixmap(width, height, mode, state)


def getIcon(icon):
    """Returns a QIcon for the given icon.

    Example::

        from qarbon.external.qt import QtGui
        from qarbon.qt.gui.icon import getIcon

        app = QtGui.QApplication([])
        icon = getIcon("folder-open") # == getThemeIcon("folder-open")
        icon = getIcon(":/controls/collapse.png") # == getQarbonIcon(":/controls/collapse.png")
        icon = getIcon("MyResource:/bla.png") # == Qt.QIcon("MyResource:/bla.png")
        icon = getIcon(QtGui.QStyle.SP_MessageBoxWarning) # == getStandardIcon(QtGui.QStyle.SP_MessageBoxWarning)
        button = QtGui.QPushButton(icon, "Something")
        button.show()
        app.exec_()

    :param icon: icon name or ID
    :type icon: str or int
    :return: the QIcon corresponding to the given icon. If the icon
             doesn't exist it returns a Null icon
    :rtype: QtGui.QIcon
    """
    if icon is None:
        return QtGui.QIcon()
    elif isinstance(icon, QtGui.QIcon):
        return icon
    elif isString(icon):
        if icon.startswith(":"):
            return getQarbonIcon(icon)
        elif ":" in icon:
            return QtGui.QIcon(icon)
        # TODO: distinguish between theme icon and absolute path icon
        # "folder-open" and "c:\logo.png" or "/tmp/logo.png"
        else:
            return getThemeIcon(icon)
    else:
        return getStandardIcon(icon)


def getPixmap(pixmap, width, height=None, mode=QtGui.QIcon.Normal,
              state=QtGui.QIcon.Off):
    """Returns a QPixmap for the given pixmap.

    Example::

        from qarbon.external.qt import QtGui
        from qarbon.qt.gui.icon import getIcon

        app = QtGui.QApplication([])
        icon = getIcon("folder-open") # == getThemeIcon("folder-open")
        icon = getIcon(":/controls/collapse.png") # == getQarbonIcon(":/controls/collapse.png")
        icon = getIcon("MyResource:/bla.png") # == Qt.QIcon("MyResource:/bla.png")
        icon = getIcon(QtGui.QStyle.SP_MessageBoxWarning) # == getStandardIcon(QtGui.QStyle.SP_MessageBoxWarning)
        button = QtGui.QPushButton(icon, "Something")
        button.show()
        app.exec_()

    :param pixmap: pixmap name or ID
    :type pixmap: str or int
    :param width: pixmap width
    :type width: int
    :param height: pixmap height [default: None meaning use given width]
    :type height: int
    :param mode: icon mode
    :type mode: QtGui.QIcon.Mode
    :param state: icon state
    :type state: QtGui.QIcon.State
    :return: the QPixmap corresponding to the given pixmap. If the pixmap
             doesn't exist it returns a Null QPixmap
    :rtype: QtGui.QPixmap
    """
    if height is None:
        height = width
    return getIcon(pixmap).pixmap(width, height, mode, state)


__STATE_MAP = {
    State.Alarm:   QtGui.QStyle.SP_MessageBoxWarning,
    State.Disable: QtGui.QStyle.SP_MessageBoxWarning,
    State.Fault:   QtGui.QStyle.SP_MessageBoxCritical,
    State.Unknown: QtGui.QStyle.SP_MessageBoxQuestion,
}


def getStateIcon(state):
    return __STATE_MAP.get(state, QtGui.QStyle.SP_MessageBoxInformation)
