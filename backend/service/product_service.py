import math

from const import AUTH

class ProductService:

    def __init__(self, product_dao, config):
        self.product_dao = product_dao
        self.config   = config

    def get_sellers_for_master(self, auth, filters, db_connection):
        try:
            # 권한 ID가 마스터가 아닐 경우 권한 없음 에러 메시지 표시
            if auth is not AUTH['MASTER']:
                return {'message': 'UNAUTHORIZED'}, 401

            # 셀러 권한 ID들의 한국 이름, 프로필 불러오기
            sellers_kor_names = self.product_dao.get_sellers_for_master(filters, db_connection)
            return sellers_kor_names

        except KeyError as e:
            return {'message': 'KEY_ERROR' + str(e)}, 400

        except TypeError as e:
            return {'message': 'TYPE ERROR' + str(e)}, 400

    def registration_page_color_filter(self, db_connection):
        try:
            # 색상 필터 id, 이름, 이미지 url 불러오기
            color_filters = self.product_dao.get_color_filters(db_connection)
            return color_filters

        except KeyError as e:
            return {'message': 'KEY_ERROR' + str(e)}, 400

        except TypeError as e:
            return {'message': 'TYPE ERROR' + str(e)}, 400

    def registration_page_options(self, db_connection):
        try:
            # 색상 선택지, 사이즈 선택지 불러오기
            colors = self.product_dao.get_colors(db_connection)
            sizes = self.product_dao.get_sizes(db_connection)

            return {'option_color'     : colors,
                    'option_size'      : sizes}

        except KeyError as e:
            return {'message': 'KEY_ERROR' + str(e)}, 400

        except TypeError as e:
            return {'message': 'TYPE ERROR' + str(e)}, 400

    def get_attribute_id(self, seller_key_id, db_connection):
        try:
            attribute_id = self.product_dao.get_seller_attribute(seller_key_id, db_connection)

            return attribute_id

        except KeyError:
            return {'message': 'KEY_ERROR'}, 400

        except TypeError as e:
            return {'message': 'TYPE ERROR' + str(e)}, 400

    def get_first_category(self, seller_key_id, db_connection):
        try:
            # 셀러 속성 정보를 기반으로 상품 속성 그룹을 불러오기
            attribute_group_id = self.product_dao.get_attribute_group_id(seller_key_id, db_connection)

            # 셀러 속성 그룹 ID를 선택했을 때 보여지는 1차 카테고리 불러오기
            categories = self.product_dao.get_first_category(attribute_group_id, db_connection)

            first_categories = [
                {'id': category['first_category_id'],
                 'name': category['first_category_name']
                 } for category in categories]

            return first_categories

        except KeyError as e:
            return {'message': 'KEY_ERROR' + str(e)}, 400

        except TypeError as e:
            return {'message': 'TYPE ERROR' + str(e)}, 400

    def get_second_category(self, seller_key_id, first_category_id, db_connection):
        try:
            # 셀러 속성 정보를 기반으로 속성 그룹 ID를 불러오기
            attribute_group_id = self.product_dao.get_attribute_group_id(seller_key_id, db_connection)

            # request body에 저장된 1차 카테고리, 위에서 가져온 상품 속성 그룹을 넣어 2차 카테고리 불러오기
            categories = self.product_dao.get_second_category(attribute_group_id, first_category_id, db_connection)

            second_categories = [
                {'id': category['second_category_id'],
                 'name': category['second_category_name']} for category in categories]

            return {'second_categories':second_categories}, 200

        except KeyError as e:
            return {'message': 'KEY_ERROR' + str(e)}, 400

        except TypeError as e:
            return {'message': 'TYPE ERROR' + str(e)}, 400

    def create_new_product(self, product, seller_key_id, db_connection):
        try:
            # 할인율은 명시되었는데 기간이 없을 때, 에러 메시지를 띄워줌
            if product['discount_rate'] is not None and product['discount_rate'] is not 0:
                if product['discount_start'] is None or product['discount_end'] is None:
                    return {'message' : 'DISCOUNT PERIOD NEEDED'}

            # request value 중 option은 리스트 안에 딕셔너리가 여러개 있는 형태이므로, 우선 제외하고 데이터 insert
            options = product.pop('options', None)

            # 상품 KEY ID insert하고, 해당 row에 상품 번호(문자+숫자 조합)를 추가
            product['product_key_id'] = self.product_dao.insert_product_key(seller_key_id, db_connection)
            self.product_dao.update_product_number(db_connection)

            # 상품 고시 정보를 상세 상품 정보에 표시할 경우 notices id를 null 값으로 표시
            product['notices_id'] = None

            # 상세 상품 정보에 기입하지 않고 직접 등록할 경우 제조 관련 정보를 field(3개) insert
            if product['is_detail_reference'] is 0:
                notice_id_check = self.product_dao.select_notices_id(product['manufacture'], db_connection)

                if notice_id_check is 0:
                    product['notices_id'] = self.product_dao.insert_manufacturer(product['manufacture'], db_connection)

            # 셀러 속성 값에 따른 셀러 속성 그룹, 속성 그룹 id+카테고리 id 조합을 변수에 저장
            product['attribute_group_id'] = self.product_dao.get_attribute_group_id(seller_key_id, db_connection)

            product['attribute_category_id'] = self.product_dao.get_attribute_category_id(product, db_connection)
            if product['attribute_category_id'] == 0:
                return {'message': 'NO COMBINATION AVAILABLE'}, 400

            # request body에서 받은 id와 데이터 조합으로 Product 등록
            product_id = self.product_dao.insert_product(product, db_connection)

            # product id를 options의 각 딕셔너리에 담고, option 조합 db에 추가
            for option in options:
                option['product_id'] = product_id

            self.product_dao.insert_options(options, db_connection)

            # tag가 db에 없을 경우 db에 태그를 추가한 뒤 id를 받고, 있을 경우 id를 찾아서 tag_id 리스트에 추가함
            tags = []
            for tag_name in product['tags']:
                tag_check = self.product_dao.find_tags(tag_name, db_connection)

                if tag_check is 0:
                    tags.append(self.product_dao.insert_tags(tag_name, db_connection))
                else:
                    tags.append(tag_check)

            # db에 있는 태그의 id, 혹은 새로 받은 태그의 id를 상품 & 태그 조합 테이블에 추가
            [self.product_dao.insert_product_tags(product_id, tag_id, db_connection) for tag_id in tags]

            return "", 200

        except KeyError as e:
            db_connection.rollback()
            return {'message': 'KEY_ERROR' + str(e)}, 400

        except TypeError as e:
            db_connection.rollback()
            return {'message': 'TYPE ERROR' + str(e)}, 400

    def get_product(self, product_key_id, seller_key_id, db_connection):
        try:
            # 셀러가 가진 상품 key ID를 찾고, 선분 이력으로 가장 최근에 저장된 상품 ID를 가져옴
            recent_product = self.product_dao.get_recent_product(product_key_id, seller_key_id, db_connection)

            # 만약 리턴되는 ID가 없을 경우, DB에 없는 상품이므로 선택되지 않았다는 메시지를 보내줌
            if recent_product is 0:
                return {'message' : 'NO PRODUCT SELECTED'}, 400

            # DB에서 불러온 최근 상품의 id를 변수에 저장
            recent_product_id = recent_product['id']

            recent_product['options'] = self.product_dao.get_recent_options(recent_product_id, db_connection)

            if recent_product['is_detail_reference'] == 0:
                recent_product['manufacture'] = self.product_dao.get_recent_manufacture(recent_product_id, db_connection)

            tags = self.product_dao.get_tag(recent_product_id, db_connection)
            tag_list = []

            [tag_list.append(tag['name']) for tag in tags]
            recent_product['tags'] = tag_list

            return {'product_detail' : recent_product}, 200

        except KeyError as e:
            return {'message': 'KEY_ERROR' + str(e)}, 400

        except TypeError as e:
            return {'message': 'TYPE ERROR' + str(e)}, 400

    def update_product(self, product_key_id, product, db_connection):
        try:
            options = product.pop('options', None)

            # 상품 key id로 최근에 수정한 상품 id를 가져온다
            product_previous_id = self.product_dao.get_product_previous_id(product_key_id, db_connection)
            if product_previous_id == 0:
                return {'message' : 'NO SELLER SELECTED'}, 400

            # 최근에 수정한 상품의 종료일을 바꿔준다
            self.product_dao.update_product_history(product_previous_id, db_connection)

            # 최근 상품 id의 내용을 그대로 가져와서 새로운 상품 id로 row를 추가해준다
            product['product_id'] = self.product_dao.copy_previous_product(product_previous_id, db_connection)
            product_id = product['product_id']

            # 상세 상품 정보에 기입하지 않고 직접 등록할 경우 제조 관련 정보를 field(3개) insert
            # 추가 하기 전 동일한 정보가 있다면 id를 받아오고, 없을 경우 새롭게 추가한다
            notices_id = self.product_dao.select_notices_id(product['notices'], db_connection)
            product['notices_id'] = notices_id

            if notices_id is 0:
                product['notices_id'] = self.product_dao.insert_manufacturer(product['notices'], db_connection)

            # request로 받아온 상품 정보를 업데이트 한다
            self.product_dao.update_product(product, db_connection)

            # product id를 options의 각 딕셔너리에 담고, option 조합 db에 추가
            for option in options:
                option['product_id'] = product['product_id']

            self.product_dao.insert_options(options, db_connection)

            # tag가 db에 없을 경우 db에 태그를 추가한 뒤 id를 받고, 있을 경우 id를 찾아서 tag_id 리스트에 추가함
            tags = []
            for tag_name in product['tags']:
                tag_check = self.product_dao.find_tags(tag_name, db_connection)

                if tag_check is 0:
                    tags.append(self.product_dao.insert_tags(tag_name, db_connection))
                else:
                    tags.append(tag_check)

            # db에 있는 태그의 id, 혹은 새로 받은 태그의 id를 상품 & 태그 조합 테이블에 추가
            [self.product_dao.insert_product_tags(product_id, tag_id, db_connection) for tag_id in tags]

            return "", 200

        except KeyError as e:
            return {'message': 'KEY_ERROR' + str(e)}, 400

        except TypeError as e:
            return {'message': 'TYPE ERROR' + str(e)}, 400

    def get_product_history(self, product_key_id, db_connection):
        try:
            product_history = self.product_dao.get_product_history(product_key_id, db_connection)

            if product_history is 0:
                return {'message' : 'PRODUCT DOES NOT EXIST'}

            return {'history' : product_history}

        except KeyError as e:
            return {'message': 'KEY_ERROR' + str(e)}, 400

        except TypeError as e:
            return {'message': 'TYPE ERROR' + str(e)}, 400

    def get_product_list(self, seller_info, filters, db_connection):
        try:        
            products = self.product_dao.get_productlist(seller_info, filters, db_connection)
            count    = self.product_dao.get_product_count(seller_info, filters, db_connection)

            #product_count   : 검색된 상품의 개수
            #number_of_pages : 페이지 개수 (한 페이지당 10개의 상품) 
            #products        : 상품 리스트            
            return {
                'product_count'   : count,
                'number_of_pages' : math.ceil(count / 10),
                'products'        : products}, 200

        except KeyError:           
            return {'message': 'KEY_ERROR'}, 400

        except TypeError:
            return {'message': 'TYPE ERROR'}, 400