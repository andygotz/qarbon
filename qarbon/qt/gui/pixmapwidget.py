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

"""a widget that displays an image (pixmap).

You can adjust properties like the aligment inside the widget space, aspect
ratio and transformation mode (quality).

Example usage::

    import qarbon
    from qarbon.external.qt import QtGui
    from qarbon.qt.gui.pixmapwidget import PixmapWidget

    app = QtGui.QApplication([])
    panel = QtGui.QWidget()
    layout = QtGui.QGridLayout()
    layout.setContentsMargins(2, 2, 2, 2)
    layout.setSpacing(2)
    panel.setLayout(layout)
    img = PixmapWidget()
    layout.addWidget(img)

    img.setPixmap(QtGui.QPixmap(qarbon.NAMESPACE + ":/led/led_red_on.png")
    img.show()
    app.exec_()
"""

__all__ = ["PixmapWidget"]

__docformat__ = 'restructuredtext'

from qarbon.external.qt import QtCore, QtGui


class PixmapWidget(QtGui.QWidget):
    """This widget displays an image (pixmap). By default the pixmap is
    scaled to the widget size and the aspect ratio is kept.
    The default alignment of the pixmap inside the widget space is horizontal
    left, vertical center."""

    DefaultAlignment = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
    DefaultAspectRatioMode = QtCore.Qt.KeepAspectRatio
    DefaultTransformationMode = QtCore.Qt.SmoothTransformation

    #: Signal emited when pixmap source changes
    pixmapChanged = QtCore.Signal()

    def __init__(self, parent=None):
        self._pixmap = QtGui.QPixmap()
        self._pixmapDrawn = None
        self._alignment = self.DefaultAlignment
        self._pixmapAspectRatioMode = self.DefaultAspectRatioMode
        self._pixmapTransformationMode = self.DefaultTransformationMode

        QtGui.QWidget.__init__(self, parent)

    def _getPixmap(self):
        if self._pixmapDrawn is None:
            self._pixmapDrawn = self.recalculatePixmap()
        return self._pixmapDrawn

    def recalculatePixmap(self):
        origPixmap = self._pixmap
        if origPixmap.isNull():
            return origPixmap
        return origPixmap.scaled(self.size(), self._pixmapAspectRatioMode,
                                 self._pixmapTransformationMode)

    def _setDirty(self):
        self._pixmapDrawn = None

    def paintEvent(self, paintEvent):
        """Overwrite the paintEvent from QWidget to draw the pixmap"""
        pixmap = self._getPixmap()

        w, h = self.width(), self.height()
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        pw, ph = pixmap.width(), pixmap.height()
        align = self._alignment
        hAlign = align & QtCore.Qt.AlignHorizontal_Mask
        vAlign = align & QtCore.Qt.AlignVertical_Mask
        x, y = 0, 0
        if hAlign & QtCore.Qt.AlignHCenter:
            x = (w - pw) / 2
        elif hAlign & QtCore.Qt.AlignRight:
            x = w - pw
        if vAlign & QtCore.Qt.AlignVCenter:
            y = (h - ph) / 2
        elif vAlign & QtCore.Qt.AlignBottom:
            y = h - ph
        x, y = max(0, x), max(0, y)
        painter.drawPixmap(x, y, pixmap)

    def resizeEvent(self, event):
        self._setDirty()
        return QtGui.QWidget.resizeEvent(self, event)

    def sizeHint(self):
        return self._pixmap.size()

    #--------------------------------------------------------------------------
    # QT property definition
    #--------------------------------------------------------------------------

    def getPixmap(self):
        """Returns the pixmap.Returns None if no pixmap is set.

        :return: the current pixmap
        :rtype: QtGui.QPixmap"""
        return self._pixmap

    def setPixmap(self, pixmap):
        """Sets the pixmap for this widget. Setting it to None disables pixmap

        :param pixmap: the new pixmap
        :type  pixmap: QtGui.QPixmap"""
        # make sure to make a copy because of bug in PyQt 4.4. This is actually
        # not copying the internal bitmap, just the qpixmap, so there is no
        # performance penalty here
        self._pixmap = QtGui.QPixmap(pixmap)
        self._setDirty()
        self.update()
        self.pixmapChanged.emit()

    def resetPixmap(self):
        """Resets the pixmap for this widget."""
        self.setPixmap(QtGui.QPixmap())

    def getAspectRatioMode(self):
        """Returns the aspect ratio to apply when drawing the pixmap.

        :return: the current aspect ratio
        :rtype: QtCore.AspectRatioMode"""
        return self._pixmapAspectRatioMode

    def setAspectRatioMode(self, aspect):
        """Sets the aspect ratio mode to apply when drawing the pixmap.

        :param pixmap: the new aspect ratio mode
        :type  pixmap: QtCore.AspectRatioMode"""
        self._pixmapAspectRatioMode = aspect
        self._setDirty()
        self.update()

    def resetAspectRatioMode(self):
        """Resets the aspect ratio mode to KeepAspectRatio"""
        self.setAspectRatioMode(self.DefaultAspectRatioMode)

    def getTransformationMode(self):
        """Returns the transformation mode to apply when drawing the pixmap.

        :return: the current transformation mode
        :rtype: QtCore.TransformationMode"""
        return self._pixmapTransformationMode

    def setTransformationMode(self, transformation):
        """Sets the transformation mode to apply when drawing the pixmap.

        :param pixmap: the new transformation mode
        :type  pixmap: QtCore.TransformationMode"""
        self._pixmapTransformationMode = transformation
        self._setDirty()
        self.update()

    def resetTransformationMode(self):
        """Resets the transformation mode to SmoothTransformation"""
        self.setTransformationMode(self.DefaultTransformationMode)

    def getAlignment(self):
        """Returns the alignment to apply when drawing the pixmap.

        :return: the current alignment
        :rtype: QtCore.Alignment"""
        return self._alignment

    def setAlignment(self, alignment):
        """Sets the alignment to apply when drawing the pixmap.

        :param pixmap: the new alignment
        :type  pixmap: QtCore.Alignment"""
        self._alignment = alignment
        self.update()

    def resetAlignment(self):
        """Resets the transformation mode to
        QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter"""
        self.setAlignment(self.DefaultAlignment)

    #: This property holds the widget's pixmap
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`PixmapWidget.getPixmap`
    #:     * :meth:`PixmapWidget.setPixmap`
    #:     * :meth:`PixmapWidget.resetPixmap`
    pixmap = QtCore.Property("QPixmap", getPixmap, setPixmap,
                             resetPixmap, doc="the widget's pixmap")

    #: This property holds the widget's pixmap aspect ratio mode
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`PixmapWidget.getAspectRatioMode`
    #:     * :meth:`PixmapWidget.setAspectRatioMode`
    #:     * :meth:`PixmapWidget.resetAspectRatioMode`
    aspectRatioMode = QtCore.Property("Qt::AspectRatioMode",
                                      getAspectRatioMode, setAspectRatioMode,
                                      resetAspectRatioMode,
                                      doc="the widget's pixmap aspect ratio "\
                                          "mode")

    #: This property holds the widget's pixmap transformation mode
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`PixmapWidget.getTransformationMode`
    #:     * :meth:`PixmapWidget.setTransformationMode`
    #:     * :meth:`PixmapWidget.resetTransformationMode`
    transformationMode = QtCore.Property("Qt::TransformationMode",
                                         getTransformationMode,
                                         setTransformationMode,
                                         resetTransformationMode,
                                         doc="the widget's pixmap "\
                                             "transformation mode")

    #: This property holds the widget's pixmap alignment
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`PixmapWidget.getAlignment`
    #:     * :meth:`PixmapWidget.setAlignment`
    #:     * :meth:`PixmapWidget.resetAlignment`
    alignment = QtCore.Property("Qt::Alignment", getAlignment, setAlignment,
                                resetAlignment,
                                doc="the widget's pixmap alignment")


