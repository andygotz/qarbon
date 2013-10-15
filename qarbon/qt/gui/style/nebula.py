# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
# ----------------------------------------------------------------------------
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""Nebula style definition"""

from qarbon.qt.gui.style.templates import GROUPBOX_STYLESHEET_TEMPLATE

__BORDER_RADIUS = '4px'


TAB_STYLESHEET_TEMPLATE = """\

QToolTip {{
    min-width: 280px;
}}

QTabWidget {{
}}

QTabWidget::tab-bar {{
    left: 6px;
}}

QTabWidget::pane {{
    border: 0px solid;
    border-color: rgb(0, 65, 200);
    border-top-left-radius: {border_radius};
    border-top-right-radius: {border_radius};
    border-bottom-left-radius: {border_radius};
    border-bottom-right-radius: {border_radius};
    background-color: {content_background_color};
}}

XulTabpanels {{
    border: 1px solid;
    border-color: rgb(0, 65, 200);
    border-top-left-radius: 0px;
    border-top-right-radius: {border_radius};
    border-bottom-left-radius: {border_radius};
    border-bottom-right-radius: {border_radius};
    background-color: {content_background_color};
}}

QTabBar::tab {{
    color:white;
    background-color: {titlebar_background_color};
    min-width: 8ex;
    min-height: 22px;
    padding: 2px;
}}

QTabBar::tab:top {{
    border-top-left-radius:  {border_radius};
    border-top-right-radius: {border_radius};
}}

QTabBar::tab:bottom {{
    border-bottom-left-radius: {border_radius};
    border-bottom-right-radius: {border_radius};
}}

QTabBar::tab:selected {{
    background-color: {selected_titlebar_background_color};
}}

"""

QGROUPBOX_STYLESHEET_TEMPLATE = """\
QGroupBox {{
    border: 1px solid;
    border-color: rgb(0, 65, 200);
    border-radius: {border_radius};
    margin-top: 1.5ex;
    padding-top: 8px;
    background-color: {content_background_color};
 }}

QGroupBox::title {{
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding-top: 1px;
    padding-right: 3px;
    padding-bottom: 2px;
    padding-left: 3px;
    border-width: 0px;
    border-radius: {border_radius};
    color:white;
    background-color: {selected_titlebar_background_color};
    left: 5px;
}}

 QGroupBox::indicator {{
    width: 15px;
    height: 15px;
}}

"""

QDOCKWIDGET_STYLESHEET_TEMPLATE = """\
QDockWidget {{
    color: {titlebar_color};
    background-color: {content_background_color};
    titlebar-close-icon: url(:/titlebar_close_black.png);
    titlebar-normal-icon: url(:/titlebar_undock_black.png);
}}

QDockWidget::title {{
    text-align: left;
    padding-left: {border_radius};

    border-top-left-radius: {border_radius};
    border-top-right-radius: {border_radius};
    border-bottom-left-radius: {border_radius};
    border-bottom-right-radius: {border_radius};

    background-color: {selected_titlebar_background_color};
}}

"""

QTOOLBOX_STYLESHEET_TEMPLATE = """\
QToolBox:tab {{
    color: {titlebar_color};
    border-width: 0px;
    border-style: solid;
    border-color: rgb(0, 65, 200);
    border-top-left-radius: 0px;
    border-top-right-radius: {border_radius};
    border-bottom-left-radius: {border_radius};
    border-bottom-right-radius: {border_radius};
    background-color: {titlebar_background_color};
}}

QToolBox:tab:selected {{
    background-color: {selected_titlebar_background_color};
}}

QToolBox:tab:first {{
    border-top-left-radius: 0px;
    border-top-right-radius: 0px;
}}

QToolBox:tab:last {{
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
}}

QToolBox:tab:only-one {{
    background-color: {single_titlebar_background_color};
}}

"""

GROUPBOX_NEBULA_STYLESHEET_MAP = {
    'content_start_color':   'rgb(224, 224, 224)',
    'content_stop_color':    'rgb(255, 255, 255)',
    'content_border_radius': __BORDER_RADIUS,
    'title_border_radius':   __BORDER_RADIUS,
    'title_start_color':     'rgb(60, 150, 255)',
    'title_stop_color':      'rgb(0, 65, 200)',
    'title_font_color':      'white',
}

GROUPBOX_NEBULA_STYLESHEET = \
    GROUPBOX_STYLESHEET_TEMPLATE.format(**GROUPBOX_NEBULA_STYLESHEET_MAP)

NEBULA_STYLESHEET_MAP = {
    'border_radius': __BORDER_RADIUS,
    'titlebar_background_color': 'qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgb(200, 200, 200), stop: 1 rgb(150, 150, 150))',
    'selected_titlebar_background_color': 'qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgb(60, 150, 255), stop: 1 rgb(0, 65, 200))',
    'single_titlebar_background_color': 'qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgb(90, 180, 255), stop: 1 rgb(30, 95, 250))',
    'titlebar_color': 'white',
    'selected_titlebar_color': 'white',
    'content_background_color': 'qlineargradient(x1: 0, y1: 0, x2: 1.0, y2: 1.0, stop: 0 rgb(224, 224, 224), stop: 1 rgb(255, 255, 255))'
}

STYLESHEET_TEMPLATE = TAB_STYLESHEET_TEMPLATE + \
    QGROUPBOX_STYLESHEET_TEMPLATE + \
    QDOCKWIDGET_STYLESHEET_TEMPLATE + \
    QTOOLBOX_STYLESHEET_TEMPLATE

STYLESHEET = STYLESHEET_TEMPLATE.format(**NEBULA_STYLESHEET_MAP) + GROUPBOX_NEBULA_STYLESHEET
