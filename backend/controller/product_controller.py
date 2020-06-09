import pymysql

from flask      import request, g
from connection import get_connection
from utils      import authorize

def create_product_endpoints(app, product_service):
    product_service = product_service

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
                user = { 'seller_id' : g.user }
                register_response = product_service.get_category_colorfilter(user, db_connection)
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

    @app.route('/product/sellers', methods = ['GET'])
    @authorize
    def get_seller_list():

        """
        마스터 상품 등록 페이지 셀러 선택 API [GET]

        Args:

        [Header]
        Authorization : 로그인 토큰

        Returns:

        success    : {"sellers" : sellers_kor_names}, code : 200
        key error  : {"message" : "KEY_ERROR"}, code : 400

        마스터 권한 아닐 시 : {'message' : 'UNAUTHORIZED'}, code : 400
        """

        db_connection = None
        try:
            db_connection = get_connection()
            if db_connection:

                # 권한 ID가 마스터가 아닐 경우 권한 없음 에러 미시지 표시
                if g.auth is not 1:
                    return {'message' : 'UNAUTHORIZED'}, 401

                sellers_kor_names = product_service.get_sellers_for_master(g.user, db_connection)
                return {"sellers" : sellers_kor_names}, 200

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
        tag_name             : 상품 태그 (List)

        Returns:

        success    : code : 200
        key error  : {"message" : "KEY_ERROR"}, code : 400
        """

        db_connection = None
        product = request.json
        try:
            db_connection = get_connection()
            if db_connection:

                product['seller_id'] = g.user
                register_response = product_service.create_new_product(product, db_connection)
                db_connection.commit()
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

    @app.route('/resize', methods=['POST'])
    def resize_image():
        db_connection = None
      
        db_connection = get_connection()
        if db_connection:
            image_url = '/home/sungjunjin/바탕화면/brandi.jpg'
            register_response = product_service.resize_image(image_url, db_connection)
            return image_url

    @app.route('/product/category', methods = ['GET'])
    @authorize
    def get_second_category():

        """
        2차 카테고리 API [GET]

        Args:

        [Header]
        Authorization : 로그인 토큰

        [body]
        first_category_id : 1차 카테고리 id

        Returns:

        success    : {"second_categories" : second_category}, code : 200
        key error  : {"message" : "KEY_ERROR"}, code : 400
        """

        db_connection = None
        product = request.json
        try:
            db_connection = get_connection()
            if db_connection:

                product['seller_id'] = g.user
                second_category = product_service.get_second_category(product, db_connection)
                return {"second_categories" : second_category}, 200

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
            return {'message': str(e)}, 500

        finally:
            if db_connection:
                db_connection.close()

