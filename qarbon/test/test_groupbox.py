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
from qarbon.qt.gui.groupbox import GroupBox
from qarbon.qt.gui.icon import getIcon


class TestGroupBox(QarbonBaseTest):

    def test_groupBox(self):
        gb = GroupBox()

        gb.title = "Test box"
        self.assertEquals(gb.getTitle(), "Test box",
                          "Title was not properly set!")

        gb.titleIcon = getIcon("folder-open")
        self.assert_(not gb.getTitleIcon().isNull(), "Got a null icon!")

        gb.contentVisible = True
        self.assert_(gb.isContentVisible(), "Content is not visible!")

        gb.contentVisible = False
        self.assert_(not gb.isContentVisible(),
                     "Invisible content is visible!")

        content = gb.content()
        self.assert_(content is None, "content is not None!")

        content = QtGui.QFrame()
        gb.setContent(content)
        self.assert_(content == gb.content(),
                     "content is not the given content!")
        self.assert_(content.layout() is None, "content already has a layout!")

        size = gb.size()
        self.assert_(size.width() > 10, "width is suspiciously small!")
        self.assert_(size.height() > 10, "height is suspiciously small!")
