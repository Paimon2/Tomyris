"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

© Omar Junaid
"""

import sys
import cvlib as cv
import cv2
from cvlib.object_detection import draw_bbox


def get_objects_of_interest(frame):
    """REQUIRED function.

    There are two options for getting a detector's results:
    Either get_confidence_score() OR get_objects_of_interest()

    get_confidence_score() must return a confidence level from 0.00 to 1.00.
    This represents how confident the detector is that
    something is out of the ordinary.

    get_objects_of_interest() returns a list of tuples, where each object
    is formatted like this:
    (object_name, object_type, object_confidence)
    """
    objects_of_interest = []
    _, label, conf = cv.detect_common_objects(frame,
                                              confidence=0.2,
                                              model='yolov3-tiny')

    for i in range(len(label)):  # Iterate over every object
        object_tuple = (label(i), "object", conf(i))
        objects_of_interest.append(object_tuple)
    # All objects should be in the list now...
    return objects_of_interest
