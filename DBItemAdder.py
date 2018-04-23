from OtherFunctionsNonDB import get_file_names_from_folder, read_json_file
import re
from DBConnection import create_connection, close_connection


# TODO: add close_connection
class DBManager:

    def __init__(self):
        self.connection = create_connection()

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

            self.sql_insert_artist("", artist_name, website, artstation, deviantart, "", "")

    def add_used_photos(self):
        used_photos_data = read_json_file(r"C:\Users\Toshiba\Videos\usedPhotos.json")

        for item in used_photos_data:
            photo_name = item["filename"]

            # check if this image is in the database
            check_if_exists = self.sql_check_photo_exists_in_db(photo_name)
            if check_if_exists != 0:
                photo_id = str(self.sql_get_photo_id(photo_name)['PhotoID'])
                # add the id of the photo that was already used in the blog
                self.sql_insert_used_photos(photo_id)

    def sql_insert_used_photos(self, photo_id):
        table_name = "used_photos"
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `"+table_name+"`(`PhotoID`) VALUES ('" + photo_id +"')"
            cursor.execute(sql)
        self.connection.commit()

    def sql_check_photo_exists_in_db(self, photo_name):
        with self.connection.cursor() as cursor:
            sql = "SELECT EXISTS(SELECT `filename` FROM `photos` WHERE `photos`.`filename`='" + photo_name+"')"
            cursor.execute(sql)
            result = cursor.fetchone()
            num_result = result["EXISTS(SELECT `filename` FROM `photos` WHERE `photos`.`filename`='" + photo_name+"')"]

            return num_result

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

    def sql_insert_artist(self, table_name, NameSurname, websiteURL, artstationURL, deviantartURL, InstagramURL, TumblrURL):
        table_name = "artists"
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `"+table_name+"`" \
                "(`ArtistID`, `NameSurname`, `websiteURL`, `artstationURL`, `deviantartURL`, `InstagramURL`, `TumblrURL`)"+\
                  " VALUES (null,'"+NameSurname+"','"+websiteURL+"','"+artstationURL+"','"+deviantartURL+"','"+InstagramURL+"','"+TumblrURL+"')"
            cursor.execute(sql)
        self.connection.commit()

    def sql_get_artists_id(self, name_surname):
        """get the ID of the artist, from artist name"""
        # get artist of the image
        with self.connection.cursor() as cursor:
            sql = "SELECT `ArtistID` FROM `artists` WHERE `NameSurname` = '" + name_surname + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result

    def sql_get_genre_id(self, genre_name):
        """get the ID of the genre, from genre name"""
        with self.connection.cursor() as cursor:
            sql = "SELECT `GenreID` FROM `genres` WHERE `name` = '" + genre_name + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result

    def sql_get_photo_id(self, photo_name):
        """get the ID of the photo, from photo name"""
        with self.connection.cursor() as cursor:
            sql = "SELECT `PhotoID` FROM `photos` WHERE `filename` = '" + photo_name + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result

    def add_photos_assign_artist_and_genre_to_db(self):
        """Adding photos to DB and assigning them to their artists"""
        directory_items = get_file_names_from_folder(r"C:\Users\Toshiba\Pictures\Cyberpunk\space")

        for file_name in directory_items:
            # add photo to DB
            self.sql_insert_photo(file_name)

            # the photo id
            photo_id = self.sql_get_photo_id(file_name)

            # will get everything up to the first underscore of the line
            just_name = re.search("^[^_]+(?=_)", file_name)
            artist_id = self.sql_get_artists_id(just_name[0])

            # TODO: put in manualy genre name
            genre_id = self.sql_get_genre_id("space")

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
            photo_id = self.sql_get_photo_id(file_name)

            # TODO: put in manualy genre name
            genre_id = self.sql_get_genre_id("anime")

            # assign photo to genre
            self.sql_assign_photo_to_genres(str(photo_id['PhotoID']), str(genre_id['GenreID']))
