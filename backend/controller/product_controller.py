import pymysql
import traceback

from flask       import request, g
from connection  import get_connection
from utils       import authorize, connection_error
from jsonschema  import validate, ValidationError
from const       import AUTH

from json_schema import product_register_schema, product_list_queryset_schema

def create_product_endpoints(app, product_service):
    product_service = product_service

    @app.route('/sellers-for-master', methods=['GET'])
    @connection_error
    @authorize
    def get_register_page_sellers():
        """
        상품 등록 - 셀러 조회 API [GET]
        작성자: 이예은

        Args:

        [Header]
        Authorization : 로그인 토큰 (마스터 토큰만 가능)

        [Query String]
        sellers.name : 상품 등록을 원하는 유저를 조회

        Returns:
        response  : 셀러 ID, 이름(영/한), 셀러 속성, 입점 상태, 담당자 정보, site url, 액션 버튼 등
        code      : 200

        key error    : {message : KEY_ERROR}, code : 400
        type error   : {message : TYPE_ERROR}, code : 400
        unauthorized : {message : UNAUTHORIZED}, code : 401
        """
        db_connection = None

        try:
            db_connection = get_connection()
            if db_connection:

                if g.auth is not AUTH['MASTER']:
                    return {'message': 'UNAUTHORIZED'}, 401

                filters = None
                if request.args:
                    filters = request.args

                sellers = product_service.get_sellers_for_master(g.auth, filters, db_connection)

                return {'seller_list' : sellers }, 200

        finally:
            if db_connection:
                db_connection.close()

    @app.route('/product-color-filter', methods=['GET'])
    @connection_error
    @authorize
    def get_color_filter():
        """
        상품 등록 - 컬러 필터 API [GET]
        작성자: 이예은

        Args:

        [Header]
        Authorization : 로그인 토큰

        Returns:
        response  : 컬러 필터 ID, 이름(영/한), 이미지 url
        code      : 200

        key error    : {message : KEY_ERROR}, code : 400
        type error   : {message : TYPE_ERROR}, code : 400
        """

        db_connection = None

        try:
            db_connection = get_connection()
            if db_connection:
                register_response = product_service.registration_page_color_filter(db_connection)

                return {'color_filters' : register_response}, 200

        finally:
            if db_connection:
                db_connection.close()

    @app.route('/product-options', methods=['GET'])
    @connection_error
    @authorize
    def get_option():
        """
        상품 등록 - 옵션 선택 API [GET]
        작성자: 이예은

        Args:

        [Header]
        Authorization : 로그인 토큰

        Returns:
        response : 옵션 색상 & 사이즈 id, 이름 ex) White, XL
        code     : 200

        key error    : {message : KEY_ERROR}, code : 400
        type error   : {message : TYPE_ERROR}, code : 400
        """

        db_connection = None

        try:
            db_connection = get_connection()
            if db_connection:
                register_response = product_service.registration_page_options(db_connection)

                return register_response

        finally:
            if db_connection:
                db_connection.close()

    @app.route('/product/first-category', methods=['GET'])
    @connection_error
    @authorize
    def get_first_category():
        """
        상품 등록 - 1차 카테고리 선택 API [GET]
        작성자: 이예은

        Args:

        [Header]
        Authorization : 로그인 토큰

        [Query String]
        seller_key_id : 로그인 토큰이 마스터일 경우 쿼리스트링으로 해당 셀러의 정보를 조회

        Returns:
        success      : {'option_color' : colors,
                        'option_size'  : sizes }  code : 200

        key error    : {message : KEY_ERROR}, code : 400
        type error   : {message : TYPE_ERROR}, code : 400
        """
        db_connection = None

        try:
            db_connection = get_connection()
            seller_key_id = g.user

            if db_connection:
                if request.args:
                    if g.auth is AUTH['MASTER']:
                        seller_key_id = request.args['seller_key_id']
                    if g.auth is AUTH['SELLER']:
                        seller_key_id = g.user

            first_categories = product_service.get_first_category(seller_key_id, db_connection)
            attribute_id = product_service.get_attribute_id(seller_key_id, db_connection)

            return {'seller_attribute_id' : attribute_id,
                    'first_category': first_categories
                    }, 200

        finally:
            if db_connection:
                db_connection.close()

    @app.route('/product/second-category', methods = ['GET'])
    @connection_error
    @authorize
    def get_second_category():
        """
        상품 등록 - 2차 카테고리 선택 API [GET]
        작성자: 이예은

        Args:

        [Header]
        Authorization : 로그인 토큰

        [Query String]
        seller_key_id     : 셀러 속성에 맞는 1차, 2차 카테고리 조합을 보여주기 위함
        first_category_id : 1차 카테고리 선택 후 2차 카테고리 결과 노출 목적

        Returns:
        success      : {'option_color' : colors,
                        'option_size'  : sizes }  code : 200

        key error    : {message : KEY_ERROR}, code : 400
        type error   : {message : TYPE_ERROR}, code : 400
        """
        db_connection = None
        seller_key_id = g.user

        try:
            db_connection = get_connection()
            if db_connection:
                seller_key_id = g.user

                if request.args:
                    if g.auth is AUTH['MASTER']:
                        seller_key_id = request.args['seller_key_id']
                    if g.auth is AUTH['SELLER']:
                        seller_key_id = g.user
                    first_category_id = request.args['first_category_id']

                register_response = product_service.get_second_category(seller_key_id, first_category_id, db_connection)
                return register_response

        finally:
            if db_connection:
                db_connection.close()

    @app.route('/product', methods=['POST'])
    @connection_error
    @authorize
    def register_product():

        """
        신규 상품 등록 API [POST]
        작성자: 이예은

        Args:

        [Header]
        Authorization : 로그인 토큰

        [body]
        first_category_id    : 1차 카테고리 id
        second_category_id   : 2차 카테고리 id
        is_onsale            : 판매 여부 (Boolean)
        is_displayed         : 진열 여부 (Boolean)
        is_detail_reference  : 상품 정보 고시 - 상품 상세 참조 여부 (Boolean)
        manufacturer         : 제조사
        manufacture_date     : 제조일자
        origin               : 원산지

        name                 : 상품 이름
        simple_description   : 한줄 상품 설명
        color_filter_id      : 색상 필터 id
        details              : 상세 상품 정보
        manufacturer         : 제조사
        manufacture_date     : 제조일자
        origin               : 원산지

        wholesale_price      : 도매원가
        price                : 판매가
        discount_rate        : 할인율
        discount_start       : 할인 시작 시간
        discount_end         : 할인 종료 시간
        maximum_quantity     : 최대판매수량
        minimum_quantity     : 최소판매수량
        tags                 : 상품 태그 (TYPE: List)

        Returns:

        success    : code : 200
        key error  : {message : KEY_ERROR}, code : 400
        """

        db_connection = None
        product = request.json

        try:
            db_connection = get_connection()
            if db_connection:
                validate(product, product_register_schema)

                product['editor'] = g.user

                if g.auth is not AUTH['MASTER']:
                    product['seller_key_id'] = g.user

                register_response = product_service.create_new_product(product, product['seller_key_id'] , db_connection)
                db_connection.commit()

                return register_response

        except  ValidationError as e:
            db_connection.rollback()
            return {'message' : 'PARAMETER_VALIDATION_ERROR' + str(e)}, 400

        finally:
            if db_connection:
                db_connection.close()

    @app.route('/product/<int:product_key_id>', methods = ['GET'])
    @connection_error
    @authorize
    def get_product(product_key_id):
        """
        상품 상세 정보 조회 API [GET]
        작성자: 이예은

        Args:

        [Header]
        Authorization : 로그인 토큰

        [URL Parameter]
        product_key_id  : 상품의 고유 ID를 통해 상세 페이지 접근

        Returns:
        success      : code : 200

        key error    : {message : KEY_ERROR}, code : 400
        type error   : {message : TYPE_ERROR}, code : 400
        """
        db_connection = None

        try:
            db_connection = get_connection()
            if db_connection:

                seller_key_id = None

                if g.auth is not AUTH['MASTER']:
                    seller_key_id = g.user

                get_response = product_service.get_product(product_key_id, seller_key_id, db_connection)

                return get_response

        finally:
            db_connection.close()

    @app.route('/product/<int:product_key_id>', methods = ['PUT'])
    @connection_error
    @authorize
    def update_product(product_key_id):
        """
        기존 상품 수정 API [GET]
        작성자: 이예은

        Args:

        [Header]
        Authorization : 로그인 토큰

        [URL Parameter]
        product_key_id  : 상품의 고유 ID를 통해 상세 페이지 접근

        Returns:
        response : 등록 일자, 세일/판매 여부, 가격, 할인율, 수정자
        code     : 200

        key error    : {message : KEY_ERROR}, code : 400
        type error   : {message : TYPE_ERROR}, code : 400
        """
        db_connection = None

        try:
            db_connection = get_connection()

            if db_connection:

                product = request.json
                validate(product, product_register_schema)

                product['user'] = g.user
                update_response = product_service.update_product(product_key_id, product, db_connection)

                db_connection.commit()
                return update_response

        except  ValidationError as e:
            db_connection.rollback()
            return {'message' : 'PARAMETER_VALIDATION_ERROR' + str(e)}, 400

        finally:
            if db_connection:
                db_connection.close()

    @app.route('/products', methods=['GET'])
    @connection_error
    @authorize
    def get_product_list():
        """
        상품 리스트 API [GET]
        작성자 :진성준
        
        Args:

        [Header]
        Authorization : 로그인 토큰

        [Query String]
        user                : 셀러명
        product_name        : 상품명
        product_code        : 상품 코드
        product_number      : 상품 번호
        is_onsale           : 판매 여부 (Boolean)
        is_displayed        : 진열 여부 (Boolean)
        is_discount         : 할인 여부 (Boolean)
        seller_attribute_id : 셀러 속성 ID (쇼핑몰 : 1, 마켓 : 2, 로드샵 : 3, 디자이너브랜드 : 4, 제너럴브랜드 : 5, 내셔널브랜드 : 6, 뷰티 : 7)

        Returns:

        success      : code : 200
        key error    : {message : KEY_ERROR}, code : 400
        type error   : {message : TYPE_ERROR}, code : 400
        unauthorized : {message : UNAUTHORIZED}, code : 401
        """

        db_connection = None
        try:
            #필터 query string validation
            filters = request.args
            #필터 query string validation
            validate(filters, product_list_queryset_schema)

            #사용자의 권한과 고유 ID를 담아준다
            seller_info = {} 
            seller_info['auth'] = g.auth
            seller_info['seller_key_id'] = g.user            
     
            db_connection = get_connection()
            if db_connection:                
                products_list_response = product_service.get_product_list(seller_info, filters, db_connection)
                return products_list_response

        except ValidationError as e:
            return {'message' : 'PARAMETER_VALIDATION_ERROR ' + str(e.path)}, 400

        finally:
            if db_connection:
                db_connection.close()

    @app.route('/product-history/<int:product_key_id>', methods = ['GET'])
    @connection_error
    @authorize
    def get_product_history(product_key_id):
        """
        상품 수정 이력 조회 API [GET]
        작성자: 이예은

        Args:

        [Header]
        Authorization : 로그인 토큰 (마스터 Only)

        Returns:
        response : 등록 일자, 세일/판매 여부, 가격, 할인율, 수정자
        code     : 200

        key error    : {message : KEY_ERROR}, code : 400
        type error   : {message : TYPE_ERROR}, code : 400
        """
        db_connection = None

        try:
            db_connection = get_connection()

            if db_connection:
                response = product_service.get_product_history(product_key_id, db_connection)
                return response, 200

        except ValidationError as e:
            return {'message' : 'PARAMETER_VALIDATION_ERROR ' + str(e.path)}, 400

        finally:
            if db_connection:
                db_connection.close()
