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

__all__ = ["DesignerBaseWidgetPlugin", "DesignerBaseContainerExtension"]

import inspect
import logging

from qarbon.external.qt import QtGui, QtDesigner
from qarbon.qt.gui.icon import getIcon
from qarbon.qt.designer.plugins.factory import ExtensionType, \
    QarbonWidgetExtensionFactory, registerExtension


#
# Class is hidden to prevent QtDesigner from instantiating it
#
class DesignerBaseWidgetPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):
    """Qarbon"s custom base widget plugin class for QtDesginer"""

    def __init__(self, parent=None):
        QtDesigner.QPyDesignerCustomWidgetPlugin.__init__(self)
        self.__initialized = False

    def initialize(self, formEditor):
        """Overwrite if necessary. Don"t forget to call this method in case you
        want the generic extensions in your widget."""
        if self.isInitialized():
            return

        if self.isContainer():
            print "registering extension for", self.name()
            container_extension = self.getContainerExtensionClass()
            registerExtension(ExtensionType.ContainerExtension,
                              self.getWidgetClass(),
                              container_extension)

            manager = formEditor.extensionManager()
            self.__extension_factory = QarbonWidgetExtensionFactory(manager)
            manager.registerExtensions(self.__extension_factory,
                                       ExtensionType.ContainerExtension.value)
            print "Done registering extension for", self.name()

        self.__initialized = True

    def isInitialized(self):
        return self.__initialized

    def getWidgetClass(self):
        return self.WidgetClass

    def _getWidgetClassName(self):
        return self.getWidgetClass().__name__

    def createWidget(self, parent):
        try:
            w = self.getWidgetClass()(parent)
        except Exception:
            logging.error("Designer plugin error creating %s " \
                          "(see debug stream for details)", self.name())
            logging.debug("Details:", exc_info=1)
            w = None
        return w

    def getWidgetInfo(self, key, dft=None):
        if not hasattr(self, "_widgetInfo"):
            self._widgetInfo = self.getWidgetClass().getQtDesignerPluginInfo()
        return self._widgetInfo.get(key, dft)

    def name(self):
        return self._getWidgetClassName()

    def group(self):
        return self.getWidgetInfo("group", "Qarbon Widgets")

    def getIconName(self):
        return self.getWidgetInfo("icon")

    def icon(self):
        return getIcon(self.getIconName())

    def domXml(self):
        name = str(self.name())
        lowerName = name[0].lower() + name[1:]
        return """<widget class="%s" name="%s" />\n""" % (name, lowerName)

    def includeFile(self):
        return inspect.getmodule(self.getWidgetClass()).__name__

    def toolTip(self):
        tooltip = self.getWidgetInfo("tooltip")
        if tooltip is None:
            tooltip = "A %s" % self._getWidgetClassName()
        return tooltip

    def whatsThis(self):
        whatsthis = self.getWidgetInfo("whatsthis")
        if whatsthis is None:
            whatsthis = "This is a %s widget" % self._getWidgetClassName()
        return whatsthis

    def isContainer(self):
        return self.getWidgetInfo("container", False)

    def getContainerExtensionClass(self):
        return self.getWidgetInfo("container_extension",
                                  DesignerBaseContainerExtension)


class DesignerBaseContainerExtension(QtDesigner.QPyDesignerContainerExtension):

    def __init__(self, widget, parent=None):
        super(DesignerBaseContainerExtension, self).__init__(parent)
        self.__widget = widget

    def pluginWidget(self):
        return self.__widget


class DesignerBaseSingleContainerExtension(DesignerBaseContainerExtension):

    def __init__(self, widget, parent=None):
        super(DesignerBaseSingleContainerExtension, self).__init__(widget,
                                                                parent=parent)
        self.__content_widget = None

    def addWidget(self, widget):
        if self.count() > 0:
            QtGui.QMessageBox.warning(None, "Error adding page",
                                      "Cannot have more than one page",
                                      buttons=QtGui.QMessageBox.Ok,
                                      defaultButton=QtGui.QMessageBox.Ok)
            return
        self.pluginWidget().setContent(widget)
        self.__content_widget = widget

    def count(self):
        if self.__content_widget is None:
            return 0
        return 1

    def currentIndex(self):
        if self.count() > 0:
            return 0
        return -1

    def insertWidget(self, index, widget):
        self.addWidget(widget)

    def remove(self, index):
        self.pluginWidget().setContent(None)

    def setCurrentIndex(self, index):
        pass

    def widget(self, index):
        return self.__content_widget
