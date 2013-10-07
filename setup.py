#!/usr/bin/env python
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

from __future__ import print_function

__docformat__ = "restructuredtext"
__package_name__ = 'qarbon'

import os

from distutils.core import setup
from distutils.version import StrictVersion

try:
    import sphinx
    sphinx_version = StrictVersion(sphinx.__version__)
    sphinx_version_min = StrictVersion("1.0.0")
    if sphinx_version < sphinx_version_min:
        sphinx = None
except:
    sphinx = None


def abspath(*path):
    """A method to determine absolute path for a given relative path to the
    directory where this setup.py script is located"""
    setup_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(setup_dir, *path)


def get_release_info():
    name = "release"
    release_dir = abspath(__package_name__)
    import imp
    data = imp.find_module(name, [release_dir])
    return imp.load_module(name, *data)


def get_script_files():
    scripts_dir = abspath('scripts')
    scripts = []
    items = os.listdir(scripts_dir)
    for item in items:
        # avoid hidden files
        if item.startswith("."):
            continue
        abs_item = os.path.join(scripts_dir, item)
        # avoid non files
        if not os.path.isfile(abs_item):
            continue
        # avoid files that have any extension
        if len(os.path.splitext(abs_item)[1]) > 0:
            continue
        # avoid compiled version of script
        if item.endswith('c') and item[:-1] in items:
            continue
        # avoid any core dump... of course there isn't any :-) but just in case
        if item.startswith('core'):
            continue
        scripts.append('scripts/' + item)
    return scripts

if sphinx:
    from sphinx.setup_command import BuildDoc

    class build_doc(BuildDoc):

        def has_doc_api(self):
            return True

        def run(self):
            try:
                BuildDoc.run(self)
            except Exception as e:
                self.warn("Failed to build doc. Reason: %s" % str(e))


def main():
    Release = get_release_info()
    author = Release.authors[0]
    package_name = Release.name

    cmd_class = {}
    if sphinx:
        cmd_class['build_doc'] = build_doc

    setup(name=Release.name,
          version=Release.version,
          description=Release.description,
          long_description=Release.long_description,
          classifiers=Release.classifiers,
          url=Release.url,
          download_url=Release.download_url,
          keywords=Release.keywords,
          author=author[1],
          author_email=author[2],
          maintainer=author[1],
          maintainer_email=author[2],
          packages=[package_name],
          package_dir={package_name: abspath(package_name)},
          package_data={},
          data_files=[],
          scripts=[],
          provides=[package_name],
          requires=[],
          cmdclass=cmd_class)

if __name__ == "__main__":
    main()
