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

"""A led (light-emitting diode) widget.

This widget represents a led. The led has a color, an status (On/Off) and
blink (No, Slow, Medium Fast).

Here is an example showing how to display all possible combinations of color,
status and blinking::

    from qarbon.external.qt import QtGui
    from qarbon.qt.gui.led import Led, LedStatus, LedColor, Blink

    app = QtGui.QApplication([])
    panel = QtGui.QWidget()
    layout = QtGui.QGridLayout()
    layout.setContentsMargins(2, 2, 2, 2)
    layout.setSpacing(2)
    panel.setLayout(layout)
    for i, color in enumerate(LedColor):
        led = Led()
        led.ledColor = color
        led.ledStatus = LedStatus.Off
        layout.addWidget(led, i, 0)
        led = Led()
        led.ledColor = color
        led.ledStatus = LedStatus.On
        layout.addWidget(led, i, 1)
        led = Led()
        led.ledColor = color
        led.blink = Blink.Slow
        layout.addWidget(led, i, 2)
        led = Led()
        led.ledColor = color
        led.blink = Blink.Medium
        layout.addWidget(led, i, 3)
        led = Led()
        led.ledColor = color
        led.blink = Blink.Fast
        layout.addWidget(led, i, 4)
    panel.show()

    app.exec_()
"""

__all__ = ["LedColor", "LedStatus", "Blink", "Led"]

__docformat__ = "restructuredtext"

from qarbon.config import NAMESPACE
from qarbon.external.enum import Enum
from qarbon.external.qt import QtCore, QtGui
from qarbon.qt.gui.pixmapwidget import PixmapWidget


class LedColor(Enum):
    Blue, Green, Red, Yellow, Orange, Magenta, Grenoble, Black, White = \
        range(9)


class LedStatus(Enum):
    On, Off = range(2)


class Blink(Enum):
    No = 0
    Slow = 1000
    Medium = 500
    Fast = 100


