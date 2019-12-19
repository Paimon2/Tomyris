"""
The source code below consists of collated and modified snippets from:
https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/
"""

"""
--START DETECTOR SETTINGS--

Modify the values below to as you see fit.
"""


min_contour_area = 40  # Minimum area of contour to classify as high-confidence

# --END DETECTOR SETTINGS--

import time
import numpy as np
import imutils
import cv2
import datetime
import imutils
import cv2


def preprocess_frame(frame):
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    return gray


def get_confidence_score(prev, curr):
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
