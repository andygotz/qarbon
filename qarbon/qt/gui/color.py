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

"""helper functions to colors from state"""

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
