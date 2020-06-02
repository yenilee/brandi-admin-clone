import pymysql

from flask      import request
from connection import get_connection

def create_user_endpoints(app, services):
    user_service = services.user_service

    @app.route('/sign-up', methods = ['POST'])
    def sign_up(): 
        db_connection = None
        new_user = request.json       
        try:
            db_connection = get_connection()
            if db_connection:
                sign_up_response = user_service.create_new_user(new_user, db_connection)
                db_connection.commit()
                db_connection.close()
                return sign_up_response          

        except pymysql.err.InternalError:

            if db_connection: 
                db_connection.rollback()      

            return {'message' : 'DATABASE_SERVER_ERROR'}, 500
        
        except pymysql.err.OperationalError:              
            return {'message' : 'DATABASE_ACCESS_DENIED'}, 500 

    @app.route('/sign-in', methods=['POST'])
    def sign_in():
        get_user = request.json
        db_connection = get_connection()
        try:    
            if db_connection:
                get_user = user_service.check_user(get_user, db_connection)  
                return get_user

        finally:
            db_connection.close()
               
