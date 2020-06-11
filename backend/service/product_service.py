import pymysql
import json
import boto3

from collections   import defaultdict
# from PIL         import Image
# from config      import S3

class ProductService:

    def __init__(self, product_dao, config):
        self.product_dao = product_dao
        self.config   = config
        # self.s3 = boto3.client(
        #     "s3",
        #     aws_access_key_id     = S3['S3_ACCESS_KEY'],
        #     aws_secret_access_key = S3['S3_SECRET_KEY']
        # )

    def create_new_product(self, product, seller_key_id, db_connection):
        try:
            # 상품 KEY ID insert
            product['seller_key_id'] = seller_key_id
            product['product_key_id'] = self.product_dao.insert_product_key(seller_key_id, db_connection)

            # 위에서 등록한 KEY ID row에 상품 코드(문자+숫자 조합) 업데이트
            self.product_dao.update_product_number(db_connection)

            # 상품 옵션(색상, 사이즈 조합) insert
            # self.product_dao.insert_options(product, db_connection)

            # 상품 고시 정보를 상세 상품 정보에 표시할 경우 notices id를 null 값으로 표시
            product['notices_id'] = None

            # 상세 상품 정보에 기입하지 않고 직접 등록할 경우 제조 관련 정보를 field(3개) insert

            if product['is_detail_reference'] is 0:
                product['notices_id'] = self.product_dao.insert_manufacturer(product['manufacture'], db_connection)


            # 셀러 속성 값에 따른 셀러 속성 그룹 id를 변수에 저장
            product['attribute_group_id'] = self.product_dao.get_attribute_group_id(seller_key_id, db_connection)
            product['attribute_category_id'] = self.product_dao.get_attribute_category_id(product, db_connection)

            # request body를 insert
            # 위에서 받은 속성 그룹 id와 1, 2차 카테고리 조합해 속성 카테고리 조합 id 등록
            product_id = self.product_dao.insert_product(product, db_connection)

            # 여러개의 상품 태그를 리스트에 담아 받고, 반복분으로 각각 insert
            tags = [self.product_dao.insert_tags(tag, db_connection) for tag in product['tag_name']]

            for tag_id in tags:
                self.product_dao.insert_product_tags(product_id, tag_id, db_connection)

            return "", 200

        except KeyError as e:
            db_connection.rollback()
            return {'message': 'KEY_ERROR' + str(e)}, 400

        except TypeError as e:
            db_connection.rollback()
            return {'message': 'TYPE ERROR' + str(e)}, 400

    def get_sellers_for_master(self, auth, db_connection):
        try:
            # 권한 ID가 마스터가 아닐 경우 권한 없음 에러 미시지 표시
            if auth is not 1:
                return {'message': 'UNAUTHORIZED'}, 401

            # 셀러 권한 ID들의 한국 이름, 프로필 불러오기
            sellers_kor_names = self.product_dao.get_sellers_for_master(db_connection)
            return sellers_kor_names

        except KeyError as e:
            db_connection.rollback()
            return {'message': 'KEY_ERROR' + str(e)}, 400

        except TypeError as e:
            return {'message': 'TYPE ERROR' + str(e)}, 400

    def get_register_page(self, seller_key_id, db_connection):
        try:
            # 셀러 속성 정보를 기반으로 상품 속성 그룹을 불러오기
            attribute_group_id = self.product_dao.get_attribute_group_id(seller_key_id, db_connection)

            # 셀러 속성 그룹 ID를 선택했을 때 보여지는 1차 카테고리 불러오기
            categories = self.product_dao.get_first_category(attribute_group_id, db_connection)

            first_categories = [
                {'id' : category['first_category_id'],
                 'name' : category['first_category_name']
            } for category in categories ]

            # 색상 필터 id, 이름, 이미지 url 불러오기
            color_filters = self.product_dao.get_color_filters(db_connection)

            # 색상 선택지, 사이즈 선택지 불러오기
            colors = self.product_dao.get_colors(db_connection)
            sizes = self.product_dao.get_sizes(db_connection)

            return {'first_categories' : first_categories,
                    'color_filters'    : color_filters,
                    'option_color'     : colors,
                    'option_size'      : sizes}

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

    def get_second_category(self, seller_key_id, first_category_id, db_connection):
        try:
            # 셀러 속성 정보를 기반으로 속성 그룹 IDfmf 불러오기
            attribute_group_id = self.product_dao.get_attribute_group_id(seller_key_id, db_connection)

            # request body에 저장된 1차 카테고리, 위에서 가져온 상품 속성 그룹을 넣어 2차 카테고리 불러오기
            categories = self.product_dao.get_second_category(attribute_group_id, first_category_id, db_connection)

            second_categories = [
                {'id': category['second_category_id'],
                 'name': category['second_category_name']} for category in categories]

            return {'second_categories':second_categories}, 200

        except KeyError as e:
            db_connection.rollback()
            return {'message': 'KEY_ERROR' + str(e)}, 400

        except TypeError as e:
            db_connection.rollback()
            return {'message': 'TYPE ERROR' + str(e)}, 400

    def get_product_list(self, filters, db_connection):
        try:            
            
            products, count = self.product_dao.get_productlist(filters, db_connection)

            #product_count : 검색된 상품의 개수
            #products      : 상품 리스트
            return {
            'product_count' : count,
            'products' : products}, 200

        except KeyError:           
            return {'message': 'KEY_ERROR'}, 400

        except TypeError:            
            return {'message': 'TYPE ERROR'}, 400