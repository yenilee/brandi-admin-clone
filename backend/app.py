import datetime

from flask                         import Flask
from flask_cors                    import CORS
from flask.json                    import JSONEncoder

from config                        import db
from model.user_dao                import UserDao
from model.product_dao             import ProductDao
from service.user_service          import UserService
from service.product_service       import ProductService
from controller.user_controller    import create_user_endpoints
from controller.product_controller import create_product_endpoints


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.timedelta):
            return str(obj)
        
        return JSONEncoder.default(self, obj)

def create_app(test_config = None):
    app = Flask(__name__)
    app.debug = True
    app.config['JSON_SORT_KEYS'] = False
    app.json_encoder = CustomJSONEncoder
    CORS(app, resources={r'*' : {'origins': '*'}})

    app.config.from_pyfile('config.py')

    user_dao     = UserDao()
    product_dao  = ProductDao()

    user_service = UserService(user_dao, app.config)
    product_service = ProductService(product_dao, app.config)

    create_user_endpoints(app, user_service)
    create_product_endpoints(app, product_service)

    return app