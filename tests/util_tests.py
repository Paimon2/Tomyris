import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from utils import scripts


def get_path():
    return os.path.dirname(os.path.realpath(__file__)) + os.sep


class TestUtilities(unittest.TestCase):

    def test_py_files_in_folder(self):
        self.assertGreater(len(scripts.ls_in_directory("tests")), 2)


if __name__ == '__main__':
    unittest.main()
