"""
The source code below consists of collated and modified snippets from:
https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/
"""

import time
import numpy as np
import imutils
import sys
import os
import cv2
import datetime
import imutils

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import database

min_contour_area = 0


def get_detector_settings():
    """REQUIRED function.

    ../analyser.py will ask this detector what settings can be
    customised. These will be added to the database.

    This must return a List.
    """
    return ["min_contour_area"]


def set_local_settings_from_detector():
    min_contour_area = int(database.get_detector_setting("motion",
                                                         "min_contour_area"))


def preprocess_frame(frame):
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    return gray


def get_confidence_score(prev, curr):
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
    prev = preprocess_frame(prev)
    curr = preprocess_frame(curr)
    # Compute the diff between prev and curr
    frame_delta = cv2.absdiff(prev, curr)
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
    # dilate the thresholded image to fill in holes, then find contours
    # on thresholded image
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c) < min_contour_area:
            continue
        return 1  # Always return max value; motion can't be expressed a %?
    return 0  # No contours with min contour size