class Led(PixmapWidget):
    """A Led like widget"""

    DefaultLedPattern = NAMESPACE + ":/led/led_{color}_{status}.png"
    DefaultLedColor = LedColor.Green
    DefaultLedStatus = LedStatus.On
    DefaultLedInverted = False
    DefaultBlink = Blink.No

    BlinkTimer = {}

    def __init__(self, parent=None):
        self._ledStatus = self.DefaultLedStatus
        self._ledColor = self.DefaultLedColor
        self._ledPatternName = self.DefaultLedPattern
        self._ledInverted = self.DefaultLedInverted
        self._ledName = self.toLedName()
        self._blink = self.DefaultBlink
        self._blinkTimer = None

        PixmapWidget.__init__(self, parent)
        self._refresh()

    def sizeHint(self):
        return PixmapWidget.sizeHint(self)

    def minimumSizeHint(self):
        """Overwrite the default minimum size hint (0,0) to be (8, 8)

        :return: the minimum size hint 8, 8
        :rtype: QSize"""
        return QtCore.QSize(8, 8)

    def toLedName(self, status=None, color=None, inverted=None):
        """Gives the led name for the given status and color. If status or
        color are not given, the current led status or color are used.

        :param status: the status
        :type  status: bool
        :param color: the color
        :type  color: str
        :return: string containing the led name
        :rtype: str"""
        if status is None:
            status = self._ledStatus
        if color is None:
            color = self._ledColor
        if inverted is None:
            inverted = self._ledInverted
        if inverted:
            status = not status
        status = status.name.lower()
        color = color.name.lower()
        return self._ledPatternName.format(color=color, status=status)

    def isLedColorValid(self, name):
        """Determines if the given color name is valid.

        :param color: the color
        :type  color: str
        :return: True is the given color name is valid or False otherwise
        :rtype: bool"""
        return hasattr(LedColor, name)

    def _refresh(self):
        """internal usage only"""
        self._ledName = self.toLedName()

        pixmap = QtGui.QPixmap(self._ledName)
        self.setPixmap(pixmap)
        return self.update()

    #--------------------------------------------------------------------------
    # QT property definition
    #--------------------------------------------------------------------------

    def getLedPatternName(self):
        """Returns the current led pattern name
        :return: led pattern name
        :rtype: str"""
        return self._ledPatternName

    def setLedPatternName(self, name):
        """Sets the led pattern name. Should be a string containing a path
        to valid images. The string can contain the keywords:

            1. {status} - transformed to 'on' of 'off' according to the status
            2. {color} - transformed to the current led color

        Example: **:leds/images256/led_{color}_{status}.png** will be
        transformed to **:leds/images256/led_red_on.png** when the led status
        is True and the led color is red.

        :param name: new pattern
        :type  name: str"""
        self._ledPatternName = name
        self._refresh()

    def resetLedPatternName(self):
        """Resets the led pattern to **fwk4:/Leds/led_{color}_{status}.png**.
        """
        self.setLedPatternName(self.DefaultLedPattern)

    def getLedStatus(self):
        """Returns the led status
        :return: led status
        :rtype: bool"""
        return self._ledStatus

    def setLedStatus(self, status):
        """Sets the led status
        :param status: the new status
        :type  status: bool"""
        self._ledStatus = status
        self._refresh()

    def resetLedStatus(self):
        """Resets the led status"""
        self.setLedStatus(self.DefaultLedStatus)

    def toggleLedStatus(self):
        """toggles the current status of the led"""
        if self.getLedStatus() is LedStatus.On:
            self.setLedStatus(LedStatus.Off)
        else:
            self.setLedStatus(LedStatus.On)

    def getLedInverted(self):
        """Returns if the led is inverted.
        :return: inverted mode
        :rtype: bool"""
        return self._ledInverted

    def setLedInverted(self, inverted):
        """Sets the led inverted mode
        :param status: the new inverted mode
        :type  status: bool"""
        self._ledInverted = bool(inverted)
        self._refresh()

    def resetLedInverted(self):
        """Resets the led inverted mode"""
        self.setLedInverted(self.DefaultLedInverted)

    def getLedColor(self):
        """Returns the led color
        :return: led color
        :rtype: LedColor"""
        return self._ledColor

    def setLedColor(self, color):
        """Sets the led color
        :param status: the new color
        :type  status: LedColor"""
        self._ledColor = color
        self._refresh()

    def resetLedColor(self):
        """Resets the led color"""
        self.setLedColor(self.DefaultLedColor)

    def setBlink(self, blink):
        """sets the blink mode
        Set to a nonpositive number for disabling blinking

        :param interval: the blinking interval in millisecs. Set to 0 to
                         disable blinking
        :type interval: Blink"""
        old_timer = self.BlinkTimer.get(self._blink)
        if blink is Blink.No or old_timer is not None:
            old_timer.timeout.disconnect(self.toggleLedStatus)
            if not old_timer.receivers("timeout"):
                del self.BlinkTimer[self._blink]
        if blink != Blink.No:
            timer = self.BlinkTimer.get(blink)
            if timer is None:
                self.BlinkTimer[blink] = timer = QtCore.QTimer()
                timer.start(blink.value)
            timer.timeout.connect(self.toggleLedStatus)
        self._blink = blink

    def getBlink(self):
        """returns the blink interval

        :return: blink interval
        :rtype: Blink
        """
        if self._timer is None:
            return 0
        else:
            return self._timer.interval()

    def resetBlink(self):
        """resets the blink frequency"""
        self.setBlink(self.DefaultBlink)

    #: This property holds the led status: False means OFF, True means ON
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`Led.getLedStatus`
    #:     * :meth:`Led.setLedStatus`
    #:     * :meth:`Led.resetLedStatus`
    ledStatus = QtCore.Property(LedStatus, getLedStatus, setLedStatus,
                                resetLedStatus, doc="led status")

    #: This property holds the led color
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`Led.getLedColor`
    #:     * :meth:`Led.setLedColor`
    #:     * :meth:`Led.resetLedColor`
    ledColor = QtCore.Property(LedColor, getLedColor, setLedColor,
                               resetLedColor, doc="led color")

    #: This property holds the led inverted: False means do not invert the
    #. status, True means invert the status
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`Led.getLedInverted`
    #:     * :meth:`Led.setLedInverted`
    #:     * :meth:`Led.resetLedInverted`
    ledInverted = QtCore.Property(bool, getLedInverted, setLedInverted,
                                  resetLedInverted, doc="led inverted mode")

    #: This property holds the led pattern name
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`Led.getLedPatternName`
    #:     * :meth:`Led.setLedPatternName`
    #:     * :meth:`Led.resetLedPatternName`
    ledPattern = QtCore.Property(str, getLedPatternName, setLedPatternName,
                                 resetLedPatternName, doc="led pattern name")

    #: This property holds the blink or not state.
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`Led.getBlink`
    #:     * :meth:`Led.setBlink`
    #:     * :meth:`Led.resetBlink`
    blink = QtCore.Property(Blink, getBlink, setBlink, resetBlink,
                            doc="blink or not")


def main():
    import sys
    from qarbon.qt.gui.application import getApplication

    app = getApplication()
    w = QtGui.QWidget()
    layout = QtGui.QGridLayout()
    layout.setContentsMargins(2, 2, 2, 2)
    layout.setSpacing(2)
    w.setLayout(layout)
    for i, color in enumerate(LedColor):
        led = Led()
        led.ledColor = color
        led.ledStatus = LedStatus.Off
        layout.addWidget(led, i, 0)
        led = Led()
        led.ledColor = color
        led.ledStatus = LedStatus.On
        layout.addWidget(led, i, 1)
        led = Led()
        led.ledColor = color
        led.blink = Blink.Slow
        layout.addWidget(led, i, 2)
        led = Led()
        led.ledColor = color
        led.blink = Blink.Medium
        layout.addWidget(led, i, 3)
        led = Led()
        led.ledColor = color
        led.blink = Blink.Fast
        layout.addWidget(led, i, 4)
    w.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
