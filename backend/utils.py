import jwt
import pymysql

from functools  import wraps
from flask      import request, Response, g
from connection import get_connection

from config    import SECRET_KEY, ALGORITHM

def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
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