def main():
    import sys
    import qarbon.config

    app = QtGui.QApplication([])

    M = 2

    class QPixmapWidgetTestPanel(QtGui.QWidget):

        def __init__(self, parent=None):
            QtGui.QWidget.__init__(self, parent)
            panel_l = QtGui.QVBoxLayout()
            self.setLayout(panel_l)
            panel_l.setContentsMargins(M, M, M, M)
            panel_l.setSpacing(M)

            w = PixmapWidget()
            display_panel = QtGui.QGroupBox("Pixmap Widget Display")
            display_l = QtGui.QHBoxLayout()
            display_l.setContentsMargins(M, M, M, M)
            display_l.setSpacing(M)
            display_panel.setLayout(display_l)
            display_l.addWidget(w, 1)

            control_panel = QtGui.QGroupBox("Control Panel")
            control_l = QtGui.QFormLayout()
            control_l.setContentsMargins(M, M, M, M)
            control_l.setSpacing(M)
            control_panel.setLayout(control_l)
            pixmap_widget = QtGui.QLineEdit()
            ratio_widget = QtGui.QComboBox()
            transformation_widget = QtGui.QComboBox()
            halign_widget = QtGui.QComboBox()
            valign_widget = QtGui.QComboBox()
            control_l.addRow("pixmap:", pixmap_widget)
            control_l.addRow("Aspect ratio mode:", ratio_widget)
            control_l.addRow("Transformation mode:", transformation_widget)
            control_l.addRow("Horiz. alignment:", halign_widget)
            control_l.addRow("Vert. alignment:", valign_widget)

            panel_l.addWidget(display_panel, 1)
            panel_l.addWidget(control_panel, 0)

            ratio_widget.addItems(["Ignore", "Keep", "Keep by expanding"])
            transformation_widget.addItems(["Fast", "Smooth"])
            halign_widget.addItem("Left", QtCore.Qt.AlignLeft)
            halign_widget.addItem("Center", QtCore.Qt.AlignHCenter)
            halign_widget.addItem("Right", QtCore.Qt.AlignRight)
            valign_widget.addItem("Top", QtCore.Qt.AlignTop)
            valign_widget.addItem("Center", QtCore.Qt.AlignVCenter)
            valign_widget.addItem("Bottom", QtCore.Qt.AlignBottom)

            pixmap_widget.textChanged.connect(self.changePixmap)
            ratio_widget.currentIndexChanged.connect(self.changeAspectRatio)
            halign_widget.currentIndexChanged.connect(self.changeAlignment)
            valign_widget.currentIndexChanged.connect(self.changeAlignment)

            self.w = w
            self.w_pixmap = pixmap_widget
            self.w_aspect_ratio = ratio_widget
            self.w_transformation = transformation_widget
            self.w_halign = halign_widget
            self.w_valign = valign_widget

            pixmap_widget.setText(qarbon.config.NAMESPACE + \
                                  ":/led/led_red_on.png")
            ratio_widget.setCurrentIndex(1)
            transformation_widget.setCurrentIndex(1)
            halign_widget.setCurrentIndex(0)
            valign_widget.setCurrentIndex(1)

        def changePixmap(self, name):
            self.w.pixmap = QtGui.QPixmap(name)

        def changeAspectRatio(self, i):
            v = QtCore.Qt.IgnoreAspectRatio
            if i == 1:
                v = QtCore.Qt.KeepAspectRatio
            elif i == 2:
                v = QtCore.Qt.KeepAspectRatioByExpanding
            self.w.setAspectRatioMode(v)

        def changeTransformationMode(self, i):
            v = QtCore.Qt.FastTransformation
            if i == 1:
                v = QtCore.Qt.SmoothTransformation
            self.w.setTransformationMode(v)

        def changeAlignment(self, i):
            halign = self.w_halign.itemData(self.w_halign.currentIndex())
            valign = self.w_valign.itemData(self.w_valign.currentIndex())
            self.w.alignment = halign | valign

    panel = QtGui.QWidget()
    layout = QtGui.QGridLayout()
    panel.setLayout(layout)
    layout.setContentsMargins(M, M, M, M)
    layout.setSpacing(M)
    p1 = QPixmapWidgetTestPanel()
    layout.addWidget(p1, 0, 0)
    panel.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
