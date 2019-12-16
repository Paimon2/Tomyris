"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

© Omar Junaid
"""

import logging
import pymysql
import configparser

logger = logging.getLogger(__name__)

_cursor = None
_db = None

_config = None


def load_config():
    """Load the configuration file,
    which contains database information.

    The config.txt file should not be accessible to modules
    outside of database.py.
    """
    global _config
    if not _config:
        logger.debug("Loading configuration file.")
        _config = configparser.ConfigParser()
        _config.read("config.txt")


def connect():
    """Connects to the database using info specified in config.txt.

    Return codes:
    0 = success
    1 = failure (likely invalid credentials)
    2 = already connected
    """
    global _db
    if not _db:
        try:
            _db = pymysql.connect(host=_config["Database"]["Host"],
                                  port=int(_config["Database"]["Port"]),
                                  user=_config["Database"]["User"],
                                  passwd=_config["Database"]["Password"],
                                  db=_config["Database"]["Name"],
                                  autocommit=True,
                                  cursorclass=pymysql.cursors.DictCursor)

        except pymysql.err.OperationalError as e:
            logger.critical("Unable to connect to the database!")
            logger.critical(e)
            return 1
        return 0  # Connection successful
    return 2  # Already connected (_db != None)


def disconnect():
    """ "Disconnect" from the database.
    This can be run even if we are not connected anyway.
    """
    global _db
    _db = None
    _cursor = None


def get_cur():
    """Returns the database cursor.

    This method reads the config.txt file to get the
    database information. If _cursor is None, a connection
    to the database is established. Then, the cursor is returned.
    """
    global _cursor
    if not _cursor:
        connect()
    _cursor = _db.cursor()
    return _cursor


def get_db():
    """Returns the database object from PyMySQL.

    There should only be one connection at a time,
    which should be taken care of.
    """
    global _db
    if not _db:
        connect()
    return _db


load_config()
