import bcrypt
import jwt
import json
import re

from config   import SECRET_KEY, ALGORITHM
from datetime import  datetime, timedelta

class UserService:

    def __init__(self, user_dao, config):
        self.user_dao = user_dao
        self.config   = config
    
    def check_sign_in_validations(self, new_user):

            if not re.match(r'^[A-Za-z0-9][A-Za-z0-9_-]{4,20}$', new_user['user']):
                return {'message' : 'ID_VALIDATION_ERROR'}, 400

            if not re.match(r'(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{7,20}$', new_user['password']):
                return {'message' : 'PASSWORD_VALIDATION_ERROR'}, 400

            if not re.match(r'\d{3}-\d{3,4}-\d{4}$', new_user['phone_number']):
                return {'message' : 'PHONE_NUMBER_VALIDATION_ERROR'}, 400

            if not re.match(r'^[ㄱ-ㅣ가-힣-0-9A-Za-z]([0-9ㄱ-ㅣ가-힣A-Za-z]){0,20}$', new_user['name']):
                return {'message' : 'SELLER_NAME_VALIDATION_ERROR'}, 400

            if not re.match(r'^[a-z]*$', new_user['eng_name']):
                return {'message' : 'SELLER_ENGLISH_NAME_VALIDATION_ERROR'}, 400
            
            if not re.match(r'(02.{0}|^01.{1}|[0-9]{4})-([0-9]+)-([0-9]{4})', new_user['service_number']):
                return {'message' : 'SERVICE_NUMBER_VALIDATION_ERROR'}, 400

            if not re.match(r'(http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/].[^\s]*$))?', new_user['site_url']):
                return {'message' : 'SITE_URL_VALIDATION_ERROR'}, 400

    def create_new_user(self, new_user, db_connection):
        try:            
            if self.check_sign_in_validations(new_user):
                return self.check_sign_in_validations(new_user)

            user_count = self.user_dao.check_user_exists(new_user, db_connection)

            if not user_count[0] == 0:
                return {'message' : 'USER_ALREADY_EXISTS'}, 400           

            self.user_dao.insert_seller_key(new_user, db_connection)
            new_user['password'] = bcrypt.hashpw(new_user['password'].encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
            self.user_dao.insert_seller(new_user, db_connection)
            return "", 200

        except KeyError:
            db_connection.rollback()                
            return {'message' : 'KEY_ERROR'}, 400

        except TypeError:
            db_connection.rollback()             
            return {'message' : 'TYPE ERROR'}, 400

    def check_user(self, get_user, db_connection):
        user_count = self.user_dao.check_user_exists(get_user, db_connection)
        try:
            if user_count[0] == 0:
                return {'message' : 'USER_DOES_NOT_EXIST'}, 400

            user = self.user_dao.check_user(get_user, db_connection)
            password = self.user_dao.check_password(get_user, db_connection)

            if bcrypt.checkpw(get_user['password'].encode('utf-8'), password[0].encode('utf-8')):
                token = jwt.encode({'user_id': user[0], 'authority_id' : password[1], 'exp' : datetime.utcnow() + timedelta(hours=3) }, SECRET_KEY['secret'], ALGORITHM['algorithm'])
                access_token = token.decode('utf-8')
                return {'access_token' : access_token}, 200 

            return {'message' : 'INVALID ACCESS'}, 401

        except KeyError:
            return {'message' : 'KEY ERROR'}, 400

        except TypeError:
            return {'message' : 'TYPE ERROR'}, 400

    def register_seller(self, seller_infos, db_connection):
        self.user_dao.register_seller(seller_infos, db_connection)
        return {"message" : "seller"}, 200
        






