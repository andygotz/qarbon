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

"""helper functions"""

__all__ = ['isString', 'isSequence']

import collections

__str_klasses = [str]
__seq_klasses = [collections.Sequence, bytearray]

# some versions of python don't have unicode (python [3.0, 3.3])
try:
    unicode
    __str_klasses.append(unicode)
except:
    pass

# some versions of python don't have basestring (python [3.0, inf[)
try:
    basestring
    __str_klasses.insert(0, basestring)
except:
    pass

__str_klasses = tuple(__str_klasses)
__seq_klasses = tuple(__seq_klasses)


def isString(obj):
    return isinstance(obj, __str_klasses)


def isSequence(obj, inc_string=False):
    if inc_string:
        return isinstance(obj, __seq_klasses)
    else:
        return isinstance(obj, __seq_klasses) and not isString(obj)
