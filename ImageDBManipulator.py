from DBSelectQueries import DBSelectQueries as DS
from DBItemAdder import DBItemAdder as DA
from FileUtils import copy_image, get_file_names_from_folder, get_file_extension, check_cyrillic, move_file
from DBConnection import *
import re
import tkinter.messagebox


class ImageManipulator:

    def get_images_of_genre(self, genre_name):
        """Copies images of selected genre to folder"""
        connection = create_connection()
        genre_id = DS.sql_get_genre_id(connection, genre_name)['GenreID']
        # print(genre_id)
        photos_names_list = DS.sql_get_photo_name_from_genre_id(connection, genre_id)

        close_connection(connection)

        for item in photos_names_list:
            photo_name = item['filename']
            copy_image(photo_name)

    def get_images_of_artist_name(self, artist_name):
        """Copies images of selected genre to folder"""
        connection = create_connection()

        artist_photos = DS.sql_check_artist_exists_in_db(connection, artist_name)

        if artist_photos > 0:
            artist_id = DS.sql_get_artists_id(connection, artist_name)['ArtistID']

            photos_names_list_ = DS.sql_get_photo_name_from_artist_id(connection, artist_id)
        else:
            tkinter.messagebox.showinfo('Error', "Attention! No such artist!")

        close_connection(connection)

        if artist_photos > 0:
            for item in photos_names_list_:
                photo_name = item['filename']
                copy_image(photo_name)

    def get_images_of_file_extension(self, file_extension):
        """Copies images of selected genre to folder"""
        connection = create_connection()
        photos_names_list_ = DS.sql_get_photo_name_from_file_extension(connection, file_extension)
        close_connection(connection)

        for item in photos_names_list_:
            photo_name = item['filename']
            copy_image(photo_name)

    def assign_current_photos_to_genre(self, genre_name):
        connection = create_connection()

        genre_id = DS.sql_get_genre_id(connection, genre_name)['GenreID']
        images = get_file_names_from_folder(r"C:\Users\Toshiba\Videos\images_queried")

        n_img_assigned = 0
        n_img_not_added = 0
        for item in images:
            # check if item exists
            n_photo_is_in_db = DS.sql_check_photo_exists_in_db(connection, item)

            if n_photo_is_in_db > 0:
                photo_id = DS.sql_get_photo_id(connection, item)['PhotoID']
                DA.sql_assign_photo_to_genres(connection, photo_id, genre_id)
                n_img_assigned = n_img_assigned + 1
            else:
                # if does not exist move it to a different folder
                move_file(item)
                n_img_not_added = n_img_not_added + 1

        close_connection(connection)
        if n_img_not_added == 0:
            tkinter.messagebox.showinfo('Success', "Number of images: " + str(n_img_assigned) + ". Assigned to genre: " + genre_name)
        else:
            tkinter.messagebox.showinfo('Attention!', "Number of images: " + str(n_img_not_added) + " not added.|| "+ str(n_img_assigned)+ " added.")

    def assign_current_photos_to_artist(self, artist_name):
        connection = create_connection()

        n_img_added = 0

        artist_photos = DS.sql_check_artist_exists_in_db(connection, artist_name)
        print(artist_photos)

        if artist_photos > 0:
            images = get_file_names_from_folder(r"C:\Users\Toshiba\Videos\images_queried")

            for item in images:
                photo_id = DS.sql_get_photo_id(connection, item)['PhotoID']
                artist_id = DS.sql_get_artists_id(connection, artist_name)['ArtistID']
                DA.sql_assign_photo_to_artist(connection, photo_id, artist_id)

            tkinter.messagebox.showinfo('Success', "Number of images assinged: "+str(n_img_added)+" Artist: "+artist_name)
        else:
            tkinter.messagebox.showinfo('Error', "Attention! No such artist!")

        close_connection(connection)

    def add_photos_to_db(self):
        directory_items = get_file_names_from_folder(r"C:\Users\Toshiba\Videos\images_queried")

        connection = create_connection()
        n_img_not_added = 0
        n_img_added = 0

        for file_name in directory_items:
            # check if filename contains Cyrillic characters
            check = check_cyrillic(file_name)

            if check is False:
                # add photo to DB
                file_extension = get_file_extension(file_name)

                DA.sql_insert_photo(connection, file_name, file_extension, None)
                n_img_added = n_img_added + 1
            else:
                # Move file to a different folder
                move_file(file_name)
                n_img_not_added = n_img_not_added + 1

        close_connection(connection)
        if n_img_not_added > 0:
            tkinter.messagebox.showinfo('Attention!', "Image(s)" + str(n_img_not_added) + " Not added!! Check in folder 'files_not_added'")
        else:
            tkinter.messagebox.showinfo('Success', "Number of images added: " + str(n_img_added))

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