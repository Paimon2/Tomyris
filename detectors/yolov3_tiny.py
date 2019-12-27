"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

© Omar Junaid
"""

import sys
import cvlib as cv
import cv2
import logging
from cvlib.object_detection import draw_bbox

logger = logging.getLogger(__name__)

_min_confidence = None


def get_name():
    """REQUIRED function.

    Returns a human-readable string of the detector's name."""
    return "YOLOv3-Tiny object detector"


def get_description():
    """REQUIRED function.

    Returns a human-readable string of the detector's name."""
    return "A faster, more power-efficient but less accurate object detector"


def get_detector_settings():
    """REQUIRED function.

    ../analyser.py will ask this detector what settings can be
    customised. These will be added to the database.

    This must return a List.
    """
    return ["min_confidence"]


def set_local_settings_from_detector():
    global _min_confidence
    _min_confidence = int(database.get_detector_setting("yolov3_tiny",
                                                        "min_confidence"))


def get_objects_of_interest(frame):
    """REQUIRED function.

    There are two options for getting a detector's results:
    Either get_confidence_score() OR get_objects_of_interest()

    get_confidence_score() must return a confidence level from 0.00 to 1.00.
    This represents how confident the detector is that
    something is out of the ordinary.

    get_objects_of_interest() returns a list of tuples, where each object
    is formatted like this:
    (geometry, object_name, object_confidence)
    """
    global _min_confidence
    if _min_confidence is None:  # Ensure _min_confidence != None
        logger.error("Unable to fetch _min_confidence from the database!")
        logger.error("_min_confidence was None!")
        logger.warning("Falling back to default confidence of 0.25.")
        _min_confidence = 0.25
    objects_of_interest = []
    geometry, label, conf = cv.detect_common_objects(frame,
                                                     confidence=_min_confidence,
                                                     model='yolov3-tiny')

    for i in range(len(label)):  # Iterate over every object
        object_tuple = (geometry[i], label[i], conf[i])
        objects_of_interest.append(object_tuple)
    # All objects should be in the list now...
    return objects_of_interest
