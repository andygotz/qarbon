# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
# ----------------------------------------------------------------------------
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""Helper functions to deal with Qt GUI related stuff"""

import inspect

from qarbon.util import moduleImport
from qarbon.external.qt import QtGui


def isWidget(symbol):
    return inspect.isclass(symbol) and issubclass(symbol, QtGui.QWidget)


def getWidgets(module_name):
    widgets = {}
    module = moduleImport(module_name)

    for name, value in inspect.getmembers(module, isWidget):
        if inspect.getmodule(value) != module:
            continue
        full_name = module_name + "." + name
        widgets[full_name] = dict(klass=value, name=name, full_name=full_name)
    return widgets
