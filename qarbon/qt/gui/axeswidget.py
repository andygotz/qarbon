#------------------------------------------------------------------------------
# This file is part of Framework4, a graphical toolkit to build beamline
# applications
#
# http://forge.epn-campus.eu/projects/framework4
#
# Copyright 2013
#           European Synchrotron Radiation Facility,
#           BP 220, Grenoble 38043, FRANCE
#
# Framework4 is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Framework is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Framework.  If not, see <http://www.gnu.org/licenses/>.
#------------------------------------------------------------------------------

"""Multiple axis (axes) widget."""

__all__ = ["Axis", "AxesWidget"]

import weakref

from qarbon.meta import State
from qarbon.color import getCSSColorFromState
from qarbon.external.enum import Enum
from qarbon.external.qt import QtCore, QtGui
from qarbon.qt.gui.icon import Icon
from qarbon.qt.gui.groupbox import GroupBox


# TODO: implement ?1?!
def getStatusBar():
    return


class Column(Enum):
    Label, Position, Icon, Steps, StepLeft, StepRight, Stop = range(7)


class PositionColumn(Enum):
    Read, Write, ReadWrite = range(3)


__height_hint = None


def get_height_hint():
    """Little trick to get a uniform height hint between all widgets"""
    global __height_hint
    if __height_hint is None:
        h1 = QtGui.QComboBox().sizeHint().height()
        h2 = QtGui.QLineEdit().sizeHint().height()
        h3 = QtGui.QDoubleSpinBox().sizeHint().height()
        h4 = QtGui.QPushButton().sizeHint().height()
        __height_hint = min(h1, h2, h3, h4)
    return __height_hint

__minimum_height_hint = None


def get_minimum_height_hint():
    """Little trick to get a uniform height hint between all widgets"""
    global __minimum_height_hint
    if __minimum_height_hint is None:
        h1 = QtGui.QComboBox().minimumSizeHint().height()
        h2 = QtGui.QLineEdit().minimumSizeHint().height()
        h3 = QtGui.QDoubleSpinBox().minimumSizeHint().height()
        h4 = QtGui.QPushButton().minimumSizeHint().height()
        __minimum_height_hint = min(h1, h2, h3, h4)
    return __minimum_height_hint


class DisplayLabel(QtGui.QLabel):

    StyleT = "DisplayLabel {border-width:1px; border-radius: 4px; %s}"

    UnmodifiedStyle = StyleT % "border-style:transparent;"

    ModifiedStyle = StyleT % "border-style:solid; border-color: blue;"

    def __init__(self, axis, parent=None):
        super(DisplayLabel, self).__init__(parent)
        self.setStyleSheet(self.UnmodifiedStyle)
        self.axis = axis

    def setValue(self, value):
        if value is None:
            value = ""
        else:
            value += ":"
        self.setText(value)

    def setModified(self, yesno):
        if yesno:
            s = "font-weight: bold; text-decoration: underline"
            s = self.ModifiedStyle
        else:
            s = ""
            s = self.UnmodifiedStyle

        self.setStyleSheet(s)

    def contextMenuEvent(self, event):
        menu = QtGui.QMenu(self)
        refreshAction = QtGui.QAction(Icon("view-refresh"), "Refresh", self)
        refreshAction.triggered.connect(self.axis.refresh)
        menu.addAction(refreshAction)
        menu.popup(event.globalPos())


class ValueLabel(QtGui.QLabel):

    def __init__(self, axis, parent=None):
        super(DisplayLabel, self).__init__(parent)
        self.axis = axis

    def setValue(self, value):
        if value is None:
            value = ""
        self.setText(value)


