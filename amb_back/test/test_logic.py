import unittest
from settings.connector import DB_connection


class TestLogic(unittest.TestCase):
    def test_test(self):
        self.assertEqual(2, 2)

    def test_db_connection(self):
        cnx = DB_connection()
        self.assertIsNotNone(cnx)
        cnx.close()
