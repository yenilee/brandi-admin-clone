import pymysql
import traceback

from flask       import request, g
from connection  import get_connection
from utils       import authorize
from jsonschema  import validate, ValidationError
from json_schema import product_register_schema, product_list_queryset_schema

def create_product_endpoints(app, product_service):
    product_service = product_service

    # 마스터가 상품 등록할 때 셀러 ID 받는 로직 짜야됨
    @app.route('/product/registration', methods=['GET'])
    @authorize
    def get_register_page():
        """
        상품 등록 페이지 필요 정보 API [GET]

        Args:

        [Header]
        Authorization : 로그인 토큰

        Returns:

        success    : {'first_categories' : first_categories,
                       'color_filters' : color_filters}, 200

        key error  : {message : KEY_ERROR}, code : 400
        """

        db_connection = None

        try:
            db_connection = get_connection()
            if db_connection:
                seller_key_id = g.user
                register_response = product_service.get_register_page(seller_key_id, db_connection)

                if g.auth == 1:
                    sellers = product_service.get_sellers_for_master(g.auth, db_connection)
                    return {'seller_list' : sellers, 'page_info' : register_response}, 200
                return register_response

        except pymysql.err.InternalError as e:
            return {'message': 'DATABASE_SERVER_ERROR' + str(e)}, 500

        except pymysql.err.OperationalError:
            return {'message': 'DATABASE_ACCESS_DENIED'}, 500

        except pymysql.err.ProgrammingError as e:
            return {'message': 'DATABASE_PROGRAMMING_ERROR' + str(e)}, 500

        except pymysql.err.NotSupportedError:
            return {'message': 'DATABASE_NOT_SUPPORTED_ERROR'}, 500

        except pymysql.err.IntegrityError as e:
            return {'message': 'DATABASE_INTERGRITY_ERROR' + str(e)}, 500

        except Exception as e:
            db_connection.rollback()
            return {'message': str(e)}, 500

        finally:
            if db_connection:
                db_connection.close()

    @app.route('/product', methods=['POST'])
    @authorize
    def register_product():

        """
        상품 등록 API [POST]

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
        tag_name             : 상품 태그 (TYPE: List)

        Returns:

        success    : code : 200
        key error  : {"message" : "KEY_ERROR"}, code : 400
        """

        db_connection = None
        product = request.json
        try:
            db_connection = get_connection()
            if db_connection:
                validate(product, product_register_schema)

                product['seller_key_id'] = g.user
                register_response = product_service.create_new_product(product, g.user, db_connection)
                db_connection.commit()

                return register_response

        except  ValidationError as e:
            return {'message' : 'PARAMETER_VALIDATION_ERROR' + str(e)}, 400

        except pymysql.err.InternalError as e:
            return {'message': 'DATABASE_SERVER_ERROR' + str(e)}, 500

        except pymysql.err.OperationalError:
            return {'message': 'DATABASE_ACCESS_DENIED'}, 500

        except pymysql.err.ProgrammingError as e:
            return {'message': 'DATABASE_PROGRAMMING_ERROR' + str(e)}, 500

        except pymysql.err.NotSupportedError:
            return {'message': 'DATABASE_NOT_SUPPORTED_ERROR'}, 500

        except pymysql.err.IntegrityError as e:
            return {'message': 'DATABASE_INTERGRITY_ERROR' + str(e)}, 500

        except Exception as e:
            db_connection.rollback()
            return {'message': str(e)}, 500

        finally:
            if db_connection:
                db_connection.close()

    @app.route('/resize', methods=['POST'])
    def resize_image():
        db_connection = None
      
        db_connection = get_connection()
        if db_connection:
            image_url = '/home/sungjunjin/바탕화면/brandi.jpg'
            register_response = product_service.resize_image(image_url, db_connection)
            return image_url

    @app.route('/products', methods=['GET'])
    @authorize
    def get_product_list():
        """
        상품 리스트 API (마스터) [GET]

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
        key error    : {"message" : "KEY_ERROR"}, code : 400
        type error   : {"message" : "TYPE_ERROR"}, code : 400
        unauthorized : {"message" : "UNAUTHORIZED"} code : 401
        """

        #데코레이터를 통해 마스터 권한 확인 
        if g.auth is not 1:
            return {'message' : 'UNAUTHORIZED'}, 401

        db_connection = None
        try:
            #필터 query string validation
            filters = request.args
            #필터 query string validation
            validate(filters, product_list_queryset_schema)            
     
            db_connection = get_connection()
            if db_connection:                
                products_list_response = product_service.get_product_list(filters, db_connection)
                return products_list_response

        except ValidationError:
            return {'message' : 'PARAMETER_VALIDATION_ERROR'}, 400

        except pymysql.err.InternalError:
            return {'message': 'DATABASE_SERVER_ERROR'}, 500

        except pymysql.err.OperationalError:
            return {'message': 'DATABASE_ACCESS_DENIED'}, 500

        except pymysql.err.ProgrammingError:
            return {'message': 'DATABASE_PROGRAMMING_ERROR'}, 500

        except pymysql.err.NotSupportedError:
            return {'message': 'DATABASE_NOT_SUPPORTED_ERROR'}, 500

        except pymysql.err.IntegrityError:
            return {'message': 'DATABASE_INTERGRITY_ERROR'}, 500

        except  Exception as e:
            return {'message': str(e)}, 500

        finally:
            if db_connection:
                db_connection.close()

    @app.route('/product/second-category', methods = ['GET'])
    @authorize
    def get_second_category():
        db_connection = None
        first_category_id = request.json['first_category_id']

        try:
            db_connection = get_connection()
            if db_connection:
                seller_key_id = g.user
                register_response = product_service.get_second_category(seller_key_id, first_category_id, db_connection)
                return register_response

        except pymysql.err.InternalError as e:
            return {'message': 'DATABASE_SERVER_ERROR' + str(e)}, 500

        except pymysql.err.OperationalError:
            return {'message': 'DATABASE_ACCESS_DENIED'}, 500

        except pymysql.err.ProgrammingError as e:
            return {'message': 'DATABASE_PROGRAMMING_ERROR' + str(e)}, 500

        except pymysql.err.NotSupportedError:
            return {'message': 'DATABASE_NOT_SUPPORTED_ERROR'}, 500

        except pymysql.err.IntegrityError as e:
            return {'message': 'DATABASE_INTERGRITY_ERROR' + str(e)}, 500

        except Exception as e:
            db_connection.rollback()
            return {'message': str(e)}, 500

        finally:
                db_connection.close()

    @app.route('/product/<int:product_key_id>', methods = ['PUT'])
    @authorize
    def update_product(product_key_id):
        db_connection = None
        product = request.json

        try:
            db_connection = get_connection()
            if db_connection:
                update_response = product_service.update_product(product_key_id, db_connection)
                return {'get_product' : update_response },200

        except pymysql.err.InternalError as e:
            return {'message': 'DATABASE_SERVER_ERROR' + str(e)}, 500

        except pymysql.err.OperationalError:
            return {'message': 'DATABASE_ACCESS_DENIED'}, 500

        except pymysql.err.ProgrammingError as e:
            return {'message': 'DATABASE_PROGRAMMING_ERROR' + str(e)}, 500

        except pymysql.err.NotSupportedError:
            return {'message': 'DATABASE_NOT_SUPPORTED_ERROR'}, 500

        except pymysql.err.IntegrityError as e:
            return {'message': 'DATABASE_INTERGRITY_ERROR' + str(e)}, 500

        except Exception as e:
            db_connection.rollback()
            return {'message': str(e)}, 500

        finally:
            db_connection.close()