class ValueSpinBox(QtGui.QDoubleSpinBox):

    SpinStyleT = 'ValueSpinBox {font-family: "Monospace"; %s}'

    # : value applied signal
    # :
    # : emitted when the spinbox enter/return key is pressed
    valueApplied = QtCore.Signal()

    def __init__(self, axis, parent=None):
        super(ValueSpinBox, self).__init__(parent)
        self.axis = axis
        self.setAccelerated(True)
        # self.setButtonSymbols(self.PlusMinus)
        # self.setFrame(False)
        self.setDecimals(3)
        self.setMinimum(float("-inf"))
        self.setMaximum(float("+inf"))
        self.setAlignment(QtCore.Qt.AlignLeft)
        self.setStyleSheet(self.SpinStyleT % "")

    def setValue(self, value, emit=True):
        if value is None:
            value = float('nan')
        if emit:
            return super(ValueSpinBox, self).setValue(value)

        blocked = self.signalsBlocked()
        try:
            self.blockSignals(True)
            result = super(ValueSpinBox, self).setValue(value)
        finally:
            self.blockSignals(blocked)
        return result

    def setUnit(self, unit):
        if unit is None or not len(unit):
            unit = ""
        elif not unit.startswith(" "):
            unit = " " + unit
        self.setSuffix(unit)

    def setState(self, state):
        if state is None:
            state = State._Invalid
        styleSheet = getCSSColorFromState(state)
        self.setStyleSheet(self.SpinStyleT % styleSheet)

    def setSingleStep(self, value):
        if value is None:
            return
        return super(ValueSpinBox, self).setSingleStep(value)

    def setMinimum(self, value):
        if value is None:
            value = float('-inf')
        return super(ValueSpinBox, self).setMinimum(value)

    def setMaximum(self, value):
        if value is None:
            value = float('+inf')
        return super(ValueSpinBox, self).setMaximum(value)

    def sizeHint(self):
        size = super(ValueSpinBox, self).sizeHint()
        size.setHeight(get_height_hint())
        return size

    def minimumSizeHint(self):
        size = super(ValueSpinBox, self).minimumSizeHint()
        size = QtCore.QSize(size.width(), get_minimum_height_hint())
        return size

    def keyPressEvent(self, event):
        key = event.key()
        if key in (QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return):
            self.valueApplied.emit()
        elif key == QtCore.Qt.Key_Escape:
            self.axis.refresh()
        elif key == QtCore.Qt.Key_F5:
            self.axis.refresh()
        else:
            return super(ValueSpinBox, self).keyPressEvent(event)


class StepSize(QtGui.QComboBox):

    def __init__(self, axis, parent=None):
        super(StepSize, self).__init__(parent)
        self.axis = axis

    def addSteps(self, steps):
        icon = Icon(":/controls/step2.png")
        for step_label, step_value in steps:
            self.addItem(icon, step_label, step_value)

    def setSteps(self, steps):
        self.clear()
        if steps is None:
            steps = []
        self.addSteps(steps)

    def setCurrentStep(self, step):
        index = self.findData(step, QtCore.Qt.UserRole)
        self.setCurrentIndex(index)

    def sizeHint(self):
        size = super(StepSize, self).sizeHint()
        size = QtCore.QSize(size.width(), get_height_hint())
        return size

    def minimumSizeHint(self):
        size = super(StepSize, self).minimumSizeHint()
        size = QtCore.QSize(size.width(), get_minimum_height_hint())
        return size


class IconButton(QtGui.QPushButton):

    def __init__(self, axis, icon=None, parent=None):
        super(IconButton, self).__init__(parent)
        self.axis = axis
        if icon is not None:
            self.setIcon(icon)
        self.setIconSize(QtCore.QSize(16, 16))


class SquareButton(IconButton):

    def __init__(self, axis, icon=None, parent=None):
        super(SquareButton, self).__init__(axis, icon=icon, parent=parent)
        self.axis = axis

    def sizeHint(self):
        h = get_height_hint()
        return QtCore.QSize(h, h)

    def minimumSizeHint(self):
        h = get_minimum_height_hint()
        return QtCore.QSize(h, h)


