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

    def insert_manufacturer(self, product_manufacturer, db_connection):
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
        affected_row = cursor.execute(insert_notice_sql, product_manufacturer)

        if affected_row == -1:
            raise Exception("CANNOT INSERT DATA")
        notice_id = cursor.lastrowid

        return notice_id

    def find_tags(self, tag_name, db_connection):
        cursor = db_connection.cursor()

        find_tags_sql = """
        SELECT id
        FROM tags
        WHERE name = %s
        """

        affected_row = cursor.execute(find_tags_sql, tag_name)
        if affected_row == 0:
            return 0

        tag_id = cursor.fetchone()[0]
        return tag_id

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


        if 0 < int(product['discount_rate']) < 100:
            insert_product_sql = """
            INSERT INTO products(
                discount_rate,
                discount_start,
                discount_end
                ) VALUES (
                    %(discount_rate)s,
                    %(discount_start)s,
                    %(discount_end)s
                    );
            """
        if int(product['discount_rate']) == 0:
            insert_product_sql = """
            INSERT INTO products(
                discount_rate,
                discount_start,
                discount_end
                ) VALUES (
                    0,
                    '1970-01-01 23:59:59',
                    '1970-01-01 23:59:59'
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
        affected_row = cursor.executemany(insert_option_sql, options)

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
                (SELECT user FROM seller_keys WHERE id = %(seller_key_id)s),
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
        # 필터링된 상품 리스트     
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
            filter_statement = filter_statement + " AND products.name LIKE '%" + filters['product_name'] + "%'"
        # 상품 코드
        if 'product_code' in filters:
            filter_statement = filter_statement + ' AND product_keys.product_number=' + "'" + filters['product_code'] + "'"
        # 상품 번호 (product pk)   
        if 'product_number' in filters:
            filter_statement = filter_statement + ' AND product_keys.id=' + "'" + filters['product_number'] + "'"
        # 판매 여부
        if 'is_onsale' in filters:
            filter_statement = filter_statement + ' AND products.is_onsale=' + filters['is_onsale']
        # 진열 여부
        if 'is_displayed' in filters:
            filter_statement = filter_statement + ' AND products.is_displayed=' + filters['is_displayed']
        # 할인 여부
        if 'is_discount' in filters:
            filter_statement = filter_statement + ' AND (products.discount_rate != 0 AND now() BETWEEN products.discount_start AND products.discount_end)=' + filters['is_discount']
        # 셀러 속성
        if 'seller_attribute_id' in filters:
            # 셀러 속성 ID를 모두 가져온다
            seller_attributes = filters.getlist('seller_attribute_id')
            filter_statement = filter_statement + ' AND (sellers.seller_attribute_id = ' + seller_attributes[0]
            # 다중 셀러 속성 필터링 구문 추가
            for seller_attribute in seller_attributes:
                filter_statement = filter_statement + ' OR sellers.seller_attribute_id = ' + seller_attribute
            filter_statement = filter_statement + ')'

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
            filter_statement = filter_statement + " AND products.name LIKE '%" + filters['product_name'] + "%'"
        # 상품 코드
        if 'product_code' in filters:
            filter_statement = filter_statement + ' AND product_keys.product_number=' + "'" + filters['product_code'] + "'"
        # 상품 번호 (product pk)    
        if 'product_number' in filters:
            filter_statement = filter_statement + ' AND product_keys.id=' + "'" + filters['product_number'] + "'"
        # 판매 여부
        if 'is_onsale' in filters:
            filter_statement = filter_statement + ' AND products.is_onsale=' + filters['is_onsale']
        # 진열 여부
        if 'is_displayed' in filters:
            filter_statement = filter_statement + ' AND products.is_displayed=' + filters['is_displayed']
        # 할인 여부
        if 'is_discount' in filters:
            filter_statement = filter_statement + ' AND (products.discount_rate != 0 AND now() BETWEEN products.discount_start AND products.discount_end)=' + filters['is_discount']
        # 셀러 속성
        if 'seller_attribute_id' in filters:
            # 셀러 속성 ID를 모두 가져온다
            seller_attributes = filters.getlist('seller_attribute_id')
            filter_statement = filter_statement + ' AND (sellers.seller_attribute_id = ' + seller_attributes[0]
            # 다중 셀러 속성 필터링 구문 추가
            for seller_attribute in seller_attributes:
                filter_statement = filter_statement + ' OR sellers.seller_attribute_id = ' + seller_attribute
            filter_statement = filter_statement + ')'

        # 필터링 구문 종합 상품 등록일 내림차순
        filter_statement = filter_statement + ' ORDER BY product_keys.created_at DESC;'
    
        cursor.execute(products_list_sql + filter_statement)
        # 필터링된 상품의 개수를 return 
        return cursor.fetchone()[0]

    def get_product_previous_id(self, product, db_connection):
        # 가장 최근에 수정된 레코드의 id를 가져온다
        cursor = db_connection.cursor()
        get_recent_product_id_sql = """
        SELECT id
        FROM products
        WHERE product_key_id = %s AND end_date = '2037-12-31 23:59:59';
        """
        cursor.execute(get_recent_product_id_sql, product)
        return cursor.fetchone()[0]

    def get_recent_product(self, product_previous_id, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)
        get_recent_product_sql = """
        SELECT
            products.is_deleted,
            products.product_key_id,
            product_keys.product_number,
            products.name,
            products.is_onsale,
            products.is_displayed,
            products.simple_description,
            products.details,
            products.wholesale_price,
            price,
            discount_rate,
            DATE_FORMAT(products.discount_start, '%%Y-%%m-%%d %%H:%%i:%%s') as discount_start,
            DATE_FORMAT(products.discount_end,'%%Y-%%m-%%d %%H:%%i:%%s') as discount_end,
            products.minimum_quantity,
            products.maximum_quantity,
            DATE_FORMAT(product_keys.created_at, '%%Y-%%m-%%d %%H:%%i:%%s') as created_at,
            DATE_FORMAT(products.start_date, '%%Y-%%m-%%d %%H:%%i:%%s') as start_date,
            DATE_FORMAT(products.end_date, '%%Y-%%m-%%d %%H:%%i:%%s') as end_date,
            notices.manufacturer,
            notices.manufacture_date,
            notices.origin,
            attributes_categories.id  as attribute_category_id,
            products_tags.tag_id
        FROM products
        INNER JOIN product_keys ON product_keys.id = products.product_key_id
        INNER JOIN notices ON products.notices_id = notices.id
        INNER JOIN color_filters ON color_filters.id = products.color_filter_id
        INNER JOIN attributes_categories ON attributes_categories.id = products.attributes_categories_id
        INNER JOIN products_tags ON products_tags.id = products.id 
        WHERE products.id = %s
        """
        cursor.execute(get_recent_product_sql, product_previous_id)
        return cursor.fetchall()

    def update_recent_product_history(self, previous_id, db_connection):
        # 이전의 셀러 레코드의 유효종료일을 현재 시점으로 업데이트
        cursor = db_connection.cursor()
        update_product_end_date_sql = """
        UPDATE products
        SET end_date = now()
        WHERE id = %s;
        """
        cursor.execute(update_product_end_date_sql, previous_id)
        return cursor.fetchone[0]

    def update_product(self, product, db_connection):
        cursor = db_connection.cursor()
        update_product_sql = """
        UPDATE products
        SET
            %(notices_id)s,
            %(attributes_categories_id)s,
            %(color_filter_id)s,
            %(is_displayed)s,
            %(is_onsale)s,
            %(name)s,
            %(is_detail_reference)s,
            %(start_date)s,
            %(end_date)s,
            %(simple_description)s,
            %(details)s,
            %(editor)s,
            %(maximum_quantity)s,
            %(minimum_quantity)s,
            %(discount_rate)s,
            %(price)s,
            %(wholesale_price)s,
            %(discount_start)s,
            %(discount_end)s
        WHERE product_key_id = % AND end_date = '2037-12-31 23:59:59'
        """
        cursor.execute(update_product_sql, product)
