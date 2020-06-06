import json
from collections import defaultdict

class ProductService:

    def __init__(self, product_dao, config):
        self.product_dao = product_dao
        self.config   = config

    def create_new_product(self, product_infos, db_connection):
        try:
            self.product_dao.insert_product(product_infos, db_connection)
            return "", 200

        except KeyError as e:
            db_connection.rollback()
            return {'message': 'KEY_ERROR' + str(e)}, 400

        except TypeError as e:
            db_connection.rollback()
            return {'message': 'TYPE ERROR' + str(e)}, 400

    def sellers_kor_names(self, user, db_connection):
        try:
            if user is not 1:
                return {'message' : 'NOT AUTHORIZED'}, 400

            sellers_kor_names = self.product_dao.sellers_for_master(db_connection)
            return sellers_kor_names

        except KeyError as e:
            db_connection.rollback()
            return {'message': 'KEY_ERROR' + str(e)}, 400

        except TypeError as e:
            return {'message': 'TYPE ERROR' + str(e)}, 400

    def get_product_first_categories(self, user, db_connection):
        try:
            categories = self.product_dao.get_product_first_category(user, db_connection)

            first_categories = []
            [ first_categories.append(category['first_category_name'])
              for category in categories if category['first_category_name'] not in first_categories]

            return {'first_categories' : first_categories }, 200

        except KeyError as e:
            db_connection.rollback()
            return {'message': 'KEY_ERROR' + str(e)}, 400

        except TypeError as e:
            db_connection.rollback()
            return {'message': 'TYPE ERROR' + str(e)}, 400
