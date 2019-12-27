"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

© Omar Junaid
"""

import wget
import logging

logger = logging.getLogger(__name__)


def download_file(path, url):
    """Download a single file using the requests library.

    @param path An absolute directory of where to save the file
    @param url The url from which to download

    The file name will be set as per what was specified
    in path."""
    wget.download(url, path)
