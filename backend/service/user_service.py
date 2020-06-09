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
            # 회원가입 request parameter 유효성 검사

            #셀러 ID
            if not re.match(r'^[A-Za-z0-9][A-Za-z0-9_-]{4,20}$', new_user['user']):
                return {'message' : 'ID_VALIDATION_ERROR'}, 400

            #비밀번호
            if not re.match(r'(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{7,20}$', new_user['password']):
                return {'message' : 'PASSWORD_VALIDATION_ERROR'}, 400

            #핸드폰번호
            if not re.match(r'\d{3}-\d{3,4}-\d{4}$', new_user['phone_number']):
                return {'message' : 'PHONE_NUMBER_VALIDATION_ERROR'}, 400

            #한글 이름
            if not re.match(r'^[ㄱ-ㅣ가-힣-0-9A-Za-z]([0-9ㄱ-ㅣ가-힣A-Za-z]){0,20}$', new_user['name']):
                return {'message' : 'SELLER_NAME_VALIDATION_ERROR'}, 400

            #영문 이름
            if not re.match(r'^[a-z]*$', new_user['eng_name']):
                return {'message' : 'SELLER_ENGLISH_NAME_VALIDATION_ERROR'}, 400

            #고객센터 전화번호
            if not re.match(r'(02.{0}|^01.{1}|[0-9]{4})-([0-9]+)-([0-9]{4})', new_user['service_number']):
                return {'message' : 'SERVICE_NUMBER_VALIDATION_ERROR'}, 400

            #사이트 URL
            if not re.match(r'(http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/].[^\s]*$))?', new_user['site_url']):
                return {'message' : 'SITE_URL_VALIDATION_ERROR'}, 400

    def sign_up_seller(self, new_user, db_connection):
        try:
            # 회원가입 Validation 검사
            if self.check_sign_up_validations(new_user):
                return self.check_sign_up_validations(new_user)

            # 셀러 ID 중복체크 
            seller_id = self.user_dao.count_seller_id(new_user, db_connection)
            
            # 중복되는 셀러 ID 존재 
            if not seller_id['count'] == 0:
                return {'message' : 'USER_ALREADY_EXISTS'}, 400

            # 셀러 고유 ID값 삽입
            self.user_dao.sign_up_seller_key(new_user, db_connection)
            # 비밀번호 암호화 후 셀러 정보 저장 
            new_user['password'] = bcrypt.hashpw(new_user['password'].encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
            last_row_id = self.user_dao.sign_up_seller(new_user, db_connection)
            new_user['last_row_id'] = last_row_id
            # 저장된 셀러 ID를 가져와서 초기 관리자, 영업시간 정보를 저장
            self.user_dao.insert_initial_supervisor(new_user, db_connection)
            self.user_dao.insert_initial_buisness_hours(new_user, db_connection)

            return "", 200

        except KeyError as e:
            db_connection.rollback()
            return {'message' : 'KEY_ERROR' + str(e)}, 400

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
                token = jwt.encode(
                    {'user_id'      : user[0],
                     'authority_id' : password[1],
                     'exp'          : datetime.utcnow() + timedelta(days=15),

                     }, SECRET_KEY['secret'], ALGORITHM['algorithm'])

                access_token = token.decode('utf-8')
                return {'access_token' : access_token}, 200

            return {'message' : 'INVALID ACCESS'}, 401

        except KeyError:
            return {'message' : 'KEY ERROR'}, 400

        except TypeError:
            return {'message' : 'TYPE ERROR'}, 400

    def update_seller(self, user, seller_infos, db_connection):
        try: 
            # 셀러 ID를 가져온다 
            seller_infos['user'] = user

            #가장 최근에 저장된 셀러의 기본 정보(셀러 키 ID, 권한, 속성, 비밀번호 등)을 가져와 새로운 셀러 레코드를 생성한다
            recent_seller_id = self.user_dao.get_recent_seller_id(user, db_connection)
            self.user_dao.insert_new_seller(recent_seller_id, db_connection)
            # 이전 데이터와 새로운 데이터의 이력을 바꿔준다
            self.user_dao.update_history(recent_seller_id, db_connection)

            #일대다(관리자, 영업시간) 데이터 삽입
            for supervisor in seller_infos['supervisors']:
                supervisor['user'] = user
                self.user_dao.insert_supervisor(supervisor, db_connection)

            for buisness_hour in seller_infos['buisness_hours']:
                buisness_hour['user'] = user
                self.user_dao.insert_buisness_hour(buisness_hour, db_connection)

            #일대다 request 삭제
            seller_infos.pop('supervisors', None)
            seller_infos.pop('buisness_hours', None)

            #새로 생긴 셀러 레코드에 나머지 데이터를 업데이트 한다
            self.user_dao.update_seller(seller_infos, db_connection)
            return "", 200

        except KeyError:
            db_connection.rollback()
            return {'message' : 'KEY_ERROR'}, 400

        except TypeError:
            db_connection.rollback()
            return {'message' : 'TYPE_ERROR'}, 400

    def get_seller_details(self, user, db_connection):
        try:
            # 사용자 정보
            user_info        = self.user_dao.get_seller_details(user, db_connection)
            # 담당자 정보
            supervisor_info  = self.user_dao.get_supervisors(user, db_connection)
            # 영업시간
            buisness_hours   = self.user_dao.get_buisness_hours(user, db_connection)
            # 셀러 수정이력
            seller_histories = self.user_dao.get_seller_histories(user, db_connection)
            # JSON 결합 
            user_info[0]['supervisors']      = supervisor_info
            user_info[0]['buisness_hours']   = buisness_hours
            user_info[0]['seller_histories'] = seller_histories
            
            # 사용자 기본정보 + 담당자 정보 + 영업시간 + 셀러 수정이력 
            return {'data' : user_info[0]}, 200

        except KeyError:
            return {'message' : 'KEY_ERROR'}, 400

        except TypeError:
            return {'message' : 'TYPE_ERROR' + str(e)}, 400

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

