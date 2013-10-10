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

"""Helper functions to access QAction"""

__all__ = ["getAction"]

__docformat__ = 'restructuredtext'

from qarbon.external.qt import QtCore, QtGui
from qarbon.qt.gui.icon import getIcon


def getAction(text, parent=None, shortcut=None, icon=None, tip=None,
              toggled=None, triggered=None, data=None,
              context=QtCore.Qt.WindowShortcut):
    """Create a new QAction.

    :param text: label for the action
    :type text: str
    :param parent: parent QObject
    :type parent: QObject
    :param shortcut: optional shortcut
    :type shortcut:
    :param icon: optional icon. Can be a QIcon or a string
    :type icon: QIcon or str
    :param tip: optional tool tip
    :type tip: str
    :param toggled: optional toggled slot
    :type toggled: callable
    :param data: optional data
    :type data: object
    :param context: action context
    :type context: ShortcutContext

    :return: a customized QAction
    :rtype: QAction
    """
    action = QtGui.QAction(text, parent)
    if triggered is not None:
        action.triggered.connect(triggered)
    if toggled is not None:
        action.toggled.connect(toggled)
        action.setCheckable(True)
    action.setIcon(getIcon(icon))
    if shortcut is not None:
        action.setShortcut(shortcut)
    if tip is not None:
        action.setToolTip(tip)
        action.setStatusTip(tip)
    if data is not None:
        action.setData(data)
    #TODO: Hard-code all shortcuts and choose context=Qt.WidgetShortcut
    # (this will avoid calling shortcuts from another dockwidget
    #  since the context thing doesn't work quite well with these widgets)
    action.setShortcutContext(context)
    return action
