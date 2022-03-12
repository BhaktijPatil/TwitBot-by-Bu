import mysql.connector


def connect_img_db():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="7090",
        database="image_db"
    )
    return database


def disconnect_db(database):
    database.close()
