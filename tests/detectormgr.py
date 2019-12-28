import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import detectormgr


def get_path():
    return os.path.dirname(os.path.realpath(__file__)) + os.sep


class TestDetectorManagerFunctionality(unittest.TestCase):

    def test_setup(self):
        detectormgr.setup_detectors()

if __name__ == '__main__':
    unittest.main()
