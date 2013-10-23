# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
# ----------------------------------------------------------------------------
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

"""builds a mock PyQt4 module inside a mock directory relative to the path
of this file"""

from __future__ import with_statement

import os
import sys
import shutil
import inspect

import PyQt4.QtCore

module_init_template = """from __future__ import print_function

{imports}

def _mockf(*args, **kwargs): pass
"""

import_template = """import {name}"""

klass_template = """\
class {klass}({super_klass}):
  pass
{members}
{methods}"""

method_template = """  def {method}(*a,**k): pass"""
function_template = """def {function}(*a,**k): pass"""
member_template = """  {name} = {value!r}"""
constant_template = """{name} = {value!r}"""

FILTER_CLASSES = set(("pyqtWrapperType",))
FILTER_METHODS = set(("exec", "None"))
FILTER_FUNCTIONS = FILTER_METHODS


def abspath(*path):
    """A method to determine absolute path for a given relative path to the
    directory where this .py script is located"""
    this_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(this_dir, *path)


def _import(name):
    __import__(name)
    return sys.modules[name]


def build_class(k):
    k_name = k.__name__
    k_module_name = k.__module__

    super_k = k.__base__
    super_k_name = super_k.__name__
    super_k_module_name = super_k.__module__
    super_k_full_name = ".".join((super_k_module_name, super_k_name))

    if super_k_full_name:
        if super_k_module_name in (k_module_name, "__builtin__"):
            super_name = super_k_name
        else:
            super_name = super_k_full_name
    else:
        super_name = "object"
        super_k = None
        super_k_name = None
        super_k_module_name = None
        super_k_full_name = None

    methods = []
    members = []

    for klass_element_name in dir(k):
        if klass_element_name.startswith("__"):
            continue
        if klass_element_name in FILTER_METHODS:
            continue
        if super_k and hasattr(super_k, klass_element_name):
            continue
        try:
            klass_element = getattr(k, klass_element_name)
        except AttributeError:
            continue
        if inspect.isroutine(klass_element):
            methods.append(method_template.format(method=klass_element_name))
        elif isinstance(klass_element, (int, float, bool, str, unicode)):
            members.append(member_template.format(name=klass_element_name,
                                                  value=klass_element))
    members = "\n".join(members)
    methods = "\n".join(methods)
    
    if super_k_full_name.startswith("sip."):
        super_name = "object"
    klass_str = klass_template.format(klass=k_name,
                                      super_klass=super_name,
                                      methods=methods,
                                      members=members)
 
    if k is PyQt4.QtCore.QObject or not issubclass(k, PyQt4.QtCore.QObject):
        klass_str += "\n  def __init__(self, *args, **kwargs): pass\n"

    return klass_str


def classes(m):
    klasses = set()
    for i in dir(m):
        if i in FILTER_CLASSES:
            continue
        ie = getattr(m, i)
        if inspect.isclass(ie):
            klasses.add(ie)
    return sorted(klasses, key=lambda k: k.mro()[::-1])


def build_module(module_name, imports):

    rel_dir = module_name.split(".")
    abs_dir = abspath("mock", *rel_dir)
    os.makedirs(abs_dir)
    module = _import(module_name)
    fake_module_filename = os.path.join(abs_dir, "__init__.py")

    functions = []
    klasses = []
    constants = []
    for module_element_name in dir(module):
        if module_element_name.startswith("__"):
            continue
        module_element = getattr(module, module_element_name)
        if inspect.isroutine(module_element):
            if module_element_name in FILTER_FUNCTIONS:
                continue
            f_str = function_template.format(function=module_element_name)
            functions.append(f_str)
        elif inspect.isclass(module_element):
            continue
        elif isinstance(module_element, (int, float, bool, str, unicode)):
            constants.append(constant_template.format(name=module_element_name,
                                                      value=module_element))

    for klass in classes(module):
        klasses.append(build_class(klass))

    imports = "\n".join([import_template.format(name=m) for m in imports])

    module_init = module_init_template.format(imports=imports)
    constants = "\n\n".join(constants)
    functions = "\n\n".join(functions)
    klasses = "\n\n".join(klasses)
    with open(fake_module_filename, "w") as f:
        f.write(module_init)
        f.write("\n\n")
        f.write(constants)
        f.write("\n\n")
        f.write(functions)
        f.write("\n\n")
        f.write(klasses)
        f.write("\n\n")


def main():
    shutil.rmtree(abspath("mock"), ignore_errors=True)
    module_names = [("PyQt4", ("sip",)),
                    ("PyQt4.QtCore", ("sip",)),
                    ("PyQt4.QtGui", ("sip", "PyQt4.QtCore",))]
    for module_name, imports in module_names:
        build_module(module_name, imports)

if __name__ == "__main__":
    main()
