# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
# ----------------------------------------------------------------------------
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------
from qarbon.qt.gui.icon import getIcon

"""A LED (light-emitting diode) widget.

This widget represents a led. The led has a color, an status (On/Off) and
blink (No, Slow, Medium Fast).

Here is an example showing how to display all possible combinations of color,
status::

    from qarbon.external.qt import QtGui
    from qarbon.qt.gui.led import Led, LedStatus, LedColor

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
    panel.show()

    app.exec_()
"""

__all__ = ["LedColor", "LedStatus", "Led"]


from qarbon.config import NAMESPACE
from qarbon.external.enum import Enum
from qarbon.external.qt import QtCore, QtGui
from qarbon.qt.gui.pixmapwidget import PixmapWidget


class LedColor(Enum):
    """possible led colors"""

    Blue, Green, Red, Yellow, Orange, Magenta, Grenoble, Black, White = \
        range(9)


class LedStatus(Enum):
    """possible led status"""

    Off, On = range(2)


class Led(PixmapWidget):
    """A LED (light-emitting diode) like widget"""

    #: constant defining default led image filename pattern
    DefaultLedPattern = NAMESPACE + ":/led/led_{color}_{status}.png"

    #: constant defining default led color (green)
    DefaultLedColor = LedColor.Green

    #: constant defining default led status (On)
    DefaultLedStatus = LedStatus.On

    #: constant defining default led status invertion (False)
    DefaultLedInverted = False

    def __init__(self, parent=None):
        self.__ledStatus = self.DefaultLedStatus
        self.__ledColor = self.DefaultLedColor
        self.__ledPatternName = self.DefaultLedPattern
        self.__ledInverted = self.DefaultLedInverted
        self.__ledName = self.toLedName()

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
            status = self.__ledStatus
        if color is None:
            color = self.__ledColor
        if inverted is None:
            inverted = self.__ledInverted
        if inverted:
            if status is LedStatus.On:
                status = LedStatus.Off
            else:
                status = LedStatus.On
        status = status.name.lower()
        color = color.name.lower()
        return self.__ledPatternName.format(color=color, status=status)

    def isLedColorValid(self, name):
        """Determines if the given color name is valid.

        :param color: the color
        :type  color: str
        :return: True is the given color name is valid or False otherwise
        :rtype: bool"""
        return hasattr(LedColor, name)

    def _refresh(self):
        """internal usage only"""
        self.__ledName = self.toLedName()

        pixmap = QtGui.QPixmap(self.__ledName)
        self.setPixmap(pixmap)
        return self.update()

    #--------------------------------------------------------------------------
    # QT property definition
    #--------------------------------------------------------------------------

    def getLedPatternName(self):
        """Returns the current led pattern name
        :return: led pattern name
        :rtype: str"""
        return self.__ledPatternName

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
        self.__ledPatternName = name
        self._refresh()

    def resetLedPatternName(self):
        """Resets the led pattern to **fwk4:/Leds/led_{color}_{status}.png**.
        """
        self.setLedPatternName(self.DefaultLedPattern)

    def getLedStatus(self):
        """Returns the led status
        :return: led status
        :rtype: bool"""
        return self.__ledStatus.value

    def setLedStatus(self, status):
        """Sets the led status
        :param status: the new status
        :type  status: bool"""
        self.__ledStatus = LedStatus(status)
        self._refresh()

    def resetLedStatus(self):
        """Resets the led status"""
        self.setLedStatus(self.DefaultLedStatus)

    def toggleLedStatus(self):
        """toggles the current status of the led"""
        if self.__ledStatus is LedStatus.On:
            self.setLedStatus(LedStatus.Off)
        else:
            self.setLedStatus(LedStatus.On)

    def getLedInverted(self):
        """Returns if the led is inverted.
        :return: inverted mode
        :rtype: bool"""
        return self.__ledInverted

    def setLedInverted(self, inverted):
        """Sets the led inverted mode
        :param status: the new inverted mode
        :type  status: bool"""
        self.__ledInverted = bool(inverted)
        self._refresh()

    def resetLedInverted(self):
        """Resets the led inverted mode"""
        self.setLedInverted(self.DefaultLedInverted)

    def getLedColor(self):
        """Returns the led color
        :return: led color
        :rtype: LedColor"""
        return self.__ledColor.value

    def setLedColor(self, color):
        """Sets the led color
        :param status: the new color
        :type  status: LedColor"""
        self.__ledColor = LedColor(color)
        self._refresh()

    def resetLedColor(self):
        """Resets the led color"""
        self.setLedColor(self.DefaultLedColor)

    @classmethod
    def getQtDesignerPluginInfo(cls):
        return dict(icon=":/designer/ledred.png",)

    #: This property holds the led status: False means OFF, True means ON
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`Led.getLedStatus`
    #:     * :meth:`Led.setLedStatus`
    #:     * :meth:`Led.resetLedStatus`
    ledStatus = QtCore.Property(int, getLedStatus, setLedStatus,
                                resetLedStatus, doc="led status")

    #: This property holds the led color
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`Led.getLedColor`
    #:     * :meth:`Led.setLedColor`
    #:     * :meth:`Led.resetLedColor`
    ledColor = QtCore.Property(int, getLedColor, setLedColor,
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


def main():
    import sys
    from qarbon.qt.gui.application import getApplication

    app = getApplication()
    w = QtGui.QWidget()
    w.setWindowTitle("Led demo")
    w.setWindowIcon(getIcon(":/led/led_green_on.png"))
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
    w.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
