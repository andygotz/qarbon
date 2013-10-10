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

"""Helper functions to manage QApplication"""

__all__ = ["getApplication"]

__docformat__ = 'restructuredtext'

import logging

from qarbon.external.qt import QtGui


def getApplication(args=None):
    """Returns a QApplication.
    If the process has initialized before a
    QApplication it returns this instance, otherwise it creates a new one

    :param args: optional arguments to QApplication. If the QApplication is
                 already initialized, args will have no effect
    :return: the QApplication
    :rtype: QtGui.QApplication"""

    app = QtGui.QApplication.instance()
    if app is None:
        if args is None:
            args = []
        app = QtGui.QApplication(args)
    elif args is not None:
        logging.info("QApplication already initialized. args will have "
                     "no effect")
    return app
