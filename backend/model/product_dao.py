import pymysql

class ProductDao:

    def insert_product_key(self, product, db_connection):
        cursor = db_connection.cursor()
        insert_product_key_sql = """
        INSERT INTO product_keys(
            created_at,
            product_number,
            seller_key_id
        ) VALUES (
            now(),
            "default",
            %(seller_id)s
        )
        """
        affected_row = cursor.execute(insert_product_key_sql, product)
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
        INSERT INTO tags (name) VALUES (%s);
        """
        affected_row = cursor.execute(insert_tags_sql, tag)

        if affected_row == -1:
            raise Exception("CANNOT INSERT DATA")

        tag_id = cursor.lastrowid
        return tag_id

    def insert_product_tags(self, product_id, tag, db_connection):
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
        cursor.execute(insert_product_tags_sql, (product_id, tag))

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

    def insert_options(self, product, db_connection):
        cursor = db_connection.cursor()
        insert_option_sql = """
        INSERT INTO products_options(
            product_id,
            size_id,
            color_id,
            quantity
            ) VALUES (
            %(product_key_id)s,
            (SELECT id FROM sizes WHERE name = %(size)s),
            (SELECT id FROM colors WHERE name = %(color)s),
            %(quantity)s
        """
        affected_row = cursor.execute(insert_option_sql, product)

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
                (SELECT id FROM attributes_categories
                WHERE attribute_group_id = %(attribute_group_id)s
                AND first_category_id = %(first_category_id)s
                AND second_category_id = %(second_category_id)s),
                %(color_filter_id)s,
                %(is_displayed)s,
                %(is_onsale)s,
                %(name)s,
                %(is_detail_reference)s,
                now(),
                "2037-12-31 23:59:59",
                %(simple_description)s,
                %(details)s,
                (SELECT user FROM seller_keys WHERE id = %(seller_id)s),
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

    def get_attribute_group_id(self, user, db_connection):
        cursor = db_connection.cursor()

        get_attribute_group_sql = """
        SELECT attribute_group_id
        FROM seller_attributes
        INNER JOIN sellers ON sellers.seller_attribute_id = seller_attributes.id
        WHERE sellers.seller_key_id = %(seller_id)s
        """
        cursor.execute(get_attribute_group_sql, user)
        attribute_group_id = cursor.fetchone()[0]
        return attribute_group_id

    def get_first_category(self, user, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)
        get_categories_sql = """
        SELECT DISTINCT
            attributes_categories.attribute_group_id,
            first.id AS first_category_id,
            first.name AS first_category_name
        FROM attributes_categories
        INNER JOIN first_categories AS first ON attributes_categories.first_category_id = first.id
        WHERE attribute_group_id = %(attribute_group_id)s
        """
        cursor.execute(get_categories_sql, user)
        get_categories = cursor.fetchall()

        return get_categories

    def get_second_category(self, product, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)
        get_categories_sql = """
        SELECT DISTINCT
            second.id AS second_category_id,
            second.name AS second_category_name
        FROM attributes_categories
        INNER JOIN second_categories AS second ON attributes_categories.second_category_id = second.id
        WHERE attribute_group_id = %(attribute_group_id)s
        AND first_category_id = %(first_category_id)s
        """
        cursor.execute(get_categories_sql, product)
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

    def get_productlist(self, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)
        # 판매 미판매 여부는 boolean field라서 IF 구문을 활용해 1이면 판매, 0이면 미판매 문자열을 출력
        # 할인가는 판매가 - 할인율 계산하는 로직을 짜서 구현
        # 할인여부는 IF 구문을 사용해 할인율이 0이 아니면 '할인', 0이면 '미할인'

        products_list_sql = """
        SELECT
        products.id,
        product_keys.id AS product_keys_id,
        DATE_FORMAT(product_keys.created_at, '%Y-%m-%d %H:%i:%s') AS created_at,    
        products.name AS name,
        product_keys.product_number,
        seller_attributes.name AS seller_attributes_name,
        seller_keys.user,        
        CAST(products.price AS unsigned) AS price, 
        CAST((products.price - (products.discount_rate / 100 * products.price)) AS unsigned) AS discount_price,
        is_onsale,
        is_displayed,
        IF(products.discount_rate != 0, 1, 0) AS is_discount        
        FROM
        products
        INNER JOIN product_keys ON products.product_key_id = product_keys.id
        INNER JOIN seller_keys ON product_keys.seller_key_id = seller_keys.id      
        INNER JOIN sellers ON seller_keys.id = sellers.seller_key_id AND sellers.end_date = '2037-12-31 23:59:59'
        INNER JOIN seller_attributes ON sellers.seller_attribute_id = seller_attributes.id
        WHERE products.end_date = '2037-12-31 23:59:59' AND authority_id = 2       
        ORDER BY products.id DESC;
        """

        # cursor.execute 결과를 확인해 SELECT에 걸린 상품이 하나도 없으면 0을 리턴
        if cursor.execute(products_list_sql) == 0:
            return 0  

        return cursor.fetchall()
