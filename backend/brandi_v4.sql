-- MySQL dump 10.13  Distrib 5.7.30, for Linux (x86_64)
--
-- Host: localhost    Database: brandi
-- ------------------------------------------------------
-- Server version	5.7.30-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attribute_groups`
--

DROP TABLE IF EXISTS `attribute_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attribute_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `name` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '그룹 이름',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='셀러 정보 그룹';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attribute_groups`
--

LOCK TABLES `attribute_groups` WRITE;
/*!40000 ALTER TABLE `attribute_groups` DISABLE KEYS */;
INSERT INTO `attribute_groups` VALUES (1,'shop'),(2,'brand'),(3,'beauty');
/*!40000 ALTER TABLE `attribute_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attributes_categories`
--

DROP TABLE IF EXISTS `attributes_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attributes_categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `attribute_group_id` int(11) NOT NULL COMMENT '셀러 속성 ID',
  `first_category_id` int(11) NOT NULL COMMENT '1차 카테고리 ID',
  `second_category_id` int(11) DEFAULT NULL COMMENT '2차 카테고리 ID',
  PRIMARY KEY (`id`),
  KEY `FK_attributes_categories_attribute_group_id_attribute_group_id` (`attribute_group_id`),
  KEY `FK_attributes_categories_first_category_id_first_categories_id` (`first_category_id`),
  KEY `FK_attributes_categories_second_category_id_second_categories_id` (`second_category_id`),
  CONSTRAINT `FK_attributes_categories_attribute_group_id_attribute_group_id` FOREIGN KEY (`attribute_group_id`) REFERENCES `attribute_groups` (`id`),
  CONSTRAINT `FK_attributes_categories_first_category_id_first_categories_id` FOREIGN KEY (`first_category_id`) REFERENCES `first_categories` (`id`),
  CONSTRAINT `FK_attributes_categories_second_category_id_second_categories_id` FOREIGN KEY (`second_category_id`) REFERENCES `second_categories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='셀러 속성, 1,2차 카테고리 조합';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attributes_categories`
--

