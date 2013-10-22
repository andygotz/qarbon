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

from qarbon.qt.gui.application import Application


class QarbonBaseTest(TestCase):

    def setUp(self):
        self.app = Application()

    def tearDown(self):
        pass
