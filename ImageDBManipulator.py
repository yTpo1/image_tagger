from DBSelectQueries import DBSelectQueries as DS
from DBItemAdder import DBItemAdder as DA
from FileUtils import copy_image, get_file_names_from_folder
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

    def assign_current_photos_to_genre(self, genre_id):
        connection = create_connection()

        images = get_file_names_from_folder(r"C:\Users\Toshiba\Videos\images_queried")

        for item in images:
            photo_id = DS.sql_get_photo_id(connection, item)['PhotoID']
            DA.sql_assign_photo_to_genres(connection, photo_id, genre_id)

        close_connection(connection)

    # Folder name - genre, all photos in folder add to that genre


# lol = ImageManipulator()
# lol.assign_current_photos_to_genre(9000)