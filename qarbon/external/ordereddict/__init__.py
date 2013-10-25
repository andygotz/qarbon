# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
#
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------


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
