# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
# ----------------------------------------------------------------------------
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""This module exposes PyQt4/PyQt5/PySide module"""

__all__ = ['BackendName', 'Backend']

import os
import imp
import sys
import logging

from qarbon.util import moduleImport

BackendName = ""
Backend = None

__PREFERED_QT_API = 'PyQt4'


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
    QtCore = moduleImport(BackendName + ".QtCore")
    QT_LEVEL_MATCHER = {
        QtCore.QtDebugMsg:     "debug",
        QtCore.QtWarningMsg:   "warning",
        QtCore.QtCriticalMsg:  "critical",
        QtCore.QtFatalMsg:     "fatal",
        QtCore.QtSystemMsg:    "critical",
    }

    def qarbonMsgHandler(msg_type, msg):
        fname = QT_LEVEL_MATCHER.get(msg_type)
        f = getattr(logging, fname)
        return f("Qt: " + msg)

    QtCore.qInstallMsgHandler(qarbonMsgHandler)


def __initialize_resources():
    import qarbon.config
    qarbon_dir = os.path.dirname(os.path.abspath(qarbon.__file__))
    resource = os.path.join(qarbon_dir, 'resource', 'icons')

    QtCore = moduleImport(BackendName + ".QtCore")
    if os.path.isdir(resource):
        search_path = QtCore.QDir.searchPaths(qarbon.config.NAMESPACE)
        if resource not in search_path:
            QtCore.QDir.addSearchPath(qarbon.config.NAMESPACE, resource)


#------------------------------------------------------------------------------
# PyQt4
#------------------------------------------------------------------------------

def __set_pyqt4_api(element, api_version=2):
    import sip
    try:
        ver = sip.getapi(element)
    except ValueError:
        ver = -1

    if ver < 0:
        try:
            sip.setapi(element, api_version)
            logging.debug("%s API set to version %d",
                          element, sip.getapi("QString"))
        except ValueError:
            logging.warning("Error setting %s API to version %s", element,
                            api_version, exc_info=1)
            return False
    elif ver < api_version:
        logging.info("%s API set to version %s (advised: version >= %s)",
                     element, ver, api_version)
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
        logging.warning("Using old sip %s (advised >= 4.9)", sip_ver)
    else:
        __set_pyqt4_api("QString", 2)
        __set_pyqt4_api("QVariant", 2)

    import PyQt4
    return True, PyQt4


#------------------------------------------------------------------------------
# PyQt4
#------------------------------------------------------------------------------

def __prepare_pyqt5():
    import PyQt5
    return True, PyQt5


#------------------------------------------------------------------------------
# PySide
#------------------------------------------------------------------------------

def __prepare_pyside():
    import PySide
    return True, PySide


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
        logging.error("unknown Qt API '%s'", gui_backend)
        return

    mod_name, prepare_func = __KNOWN_QT_APIS[gui_backend]

    result, module = prepare_func()
    if result:
        logging.info("Successfully initialized %s", mod_name)
    else:
        logging.error("%s requested, but not installed", mod_name)
    return mod_name, module

# ugly code that has to be exeuted at import level

BackendName, Backend = __prepare()

__initialize_logging()
__initialize_resources()
