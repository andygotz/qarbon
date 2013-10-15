# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
# ----------------------------------------------------------------------------
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

""""""

import os
import logging
import collections


import qarbon
from qarbon.qt.gui.util import getWidgets
from qarbon.util import moduleDirectory


def __build_qtdesigner_widget_plugin(klass):
    from qarbon.qt.designer.extension import get_designer_class

    DesignerBaseWidgetPlugin = get_designer_class()

    name = klass.__name__

    class Plugin(DesignerBaseWidgetPlugin):
        WidgetClass = klass

    Plugin.__name__ = name + "QtDesignerPlugin"
    return Plugin


def getPlugins():
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
            widgets.update(getWidgets(modulename))
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
    plugins = getPlugins()
    globals().update(plugins)


if __name__ != "__main__":
    main()
else:
    print getPlugins()
