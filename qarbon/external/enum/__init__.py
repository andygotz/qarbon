# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
# ----------------------------------------------------------------------------
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------


try:
    # enum from python 3.4 or from enum34 installed package?
    from enum import *
except ImportError:
    # enum from local import
    import warnings
    warnings.warn("enum not available. Using local enum", ImportWarning)
    from ._enum import *
    del warnings
