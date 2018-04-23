from DBSelectQueries import DBSelectQueries as DS
from ImageUtils import copy_image
from DBConnection import *


class ImageManipulator:

    def get_images_of_genre(self, genre_id):
        """Copies images of selected genre to folder"""
        connection = create_connection()
        photos_names_list_ = DS.sql_get_photo_name_from_genre_id(connection, genre_id)
        close_connection(connection)

        for item in photos_names_list_:
            photo_name = item['filename']
            copy_image(photo_name)

