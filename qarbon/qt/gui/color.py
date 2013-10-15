# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
# ----------------------------------------------------------------------------
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""Helper functions to colors from state"""

__all__ = ["getQColorFromState",
           "getBgQColorFromState", "getFgQColorFromState"]

from qarbon.external.qt import QtGui
from qarbon.color import getStateColorMap

__QSTATE_COLOR_MAP = None


def __getQstateColorMap():
    global __QSTATE_COLOR_MAP
    if __QSTATE_COLOR_MAP is None:
        __QSTATE_COLOR_MAP = {}
        for k, (bg, fg) in getStateColorMap().items():
            __QSTATE_COLOR_MAP[k] = QtGui.QColor(*bg), QtGui.QColor(*fg)
    return __QSTATE_COLOR_MAP


def getQColorFromState(state):
    return __getQstateColorMap()[state]


def getBgQColorFromState(state):
    return getQColorFromState()[0]


def getFgQColorFromState(state):
    return getQColorFromState()[1]