class StepLeftButton(SquareButton):

    def __init__(self, axis, parent=None):
        # media-skip-backward
        # media-seek-backward
        # go-previous
        # edit-undo
        # fwk4:/backward.png
        # fwk4:/1leftarrow.png
        icon = Icon("edit-undo")
        super(StepLeftButton, self).__init__(axis, icon=icon,
                                             parent=parent)


class StepRightButton(SquareButton):

    def __init__(self, axis, parent=None):
        # media-skip-forward
        # media-seek-forward
        # go-next
        # edit-redo
        # fwk4:/forward.png
        # fwk4:/1rightarrow.png
        icon = Icon("edit-redo")
        super(StepRightButton, self).__init__(axis, icon=icon,
                                              parent=parent)


class StopButton(SquareButton):

    def __init__(self, axis, parent=None):
        # media-playback-stop
        # process-stop
        icon = Icon("process-stop")
        super(StopButton, self).__init__(axis, icon=icon, parent=parent)


class Axis(QtCore.QObject):

    # : position changed signal
    # :
    # : emitted when the axis position has changed
    # : the signal is emitted with the axis name and position value
    positionChanged = QtCore.Signal(str, float)

    # : position changed signal
    # :
    # : emitted when the axis minimum allowed position has changed
    # : the signal is emitted with the axis name and minimum position value
    limitsChanged = QtCore.Signal(str, list)

    # : step sizes changed signal
    # :
    # : emitted when the allowed axis step sizes has changed
    # : the signal is emitted with the axis name and step sizes
    stepsChanged = QtCore.Signal(str, object)

    # : current step changed signal
    # :
    # : emitted when the current step size has changed
    # : the signal is emitted with the axis name and current step size
    currentStepChanged = QtCore.Signal(str, float)

    # : state changed signal
    # :
    # : emitted when the axis state has changed
    # : the signal is emitted with the axis name, old state and new state
    stateChanged = QtCore.Signal(str, object, object)

    # : label changed signal
    # :
    # : emitted when the axis label has changed
    # : the signal is emitted with the axis name and label value
    labelChanged = QtCore.Signal(str, str)

    # : units changed signal
    # :
    # : emitted when the axis units has changed
    # : the signal is emitted with the axis name and units value
    unitChanged = QtCore.Signal(str, str)

    def __init__(self, axis_info, axes, parent=None):
        super(Axis, self).__init__(parent)
        self._axes = weakref.ref(axes)
        self.name = axis_info['name']
        self.index = axis_info['index']
        self.role = axis_info.get('role', str(self.index))
        self._label = axis_info.get('username', self.name)

        self._position = None  # float('nan')
        self._limits = None  # float('-inf'), float('+inf')
        self._state = None
        self._steps = None
        self._current_step = None
        self._unit = None

    @property
    def axes(self):
        return self._axes()

    def refresh(self):
        self.state = self.getState(cache=False)
        self.limits = self.getLimits(cache=False)
        self.position = self.getPosition(cache=False)

    def getPosition(self, cache=True):
        if cache and self._position is not None:
            result = self._position
        else:
            self._position = result = self.axes.position(self.name)
        return result

    def setPosition(self, position, emit=True):
        self._position = position
        if emit:
            self.positionChanged.emit(self.name, position)

    #: This property contains the axis position
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`Axis.getPosition`
    #:     * :meth:`Axis.setPosition`
    position = QtCore.Property(str, getPosition, setPosition)

    def getLimits(self, cache=True):
        if cache and self._limits is not None:
            result = self._limits
        else:
            self._limits = result = list(self.axes.limits(self.name))
        return result

    def setLimits(self, limits, emit=True):
        self._limits = list(limits)
        if emit:
            self.limitsChanged.emit(self.name, limits)

    #: This property contains the axis limits
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`Axis.getLimits`
    #:     * :meth:`Axis.setLimits`
    limits = QtCore.Property(list, getLimits, setLimits)

    def getState(self, cache=True):
        if cache and self._state is not None:
            result = self._state
        else:
            self._state = result = self.axes.state(self.name)
        return result

    def setState(self, state, emit=True):
        old_state = self._state
        if state is None:
            state = State._Invalid
        self._state = state
        if emit:
            self.stateChanged.emit(self.name, old_state, state)

    #: This property contains the axis state
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`Axis.getState`
    #:     * :meth:`Axis.setState`
    state = QtCore.Property(object, getState, setState)

    def getLabel(self):
        return self._label

    def setLabel(self, label, emit=True):
        if label is None:
            label = ""
        self._label = label
        if emit:
            self.labelChanged.emit(self.name, label)

    #: This property contains the axis label
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`Axis.getLabel`
    #:     * :meth:`Axis.setLabel`
    label = QtCore.Property(str, getLabel, setLabel)

    def getSteps(self):
        return self._steps

    def setSteps(self, steps, emit=True):
        if steps is None:
            steps = []
        self._steps = steps
        if emit:
            self.stepsChanged.emit(self.name, steps)

    #: This property contains the axis steps
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`Axis.getSteps`
    #:     * :meth:`Axis.setSteps`
    steps = QtCore.Property(str, getSteps, setSteps)

    def getCurrentStep(self):
        return self._current_step

    def setCurrentStep(self, current_step, emit=True):
        self._current_step = current_step
        if emit:
            self.currentStepChanged.emit(self.name, current_step)

    #: This property contains the axis current step size
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`Axis.getCurrentStep`
    #:     * :meth:`Axis.setCurrentStep`
    currentStep = QtCore.Property(float, getCurrentStep, setCurrentStep)

    def getUnit(self):
        return self._unit

    def setUnit(self, unit, emit=True):
        if unit is None:
            unit = ""
        self._unit = unit
        if emit:
            self.unitChanged.emit(self.name, unit)

    #: This property contains the axis unit
    #:
    #: **Access functions:**
    #:
    #:     * :meth:`Axis.getUnit`
    #:     * :meth:`Axis.setUnit`
    unit = QtCore.Property(float, getUnit, setUnit)

    def move(self, absolute_position):
        self.axes.move(self.name, absolute_position)

    def moveRelative(self, relative_position):
        self.move(self.position + relative_position)

    def moveUp(self):
        self.moveRelative(+self.currentStep)

    def moveDown(self):
        self.moveRelative(-self.currentStep)

    stepUp = moveUp
    stepDown = moveDown

    def stop(self):
        self.axes.abort(self.name)

    ToolTipTemplate = """<html>axis <u>{axis.label}</u> is in 
<b>{axis.state.name}</b> state, at position <b>{axis.position}</b><br/>
Limits set to <b>[{axis.limits[0]}, {axis.limits[1]}]</b><br/>
(the hardware name for this axis is: <i>{axis.name}</i>)"""

    def toolTip(self):
        return self.ToolTipTemplate.format(axis=self)


