from flask      import jsonify, request
from connection import get_connection

def create_endpoints(app, services):
    user_service = services.user_service

    @app.route('/sign-up', methods=['POST'])
    def sign_up(): 
        new_user = request.json
        db_connection = get_connection()
        try:
            if db_connection:
                new_user = user_service.create_new_user(new_user, db_connection)
                db_connection.commit() #위치모름
                return new_user

        finally:           
            db_connection.close() # 커넥션 종료
