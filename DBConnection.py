import pymysql.cursors


def create_connection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='cyberpunk_images',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


def close_connection(connection):
    connection.close()

