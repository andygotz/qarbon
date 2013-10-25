# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
#
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""Meta information for qarbon."""

__all__ = ["DataAccess", "DataType", "State"]

import sys

from qarbon.external.enum import Enum
from qarbon.util import isString

_PY3 = sys.version_info[0] > 2

class DataAccess(Enum):
    """Data access enum"""

    ReadOnly, ReadWithWrite, WriteOnly, ReadWrite, _Invalid = range(5)


class DataType(Enum):
    """Data type enum"""

    Integer, Float, String, Boolean, State, Enumeration, \
      Binary, _Invalid = range(8)

    #: dictionary dict<data type, :class:`DataType`>
    __DTYPE_MAP = { 
        'int':         Integer,
        'integer':     Integer,
        int:           Integer,
        'long':        Integer,
        Integer:       Integer,
        'float':       Float,
        'double':      Float,
        float:         Float,
        Float:         Float,
        'str':         String,
        'string':      String,
        str:           String,
        String:        String,
        'bool':        Boolean,
        'boolean':     Boolean,
        bool:          Boolean,
        Boolean:       Boolean,
        'state':       State,
        State:         State,
        'enum':        Enumeration,
        'enumeration': Enumeration,
        Enumeration:   Enumeration,
        'bin':         Binary,
        'binary':      Binary,
        'bytes':       Binary,
        Binary:        Binary,
    }
    
    if _PY3:
        __DTYPE_MAP[bytes] = Binary
    else:
        __DTYPE_MAP[long] = Integer
    
    __PYTYPE_MAP = {
        Integer:     int,
        Float:       float,
        String:      str,
        Boolean:     bool,
        State:       State,
        Enumeration: Enum,
        Binary:      bytes
    }

    @staticmethod
    def toPythonType(dtype):
        """Convert from DataType to python type"""
        dtype = DataType.toDataType(dtype)
        return DataType.__PYTYPE_MAP[dtype]

    @staticmethod
    def toDataType(dtype):
        """Convert from type to DataType"""
        if isString(dtype):
            dtype = dtype.lower()
        return DataType.__DTYPE_MAP[dtype]


class State(Enum):
    """State enum"""
    # On, Moving, Fault, Alarm, Unknown, _Invalid = range(6)

    On, Off, Close, Open, Insert, Extract, Moving, Standby, Fault, Init, \
    Running, Alarm, Disable, Unknown, Disconnected, _Invalid = range(16)
