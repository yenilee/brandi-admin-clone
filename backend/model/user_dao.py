import pymysql
import datetime

class UserDao:

    def sign_up_seller_key(self, new_user, db_connection):
        cursor = db_connection.cursor()

        seller_key_insert_sql = """
        INSERT INTO seller_keys(
            user
        ) VALUES (
            %(user)s
            )
        """
        cursor.execute(seller_key_insert_sql, new_user)

    def sign_up_seller(self, new_user, db_connection):
        cursor = db_connection.cursor()

        seller_insert_sql =  """
                INSERT INTO sellers (
                    seller_key_id,
                    authority_id,
                    seller_attribute_id,
                    seller_status_id,
                    password,
                    phone_number,
                    name,
                    eng_name,
                    service_number,
                    site_url,
                    editor,
                    start_date,
                    end_date
                    ) VALUES (
                        (SELECT id FROM seller_keys WHERE user = %(user)s),
                        1,
                        %(seller_attribute_id)s,
                        1,
                        %(password)s,
                        %(phone_number)s,
                        %(name)s,
                        %(eng_name)s,
                        %(service_number)s,
                        %(site_url)s,
                        %(user)s,
                        now(),
                        '2037-12-31 23:59:59'
                        );
                        """

        cursor.execute(seller_insert_sql, new_user)

    def count_seller_id(self, new_user, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)

        check_user_sql = """
        SELECT count(user) AS count
        FROM seller_keys
        WHERE user = %(user)s
        """

        cursor.execute(check_user_sql,new_user)
        user = cursor.fetchone()
        return user

    def check_user(self, get_user, db_connection):
        cursor = db_connection.cursor()

        check_user_sql = """
        SELECT id, user
        FROM seller_keys
        WHERE user = %(user)s
        """

        cursor.execute(check_user_sql, get_user)
        user = cursor.fetchone()
        return user

    def check_password(self, get_user, db_connection):
        cursor = db_connection.cursor()
        check_pw_sql = """
        SELECT password,
            authority_id
        FROM sellers
        WHERE seller_key_id =
            (SELECT id
            FROM seller_keys
            WHERE user = %(user)s)
        """

        cursor.execute(check_pw_sql, get_user)
        password = cursor.fetchone()
        return password

    def get_seller_details(self, user, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)
        seller_infos_get_sql = """
        SELECT
            sellers.id,
            seller_key_id,
            auth.name AS authorization,
            sellers.is_deleted,
            attributes.name AS attribute,
            profile,
            status.name,
            sellers.name AS kor_name,
            eng_name,
            user.user AS user_id,
            background_image,
            simple_introduction,
            detail_introduction,
            site_url,
            service_number,
            zip_code,
            address,
            detail_address,
            bank,
            account_owner,
            bank_account,
            shipping_information,
            refund_information,
            model_height,
            model_size_top,
            model_size_bottom,
            model_size_foot,
            feed_message
        FROM sellers
        INNER JOIN authorities AS auth ON sellers.authority_id = auth.id
        INNER JOIN seller_attributes AS attributes ON sellers.seller_attribute_id = attributes.id
        INNER JOIN seller_status AS status ON sellers.seller_status_id = status.id
        INNER JOIN seller_keys AS user ON sellers.seller_key_id = user.id
        WHERE seller_key_id = %s AND end_date = '2037-12-31 23:59:59';
        """
        cursor.execute(seller_infos_get_sql, user)
        return cursor.fetchall()

    def get_supervisors(self, user, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)
        supervisor_infos_get_sql = """
        SELECT *
        FROM supervisor_infos
        WHERE seller_id = (SELECT id FROM sellers WHERE seller_key_id = %s AND end_date = '2037-12-31 23:59:59');
        """
        cursor.execute(supervisor_infos_get_sql, user)
        return cursor.fetchall()

    def get_buisness_hours(self, user, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)
        buisness_hours_get_sql = """
        SELECT *
        FROM buisness_hours
        WHERE seller_id = (SELECT id FROM sellers WHERE seller_key_id = %s AND end_date = '2037-12-31 23:59:59');
        """
        cursor.execute(buisness_hours_get_sql, user)
        return cursor.fetchall()

    def get_seller_histories(self, user, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)
        seller_histories_get_sql = """
        SELECT
            start_date,
            status.name
        FROM sellers
        INNER JOIN seller_status AS status ON sellers.seller_status_id = status.id
        WHERE seller_key_id = %s AND end_date = '2037-12-31 23:59:59';
        """
        cursor.execute(seller_histories_get_sql, user)
        return cursor.fetchall()

    def update_seller(self, seller_infos, db_connection):
        cursor = db_connection.cursor()
        seller_register_sql = """
        UPDATE sellers
        SET
            profile = %(profile)s,
            background_image = %(background_image)s,
            simple_introduction = %(simple_introduction)s,
            detail_introduction = %(detail_introduction)s,
            site_url = %(site_url)s,
            service_number = %(service_number)s,
            zip_code = %(zip_code)s,
            address = %(address)s,
            detail_address = %(detail_address)s,
            bank = %(bank)s,
            account_owner =  %(account_owner)s,
            bank_account = %(bank_account)s,
            shipping_information = %(shipping_information)s,
            refund_information = %(refund_information)s,
            model_height = %(model_height)s,
            model_size_top = %(model_size_top)s,
            model_size_bottom = %(model_size_bottom)s,
            model_size_foot = %(model_size_foot)s,
            feed_message = %(feed_message)s

        WHERE seller_key_id = %(user)s AND end_date = '2037-12-31 23:59:59'
        """
        cursor.execute(seller_register_sql, seller_infos)

    def insert_supervisor(self, supervisor, db_connection):
        cursor = db_connection.cursor()
        supervisor_register_sql = """
        INSERT INTO supervisor_infos (
           seller_id,
           name,
           phone_number,
           email,
           `order`
        ) VALUES(
            (SELECT id FROM sellers WHERE end_date = '2037-12-31 23:59:59' AND seller_key_id = %(user)s),
            %(supervisor_name)s,
            %(supervisor_phone_number)s,
            %(supervisor_email)s,
            %(order)s
        )
        """
        cursor.execute(supervisor_register_sql, supervisor)

    def insert_buisness_hour(self, buisness_hour, db_connection):
        cursor = db_connection.cursor()
        supervisor_register_sql = """
        INSERT INTO buisness_hours (
           seller_id,
           start_time,
           end_time,
           is_weekend
        ) VALUES (
            (SELECT id FROM sellers WHERE end_date = '2037-12-31 23:59:59' AND seller_key_id = %(user)s),
            %(start_time)s,
            %(end_time)s,
            %(is_weekend)s
        )
        """
        cursor.execute(supervisor_register_sql, buisness_hour)

    def insert_new_seller(self, previous_id, db_connection):

        cursor = db_connection.cursor()
        insert_seller_infos_sql = """
        INSERT INTO sellers (
        seller_key_id,
        authority_id,
        seller_attribute_id,
        seller_status_id,
        editor,
        password,
        phone_number,
        name,
        eng_name,
        service_number,
        site_url,
        start_date,
        end_date
        )
        SELECT
            seller_key_id,
            authority_id,
            seller_attribute_id,
            seller_status_id,
            editor,
            password,
            phone_number,
            name,
            eng_name,
            service_number,
            site_url,
            now(),
            end_date
        FROM
            sellers
        WHERE id = %s;
        """
        cursor.execute(insert_seller_infos_sql, previous_id)

    def update_history(self, previous_id, db_connection):
        cursor = db_connection.cursor()
        insert_seller_infos_sql = """
        UPDATE sellers
        SET end_date = now()
        WHERE id = %s;
        """
        cursor.execute(insert_seller_infos_sql, previous_id)

    def get_previous_id(self, user, db_connection):
        cursor = db_connection.cursor()
        get_previous_id_sql = """
        SELECT id
        FROM sellers
        WHERE seller_key_id = %s AND end_date = '2037-12-31 23:59:59';
        """
        cursor.execute(get_previous_id_sql, user)
        return cursor.fetchone()

    def get_sellerlist(self, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)
        sellers_list_sql = """
        SELECT DISTINCT
            sellers.id AS id,
            seller_keys.user AS seller_id,
            sellers.eng_name AS seller_eng_name,
            sellers.name AS seller_kor_name,
            seller_attributes.id AS seller_attribute_id,
            seller_attributes.name AS seller_attribute_name,
            sellers.seller_status_id AS status_id,
            seller_status.name AS status_name,
            supervisor_infos.name AS manager_name,
            supervisor_infos.phone_number AS manager_phone_number,
            supervisor_infos.email AS manager_email,
            (SELECT COUNT('product_keys.product_number')
                FROM product_keys
                WHERE sellers.seller_key_id = product_keys.seller_key_id) AS number_of_product,
            sellers.site_url AS site_url,
            DATE_FORMAT(start_date, '%Y-%m-%d %H:%i:%s') AS created_at
        FROM sellers
        INNER JOIN seller_keys ON sellers.seller_key_id = seller_keys.id
        INNER JOIN seller_status ON sellers.seller_status_id = seller_status.id
        INNER JOIN seller_attributes ON sellers.seller_attribute_id = seller_attributes.id
        LEFT JOIN `supervisor_infos` ON supervisor_infos.seller_id = sellers.id AND supervisor_infos.order=1
        LEFT JOIN product_keys ON sellers.seller_key_id = product_keys.seller_key_id
        WHERE end_date = '2037-12-31 23:59:59' AND authority_id = 2
        ORDER BY sellers.id DESC;
        """
        cursor.execute(sellers_list_sql)
        sellers = cursor.fetchall()
        return sellers

    def get_seller_action(self, db_connection):
        cursor = db_connection.cursor()
        seller_actions_sql = """
        SELECT seller_status_id, action_type
        FROM seller_actions
        """
        cursor.execute(seller_actions_sql)
        seller_actions = cursor.fetchall()
        return seller_actions


