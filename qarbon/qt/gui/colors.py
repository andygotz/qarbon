##############################################################################
##
## This file is part of Framework4, a graphical toolkit to build beamline
## applications
##
## http://forge.epn-campus.eu/projects/framework4
##
## Copyright 2013
##           European Synchrotron Radiation Facility,
##           BP 220, Grenoble 38043
##           FRANCE
##
## Framework4 is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## Framework is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with Framework.  If not, see <http://www.gnu.org/licenses/>.
##
##############################################################################

from qarbon.external.qt import QtGui
from qarbon.colors import get_state_color_map

__QSTATE_COLOR_MAP = None


def _get_qstate_color_map():
    global __QSTATE_COLOR_MAP
    if __QSTATE_COLOR_MAP is None:
        __QSTATE_COLOR_MAP = {}
        for k, (bg, fg) in get_state_color_map().items():
            __QSTATE_COLOR_MAP[k] = QtGui.QColor(*bg), QtGui.QColor(*fg)
    return __QSTATE_COLOR_MAP


def get_qcolor_from_state(state):
    return _get_qstate_color_map()[state]


def get_bg_qcolor_from_state(state):
    return get_qcolor_from_state()[0]


def get_fg_qcolor_from_state(state):
    return get_qcolor_from_state()[1]


__all__ = ["get_qcolor_from_state",
           "get_bg_qcolor_from_state", "get_fg_qcolor_from_state"]
