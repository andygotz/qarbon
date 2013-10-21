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

__all__ = ["QarbonWidgetExtensionFactory", "ExtensionType",
           "registerExtension"]


from qarbon.external.enum import Enum
from qarbon.external.qt import QtDesigner


class ExtensionType(Enum):

    ContainerExtension = "com.trolltech.Qt.Designer.Container"
    PropertySheetExtension = "com.trolltech.Qt.Designer.PropertySheet"
    TaskMenuExtension = "com.trolltech.Qt.Designer.TaskMenu"
    MemberSheetExtension = "com.trolltech.Qt.Designer.MemberSheet"


#: map of registered container extensions
#: <Q_TYPEID, dict<QWidget class, ContainerExtension class>>
Extensions = {}


class QarbonWidgetExtensionFactory(QtDesigner.QExtensionFactory):
    def __init__(self, parent=None):
        super(QarbonWidgetExtensionFactory, self).__init__(parent)

    def createExtension(self, obj, iid, parent):
        return createExtension(obj, iid, parent)


def getExtensionClass(widget, extension_type):
    extension = Extensions.get(ExtensionType(extension_type))
    if extension:
        widget_klass = widget.__class__
        return extension.get(widget_klass)


def createExtension(widget, extension_type, parent=None):
    extension_klass = getExtensionClass(widget, extension_type)
    if extension_klass:
        return extension_klass(widget, parent)


def registerExtension(extension_type, widget_klass, extension_klass):
    global Extensions
    extension_type = ExtensionType(extension_type)
    extension = Extensions.get(extension_type)
    if extension is None:
        Extensions[extension_type] = extension = {}
    extension[widget_klass] = extension_klass
