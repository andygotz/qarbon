# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
#
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""Helper functions to deal with Qt GUI related stuff"""

__all__ = ["isWidget", "isWidgetClass", "getWidgetClasses",
           "grabWidget"]

import time
import inspect
import logging
import threading

from qarbon.util import moduleImport
from qarbon.external.qt import QtCore, QtGui


def isWidget(obj):
    """Determines if the given object is a Qt Widget.

    :param obj: object
    :return: True if the given object is a Qt Widget or False otherwise
    :rtype: bool
    """
    return isinstance(obj, QtCore.QObject) and obj.isWidgetType()


def isWidgetClass(obj):
    """Determines if the given object is a Qt Widget class.

    :param obj: object
    :return: True if the given object is a Qt Widget class or False otherwise
    :rtype: bool
    """
    return inspect.isclass(obj) and issubclass(obj, QtGui.QWidget)


def getWidgetClasses(module_name):
    """Returns the widget classes defined in a given module.

    Returns:

    {widget full name(str): {"klass": widget class(class),
    "name": widget name(str), "full_name": widget full name(str)}}

    :param module_name: name of the module in the format "a.b.c"
    :type module_name: str
    :return: a map with the widgets for the given module
    :rtype: dict
    """
    widgets = {}
    module = moduleImport(module_name)

    for name, value in inspect.getmembers(module, isWidgetClass):
        if inspect.getmodule(value) != module:
            continue
        full_name = module_name + "." + name
        widgets[full_name] = dict(klass=value, name=name, full_name=full_name)
    return widgets


class __GrabberThread(threading.Thread):
    """Helper to trigger grabbing a widget periodically"""
    
    def __init__(self, widget, fileName, period):
        threading.Thread.__init__(self, name="Grabber")
        self.daemon = True
        if period <= 0:
            raise ValueError("period MUST be greater than 0")
        self.__period = period
        self.__continue = True
        self.__grabber = __Grabber(widget, fileName)
        
    def run(self):
        period = self.__period
        while self.__continue:
            self.__grabber.grabTrigger()
            time.sleep(period)
    
    def stop(self):
        self.__continue = False
    

class __Grabber(QtCore.QObject):

    grab = QtCore.Signal()

    def __init__(self, widget, fileName):
        QtCore.QObject.__init__(self)
        self.__widget = widget
        self.__fileName = fileName
        self.grab.connect(self.__onGrab)
    
    def grabTrigger(self):
        self.grab.emit()
        
    def __onGrab(self):
        grabWidget(self._widget, self._fileName)


def grabWidget(widget, fileName, period=None):
    """Grabs the given widget into the given image filename. If period is
    None (default) it grabs immediately once and returns.
    If period is given and >0 means grab the image every period (in seconds).
    
    .. warning::
        this method **MUST** be called from the same thread which created
        the widget
    
    :param widget: the Qt widget to be grabbed
    :type widget: QtWidget
    :param fileName:  the name of the image file
    :type fileName: str
    :param period: period (seconds)
    :type period: float
    """
    if period is None:
        widgetName = widget.objectName()
        widgetTitle = widget.windowTitle()
        logging.debug("Grabbing widget '%s' to '%s':", widgetName, fileName)
        try:
            pixmap = QtGui.QPixmap.grabWidget(widget)
            if fileName.endswith('.svg'):
                import qarbon.external.qt.QtSvg
                generator = qarbon.external.qt.QtSvg.QSvgGenerator()
                generator.setFileName(fileName)
                generator.setSize(pixmap.size());
                if hasattr(generator, 'setViewBox'):
                    viewBox = QtCore.QRect(QtCore.QPoint(0, 0), pixmap.size())
                    generator.setViewBox(viewBox)
                title = "Qarbon widget"
                if widgetTitle:
                    title += " - " + widgetTitle
                elif widgetName:
                    title += " - " + widgetName
                desc = "An SVG created by the qarbon widget grabber"
                generator.setTitle(title)
                generator.setDescription(desc)
                painter = QtGui.QPainter()
                painter.begin(generator)
                try:
                    painter.drawPixmap(0, 0, -1, -1, pixmap)
                finally:
                    painter.end()
            else:
                pixmap.save(fileName, quality=100)
        except Exception:
            logging.warning("Could not save file into '%s':", fileName)
            logging.debug("Details:", exc_info=1)

    ret = __GrabberThread(widget, fileName, period)
    ret.start()
    return ret

