from flask                      import Flask
from flask_cors                 import CORS

from config                     import db
from model.user_dao             import UserDao
from service.user_service       import UserService
from controller.user_controller import create_user_endpoints

def create_app(test_config = None):
    app = Flask(__name__)
    app.debug = True
    app.config['JSON_SORT_KEYS'] = False
    CORS(app, resources={r'*' : {'origins': '*'}})

    app.config.from_pyfile('config.py')

    user_dao     = UserDao()
    user_service = UserService(user_dao, app.config)
    create_user_endpoints(app, user_service)

    return app