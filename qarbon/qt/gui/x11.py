# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
#
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""A X11 widget that may run any command and an XTermWidget runs a xterm.

.. note:: this widget only works on X11 systems.

Example::

    from qarbon.external.qt import QtGui
    from qarbon.qt.gui.application import Application
    from qarbon.qt.gui.x11terminal import XTermWindow

    app = Application()
    term = XTermWindow()
    term.start()
    term.show()
    app.exec_()"""

__all__ = ["XEmbedCommandWidget", "XTermWidget",
           "XEmbedCommandWindow", "XTermWindow"]

import logging
import weakref

from qarbon.external.qt import QtCore, QtGui
from qarbon.qt.gui.application import Application
from qarbon.qt.gui.action import Action
from qarbon.qt.gui.icon import Icon


class XEmbedCommandWidget(QtGui.QX11EmbedContainer):
    """A widget displaying an X11 window inside from a command.

    Example::

        from qarbon.external.qt import QtGui
        from qarbon.qt.gui.application import Application
        from qarbon.qt.gui.x11 import XEmbedCommandWidget
        
        app = Application()
        w = QtGui.QMainWindow()
        cmdWidget = XEmbedCommandWidget(parent=w)
        cmdWidget.command = 'xterm'
        cmdWidget.winIdParam = '-into'
        cmdWidget.start()
        w.setCentralWidget(cmdWidget)
        w.show()
        app.exec_()"""

    DefaultAutoRestart = False
    DefaultWinIdParam = '-into'

    def __init__(self, parent=None):
        super(XEmbedCommandWidget, self).__init__(parent)
        self.error.connect(self.__onError)
        self.__process = process = QtCore.QProcess(self)
        self.resetCommand()
        self.resetAutoRestart()
        self.resetWinIdParam()
        self.resetExtraParams()

    def __onError(self, error):
        logging.error("XEmbedContainer: Error")

    def getProcess(self):
        return self.__process

    def getCommand(self):
        return self.__command

    def setCommand(self, command):
        self.__command = command
        if command is None:
            self.setWindowTitle("<None>")
        else:
            self.setWindowTitle(command)

    def resetCommand(self):
        self.setCommand(None)

    def getWinIdParam(self):
        return self.__winIdParam

    def setWinIdParam(self, winIdParam):
        self.__winIdParam = winIdParam

    def resetWinIdParam(self):
        self.setWinIdParam(self.DefaultWinIdParam)

    def setExtraParams(self, params):
        if params is None:
            params = []
        self.__extraParams = params

    def getExtraParams(self):
        return self.__extraParams 

    def resetExtraParams(self):
        self.setExtraParams(None)

    def setAutoRestart(self, yesno):
        self.__autoRestart = yesno

    def getAutoRestart(self):
        return self.__autoRestart

    def resetAutoRestart(self):
        return self.setAutoRestart(self.DefaultAutoRestart)

    def setWorkingDirectory(self, wd):
        if wd is not None:
            self.getProcess().setWorkingDirectory(wd)

    def getWorkingDirectory(self):
        return self.getProcess().workingDirectory()

    def __convert_wait(self, wait):
        if wait:
            if wait < 0:
                wait = -1
            else:
                wait = int(wait * 1000)
        return wait

    def start(self, wait=0):
        """wait < 0 -> wait forever,
           wait == 0 -> not wait,
           wait > 0 -> wait amount in seconds"""
        if self.__command is None:
            raise Exception("Cannot start: no command")
        if self.__winIdParam is None:
            raise Exception("Cannot start: no winIdParam")
        process = self.__process
        params = [self.__winIdParam, str(self.winId())] + self.__extraParams
        process.start(self.__command, params)
        wait = self.__convert_wait(wait)
        if wait:
            return process.waitForStarted(msecs=wait)

    def restart(self, wait=0):
        self.terminate(wait=-1)
        return self.start(wait=wait)

    def __finish(self, finish_func, wait=0):
        process = self.__process
        wait = self.__convert_wait(wait)
        finish_func()
        if wait:
            return process.waitForFinished(msecs=wait)

    def kill(self, wait=0):
        return self.__finish(self.__process.kill, wait=wait)

    def terminate(self, wait=0):
        return self.__finish(self.__process.terminate, wait=wait)

    def event(self, event):
        ret = super(XEmbedCommandWidget, self).event(event)
        etype = event.type()
        if etype == QtCore.QEvent.ParentAboutToChange:
            if self.__process.state() != QtCore.QProcess.NotRunning:
                self.terminate()
        elif etype == QtCore.QEvent.ParentChange:
            if self.autoRestart:
                logging.info("restarting...")
                self.restart(wait=3)
        return ret

    def destroy(self, *args, **kwargs):
        print("Destroying embeded widget")        
        logging.warning("Destroying embeded widget")
        self.terminate(wait=-1)
        return super(XEmbedCommandWidget, self).destroy(*args, **kwargs)

    command = QtCore.Property(str, getCommand, setCommand, resetCommand)

    winIdParam = QtCore.Property(str, getWinIdParam, setWinIdParam,
                                 resetWinIdParam)

    extraParams = QtCore.Property("QStringList", getExtraParams,
                                  setExtraParams, resetExtraParams)

    autoRestart = QtCore.Property(bool, getAutoRestart, setAutoRestart,
                                  resetAutoRestart)

    workingDirectory = QtCore.Property(str, getWorkingDirectory,
                                       setWorkingDirectory)


class XEmbedCommandWindow(QtGui.QMainWindow):
    """The QMainWindow version of :class:`XEmbedCommandWidget`.

    Example::

        from qarbon.external.qt import QtGui
        from qarbon.qt.gui.application import Application
        from qarbon.qt.gui.x11 import XEmbedCommandWindow
        
        app = Application()
        w = XEmbedCommandWindow()
        w.command = 'xterm'
        w.winIdParam = '-into'
        w.start()
        w.show()
        app.exec_()"""

    Widget = XEmbedCommandWidget

    def __init__(self, **kwargs):
        parent = kwargs.pop('parent', None)
        flags = kwargs.pop('flags', QtCore.Qt.WindowFlags())
        super(XEmbedCommandWindow, self).__init__(parent=parent, flags=flags)
        x11 = self.Widget(parent=self, **kwargs)
        self.setCentralWidget(x11)
        toolBar = self.addToolBar("Actions")
        self.__actionsToolBar = weakref.ref(toolBar)
        self.__restartAction = Action("Restart", parent=self,
                                      icon=Icon("view-refresh"),
                                      tooltip="restart the current command",
                                      triggered=self.restart)
        toolBar.addAction(self.__restartAction)

    def XWidget(self):
        return self.centralWidget()

    def start(self, wait=0):
        self.XWidget().start(wait=wait)

    def restart(self, wait=0):
        self.XWidget().restart(wait=wait)

    def terminate(self, wait=0):
        self.XWidget().terminate(wait=wait)

    def getCommand(self):
        return XWidget().command
    
    def setCommand(self, command):
        self.XWidget().command = command
    
    def resetCommand(self):
        self.XWidget().resetCommand()

    def getWinIdParam(self):
        return self.XWidget().winIdParam

    def setWinIdParam(self, winIdParam):
        self.XWidget().winIdParam = winIdParam

    def resetWinIdParam(self):
        self.XWidget().resetWinIdParam()

    def setExtraParams(self, params):
        self.XWidget().extraParams = params

    def getExtraParams(self):
        return self.XWidget().extraParams 

    def resetExtraParams(self):
        self.XWidget().resetExtraParams()

    def setAutoRestart(self, yesno):
        self.XWidget().autoRestart = yesno

    def getAutoRestart(self):
        return self.XWidget().autoRestart

    def resetAutoRestart(self):
        self.XWidget().resetAutoRestart()

    def setWorkingDirectory(self, wd):
        self.XWidget().workingDirectory = wd

    def getWorkingDirectory(self):
        return self.XWidget().workingDirectory

    def destroy(self, *args, **kwargs):
        logging.warning("Destroying embeded window")
        self.terminate(wait=-1)
        return super(XEmbedCommandWindow, self).destroy(*args, **kwargs)

    command = QtCore.Property(str, getCommand, setCommand, resetCommand)

    winIdParam = QtCore.Property(str, getWinIdParam, setWinIdParam,
                                 resetWinIdParam)

    extraParams = QtCore.Property("QStringList", getExtraParams,
                                  setExtraParams, resetExtraParams)

    autoRestart = QtCore.Property(bool, getAutoRestart, setAutoRestart,
                                        resetAutoRestart)

    workingDirectory = QtCore.Property(str, getWorkingDirectory,
                                       setWorkingDirectory)


class XTermWidget(XEmbedCommandWidget):
    """A widget with an xterm console inside.
    
    Example::

        from qarbon.external.qt import QtGui
        from qarbon.qt.gui.application import Application
        from qarbon.qt.gui.x11 import XTermWidget

        app = Application()
        w = QtGui.QMainWindow()
        term = XTermWidget(parent=w)
        w.setCentralWidget(term)
        w.start()
        w.show()
        app.exec_()"""

    def __init__(self, auto_start=False, parent=None):
        super(XTermWidget, self).__init__(parent=parent)
        self.command = 'xterm'
        if auto_start:
            self.start()

    def sizeHint(self):
        return QtCore.QSize(800, 600)


class XTermWindow(XEmbedCommandWindow):
    """The QMainWindow version of :class:`XTermWidget`

        from qarbon.external.qt import QtGui
        from qarbon.qt.gui.application import Application
        from qarbon.qt.gui.x11 import XTermWidget

        app = Application()
        term = XTermWindow()
        term.start()
        term.show()
        app.exec_()"""

    Widget = XTermWidget


def main():
    logging.basicConfig(level=logging.DEBUG)
    app = Application()
    w = XTermWidget()
#    w.extraParams = ["-e", "spec"]
    w.start()
    w.show()
    app.exec_()

if __name__ == "__main__":
    main()
