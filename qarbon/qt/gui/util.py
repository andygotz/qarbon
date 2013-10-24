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

__all__ = ["isWidget", "getWidgets"]

import inspect

from qarbon.util import moduleImport
from qarbon.external.qt import QtGui


def isWidget(obj):
    """Determines if the given object is a Qt Widget.

    :param obj: object
    :return: True if the given object is a Qt Widget or False otherwise
    :rtype: bool
    """
    return inspect.isclass(obj) and issubclass(obj, QtGui.QWidget)


def getWidgets(module_name):
    """Returns the widgets defined in a given module.

    :param module_name: name of the module in the format "a.b.c"
    :type module_name: str
    :return: a map with the widgets for the given module
    :rtype: dict<widget full name(str): dict<"klass": widget class(class),
            "name": widget name(str), "full_name": widget full name(str)>>
    """
    widgets = {}
    module = moduleImport(module_name)

    for name, value in inspect.getmembers(module, isWidget):
        if inspect.getmodule(value) != module:
            continue
        full_name = module_name + "." + name
        widgets[full_name] = dict(klass=value, name=name, full_name=full_name)
    return widgets
