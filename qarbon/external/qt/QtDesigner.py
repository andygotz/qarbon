# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
#
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""This module exposes QtDesigner module"""

from qarbon.external.qt import getQt

__backend = getQt().__name__

if __backend == 'PyQt4':
    from PyQt4.QtDesigner import *
elif __backend == 'PyQt5':
    from PyQt5.QtDesigner import *
elif __backend == 'PySide':
    from PySide.QtDesigner import *

del getQt
