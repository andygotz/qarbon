# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
#
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""Helper functions to access QAction.

Example::

    from qarbon.external.qt import QtGui
    from qarbon.qt.gui.application import Application
    from qarbon.qt.gui.action import Action
    from qarbon.qt.gui.icon import Icon
    
    def onImageFileOpen():
        fileName = QtGui.QFileDialog.getOpenFileName(None,
            "Open Image", "/home/homer",
            "Image Files (*.png *.jpg *.bmp)")
        print (fileName)

    app = Application()
    window = QtGui.QMainWindow()
    openImageAction = Action("Open &image...", parent=window,
                             icon=Icon("folder-open"),
                             shortcut=QtGui.QKeySequence.Open,
                             tooltip="open an existing image file",
                             triggered=onImageFileOpen)

    menuBar = window.menuBar()
    fileMenu = menuBar.addMenu("&File")
    fileMenu.addAction(openImageAction)
    window.show()
    app.exec_()
"""

__all__ = ["Action"]

from qarbon.external.qt import QtCore, QtGui
from qarbon.qt.gui.icon import Icon


def getAction(text, parent=None, shortcut=None, icon=None, tooltip=None,
              toggled=None, triggered=None, data=None,
              context=QtCore.Qt.WindowShortcut):
    """Create a new QAction.

    This is function as the same effect as :func:`Action`. Please use
    :func:`Action` instead.

    :param text: label for the action
    :type text: str
    :param parent: parent QObject
    :type parent: QObject
    :param shortcut: optional shortcut
    :type shortcut: QtGui.QKeySequence
    :param icon: optional icon. Can be a QIcon or a string
    :type icon: QIcon or str
    :param tooltip: optional tool tip
    :type tooltip: str
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
    action.setIcon(Icon(icon))
    if shortcut is not None:
        action.setShortcut(shortcut)
    if tooltip is not None:
        action.setToolTip(tooltip)
        action.setStatusTip(tooltip)
    if data is not None:
        action.setData(data)
    #TODO: Hard-code all shortcuts and choose context=Qt.WidgetShortcut
    # (this will avoid calling shortcuts from another dockwidget
    #  since the context thing doesn't work quite well with these widgets)
    action.setShortcutContext(context)
    return action


def Action(text, parent=None, shortcut=None, icon=None, tooltip=None,
           toggled=None, triggered=None, data=None,
           context=QtCore.Qt.WindowShortcut):
    """Create a new QAction.

    Example::

        from qarbon.external.qt import QtGui
        from qarbon.qt.gui.application import Application
        from qarbon.qt.gui.action import Action
        from qarbon.qt.gui.icon import Icon

        def onImageFileOpen():
            fileName = QtGui.QFileDialog.getOpenFileName(None,
                "Open Image", "/home/homer",
                "Image Files (*.png *.jpg *.bmp)")
            print (fileName)

        app = Application()
        window = QtGui.QMainWindow()
        openImageAction = Action("Open &image...", parent=window,
                                 icon=Icon("folder-open"),
                                 shortcut=QtGui.QKeySequence.Open,
                                 tooltip="open an existing image file",
                                 triggered=onImageFileOpen)

        menuBar = window.menuBar()
        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(openImageAction)
        window.show()
        app.exec_()

    :param text: label for the action
    :type text: str
    :param parent: parent QObject
    :type parent: QObject
    :param shortcut: optional shortcut
    :type shortcut:
    :param icon: optional icon. Can be a QIcon or a string
    :type icon: QIcon or str
    :param tooltip: optional tool tip
    :type tooltip: str
    :param toggled: optional toggled slot
    :type toggled: callable
    :param data: optional data
    :type data: object
    :param context: action context
    :type context: ShortcutContext

    :return: a customized QAction
    :rtype: QAction
    """
    return getAction(text, parent=parent, shortcut=shortcut, icon=icon,
                     tooltip=tooltip, toggled=toggled, triggered=triggered,
                     data=data, context=context)
