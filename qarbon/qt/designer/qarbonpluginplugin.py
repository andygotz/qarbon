# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
#
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""Helper module for Qt Designer.

It is supposed to be imported by Qt Designer python plugin. At that time it 
will generate plugin classes, one for each *Qt Designer enabled* qarbon
widget."""

import os
import logging
import collections

import qarbon
from qarbon.util import moduleDirectory
from qarbon.qt.gui.util import getWidgetClasses


def __build_qtdesigner_widget_plugin(klass):
    """Helper method that will generate a QtDesigner custom widget plugin
    class for the given widget"""

    from qarbon.qt.designer.plugins.base import DesignerBaseWidgetPlugin

    name = klass.__name__

    class Plugin(DesignerBaseWidgetPlugin):
        WidgetClass = klass

    Plugin.__name__ = name + "QtDesignerPlugin"

    return Plugin


def getPlugins():
    """Returns a map with all custom widget plugins."""

    widgets = {}
    plugins = {}
    qarbon_dir = moduleDirectory(qarbon)
    base_widget_dir = os.path.join(qarbon_dir, "qt", "gui")
    base_package = "qarbon.qt.gui."

    for filename in os.listdir(base_widget_dir):
        if filename.startswith(".") or filename.startswith("_") or \
           not filename.endswith(".py"):
            continue
        fullpath = os.path.join(base_widget_dir, filename)
        if not os.path.isfile(fullpath):
            continue
        modulename = base_package + os.path.splitext(filename)[0]
        try:
            widgets.update(getWidgetClasses(modulename))
        except ImportError:
            logging.warning("Error importing %s", modulename)

    for _, widget_info in widgets.items():
        widget_klass = widget_info["klass"]
        widget_name = widget_info['name']
        info_func = getattr(widget_klass, "getQtDesignerPluginInfo", None)
        if info_func is None:
            logging.debug("widget '%s' has no 'getQtDesignerPluginInfo'",
                          widget_name)
            continue
        info = info_func()
        if isinstance(info, collections.Mapping):
            plugin_klass = __build_qtdesigner_widget_plugin(widget_klass)
            plugin_klass_name = plugin_klass.__name__
            #globals()[plugin_klass_name] = plugin_klass
            plugins[plugin_klass_name] = plugin_klass
    return plugins

def main():
    try:
        level = os.environ["QARBON_DESIGNER_LOG_LEVEL"]
        level = getattr(logging, level.upper())
    except:
        level = logging.WARNING
    logging.getLogger().setLevel(level)

    plugins = getPlugins()
    globals().update(plugins)


if __name__ != "__main__":
    main()
else:
    print getPlugins()
