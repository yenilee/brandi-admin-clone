import jwt
import pymysql

from functools  import wraps
from flask      import request, Response, g
from connection import get_connection

from config    import SECRET_KEY, ALGORITHM

def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        """
        로그인 데코레이터
        작성자: 이예은

        request header의 토큰에서 로그인 계정의 고유 ID, 권한 ID 파악
        해당 데코레이터를 추가한 함수에서 g.user & g.auth 로 ID 확인 가능
        """

        if not 'Authorization' in request.headers:
            return {'message' : 'ACCESS NOT ALLOWED'}, 401
        
        access_token = request.headers.get('Authorization')
        try:
            payload = jwt.decode(access_token, SECRET_KEY['secret'], ALGORITHM['algorithm'])

        except jwt.ExpiredSignatureError:
            return {'message' : 'LOGIN EXPIRED'}, 440
            
        except jwt.InvalidTokenError:
            return {'message' : 'INVALID TOKEN'}, 400
        
        g.user = payload['user_id']
        g.auth = payload['authority_id']
            
        return f(*args, **kwargs)
    return decorated_function

def connection_error(f):
    @wraps(f)
    def func_wrapper(*args, **kwargs):
        """
        DB connection error check 데코레이터
        작성자: 이예은

        데이터베이스 관련 에러의 경우 모든 함수에서 동일하게 작동하기 때문에,
        except에서 일괄적으로 return할 수 있도록 별도 데코레이터 생성

        *rollback의 경우 internal error에만 적용하였으며,
        데이터를 get하는 경우에는 무관하고 추가, 수정할 경우에만 해당
        """
        try:
            return f(*args, **kwargs)

        except pymysql.err.InternalError:
            db_connection = get_connection()

            if db_connection:
                db_connection.rollback()

            return {'message': 'DATABASE_SERVER_ERROR'}, 500

        except pymysql.err.OperationalError:
            return {'message': 'DATABASE_ACCESS_DENIED'}, 500

        except pymysql.err.ProgrammingError:
            return {'message': 'DATABASE_PROGRAMMING_ERROR'}, 500

        except pymysql.err.NotSupportedError:
            return {'message': 'DATABASE_NOT_SUPPORTED_ERROR'}, 500

        except pymysql.err.IntegrityError as e:
            return {'message': 'DATABASE_INTERGRITY_ERROR' + str(e)}, 500

        except  Exception as e:
            return {'message': str(e)}, 500

    return func_wrapper