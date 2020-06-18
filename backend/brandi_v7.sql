CREATE TABLE first_categories
(
    `id`          INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `is_deleted`  TINYINT        NOT NULL    DEFAULT 0  COMMENT '삭제여부', 
    `name`        VARCHAR(10)    NOT NULL    COMMENT '카테고리 이름', 
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE first_categories COMMENT '1차 카테고리 (아우터, 상의, 스커트, 바지, 원피스, 신발, 가방';

CREATE TABLE attribute_groups
(
    `id`    INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `name`  VARCHAR(45)    NOT NULL    COMMENT '그룹 이름', 
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE attribute_groups COMMENT '셀러 정보 그룹';

CREATE TABLE second_categories
(
    `id`                 INT             NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `is_deleted`         TINYINT         NOT NULL    DEFAULT 0  COMMENT '삭제여부', 
    `name`               VARCHAR(100)    NOT NULL    COMMENT '카테고리 이름', 
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE second_categories COMMENT '2차 카테고리 (코트, 점퍼, 재킷, 가디건 등)';

CREATE TABLE seller_attributes
(
    `id`                  INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `attribute_group_id`  INT            NOT NULL    COMMENT '셀러속성 그룹 ID', 
    `is_deleted`          TINYINT        NOT NULL    DEFAULT 0  COMMENT '삭제 여부', 
    `name`                VARCHAR(45)    NOT NULL    COMMENT '카테고리 이름', 
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE seller_attributes COMMENT '셀러 속성 (쇼핌몰, 마켓, 로드샵/ 디자이너브랜드, 제너럴브랜드,내셔널브랜드 / 뷰티)';

ALTER TABLE seller_attributes
    ADD CONSTRAINT FK_seller_attributes_attribute_group_id_attribute_groups_id FOREIGN KEY (attribute_group_id)
        REFERENCES attribute_groups (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

CREATE TABLE `seller_keys` (
  `id`         int(11)                                 NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `user`       varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '아이디',
  `created_at` timestamp                               NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='셀러 키';

CREATE TABLE `notices` (
  `id`               int(11)                                 NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `is_deleted`       tinyint(4)                              NOT NULL DEFAULT '0' COMMENT '삭제 여부',
  `manufacturer`     varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '제조사(수입사)',
  `manufacture_date` date DEFAULT                            NULL COMMENT '제조일자',
  `origin`           varchar(45) COLLATE utf8mb4_unicode_ci  NOT NULL COMMENT '원산지',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='상품 정보 고시';

ALTER TABLE notices COMMENT '상품 정보 고시';

CREATE TABLE color_filters
(
    `id`          INT              NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `is_deleted`  TINYINT          NOT NULL    DEFAULT 0   COMMENT '삭제 여부', 
    `name`        VARCHAR(45)      NOT NULL    COMMENT '색상 이름(한글)', 
    `eng_name`    VARCHAR(45)      NOT NULL    COMMENT '색상 이름(영문)', 
    `image`       VARCHAR(100)     NOT NULL    COMMENT '이미지', 
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE color_filters COMMENT '색상 필터명';

CREATE TABLE product_keys
(
    `id`              INT         NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `seller_key_id`   INT         NULL        COMMENT '셀러 키 ID', 
    `product_number`  VARCHAR(20) NOT NULL    COMMENT '상품번호', 
    `created_at`      TIMESTAMP   NULL        DEFAULT CURRENT_TIMESTAMP        COMMENT '생성일', 
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE product_keys COMMENT '제품 키';

ALTER TABLE product_keys
    ADD CONSTRAINT FK_product_keys_seller_key_id_seller_keys_id FOREIGN KEY (seller_key_id)
        REFERENCES seller_keys (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

CREATE TABLE attributes_categories
(
    `id`                  INT    NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `attribute_group_id`  INT    NOT NULL    COMMENT '셀러 속성 ID', 
    `first_category_id`   INT    NOT NULL    COMMENT '1차 카테고리 ID', 
    `second_category_id`  INT                COMMENT '2차 카테고리 ID', 
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE attributes_categories COMMENT '셀러 속성, 1,2차 카테고리 조합';

ALTER TABLE attributes_categories
    ADD CONSTRAINT FK_attributes_categories_attribute_group_id_attribute_group_id FOREIGN KEY (attribute_group_id)
        REFERENCES attribute_groups (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE attributes_categories
    ADD CONSTRAINT FK_attributes_categories_first_category_id_first_categories_id FOREIGN KEY (first_category_id)
        REFERENCES first_categories (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE attributes_categories
    ADD CONSTRAINT FK_attributes_categories_second_category_id_second_categories_id FOREIGN KEY (second_category_id)
        REFERENCES second_categories (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

CREATE TABLE products
(
    `id`                        INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `product_key_id`            INT            NULL        COMMENT '상품 KEY ID', 
    `notices_id`                INT            NULL        DEFAULT NULL COMMENT '상품 정보 고시 ID', 
    `attributes_categories_id`  INT            NULL        COMMENT '속성, 카테고리 조합 ID', 
    `color_filter_id`           INT            NULL        COMMENT '색상 필터 ID', 
    `is_deleted`                TINYINT        NOT NULL    DEFAULT 0   COMMENT '삭제 여부', 
    `is_detail_reference`       TINYINT        NOT NULL    COMMENT '상품 상세 참조', 
    `name`                      VARCHAR(45)    NOT NULL    COMMENT '상품명', 
    `simple_description`        VARCHAR(50)    NULL        COMMENT '한줄 상품 설명', 
    `details`                   LONGTEXT       NOT NULL    COMMENT '상세 상품 정보', 
    `wholesale_price`           INT            NULL        COMMENT '도매 원가', 
    `discount_start`            TIMESTAMP      NULL        DEFAULT CURRENT_TIMESTAMP        COMMENT '할인기간 시작', 
    `discount_end`              TIMESTAMP      NULL        DEFAULT CURRENT_TIMESTAMP        COMMENT '할인기간 종료', 
    `minimum_quantity`          INT            NOT NULL    COMMENT '최소 판매 수량', 
    `maximum_quantity`          INT            NOT NULL    COMMENT '최대 판매 수량', 
    `start_date`                TIMESTAMP      NOT NULL    DEFAULT CURRENT_TIMESTAMP    COMMENT '유효시작일', 
    `end_date`                  TIMESTAMP      NOT NULL    DEFAULT CURRENT_TIMESTAMP    COMMENT '유효종료일', 
    `is_onsale`                 TINYINT        NOT NULL    COMMENT '판매여부', 
    `is_displayed`              TINYINT        NOT NULL    COMMENT '진열여부', 
    `price`                     INT            NOT NULL    COMMENT '판매가격', 
    `discount_rate`             INT            NULL        COMMENT '할인율', 
    `editor`                    VARCHAR(45)    NOT NULL    COMMENT '수정자', 
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE products COMMENT '상품';

ALTER TABLE products
    ADD CONSTRAINT FK_products_notices_id_notices_id FOREIGN KEY (notices_id)
        REFERENCES notices (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE products
    ADD CONSTRAINT FK_products_color_filter_id_color_filters_id FOREIGN KEY (color_filter_id)
        REFERENCES color_filters (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE products
    ADD CONSTRAINT FK_products_product_key_id_product_keys_id FOREIGN KEY (product_key_id)
        REFERENCES product_keys (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE products
    ADD CONSTRAINT FK_products_attributes_categories_id_attributes_categories_id FOREIGN KEY (attributes_categories_id)
        REFERENCES attributes_categories (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

CREATE TABLE seller_status
(
    `id`          INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `is_deleted`  TINYINT        NOT NULL    DEFAULT 0   COMMENT '삭제 여부', 
    `name`        VARCHAR(45)    NOT NULL    COMMENT '상태 이름', 
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE seller_status COMMENT '셀러상태 (입점 대기, 퇴점 대기, 퇴점, 입점)';

CREATE TABLE authorities
(
    `id`          INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `is_deleted`  TINYINT        NOT NULL    DEFAULT 0  COMMENT '삭제 여부', 
    `name`        VARCHAR(45)    NOT NULL    COMMENT '권한 이름', 
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE authorities COMMENT '권한 (셀러, 마스터)';

CREATE TABLE sellers
(
    `id`                    INT              NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `seller_key_id`         INT              NOT NULL    COMMENT '셀러 키 ID', 
    `authority_id`          INT              NOT NULL    COMMENT '권한 ID', 
    `seller_attribute_id`   INT              NOT NULL    COMMENT '셀러 속성 ID', 
    `seller_status_id`      INT              NOT NULL    COMMENT '셀러 상태 ID', 
    `is_deleted`            TINYINT          DEFAULT 0  NOT NULL    COMMENT '삭제 여부', 
    `password`              VARCHAR(60)      NOT NULL    COMMENT '비밀번호', 
    `phone_number`          VARCHAR(20)      NOT NULL    COMMENT '핸드폰번호', 
    `name`                  VARCHAR(45)      NOT NULL    COMMENT '셀러명', 
    `eng_name`              VARCHAR(45)      NOT NULL    COMMENT '영문셀러명', 
    `service_number`        VARCHAR(20)      NOT NULL    COMMENT '고객센터 전화번호', 
    `site_url`              VARCHAR(200)     NOT NULL    COMMENT '사이트 URL', 
    `seller_number`         INT              NULL        COMMENT '회원번호', 
    `profile`               VARCHAR(200)     NULL        COMMENT '셀러 프로필', 
    `background_image`      VARCHAR(200)     NULL        COMMENT '셀러 배경이미지', 
    `detail_introduction`   LONGTEXT         NULL        COMMENT '상세 소개', 
    `zip_code`              VARCHAR(10)      NULL        COMMENT '우편번호', 
    `simple_introduction`   VARCHAR(100)     NULL        COMMENT '한줄 소개', 
    `address`               VARCHAR(100)     NULL        COMMENT '주소', 
    `detail_address`        VARCHAR(150)     NULL        COMMENT '상세주소', 
    `bank`                  VARCHAR(20)      NULL        COMMENT '은행', 
    `account_owner`         VARCHAR(45)      NULL        COMMENT '계좌주', 
    `bank_account`          VARCHAR(30)      NULL        COMMENT '계좌번호', 
    `shipping_information`  LONGTEXT         NULL        COMMENT '배송정보', 
    `refund_information`    LONGTEXT         NULL        COMMENT '교환/환불/정보', 
    `model_height`          INT              NULL        COMMENT '셀러 모델 사이즈 키', 
    `model_size_top`        INT              NULL        COMMENT '상의 사이즈', 
    `model_size_bottom`     INT              NULL        COMMENT '하의 사이즈', 
    `model_size_foot`       INT              NULL        COMMENT '발 사이즈', 
    `feed_message`          LONGTEXT         NULL        COMMENT '피드 업데이트 메세지', 
    `editor`                VARCHAR(45)      NOT NULL    COMMENT '변경 실행자', 
    `start_date`            TIMESTAMP DEFAULT CURRENT_TIMESTAMP        NOT NULL    COMMENT '유효시작일', 
    `end_date`              TIMESTAMP DEFAULT CURRENT_TIMESTAMP        NOT NULL    COMMENT '유효종료일', 
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE sellers COMMENT '셀러';

ALTER TABLE sellers
    ADD CONSTRAINT FK_sellers_seller_attribute_id_seller_attributes_id FOREIGN KEY (seller_attribute_id)
        REFERENCES seller_attributes (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE sellers
    ADD CONSTRAINT FK_sellers_seller_key_id_seller_keys_id FOREIGN KEY (seller_key_id)
        REFERENCES seller_keys (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE sellers
    ADD CONSTRAINT FK_sellers_authority_id_authorities_id FOREIGN KEY (authority_id)
        REFERENCES authorities (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE sellers
    ADD CONSTRAINT FK_sellers_seller_status_id_seller_status_id FOREIGN KEY (seller_status_id)
        REFERENCES seller_status (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

CREATE TABLE sizes
(
    `id`          INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `is_deleted`  TINYINT        NOT NULL    DEFAULT 0  COMMENT '삭제여부', 
    `name`        VARCHAR(45)    NOT NULL    COMMENT '사이즈명', 
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE sizes COMMENT '사이즈 (옵션)';

CREATE TABLE colors
(
    `id`          INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `is_deleted`  TINYINT        NOT NULL    DEFAULT 0  COMMENT '삭제여부', 
    `name`        VARCHAR(45)    NOT NULL    COMMENT '색상 이름', 
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE colors COMMENT '색상 (옵션)';

CREATE TABLE tags
(
    `id`          INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `is_deleted`  TINYINT        NOT NULL    DEFAULT 0  COMMENT '삭제 여부', 
    `name`        VARCHAR(45)    NOT NULL    COMMENT '태그 이름', 
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE tags COMMENT '상품 태그';

CREATE TABLE supervisor_infos
(
    `id`            INT             NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `seller_id`     INT             NOT NULL    COMMENT '셀러 ID', 
    `is_deleted`    TINYINT         NOT NULL    DEFAULT 0  COMMENT '삭제 여부', 
    `order`         INT             NULL        COMMENT '순서', 
    `name`          VARCHAR(45)     NULL        COMMENT '이름', 
    `phone_number`  VARCHAR(20)     NULL        COMMENT '핸드폰번호', 
    `email`         VARCHAR(200)    NULL        COMMENT '이메일', 
    PRIMARY KEY (id)
 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE supervisor_infos COMMENT '담당자 정보';

ALTER TABLE supervisor_infos
    ADD CONSTRAINT FK_supervisor_infos_seller_id_sellers_id FOREIGN KEY (seller_id)
        REFERENCES sellers (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

CREATE TABLE buisness_hours
(
    `id`          INT        NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `seller_id`   INT        NOT NULL    COMMENT '셀러 ID', 
    `start_time`  TIME       NULL        COMMENT '시작 시간', 
    `end_time`    TIME       NULL        COMMENT '종료 시간', 
    `is_weekend`  TINYINT    NULL        COMMENT '주중 / 주말', 
    `is_deleted`  TINYINT    NOT NULL    DEFAULT 0  COMMENT '삭제여부', 
    PRIMARY KEY (id)
    

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE buisness_hours COMMENT '고객센터 운영시간';

ALTER TABLE buisness_hours
    ADD CONSTRAINT FK_buisness_hours_seller_id_sellers_id FOREIGN KEY (seller_id)
        REFERENCES sellers (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

CREATE TABLE product_images
(
    `id`          INT              NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `product_id`  INT              NOT NULL    COMMENT '상품 ID', 
    `is_deleted`  TINYINT          NOT NULL    DEFAULT 0  COMMENT '삭제 여부', 
    `image`       VARCHAR(200)     NOT NULL    COMMENT '이미지 URL', 
    `order`       TINYINT          NOT NULL    COMMENT '순서', 
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE product_images COMMENT '순서 1이 대표이미지';

ALTER TABLE product_images
    ADD CONSTRAINT FK_product_images_product_id_products_id FOREIGN KEY (product_id)
        REFERENCES products (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

CREATE TABLE products_options
(
    `id`          INT        NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `product_id`  INT        NOT NULL    COMMENT '상품 ID', 
    `size_id`     INT        NOT NULL    COMMENT '사이즈 ID', 
    `color_id`    INT        NOT NULL    COMMENT '색상 ID', 
    `is_deleted`  TINYINT    NOT NULL    DEFAULT 0  COMMENT '삭제여부', 
    `quantity`    INT        NULL        COMMENT '재고', 
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE products_options COMMENT '상품 기본옵션 M2M';

ALTER TABLE products_options
    ADD CONSTRAINT FK_products_options_product_id_products_id FOREIGN KEY (product_id)
        REFERENCES products (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE products_options
    ADD CONSTRAINT FK_products_options_size_id_sizes_id FOREIGN KEY (size_id)
        REFERENCES sizes (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE products_options
    ADD CONSTRAINT FK_products_options_color_id_colors_id FOREIGN KEY (color_id)
        REFERENCES colors (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

CREATE TABLE products_tags
(
    `id`          INT        NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `product_id`  INT        NOT NULL    COMMENT '상품 ID', 
    `tag_id`      INT        NOT NULL    COMMENT '태그 ID', 
    `is_deleted`  TINYINT    NOT NULL    DEFAULT 0  COMMENT '삭제여부', 
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE products_tags COMMENT '상품 태그 M2M';

ALTER TABLE products_tags
    ADD CONSTRAINT FK_products_tags_tag_id_tags_id FOREIGN KEY (tag_id)
        REFERENCES tags (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE products_tags
    ADD CONSTRAINT FK_products_tags_product_id_products_id FOREIGN KEY (product_id)
        REFERENCES products (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

CREATE TABLE `seller_actions` 
(
  `id`               int(11)                                NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `seller_status_id` int(11)                                NOT NULL COMMENT '셀러상태 ID',
  `is_deleted`       tinyint(4)                             NOT NULL DEFAULT '0' COMMENT '삭제 여부',
  `action_type`      varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '액션 타입',
  `next_status_id`   int(11)                                NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_seller_actions_seller_status_id_seller_status_id` (`seller_status_id`),
  KEY `FK_seller_actions_next_status_id_next_status_id_id` (`next_status_id`),
  CONSTRAINT `FK_seller_actions_seller_status_id_seller_status_id` FOREIGN KEY (`seller_status_id`) REFERENCES `seller_status` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='셀러 액션';

