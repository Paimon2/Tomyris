"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

© Omar Junaid
"""

from os import path
import sys
import logging.config

logging.config.fileConfig("logging.conf")

import database


def init_tomyris():
    # Connect to the database
    database.connect()


init_tomyris()
