import pymysql
import json
import boto3

from collections import defaultdict
from PIL         import Image

from config      import S3

class ProductService:

    def __init__(self, product_dao, config):
        self.product_dao = product_dao
        self.config   = config
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id     = S3['S3_ACCESS_KEY'],
            aws_secret_access_key = S3['S3_SECRET_KEY']
        )

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

    def resize_image(self, image_url, db_connection):

        IMAGE_SMALL  = (150, 150)
        IMAGE_MEDIUM = (320, 320)
        IMAGE_LARGE  = (640, 640)

        image = Image.open(image_url)

        image_large  = image.resize(IMAGE_LARGE)
        image_medium = image.resize(IMAGE_MEDIUM)
        image_small  = image.resize(IMAGE_SMALL)

        filename = 'test'
        # image_large.show()
        # image_medium.show()
        # image_small.show()
       
        self.s3.upload_file(
            image_url,
            self.config['S3']['S3_BUCKET'],
            "image_large"
        )

    def get_product_list(self, db_connection):
        try:
            product = self.product_dao.get_product_list(db_connection)
            return {'first_categories' : product}, 200

        except KeyError as e:
            db_connection.rollback()
            return {'message': 'KEY_ERROR' + str(e)}, 400

        except TypeError as e:
            db_connection.rollback()
            return {'message': 'TYPE ERROR' + str(e)}, 400