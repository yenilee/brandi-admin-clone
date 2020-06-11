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
        cursor.execute(seller_key_insert_sql, new_user)

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

        cursor.execute(seller_insert_sql, new_user)
        return cursor.lastrowid

    def count_seller_id(self, new_user, db_connection):
        # 셀러 ID로 가입된 셀러 존재 여부 확인
        # COUNT가 0일 아닐 경우 : 셀러 중복   
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)

        check_user_sql = """
        SELECT COUNT(user) AS count
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
        # cursor.execute 결과를 확인해 SELECT에 걸린 상품이 하나도 없으면 0을 리턴
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
        start_time,
        end_time,
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
            DATE_FORMAT(start_date, '%%Y-%%m-%%d %%H:%%i:%%s') AS created_at,
            status.name,
            editor
        FROM sellers
        INNER JOIN seller_status AS status ON sellers.seller_status_id = status.id
        WHERE seller_key_id = %s AND end_date = '2037-12-31 23:59:59';
        """
        cursor.execute(seller_histories_get_sql, user)
        return cursor.fetchall()

    def update_seller(self, seller_infos, db_connection):
        #  셀러 나머지 정보 (한줄 소개, 간략 소개, 배경 이미지, 계좌 정보, 배송, 환불 정보 등) 업데이트
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
        # 담당자 정보 삽입
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
        cursor.execute(supervisor_register_sql, buisness_hour)

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
        )
        """
        cursor.execute(supervisor_register_sql, new_user)

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
        )
        """
        cursor.execute(supervisor_register_sql, new_user)

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
        cursor.execute(insert_first_supervisor_sql, user_id)

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
        cursor.execute(insert_first_buisness_hour_sql, user_id)  

    def insert_new_seller(self, recent_id, db_connection):
        #셀러 정보 수정 시 가장 최근 셀러 기록에서 기본정보 (셀러 키 ID, 권한, 속성, 셀러 정보, 비밀번호, 이름, 영문 이름를 가져와 새로운 셀러 레코드 생성
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
        cursor.execute(insert_seller_infos_sql, recent_id)

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
        cursor.execute(get_recent_seller_id_sql, user)
        return cursor.fetchone()

    def get_seller_list(self, filters, db_connection):
        cursor = db_connection.cursor(pymysql.cursors.DictCursor)

        # 밑에서 추가할 SQL statement를 정의
        statement = ""

        # controller에서 받아온 쿼리스트링이 None이 아닌 경우, SQL statement에 filter 값을 WHERE문에 추가
        if filters is not None:
            for key in filters.keys():
                statement += f" AND {key}=" + str(filters[f'{key}'])
                print(statement)

        sellers_list_sql = """
        SELECT DISTINCT
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
            DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at
        FROM sellers
        INNER JOIN seller_keys ON sellers.seller_key_id = seller_keys.id
        INNER JOIN seller_status ON sellers.seller_status_id = seller_status.id
        INNER JOIN seller_attributes ON sellers.seller_attribute_id = seller_attributes.id
        LEFT JOIN `supervisor_infos` ON supervisor_infos.seller_id = sellers.id AND supervisor_infos.order=1
        LEFT JOIN product_keys ON sellers.seller_key_id = product_keys.seller_key_id
        WHERE end_date = '2037-12-31 23:59:59' 
        AND (authority_id = 2 OR authority_id = 3) """ + statement + " ORDER BY sellers.id DESC"

        if cursor.execute(sellers_list_sql) == 0:
            return 0
        sellers = cursor.fetchall()
        return sellers

    def get_next_status(self, action_type, db_connection):
        cursor = db_connection.cursor()
        change_status_sql = """
        SELECT next_status_id 
        FROM seller_actions
        WHERE action_type = %(action_type)s
        """
        cursor.execute(change_status_sql, action_type)
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
        cursor.execute(update_seller_all_sql, user)
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

    def update_authority(self, user, db_connection):
        cursor = db_connection.cursor()
        update_status_sql = """
        UPDATE sellers SET authority_id = %s
        WHERE id = %s
        """
        cursor.execute(update_status_sql, (2, user))
