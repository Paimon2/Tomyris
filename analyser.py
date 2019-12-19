"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

© Omar Junaid
"""

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
