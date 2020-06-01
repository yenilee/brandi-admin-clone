from flask      import Flask
from flask_cors import CORS

from config     import db
from model.user_dao import UserDao
from service.user_service    import UserService
from view       import create_endpoints

class Services:
    pass

def create_app(test_config = None):
    app = Flask(__name__)
    app.debug = True
    CORS(app)

    if test_config is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.update(test_config)

    user_dao = UserDao()
    services = Services
    services.user_service = UserService(user_dao, app.config)

    create_endpoints(app, services)
    return app
