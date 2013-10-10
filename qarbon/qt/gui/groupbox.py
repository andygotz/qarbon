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

"""A colapsable container widget with (optional) title"""

__all__ = ["GroupBox"]

__docformat__ = 'restructuredtext'

from qarbon.external.qt import QtCore, QtGui

from qarbon.qt.gui.application import getApplication
from qarbon.qt.gui.style.templates import GROUPBOX_STYLESHEET_TEMPLATE
from qarbon.qt.gui.style.nebula import GROUPBOX_NEBULA_STYLESHEET
from qarbon.qt.gui.style.nebula import GROUPBOX_NEBULA_STYLESHEET_MAP


class TitleLabel(QtGui.QLabel):
    pass


class TitleBar(QtGui.QFrame):
    pass


class ContentPanel(QtGui.QFrame):
    pass


class GroupBox(QtGui.QWidget):
    """An expandable/collapsible composite widget"""

    DefaultContentVisible = True
    DefaultTitleBarVisible = True
    DefaultTitleBarHeight = 16

    DefaultStyle = GROUPBOX_NEBULA_STYLESHEET_MAP

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self._titleVisible = self.DefaultTitleBarVisible
        self._contentVisible = self.DefaultContentVisible
        self._style = self.DefaultStyle
        self.__init()
        self.resetContentVisible()
        self.resetTitleHeight()
        self.resetTitleVisible()

    def __init(self):
        panelLayout = QtGui.QVBoxLayout()
        panelLayout.setSpacing(0)
        panelLayout.setMargin(0)
        self.setLayout(panelLayout)

        self._titleBar = titleBar = TitleBar()
        panelLayout.addWidget(titleBar, 0)

        l = QtGui.QHBoxLayout()
        l.setMargin(2)
        l.setSpacing(2)
        self._titleBar.setLayout(l)

        self._titleButton = QtGui.QToolButton()
        self._titleButton.setStyleSheet("border: 0px")
        styleOption = QtGui.QStyleOption()
        styleOption.initFrom(self._titleButton)
        style = getApplication().style()
        icon = style.standardIcon(QtGui.QStyle.SP_DesktopIcon, styleOption,
                                  self._titleButton)
        self._titleButton.setIcon(icon)
        self._titleLabel = TitleLabel()
        self._upDownButton = QtGui.QToolButton()
        self._upDownButton.setStyleSheet("border: 0px")
        self._upDownButton.clicked.connect(self.switchContentVisible)
        l.addWidget(self._titleButton, 0)
        l.addWidget(self._titleLabel, 1)
        l.addWidget(self._upDownButton, 0)

        self._content = content = ContentPanel()
        panelLayout.addWidget(content, 1)

    def _updateStyle(self):
        """Internal method that updates the style """
        style = GROUPBOX_STYLESHEET_TEMPLATE.format(**self._style)
        self.setStyleSheet(style)

    def content(self):
        """Returns the contents widget

        :return: (Qt.QFrame) the content widget"""
        return self._content

    def titleBar(self):
        """Returns the title bar widget

        :return: (Qt.QFrame) the title bar widget"""
        return self._titleBar

    def titleButton(self):
        """Returns the title button widget

        :return: (Qt.QToolButton) the title button widget"""
        return self._titleButton

    def collapseButton(self):
        """Returns the collapse button widget

        :return: (Qt.QToolButton) the collapse button widget"""
        return self._upDownButton

    def setTitle(self, title):
        """Sets this widget's title

        :param title: (str) the new widget title"""
        self._titleLabel.setText(title)
        self.setToolTip("<html>The <b>{0}</b>".format(title))

    def getTitle(self):
        """Returns this widget's title

        :return: (str) this widget's title"""
        return self._titleLabel.text()

    def setTitleIcon(self, icon):
        """Sets this widget's title icon

        :param icon: (Qt.QIcon) the new widget title icon"""
        self._titleButton.setIcon(icon)

    def getTitleIcon(self):
        """Returns this widget's title icon

        :return: (Qt.QIcon) this widget's title icon"""
        return self._titleButton.icon()

    def switchContentVisible(self):
        """Switches this widget's contents visibility"""
        self.setContentVisible(not self.isContentVisible())

    def isContentVisible(self):
        """Returns this widget's contents visibility

        :return: (bool) this widget's contents visibility"""
        return self._contentVisible

    def resetContentVisible(self):
        """Resets this widget's contents visibility"""
        self.setContentVisible(self.DefaultContentVisible)

    def setContentVisible(self, show):
        """Sets this widget's contents visibility

        :param show: (bool) the new widget contents visibility"""
        self._contentVisible = show

        if show:
            icon_name = QtGui.QStyle.SP_TitleBarShadeButton
        else:
            icon_name = QtGui.QStyle.SP_TitleBarUnshadeButton
        icon = self.style().standardIcon(icon_name)
        self._upDownButton.setIcon(icon)
        self._content.setVisible(show)
        self.adjustSize()

    def isTitleVisible(self):
        """Returns this widget's title visibility

        :return: (bool) this widget's title visibility"""
        return self._titleVisible

    def resetTitleVisible(self):
        """Resets this widget's title visibility"""
        self.setTitleVisible(self.DefaultTitleBarVisible)

    def setTitleVisible(self, show):
        """Sets this widget's title visibility

        :param icon: (bool) the new widget title visibility"""
        self._titleVisible = show
        self._titleBar.setVisible(show)

    def getTitleHeight(self):
        """Returns this widget's title height

        :return: (bool) this widget's title height"""
        return self.titleButton().iconSize().height()

    def setTitleHeight(self, h):
        """Sets this widget's title height

        :param icon: (bool) the new widget title height"""
        s = QtCore.QSize(h, h)
        self.titleButton().setIconSize(s)
        self.collapseButton().setIconSize(s)

    def resetTitleHeight(self):
        """Resets this widget's title height"""
        self.setTitleHeight(self.DefaultTitleBarHeight)

    def getStyleMap(self):
        """Returns this widget's style

        :return: (dict) this widget's style"""
        return self._titleBarStyle

    def setStyleMap(self, style_map):
        """Sets this widget's title style
        Used key/values for style_map:

            - 'title_start_color'  : brush (Ex.: '#E0E0E0')
            - 'title_stop_color'   : brush (Ex.: '#E0E0E0')
            - 'title_font_color'   : brush (Ex.: '#E0E0E0')
            - 'title_border_radius': radius (Ex.: '5px')
            - 'content_start_color'  : brush (Ex.: '#E0E0E0')
            - 'content_stop_color'   : brush (Ex.: '#E0E0E0')
            - 'content_border_radius': radius (Ex.: '5px')

        :param style_map: (dict) the new widget title style"""
        style = self.DefaultStyle.copy()
        style.update(style_map)
        self._style = style
        self._updateStyle()

    def resetStyleMap(self):
        """Resets this widget's title style"""
        self.setStyleMap({})

    #: This property contains the widget's title
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`qarbon.gt.gui.groupbox.getTitle`
    #:     * :meth:`qarbon.gt.gui.groupbox.setTitle`
    title = QtCore.Property(str, getTitle, setTitle)

    #: This property contains the widget's title icon
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`qarbon.gt.gui.groupbox.getTitleIcon`
    #:     * :meth:`qarbon.gt.gui.groupbox.setTitleIcon`
    titleIcon = QtCore.Property("QIcon", getTitleIcon, setTitleIcon)

    #: This property contains the widget's title height
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`qarbon.gt.gui.groupbox.getTitleHeight`
    #:     * :meth:`qarbon.gt.gui.groupbox.setTitleHeight`
    #:     * :meth:`qarbon.gt.gui.groupbox.resetTitleHeight`
    titleHeight = QtCore.Property(int, getTitleHeight, setTitleHeight,
                                  resetTitleHeight)

    #: This property contains the widget's title visibility
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`qarbon.gt.gui.groupbox.isTitleVisible`
    #:     * :meth:`qarbon.gt.gui.groupbox.setTitleVisible`
    titleVisible = QtCore.Property(bool, isTitleVisible, setTitleVisible)

    #: This property contains the widget's style map
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`qarbon.gt.gui.groupbox.getStyleMap`
    #:     * :meth:`qarbon.gt.gui.groupbox.setStyleMap`
    #:     * :meth:`qarbon.gt.gui.groupbox.resetStyleMap`
    styleMap = QtCore.Property(dict, getStyleMap, setStyleMap, resetStyleMap)

    #: This property contains the widget's content's visibility
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`qarbon.gt.gui.groupbox.isContentVisible`
    #:     * :meth:`qarbon.gt.gui.groupbox.setContentVisible`
    #:     * :meth:`qarbon.gt.gui.groupbox.resetContentVisible`
    contentVisible = QtCore.Property(bool, isContentVisible,
                                     setContentVisible, resetContentVisible)


