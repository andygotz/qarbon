# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
#
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""Helper functions to manage QApplication.

Most common use case::


    from qarbon.external.qt import QtGui
    from qarbon.qt.gui.application import Application

    app = Application()
    label = QtGui.QLabel("Hello, world!")
    label.show()
    app.exec_()

The advantage here is you can call :func:`Application` anywhere on your
program.
"""

__all__ = ["Application"]

import logging

from qarbon.external.qt import QtGui


def getApplication(argv=None, **properties):
    """Returns a QApplication.

    If the process has initialized before a QApplication it returns the
    existing instance, otherwise it creates a new one.

    When a QApplication is created it takes argv into account. If argv is
    None (default), it take arguments from :attr:`sys.argv`.

    If argv is given and a QApplication already exists, argv will have no
    effect.

    This is function as the same effect as :func:`Application`. Please use
    :func:`Application` instead.

    Example::

        from qarbon.external.qt import QtGui
        from qarbon.qt.gui.application import getApplication

        app = getApplication()
        label = QtGui.QLabel("Hello, world!")
        label.show()
        app.exec_()

    :param argv: optional arguments to QApplication. If the QApplication is
                 already initialized, argv will have no effect
    :param properties: currently unused
    :return: the QApplication
    :rtype: QtGui.QApplication"""

    app = QtGui.QApplication.instance()
    if app is None:
        if argv is None:
            from sys import argv
        app = QtGui.QApplication(argv)
    elif argv:
        logging.info("QApplication already initialized. argv will have no "
                     "effect")
    return app


def Application(argv=None, **properties):
    """Returns a QApplication.

    If the process has initialized before a QApplication it returns the
    existing instance, otherwise it creates a new one.

    When a QApplication is created it takes argv into account. If argv is
    None (default), it take arguments from :attr:`sys.argv`.

    If argv is given and a QApplication already exists, argv will have no
    effect.

    :param argv: optional arguments to QApplication. If the QApplication is
                 already initialized, argv will have no effect.

    Example::

        from qarbon.external.qt import QtGui
        from qarbon.qt.gui.application import Application

        app = Application()
        label = QtGui.QLabel("Hello, world!")
        label.show()
        app.exec_()

    :param properties: currently unused
    :return: the QApplication
    :rtype: QtGui.QApplication"""

    return getApplication(argv=argv, **properties)
