import pymysql

from flask      import request, g
from connection import get_connection
from utils      import authorize

def create_product_endpoints(app, product_service):
    product_service = product_service

    @app.route('/product', methods=['POST'])
    @authorize
    def product_register():
        # 상품 등록 API

        db_connection = None
        product_infos = request.json
        try:
            db_connection = get_connection()
            if db_connection:
                product_infos['seller_id'] = g.user
                register_response = product_service.create_new_product(product_infos, db_connection)
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

    @app.route('/product/sellers', methods = ['GET'])
    @authorize
    def get_seller_list():
        # 마스터 상품 등록 시 셀러 리스트 찾기
        db_connection = None
        try:
            db_connection = get_connection()
            if db_connection:
                sellers_kor_names = product_service.sellers_kor_names(g.user, db_connection)
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

    @app.route('/product/category', methods=['GET'])
    @authorize
    def get_product_first_category():
        db_connection = None

        try:
            db_connection = get_connection()
            if db_connection:
                user = {}
                user['user'] = g.user
                register_response = product_service.get_product_first_categories(user, db_connection)
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
