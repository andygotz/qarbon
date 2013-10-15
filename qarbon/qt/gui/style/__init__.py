# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
# ----------------------------------------------------------------------------
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""Helper classes to manage Qt styles and stylesheets"""

from qarbon.qt.gui.application import getApplication


def getStyle():
    """Returns the current active application style

    :return: the current active application style
    :rtype: QtGui.QStyle"""
    return getApplication().style()
