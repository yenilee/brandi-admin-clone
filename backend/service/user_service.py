import bcrypt
import jwt
import re
import collections

from config   import SECRET_KEY, ALGORITHM
from datetime import datetime, timedelta

class UserService:

    def __init__(self, user_dao, config):
        self.user_dao = user_dao
        self.config   = config

    def check_sign_up_validations(self, new_user):

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

    def sign_up_seller(self, new_user, db_connection):
        try:

            if self.check_sign_up_validations(new_user):
                return self.check_sign_up_validations(new_user)

            seller_id = self.user_dao.count_seller_id(new_user, db_connection)

            if not seller_id['count'] == 0:
                return {'message' : 'USER_ALREADY_EXISTS'}, 400

            self.user_dao.sign_up_seller_key(new_user, db_connection)
            new_user['password'] = bcrypt.hashpw(new_user['password'].encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
            self.user_dao.sign_up_seller(new_user, db_connection)
            return "", 200

        except KeyError:
            db_connection.rollback()
            return {'message' : 'KEY_ERROR'}, 400

        except TypeError:
            db_connection.rollback()
            return {'message' : 'TYPE ERROR'}, 400

    def check_user(self, get_user, db_connection):
        try:
            seller_id = self.user_dao.count_seller_id(get_user, db_connection)

            if seller_id['count'] == 0:
                return {'message' : 'USER_DOES_NOT_EXIST'}, 400

            user = self.user_dao.check_user(get_user, db_connection)
            password = self.user_dao.check_password(get_user, db_connection)

            if bcrypt.checkpw(get_user['password'].encode('utf-8'), password[0].encode('utf-8')):
                token = jwt.encode({'user_id': user[0], 'authority_id' : password[1], 'exp' : datetime.utcnow() + timedelta(days=15) }, SECRET_KEY['secret'], ALGORITHM['algorithm'])

                access_token = token.decode('utf-8')
                return {'access_token' : access_token}, 200

            return {'message' : 'INVALID ACCESS'}, 401

        except KeyError:
            return {'message' : 'KEY ERROR'}, 400

        except TypeError:
            return {'message' : 'TYPE ERROR'}, 400

    def update_seller(self, user, seller_infos, db_connection):
        seller_infos['user'] = user

        previous_id = self.user_dao.get_previous_id(user, db_connection)
        self.user_dao.insert_new_seller(previous_id, db_connection)
        self.user_dao.update_history(previous_id, db_connection)

        for supervisor in seller_infos['supervisors']:
            supervisor['user'] = user
            self.user_dao.insert_supervisor(supervisor, db_connection)

        for buisness_hour in seller_infos['buisness_hours']:
            buisness_hour['user'] = user
            self.user_dao.insert_buisness_hour(buisness_hour, db_connection)

        seller_infos.pop('supervisors', None)
        seller_infos.pop('buisness_hours', None)

        self.user_dao.update_seller(seller_infos, db_connection)
        return "", 200

    def get_seller_details(self, user, db_connection):
        try:
            user_info        = self.user_dao.get_seller_details(user, db_connection)
            supervisor_info  = self.user_dao.get_supervisors(user, db_connection)
            buisness_hours   = self.user_dao.get_buisness_hours(user, db_connection)
            seller_histories = self.user_dao.get_seller_histories(user, db_connection)
            user_info[0]['supervisors']      = supervisor_info
            user_info[0]['buisness_hours']   = buisness_hours
            user_info[0]['seller_histories'] = seller_histories

            return {'data' : user_info[0]}, 200

        except KeyError:
            return {'message' : 'KEY_ERROR'}, 400

        except TypeError:
            return {'message' : 'TYPE_ERROR'}, 400

    def get_sellerlist(self, db_connection):
        try:
            sellers = self.user_dao.get_sellerlist(db_connection)
            seller_actions = self.user_dao.get_seller_action(db_connection)

            merge_tuples = collections.defaultdict(list)
            [ merge_tuples[k].extend(v.split(',')) for k, v in seller_actions ]

            for seller in sellers:
                for action in list(merge_tuples.items()):
                    if action[0]== seller['status_id']:
                        seller.update({"actions_by_status" : action[1]})

            return sellers

        except KeyError:
            return {'message' : 'KEY ERROR'}, 400

        except TypeError:
            return {'message' : 'TYPE ERROR'}, 400

