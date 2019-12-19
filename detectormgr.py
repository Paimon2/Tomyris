"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

© Omar Junaid
"""
import importlib
import os
import sys
import hashlib
import database
from utils.scripts import ls_in_directory

_detectors = None


def does_detector_fn_exist(detector_name, function_name):
    """Does a function in a detector exist?

    This can also be used for other files.
    NOTE: Arguments MUST be checked for validity.
    This only checks if a specified function exists.
    Nothing less, nothing more."""
    try:
        return callable(getattr(detector_name, function_name))
    except AttributeError:
        return False


def add_detector_to_database(name, params):
    if database.table_exists(name):  # Just in case!
        database.delete_table(name)


def get_detectors_path_name():
    return os.sep + "detectors" + os.sep


def get_detectors_path():
    return os.path.dirname(os.path.abspath(__file__)) + get_detectors_path_name()


def import_detectors():
    """Iterate over all files in detectors dir and import them.

    The way we do this is by adding each script to the _detectors dictionary,
    where the key is the detector name and the value is the imported script,
    which can be used inside the file.
    """
    global _detectors
    _detectors = {}
    for detector in ls_in_directory(get_detectors_path()):
        _detectors[detector] = importlib.import_module("detectors." + detector)


def setup_detectors():
    pass


def get_detectors():
    return _detectors


import_detectors()
# setup_detectors()


