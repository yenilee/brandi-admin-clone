from flask      import jsonify, request
from connection import get_connection

def create_user_endpoints(app, services):
    user_service = services.user_service

    @app.route('/sign-up', methods=['POST'])
    def sign_up(): 
        new_user = request.json
        db_connection = get_connection()
        try:
            if db_connection:
                new_user = user_service.create_new_user(new_user, db_connection)
                db_connection.commit()
                return new_user

        finally:           
            db_connection.close()

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
               
