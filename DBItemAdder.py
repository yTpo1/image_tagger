from DBSelectQueries import DBSelectQueries as DBSel
from OtherFunctionsNonDB import get_file_names_from_folder, read_json_file
import re
from DBConnection import create_connection, close_connection


class DBManager:

    def __init__(self):
        self.connection = create_connection()

    def close_connection(self):
        """Remember to call this function after working with DB"""
        close_connection(self.connection)

    def add_artists_to_db_from_json(self):
        artists_data = read_json_file(r"C:\Users\Toshiba\Videos\artists.json")

        for item in artists_data:
            artist_name = item["Name"]

            if item["website"]:
                website = item["website"]
            else:
                website = ''

            if item["artstation"]:
                artstation = item["artstation"]
            else:
                artstation = ''

            if item["deviantart"]:
                deviantart = item["deviantart"]
            else:
                deviantart = ''

            self.sql_insert_artist(artist_name, website, artstation, deviantart, "", "")

    def add_used_photos(self):
        used_photos_data = read_json_file(r"C:\Users\Toshiba\Videos\usedPhotos.json")

        for item in used_photos_data:
            photo_name = item["filename"]

            # check if this image is in the database
            check_if_exists = DBSel.sql_check_photo_exists_in_db(self.connection, photo_name)
            if check_if_exists != 0:
                photo_id = str(DBSel.sql_get_photo_id(self.connection, photo_name)['PhotoID'])
                # add the id of the photo that was already used in the blog
                self.sql_insert_used_photos(photo_id)

    def sql_insert_used_photos(self, photo_id):
        table_name = "used_photos"
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `"+table_name+"`(`PhotoID`) VALUES ('" + photo_id +"')"
            cursor.execute(sql)
        self.connection.commit()

    def sql_insert_photo(self, filename):
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `" + "photos" + "`(`PhotoID`, `filename`) VALUES (null,'"+filename+"')"
                cursor.execute(sql)
            self.connection.commit()

    def sql_assign_photo_to_artist(self, photo_id, artist_id):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `" + "photos_to_artists" + "`(`PhotoID`, `ArtistID`) VALUES ('"+photo_id+"','" + artist_id + "')"
            cursor.execute(sql)
        self.connection.commit()

    def sql_assign_photo_to_genres(self, photo_id, genre_id):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `" + "photos_to_genres" + "`(`PhotoID`, `GenreID`) VALUES ('"+photo_id+"','" + genre_id + "')"
            cursor.execute(sql)
        self.connection.commit()

    def sql_insert_artist(self, NameSurname, websiteURL, artstationURL, deviantartURL, InstagramURL, TumblrURL):
        table_name = "artists"
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `"+table_name+"`" \
                "(`ArtistID`, `NameSurname`, `websiteURL`, `artstationURL`, `deviantartURL`, `InstagramURL`, `TumblrURL`)"+\
                  " VALUES (null,'"+NameSurname+"','"+websiteURL+"','"+artstationURL+"','"+deviantartURL+"','"+InstagramURL+"','"+TumblrURL+"')"
            cursor.execute(sql)
        self.connection.commit()

    def add_photos_assign_artist_and_genre_to_db(self):
        """Adding photos to DB and assigning them to their artists"""
        directory_items = get_file_names_from_folder(r"C:\Users\Toshiba\Pictures\Cyberpunk\space")

        for file_name in directory_items:
            # add photo to DB
            self.sql_insert_photo(file_name)

            # the photo id
            photo_id = DBSel.sql_get_photo_id(self.connection, file_name)

            # will get everything up to the first underscore of the line
            just_name = re.search("^[^_]+(?=_)", file_name)
            artist_id = DBSel.sql_get_artists_id(self.connection, just_name[0])

            # TODO: put in manualy genre name
            genre_id = DBSel.sql_get_genre_id(self.connection, "space")

            # assign photo to artist
            self.sql_assign_photo_to_artist(str(photo_id['PhotoID']), str(artist_id['ArtistID']))

            # assign photo to genre
            self.sql_assign_photo_to_genres(str(photo_id['PhotoID']), str(genre_id['GenreID']))

    def add_photos_anime_genre_to_db(self):
        """Adding photos to DB and assigning them to their artists"""
        directory_items = get_file_names_from_folder(r"C:\Users\Toshiba\Pictures\Cyberpunk\anime")

        for file_name in directory_items:
            # add photo to DB
            self.sql_insert_photo(file_name)

            # the photo id
            photo_id = DBSel.sql_get_photo_id(self.connection, file_name)

            # TODO: put in manualy genre name
            genre_id = DBSel.sql_get_genre_id(self.connection, "anime")

            # assign photo to genre
            self.sql_assign_photo_to_genres(str(photo_id['PhotoID']), str(genre_id['GenreID']))
