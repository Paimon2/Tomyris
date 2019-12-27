"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

© Omar Junaid
"""

import os


def ls_in_directory(path):
    """List all scripts (.py files) in a directory.

    This returns a List object (you guessed it).
    Just pass the path."""
    scripts_list = []
    for file in os.listdir(path):
        if file.endswith(".py"):
            temp_file = file.replace(".py", "")
            scripts_list.append(temp_file)
    return scripts_list


def get_path():
    """Get the path to the current file."""
    return os.path.dirname(os.path.realpath(__file__)) + os.sep
