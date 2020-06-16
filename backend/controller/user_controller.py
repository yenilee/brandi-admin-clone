import pymysql

from jsonschema      import validate, ValidationError
from flask           import request, g
from connection      import get_connection

from utils           import authorize, connection_error
from json_schema     import (
    seller_register_schema,
    seller_action_schema,
    seller_sign_up_schema,
    seller_list_query_schema
    )
from const           import AUTH

def create_user_endpoints(app, user_service):
    user_service = user_service

    @app.route('/sign-up', methods = ['POST'])
    @connection_error
    def sign_up():

        """
        회원가입 API [POST]

        Args:
            [Body]
                user                : 셀러 id
                password            : 비밀번호
                phone_number        : 핸드폰번호
                seller_attribute_id : 셀러 정보 id (쇼핑몰 : 1, 마켓 : 2, 로드샵 : 3, 디자이너브랜드 : 4, 제너럴브랜드 : 5, 내셔널브랜드 : 6, 뷰티 : 7)
                name                : 셀러명 (상호)
                eng_name            : 영문 셀러명(영문상호)
                service_number      : 고객센터 전화번호
                site_url            : 사이트 URL

        Returns:

            success                : code : 200
            key error              : {message : KEY_ERROR}, code : 400

            셀러 ID 중복            : {message : USER_ALREADY_EXISTS}, code : 400
            셀러 ID 형식 위반       : {message : ID_VALIDATION_ERROR}, code :400
            비밀번호 형식 위반       : {message : PASSWORD_VALIDATION_ERROR}, code : 400
            핸드폰번호 형식 위반     : {message : PHONE_NUMBER_VALIDATION_ERROR}, code : 400
            셀러 이름 형식 위반      : {message : SELLER_NAME_VALIDATION_ERROR}, code : 400
            셀러 영문 이름 형식 위반 : {message : SELLER_ENGLISH_NAME_VALIDATION_ERROR}, code :400
            사이트 URL 형식 위반     : {message : SITE_URL_VALIDATION_ERROR}, code :400

        """

        db_connection = None
        try:
            db_connection = get_connection()
            new_user = request.json

            #회원가입 형식 유효성 검사
            validate(new_user, seller_sign_up_schema)

            if db_connection:
                sign_up_response = user_service.sign_up_seller(new_user, db_connection)
                db_connection.commit()

                return sign_up_response

        except ValidationError as e:
            return {'message' : 'PARAMETER_VALIDATION_ERROR ' + str(e.path)}, 400

        finally:
            if db_connection:
                db_connection.close()

    @app.route('/sign-in', methods=['POST'])
    @connection_error
    def sign_in():

        """
        로그인 API [POST]

        Args:

        user        : 셀러 id
        password    : 비밀번호

        Returns:

        Success     : {access_token : token}, 200
        key error   : {message : KEY_ERROR}, code : 400

        로그인 ID 오류   : {'message' : 'USER_DOES_NOT_EXIST'}, code : 400
        비밀번호 불일치   : {'message' : 'INVALID ACCESS'}
        """

        db_connection = None
        get_user = request.json
        try:
            db_connection = get_connection()
            if db_connection:
                sign_in_response = user_service.check_user(get_user, db_connection)

                return sign_in_response

        finally:
            if db_connection:
                db_connection.close()

    @app.route('/sellers', methods=['GET'])
    @connection_error
    @authorize
    def get_sellers_list():

        """
        셀러 계정 관리 리스트 API [GET]

        Args:

        [Header] Authorization : 로그인 토큰

        Returns:

        Success     : {'number_of_sellers' : number_of_sellers,
                       'number_of_pages'   : number_of_pages,
                       'sellers'           : sellers }, 200
        key error   : {message : KEY_ERROR}, code : 400

        마스터 권한 아닐 시 : {'message' : 'UNAUTHORIZED'}, code : 400
        """

        if g.auth is not AUTH['MASTER']:
            return {'message' : 'UNAUTHORIZED'}, 401

        db_connection = None
        try:
            db_connection = get_connection()
            if db_connection:

                if request.args:
                    filters = request.args
                    validate(filters, seller_list_query_schema)
                else:
                    filters = None

                sellers_response = user_service.get_seller_list(filters, db_connection)
                return sellers_response

        except ValidationError as e:
            return {'message' : 'PARAMETER_VALIDATION_ERROR' + str(e.path)}, 400

        finally:
            if db_connection:
                db_connection.close()

    @app.route('/seller', methods=['PUT'])
    @connection_error
    @authorize
    def update_seller():
        """
        셀러 수정 (셀러 권한) API [PUT]

        Args:

            [Header]
                Authorization : 로그인 토큰

            [Body]
                (기본 정보)
                profile : 셀러 프로필

                (상세정보)
                background_image    : 셀러페이지 배경이미지
                simple_introduction : 셀러 한줄 소개 (required)
                detail_introduction : 셀러 상세 소개
                site_url            : 사이트 URL
                bank                : 정산은행 (required)
                account_owner       : 계좌주 (required)
                bank_account        : 계좌번호 (required)
                order               : 순서
                service_number      : 고객센터 전화번호 (required)
                zip_code            : 우편번호
                address             : 주소 (택배 수령지)
                detail_address      : 상세주소 (택배 수령지) (required)

                (담당자 정보) (required)
                supervisor_name         : 담당자명
                supervisor_phone_number : 담당자 핸드폰번호
                supervisor_email        : 담당자 이메일

                (고객센터 운영시간)
                start_time : 9:00:00
                end_time   : 6:00:00
                is_weekend : 0

                (배송정보 및 교환/환불 정보)
                shipping_information : 배송정보 (required)
                refund_information   : 교환 / 환불 정보 (required)

                (셀러 모델 사이즈 정보)
                model_height      : 키
                model_size_top    : 상의 사이즈
                model_size_bottom : 하의 사이즈
                model_size_foot   : 발 사이즈

                (쇼핑피드 업데이트 메세지)
                feed_message : 쇼핑피드 업데이트 메세지

        Returns:
            Success : status code : 200

            Key error                          : {message : KEY_ERROR}, code : 400
            Type error                         : {message : TYPE_ERROR}, code : 400
            Request Parameter Validation Error : {message : PARAMETER_VALIDATION_ERROR}, code : 400
        """
        db_connection = None
        seller_infos = request.json

        try:
            validate(seller_infos, seller_register_schema)
            db_connection = get_connection()

            #변경실행자에 대한 정보를 request에 담아준다
            seller_infos['editor'] = g.user

            if db_connection:
                update_response = user_service.update_seller(g.user, seller_infos, db_connection)
                db_connection.commit()
                return update_response

        except ValidationError as e:
            return {'message' : 'PARAMETER_VALIDATION_ERROR ' + str(e.path)}, 400

        finally:

            if db_connection:
                db_connection.close()

    @app.route('/seller/<int:seller_key_id>', methods=['PUT'])
    @connection_error
    @authorize
    def update_seller_master(seller_key_id):
        """
        셀러 수정 (마스터 권한) API [PUT]

        Args:

            [Header]
                Authorization : 로그인 토큰
            
            [URL PARAMETER]
                seller_key_id : 셀러 고유 ID

            [Body]
                (기본 정보)
                profile : 셀러 프로필

                (상세정보)
                background_image    : 셀러페이지 배경이미지
                simple_introduction : 셀러 한줄 소개 (required)
                detail_introduction : 셀러 상세 소개
                site_url            : 사이트 URL
                bank                : 정산은행 (required)
                account_owner       : 계좌주 (required)
                bank_account        : 계좌번호 (required)
                order               : 순서
                service_number      : 고객센터 전화번호 (required)
                zip_code            : 우편번호
                address             : 주소 (택배 수령지)
                detail_address      : 상세주소 (택배 수령지) (required)

                (담당자 정보) (required)
                supervisor_name         : 담당자명
                supervisor_phone_number : 담당자 핸드폰번호
                supervisor_email        : 담당자 이메일

                (고객센터 운영시간)
                start_time : 9:00:00
                end_time   : 6:00:00
                is_weekend : 0    

                (배송정보 및 교환/환불 정보)
                shipping_information : 배송정보 (required)
                refund_information   : 교환 / 환불 정보 (required)

                (셀러 모델 사이즈 정보)
                model_height      : 키
                model_size_top    : 상의 사이즈
                model_size_bottom : 하의 사이즈
                model_size_foot   : 발 사이즈

                (쇼핑피드 업데이트 메세지)
                feed_message : 쇼핑피드 업데이트 메세지          

        Returns:
            Success : status code : 200

            Key error                          : {message : KEY_ERROR}, code : 400
            Type error                         : {message : TYPE_ERROR}, code : 400
            Request Parameter Validation Error : {message : PARAMETER_VALIDATION_ERROR}, code : 400
        """
        db_connection = None
        seller_infos = request.json
        
        try: 
            #권한이 마스터가 아니면 UNAUTHORIZED return 
            if g.auth is not AUTH['MASTER']:
                return {'message' : 'UNAUTHORIZED'}, 401

            validate(seller_infos, seller_register_schema)
            #변경실행자에 대한 정보를 request에 담아준다 
            seller_infos['editor'] = g.user

            db_connection = get_connection()  

            if db_connection:
                update_response = user_service.update_seller(seller_key_id, seller_infos, db_connection)
                db_connection.commit()
                return update_response

        except ValidationError as e:
            return {'message' : 'PARAMETER_VALIDATION_ERROR' + str(e.path)}, 400

        finally:
            
            if db_connection:
                db_connection.close()

    @app.route('/seller_details/<int:seller_key_id>', methods = ['GET'])
    @connection_error
    @authorize
    def get_seller_details_master(seller_key_id):
        """
        셀러 상세 정보 (마스터권한) [GET]

        Args:
            [Header]
                Authorization : 로그인 토큰
                
            [URL Parameter]
                seller_key_id : 셀러 고유 아이디

        Returns:

            Success             : {data : user_info}, code : 200

            Key error           : {message : KEY_ERROR}, code : 400
            Type error          : {message : TYPE_ERROR}, code : 400

            unauthorized        : {message : UNAUTHORIZED}, code : 401
            no selected sellers : {message : NO_SELLER_SELECTED}, code : 400
        """

        db_connection = None
        try:
            db_connection = get_connection()
            if db_connection: 
                
                #권한이 마스터가 아니면 UNAUTHORIZED return 
                if g.auth is not AUTH['MASTER']:
                    return {'message' : 'UNAUTHORIZED'}, 401   

                seller_infos = user_service.get_seller_details(seller_key_id, db_connection)
                return seller_infos

        finally:
            if db_connection:
                db_connection.close()

    @app.route('/seller_details', methods = ['GET'])
    @connection_error
    @authorize
    def get_seller_details():
        """
        셀러 상세 정보 (셀러권한) [GET]

        Args:
            [Header]
                Authorization : 로그인 토큰

        Returns:

            Success             : {data : user_info}, code : 200

            Key error           : {message : KEY_ERROR}, code : 400
            Type error          : {message : TYPE_ERROR}, code : 400

            unauthorized        : {message : UNAUTHORIZED}, code : 401
            no selected sellers : {message : NO_SELLER_SELECTED}, code : 400
        """

        db_connection = None
        try:
            db_connection = get_connection()
            if db_connection: 
                # 일반 셀러의 경우 토큰의 셀러 고유 id 값으로 상세 정보를 가져온다. 
                seller_infos = user_service.get_seller_details(g.user, db_connection)
                return seller_infos

        finally:
            if db_connection:
                db_connection.close()

    @app.route('/action', methods = ['PUT'])
    @connection_error
    @authorize
    def update_seller_status():

        db_connection = None
        try:
            db_connection = get_connection()

            if db_connection:
                action_type = request.json
                validate(action_type, seller_action_schema)

                if g.auth is not AUTH['MASTER']:
                    return {'message' : 'UNAUTHORIZED'}, 400

                user = action_type['user']

                action_response = user_service.update_status(user, action_type, db_connection)
                db_connection.commit()

                return action_response

        except  ValidationError as e:
            return {'message' : 'PARAMETER_VALIDATION_ERROR' + str(e)}, 400

        finally:
            if db_connection:
                db_connection.close()
