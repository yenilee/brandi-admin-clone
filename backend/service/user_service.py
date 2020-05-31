import bcrypt

from flask import jsonify

class UserService:

    def __init__(self, user_dao, config):
        self.user_dao = user_dao
        self.config = config

    def create_new_user(self, new_user, db_connection):
        user_count = self.user_dao.check_user_exists(new_user, db_connection)
        
        if not user_count[0] == 0:
            return jsonify({'message' : 'USER_ALREADY_EXISTS'}), 400

        self.user_dao.insert_seller_key(new_user, db_connection)
        new_user['password'] = bcrypt.hashpw(new_user['password'].encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
        self.user_dao.insert_seller(new_user, db_connection)
        return "", 200  

