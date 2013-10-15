# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
# ----------------------------------------------------------------------------
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""meta information for qarbon 4"""

from qarbon.external.enum import Enum


class DataAccess(Enum):
    """Data access enum"""

    ReadOnly, ReadWithWrite, WriteOnly, ReadWrite, _Invalid = range(5)


class DataType(Enum):
    """Data type enum"""

    Integer, Float, String, Boolean, State, Binary, _Invalid = range(7)

    _type_map = {Integer: int, Float: float, String: str, Boolean: bool,
                 State: int, Binary: bytes}

    @staticmethod
    def to_python_type(py_type):
        """Convert from python type to DataType"""
        return DataType._type_map[py_type]


class State(Enum):
    """State enum"""
    # On, Moving, Fault, Alarm, Unknown, _Invalid = range(6)

    On, Off, Close, Open, Insert, Extract, Moving, Standby, Fault, Init, \
    Running, Alarm, Disable, Unknown, Disconnected, _Invalid = range(16)


__all__ = ["DataAccess", "DataType", "State"]
