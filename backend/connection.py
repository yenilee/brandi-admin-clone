import pymysql

from config     import db

def get_connection():
    db_connection = pymysql.connect(

    host        = db['host'],
    user        = db['user'],
    password    = db['password'],
    db          = db['database']
    )

    db_connection.cursor().execute("SET AUTOCOMMIT = FALSE;")
    db_connection.cursor().execute("COMMIT;")

    return db_connection
