#------------------------------------------------------------------------------
# This file is part of Framework4, a graphical toolkit to build beamline
# applications
#
# http://forge.epn-campus.eu/projects/framework4
#
# Copyright 2013
#           European Synchrotron Radiation Facility,
#           BP 220, Grenoble 38043, FRANCE
#
# Framework4 is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Framework is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Framework.  If not, see <http://www.gnu.org/licenses/>.
#------------------------------------------------------------------------------

from qarbon.meta import State

# color        R     G     B     A
black = 0x00, 0x00, 0x00, 0xFF
white = 0xFF, 0xFF, 0xFF, 0xFF

gray = 0x7F, 0x7F, 0x7F, 0xFF
darkgray = 0x40, 0x40, 0x40, 0xFF
lightgray = 0xC0, 0xC0, 0xC0, 0xFF

red = 0xFF, 0x00, 0x00, 0xFF
darkred = 0x7F, 0x00, 0x00, 0xFF
lightred = 0xFF, 0x7F, 0x7F, 0xFF

green = 0x00, 0x80, 0x00, 0xFF
mediumgreen = 0x24, 0x62, 0x24, 0xFF
darkgreen = 0x25, 0x41, 0x17, 0xFF
lightgreen = 0x4A, 0xA0, 0x2C, 0xFF

blue = 0x00, 0x00, 0xFF, 0xFF
darkblue = 0x00, 0x00, 0xA0, 0xFF
lightblue = 0xAD, 0xD8, 0xE6, 0xFF
cyan = 0x00, 0xFF, 0xFF, 0xFF

yellow = 0xFF, 0xFF, 0x00, 0xFF
magenta = 0xFF, 0x00, 0xFF, 0xFF
purple = 0x80, 0x00, 0x80, 0xFF
orange = 0xFF, 0x8C, 0x00, 0xFF


_grenoble = 0xCC, 0xCC, 0x7A, 0xFF

__STATE_COLOR_MAP = {
#    state               background Foreground
    State.On:            (green, white),
    State.Off:           (white, black),
    State.Close:         (white, green),
    State.Open:          (mediumgreen, white),
    State.Insert:        (white, black),
    State.Extract:       (mediumgreen, white),
    State.Moving:        (blue, white),
    State.Standby:       (yellow, black),
    State.Fault:         (red, white),
    State.Init:          (_grenoble, black),
    State.Running:       (lightblue, black),
    State.Alarm:         (orange, white),
    State.Disable:       (magenta, black),
    State.Unknown:       (lightgray, black),
    State.Disconnected:  (gray, white),
    State._Invalid:      (darkgray, white),
    None:                (darkgray, white),  # None == _Invalid
}


def get_state_color_map():
    return __STATE_COLOR_MAP


def get_color_from_state(state):
    return get_state_color_map()[state]


def get_css_color_from_state(state):
    bg, fg = get_color_from_state(state)
    return "background-color: rgba{0}; color: rgba{1};".format(bg, fg)


def get_bg_color_from_state(state):
    return get_color_from_state(state)[0]


def get_fg_color_from_state(state):
    return get_color_from_state(state)[1]

__all__ = ["get_state_color_map", "get_color_from_state",
           "get_css_color_from_state",
           "get_bg_color_from_state", "get_fg_color_from_state"]
