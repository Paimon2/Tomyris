"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

© Omar Junaid
"""

import logging
import sys
import os
import cv2

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import scripts
from utils import downloader

logger = logging.getLogger(__name__)

_min_confidence = None
_net = None

classes = ["background", "aeroplane", "bicycle",
           "bird", "boat", "bottle",
           "bus", "car", "cat",
           "chair", "cow", "diningtable",
           "dog", "horse", "motorbike",
           "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]


def download_files():
    """Download files that are required by the
    MobileNet-SSD detector."""
    # Download the caffemodel, followed by the prototxt
    downloader.download_file(scripts.get_path() + "MobileNetSSD.caffemodel",
                             "https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/mobilenet_iter_73000.caffemodel")
    downloader.download_file(scripts.get_path() + "MobileNetSSD.prototxt",
                             "https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/voc/MobileNetSSD_deploy.prototxt")


def initial_setup():
    """REQUIRED function.

    Set up anything for first-time use.
    If you do not wish to use this function, include it but don't do anything."""
    # We can assume both files are missing if one is not present
    if not os.path.isfile(scripts.get_path() + "MobileNetSSD.prototxt"):
        download_files()


def get_name():
    """REQUIRED function.

    Returns a human-readable string of the detector's name."""
    return "MobileNet SSD object detector"


def get_description():
    """REQUIRED function.

    Returns a human-readable string of the detector's name."""
    return "An object detector with a balance between accuracy and performance"


def get_detector_settings():
    """REQUIRED function.

    ../analyser.py will ask this detector what settings can be
    customised. These will be added to the database.

    This must return a List.
    """
    return ["min_confidence"]


def set_local_settings_from_detector():
    global _min_confidence
    _min_confidence = int(database.get_detector_setting("mobilenet_ssd",
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
    global _net
    if _net is None:
        _net = cv2.dnn.readNetFromCaffe(scripts.get_path()
                                        + "MobileNetSSD.prototxt",
                                        scripts.get_path()
                                        + "MobileNetSSD.caffemodel")
    (h, w) = frame.shape[:2]
    # Construct a blob for our frame
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)),
                                 0.007843,
                                 (300, 300),
                                 127.5)
    _net.setInput(blob)
    objects_of_interest = []
    # Get the detections from the neural network
    detections = net.forward()
    # TLDR: For each detection
    for i in np.arange(0, detections.shape[2]):
        # Get detection data
        confidence = detections[0, 0, i, 2]
        identifier = int(detections[0, 0, i, 1])
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        """
        Now append our tuple!
        Remember (see above):
        (geometry, object_name, object_confidence)
        """
        objects_of_interest.append((box, classes[identifier], confidence))
    return objects_of_interest
