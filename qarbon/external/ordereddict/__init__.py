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

__docformat__ = "restructuredtext"

try:
    # ordereddict from python 2.7 or from ordereddict installed package?
    import ordereddict as __ordereddict
    from ordereddict import *
except ImportError:
    import warnings
    warnings.warn("ordereddict not available. Using local ordereddict",
                  ImportWarning)
    # ordereddict from local import
    import _ordereddict as __ordereddict
    from ._ordereddict import *
    del warnings
