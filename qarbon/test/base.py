# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
# ----------------------------------------------------------------------------
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

from unittest import TestCase

from qarbon.external.qt import QtGui

__Application = None


def _getApplication():
    global __Application
    if __Application is None:
        __Application = QtGui.QApplication([])
    return __Application


class QarbonBaseTest(TestCase):

    def setUp(self):
        self.app = _getApplication()

    def tearDown(self):
        pass
