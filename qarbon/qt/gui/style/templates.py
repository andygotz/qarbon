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

"""Templates to be used by styles"""

GROUPBOX_STYLESHEET_TEMPLATE = """\
.TitleLabel {{ color : {title_font_color}; }}

GroupBox[contentVisible="true"] .TitleBar {{
    border-width: 0px;
    border-style: solid;
    border-color: {title_stop_color};
    border-top-left-radius: {title_border_radius};
    border-top-right-radius: {title_border_radius};
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 {title_start_color}
                                      stop: 1 {title_stop_color});
}}

GroupBox[contentVisible="false"] .TitleBar {{
    border-width: 0px;
    border-style: solid;
    border-color: {title_stop_color};
    border-top-left-radius: {title_border_radius};
    border-top-right-radius: {title_border_radius};
    border-bottom-left-radius: {title_border_radius};
    border-bottom-right-radius: {title_border_radius};
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 {title_start_color},
                                      stop: 1 {title_stop_color});
}}

GroupBox[titleVisible="true"] .ContentPanel {{
    border-top-width: 0px;
    border-left-width: 1px;
    border-right-width: 1px;
    border-bottom-width: 1px;
    border-style: solid;
    border-color: {title_stop_color};
    border-top-left-radius: 0px;
    border-top-right-radius: 0px;
    border-bottom-left-radius: {content_border_radius};
    border-bottom-right-radius: {content_border_radius};
    background-color: qlineargradient(x1: 0, y1: 0, x2: 1.0, y2: 1.0,
                                      stop: 0 {content_start_color},
                                      stop: 1 {content_stop_color});
}}

GroupBox[titleVisible="false"] .ContentPanel {{
border-width: 1px;
border-style: solid;
border-color: {title_stop_color};
border-top-left-radius: {content_border_radius};
border-top-right-radius: {content_border_radius};
border-bottom-left-radius: {content_border_radius};
border-bottom-right-radius: {content_border_radius};
background-color: qlineargradient(x1: 0, y1: 0, x2: 1.0, y2: 1.0,
                                  stop: 0 {content_start_color},
                                  stop: 1 {content_stop_color});
}}
"""