class AxesWidget(GroupBox):
    """A multiple axis widget."""
    DefaultUpdateStatusBar = True

    def __init__(self, title=None, axes=None, parent=None):
        super(AxesWidget, self).__init__(parent)
        self._axes = {}
        contentWidget = QtGui.QWidget()
        layout = QtGui.QGridLayout()
        layout.setColumnStretch(Column.Position.value, 1)
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(2)
        contentWidget.setLayout(layout)
        self.setContent(contentWidget)
        self.setTitle(title)
        self.setTitleIcon(Icon(":/objects/motor.png"))
        self.setAxes(axes)
        self.resetUpdateStatusBar()

    def axes(self):
        return self._axes

    def setAxes(self, axes):
        for axis_id in self._axes:
            self.removeAxisID(axis_id)

        if axes is None:
            return

        for axis in axes:
            self.addAxis(axis)

    def addAxis(self, axis):
        self._axes[axis.name] = axis
        self.__buildAxisGUI(axis)
        axis.positionChanged.connect(self.onAxisPositionChanged)
        axis.stateChanged.connect(self.onAxisStateChanged)
        axis.labelChanged.connect(self.onAxisLabelChanged)
        axis.stepsChanged.connect(self.onAxisStepsChanged)
        axis.currentStepChanged.connect(self.onAxisCurrentStepChanged)
        axis.limitsChanged.connect(self.onAxisLimitsChanged)
        axis.unitChanged.connect(self.onAxisUnitChanged)

    def removeAxisID(self, axis_id):
        self.removeAxis(self.getAxis(axis_id))

    def removeAxis(self, axis):
        axis.positionChanged.disconnect(self.onAxisPositionChanged)
        axis.stateChanged.disconnect(self.onAxisStateChanged)
        axis.labelChanged.disconnect(self.onAxisLabelChanged)
        axis.stepsChanged.disconnect(self.onAxisStepsChanged)
        axis.currentStepChanged.disconnect(self.onAxisCurrentStepChanged)
        axis.limitsChanged.disconnect(self.onAxisLimitsChanged)
        axis.unitChanged.disconnect(self.onAxisUnitChanged)

        layout = self.content().layout()
        for role in Column:
            w = self.axisColumnWidget(axis, role)
            layout.removeWidget(w)
            w.setParent(None)
        self._axes.pop(axis.id)

    def getAxis(self, name):
        return self._axes[name]

    def getAxisByRole(self, role):
        for axis in self._axes.values():
            if axis.role == role:
                return axis
        raise KeyError(role)

    def __buildAxisGUI(self, axis):
        row = axis.index
        layout = self.content().layout()

        # create widgets
        label_widget = DisplayLabel(axis)
        position_widget = ValueSpinBox(axis)
        icon_widget = QtGui.QLabel()
        steps_widget = StepSize(axis)
        step_left_widget = StepLeftButton(axis)
        step_right_widget = StepRightButton(axis)
        stop_widget = StopButton(axis)

        # add widgets to container
        layout.addWidget(label_widget, row, Column.Label.value)
        layout.addWidget(position_widget, row, Column.Position.value)
        layout.addWidget(icon_widget, row, Column.Icon.value)
        layout.addWidget(steps_widget, row, Column.Steps.value)
        layout.addWidget(step_left_widget, row, Column.StepLeft.value)
        layout.addWidget(step_right_widget, row, Column.StepRight.value)
        layout.addWidget(stop_widget, row, Column.Stop.value)

        # initialize values
        label_widget.setValue(axis.label)

        position_widget.setValue(axis.position)
        position_widget.setState(axis.state)
        position_widget.setRange(*axis.limits)
        position_widget.setSingleStep(axis.currentStep)
        position_widget.setUnit(axis.unit)

        steps_widget.setSteps(axis.steps)
        steps_widget.setCurrentStep(axis.currentStep)

        # set buddy
        label_widget.setBuddy(position_widget)

        icon_widget.hide()

        # connect signals
        steps_widget.activated.connect(self.onUserCurrentStepsChanged)
        position_widget.valueApplied.connect(self.onUserPositionApplied)
        position_widget.valueChanged.connect(self.onUserPositionChanged)
        step_left_widget.clicked.connect(self.onUserStepLeft)
        step_right_widget.clicked.connect(self.onUserStepRight)
        stop_widget.clicked.connect(self.onUserStop)

        # initialize enable/disable and tooltips
        self.__updateAxis(axis)

    def axisColumnWidget(self, axis, role):
        layout = self.content().layout()
        return layout.itemAtPosition(axis.index, role.value).widget()

    def axisIDColumnWidget(self, name, role):
        return self.axisColumnWidget(self.getAxis(name), role)

    def setAxisColumnVisible(self, axis, role, show=True):
        self.axisColumnWidget(axis, role).setVisible(show)

    def setAxisIDColumnVisible(self, name, role, show=True):
        self.setAxisColumnVisible(self.getAxis(name), role, show=show)

    def setColumnVisible(self, role, show=True):
        for axis in self._axes.values():
            self.setAxisColumnVisible(axis, role, show=show)

    def __updateAxis(self, axis):
        state = axis.state
        position = axis.position
        step = axis.currentStep
        min_value, max_value = axis.limits

        label_widget = self.axisColumnWidget(axis, Column.Label)
        position_widget = self.axisColumnWidget(axis, Column.Position)
        steps_widget = self.axisColumnWidget(axis, Column.Steps)
        step_left_widget = self.axisColumnWidget(axis, Column.StepLeft)
        step_right_widget = self.axisColumnWidget(axis, Column.StepRight)
        stop_widget = self.axisColumnWidget(axis, Column.Stop)

        if state is State.Moving:
            position_widget.setEnabled(False)
            step_left_widget.setEnabled(False)
            step_right_widget.setEnabled(False)
            label_widget.setModified(False)
        else:
            position_widget.setEnabled(True)
            step_left_widget.setEnabled((position - step) >= min_value)
            step_right_widget.setEnabled((position + step) <= max_value)
            label_widget.setModified(position_widget.value() != position)

        toolTip = axis.toolTip()
        label_widget.setToolTip(toolTip)
        position_widget.setToolTip(toolTip)
        steps_widget.setToolTip(toolTip)
        step_left_widget.setToolTip(toolTip)
        step_right_widget.setToolTip(toolTip)
        stop_widget.setToolTip(toolTip)

    def refreshAxes(self):
        for axis in self.axes().values():
            axis.refresh()

    #
    # slots to react on user interaction
    #

    def onUserPositionApplied(self):
        widget = self.sender()
        axis = widget.axis
        position = widget.value()
        label = self.axisColumnWidget(axis, Column.Label)
        label.setModified(False)
        axis.move(position)

    def onUserPositionChanged(self, value):
        widget = self.sender()
        axis = widget.axis
        label_w = self.axisColumnWidget(axis, Column.Label)
        label_w.setModified(widget.value() != axis.position)

    def onUserCurrentStepsChanged(self, index):
        widget = self.sender()
        step = widget.itemData(index)
        axis = widget.axis
        axis.currentStep = step

        position_widget = self.axisColumnWidget(axis, Column.Position)
        position_widget.setSingleStep(step)

        self.__updateAxis(axis)

    def onUserStepLeft(self):
        widget = self.sender()
        axis = widget.axis
        axis.stepDown()

    def onUserStepRight(self):
        widget = self.sender()
        axis = widget.axis
        axis.stepUp()

    def onUserStop(self):
        widget = self.sender()
        axis = widget.axis
        axis.stop()

    #
    # axis has changed programatically through a signal coming from the model
    #

    def onAxisPositionChanged(self, name, position):
        axis = self.getAxis(name)
        position_widget = self.axisColumnWidget(axis, Column.Position)
        position_widget.setValue(position, emit=False)
        self.__updateAxis(axis)

    def onAxisStateChanged(self, name, old_state, state):
        axis = self.getAxis(name)
        position_widget = self.axisColumnWidget(axis, Column.Position)
        position_widget.setState(state)
        if self.updateStatusBar and old_state != state:
            icon = Icon(state)
            message = axis.label + " "
            if state == State.Moving:
                message += "started to move..."
            elif old_state == State.Moving:
                message += "stopped!"
            else:
                message += "changed from {0} to {1}".format(old_state.name,
                                                            state.name)
            self.__setStatus(message, icon)
        self.__updateAxis(axis)

    def onAxisLabelChanged(self, name, label):
        axis = self.getAxis(name)
        label_widget = self.axisColumnWidget(axis, Column.Label)
        label_widget.setValue(label)

    def onAxisStepsChanged(self, name, steps):
        axis = self.getAxis(name)
        steps_widget = self.axisColumnWidget(axis, Column.Steps)
        steps_widget.setSteps(steps)
        self.__updateAxis(axis)

    def onAxisCurrentStepChanged(self, name, step):
        """Steps changed from the Axis model:
        - change the current step value on the combo box
        - change the step size on the position spin box
        - update (enable/disable the stepLeft and stepRight buttons according
          to the current axis limits)
        """
        axis = self.getAxis(name)
        steps_widget = self.axisColumnWidget(axis, Column.Steps)
        position_widget = self.axisColumnWidget(axis, Column.Position)
        steps_widget.setCurrentStep(step)
        position_widget.setSingleStep(step)
        self.__updateAxis(axis)

    def onAxisLimitsChanged(self, name, limits):
        axis = self.getAxis(name)
        position_widget = self.axisColumnWidget(axis, Column.Position)
        if limits is None:
            limits = [float("-inf"), float("+inf")]
        position_widget.setRange(*limits)
        self.__updateAxis(axis)

    def onAxisUnitChanged(self, name, unit):
        axis = self.getAxis(name)
        position_widget = self.axisColumnWidget(axis, Column.Position)
        position_widget.setUnit(unit)
        self.__updateAxis(axis)

    def __setStatus(self, message, icon=QtGui.QStyle.SP_MessageBoxInformation):
        if not self.updateStatusBar:
            return
        statusBar = getStatusBar(self)
        if statusBar is None:
            return
        if hasattr(statusBar, 'setStatus'):
            statusBar.setStatus(message, icon)
        else:
            statusBar.showMessage(message)

    def setUpdateStatusBar(self, update):
        self.__updateStatusBar = update

    def getUdpateStatusBar(self):
        return self.__updateStatusBar

    def resetUpdateStatusBar(self):
        self.setUpdateStatusBar(self.DefaultUpdateStatusBar)

    #: This property sets if the widget should update stauts bar with messages
    #:
    #: **Access functions:**
    #:
    #: * :meth:`AxesWidget.getUdpateStatusBar`
    #: * :meth:`AxesWidget.setUpdateStatusBar`
    #: * :meth:`AxesWidget.resetUpdateStatusBar`
    updateStatusBar = QtCore.Property(bool, getUdpateStatusBar,
                                      setUpdateStatusBar, resetUpdateStatusBar)


