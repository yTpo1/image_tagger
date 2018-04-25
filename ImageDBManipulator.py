from DBSelectQueries import DBSelectQueries as DS
from DBItemAdder import DBItemAdder as DA
from FileUtils import copy_image, get_file_names_from_folder, get_file_extension
from DBConnection import *
import re


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

    def add_photos_to_db(self):
        connection = create_connection()

        directory_items = get_file_names_from_folder(r"C:\Users\Toshiba\Videos\images_queried")

        for file_name in directory_items:
            # add photo to DB
            file_extension = get_file_extension(file_name)
            DA.sql_insert_photo(connection, file_name, file_extension, 'null')

        close_connection(connection)

    def add_photos_assign_artist_and_genre_to_db(self, genre):
        """Adding photos to DB and assigning them to their artists"""
        connection = create_connection()

        directory_items = get_file_names_from_folder(r"C:\Users\Toshiba\Videos\images_queried")

        for file_name in directory_items:
            # add photo to DB
            file_extension = get_file_extension(file_name)
            DA.sql_insert_photo(connection, file_name, file_extension, 'null')

            # the photo id
            photo_id = DS.sql_get_photo_id(connection, file_name)

            # will get everything up to the first underscore of the line
            just_name = re.search("^[^_]+(?=_)", file_name)
            artist_id = DS.sql_get_artists_id(connection, just_name[0])

            # TODO: put in manualy genre name
            genre_id = DS.sql_get_genre_id(connection, genre)

            # assign photo to artist
            DA.sql_assign_photo_to_artist(connection, str(photo_id['PhotoID']), str(artist_id['ArtistID']))

            # assign photo to genre
            DA.sql_assign_photo_to_genres(connection, str(photo_id['PhotoID']), str(genre_id['GenreID']))

        close_connection(connection)