# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
#
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""This module exposes QtCore module"""

from qarbon.external.qt import getQt

__backend = getQt().__name__

def __to_qvariant_1(pyobj=None):
    """Properly converts a python object into a proper QVariant according to
    the PySide or PyQt API version in use

    :param pyobj: object to be converted
    :return: A proper QVariant"""
    from PyQt4.QtCore import QVariant
    if pyobj is None:
        return QVariant()  # PyQt 4.4 doesn't accept QVariant(None)
    return QVariant(pyobj)


def __from_qvariant_1(qobj=None, convfunc=None):
    """Properly converts a QVariant/QVariant equivalent to a python object
    according to the PySide or PyQt API version in use

    :param qobj: object to be converted
    :param convfunc:
        conversion function. Not used if QVariant is not available.
        If QVariant is available:  [default: None, meaning use
        qobj.toPyObject()]. Can be a function like str, int, bool, float or
        a string containing the conversion method (ex.: 'toByteArray') will
        call qobj.toByteArray()
    :return: A proper python object"""
    if convfunc is None:
        return qobj.toPyObject()
    elif callable(convfunc):
        if convfunc in (unicode, str):
            return convfunc(qobj.toString())
        elif convfunc is bool:
            return qobj.toBool()
        elif convfunc is int:
            return qobj.toInt()[0]
        elif convfunc is float:
            return qobj.toDouble()[0]
    elif isinstance(convfunc, (str, unicode)):
        return getattr(qobj, convfunc)()


def __QVariant_2(pyobj=None):
    return pyobj


def __to_qvariant_2(pyobj=None):
    """Properly converts a python object into a proper QVariant according to
    the PySide or PyQt4 API version in use

    :param pyobj: object to be converted
    :return: A proper QVariant"""
    return pyobj


def __from_qvariant_2(qobj=None, convfunc=None):
    """Properly converts a QVariant/QVariant equivalent to a python object
    according to the PySide or PyQt4 API version in use

    :param qobj: object to be converted
    :param convfunc:
        conversion function. Not used if QVariant is not available.
        If QVariant is available:  [default: None, meaning use
        qobj.toPyObject()]. Can be a function like str, int, bool, float or
        a string containing the conversion method (ex.: 'toByteArray') will
        call qobj.toByteArray()
    :return: A proper python object"""
    return qobj


__QString_2 = str

__QStringList_2 = list


if __backend == 'PyQt4':
    from PyQt4 import QtCore as __QtCore

    # Alias PyQt-specific functions for PySide compatibility.
    if hasattr(__QtCore, "pyqtSignal"):
        Signal = __QtCore.pyqtSignal
    if hasattr(__QtCore, "pyqtSlot"):
        Slot = __QtCore.pyqtSlot
    if hasattr(__QtCore, "pyqtProperty"):
        Property = __QtCore.pyqtProperty

    try:
        __api_version__ = __QtCore.QT_VERSION_STR
    except AttributeError:
        pass

    try:
        import sip
        PYQT_QVARIANT_API_1 = sip.getapi('QVariant') < 2
        PYQT_QSTRING_API_1 = sip.getapi('QString') < 2
    except (ImportError, AttributeError):
        PYQT_QVARIANT_API_1 = True
        PYQT_QSTRING_API_1 = True

    if PYQT_QVARIANT_API_1:
        to_qvariant = __to_qvariant_1
        from_qvariant = __from_qvariant_1
    else:
        __QtCore.QVariant = QVariant = __QVariant_2
        to_qvariant = __to_qvariant_2
        from_qvariant = __from_qvariant_2


    if not PYQT_QSTRING_API_1:
        __QtCore.QString = QString = __QString_2
        __QtCore.QStringList = QStringList = __QStringList_2

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

    try:
        __api_version__ = __QtCore.QT_VERSION_STR
    except AttributeError:
        pass

    __QtCore.QVariant = QVariant = __QVariant_2
    to_qvariant = __to_qvariant_2
    from_qvariant = __from_qvariant_2
    __QtCore.QString = QString = __QString_2
    __QtCore.QStringList = QStringList = __QStringList_2


    from PyQt5.QtCore import *

elif __backend == 'PySide':
    from PySide import QtCore as __QtCore
    from PySide.QtCore import *
    __api_version__ = __QtCore.QT_VERSION_STR

    __QtCore.QVariant = QVariant = __QVariant_2
    to_qvariant = __to_qvariant_2
    from_qvariant = __from_qvariant_2
    __QtCore.QString = QString = __QString_2
    __QtCore.QStringList = QStringList = __QStringList_2

del getQt
