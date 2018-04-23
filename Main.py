from DBItemAdder import DBManager


if __name__ == "__main__":
    CyberDB = DBManager()
    # add_photos_assign_artist_and_genre_to_db()
    # CyberDB.add_photos_anime_genre_to_db()

    # CyberDB.add_used_photos()

    CyberDB.test_artist()
    CyberDB.close_connection()


# TODO: when calling sql_get_photo_id() - if doesn't find anything, returns none