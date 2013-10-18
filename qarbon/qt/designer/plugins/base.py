# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
# ----------------------------------------------------------------------------
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""internal module defining base WidgetPlugin class to interface between
qarbon and QtDesigner"""

__all__ = ["get_designer_class"]

import inspect
import logging

from qarbon.external.qt import QtDesigner
from qarbon.qt.gui.icon import getIcon


#
# Class is hidden to prevent QtDesigner from instantiating it
#
class __DesignerBaseWidgetPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):
    """Qarbon's custom base widget plugin class for QtDesginer"""

    def __init__(self, parent=None):
        QtDesigner.QPyDesignerCustomWidgetPlugin.__init__(self)
        self.initialized = False

    def initialize(self, formEditor):
        """Overwrite if necessary. Don't forget to call this method in case you
        want the generic extensions in your widget."""
        if self.isInitialized():
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def getWidgetClass(self):
        return self.WidgetClass

    def _getWidgetClassName(self):
        return self.getWidgetClass().__name__

    def createWidget(self, parent):
        try:
            klass = self.getWidgetClass()
            w = klass(parent)
        except Exception:
            name = self._getWidgetClassName()
            logging.error("Designer plugin error creating %s " \
                          "(see debug stream for details)", name)
            logging.debug("Details:", exc_info=1)
            w = None
        return w

    def getWidgetInfo(self, key, dft=None):
        if not hasattr(self, '_widgetInfo'):
            self._widgetInfo = self.getWidgetClass().getQtDesignerPluginInfo()
        return self._widgetInfo.get(key, dft)

    def name(self):
        return self._getWidgetClassName()

    def group(self):
        return self.getWidgetInfo('group', 'Qarbon Widgets')

    def getIconName(self):
        return self.getWidgetInfo('icon')

    def icon(self):
        return getIcon(self.getIconName())

    def domXml(self):
        name = str(self.name())
        lowerName = name[0].lower() + name[1:]
        return '<widget class="%s" name=\"%s\" />\n' % (name, lowerName)

    def includeFile(self):
        """Returns the module containing the custom widget class.
        It may include a module path."""
        klass = self.getWidgetClass()
        return inspect.getmodule(klass).__name__

    def toolTip(self):
        tooltip = self.getWidgetInfo('tooltip')
        if tooltip is None:
            tooltip = "A %s" % self._getWidgetClassName()
        return tooltip

    def whatsThis(self):
        whatsthis = self.getWidgetInfo('whatsthis')
        if whatsthis is None:
            whatsthis = "This is a %s widget" % self._getWidgetClassName()
        return whatsthis

    def isContainer(self):
        return self.getWidgetInfo('container', False)


def get_designer_class():
    return __DesignerBaseWidgetPlugin
