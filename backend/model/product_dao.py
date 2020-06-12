import pymysql

class ProductDao:

    def insert_product_key(self, seller_key_id, db_connection):
        cursor = db_connection.cursor()
        insert_product_key_sql = """
        INSERT INTO product_keys(
            created_at,
            product_number,
            seller_key_id
        ) VALUES (
            now(),
            "default",
            %s
        )
        """
        affected_row = cursor.execute(insert_product_key_sql, seller_key_id)
        if affected_row == -1:
            raise Exception("CANNOT INSERT DATA")

        product_key_id = cursor.lastrowid
        return product_key_id

    def update_product_number(self, db_connection):
        cursor = db_connection.cursor()
        insert_product_number_sql = """
         UPDATE product_keys SET product_number = (SELECT CONCAT ('BRANDI', (SELECT max(id))))
         WHERE product_number = "default";
         """
        affected_row = cursor.execute(insert_product_number_sql)
        if affected_row == -1:
            raise Exception("CANNOT INSERT DATA")

    def insert_manufacturer(self, product, db_connection):
        cursor = db_connection.cursor()
        insert_notice_sql = """
        INSERT INTO notices(
            manufacturer,
            manufacture_date,
            origin
            ) VALUES (
                %(manufacturer)s,
                %(manufacture_date)s,
                %(origin)s
            );
        """
        affected_row = cursor.execute(insert_notice_sql, product)

        if affected_row == -1:
            raise Exception("CANNOT INSERT DATA")
        notice_id = cursor.lastrowid

        return notice_id

    def insert_tags(self, tag, db_connection):
        cursor = db_connection.cursor()

        insert_tags_sql = """
        INSERT INTO tags(name) VALUES (%s)
        """

        affected_row = cursor.execute(insert_tags_sql, tag)

        if affected_row == -1:
            raise Exception("CANNOT INSERT DATA")

        tags = cursor.lastrowid

        return tags

    def insert_product_tags(self, product_id, tag_id, db_connection):
        cursor = db_connection.cursor()

        insert_product_tags_sql = """
        INSERT INTO products_tags(
            product_id,
            tag_id
            ) VALUES (
            %s,
            %s
            )
        """
        cursor.execute(insert_product_tags_sql, (product_id, tag_id))

    def insert_discount(self, product, db_connection):
        cursor = db_connection.cursor()
        insert_product_sql = """
        INSERT INTO products(
            discount_rate,
            wholesale_price,
            discount_start,
            discount_end
            ) VALUES (
                %(discount_rate)s,
                %(wholesale_price)s,
                %(discount_start)s,
                %(discount_end)s
                );
        """
        affected_row = cursor.execute(insert_product_sql, product)

        if affected_row == -1:
            raise Exception("CANNOT INSERT DATA")

    def insert_options(self, options, db_connection):
        cursor = db_connection.cursor()
        insert_option_sql = """
        INSERT INTO products_options(
            product_id,
            size_id,
            color_id,
            quantity
            ) VALUES (
            %(product_id)s,
            %(size_id)s,
            %(color_id)s,
            %(quantity)s
            )
        """
        affected_row = cursor.execute(insert_option_sql, options)

        if affected_row == -1:
            raise Exception("CANNOT INSERT DATA")

    def insert_product(self, product, db_connection):
        cursor = db_connection.cursor()
        insert_product_sql = """
        INSERT INTO products(
            product_key_id,
            notices_id,
            attributes_categories_id,
            color_filter_id,
            is_displayed,
            is_onsale,
            name,
            is_detail_reference,
            start_date,
            end_date,
            simple_description,
            details,
            editor,
            maximum_quantity,
            minimum_quantity,
            discount_rate,
            price,
            wholesale_price,
            discount_start,
            discount_end
            ) VALUES (
                %(product_key_id)s,
                %(notices_id)s,
                %(attribute_category_id)s,
                %(color_filter_id)s,
                %(is_displayed)s,
                %(is_onsale)s,
                %(name)s,
                %(is_detail_reference)s,
                now(),
                "2037-12-31 23:59:59",
                %(simple_description)s,
                %(details)s,
                %(seller_key_id)s,
                %(maximum_quantity)s,
                %(minimum_quantity)s,
                %(discount_rate)s,
                %(price)s,
                %(wholesale_price)s,
                %(discount_start)s,
                %(discount_end)s
                );
        """
        cursor.execute(insert_product_sql, product)
        return cursor.lastrowid

    def get_colors(self, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)
        get_colors = "SELECT id, name FROM colors"
        cursor.execute(get_colors)

        return cursor.fetchall()

    def get_sizes(self, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)
        get_sizes = "SELECT id, name FROM sizes"
        cursor.execute(get_sizes)

        return cursor.fetchall()

    def get_attribute_category_id(self, product, db_connection):
        cursor = db_connection.cursor()

        get_attribute_category_id_sql = """
        SELECT attributes_categories.id
        FROM attributes_categories
        WHERE attribute_group_id = %(attribute_group_id)s
        AND first_category_id = %(first_category_id)s
        AND second_category_id = %(second_category_id)s
        """
        cursor.execute(get_attribute_category_id_sql, product)
        attribute_category_id = cursor.fetchone()[0]

        return attribute_category_id

    def get_sellers_for_master(self, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)

        get_sellers_sql = """
        SELECT
            seller_keys.id AS seller_key_id,
            sellers.name AS seller_name,
            sellers.profile AS seller_profile_image
        FROM sellers
        INNER JOIN seller_keys ON sellers.seller_key_id = seller_keys.id
        WHERE sellers.authority_id = 2 
        AND sellers.end_date = '2037-12-31 23:59:59'
        """

        affected_row = cursor.execute(get_sellers_sql)
        if affected_row == 0:
            raise Exception("DATA DOES NOT EXIST")

        return cursor.fetchall()

    def get_attribute_group_id(self, seller_key_id, db_connection):
        cursor = db_connection.cursor()

        get_attribute_group_sql = """
        SELECT attribute_group_id
        FROM seller_attributes
        INNER JOIN sellers ON sellers.seller_attribute_id = seller_attributes.id
        WHERE sellers.seller_key_id = %s
        """
        cursor.execute(get_attribute_group_sql, seller_key_id)
        attribute_group_id = cursor.fetchone()[0]
        return attribute_group_id

    def get_first_category(self, attribute_group_id, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)
        get_categories_sql = """
        SELECT DISTINCT
            attributes_categories.attribute_group_id,
            first.id AS first_category_id,
            first.name AS first_category_name
        FROM attributes_categories
        INNER JOIN first_categories AS first ON attributes_categories.first_category_id = first.id
        WHERE attribute_group_id = %s
        """
        cursor.execute(get_categories_sql, attribute_group_id)
        get_categories = cursor.fetchall()

        return get_categories

    def get_second_category(self, attribute_group_id, first_category_id, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)
        get_categories_sql = """
        SELECT DISTINCT
            second.id AS second_category_id,
            second.name AS second_category_name
        FROM attributes_categories
        INNER JOIN second_categories AS second ON attributes_categories.second_category_id = second.id
        WHERE attribute_group_id = %s
        AND first_category_id = %s
        """
        cursor.execute(get_categories_sql, (attribute_group_id, first_category_id))
        get_categories = cursor.fetchall()

        return get_categories

    def get_color_filters(self, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)

        get_color_filter_sql = """
        SELECT
            id,
            name,
            eng_name,
            image
        FROM color_filters
        """
        cursor.execute(get_color_filter_sql)
        color_filters = cursor.fetchall()
        return color_filters

    def get_productlist(self, filters, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)      
        # 할인가 할인줄일 때는 할인율 계산하는 로직을 짜서 구현, 할인중이 아닐때는 판매가로 
        products_list_sql = """
        SELECT
        products.id,
        product_keys.id AS product_keys_id,
        DATE_FORMAT(product_keys.created_at, '%Y-%m-%d %H:%i:%s') AS created_at,    
        products.name AS name,
        product_keys.product_number AS product_code,
        seller_attributes.name AS seller_attributes_name,
        seller_keys.user,        
        products.price AS price, 
        IF(products.discount_rate != 0 AND now() BETWEEN products.discount_start AND products.discount_end, CAST((products.price - (products.discount_rate / 100 * products.price)) AS signed), products.price) AS discount_price,
        products.discount_rate,
        is_onsale,
        is_displayed,
        IF(products.discount_rate != 0 AND now() BETWEEN products.discount_start AND products.discount_end, 1, 0) AS is_discount          
        FROM
        products
        INNER JOIN product_keys ON products.product_key_id = product_keys.id
        INNER JOIN seller_keys ON product_keys.seller_key_id = seller_keys.id      
        INNER JOIN sellers ON seller_keys.id = sellers.seller_key_id AND sellers.end_date = '2037-12-31 23:59:59'
        INNER JOIN seller_attributes ON sellers.seller_attribute_id = seller_attributes.id
        WHERE products.end_date = '2037-12-31 23:59:59' AND authority_id = 2   
        """

        # 필터링 구문
        filter_statement = ""

        # 셀러명이 포함된 검색기능
        if 'user' in filters:
            filter_statement = filter_statement + " AND seller_keys.user LIKE '%" + filters['user'] + "%'"
        # 상품명이 포함된 검색기능
        if 'product_name' in filters:
            filter_statement = filter_statement + " AND products.name LIKE '%" + filters['user'] + "%'"
        # 상품 코드
        if 'product_code' in filters:
            filter_statement = filter_statement + ' AND product_keys.product_number=' + "'" + filters['product_code'] + "'"
        # 셀러 속성
        if 'seller_attribute_id' in filters:
            filter_statement = filter_statement + ' AND sellers.seller_attribute_id=' + filters['seller_attribute_id']
        # 판매 여부
        if 'is_onsale' in filters:
            filter_statement = filter_statement + ' AND products.is_onsale=' + filters['is_onsale']
        # 진열 여부
        if 'is_displayed' in filters:
            filter_statement = filter_statement + ' AND products.is_displayed=' + filters['is_displayed']
        # 할인 여부
        if 'is_discount' in filters:
            filter_statement = filter_statement + ' AND (products.discount_rate != 0 AND now() BETWEEN products.discount_start AND products.discount_end)=' + filters['is_discount']

        # 필터링 구문 종합 상품 등록일 내림차순
        filter_statement = filter_statement + ' ORDER BY product_keys.created_at DESC;' 
        # 리스트 조회 쿼리에서 반환된 row의 개수를 담는다
        cursor.execute(products_list_sql + filter_statement)

        # 상품 리스트와 상품의 개수를 return
        return cursor.fetchall()
        
    def get_product_count(self, filters, db_connection):
        # 필터링된 상품 개수
        cursor = db_connection.cursor()      
        products_list_sql = """
        SELECT
        COUNT(products.id) AS product_count        
        FROM
        products
        INNER JOIN product_keys ON products.product_key_id = product_keys.id
        INNER JOIN seller_keys ON product_keys.seller_key_id = seller_keys.id      
        INNER JOIN sellers ON seller_keys.id = sellers.seller_key_id AND sellers.end_date = '2037-12-31 23:59:59'
        WHERE products.end_date = '2037-12-31 23:59:59' AND authority_id = 2
        """

        # 필터링 구문
        filter_statement = ""

        # 셀러명이 포함된 검색기능
        if 'user' in filters:
            filter_statement = filter_statement + " AND seller_keys.user LIKE '%" + filters['user'] + "%'"
        # 상품명이 포함된 검색기능
        if 'product_name' in filters:
            filter_statement = filter_statement + " AND products.name LIKE '%" + filters['user'] + "%'"
        # 상품 코드
        if 'product_code' in filters:
            filter_statement = filter_statement + ' AND product_keys.product_number=' + "'" + filters['product_code'] + "'"
        # 셀러 속성
        if 'seller_attribute_id' in filters:
            filter_statement = filter_statement + ' AND sellers.seller_attribute_id=' + filters['seller_attribute_id']
        # 판매 여부
        if 'is_onsale' in filters:
            filter_statement = filter_statement + ' AND products.is_onsale=' + filters['is_onsale']
        # 진열 여부
        if 'is_displayed' in filters:
            filter_statement = filter_statement + ' AND products.is_displayed=' + filters['is_displayed']
        # 할인 여부
        if 'is_discount' in filters:
            filter_statement = filter_statement + ' AND (products.discount_rate != 0 AND now() BETWEEN products.discount_start AND products.discount_end)=' + filters['is_discount']
    
        cursor.execute(products_list_sql + filter_statement)

        # 검색된 상품의 개수를 return
        return cursor.fetchone()[0]

    def get_recent_product_id(self, product, db_connection):
        # 가장 최근에 수정된 레코드의 id를 가져온다
        cursor = db_connection.cursor()
        get_recent_product_id_sql = """
        SELECT id
        FROM products
        WHERE product_key_id = %s AND end_date = '2037-12-31 23:59:59';
        """
        cursor.execute(get_recent_product_id_sql, product)
        return cursor.fetchone()

    def get_recent_product(self, product, db_connection):
        cursor = db_connection.cursor()
        get_recent_product_sql = """
        SELECT * FROM products 
        WHERE product_key_id = %s
        """
        cursor.execute( get_recent_product_sql, product)
        return cursor.fetchone()



