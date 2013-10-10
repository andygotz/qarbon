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
