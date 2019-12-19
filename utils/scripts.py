"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

© Omar Junaid
"""

import os


def ls_in_directory(path):
    for file in os.listdir(path):
        if file.endswith(".py"):
            print(file)
