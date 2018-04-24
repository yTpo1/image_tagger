from DBItemAdder import DBItemAdder
from ImageManipulator import *


if __name__ == "__main__":
    # CyberDB = DBItemAdder()
    # add_photos_assign_artist_and_genre_to_db()
    # CyberDB.add_photos_anime_genre_to_db()

    # CyberDB.add_used_photos()

    # CyberDB.close_connection()
    ImgBoss = ImageManipulator()

    # ImgBoss.get_images_of_genre(9)
    ImgBoss.assign_current_photos_to_genre(23)



# TODO: when calling sql_get_photo_id() - if doesn't find anything, returns none