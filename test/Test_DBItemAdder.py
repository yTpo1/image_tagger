import unittest
from DBItemAdder import DBManager


class Test_DBItemAdder(unittest.TestCase):

    def test_sql_check_photo_exists_in_db_true(self):
        """Item that exists in the database"""
        obj = DBManager()
        data = obj.sql_check_photo_exists_in_db("Mad Dog Jones_03.jpg")
        self.assertEqual(data, 1)

    def test_sql_check_photo_exists_in_db_false(self):
        """Item that doesn't exists in the database"""
        obj = DBManager()
        data = obj.sql_check_photo_exists_in_db("Mad Dog Jones_0344.jpg")
        self.assertEqual(data, 0)
