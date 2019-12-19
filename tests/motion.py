import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import cv2
from detectors import motion


def get_path():
    return os.path.dirname(os.path.realpath(__file__)) + os.sep


class TestMotionDetectorFunctionality(unittest.TestCase):

    def test_motion_detector(self):
        one = cv2.imread(get_path() + "motion1.png")
        two = cv2.imread(get_path() + "motion2.png")
        result = motion.get_confidence_score(one, two)
        self.assertEqual(result, 1)

    def test_no_motion(self):
        one = cv2.imread(get_path() + "motion1.png")
        two = cv2.imread(get_path() + "motion1.png")
        result = motion.get_confidence_score(one, two)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