def main():
    from qarbon.qt.gui.application import Application
    app = Application()

    class Axes(object):
        axes = {}

        def get(self, name):
            if not name in self.axes:
                self.axes[name] = [State.On, 0, [-10, 10]]
            return self.axes[name]

        def state(self, name):
            return self.get(name)[0]

        def position(self, name):
            return self.get(name)[1]

        def limits(self, name):
            return self.get(name)[2]

        def move(self, name, v):
            self.get(name)[1] = v

    p = QtGui.QWidget()
    layout = QtGui.QVBoxLayout()
    p.setLayout(layout)

    axes = Axes()
    axes_list = []
    for i in range(16):
        name = "axis%02d" % i
        label = "Axis %02d" % i
        info = dict(name=name, label=label, role=str(i), index=i)
        axis = Axis(info, axes)
        axis.steps = [["1 um", 0.001], ["10 um", 0.01], ["1 mm", 1]]
        axis.currentStep = 0.01
        axis.unit = "mm"
        axis.state = State(i)
        axes_list.append(axis)

    axis_w1 = AxesWidget(axes=axes_list)
    axis_w1.title = "First axes"
    layout.addWidget(axis_w1)

    axes_list[0].setLabel("Bla")
    # simulate motor at 5.4
    axes.move("axis00", 5.4)
    axes_list[0].setPosition(5.4)

    axis_w2 = AxesWidget(axes=axes_list[:5])
    axis_w2.title = "Second axes"
    layout.addWidget(axis_w2)
    layout.addStretch(1)
    p.show()

    app.exec_()

if __name__ == "__main__":
    main()
