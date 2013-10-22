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

__all__ = ["initialize", "getQtName", "getQt"]

import os
import imp
import sys
import logging
import warnings

try:
    import sip
except ImportError:
    sip = None

import qarbon.config

__QT = None
__QT_NAME = None
__QT_KNOWN_APIS = "PyQt4", "PyQt5", "PySide"
__QT_LOG_INIT = False
__QT_RES_INIT = False


def __assertQt(name, qt=None, strict=True):
    qt = qt or __QT
    if name is None or qt is None:
        return
    qt_name = qt.__name__
    if qt_name != name:
        msg = "Cannot use %s because %s already in use" % (name, qt_name)
        if strict:
            raise Exception(msg)
        else:
            warnings.warn(msg)


def __import(name):
    __import__(name)
    return sys.modules[name]


def __importQt(name):
    return __import(getQtName() + "." + name)


def __initialize_logging():
    QtCore = __importQt("QtCore")
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
    qarbon_dir = os.path.dirname(os.path.abspath(qarbon.__file__))
    resource = os.path.join(qarbon_dir, "resource", "icons")

    QtCore = __importQt("QtCore")
    if os.path.isdir(resource):
        search_path = QtCore.QDir.searchPaths(qarbon.config.NAMESPACE)
        if search_path is None or resource not in search_path:
            QtCore.QDir.addSearchPath(qarbon.config.NAMESPACE, resource)


#------------------------------------------------------------------------------
# PyQt4
#------------------------------------------------------------------------------

def __setPyQt4API(element, api_version=2):
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


def __preparePyQt4():

    # In python 3 both QString and QVariant API are set to level 2 so
    # nothing to do
    if sys.version_info[0] > 2:
        return __import("PyQt4")

    # For PySide compatibility, use the new-style string API that
    # automatically converts QStrings to Unicode Python strings. Also,
    # automatically unpack QVariants to their underlying objects.
    if sip is None:
        logging.warning("Could not find sip")
    elif sip.SIP_VERSION < 0x040900:
        sip_ver = sip.SIP_VERSION_STR
        logging.warning("Using old sip %s (advised >= 4.9)", sip_ver)
    else:
        __setPyQt4API("QString", 2)
        __setPyQt4API("QVariant", 2)

    return __import("PyQt4")


#------------------------------------------------------------------------------
# PyQt4
#------------------------------------------------------------------------------

def __preparePyQt5():
    return __import("PyQt5")


#------------------------------------------------------------------------------
# PySide
#------------------------------------------------------------------------------

def __preparePySide():
    return __import("PySide")


def getQt(name=None, strict=True):
    global __QT, __QT_NAME
    if __QT:
        __assertQt(name, qt=__QT, strict=strict)
        return __QT

    modules = sys.modules
    for api_name in __QT_KNOWN_APIS:
        api = modules.get(api_name)
        if api:
            __assertQt(name, qt=api, strict=strict)
            __QT = api
            __QT_NAME = name
            return __QT

    # no qt imported yet
    if strict and name:
        apis = [name]
    else:
        apis = list(__QT_KNOWN_APIS)
        if name:
            apis.remove(name)
            apis.insert(0, name)
    for api_name in apis:
        f = globals()["__prepare" + api_name]
        try:
            __QT = f()
            __QT_NAME = api_name
            return __QT
        except ImportError:
            continue
    raise ImportError("No suitable Qt found")


def getQtName(name=None, strict=True):
    # force initialization of Qt
    getQt(name=name, strict=strict)
    return __QT_NAME


def initialize(name=None, strict=True, logging=True,
               resources=True, remove_inputhook=True):
    qt = getQt(name=name, strict=strict)
    if logging:
        __initialize_logging()
    if resources:
        __initialize_resources()

    return qt


if qarbon.config.QT_AUTO_INIT:
    initialize(name=qarbon.config.QT_AUTO_API,
               strict=qarbon.config.QT_AUTO_STRICT,
               logging=qarbon.config.QT_AUTO_INIT_LOG,
               resources=qarbon.config.QT_AUTO_INIT_RES,
               remove_inputhook=qarbon.config.QT_AUTO_REMOVE_INPUTHOOK)
