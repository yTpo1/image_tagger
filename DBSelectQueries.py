

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
            cursor.execute(sql)
            result = cursor.fetchone()
            return result

    @staticmethod
    def sql_get_photo_id(connection, photo_name):
        """get the ID of the photo, from photo name"""
        with connection.cursor() as cursor:
            sql = "SELECT `PhotoID` FROM `photos` WHERE `filename` = '" + photo_name + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result

    @staticmethod
    def sql_check_photo_exists_in_db(connection, photo_name):
        with connection.cursor() as cursor:
            sql = "SELECT EXISTS(SELECT `filename` FROM `photos` WHERE `photos`.`filename`='" + photo_name+"')"
            cursor.execute(sql)
            result = cursor.fetchone()
            num_result = result["EXISTS(SELECT `filename` FROM `photos` WHERE `photos`.`filename`='" + photo_name+"')"]

            return num_result