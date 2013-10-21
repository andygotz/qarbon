# ----------------------------------------------------------------------------
# This file is part of qarbon (http://qarbon.rtfd.org/)
# ----------------------------------------------------------------------------
# Copyright (c) 2013 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# ----------------------------------------------------------------------------

import sys
import os.path
import optparse

import qarbon
import qarbon.config
from qarbon.external.qt import getQt, QtCore


def env_index(env, env_name):
    env_name = str(env_name)
    for i, e in enumerate(env):
        e = str(e)
        if e.startswith(env_name):
            return i
    return -1


def has_env(env, env_name):
    return env_index(env, env_name) != -1


def get_env(env, env_name):
    env_name = str(env_name)
    for e in env:
        e = str(e)
        if e.startswith(env_name):
            return e.split("=")[1]
    return None


def append_or_create_env(env, env_name, env_value, is_path_like=True):
    i = env_index(env, env_name)
    if i == -1:
        env.append(env_name + "=" + env_value)
    else:
        if is_path_like:
            _, e_v = env[i].split("=")
            paths = e_v.split(os.path.pathsep)
            if not env_value in paths:
                env_value += os.path.pathsep + e_v
        env[i] = env_name + "=" + env_value


def append_or_create_env_list(env, env_name, env_value):
    env_value = os.path.pathsep.join(env_value)
    append_or_create_env(env, env_name, env_value)


def get_qtdesigner_bin():
    designer_bin = str(QtCore.QLibraryInfo.location(
                                    QtCore.QLibraryInfo.BinariesPath))

    plat = sys.platform
    if plat == "darwin":
        designer_bin = os.path.join(designer_bin, "Designer.app", "Contents",
                                    "MacOS")
    elif plat in ("win32", "nt"):
        qt = getQt()
        designer_bin = os.path.abspath(os.path.dirname(qt.__file__))

    designer_bin = os.path.join(designer_bin, "designer")
    return designer_bin


def get_qarbon_designer_path():
    """Returns a list of directories containing qarbon designer plugins"""
    # Set PYQTDESIGNERPATH to look inside qarbon for designer plugins
    path = os.path.dirname(os.path.abspath(qarbon.__file__))
    qt_designer_path = os.path.join(path, 'qt', 'designer')
    return [qt_designer_path]


def qtdesigner_prepare_qarbon(env=None, extra_path=None):

    # Tell Qt Designer where it can find the directory containing the plugins
    if env is None:
        env = QtCore.QProcess.systemEnvironment()

    # Set PYQTDESIGNERPATH to look inside qarbon for designer plugins
    designer_path = get_qarbon_designer_path()

    append_or_create_env_list(env, "PYQTDESIGNERPATH", designer_path)

    # Set QARBONDESIGNERPATH
    if extra_path is not None:
        append_or_create_env(env, "QARBONDESIGNERPATH", extra_path)
        append_or_create_env(env, "PYTHONPATH", extra_path)
    return env


def qtdesigner_start(args, env=None):
    # Start Designer.
    designer_bin = get_qtdesigner_bin()

    designer = QtCore.QProcess()
    designer.setProcessChannelMode(QtCore.QProcess.ForwardedChannels)
    designer.setEnvironment(env)
    designer.start(designer_bin, args)
    designer.waitForFinished(-1)

    return designer.exitCode()


def main(env=None):
    qarbon.config.QT_AUTO_API = False

    version = "qarbon-designer %s" % (qarbon.__version__)
    usage = "Usage: %prog [options] <ui file(s)>"
    description = "The Qt designer application customized for qarbon"
    parser = optparse.OptionParser(version=version, usage=usage,
        description=description)
    parser.add_option("--qarbon-path", dest="qarbonpath", default="",
        help="additional directories to look for qarbon widgets")
    parser.add_option("--qt-designer-path", dest="pyqtdesignerpath",
        default="",
        help="additional directories to look for python qt widgets")

    options, args = parser.parse_args()

    extra_path = None
    # Set QARBONQTDESIGNERPATH
    if len(options.qarbonpath) > 0:
        extra_path = options.qarbonpath

    env = qtdesigner_prepare_qarbon(env=env, extra_path=extra_path)

    sys.exit(qtdesigner_start(args, env=env))


if __name__ == "__main__":
    main()
