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
                     'exp'          : datetime.utcnow() + timedelta(days = 15),
                    }, SECRET_KEY['secret'], ALGORITHM['algorithm'])
                access_token = token.decode('utf-8')

                if self.user_dao.check_user_auth(get_user, db_connection) is 3:
                    return {'message' : 'UNAUTHORIZED USER'}, 401

                return {'access_token' : access_token}, 200
            return {'message' : 'INVALID ACCESS'}, 400            

        except KeyError:
            return {'message' : 'KEY ERROR'}, 400

        except TypeError:
            return {'message' : 'TYPE ERROR'}, 400

    def update_seller(self, user, seller_infos, db_connection):
        try: 
            # user - 셀러권한 : 자기 자신의 고유 ID, 마스터권한 : url parameter로 받은 셀러 고유 ID

            # 고유 ID를 request에 추가 
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
            # user - 셀러권한 : 자기 자신의 고유 ID, 마스터권한 : url parameter로 받은 셀러 고유 ID

            # 사용자 정보
            user_info        = self.user_dao.get_seller_details(user, db_connection)
            
            # 셀러가 존재하지 않을 경우 
            if user_info == 0:
                return {'message' : 'NO_SELLER_SELECTED'}, 500

            # 담당자 정보 가져오기
            supervisor_info  = self.user_dao.get_supervisors(user, db_connection)
            # 영업시간 가져오기
            buisness_hours   = self.user_dao.get_buisness_hours(user, db_connection)
            # 셀러 수정이력 가져오기
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
            return {'message' : 'TYPE_ERROR'}, 400

    def get_seller_list(self, filters, db_connection):
        try:
            # seller list를 불러오는 dao 함수 실행
            sellers = self.user_dao.get_seller_list(filters, db_connection)

            # dao 함수에서 가져온 seller가 없을 경우, 메시지를 보내줌
            if sellers == 0:
                return {'message' : 'NO SELLER SELECTED'}

            # 셀러의 상태 값에 따른 액션 상태를 딕셔너리로 불러옴
            seller_actions = self.user_dao.get_seller_action(db_connection)

            # 같은 상태 값을 가진 액션을 셀러 상태 : [액션1, 액션2, 액션3] 상태로 만들어줌
            merge_tuples = collections.defaultdict(list)
            [ merge_tuples[k].extend(v.split(',')) for k, v in seller_actions ]

            # 위에서 만든 값을 셀러의 상태 ID와 매칭해줌
            for seller in sellers:
                for action in list(merge_tuples.items()):
                    if action[0]== seller['status_id']:
                        seller.update({"actions_by_status" : action[1]})

            return {'number_of_sellers' : len(sellers),
                    'number_of_pages' : int(len(sellers)/10)+1,
                    'sellers' : sellers}, 200

        except KeyError as e:
            return {'message' : 'KEY ERROR' + str(e)}, 400

        except TypeError as e:
            return {'message' : 'TYPE ERROR' +str(e)}, 400

    def update_status(self, user, action_type, db_connection):
        try:
            # 예전 기록 중 셀러의 최신 수정 데이터를 갖고 있는 ID를 불러오기
            previous_seller_id = self.user_dao.get_recent_seller_id(user, db_connection)[0]

            # 위에서 가져온 ID의 데이터 종료일을 현재로 바꿔줌
            self.user_dao.update_history(previous_seller_id, db_connection)

            # 최신 셀러의 데이터를 insert하고 현재의 ID 값을 가져옴
            recent_seller_id = self.user_dao.update_seller_all(previous_seller_id, db_connection)

            # 셀러의 이전 ID 값과 최신 ID값을 조합
            user_id = {}
            user_id['previous_id'] = previous_seller_id
            user_id['recent_id'] = recent_seller_id

            # 이전 ID 값의 담당자 정보와 고객센터 운영시간 정보를 가져와 새로운 데이터를 insert 한다 
            self.user_dao.update_supervisor(user_id, db_connection)
            self.user_dao.update_buisness_hour(user_id, db_connection)

            # request에 담긴 action을 기반으로 다음 status 불러오기
            next_status_id = self.user_dao.get_next_status(action_type, db_connection)

            # 퇴점 신청 처리일 경우 is_deleted를 1로 바꿔서 soft delete 실행
            if next_status_id == 6 or next_status_id == 7:
                self.user_dao.soft_delete_seller(recent_seller_id, db_connection)

            # 입점 승인 요청일 경우 권한 ID를 2에서 3으로 바꿈
            if action_type['action_type'] == '입점 승인':
                self.user_dao.update_authority(recent_seller_id, db_connection)

            # 다음 status id와 seller의 최신 ID를 가져와 반영해준다.
            self.user_dao.update_status(next_status_id, recent_seller_id, db_connection)

            return "", 200

        except KeyError:
            db_connection.rollback()
            return {'message' : 'KEY_ERROR'}, 400

        except TypeError:
            db_connection.rollback()
            return {'message' : 'TYPE_ERROR'}, 400
