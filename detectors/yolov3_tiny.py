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
    bbox, label, conf = cv.detect_common_objects(frame, confidence=0.2, model='yolov3-tiny')
    print(bbox, label, conf)

    # draw bounding box over detected objects
    out = draw_bbox(frame, bbox, label, conf, write_conf=True)

    # display output
    cv2.imshow("Real-time object detection", out)
    # press "Q" to stop
    cv2.waitKey(1000000)
