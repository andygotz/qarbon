# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
# ----------------------------------------------------------------------------
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""Helper functions to access QAction"""

__all__ = ["getAction"]

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
