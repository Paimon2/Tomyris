import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import cv2
from detectors import yolov3_tiny

def get_path():
    return os.path.dirname(os.path.realpath(__file__)) + os.sep

class TestDatabaseFunctionality(unittest.TestCase):

    def test_cars(self):
        frame = cv2.imread(get_path() + "cars1.png")
        objs = yolov3_tiny.get_objects_of_interest(frame)
        self.assertGreater(len(objs), 4)

    def test_people(self):
        frame = cv2.imread(get_path() + "people1.png")
        objs = yolov3_tiny.get_objects_of_interest(frame)
        self.assertGreater(len(objs), 16)


if __name__ == '__main__':
    unittest.main()
