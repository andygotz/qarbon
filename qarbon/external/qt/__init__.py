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

"""This module exposes PyQt4/PyQt5/PySide module"""

import os
import imp
import sys
import logging


backend = ""

__PREFERED_QT_API = 'PyQt4'

__logger = logging.getLogger('Qt')


def __get_gui_backend():
    modules = sys.modules
    if 'PySide' in modules:
        api = 'PySide'
    elif 'PyQt5' in modules:
        api = 'PyQt5'
    elif 'PyQt4' in modules:
        api = 'PyQt4'
    else:
        api = os.environ.get("QT_API", __PREFERED_QT_API)
    return api


def __initialize_logging():
    from qarbon.external.qt import QtCore
    QT_LEVEL_MATCHER = {
        QtCore.QtDebugMsg:     "debug",
        QtCore.QtWarningMsg:   "warning",
        QtCore.QtCriticalMsg:  "critical",
        QtCore.QtFatalMsg:     "fatal",
        QtCore.QtSystemMsg:    "critical",
    }

    def qarbonMsgHandler(msg_type, msg):
        fname = QT_LEVEL_MATCHER.get(msg_type)
        f = getattr(__logger, fname)
        return f(msg)

    QtCore.qInstallMsgHandler(qarbonMsgHandler)


def __initialize_resources():
    import qarbon
    qarbon_dir = os.path.dirname(os.path.abspath(qarbon.__file__))
    resource = os.path.join(qarbon_dir, 'resource')

    from qarbon.external.qt import QtCore
    if os.path.isdir(resource):
        search_path = QtCore.QDir.searchPaths(qarbon.NAMESPACE)
        if resource not in search_path:
            QtCore.QDir.addSearchPath(qarbon.NAMESPACE, resource)


#------------------------------------------------------------------------------
# PyQt4
#------------------------------------------------------------------------------

def __set_pyqt4_api(element, api_version=2):
    import sip
    try:
        ver = sip.getapi(element)
    except ValueError:
        ver = 0

    if ver < api_version:
        try:
            sip.setapi(element, api_version)
            __logger.debug("%s API set to level %d",
                           element, sip.getapi("QString"))
        except ValueError:
            __logger.warning("Error setting %s API to %d", element,
                             api_version, exc_info=1)
            return False
    return True


def __prepare_pyqt4():

    # In python 3 both QString and QVariant API are set to level 2 so
    # nothing to do
    if sys.version_info[0] > 2:
        return

    # For PySide compatibility, use the new-style string API that
    # automatically converts QStrings to Unicode Python strings. Also,
    # automatically unpack QVariants to their underlying objects.
    import sip

    if sip.SIP_VERSION < 0x040900:
        sip_ver = sip.SIP_VERSION_STR
        __logger.warning("Using old sip %s (advised >= 4.9)", sip_ver)
    else:
        __set_pyqt4_api("QString", 2)
        __set_pyqt4_api("QVariant", 2)

    return True


#------------------------------------------------------------------------------
# PyQt4
#------------------------------------------------------------------------------

def __prepare_pyqt5():
    return True


#------------------------------------------------------------------------------
# PySide
#------------------------------------------------------------------------------

def __prepare_pyside():
    return True


#------------------------------------------------------------------------------
# prepare functions
#------------------------------------------------------------------------------

__KNOWN_QT_APIS = dict(
    pyqt4=('PyQt4', __prepare_pyqt4,),
    pyqt5=('PyQt5', __prepare_pyqt5,),
    pyside=('PySide', __prepare_pyside,),
)


def __prepare():
    gui_backend = __get_gui_backend().lower()

    if not gui_backend in __KNOWN_QT_APIS:
        __logger.error("unknown Qt API '%s'", gui_backend)
        return

    mod_name, prepare_func = __KNOWN_QT_APIS[gui_backend]

    ret = prepare_func()
    if ret:
        __logger.info("Successfully initialized %s", mod_name)
    else:
        __logger.error("%s requested, but not installed", mod_name)
    return mod_name

# ugly code that has to be exeuted at import level

backend = __prepare()

__initialize_logging()
__initialize_resources()

del __prepare_pyqt4, __prepare_pyqt5, __prepare_pyside
del __prepare
del __get_gui_backend
del logging
del sys
del imp
del os

__all__ = [
    'backend'
]
