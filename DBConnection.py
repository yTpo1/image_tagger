import pymysql.cursors
import logging
# import pymysql


def create_connection():
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='cyberpunk_images',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    except Exception as e:
        logging.warning("Exception is :" + str(e))
    else:
        return connection


def close_connection(connection):
    try:
        connection.close()
    except Exception as e:
        logging.warning("Exception is :" + str(e))

