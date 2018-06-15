from DBSelectQueries import DBSelectQueries as DBSel
from FileUtils import get_file_names_from_folder, read_json_file
import re
import logging


class DBItemAdder:

    @staticmethod
    def sql_insert_used_photos(connection, photo_id):
        table_name = "used_photos"
        with connection.cursor() as cursor:
            sql = "INSERT INTO `"+table_name+"`(`PhotoID`) VALUES ('" + str(photo_id) + "')"
            cursor.execute(sql)
        connection.commit()

    @staticmethod
    def sql_insert_photo(connection, filename, file_extension, description):
        with connection.cursor() as cursor:
            sql = "INSERT INTO `photos`(`PhotoID`, `filename`, `file extension`, `description`)" + \
                  "VALUES (null,'"+filename+"','"+file_extension

            if description is None:
                sql = sql + "', null )"
            else:
                sql = sql + "','" + description + " ')"

            try:
                cursor.execute(sql)
            except Exception as e:
                logging.warning("Exception is :" + str(e) + "\n"+filename+"\n"+file_extension+"\n"+description)

        connection.commit()

    @staticmethod
    def sql_assign_photo_to_artist(connection, photo_id, artist_id):
        table_name = "photos_to_artists"
        with connection.cursor() as cursor:
            sql = "INSERT INTO `" + table_name + "`(`PhotoID`, `ArtistID`)" + \
                  " VALUES ('"+str(photo_id)+"','" + str(artist_id) + "')"
            cursor.execute(sql)
        connection.commit()

    @staticmethod
    def sql_assign_photo_to_genres(connection, photo_id, genre_id):
        table_name = "photos_to_genres"
        with connection.cursor() as cursor:
            sql = "INSERT INTO `" + table_name + "`(`PhotoID`, `GenreID`)" + \
                  " VALUES ('"+str(photo_id)+"','" + str(genre_id) + "')"
            cursor.execute(sql)
        connection.commit()

    @staticmethod
    def sql_insert_artist(connection, NameSurname, websiteURL, artstationURL, deviantartURL, InstagramURL, TumblrURL):
        table_name = "artists"
        with connection.cursor() as cursor:
            sql = "INSERT INTO `"+table_name+"`" \
                "(`ArtistID`, `NameSurname`, `websiteURL`, `artstationURL`, `deviantartURL`, `InstagramURL`, `TumblrURL`)"+\
                  " VALUES (null,'"+NameSurname+"','"+websiteURL+"','"+artstationURL+"','"+deviantartURL+"','"+InstagramURL+"','"+TumblrURL+"')"
            cursor.execute(sql)
        connection.commit()

    # def add_photos_assign_artist_and_genre_to_db(self):
    #     """Adding photos to DB and assigning them to their artists"""
    #     directory_items = get_file_names_from_folder(r"C:\Users\Toshiba\Pictures\Cyberpunk\space")
    #
    #     for file_name in directory_items:
    #         # add photo to DB
    #         self.sql_insert_photo(file_name)
    #
    #         # the photo id
    #         photo_id = DBSel.sql_get_photo_id(self.connection, file_name)
    #
    #         # will get everything up to the first underscore of the line
    #         just_name = re.search("^[^_]+(?=_)", file_name)
    #         artist_id = DBSel.sql_get_artists_id(self.connection, just_name[0])
    #
    #         # TODO: put in manualy genre name
    #         genre_id = DBSel.sql_get_genre_id(self.connection, "space")
    #
    #         # assign photo to artist
    #         self.sql_assign_photo_to_artist(str(photo_id['PhotoID']), str(artist_id['ArtistID']))
    #
    #         # assign photo to genre
    #         self.sql_assign_photo_to_genres(str(photo_id['PhotoID']), str(genre_id['GenreID']))
    #
    # def add_photos_anime_genre_to_db(self):
    #     """Adding photos to DB and assigning them to their artists"""
    #     directory_items = get_file_names_from_folder(r"C:\Users\Toshiba\Pictures\Cyberpunk\anime")
    #
    #     for file_name in directory_items:
    #         # add photo to DB
    #         self.sql_insert_photo(file_name)
    #
    #         # the photo id
    #         photo_id = DBSel.sql_get_photo_id(self.connection, file_name)
    #
    #         # TODO: put in manualy genre name
    #         genre_id = DBSel.sql_get_genre_id(self.connection, "anime")
    #
    #         # assign photo to genre
    #         self.sql_assign_photo_to_genres(str(photo_id['PhotoID']), str(genre_id['GenreID']))
    #
    # def add_artists_to_db_from_json(self):
    #     artists_data = read_json_file(r"C:\Users\Toshiba\Videos\artists.json")
    #
    #     for item in artists_data:
    #         artist_name = item["Name"]
    #
    #         if item["website"]:
    #             website = item["website"]
    #         else:
    #             website = ''
    #
    #         if item["artstation"]:
    #             artstation = item["artstation"]
    #         else:
    #             artstation = ''
    #
    #         if item["deviantart"]:
    #             deviantart = item["deviantart"]
    #         else:
    #             deviantart = ''
    #
    #         self.sql_insert_artist(artist_name, website, artstation, deviantart, "", "")
    #
    # def add_used_photos(self):
    #     used_photos_data = read_json_file(r"C:\Users\Toshiba\Videos\usedPhotos.json")
    #
    #     for item in used_photos_data:
    #         photo_name = item["filename"]
    #
    #         # check if this image is in the database
    #         check_if_exists = DBSel.sql_check_photo_exists_in_db(self.connection, photo_name)
    #         if check_if_exists != 0:
    #             photo_id = str(DBSel.sql_get_photo_id(self.connection, photo_name)['PhotoID'])
    #             # add the id of the photo that was already used in the blog
    #             self.sql_insert_used_photos(photo_id)