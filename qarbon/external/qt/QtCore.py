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

"""This module exposes QtCore module"""

from qarbon.external.qt import backend as __backend

if __backend == 'PyQt4':
    from PyQt4 import QtCore as __QtCore

    # Alias PyQt-specific functions for PySide compatibility.
    if hasattr(__QtCore, "pyqtSignal"):
        Signal = __QtCore.pyqtSignal
    if hasattr(__QtCore, "pyqtSlot"):
        Slot = __QtCore.pyqtSlot
    if hasattr(__QtCore, "pyqtProperty"):
        Property = __QtCore.pyqtProperty
    __api_version__ = __QtCore.QT_VERSION_STR

    __QtCore.pyqtRemoveInputHook()

    from PyQt4.QtCore import *

elif __backend == 'PyQt5':
    from PyQt5 import QtCore as __QtCore

    # Alias PyQt-specific functions for PySide compatibility.
    if hasattr(__QtCore, "pyqtSignal"):
        Signal = __QtCore.pyqtSignal
    if hasattr(__QtCore, "pyqtSlot"):
        Slot = __QtCore.pyqtSlot
    if hasattr(__QtCore, "pyqtProperty"):
        Property = __QtCore.pyqtProperty
    __api_version__ = __QtCore.QT_VERSION_STR

    __QtCore.pyqtRemoveInputHook()

    from PyQt5.QtCore import *

elif __backend == 'PySide':
    from PySide import QtCore as __QtCore
    from PySide.QtCore import *
    __api_version__ = __QtCore.QT_VERSION_STR
