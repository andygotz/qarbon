# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
# ----------------------------------------------------------------------------
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""This module exposes PyQt4/PyQt5/PySide QtUiTools module"""

from qarbon.external.qt import BackendName as __backend

if __backend == 'PySide':
    from PySide.QtUiTools import *
