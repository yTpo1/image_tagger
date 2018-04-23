from DBItemAdder import DBManager


if __name__ == "__main__":
    CyberDB = DBManager()
    # add_photos_assign_artist_and_genre_to_db()
    # CyberDB.add_photos_anime_genre_to_db()

    # CyberDB.add_used_photos()

    photo_id = CyberDB.sql_get_photo_id("Daniel Tyka_21.jpg")
    print(photo_id)


# TODO: when calling sql_get_photo_id() - if doesn't find anything, returns none