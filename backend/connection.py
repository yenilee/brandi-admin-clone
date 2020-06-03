import pymysql

from config     import db

def get_connection():
    return pymysql.connect(

    host        = db['host'],
    user        = db['user'],
    password    = db['password'],
    db          = db['database'],
    autocommit  = False
    )