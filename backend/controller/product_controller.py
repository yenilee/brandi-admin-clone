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
        name : 상품 등록을 원하는 셀러의 한글 이름 조회

        Returns:
        response  : 셀러 ID, 이름(영/한), 셀러 속성, 입점 상태, 담당자 정보, site url, 액션 버튼 등
        code      : 200

        key error      : {message : KEY_ERROR}, code : 400
        type error     : {message : TYPE_ERROR}, code : 400
        셀러 조회 권한 없음 : {message : UNAUTHORIZED}, code : 401
        """
        db_connection = None

        try:
            db_connection = get_connection()
            if db_connection:

                # 권한 ID가 마스터가 아닐 경우 권한 없음 에러 메시지 표시
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
        """

        db_connection = None

        try:
            db_connection = get_connection()
            if db_connection:
                color_filter = product_service.registration_page_color_filter(db_connection)

                return {'color_filters' : color_filter}, 200

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
        """

        db_connection = None

        try:
            db_connection = get_connection()
            if db_connection:
                option_response = product_service.registration_page_options(db_connection)

                return option_response

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
        success      : {seller_attribute_id : ID, 이름,
                        first_category : ID, 이름 }, code : 200

        key error    : {message : KEY_ERROR}, code : 400
        type error   : {message : TYPE_ERROR}, code : 400
        """
        db_connection = None

        try:
            db_connection = get_connection()
            if db_connection:
                # 셀러일 경우 토큰에 있는 고유 ID로, 마스터일 경우 request body의 seller_key_id로 셀러 고유 ID 조회
                seller_key_id = g.user

                if request.args:
                    if g.auth is AUTH['MASTER']:
                        seller_key_id = request.args['seller_key_id']

                first_categories = product_service.get_first_category(seller_key_id, db_connection)
                attribute_id = product_service.get_attribute_id(seller_key_id, db_connection)

                return {'seller_attribute_id' : attribute_id,
                        'first_category': first_categories}, 200

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
        seller_key_id  : 마스터 권한 유저의 경우 쿼리스트링으로 셀러 고유 ID를 받고,
        셀러 권한 유저는 로그인 토근 값으로 셀러 속성에 맞는 1차, 2차 카테고리 조합을 조회

        first_category_id : 선택된 1차 카테고리에 따라 2차 카테고리 결과 조회

        Returns:
        success      : {second_category : ID, 이름}  code : 200
        """
        db_connection = None

        try:
            db_connection = get_connection()
            if db_connection:

                # 셀러일 경우 토큰에 있는 고유 ID로, 마스터일 경우 request body의 seller_key_id로 셀러 고유 ID 조회
                seller_key_id = g.user

                if request.args:
                    first_category_id = request.args['first_category_id']

                    if g.auth is AUTH['MASTER']:
                        seller_key_id = request.args['seller_key_id']
                second_categories = product_service.get_second_category(seller_key_id, first_category_id, db_connection)

                return {'second_category': second_categories}, 200

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
        seller_key_id        : 셀러 고유 ID (마스터 등록 시)
        is_onsale            : 판매 여부 (Boolean)
        is_displayed         : 진열 여부 (Boolean)
        color_filter_id      : 컬러 필터 id
        first_category_id    : 1차 카테고리 id
        second_category_id   : 2차 카테고리 id
        is_detail_reference  : 상품 정보 고시 - 상품 상세 참조 여부 (Boolean)

        manufacture : {
        manufacturer         : 제조사
        manufacture_date     : 제조일자
        origin               : 원산지 }

        name                 : 상품 이름
        simple_description   : 한줄 상품 설명
        details              : 상세 상품 정보

        options : {[
          "size"     : "XL",
          "color"    : "White",
          "quantity" : 30 ]}

        wholesale_price      : 도매원가
        price                : 판매가
        discount_rate        : 할인율
        discount_start       : 할인 시작 시간
        discount_end         : 할인 종료 시간
        maximum_quantity     : 최대 판매 수량
        minimum_quantity     : 최소 판매 수량
        tag_name             : 상품 태그 (TYPE: List)

        Returns:

        success          : code : 200
        key error        : {message : KEY_ERROR}, code : 400
        type error       : {message : TYPE_ERROR}, code : 400
        validation error : {message : PARAMETER_VALIDATION_ERROR}, code : 400
        """

        db_connection = None
        product = request.json

        try:
            db_connection = get_connection()
            if db_connection:
                validate(product, product_register_schema)

                product['editor'] = g.user

                # 마스터 권한이 아닐 경우 request body에 토큰 값의 seller 고유 ID추가, 마스터 권한은 request에서 고유 ID 확인
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
        """
        db_connection = None

        try:
            db_connection = get_connection()
            if db_connection:

                # 마스터일 경우 모든 셀러 조회가 가능하고, 셀러일 경우 토큰 값으로 고유 ID에 해당하는 상품만 볼 수 있도록 seller 고유 id 설정
                seller_key_id = None

                if g.auth is not AUTH['MASTER']:
                    seller_key_id = g.user

                get_product = product_service.get_product(product_key_id, seller_key_id, db_connection)

                return get_product

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
        response : 등록 일자, 세일/판매 여부, 가격, 할인율, 수정자 등
        code     : 200

        key error        : {message : KEY_ERROR}, code : 400
        type error       : {message : TYPE_ERROR}, code : 400
        validation error : {message : PARAMETER_VALIDATION_ERROR}, code : 400
        """
        db_connection = None

        try:
            db_connection = get_connection()

            if db_connection:

                product = request.json
                validate(product, product_register_schema)

                product['editor'] = g.user

                # 셀러 권한은 토큰 값에 있는 seller 고유 ID로, 마스터 권한은 request body에 있는 고유 ID로 조회
                if g.auth is not AUTH['MASTER']:
                    product['seller_key_id'] = g.user

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

        key error         : {message : KEY_ERROR}, code : 400
        type error        : {message : TYPE_ERROR}, code : 400
        마스터 권한이 아닐 경우 : {message : UNAUTHORIZED}, code: 400
        """
        db_connection = None

        try:
            db_connection = get_connection()

            if db_connection:

                if g.auth is not AUTH['MASTER']:
                    return {'message' : 'UNAUTHORIZED'}, 400

                response = product_service.get_product_history(product_key_id, db_connection)

                return response, 200

        finally:
            if db_connection:
                db_connection.close()
