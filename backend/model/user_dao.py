import pymysql
import datetime

class UserDao:

    def sign_up_seller_key(self, new_user, db_connection):
        # 셀러 고유 ID 저장 
        cursor = db_connection.cursor()

        seller_key_insert_sql = """
        INSERT INTO seller_keys(
            user
        ) VALUES (
            %(user)s
            )
        """
        affected_row = cursor.execute(seller_key_insert_sql, new_user)
        if affected_row == -1:
            raise Exception("CANNOT INSERT DATA")

    def sign_up_seller(self, new_user, db_connection):
        # 회원가입 시 필요한 셀러 정보 저장 
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
                        3,
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

        affected_row = cursor.execute(seller_insert_sql, new_user)
        if affected_row == -1:
            raise Exception("CANNOT INSERT DATA")

        return cursor.lastrowid

    def count_seller_id(self, new_user, db_connection):
        # 셀러 ID로 가입된 셀러 존재 여부 확인
        # COUNT가 0일 아닐 경우 : 셀러 중복   
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)

        check_user_sql = """
        SELECT
            COUNT(user) AS count
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

    def check_user_auth(self, get_user, db_connection):
        cursor = db_connection.cursor()

        check_user_auth_sql = """
        SELECT authority_id
        FROM sellers
        INNER JOIN seller_keys ON seller_keys.id = sellers.seller_key_id
        WHERE seller_keys.user = %(user)s AND end_date = '2037-12-31 23:59:59'
        """
        cursor.execute(check_user_auth_sql, get_user)
        user = cursor.fetchone()[0]

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
        #셀러 상세 정보 조회
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
        # cursor.execute 결과를 확인해 SELECT에 걸린 셀러가 하나도 없으면 0을 리턴
        if cursor.execute(seller_infos_get_sql, user) == 0:
            return 0

        return cursor.fetchall()

    def get_supervisors(self, user, db_connection):
        #셀러 담당자 정보 조회
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)
        supervisor_infos_get_sql = """
        SELECT 
            name as supervisor_name,
            phone_number as supervisor_phone_number,
            email as supervisor_email,
            `order`
        FROM supervisor_infos
        WHERE seller_id = (SELECT id FROM sellers WHERE seller_key_id = %s AND end_date = '2037-12-31 23:59:59');
        """
        cursor.execute(supervisor_infos_get_sql, user)
        return cursor.fetchall()

    def get_buisness_hours(self, user, db_connection):
        #셀러 영업시간 조회
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)
        buisness_hours_get_sql = """
        SELECT
            id,
            seller_id,
            TIME_FORMAT(start_time, '%%H:%%i:%%s') AS start_time,
            TIME_FORMAT(end_time, '%%H:%%i:%%s') AS end_time,
            is_weekend,
            is_deleted
        FROM buisness_hours
        WHERE seller_id = (SELECT id FROM sellers WHERE seller_key_id = %s AND end_date = '2037-12-31 23:59:59');
        """
        cursor.execute(buisness_hours_get_sql, user)
        return cursor.fetchall()

    def get_seller_histories(self, user, db_connection):
        #셀러상태 변경기록 조회
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)
        seller_histories_get_sql = """
        SELECT
            DATE_FORMAT(MAX(start_date), '%%Y-%%m-%%d %%H:%%i:%%s') AS created_at,
            status.name,
            sellers.editor AS editor
        FROM
        sellers
        INNER JOIN seller_status AS status ON sellers.seller_status_id = status.id
        WHERE seller_key_id = %s
        GROUP BY status.name, sellers.editor
        ORDER BY created_at
        """
        cursor.execute(seller_histories_get_sql, user)
        return cursor.fetchall()

    def update_seller(self, seller_infos, db_connection):
        #  가장 최신의 셀러 나머지 정보 
        # (한줄 소개, 간략 소개, 배경 이미지, 계좌 정보, 배송, 환불 정보, 변경 실행자 등) 업데이트
        cursor = db_connection.cursor()
        seller_register_sql = """
        UPDATE sellers
        SET
            profile              = %(profile)s,
            background_image     = %(background_image)s,
            simple_introduction  = %(simple_introduction)s,
            detail_introduction  = %(detail_introduction)s,
            site_url             = %(site_url)s,
            service_number       = %(service_number)s,
            zip_code             = %(zip_code)s,
            address              = %(address)s,
            detail_address       = %(detail_address)s,
            bank                 = %(bank)s,
            account_owner        = %(account_owner)s,
            bank_account         = %(bank_account)s,
            shipping_information = %(shipping_information)s,
            refund_information   = %(refund_information)s,
            model_height         = %(model_height)s,
            model_size_top       = %(model_size_top)s,
            model_size_bottom    = %(model_size_bottom)s,
            model_size_foot      = %(model_size_foot)s,
            feed_message         = %(feed_message)s,
            editor               = (SELECT user from seller_keys WHERE id = %(editor)s)     
        WHERE seller_key_id = %(user)s AND end_date = '2037-12-31 23:59:59'
        """
        affected_row = cursor.execute(seller_register_sql, seller_infos)
        if affected_row == -1:
            raise Exception("CANNOT UPDATE DATA")

    def insert_supervisor(self, supervisor, db_connection):
        # 가장 최신 셀러 ID에 담당자 정보 삽입
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
        affected_row = cursor.execute(supervisor_register_sql, supervisor)
        if affected_row == -1:
            raise Exception("CANNOT INSERT DATA")

    def insert_buisness_hour(self, buisness_hour, db_connection):
        # 영업시간 정보 삽입
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
        affected_row = cursor.execute(supervisor_register_sql, buisness_hour)
        if affected_row == -1:
            raise Exception("CANNOT INSERT DATA")

    def insert_initial_supervisor(self, new_user, db_connection):
        # 초기 회원가입 시 담당자 정보에 셀러 핸드폰번호 초기화
        cursor = db_connection.cursor()
        supervisor_register_sql = """
        INSERT INTO supervisor_infos (
           seller_id,
           phone_number,
           `order`
        ) VALUES (
            %(last_row_id)s,
            %(service_number)s,
            1
        ),
        (
            %(last_row_id)s,
            null,
            2
        ),
        (
            %(last_row_id)s,
            null,
            3
        )
        """
        affected_row = cursor.execute(supervisor_register_sql, new_user)
        if affected_row == -1:
            raise Exception("CANNOT INSERT DATA")

    def insert_initial_buisness_hours(self, new_user, db_connection):
        # 초기 회원가입 시 담당자 정보에 셀러 영업시간 초기화
        cursor = db_connection.cursor()
        supervisor_register_sql = """
        INSERT INTO buisness_hours (
           seller_id,
           start_time,
           end_time,
           is_weekend
        ) VALUES (
            %(last_row_id)s,
            '09:00:00',
            '18:00:00',
            0
        ),
        (
            %(last_row_id)s,
            null,
            null,
            1
        )
        """
        affected_row = cursor.execute(supervisor_register_sql, new_user)
        if affected_row == -1:
            raise Exception("CANNOT INSERT DATA")

    def update_supervisor(self, user_id, db_connection):
        # 셀러의 이전 ID 값의 담당자 정보를 새롭게 업데이트 해준다 
        cursor = db_connection.cursor()
        insert_first_supervisor_sql = """
        INSERT INTO supervisor_infos (
            seller_id,
            name,
            phone_number,
            email,
            `order`
        )
        SELECT
            %(recent_id)s,
            name,
            phone_number,
            email,
            `order`
        FROM
        supervisor_infos
        WHERE seller_id = %(previous_id)s
        """
        affected_row = cursor.execute(insert_first_supervisor_sql, user_id)
        if affected_row == -1:
            raise Exception("CANNOT INSERT DATA")

    def update_buisness_hour(self, user_id, db_connection):
        # 셀러의 이전 ID 값의 고객센터 영업시간 정보를 새롭게 업데이트 해준다 
        cursor = db_connection.cursor()
        insert_first_buisness_hour_sql = """
        INSERT INTO buisness_hours (
            seller_id,
            start_time,
            end_time,
            is_weekend
        )
        SELECT
            %(recent_id)s,
            start_time,
            end_time,
            is_weekend
        FROM
        buisness_hours
        WHERE seller_id = %(previous_id)s
        """
        affected_row = cursor.execute(insert_first_buisness_hour_sql, user_id)
        if affected_row == -1:
            raise Exception("CANNOT INSERT DATA")  

    def update_history(self, previous_id, db_connection):
        # 이전의 셀러 레코드의 유효종료일을 현재 시점으로 업데이트
        cursor = db_connection.cursor()
        insert_seller_infos_sql = """
        UPDATE sellers
        SET end_date = now()
        WHERE id = %s;
        """
        cursor.execute(insert_seller_infos_sql, previous_id)

    def get_recent_seller_id(self, user, db_connection):
        # 가장 최근에 수정된 셀러 레코드의 id를 가져온다 
        cursor = db_connection.cursor()
        get_recent_seller_id_sql = """
        SELECT id
        FROM sellers
        WHERE seller_key_id = %s AND end_date = '2037-12-31 23:59:59';
        """
        affected_row = cursor.execute(get_recent_seller_id_sql, user)
        if affected_row == 0:
            return 0
        return cursor.fetchone()[0]

    def get_seller_list(self, filters, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)

        statement = ""
        equal_search = ['sellers.id', 'sellers.seller_status_id', 'sellers.seller_attribute_id']
        like_search = ['seller_keys.user', 'sellers.eng_name', 'sellers.name', 'supervisor_infos.name',
                       'supervisor_infos.phone_number', 'supervisor_infos.email']

        offset_statement = " OFFSET 1"

        if filters is not None:
            for k, v in filters.items():
                if k in equal_search:
                    statement += f" AND {k} = {v}"
                    offset_statement = ""

                if k in like_search:
                    statement += f" AND {k} LIKE '%{v}%'"
                    offset_statement = ""

                if k == 'pages':
                    if v is not '1':
                        v = (int(v) - 1) * 10 + 1
                        offset_statement = f" OFFSET {v}"

        sellers_list_sql = """
        SELECT DISTINCT
            sellers.is_deleted,
            sellers.id AS id,
            seller_keys.user AS seller_id,
            seller_keys.id AS seller_key_id,
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
            DATE_FORMAT(seller_keys.created_at, '%Y-%m-%d %H:%i:%s') AS created_at
        FROM sellers
        INNER JOIN seller_keys ON sellers.seller_key_id = seller_keys.id
        INNER JOIN seller_status ON sellers.seller_status_id = seller_status.id
        INNER JOIN seller_attributes ON sellers.seller_attribute_id = seller_attributes.id
        LEFT JOIN `supervisor_infos` ON supervisor_infos.seller_id = sellers.id AND supervisor_infos.order=1
        LEFT JOIN product_keys ON sellers.seller_key_id = product_keys.seller_key_id
        WHERE end_date = '2037-12-31 23:59:59' 
        AND sellers.seller_status_id <> 6 
        AND sellers.seller_status_id <> 7
        AND (authority_id = 2 OR authority_id = 3)""" + statement + " ORDER BY sellers.id DESC LIMIT 10" + offset_statement
    
        if cursor.execute(sellers_list_sql) == 0:
            return 0

        sellers = cursor.fetchall()
        return sellers

    def get_next_status(self, action_type_name, db_connection):
        cursor = db_connection.cursor()
        change_status_sql = """
        SELECT next_status_id 
        FROM seller_actions
        WHERE action_type = %(action_type)s
        """
        affected_row = cursor.execute(change_status_sql, action_type_name)
        if affected_row == 0:
            return 0

        next_status_id = cursor.fetchone()[0]
        return next_status_id

    def update_seller_all(self, user, db_connection):
        cursor = db_connection.cursor()
        update_seller_all_sql = """
        INSERT INTO sellers(
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
            end_date,
            profile,
            background_image, 
            simple_introduction, 
            detail_introduction, 
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
            ) SELECT 
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
                '2037-12-31 23:59:59',
                profile,
                background_image, 
                simple_introduction, 
                detail_introduction, 
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
            WHERE id = %s;
        """
        sellers = cursor.execute(update_seller_all_sql, user)
        if sellers == 0:
            return 0

        return cursor.lastrowid

    def update_status(self, next_status_id, user, db_connection):
        cursor = db_connection.cursor()
        update_status_sql = """
        UPDATE sellers SET seller_status_id = %s
        WHERE id = %s
        """
        cursor.execute(update_status_sql, (next_status_id, user))

    def get_seller_action(self, db_connection):
        cursor = db_connection.cursor()
        seller_actions_sql = """
        SELECT seller_status.id, action_type
        FROM seller_actions
        INNER JOIN seller_status ON seller_actions.seller_status_id = seller_status.id
        """
        cursor.execute(seller_actions_sql)
        seller_actions = cursor.fetchall()
        return seller_actions

    def update_authority(self, authority_user, db_connection):
        cursor = db_connection.cursor()
        update_status_sql = """
        UPDATE sellers SET authority_id = %s
        WHERE id = %s
        """
        cursor.execute(update_status_sql, (2, authority_user))

    def soft_delete_seller(self, seller_key_id, db_connection):
        cursor = db_connection.cursor()
        soft_delete_seller_sql = """
        UPDATE sellers
        SET is_deleted = 1
        WHERE id = %s AND end_date = '2037-12-31 23:59:59';
        """
        cursor.execute(soft_delete_seller_sql, seller_key_id)

    def get_number_of_sellers(self, db_connection):

        cursor = db_connection.cursor()
        get_number_of_sellers_sql = """
        SELECT count(seller_key_id)
        FROM sellers
        WHERE end_date = '2037-12-31 23:59:59'
        """
        affected_row = cursor.execute(get_number_of_sellers_sql)
        if affected_row == 0:
            return 0

        return cursor.fetchone()[0]
 
