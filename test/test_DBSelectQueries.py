import unittest
from DBSelectQueries import DBSelectQueries as D
from DBConnection import create_connection, close_connection

class Test_DBSelectQueries(unittest.TestCase):

    def test_sql_get_photo_id_and_name_from_genre_id(self):

        connection = create_connection()
        print(type(D.sql_get_photo_id_and_name_from_genre_id(connection, 9)))

        # self.assertEqual(D.sql_get_photo_id_and_name_from_genre_id(9), ['yeah'])