def demo():
    "QGroup Widget"

    from qarbon.qt.gui.icon import getIcon
    w = QtGui.QWidget()
    l = QtGui.QVBoxLayout()
    w.setLayout(l)

    panel = GroupBox()
    panel.title = "Database"
    contentLayout = QtGui.QFormLayout()
    panel.content().setLayout(contentLayout)
    contentLayout.addRow("&Host", QtGui.QLineEdit())
    contentLayout.addRow("&Port", QtGui.QLineEdit())
    l.addWidget(panel, 0)

    panel = GroupBox()
    panel.title = "Hello world"
    panel.titleIcon = getIcon("video-x-generic")
    panel.styleMap = {
        'title_start_color':     'rgb(255, 60, 60)',
        'title_stop_color':      'rgb(200, 0, 0)',
        'title_font_color':      'rgb(140, 0, 0)',
        'title_border_radius':   '10px',
        'content_border_radius': '0px',
    }

    contentLayout = QtGui.QFormLayout()
    panel.content().setLayout(contentLayout)
    contentLayout.addRow("State", QtGui.QPushButton("Press here"))
    contentLayout.addRow("Status", QtGui.QLineEdit())
    contentLayout.addRow("Coment", QtGui.QLineEdit())
    contentLayout.addRow("Build", QtGui.QCheckBox())
    contentLayout.addRow("Upper limit", QtGui.QSpinBox())
    contentLayout.addRow("Lower limit", QtGui.QSpinBox())
    l.addWidget(panel, 0)

    panel = GroupBox()
    panel.title = "Hello world 2"
    panel.titleIcon = getIcon("network-server")
    panel.titleVisible = False
    contentLayout = QtGui.QFormLayout()
    panel.content().setLayout(contentLayout)
    contentLayout.addRow("Something", QtGui.QLineEdit())
    contentLayout.addRow("More", QtGui.QLineEdit())
    l.addWidget(panel, 0)

    panel = GroupBox()
    panel.title = "5"
    panel.titleIcon = getIcon("folder")
    contentLayout = QtGui.QVBoxLayout()
    panel.content().setLayout(contentLayout)
    panel2 = GroupBox()
    panel2.title = "5.1"
    panel2.titleIcon = getIcon("folder")
    panel2.titleHeight = 48
    contentLayout2 = QtGui.QFormLayout()
    panel2.content().setLayout(contentLayout2)
    contentLayout2.addRow("Something", QtGui.QLineEdit())
    contentLayout2.addRow("More", QtGui.QLineEdit())
    contentLayout.addWidget(panel2, 0)
    l.addWidget(panel, 0)

    l.addStretch(1)

    w.show()
    w.adjustSize()
    return w


def main():
    app = getApplication()
    app.setStyleSheet(GROUPBOX_NEBULA_STYLESHEET)

    w = demo()
    w.show()
    app.exec_()

if __name__ == '__main__':
    main()
