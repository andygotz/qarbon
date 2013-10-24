# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
# ----------------------------------------------------------------------------
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""Release data for the qarbon project.

It contains the following members:

    - version : (str) version string
    - description : (str) brief description
    - long_description : (str) a long description
    - license : (str) license
    - authors : (seq<seq<str,str,str>>) the list of authors
    - url : (str) the project url
    - download_url : (str) the project download url
    - keywords : list<str> list of keywords
    - classifiers : list<str> list of applicable classifiers"""

#: Name of the package for release purposes.  This is the name which labels
#: the tarballs and RPMs made by distutils, so it's best to lowercase it.
name = 'qarbon'

#: For versions with substrings (like 0.6.16.svn), use an extra . to separate
#: the new substring. We have to avoid using either dashes or underscores,
#: because bdist_rpm does not accept dashes (an RPM) convention, and
#: bdist_deb does not accept underscores (a Debian convention).
version_info = (0, 1, 0, 'dev', 0)
version = '.'.join(map(str, version_info[:3]))

#: revision number
revision = str(version_info[4])

#: package description
description = \
"""python library of Qt widgets."""

#: long description
long_description = \
"""Qarbon is a python library of Qt widgets."""

#: license
license = 'GNU Lesser General Public License v3 or later (LGPLv3+)'

#: authors
authors = [('Tiago', 'Tiago Coutinho', 'coutinho@esrf.fr')]

#: package URL
url = 'http://%s.rtfd.org/' % name

#: download URL
download_url = 'http://pypi.python.org/pypi/qarbon/'

#: keywords
keywords = ['Python', 'Qt']

#: package classifiers
classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: ' + license,
    'Operating System :: Microsoft :: Windows',
    'Operating System :: Microsoft :: Windows :: Windows 95/98/2000',
    'Operating System :: Microsoft :: Windows :: Windows XP',
    'Operating System :: Microsoft :: Windows :: Windows 7',
    'Operating System :: MacOS',
    'Operating System :: POSIX',
    'Operating System :: POSIX :: Linux',
    'Operating System :: Unix',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries',
]

#: external requirements
requirements = [
]
