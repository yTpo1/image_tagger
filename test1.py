import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='cyberpunk_images',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# select everything from a table
def sql_select(table_name):
    # try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `" + table_name + "`"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    #
    # finally:
    #     connection.close()


# get the ID of the photo, from photo name
def sql_get_photo_id(photo_name):
    with connection.cursor() as cursor:
        sql = "SELECT `PhotoID` FROM `photos` WHERE `filename` = '" + photo_name + "'"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


# get artist of the image
def sql_get_artists_id(photoid):
    # try:
        with connection.cursor() as cursor:
            sql = "SELECT `ArtistID` FROM `photos` WHERE `PhotoID` = '" + photoid + "'"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    #
    # finally:
    #     connection.close()


# get artists name
def sql_get_artists_name(artists_id):
    # try:
        with connection.cursor() as cursor:
            sql = "SELECT `NameSurname` FROM `artists` WHERE `ArtistID` = '" + str(artists_id) + "'"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    #
    # finally:
    #     connection.close()


# get artists name
def sql_get_genre_id(photo_id):
    with connection.cursor() as cursor:
        sql = "SELECT `GenreID` FROM `photos_to_genres_mn_relation` WHERE `PhotoID` = '" + str(photo_id) + "'"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


# get genre name
def sql_get_genre_name(genre_id):
    with connection.cursor() as cursor:
        sql = "SELECT `name` FROM `genres` WHERE `GenreID` = '" + genre_id + "'"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


def sql_get_artist_url(artist_id):
    with connection.cursor() as cursor:
        sql = "SELECT `websiteURL`, `artstationURL`, `deviantartURL`, `InstagramURL`, `TumblrURL` " \
              "FROM `artists` WHERE `ArtistID` = '" + artist_id + "'"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result



list_sql_photo_id = sql_get_photo_id("Mad Dog Jones_15")
photo_id = str(list_sql_photo_id[0]['PhotoID'])

list_sql_artist_id = sql_get_artists_id(photo_id)
artist_id = str(list_sql_artist_id[0]['ArtistID'])

list_artist_name = sql_get_artists_name(artist_id)
artist_name = list_artist_name[0]['NameSurname']

list_sql_genre_id = sql_get_genre_id(photo_id)

# list of only genre_id's
genre_id = []
for item in list_sql_genre_id:
    genre_id.append(item['GenreID'])

genre_list = []
for item in genre_id:
    list_sql_genre_name = sql_get_genre_name(str(item))
    genre_list.append(list_sql_genre_name[0]['name'])

print("photo_id - "+photo_id
      +" artist_id - "+artist_id
      +" artist_name - " + artist_name + ". Genres: ")

for item in genre_list:
    print(item)

dict_artist_url = sql_get_artist_url(artist_id)
website_url = dict_artist_url[0]['websiteURL']
artstation_url = dict_artist_url[0]['artstationURL']
deviantart_url = dict_artist_url[0]['deviantartURL']
instagram_url = dict_artist_url[0]['InstagramURL']
tumblr_url = dict_artist_url[0]['TumblrURL']

if website_url:
    print(website_url)

if artstation_url:
    print(artstation_url)

if deviantart_url:
    print(deviantart_url)

if instagram_url:
    print(instagram_url)

if tumblr_url:
    print(tumblr_url)

connection.close()

