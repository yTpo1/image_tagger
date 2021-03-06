import logging


class DBSelectQueries:

    @staticmethod
    def sql_get_photo_name_from_genre_id(connection, genre_id):
        """Returns a list"""
        with connection.cursor() as cursor:
            sql = "SELECT `filename` " + \
                "FROM `photos`" + \
                "WHERE `photos`.`PhotoID` IN (" + \
                "SELECT `PhotoId`" + \
                "FROM `photos_to_genres`" + \
                "WHERE `photos_to_genres`.`GenreID` =" + str(genre_id) + ")"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    @staticmethod
    def sql_get_photo_name_from_artist_id(connection, artist_id):
        """Returns a list"""
        with connection.cursor() as cursor:
            sql = "SELECT `filename` " + \
                "FROM `photos`" + \
                "WHERE `photos`.`PhotoID` IN (" + \
                "SELECT `PhotoId`" + \
                "FROM `photos_to_artists`" + \
                "WHERE `photos_to_artists`.`ArtistID` =" + str(artist_id) + ")"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    @staticmethod
    def sql_get_photo_name_from_file_extension(connection, file_extension):
        """Returns a list"""
        with connection.cursor() as cursor:
            sql = "SELECT `filename` " + \
                "FROM `photos`" + \
                "WHERE `file extension` = '" + file_extension + "'"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    @staticmethod
    def sql_get_artists_id(connection, name_surname):
        """get the ID of the artist, from artist name"""
        # get artist of the image
        with connection.cursor() as cursor:
            sql = "SELECT `ArtistID` FROM `artists` WHERE `NameSurname` = '" + name_surname + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result

    @staticmethod
    def sql_get_genre_id(connection, genre_name):
        """get the ID of the genre, from genre name"""
        with connection.cursor() as cursor:
            sql = "SELECT `GenreID` FROM `genres` WHERE `name` = '" + genre_name + "'"
            try:
                cursor.execute(sql)
                result = cursor.fetchone()
            except Exception as e:
                logging.warning("Exception is :" + str(e) + "\ngenre_name is: " + genre_name)
            else:
                return result

    @staticmethod
    def sql_get_genre_name(connection, genre_id):
        """get the name of the genre, from GenreID"""
        with connection.cursor() as cursor:
            sql = "SELECT `name` FROM `genres` WHERE `GenreID` = '" + genre_id + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result

    @staticmethod
    def sql_get_photo_id(connection, photo_name):
        """get the ID of the photo, from photo name"""
        with connection.cursor() as cursor:
            # When error: photo_name into log
            sql = "SELECT `PhotoID` FROM `photos` WHERE `filename` = '" + str(photo_name) + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result

    @staticmethod
    def sql_check_artist_exists_in_db(connection, artist_name):
        with connection.cursor() as cursor:
            sql = "SELECT EXISTS(SELECT `NameSurname` FROM `artists` WHERE `artists`.`NameSurname`='" + artist_name + "')"
            cursor.execute(sql)
            result = cursor.fetchone()
            # num_result will be a number. result is a dictionary object
            num_result = result["EXISTS(SELECT `NameSurname` FROM `artists` WHERE `artists`.`NameSurname`='" + artist_name + "')"]

            return num_result

    @staticmethod
    def sql_check_photo_exists_in_db(connection, photo_name):
        with connection.cursor() as cursor:
            sql = "SELECT EXISTS(SELECT `filename` FROM `photos` WHERE `photos`.`filename`='" + photo_name+"')"
            cursor.execute(sql)
            result = cursor.fetchone()
            num_result = result["EXISTS(SELECT `filename` FROM `photos` WHERE `photos`.`filename`='" + photo_name+"')"]

            return num_result

    @staticmethod
    def sql_get_all_genres(connection):
        with connection.cursor() as cursor:
            sql = "SELECT name from genres"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result