LOCK TABLES `attributes_categories` WRITE;
/*!40000 ALTER TABLE `attributes_categories` DISABLE KEYS */;
INSERT INTO `attributes_categories` VALUES (1,1,15,1),(2,1,15,2),(3,1,15,3),(4,1,15,4),(5,1,9,5),(6,1,9,6),(7,1,9,7),(8,1,9,8),(9,1,9,9),(10,1,12,10),(11,1,12,11),(12,1,7,12),(13,1,7,13),(14,1,7,14),(15,1,7,15),(16,1,19,16),(17,1,14,17),(18,1,14,18),(19,1,14,19),(20,1,14,20),(21,1,14,21),(22,1,1,22),(23,1,1,23),(24,1,1,24),(25,1,1,25),(26,1,1,26),(27,1,21,27),(28,1,21,28),(29,1,21,29),(30,1,21,30),(31,1,21,31),(32,1,21,32),(33,1,21,33),(34,1,21,34),(35,1,22,35),(36,1,22,36),(37,1,22,37),(38,1,4,38),(39,1,4,39),(40,1,4,40),(41,1,8,41),(42,1,8,42),(43,1,8,43),(44,1,8,44),(45,1,8,45),(46,2,15,46),(47,2,15,1),(48,2,15,47),(49,2,15,4),(50,2,15,2),(51,2,15,34),(52,2,9,48),(53,2,9,5),(54,2,9,49),(55,2,9,50),(56,2,9,51),(57,2,9,52),(58,2,9,34),(59,2,19,53),(60,2,19,54),(61,2,19,55),(62,2,19,56),(63,2,19,34),(64,2,23,57),(65,2,23,58),(66,2,23,59),(67,2,23,60),(68,2,23,34),(69,2,12,53),(70,2,12,54),(71,2,12,55),(72,2,12,34),(73,2,10,17),(74,2,10,61),(75,2,10,20),(76,2,10,62),(77,2,10,63),(78,2,10,18),(79,2,10,64),(80,2,10,34),(81,2,1,24),(82,2,1,25),(83,2,1,65),(84,2,1,66),(85,2,1,26),(86,2,1,67),(87,2,1,68),(88,2,1,34),(89,2,16,35),(90,2,16,37),(91,2,16,69),(92,2,16,32),(93,2,16,29),(94,2,16,30),(95,2,16,31),(96,2,16,70),(97,2,16,71),(98,2,16,72),(99,2,16,73),(100,2,16,34),(101,2,11,74),(102,2,11,75),(103,2,11,76),(104,2,11,34),(105,2,18,77),(106,2,18,78),(107,2,18,79),(108,2,18,80),(109,2,18,39),(110,2,18,34),(111,3,13,84),(112,3,5,81),(113,3,5,82),(114,3,6,84),(115,3,3,84),(116,3,20,84),(117,3,17,41),(118,3,17,42),(119,3,17,83),(120,3,17,34),(121,3,25,84),(122,3,24,84),(123,3,2,84);
/*!40000 ALTER TABLE `attributes_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authorities`
--

DROP TABLE IF EXISTS `authorities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authorities` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '삭제 여부',
  `name` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '권한 이름',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='권한 (셀러, 마스터)';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authorities`
--

LOCK TABLES `authorities` WRITE;
/*!40000 ALTER TABLE `authorities` DISABLE KEYS */;
INSERT INTO `authorities` VALUES (1,0,'master'),(2,0,'seller');
/*!40000 ALTER TABLE `authorities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `buisness_hours`
--

DROP TABLE IF EXISTS `buisness_hours`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `buisness_hours` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `seller_id` int(11) NOT NULL COMMENT '셀러 ID',
  `start_time` time NOT NULL COMMENT '시작 시간',
  `end_time` time NOT NULL COMMENT '종료 시간',
  `is_weekend` tinyint(4) NOT NULL COMMENT '주중 / 주말',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '삭제여부',
  PRIMARY KEY (`id`),
  KEY `FK_buisness_hours_seller_id_sellers_id` (`seller_id`),
  CONSTRAINT `FK_buisness_hours_seller_id_sellers_id` FOREIGN KEY (`seller_id`) REFERENCES `sellers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='고객센터 운영시간';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buisness_hours`
--

LOCK TABLES `buisness_hours` WRITE;
/*!40000 ALTER TABLE `buisness_hours` DISABLE KEYS */;
/*!40000 ALTER TABLE `buisness_hours` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `color_filters`
--

DROP TABLE IF EXISTS `color_filters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `color_filters` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '삭제 여부',
  `name` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '색상 이름(한글)',
  `eng_name` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '색상 이름(영문)',
  `image` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '이미지',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='색상 필터명';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `color_filters`
--

LOCK TABLES `color_filters` WRITE;
/*!40000 ALTER TABLE `color_filters` DISABLE KEYS */;
INSERT INTO `color_filters` VALUES (1,0,'빨강','Red','http://sadmin.brandi.co.kr/include/img/product/color/red_check.png'),(2,0,'주황','Orange','http://sadmin.brandi.co.kr/include/img/product/color/orange.png'),(3,0,'노랑','Yellow','http://sadmin.brandi.co.kr/include/img/product/color/yellow.png'),(4,0,'베이지','Beige','http://sadmin.brandi.co.kr/include/img/product/color/beige.png'),(5,0,'갈색','Brown','http://sadmin.brandi.co.kr/include/img/product/color/brown.png'),(6,0,'초록','Green','http://sadmin.brandi.co.kr/include/img/product/color/green.png'),(7,0,'민트','Mint','http://sadmin.brandi.co.kr/include/img/product/color/mint.png'),(8,0,'하늘','Skyblue','http://sadmin.brandi.co.kr/include/img/product/color/skyblue.png'),(9,0,'파랑','Blue','http://sadmin.brandi.co.kr/include/img/product/color/blue.png'),(10,0,'남색','Navy','http://sadmin.brandi.co.kr/include/img/product/color/navy.png'),(11,0,'보라','Violet','http://sadmin.brandi.co.kr/include/img/product/color/violet.png'),(12,0,'분홍','Pink','http://sadmin.brandi.co.kr/include/img/product/color/pink.png'),(13,0,'흰색','White','http://sadmin.brandi.co.kr/include/img/product/color/white.png'),(14,0,'회색','Gray','http://sadmin.brandi.co.kr/include/img/product/color/gray.png'),(15,0,'검정','Black','http://sadmin.brandi.co.kr/include/img/product/color/black.png'),(16,0,'골드','Gold','http://sadmin.brandi.co.kr/include/img/product/color/gold.png'),(17,0,'로즈골드','Rosegold','http://sadmin.brandi.co.kr/include/img/product/color/rosegold.png'),(18,0,'실버','Silver','http://sadmin.brandi.co.kr/include/img/product/color/silver.png');
/*!40000 ALTER TABLE `color_filters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `colors`
--

DROP TABLE IF EXISTS `colors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `colors` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '삭제여부',
  `name` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '색상 이름',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='색상 (옵션)';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colors`
--

LOCK TABLES `colors` WRITE;
/*!40000 ALTER TABLE `colors` DISABLE KEYS */;
INSERT INTO `colors` VALUES (1,0,'Black'),(2,0,'White'),(3,0,'Gray'),(4,0,'Ivory'),(5,0,'Navy'),(6,0,'Brown'),(7,0,'Wine');
/*!40000 ALTER TABLE `colors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `first_categories`
--

DROP TABLE IF EXISTS `first_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `first_categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '삭제여부',
  `name` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '카테고리 이름',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='1차 카테고리 (아우터, 상의, 스커트, 바지, 원피스, 신발, 가방';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `first_categories`
--

LOCK TABLES `first_categories` WRITE;
/*!40000 ALTER TABLE `first_categories` DISABLE KEYS */;
INSERT INTO `first_categories` VALUES (1,0,'가방'),(2,0,'기타'),(3,0,'네일'),(4,0,'라이프웨어'),(5,0,'메이크업'),(6,0,'바디/헤어'),(7,0,'바지'),(8,0,'빅사이즈'),(9,0,'상의'),(10,0,'슈즈'),(11,0,'스윔웨어'),(12,0,'스커트'),(13,0,'스킨케어'),(14,0,'신발'),(15,0,'아우터'),(16,0,'악세서리'),(17,0,'애슬레저'),(18,0,'언더웨어'),(19,0,'원피스'),(20,0,'이너뷰티'),(21,0,'잡화'),(22,0,'주얼리'),(23,0,'팬츠'),(24,0,'푸드'),(25,0,'홈트레이닝');
/*!40000 ALTER TABLE `first_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notices`
--

DROP TABLE IF EXISTS `notices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notices` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '삭제 여부',
  `manufacturer` tinyint(4) NOT NULL COMMENT '제조사(수입사)',
  `manufacture_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '제조일자',
  `origin` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '원산지',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='상품 정보 고시';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notices`
--

LOCK TABLES `notices` WRITE;
/*!40000 ALTER TABLE `notices` DISABLE KEYS */;
/*!40000 ALTER TABLE `notices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_images`
--

DROP TABLE IF EXISTS `product_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_images` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `product_id` int(11) NOT NULL COMMENT '상품 ID',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '삭제 여부',
  `image` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '이미지 URL',
  `order` tinyint(4) NOT NULL COMMENT '순서',
  PRIMARY KEY (`id`),
  KEY `FK_product_images_product_id_products_id` (`product_id`),
  CONSTRAINT `FK_product_images_product_id_products_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='순서 1이 대표이미지';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_images`
--

LOCK TABLES `product_images` WRITE;
/*!40000 ALTER TABLE `product_images` DISABLE KEYS */;
/*!40000 ALTER TABLE `product_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_keys`
--

DROP TABLE IF EXISTS `product_keys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_keys` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `seller_key_id` int(11) DEFAULT NULL COMMENT '셀러 키 ID',
  `product_number` int(11) NOT NULL COMMENT '상품번호',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '생성일',
  PRIMARY KEY (`id`),
  KEY `FK_product_keys_seller_key_id_seller_keys_id` (`seller_key_id`),
  CONSTRAINT `FK_product_keys_seller_key_id_seller_keys_id` FOREIGN KEY (`seller_key_id`) REFERENCES `seller_keys` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='제품 키';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_keys`
--

LOCK TABLES `product_keys` WRITE;
/*!40000 ALTER TABLE `product_keys` DISABLE KEYS */;
/*!40000 ALTER TABLE `product_keys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `product_key_id` int(11) NOT NULL COMMENT '상품 KEY ID',
  `notices_id` int(11) NOT NULL COMMENT '상품 정보 고시 ID',
  `attributes_categories_id` int(11) DEFAULT NULL COMMENT '속성, 카테고리 조합 ID',
  `color_filter_id` int(11) DEFAULT NULL COMMENT '색상 필터 ID',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '삭제 여부',
  `is_detail_reference` tinyint(4) NOT NULL COMMENT '상품 상세 참조',
  `name` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '상품명',
  `simple_description` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '한줄 상품 설명',
  `details` longtext COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '상세 상품 정보',
  `wholesale_price` int(11) DEFAULT NULL COMMENT '도매 원가',
  `discount_start` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '할인기간 시작',
  `discount_end` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '할인기간 종료',
  `minimum_quantity` int(11) NOT NULL COMMENT '최소 판매 수량',
  `maximum_quantity` int(11) NOT NULL COMMENT '최대 판매 수량',
  `start_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '유효시작일',
  `end_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '유효종료일',
  `is_onsale` tinyint(4) NOT NULL COMMENT '판매여부',
  `is_displayed` tinyint(4) NOT NULL COMMENT '진열여부',
  `price` int(11) NOT NULL COMMENT '판매가격',
  `discount_rate` int(11) NOT NULL COMMENT '할인율',
  `editor` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '수정자',
  PRIMARY KEY (`id`),
  KEY `FK_products_notices_id_notices_id` (`notices_id`),
  KEY `FK_products_color_filter_id_color_filters_id` (`color_filter_id`),
  KEY `FK_products_product_key_id_product_keys_id` (`product_key_id`),
  KEY `FK_products_attributes_categories_id_attributes_categories_id` (`attributes_categories_id`),
  CONSTRAINT `FK_products_attributes_categories_id_attributes_categories_id` FOREIGN KEY (`attributes_categories_id`) REFERENCES `attributes_categories` (`id`),
  CONSTRAINT `FK_products_color_filter_id_color_filters_id` FOREIGN KEY (`color_filter_id`) REFERENCES `color_filters` (`id`),
  CONSTRAINT `FK_products_notices_id_notices_id` FOREIGN KEY (`notices_id`) REFERENCES `notices` (`id`),
  CONSTRAINT `FK_products_product_key_id_product_keys_id` FOREIGN KEY (`product_key_id`) REFERENCES `product_keys` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='상품';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_options`
--

DROP TABLE IF EXISTS `products_options`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_options` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `product_id` int(11) NOT NULL COMMENT '상품 ID',
  `size_id` int(11) NOT NULL COMMENT '사이즈 ID',
  `color_id` int(11) NOT NULL COMMENT '색상 ID',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '삭제여부',
  `quantity` int(11) DEFAULT NULL COMMENT '재고',
  PRIMARY KEY (`id`),
  KEY `FK_products_options_product_id_products_id` (`product_id`),
  KEY `FK_products_options_size_id_sizes_id` (`size_id`),
  KEY `FK_products_options_color_id_colors_id` (`color_id`),
  CONSTRAINT `FK_products_options_color_id_colors_id` FOREIGN KEY (`color_id`) REFERENCES `colors` (`id`),
  CONSTRAINT `FK_products_options_product_id_products_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),
  CONSTRAINT `FK_products_options_size_id_sizes_id` FOREIGN KEY (`size_id`) REFERENCES `sizes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='상품 기본옵션 M2M';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_options`
--

LOCK TABLES `products_options` WRITE;
/*!40000 ALTER TABLE `products_options` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_options` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_tags`
--

DROP TABLE IF EXISTS `products_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `product_id` int(11) NOT NULL COMMENT '상품 ID',
  `tag_id` int(11) NOT NULL COMMENT '태그 ID',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '삭제여부',
  PRIMARY KEY (`id`),
  KEY `FK_products_tags_tag_id_tags_id` (`tag_id`),
  KEY `FK_products_tags_product_id_products_id` (`product_id`),
  CONSTRAINT `FK_products_tags_product_id_products_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),
  CONSTRAINT `FK_products_tags_tag_id_tags_id` FOREIGN KEY (`tag_id`) REFERENCES `tags` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='상품 태그 M2M';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_tags`
--

LOCK TABLES `products_tags` WRITE;
/*!40000 ALTER TABLE `products_tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `second_categories`
--

DROP TABLE IF EXISTS `second_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `second_categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '삭제여부',
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '카테고리 이름',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='2차 카테고리 (코트, 점퍼, 재킷, 가디건 등)';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `second_categories`
--

LOCK TABLES `second_categories` WRITE;
/*!40000 ALTER TABLE `second_categories` DISABLE KEYS */;
INSERT INTO `second_categories` VALUES (1,0,'코트'),(2,0,'점퍼'),(3,0,'재킷'),(4,0,'가디건'),(5,0,'니트'),(6,0,'티셔츠'),(7,0,'블라우스/셔츠'),(8,0,'후드/맨투맨'),(9,0,'베스트'),(10,0,'롱스커트'),(11,0,'미니스커트'),(12,0,'청바지'),(13,0,'슬랙스'),(14,0,'반바지'),(15,0,'레깅스'),(16,0,'null'),(17,0,'스니커즈'),(18,0,'부츠'),(19,0,'힐'),(20,0,'플랫/로퍼'),(21,0,'샌들'),(22,0,'크로스백'),(23,0,'클러치'),(24,0,'숄더백'),(25,0,'토트백'),(26,0,'백팩'),(27,0,'휴대폰케이스'),(28,0,'지갑/파우치'),(29,0,'스카프/머플러'),(30,0,'모자'),(31,0,'양말'),(32,0,'시계'),(33,0,'아이웨어'),(34,0,'기타'),(35,0,'귀걸이'),(36,0,'목걸이/팔찌'),(37,0,'반지'),(38,0,'언더웨어'),(39,0,'홈웨어'),(40,0,'스윔웨어'),(41,0,'아우터'),(42,0,'상의'),(43,0,'스커트'),(44,0,'바지'),(45,0,'드레스'),(46,0,'자켓'),(47,0,'집업'),(48,0,'티/반팔티'),(49,0,'맨투맨'),(50,0,'후디'),(51,0,'셔츠/블라우스'),(52,0,'민소매/나시'),(53,0,'미니'),(54,0,'미디'),(55,0,'롱'),(56,0,'점프수트'),(57,0,'스키니'),(58,0,'스트레이트'),(59,0,'와이드'),(60,0,'숏'),(61,0,'러닝화'),(62,0,'로퍼'),(63,0,'펌프스'),(64,0,'샌들/슬리퍼'),(65,0,'미니백'),(66,0,'캔버스백'),(67,0,'지갑/카드케이스'),(68,0,'클러치/파우치'),(69,0,'팔찌/발찌'),(70,0,'폰 악세서리'),(71,0,'헤어 악세서리'),(72,0,'선글라스/아이웨어'),(73,0,'시즌아이템'),(74,0,'비키니'),(75,0,'원피스'),(76,0,'래쉬가드'),(77,0,'브라'),(78,0,'팬티'),(79,0,'세트'),(80,0,'슬립'),(81,0,'베이스'),(82,0,'색조'),(83,0,'하의'),(84,0,'2차 카테고리가 존재하지 않습니다.');
/*!40000 ALTER TABLE `second_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seller_actions`
--

DROP TABLE IF EXISTS `seller_actions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `seller_actions` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `seller_status_id` int(11) NOT NULL COMMENT '셀러상태 ID',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '삭제 여부',
  `action_type` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '액션 타입',
  PRIMARY KEY (`id`),
  KEY `FK_seller_actions_seller_status_id_seller_status_id` (`seller_status_id`),
  CONSTRAINT `FK_seller_actions_seller_status_id_seller_status_id` FOREIGN KEY (`seller_status_id`) REFERENCES `seller_status` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='셀러 액션';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seller_actions`
--

LOCK TABLES `seller_actions` WRITE;
/*!40000 ALTER TABLE `seller_actions` DISABLE KEYS */;
INSERT INTO `seller_actions` VALUES (1,1,0,'입점 승인'),(2,1,0,'입점 거절'),(3,2,0,'휴점 신청'),(4,2,0,'휴점 해제'),(5,2,0,'퇴점신청 처리'),(6,3,0,'퇴점 해제 처리'),(7,3,0,'퇴점 철회 처리'),(8,4,0,'퇴점 확정 처리');
/*!40000 ALTER TABLE `seller_actions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seller_attributes`
--

DROP TABLE IF EXISTS `seller_attributes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `seller_attributes` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `attribute_group_id` int(11) NOT NULL COMMENT '셀러속성 그룹 ID',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '삭제 여부',
  `name` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '카테고리 이름',
  PRIMARY KEY (`id`),
  KEY `FK_seller_attributes_attribute_group_id_attribute_groups_id` (`attribute_group_id`),
  CONSTRAINT `FK_seller_attributes_attribute_group_id_attribute_groups_id` FOREIGN KEY (`attribute_group_id`) REFERENCES `attribute_groups` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='셀러 속성 (쇼핌몰, 마켓, 로드샵/ 디자이너브랜드, 제너럴브랜드,내셔널브랜드 / 뷰티)';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seller_attributes`
--

LOCK TABLES `seller_attributes` WRITE;
/*!40000 ALTER TABLE `seller_attributes` DISABLE KEYS */;
INSERT INTO `seller_attributes` VALUES (1,1,0,'쇼핑몰'),(2,1,0,'마켓'),(3,1,0,'로드샵'),(4,2,0,'디자이너브랜드'),(5,2,0,'제너럴브랜드'),(6,2,0,'내셔널브랜드'),(7,3,0,'뷰티');
/*!40000 ALTER TABLE `seller_attributes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seller_keys`
--

DROP TABLE IF EXISTS `seller_keys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `seller_keys` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `user` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '아이디',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=236 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='셀러 키';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seller_keys`
--

LOCK TABLES `seller_keys` WRITE;
/*!40000 ALTER TABLE `seller_keys` DISABLE KEYS */;
INSERT INTO `seller_keys` VALUES (232,'review'),(233,'qwer1234'),(234,'asdf1234'),(235,'test1');
/*!40000 ALTER TABLE `seller_keys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seller_status`
--

DROP TABLE IF EXISTS `seller_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `seller_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '삭제 여부',
  `name` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '상태 이름',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='셀러상태 (입점 대기, 퇴점 대기, 퇴점, 입점)';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seller_status`
--

LOCK TABLES `seller_status` WRITE;
/*!40000 ALTER TABLE `seller_status` DISABLE KEYS */;
INSERT INTO `seller_status` VALUES (1,0,'입점대기'),(2,0,'입점'),(3,0,'휴점'),(4,0,'퇴점대기'),(5,0,'퇴점');
/*!40000 ALTER TABLE `seller_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellers`
--

DROP TABLE IF EXISTS `sellers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sellers` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `seller_key_id` int(11) NOT NULL COMMENT '셀러 키 ID',
  `authority_id` int(11) NOT NULL COMMENT '권한 ID',
  `seller_attribute_id` int(11) NOT NULL COMMENT '셀러 속성 ID',
  `seller_status_id` int(11) NOT NULL COMMENT '셀러 상태 ID',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '삭제 여부',
  `password` varchar(60) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '비밀번호',
  `phone_number` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '핸드폰번호',
  `name` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '셀러명',
  `eng_name` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '영문셀러명',
  `service_number` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '고객센터 전화번호',
  `site_url` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '사이트 URL',
  `seller_number` int(11) DEFAULT NULL COMMENT '회원번호',
  `profile` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '셀러 프로필',
  `background_image` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '셀러 배경이미지',
  `detail_introduction` longtext COLLATE utf8mb4_unicode_ci COMMENT '상세 소개',
  `zip_code` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '우편번호',
  `simple_introduction` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '한줄 소개',
  `address` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '주소',
  `detail_address` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '상세주소',
  `bank` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '은행',
  `account_owner` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '계좌주',
  `bank_account` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '계좌번호',
  `shipping_information` longtext COLLATE utf8mb4_unicode_ci COMMENT '배송정보',
  `refund_information` longtext COLLATE utf8mb4_unicode_ci COMMENT '교환/환불/정보',
  `model_height` int(11) DEFAULT NULL COMMENT '셀러 모델 사이즈 키',
  `model_size_top` int(11) DEFAULT NULL COMMENT '상의 사이즈',
  `model_size_bottom` int(11) DEFAULT NULL COMMENT '하의 사이즈',
  `model_size_foot` int(11) DEFAULT NULL COMMENT '발 사이즈',
  `feed_message` longtext COLLATE utf8mb4_unicode_ci COMMENT '피드 업데이트 메세지',
  `editor` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '변경 실행자',
  `start_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '유효시작일',
  `end_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '유효종료일',
  PRIMARY KEY (`id`),
  KEY `FK_sellers_seller_attribute_id_seller_attributes_id` (`seller_attribute_id`),
  KEY `FK_sellers_seller_key_id_seller_keys_id` (`seller_key_id`),
  KEY `FK_sellers_authority_id_authorities_id` (`authority_id`),
  KEY `FK_sellers_seller_status_id_seller_status_id` (`seller_status_id`),
  CONSTRAINT `FK_sellers_authority_id_authorities_id` FOREIGN KEY (`authority_id`) REFERENCES `authorities` (`id`),
  CONSTRAINT `FK_sellers_seller_attribute_id_seller_attributes_id` FOREIGN KEY (`seller_attribute_id`) REFERENCES `seller_attributes` (`id`),
  CONSTRAINT `FK_sellers_seller_key_id_seller_keys_id` FOREIGN KEY (`seller_key_id`) REFERENCES `seller_keys` (`id`),
  CONSTRAINT `FK_sellers_seller_status_id_seller_status_id` FOREIGN KEY (`seller_status_id`) REFERENCES `seller_status` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='셀러';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellers`
--

LOCK TABLES `sellers` WRITE;
/*!40000 ALTER TABLE `sellers` DISABLE KEYS */;
INSERT INTO `sellers` VALUES (58,232,1,1,1,0,'$2b$12$Txal81EtuWbBfZvFUNHKae/tDyl7H8ngVY0cyBh8xp.rJl/UecvxO','010-1111-2222','진성준','sungjun','010-4086-8910','http://www.naver.com',NULL,'url','url','자세한 소개',NULL,'안녕하세요. 222나는 셀러입니다',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'review','2020-06-03 07:03:18','2037-12-31 14:59:59'),(59,233,1,1,1,0,'$2b$12$ojwA5cHLhhhAT7Dv6C.H8O9rIz0kzMN2m.g5stqb5rinWCV6afjIC','010-1234-1234','안녕하세요','hi','02-1234-1234','http://www.naver.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'qwer1234','2020-06-03 07:12:46','2037-12-31 14:59:59'),(60,234,1,6,1,0,'$2b$12$tJlATy06r5.KmwVFVVIhfeSm9LRWxSIQyYrVoKWUus/raSjRTHNvq','010-1111-1111','gkkgkg','gkgkgkg','02-1111-1111','http://www.naver.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'asdf1234','2020-06-03 07:16:23','2037-12-31 14:59:59'),(61,235,1,1,1,0,'$2b$12$1S9mq7Br9MvoLEfpTJSD7.SvnlEGZCdmFkHa4weHGU3K9o46AVdU6','010-1111-2222','진성준','sungjun','010-4086-8910','http://www.naver.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'test1','2020-06-04 00:29:39','2037-12-31 14:59:59');
/*!40000 ALTER TABLE `sellers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sizes`
--

DROP TABLE IF EXISTS `sizes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sizes` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '삭제여부',
  `name` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '사이즈명',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='사이즈 (옵션)';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sizes`
--

LOCK TABLES `sizes` WRITE;
/*!40000 ALTER TABLE `sizes` DISABLE KEYS */;
INSERT INTO `sizes` VALUES (1,0,'Free'),(2,0,'XL'),(3,0,'L'),(4,0,'M'),(5,0,'S'),(6,0,'XS');
/*!40000 ALTER TABLE `sizes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supervisor_infos`
--

DROP TABLE IF EXISTS `supervisor_infos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `supervisor_infos` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `seller_id` int(11) NOT NULL COMMENT '셀러 ID',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '삭제 여부',
  `order` int(11) NOT NULL COMMENT '순서',
  `name` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '이름',
  `phone_number` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '핸드폰번호',
  `email` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '이메일',
  PRIMARY KEY (`id`),
  KEY `FK_supervisor_infos_seller_id_sellers_id` (`seller_id`),
  CONSTRAINT `FK_supervisor_infos_seller_id_sellers_id` FOREIGN KEY (`seller_id`) REFERENCES `sellers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='담당자 정보';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supervisor_infos`
--

LOCK TABLES `supervisor_infos` WRITE;
/*!40000 ALTER TABLE `supervisor_infos` DISABLE KEYS */;
/*!40000 ALTER TABLE `supervisor_infos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tags`
--

DROP TABLE IF EXISTS `tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '삭제 여부',
  `name` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '태그 이름',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='상품 태그';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tags`
--

LOCK TABLES `tags` WRITE;
/*!40000 ALTER TABLE `tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `tags` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-04 10:17:40
