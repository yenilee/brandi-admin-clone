import pymysql

class ProductDao:

    def insert_product(self, product_infos, db_connection):
        cursor = db_connection.cursor()

        insert_product_key_sql = """
        INSERT INTO product_keys(
            created_at,
            product_number,
            seller_key_id
        ) VALUES (
            now(),
            %(product_number)s,
            %(seller_id)s
        );
        """
        cursor.execute(insert_product_key_sql, product_infos)
        product_infos['product_key_id'] = cursor.lastrowid

        product_infos['notices_id'] = None
        if product_infos['is_detail_reference'] is 0:
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
            cursor.execute(insert_notice_sql, product_infos)
            product_infos['notices_id'] = cursor.lastrowid

        insert_product_sql = """
        INSERT INTO products(
            product_key_id,
            notices_id,
            color_filter_id,
            attributes_categories_id,
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
                %(color_filter_id)s,
                %(attributes_categories_id)s,
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
        cursor.execute(insert_product_sql, product_infos)

    def sellers_for_master(self, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)

        get_sellers_sql = """
        SELECT 
            seller_keys.id AS seller_key_id, 
            sellers.name AS seller_name, 
            sellers.profile AS seller_profile_image
        FROM sellers
        INNER JOIN seller_keys ON sellers.seller_key_id = seller_keys.id
        """

        cursor.execute(get_sellers_sql)
        return cursor.fetchall()

    def get_product_first_category(self, user, db_connection):  
        cursor = db_connection.cursor()

        get_attribute_group_sql = """
        SELECT attribute_group_id
        FROM seller_attributes 
        INNER JOIN sellers ON sellers.seller_attribute_id = seller_attributes.id
        WHERE sellers.seller_key_id = %(user)s
        """
        cursor.execute(get_attribute_group_sql, user)

        user['attribute_group_id'] = cursor.fetchone()[0]

        cursor = db_connection.cursor(pymysql.cursors.DictCursor)
        get_categories_sql = """
        SELECT 
            attributes_categories.attribute_group_id, 
            first.id AS first_category_id,
            first.name AS first_category_name,
            second.id AS second_category_id,
            second.name AS second_category_name
        FROM attributes_categories
        INNER JOIN first_categories AS first ON attributes_categories.first_category_id = first.id
        INNER JOIN second_categories AS second ON attributes_categories.second_category_id = second.id
        WHERE attribute_group_id = %(attribute_group_id)s
        """
        cursor.execute(get_categories_sql, user)
        get_categories = cursor.fetchall()

        return get_categories

    def get_product_list(self, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)

        product_list_sql = """

        SELECT 
        DATE_FORMAT(start_date, '%%Y-%%m-%%d %%H:%%i:%%s') AS created_at,
        name 
        FROM products
        """

        cursor.execute(product_list_sql)
        return cursor.fetchall()

        
    
