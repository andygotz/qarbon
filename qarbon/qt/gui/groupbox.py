# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
#
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""A colapsable container widget with (optional) title.

Here is a simple example that shows how to create a :class:`GroupBox` with
some content inside::

    from qarbon.external.qt import QtGui
    from qarbon.qt.gui.application import Application
    from qarbon.qt.gui.icon import Icon
    from qarbon.qt.gui.groupbox import GroupBox

    app = Application()
    panel = QtGui.QWidget()
    layout = QtGui.QVBoxLayout()
    panel.setLayout(layout)
    gb = GroupBox()
    layout.addWidget(gb)

    gb.title = "Configuration"
    gb.icon = Icon("applications-accessories")

    content = QtGui.QWidget()
    gb.setContent(content)
    contentLayout = QtGui.QHBoxLayout()
    content.setLayout(contentLayout)
    label = QtGui.QLabel("File:")
    edit = QtGui.QLineEdit()
    button = QtGui.QPushButton(Icon("folder-open"), "Open a file...")
    contentLayout.addWidget(label)
    contentLayout.addWidget(edit)
    contentLayout.addWidget(button)

    panel.show()
    app.exec_()"""

__all__ = ["GroupBox"]

from qarbon.external.qt import QtCore, QtGui
from qarbon.qt.gui.application import Application
from qarbon.qt.gui.style.templates import GROUPBOX_STYLESHEET_TEMPLATE
from qarbon.qt.gui.style.nebula import GROUPBOX_NEBULA_STYLESHEET
from qarbon.qt.gui.style.nebula import GROUPBOX_NEBULA_STYLESHEET_MAP


class TitleLabel(QtGui.QLabel):
    pass


class TitleBar(QtGui.QFrame):
    pass


class ContentPanel(QtGui.QFrame):

    def __init__(self, parent=None):
        super(ContentPanel, self).__init__(parent)
        self.__content = None
        layout = QtGui.QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def setContent(self, qwidget):
        self.__content = qwidget
        layout = self.layout()
        for _ in range(layout.count()):
            layout.takeAt(0)
        if qwidget is not None:
            layout.addWidget(qwidget)

    def content(self):
        return self.__content


class GroupBox(QtGui.QWidget):
    """An expandable/collapsible container widget"""

    DefaultContentVisible = True
    DefaultTitleBarVisible = True
    DefaultTitleBarHeight = 16

    DefaultStyle = GROUPBOX_NEBULA_STYLESHEET_MAP

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.__titleVisible = self.DefaultTitleBarVisible
        self.__contentVisible = self.DefaultContentVisible
        self.__contentPanel = None
        self.__content = None
        self.__style = self.DefaultStyle
        self.__init()
        self.resetStyleMap()
        self.resetContentVisible()
        self.resetTitleHeight()
        self.resetTitleVisible()

    def __init(self):
        panelLayout = QtGui.QVBoxLayout()
        panelLayout.setSpacing(0)
        panelLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(panelLayout)

        self.__titleBar = titleBar = TitleBar()
        panelLayout.addWidget(titleBar, 0)

        l = QtGui.QHBoxLayout()
        l.setContentsMargins(2, 2, 2, 2)
        l.setSpacing(2)
        self.__titleBar.setLayout(l)

        self.__titleButton = QtGui.QToolButton()
        self.__titleButton.setStyleSheet("border: 0px")
        styleOption = QtGui.QStyleOption()
        styleOption.initFrom(self.__titleButton)
        style = Application().style()
        icon = style.standardIcon(QtGui.QStyle.SP_DesktopIcon, styleOption,
                                  self.__titleButton)
        self.__titleButton.setIcon(icon)
        self.__titleLabel = TitleLabel()
        self.__upDownButton = QtGui.QToolButton()
        self.__upDownButton.setStyleSheet("border: 0px")
        self.__upDownButton.clicked.connect(self.switchContentVisible)
        l.addWidget(self.__titleButton, 0)
        l.addWidget(self.__titleLabel, 1)
        l.addWidget(self.__upDownButton, 0)

        self.__contentPanel = contentPanel = ContentPanel()
        panelLayout.addWidget(contentPanel, 1)

    def _updateStyle(self):
        """Internal method that updates the style"""
        style = GROUPBOX_STYLESHEET_TEMPLATE.format(**self.__style)
        self.setStyleSheet(style)

    def content(self):
        """Returns the contents widget

        :return: the current content widget or None if no content is set
        :rtype: QWidget"""
        return self.__contentPanel.content()

    def setContent(self, qwidget):
        """Sets the content widget

        :param qwidget: the content widget or None
        :type qwidget: QWidget"""
        self.__contentPanel.setContent(qwidget)

    def titleBar(self):
        """Returns the title bar widget

        :return: the title bar widget
        :rtype: QFrame"""
        return self.__titleBar

    def titleButton(self):
        """Returns the title button widget

        :return: the title button widget
        :rtype: QToolButton"""
        return self.__titleButton

    def collapseButton(self):
        """Returns the collapse button widget

        :return: the collapse button widget
        :rtype: QToolButton"""
        return self.__upDownButton

    def setTitle(self, title):
        """Sets this widget's title

        :param title:the new widget title
        :type title: str"""
        self.__titleLabel.setText(title)
        self.setToolTip("<html>The <b>{0}</b>".format(title))

    def getTitle(self):
        """Returns this widget's title

        :return: this widget's title
        :rtype: str"""
        return self.__titleLabel.text()

    def setTitleIcon(self, icon):
        """Sets this widget's title icon

        :param icon: (Qt.QIcon) the new widget title icon"""
        self.__titleButton.setIcon(icon)

    def getTitleIcon(self):
        """Returns this widget's title icon

        :return: this widget's title icon
        :rtype: QIcon"""
        return self.__titleButton.icon()

    def switchContentVisible(self):
        """Switches this widget's contents visibility"""
        self.setContentVisible(not self.isContentVisible())

    def isContentVisible(self):
        """Returns this widget's contents visibility

        :return: this widget's contents visibility
        :rtype: bool"""
        return self.__contentVisible

    def resetContentVisible(self):
        """Resets this widget's contents visibility"""
        self.setContentVisible(self.DefaultContentVisible)

    def setContentVisible(self, show):
        """Sets this widget's contents visibility

        :param show: the new widget contents visibility
        :type show: bool"""
        self.__contentVisible = show

        if show:
            icon_name = QtGui.QStyle.SP_TitleBarShadeButton
        else:
            icon_name = QtGui.QStyle.SP_TitleBarUnshadeButton
        icon = self.style().standardIcon(icon_name)
        self.__upDownButton.setIcon(icon)
        self.__contentPanel.setVisible(show)
        self.adjustSize()

    def isTitleVisible(self):
        """Returns this widget's title visibility

        :return: this widget's title visibility
        :rtype: bool"""
        return self.__titleVisible

    def resetTitleVisible(self):
        """Resets this widget's title visibility"""
        self.setTitleVisible(self.DefaultTitleBarVisible)

    def setTitleVisible(self, show):
        """Sets this widget's title visibility

        :param show: the new widget title visibility
        :type show: bool"""
        self.__titleVisible = show
        self.__titleBar.setVisible(show)

    def getTitleHeight(self):
        """Returns this widget's title height

        :return: this widget's title height
        :rtype: int"""
        return self.titleButton().iconSize().height()

    def setTitleHeight(self, height):
        """Sets this widget's title height

        :param height: the new widget title height
        :type height: int"""
        s = QtCore.QSize(height, height)
        self.titleButton().setIconSize(s)
        self.collapseButton().setIconSize(s)

    def resetTitleHeight(self):
        """Resets this widget's title height"""
        self.setTitleHeight(self.DefaultTitleBarHeight)

    def getStyleMap(self):
        """Returns this widget's style

        :return: this widget's style
        :rtype: dict"""
        return self.__style

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

        :param style_map: the new widget title style
        :type style_map: dict"""
        style = self.DefaultStyle.copy()
        style.update(style_map)
        self.__style = style
        self._updateStyle()

    def resetStyleMap(self):
        """Resets this widget's title style"""
        self.setStyleMap({})

    @classmethod
    def getQtDesignerPluginInfo(cls):
        from qarbon.qt.designer.plugins.base import DesignerBaseSingleContainerExtension
        return dict(icon=":/designer/groupwidget.png", container=True,
                    container_extension=DesignerBaseSingleContainerExtension)

    #: This property contains the widget's title
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`getTitle`
    #:     * :meth:`setTitle`
    title = QtCore.Property(str, getTitle, setTitle)

    #: This property contains the widget's title icon
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`getTitleIcon`
    #:     * :meth:`setTitleIcon`
    titleIcon = QtCore.Property("QIcon", getTitleIcon, setTitleIcon)

    #: This property contains the widget's title height
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`getTitleHeight`
    #:     * :meth:`setTitleHeight`
    #:     * :meth:`resetTitleHeight`
    titleHeight = QtCore.Property(int, getTitleHeight, setTitleHeight,
                                  resetTitleHeight)

    #: This property contains the widget's title visibility
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`isTitleVisible`
    #:     * :meth:`setTitleVisible`
    titleVisible = QtCore.Property(bool, isTitleVisible, setTitleVisible)

    #: This property contains the widget's style map
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`getStyleMap`
    #:     * :meth:`setStyleMap`
    #:     * :meth:`resetStyleMap`
    styleMap = QtCore.Property(dict, getStyleMap, setStyleMap, resetStyleMap,
                               designable=False)

    #: This property contains the widget's content's visibility
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`isContentVisible`
    #:     * :meth:`setContentVisible`
    #:     * :meth:`resetContentVisible`
    contentVisible = QtCore.Property(bool, isContentVisible,
                                     setContentVisible, resetContentVisible)


