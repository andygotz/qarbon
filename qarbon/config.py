# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
# ----------------------------------------------------------------------------
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""Global configuration."""

#: qarbon namespace
NAMESPACE = "qarbon"

#: Auto initialize Qt
QT_AUTO_INIT = True

#: Set preffered API if not is already loaded
QT_AUTO_API = 'PyQt4'

#: Whether or not should be strict in choosing Qt API
QT_AUTO_STRICT = False

#: Auto initialize Qt logging to python logging
QT_AUTO_INIT_LOG = True

#: Auto initialize Qarbon resources (icons)
QT_AUTO_INIT_RES = True

#: Remove input hook (only valid for PyQt4)
QT_AUTO_REMOVE_INPUTHOOK = True
