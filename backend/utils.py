import jwt

from functools import wraps
from flask     import request, Response, g
from config    import SECRET_KEY, ALGORITHM

def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'Authorization' in request.headers:
            return '', 401
        
        access_token = request.headers.get('Authorization')
        try:
            payload = jwt.decode(access_token, SECRET_KEY['secret'], ALGORITHM['algorithm'])

        except jwt.InvalidTokenError:
            payload = None
            return '', 400
            
        user = payload['user_id']
        g.user = user 
        auth = payload['authority_id']
        g.auth = auth 
            
        return f(*args, **kwargs)
    return decorated_function()