def main():
    from qarbon.qt.gui.icon import getIcon

    app = Application()
    app.setStyleSheet(GROUPBOX_NEBULA_STYLESHEET)

    w = QtGui.QWidget()
    l = QtGui.QVBoxLayout()
    w.setLayout(l)

    panel = GroupBox()
    panel.title = "Database"
    content = QtGui.QWidget()
    contentLayout = QtGui.QFormLayout()
    content.setLayout(contentLayout)
    panel.setContent(content)
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

    content = QtGui.QWidget()
    contentLayout = QtGui.QFormLayout()
    content.setLayout(contentLayout)
    panel.setContent(content)
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
    content = QtGui.QWidget()
    contentLayout = QtGui.QFormLayout()
    content.setLayout(contentLayout)
    panel.setContent(content)
    contentLayout.addRow("Something", QtGui.QLineEdit())
    contentLayout.addRow("More", QtGui.QLineEdit())
    l.addWidget(panel, 0)

    panel = GroupBox()
    panel.title = "5"
    panel.titleIcon = getIcon("folder")
    content = QtGui.QWidget()
    contentLayout = QtGui.QVBoxLayout()
    content.setLayout(contentLayout)
    panel.setContent(content)
    panel2 = GroupBox()
    panel2.title = "5.1"
    panel2.titleIcon = getIcon("folder")
    panel2.titleHeight = 48

    content2 = QtGui.QWidget()
    contentLayout2 = QtGui.QFormLayout()
    content2.setLayout(contentLayout2)
    panel2.setContent(content2)
    contentLayout2.addRow("Something", QtGui.QLineEdit())
    contentLayout2.addRow("More", QtGui.QLineEdit())
    contentLayout.addWidget(panel2, 0)
    l.addWidget(panel, 0)

    l.addStretch(1)

    w.show()
    w.adjustSize()

    app.exec_()
    return w


if __name__ == '__main__':
    main()
