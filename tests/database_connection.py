import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import database


class TestDatabaseFunctionality(unittest.TestCase):

    def test_connection(self):
        database.disconnect()
        self.assertEqual(database.connect(), 0)

    def test_already_connected(self):
        database.disconnect()
        self.assertEqual(database.connect(), 0)
        self.assertEqual(database.connect(), 2)

if __name__ == '__main__':
    unittest.main()
