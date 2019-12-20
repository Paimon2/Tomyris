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
        logger.info("Connected to the database successfully.")
        return 0  # Connection successful
    logger.warn("Already connected to the database; 2nd connection attempted?")
    return 2  # Already connected (_db != None)


def disconnect():
    """"Disconnect" from the database.
    This can be run even if we are not connected anyway.
    """
    logger.info("Disconnecting from the database!")
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


def table_exists(table_name):
    """Does a table exist?
    No, literally. That's it.
    True if it does, False if it doesn't.
    """
    try:
        _cursor.execute("SELECT 1 FROM " + table_name + " LIMIT 1;")
    except pymysql.err.ProgrammingError:
        return False
    return True


def create_table(name, params):
    """Create a table with the parameters specified.

    Brackets must be included in the parameters."""
    logger.info("Creating table " + name + "!")
    _cursor.execute('CREATE TABLE ' + name + ' ' + params + ';')


def delete_table(name):
    """Deletes the table with the specified name.
    Simple as that.
    """
    logger.info("Deleting table " + name + "!")
    _cursor.execute('DROP TABLE ' + name + ' ;')


def create_detectors_table():
    """Creates the detector_settings table.

    Will silently fail if table already exists.

    We don't really need a table to represent detectors.
    (Detectors will just be loaded from the detectors/ directory.)
    We just represent their settings instead, including whether
    they are currently enabled or not.
    """
    if table_exists("detector_settings"):
        logger.warning("detector_settings already exists!")
        logger.warning("That table will not be created again.")
        return
    create_table("detector_settings",
                 "(name varchar(64),"
                 "value varchar(128),"
                 "enabled tinyint)")


def create_entry_for_detector(name, setting, value):
    """Creates an entry for a detector in the detector_settings table.

    name (str): The name of the detector (without the .py extension, of course)
    setting (str): The name of the setting that can be changed
    By default, the enabled value (int) will always be set to 1.
    This can be changed with tomyrisctl.
    """
    _cursor.execute("INSERT INTO detector_settings (name, value, enabled)"
                    "VALUES ('%s', '%s', %s,)",
                    (name, setting, value))


def get_detector_setting(detector_name, setting):
    """Fetch a specified setting from the detector_settings table.

    An example of what the table would look like is below.

    ||||||TABLE: detector_settings|||||||
    | name   |  setting         | value | enabled
    |--------|------------------|-------|---------|
    | motion | min_contour_size | "40"  |    1
    |--------|------------------|-------|---------|
    | ex1    | ex_setting_1     | "260" |    0    |
    |--------|------------------|-------|---------|
    | ex2    | ex_setting_2     | "hi"  |    1    |
    |--------|------------------|-------|---------|"""
    _cursor.execute("SELECT value FROM detector_settings WHERE name = '%s'"
                    "AND setting = '%s';",
                    (detector_name, setting))
    return _cursor.fetchone()["value"]


def set_detector_setting(detector_name, setting, value):
    """Set a specified setting from the detector_settings table.

    NOTE: ALL THREE parameters (detector_name, setting and value)
    MUST BE strs.
   
    An example of what the table would look like is below.

    ||||||TABLE: detector_settings|||||||
    | name   |  setting         | value | enabled
    |--------|------------------|-------|---------|
    | motion | min_contour_size | "40"  |    1
    |--------|------------------|-------|---------|
    | ex1    | ex_setting_1     | "260" |    0    |
    |--------|------------------|-------|---------|
    | ex2    | ex_setting_2     | "hi"  |    1    |
    |--------|------------------|-------|---------|"""
    _cursor.execute("UPDATE detector_settings"
                    "SET setting = '%s', value = '%s'"
                    "WHERE name = '%s';",
                    (detector_name, setting, value))


load_config()
