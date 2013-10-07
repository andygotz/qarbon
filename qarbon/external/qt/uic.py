#!/usr/bin/env python
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

"""This module exposes PyQt4/PSide uic module"""

from qarbon.external.qt import backend as __backend

if __backend == 'PyQt4':
    from PyQt4.uic import *
    from PyQt4.uic import uiparser
    from PyQt4.uic import properties

    # prevent ui parser from logging debug messages
    class __IgnoreCalls:
        def __call__(self, *args, **kwargs):
            pass

    uiparser.DEBUG = __IgnoreCalls()
    properties.DEBUG = __IgnoreCalls()

    def loadUI(uiFilename, parent=None):
        newWidget = loadUi(uiFilename)
        newWidget.setParent(parent)
        return newWidget

elif __backend == 'PyQt5':
    from PyQt5.uic import *
    from PyQt5.uic import uiparser
    from PyQt5.uic import properties

    # prevent ui parser from logging debug messages
    class __IgnoreCalls:
        def __call__(self, *args, **kwargs):
            pass

    uiparser.DEBUG = __IgnoreCalls()
    properties.DEBUG = __IgnoreCalls()

    def loadUI(uiFilename, parent=None):
        newWidget = loadUi(uiFilename)
        newWidget.setParent(parent)
        return newWidget

elif __backend == 'PySide':
    _uiLoader = None
    import logging
    __logger = logging.getLogger('Qt')
    from PySide import QtCore as __QtCore
    from PySide import QtUiTools as __QtUiTools

    class UiLoader(__QtUiTools.QUiLoader):
        def __init__(self):
            super(UiLoader, self).__init__()
            self._rootWidget = None

        def createWidget(self, className, parent=None, name=''):
            widget = super(UiLoader, self).createWidget(
                    className, parent, name)

            if name:
                if self._rootWidget is None:
                    self._rootWidget = widget
                elif not hasattr(self._rootWidget, name):
                    setattr(self._rootWidget, name, widget)
                else:
                    __logger.error("Name collision! Ignoring second "
                                   "occurrance of %r.", name)

                if parent is not None:
                    setattr(parent, name, widget)
                else:
                    # Sadly, we can't reparent it to self, since QUiLoader
                    # isn't a QWidget.
                    __logger.error("No parent specified! This will probably "
                                   "crash due to C++ object deletion.")

            return widget

        def load(self, fileOrName, parentWidget=None):
            if self._rootWidget is not None:
                raise Exception("UiLoader is already started loading UI!")

            widget = super(UiLoader, self).load(fileOrName, parentWidget)

            if widget != self._rootWidget:
                __logger.error("Returned widget isn't the root widget... ")

            self._rootWidget = None
            return widget

    def loadUI(uiFilename, parent=None):
        global _uiLoader
        if _uiLoader is None:
            _uiLoader = UiLoader()

        uiFile = __QtCore.QFile(uiFilename, parent)
        if not uiFile.open(__QtCore.QIODevice.ReadOnly):
            __logger.error("Couldn't open file %r!", uiFilename)
            return None

        try:
            return _uiLoader.load(uiFile, parent)

        except:
            __logger.exception("Exception loading UI from %r!", uiFilename)

        finally:
            uiFile.close()
            uiFile.deleteLater()

        return None
