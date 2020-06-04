import pymysql

from flask      import request, g
from connection import get_connection
from utils      import authorize
from decimal    import ROUND_HALF_UP

def create_user_endpoints(app, user_service):
    user_service = user_service
    
    @app.route('/sign-up', methods = ['POST'])
    def sign_up():

        """
        회원가입 API [POST]

        Args:

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
            if db_connection:
                sign_up_response = user_service.create_new_user(new_user, db_connection)
                db_connection.commit()
                return sign_up_response          

        except pymysql.err.InternalError:

            if db_connection: 
                db_connection.rollback()      

            return {'message' : 'DATABASE_SERVER_ERROR'}, 500
        
        except pymysql.err.OperationalError:              
            return {'message' : 'DATABASE_ACCESS_DENIED'}, 500

        except pymysql.err.ProgrammingError:
            return {'message' : 'DATABASE_PROGRAMMING_ERROR'}, 500

        except pymysql.err.NotSupportedError:
            return {'message' : 'DATABASE_NOT_SUPPORTED_ERROR'}, 500

        except pymysql.err.IntegrityError:
            db_connection.rollback() 
            return {'message' : 'DATABASE_INTERGRITY_ERROR'}, 500

        except Exception as e:
            db_connection.rollback()
            return {'message' : str(e)}, 500     

        finally:
            if db_connection:
                db_connection.close()

    @app.route('/sign-in', methods=['POST'])
    def sign_in():

        """
        로그인 API [POST]
        
        Args:

        user        : 셀러 id
        password    : 비밀번호
        
        Returns:

        Success     : {access_token : token}, 200
        Key error   : {message : KEY_ERROR}, status code : 400
        Type eeror  : {message : Type_ERROR}, status code : 400
        """
        
        db_connection = None 
        get_user = request.json
        try:
            db_connection = get_connection()
            if db_connection:
                sign_in_response = user_service.check_user(get_user, db_connection)

                return sign_in_response

        except pymysql.err.InternalError:       
            return {'message' : 'DATABASE_SERVER_ERROR'}, 500
        
        except pymysql.err.OperationalError:              
            return {'message' : 'DATABASE_ACCESS_DENIED'}, 500

        except pymysql.err.ProgrammingError as e :
            return {'message' : 'DATABASE_PROGRAMMING_ERROR'+ str(e)}, 500

        except pymysql.err.NotSupportedError:
            return {'message' : 'DATABASE_NOT_SUPPORTED_ERROR'}, 500

        except pymysql.err.IntegrityError:  
            return {'message' : 'DATABASE_INTERGRITY_ERROR'}, 500  

        except  Exception as e:
            db_connection.rollback()
            return {'message' : str(e)}, 500

        finally:
            if db_connection:
                db_connection.close()


    @app.route('/sellers', methods=['GET'])
    @authorize
    def seller_list():

        if g.auth is not 1:
            return {'message' : 'UNAUTHORIZED'}, 401

        db_connection = None
        try:
            db_connection = get_connection()
            if db_connection:
                sellers = user_service.get_sellerlist(db_connection)

                return {'number_of_sellers' : len(sellers),
                        'number_of_pages' : int(len(sellers)/10)+1,
                        'sellers' : sellers,
                        }, 200

        except pymysql.err.InternalError as e:
            return {'message': 'DATABASE_SERVER_ERROR' +str(e)}, 500

        except pymysql.err.OperationalError:
            return {'message': 'DATABASE_ACCESS_DENIED'}, 500

        except pymysql.err.ProgrammingError as e:
            return {'message': 'DATABASE_PROGRAMMING_ERROR' + str(e)}, 500

        except pymysql.err.NotSupportedError:
            return {'message': 'DATABASE_NOT_SUPPORTED_ERROR'}, 500

        except pymysql.err.IntegrityError:
            return {'message': 'DATABASE_INTERGRITY_ERROR'}, 500

        except  Exception as e:
            return {'message': str(e)}, 500

        finally:
            if db_connection:
                db_connection.close()
    
    @app.route('/seller', methods = ['POST'])
    def seller_register():
        db_connection = None 
        seller_infos = request.json
        try:
            db_connection = get_connection()
            if db_connection:
                register_response = user_service.register_seller(seller_infos, db_connection)
                db_connection.commit()                
                return register_response

        except pymysql.err.InternalError as e:       

            return {'message' : 'DATABASE_SERVER_ERROR' + str(e)}, 500
        
        except pymysql.err.OperationalError:              
            return {'message' : 'DATABASE_ACCESS_DENIED'}, 500

        except pymysql.err.ProgrammingError:
            return {'message' : 'DATABASE_PROGRAMMING_ERROR'}, 500

        except pymysql.err.NotSupportedError:
            return {'message' : 'DATABASE_NOT_SUPPORTED_ERROR'}, 500

        except pymysql.err.IntegrityError:  
            return {'message' : 'DATABASE_INTERGRITY_ERROR'}, 500

        except Exception as e:
            db_connection.rollback()
            return {'message' : str(e)}, 500    

        finally:
            if db_connection:
                db_connection.close()
    

    @app.route('/seller_details', methods = ['GET'])
    @authorize
    def get_seller_info():

        """
        셀러 상세 (셀러 권한) API [GET]
        
        Args:
        [Header]`
        Authorization : 로그인 토큰

        Returns:

        Success     : {data : user_info}, 200
        
        Key error   : {message : KEY_ERROR}, status code : 400
        Type error   :{message : TYPE_ERROR}, status code : 400
        """

        db_connection = None         
        try:
            db_connection = get_connection()
            if db_connection:
                seller_infos = user_service.get_seller_info(g.user, db_connection)                                
                return seller_infos

        except pymysql.err.InternalError as e:       

            return {'message' : 'DATABASE_SERVER_ERROR' + str(e)}, 500
        
        except pymysql.err.OperationalError:              
            return {'message' : 'DATABASE_ACCESS_DENIED'}, 500

        except pymysql.err.ProgrammingError as e:
            return {'message' : 'DATABASE_PROGRAMMING_ERROR' + str(e)}, 500

        except pymysql.err.NotSupportedError:
            return {'message' : 'DATABASE_NOT_SUPPORTED_ERROR'}, 500

        except pymysql.err.IntegrityError:  
            return {'message' : 'DATABASE_INTERGRITY_ERROR'}, 500

        except Exception as e:
            db_connection.rollback()
            return {'message' : str(e)}, 500  

        finally:
            if db_connection:
                db_connection.close()       