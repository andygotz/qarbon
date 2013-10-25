# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
#
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

from qarbon.test.base import QarbonBaseTest
from qarbon.external.qt import QtGui
from qarbon.qt.gui.icon import getThemeIcon, getStandardIcon, getIcon


class TestIcon(QarbonBaseTest):

    def test_getThemeIcon(self):
        icon = getThemeIcon("folder-open")
        self.assert_(not icon.isNull(), "Got a null icon!")

        icon = getThemeIcon("non existing icon")
        self.assert_(icon.isNull(), "Got a non null icon!")

    def test_getStandardIcon(self):
        icon = getStandardIcon(QtGui.QStyle.SP_MessageBoxWarning)
        self.assert_(not icon.isNull(), "Got a null icon!")

    def test_getIcon(self):
        icon = getIcon("folder-open")
        self.assert_(not icon.isNull(), "Got a null icon!")

        icon = getIcon(":/controls/collapse.png")
        self.assert_(not icon.isNull(), "Got a null icon!")

        icon = getIcon(QtGui.QStyle.SP_MessageBoxWarning)
        self.assert_(not icon.isNull(), "Got a null icon!")
