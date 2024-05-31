CREATE DATABASE  IF NOT EXISTS `nft` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `nft`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: nft
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts_korisnik`
--

DROP TABLE IF EXISTS `accounts_korisnik`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_korisnik` (
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `idkor` int NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `user_type` varchar(20) NOT NULL,
  PRIMARY KEY (`idkor`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_korisnik`
--

LOCK TABLES `accounts_korisnik` WRITE;
/*!40000 ALTER TABLE `accounts_korisnik` DISABLE KEYS */;
INSERT INTO `accounts_korisnik` VALUES ('pbkdf2_sha256$600000$VT2NyrH3zLvX41hg0dCV8S$kspkN2iAIfCho9ng4ipfTxo9fOjkygTI39mns9TJlIc=','2024-05-31 21:29:47.463467',1,'admin','admin'),('pbkdf2_sha256$600000$sbh83h87FIRWJPO1au2wMg$ZTRS1uaJLtO6ZJ7zFzUVfVLhHqKFTiWrioiBkCXDk7I=','2024-05-31 20:54:11.192796',2,'zeks','kreator'),('pbkdf2_sha256$600000$AXsMCEspLR1X0QOkyDTCt5$+3Dh2PUMPbKQCxcArp7EFY1Iu0G5j/CvCZcb1ZFGfio=','2024-05-31 20:30:31.996037',3,'LeaderOfHorde','kreator'),('pbkdf2_sha256$600000$4WX05wojScu6Xj1s50nHZo$UGEr0QYF+VHxeUHMLQPuK27ltUlvmOfo8qc0ow34OZk=','2024-05-31 20:43:09.847207',4,'margo','kolekcionar'),('pbkdf2_sha256$720000$GZWDFVtubkXCVqZTCJQJs2$HKKnCnNhpmIjUhBEwSmTu6d+8uBwIYdYmogm9VHML3U=','2024-05-30 11:22:57.353231',5,'voks','kolekcionar'),('pbkdf2_sha256$600000$W1v951RyxsTRMhFf6OzG99$NiNfXvqWpQQICWU12T9kb1si31UU0Vy7bOxuxTXIPaU=','2024-05-31 21:45:54.353866',6,'medwed','kupac'),('pbkdf2_sha256$720000$eTVizh4THB1GDmbjxcV3SF$SOgSSvlHRyLoMCJUK2JX30AIhvColzSO1Wl8sa4nato=',NULL,7,'mariasharapova','kupac'),('pbkdf2_sha256$600000$IHJa8NGFIzxIAHPTorj8Nn$iIoq5+2/BVa7f3U7tID4B2UwrxQdaghIc5CcPjiUpHc=','2024-05-31 18:55:04.841871',8,'nale123','kreator');
/*!40000 ALTER TABLE `accounts_korisnik` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `administrator`
--

DROP TABLE IF EXISTS `administrator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrator` (
  `IdKor` int NOT NULL,
  PRIMARY KEY (`IdKor`),
  CONSTRAINT `administrator_IdKor_bc98f3ef_fk_accounts_korisnik_idkor` FOREIGN KEY (`IdKor`) REFERENCES `accounts_korisnik` (`idkor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrator`
--

LOCK TABLES `administrator` WRITE;
/*!40000 ALTER TABLE `administrator` DISABLE KEYS */;
INSERT INTO `administrator` VALUES (1);
/*!40000 ALTER TABLE `administrator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add korisnik',6,'add_korisnik'),(22,'Can change korisnik',6,'change_korisnik'),(23,'Can delete korisnik',6,'delete_korisnik'),(24,'Can view korisnik',6,'view_korisnik'),(25,'Can add zahtevzaregistraciju',7,'add_zahtevzaregistraciju'),(26,'Can change zahtevzaregistraciju',7,'change_zahtevzaregistraciju'),(27,'Can delete zahtevzaregistraciju',7,'delete_zahtevzaregistraciju'),(28,'Can view zahtevzaregistraciju',7,'view_zahtevzaregistraciju'),(29,'Can add administrator',8,'add_administrator'),(30,'Can change administrator',8,'change_administrator'),(31,'Can delete administrator',8,'delete_administrator'),(32,'Can view administrator',8,'view_administrator'),(33,'Can add listanft',9,'add_listanft'),(34,'Can change listanft',9,'change_listanft'),(35,'Can delete listanft',9,'delete_listanft'),(36,'Can view listanft',9,'view_listanft'),(37,'Can add izlozba',10,'add_izlozba'),(38,'Can change izlozba',10,'change_izlozba'),(39,'Can delete izlozba',10,'delete_izlozba'),(40,'Can view izlozba',10,'view_izlozba'),(41,'Can add kolekcija',11,'add_kolekcija'),(42,'Can change kolekcija',11,'change_kolekcija'),(43,'Can delete kolekcija',11,'delete_kolekcija'),(44,'Can view kolekcija',11,'view_kolekcija'),(45,'Can add portfolio',12,'add_portfolio'),(46,'Can change portfolio',12,'change_portfolio'),(47,'Can delete portfolio',12,'delete_portfolio'),(48,'Can view portfolio',12,'view_portfolio'),(49,'Can add pripada',13,'add_pripada'),(50,'Can change pripada',13,'change_pripada'),(51,'Can delete pripada',13,'delete_pripada'),(52,'Can view pripada',13,'view_pripada'),(53,'Can add nft',14,'add_nft'),(54,'Can change nft',14,'change_nft'),(55,'Can delete nft',14,'delete_nft'),(56,'Can view nft',14,'view_nft'),(57,'Can add ocena',15,'add_ocena'),(58,'Can change ocena',15,'change_ocena'),(59,'Can delete ocena',15,'delete_ocena'),(60,'Can view ocena',15,'view_ocena'),(61,'Can add registrovanikorisnik',16,'add_registrovanikorisnik'),(62,'Can change registrovanikorisnik',16,'change_registrovanikorisnik'),(63,'Can delete registrovanikorisnik',16,'delete_registrovanikorisnik'),(64,'Can view registrovanikorisnik',16,'view_registrovanikorisnik'),(65,'Can add kolekcionar',17,'add_kolekcionar'),(66,'Can change kolekcionar',17,'change_kolekcionar'),(67,'Can delete kolekcionar',17,'delete_kolekcionar'),(68,'Can view kolekcionar',17,'view_kolekcionar'),(69,'Can add kreator',18,'add_kreator'),(70,'Can change kreator',18,'change_kreator'),(71,'Can delete kreator',18,'delete_kreator'),(72,'Can view kreator',18,'view_kreator'),(73,'Can add kupac',19,'add_kupac'),(74,'Can change kupac',19,'change_kupac'),(75,'Can delete kupac',19,'delete_kupac'),(76,'Can view kupac',19,'view_kupac');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_korisnik_idkor` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_korisnik_idkor` FOREIGN KEY (`user_id`) REFERENCES `accounts_korisnik` (`idkor`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (8,'accounts','administrator'),(6,'accounts','korisnik'),(7,'accounts','zahtevzaregistraciju'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(10,'exhibitions','izlozba'),(11,'exhibitions','kolekcija'),(9,'exhibitions','listanft'),(12,'exhibitions','portfolio'),(13,'exhibitions','pripada'),(14,'nft','nft'),(15,'nft','ocena'),(17,'profiles','kolekcionar'),(18,'profiles','kreator'),(19,'profiles','kupac'),(16,'profiles','registrovanikorisnik'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'accounts','0001_initial','2024-05-31 18:32:59.000327'),(2,'profiles','0001_initial','2024-05-31 18:33:04.631043'),(3,'profiles','0002_alter_registrovanikorisnik_brojkartice','2024-05-31 18:33:04.743424'),(4,'nft','0001_initial','2024-05-31 18:33:14.505733'),(5,'nft','0002_alter_nft_opis','2024-05-31 18:33:14.560071'),(6,'nft','0003_alter_nft_prosecnaocena','2024-05-31 18:33:14.752845'),(7,'contenttypes','0001_initial','2024-05-31 18:33:21.764410'),(8,'admin','0001_initial','2024-05-31 18:33:22.137347'),(9,'admin','0002_logentry_remove_auto_add','2024-05-31 18:33:22.151347'),(10,'admin','0003_logentry_add_action_flag_choices','2024-05-31 18:33:22.164426'),(11,'contenttypes','0002_remove_content_type_name','2024-05-31 18:33:22.348319'),(12,'auth','0001_initial','2024-05-31 18:33:23.121598'),(13,'auth','0002_alter_permission_name_max_length','2024-05-31 18:33:23.282542'),(14,'auth','0003_alter_user_email_max_length','2024-05-31 18:33:23.298211'),(15,'auth','0004_alter_user_username_opts','2024-05-31 18:33:23.316215'),(16,'auth','0005_alter_user_last_login_null','2024-05-31 18:33:23.330209'),(17,'auth','0006_require_contenttypes_0002','2024-05-31 18:33:23.340206'),(18,'auth','0007_alter_validators_add_error_messages','2024-05-31 18:33:23.404129'),(19,'auth','0008_alter_user_username_max_length','2024-05-31 18:33:23.422316'),(20,'auth','0009_alter_user_last_name_max_length','2024-05-31 18:33:23.441366'),(21,'auth','0010_alter_group_name_max_length','2024-05-31 18:33:23.496433'),(22,'auth','0011_update_proxy_permissions','2024-05-31 18:33:23.523860'),(23,'auth','0012_alter_user_first_name_max_length','2024-05-31 18:33:23.543930'),(24,'exhibitions','0001_initial','2024-05-31 18:33:24.512101'),(25,'exhibitions','0002_alter_izlozba_opis','2024-05-31 18:33:24.554363'),(26,'exhibitions','0003_alter_izlozba_prosecnaocena','2024-05-31 18:33:24.723102'),(27,'sessions','0001_initial','2024-05-31 18:33:24.819695'),(28,'exhibitions','0004_alter_izlozba_prosecnaocena','2024-05-31 19:51:39.693953'),(29,'nft','0004_alter_nft_prosecnaocena','2024-05-31 21:44:10.846759'),(30,'nft','0005_alter_nft_idvla','2024-05-31 21:44:10.860201');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('axahegysk0rxtme6uckx5b7ubeyw6qof','.eJxVjE0OwiAYBe_C2hCwQMGl-56BfD8gVQNJaVfGu2uTLnT7Zua9RIRtLXHraYkzi4sI4vS7IdAj1R3wHeqtSWp1XWaUuyIP2uXUOD2vh_t3UKCXbz3qoMl4RYReIykweWDkbBQbDsoozOicxREsWm89JT8EAGdhOLtkQbw_-EQ4XQ:1sD9TH:kSiEQJm1KT87fl1kW10WO0DQiXP8nyQ_wSBSyJb9aV8','2024-06-14 21:07:31.388892'),('rtukg31sgn2yko0qq13y96pidnqvqjss','.eJxVjE0OwiAYBe_C2hCwQMGl-56BfD8gVQNJaVfGu2uTLnT7Zua9RIRtLXHraYkzi4sI4vS7IdAj1R3wHeqtSWp1XWaUuyIP2uXUOD2vh_t3UKCXbz3qoMl4RYReIykweWDkbBQbDsoozOicxREsWm89JT8EAGdhOLtkQbw_-EQ4XQ:1sD9Ja:TfXKOgnQQ004lx6l_EEEUoQvv9jCGWkyu-G7jV9NOwg','2024-06-14 20:57:30.074459'),('xoaljye4vpf9llnj0nn8zbqgpwx41rjk','.eJxVjDsOwjAQBe_iGln4G5uSPmewdr1rHECOFCcV4u4QKQW0b2beSyTY1pq2zkuaSFyEEaffDSE_uO2A7tBus8xzW5cJ5a7Ig3Y5zsTP6-H-HVTo9Vt7zAaiPruANlIJ3rgCGYNGH02xnJ1TFrMmS0oHLo69J-d5UEgQBiXeH-_8OEI:1sD7iE:0RaSOGUfQWAAlaq_g4cFx8LkS-nDgsMCUePLGEC-Sls','2024-06-14 19:14:50.547258');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `izlozba`
--

DROP TABLE IF EXISTS `izlozba`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `izlozba` (
  `IdLis` int NOT NULL,
  `Naziv` varchar(18) DEFAULT NULL,
  `Opis` varchar(1024) DEFAULT NULL,
  `DatumKreiranja` varchar(18) DEFAULT NULL,
  `ProsecnaOcena` decimal(10,2) NOT NULL,
  PRIMARY KEY (`IdLis`),
  CONSTRAINT `izlozba_IdLis_d70d3443_fk_listanft_IdLis` FOREIGN KEY (`IdLis`) REFERENCES `listanft` (`IdLis`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `izlozba`
--

LOCK TABLES `izlozba` WRITE;
/*!40000 ALTER TABLE `izlozba` DISABLE KEYS */;
INSERT INTO `izlozba` VALUES (9,'repka','srbija i partizan','2024-05-30',0.00),(10,'nba','amerika','2024-05-30',0.00),(11,'prizori','priroda','2024-05-30',5.00),(12,'kuba','slike sa puta','2024-05-30',4.75),(17,'Bugs','buuuuuuuuugs buuuuuuugs','2024-05-31',0.00),(18,'mfers','mfers','2024-05-31',0.00),(19,'Punks','crypto punks','2024-05-31',0.00),(20,'tigersss','goo tigers','2024-05-31',0.00),(21,'monkeys','monkey monkey','2024-05-31',0.00),(22,'sugartown','citizens of sugartown','2024-05-31',0.00),(23,'lil pudgies','little penguins randomly generated','2024-05-31',0.00),(26,'my super','from creator leader of horde\r\n','2024-05-31',3.80),(27,'my bugs','bugs','2024-05-31',5.00),(28,'all margo','all nfts in my collections','2024-05-31',4.33);
/*!40000 ALTER TABLE `izlozba` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kolekcija`
--

DROP TABLE IF EXISTS `kolekcija`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kolekcija` (
  `IdLis` int NOT NULL,
  PRIMARY KEY (`IdLis`),
  CONSTRAINT `kolekcija_IdLis_a05d8182_fk_listanft_IdLis` FOREIGN KEY (`IdLis`) REFERENCES `listanft` (`IdLis`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kolekcija`
--

LOCK TABLES `kolekcija` WRITE;
/*!40000 ALTER TABLE `kolekcija` DISABLE KEYS */;
INSERT INTO `kolekcija` VALUES (1),(3),(5),(6),(7),(8),(14);
/*!40000 ALTER TABLE `kolekcija` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kolekcionar`
--

DROP TABLE IF EXISTS `kolekcionar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kolekcionar` (
  `IdKor` int NOT NULL,
  PRIMARY KEY (`IdKor`),
  CONSTRAINT `kolekcionar_IdKor_3f1ccb0d_fk_registrovanikorisnik_IdKor` FOREIGN KEY (`IdKor`) REFERENCES `registrovanikorisnik` (`IdKor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kolekcionar`
--

LOCK TABLES `kolekcionar` WRITE;
/*!40000 ALTER TABLE `kolekcionar` DISABLE KEYS */;
INSERT INTO `kolekcionar` VALUES (4),(5);
/*!40000 ALTER TABLE `kolekcionar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kreator`
--

DROP TABLE IF EXISTS `kreator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kreator` (
  `IdKor` int NOT NULL,
  PRIMARY KEY (`IdKor`),
  CONSTRAINT `kreator_IdKor_47fa6285_fk_registrovanikorisnik_IdKor` FOREIGN KEY (`IdKor`) REFERENCES `registrovanikorisnik` (`IdKor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kreator`
--

LOCK TABLES `kreator` WRITE;
/*!40000 ALTER TABLE `kreator` DISABLE KEYS */;
INSERT INTO `kreator` VALUES (2),(3),(8);
/*!40000 ALTER TABLE `kreator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kupac`
--

DROP TABLE IF EXISTS `kupac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kupac` (
  `IdKor` int NOT NULL,
  PRIMARY KEY (`IdKor`),
  CONSTRAINT `kupac_IdKor_d7f6d34a_fk_registrovanikorisnik_IdKor` FOREIGN KEY (`IdKor`) REFERENCES `registrovanikorisnik` (`IdKor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kupac`
--

LOCK TABLES `kupac` WRITE;
/*!40000 ALTER TABLE `kupac` DISABLE KEYS */;
INSERT INTO `kupac` VALUES (6),(7);
/*!40000 ALTER TABLE `kupac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `listanft`
--

DROP TABLE IF EXISTS `listanft`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `listanft` (
  `IdLis` int NOT NULL AUTO_INCREMENT,
  `UkupnaVrednost` double NOT NULL,
  `BrojNFT` int NOT NULL,
  `IdVla` int DEFAULT NULL,
  PRIMARY KEY (`IdLis`),
  KEY `listanft_IdVla_5906fe56_fk_registrovanikorisnik_IdKor` (`IdVla`),
  CONSTRAINT `listanft_IdVla_5906fe56_fk_registrovanikorisnik_IdKor` FOREIGN KEY (`IdVla`) REFERENCES `registrovanikorisnik` (`IdKor`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `listanft`
--

LOCK TABLES `listanft` WRITE;
/*!40000 ALTER TABLE `listanft` DISABLE KEYS */;
INSERT INTO `listanft` VALUES (1,5760,30,2),(2,7068,37,2),(3,3660,27,3),(4,3502,33,3),(5,483,11,4),(6,616,3,5),(7,123,1,6),(8,0,0,7),(9,592,5,3),(10,295,4,3),(11,1139,5,2),(12,580,4,2),(14,2995,19,8),(15,3423,23,8),(17,1324,7,8),(18,862,6,8),(19,516,4,8),(20,1866,8,3),(21,539,8,3),(22,2224,11,2),(23,903,5,2),(25,106,6,4),(26,106,6,4),(27,365,4,4),(28,483,11,4);
/*!40000 ALTER TABLE `listanft` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nft`
--

DROP TABLE IF EXISTS `nft`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nft` (
  `IdNFT` int NOT NULL AUTO_INCREMENT,
  `Naziv` varchar(20) NOT NULL,
  `Vrednost` double NOT NULL,
  `ProsecnaOcena` decimal(10,2) NOT NULL,
  `Opis` varchar(1024) NOT NULL,
  `Slika` varchar(100) NOT NULL,
  `Url` varchar(128) NOT NULL,
  `IdKre` int DEFAULT NULL,
  `IdVla` int DEFAULT NULL,
  PRIMARY KEY (`IdNFT`),
  KEY `nft_IdKre_f3486202_fk_registrovanikorisnik_IdKor` (`IdKre`),
  KEY `nft_IdVla_cebaea32_fk_registrovanikorisnik_IdKor` (`IdVla`),
  CONSTRAINT `nft_IdKre_f3486202_fk_registrovanikorisnik_IdKor` FOREIGN KEY (`IdKre`) REFERENCES `registrovanikorisnik` (`IdKor`) ON DELETE SET NULL,
  CONSTRAINT `nft_IdVla_cebaea32_fk_registrovanikorisnik_IdKor` FOREIGN KEY (`IdVla`) REFERENCES `registrovanikorisnik` (`IdKor`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nft`
--

LOCK TABLES `nft` WRITE;
/*!40000 ALTER TABLE `nft` DISABLE KEYS */;
INSERT INTO `nft` VALUES (1,'reprentacija',88,0.00,'svetsko prvenstvo 2019','nft_images/prva.PNG','',3,3),(2,'partizan',143,0.00,'jedna iz mladjih dana','nft_images/druga.PNG','',3,3),(3,'sakramento',63,0.00,'nba sakramento','nft_images/treca.PNG','',3,3),(4,'atlanta',77,0.00,'atlanta slika 2021','nft_images/cetvrta.PNG','',3,3),(5,'kapiten',153,0.00,'broj 7','nft_images/peta.PNG','',3,3),(6,'manila',76,0.00,'sp 2023','nft_images/sesta.PNG','',3,3),(7,'Repka 2015',132,0.00,'repka iz mladjih dana','nft_images/sedma.PNG','',3,3),(8,'atl #13',112,0.00,'za pobedu','nft_images/osma.PNG','',3,3),(9,'draft',43,0.00,'ovako je pocelo','nft_images/deveta.PNG','',3,3),(10,'sac #8',92,0.00,'pocetak','nft_images/11.PNG','',3,8),(11,'Metascapes #2316',204,5.00,'2555 hand-picked AI landscape images of a unique collaboration between Cath Simard, Ryan Newburn, Iurie Belegurschi and Artificial Intelligence, bridging the natural and the supernatural.\r\n\r\nhttps://metascapes.sloika.xyz/','nft_images/Metascapes_231611.jpg','',2,2),(12,'Metascapes #2064',146,0.00,'2555 hand-picked AI landscape images of a unique collaboration between Cath Simard, Ryan Newburn, Iurie Belegurschi and Artificial Intelligence, bridging the natural and the supernatural.\r\n\r\nhttps://metascapes.sloika.xyz/','nft_images/Metascapes_206412.jpg','',2,2),(13,'Metascapes #1689',223,0.00,'2555 hand-picked AI landscape images of a unique collaboration between Cath Simard, Ryan Newburn, Iurie Belegurschi and Artificial Intelligence, bridging the natural and the supernatural.\r\n\r\nhttps://metascapes.sloika.xyz/','nft_images/Metascapes_168913.jpg','',2,2),(14,'Metascapes #2019',312,0.00,'2555 hand-picked AI landscape images of a unique collaboration between Cath Simard, Ryan Newburn, Iurie Belegurschi and Artificial Intelligence, bridging the natural and the supernatural.\r\n\r\nhttps://metascapes.sloika.xyz/','nft_images/Metascapes_201914.jpg','',2,2),(15,'Metascapes #1724',254,0.00,'2555 hand-picked AI landscape images of a unique collaboration between Cath Simard, Ryan Newburn, Iurie Belegurschi and Artificial Intelligence, bridging the natural and the supernatural.\r\n\r\nhttps://metascapes.sloika.xyz/','nft_images/Metascapes_172415.jpg','',2,2),(16,'Cuba #02',44,5.00,'Cuba; a place that stole our hearts, with its people, food, classic cars and somewhat it\'s beautiful decay that felt like it was frozen in time for over half a century.','nft_images/Cuba_0216.jpg','',2,2),(17,'Cuba #10',198,5.00,'Cuba; a place that stole our hearts, with its people, food, classic cars and somewhat it\'s beautiful decay that felt like it was frozen in time for over half a century.','nft_images/Cuba_1017.jpg','',2,2),(18,'Cuba #03',122,4.00,'Cuba; a place that stole our hearts, with its people, food, classic cars and somewhat it\'s beautiful decay that felt like it was frozen in time for over half a century.','nft_images/Cuba_0318.jpg','',2,2),(19,'Cuba #05',216,5.00,'Cuba; a place that stole our hearts, with its people, food, classic cars and somewhat it\'s beautiful decay that felt like it was frozen in time for over half a century.','nft_images/Cuba_0519.jpg','',2,2),(20,'Cuba #25',201,0.00,'Cuba; a place that stole our hearts, with its people, food, classic cars and somewhat it\'s beautiful decay that felt like it was frozen in time for over half a century.','nft_images/Cuba_2520.jpg','',2,8),(21,'Kiss on it!',288,0.00,'During the new born season there is a lot of cuddling between mothers and their calfs in the field, it is always a joy to witness those precious moments. On a moody evening this mother and calf where all alone in the field which I thought was a little bit strange, because normally there is a group of at least 20 Teddycows out there. But when I came close I saw why: this calf was just born and the mother was busy licking the fur of the calf. This specific moment was like mother kissing the little mocca coloured calf, I was happy to capture it. After a few photos I decided to respect their privacy and leave them alone.','nft_images/Kiss_on_it21.jpg','',2,5),(22,'My precious',166,0.00,'With my photography I always aim to capture special moments in nature, this moment with the cutest little Chipmunk is one of those. These little fellas simply adore nuts and at the end of the summer they try to collect as much nuts as possible. After collecting they hide them between the branches, under some leaves, all in preparation for winter. And sometimes, between all the hard work, they allow themselves to enjoy some nuts. Those moments are the ones I’m waiting for, have my camera ready and shoot a burst to capture as much content as possible of that specific moment. A lot of the times you miss the moment because they are fast, really fast, but sometimes I’m lucky with photo like this as the result.','nft_images/My_precious22.jpg','',2,3),(23,'My precious',166,0.00,'With my photography I always aim to capture special moments in nature, this moment with the cutest little Chipmunk is one of those. These little fellas simply adore nuts and at the end of the summer they try to collect as much nuts as possible. After collecting they hide them between the branches, under some leaves, all in preparation for winter. And sometimes, between all the hard work, they allow themselves to enjoy some nuts. Those moments are the ones I’m waiting for, have my camera ready and shoot a burst to capture as much content as possible of that specific moment. A lot of the times you miss the moment because they are fast, really fast, but sometimes I’m lucky with photo like this as the result.','nft_images/My_precious23.jpg','',2,5),(24,'Play time!',202,0.00,'I had the opportunity to spend a few hours with 3 Fox cubs during a very hot afternoon. They were running around, playing with each other and at a certain point this cub decided that is was time to lay down and play with a stick. I was sitting on the ground just a few meters away from this little beauty, observing it and I tried to capture as much special moments like this. I really love to experience special moments like this, especially with baby animals because they are so curious, adorable and simply the cutest!','nft_images/Play_time24.jpg','',2,2),(25,'Play time!',202,0.00,'I had the opportunity to spend a few hours with 3 Fox cubs during a very hot afternoon. They were running around, playing with each other and at a certain point this cub decided that is was time to lay down and play with a stick. I was sitting on the ground just a few meters away from this little beauty, observing it and I tried to capture as much special moments like this. I really love to experience special moments like this, especially with baby animals because they are so curious, adorable and simply the cutest!','nft_images/Play_time25.jpg','',2,3),(26,'Red-Bull',162,0.00,'A moody Sunday afternoon well spent. After a few days of rain and being inside, I wanted to go out so badly. After checking the radar I noticed it would be dry for the next hour, so I quickly grabbed my camera and 15 minutes later I found a lot of Teddycows grazing in the field. It was good so smell some fresh air after being inside for a few days, but I was also a little bit disappointed because when Teddycows graze, the really only graze! So I decided to just enjoy the scenery and the fact that I was outside in nature with these magical creatures. At some point I saw something coming from behind a little hill and I quickly realized it was one of the biggest Bulls of the area. I was stoked and started walking towards him. Just a few moments later I got the opportunity to capture this intriguing portrait of Red-Bull!\r\n\r\nArtist: Nick Bng  \r\nEdition Size: 50','nft_images/Red-Bull26.jpg','',2,5),(27,'The cutest baby face',242,0.00,'This cutest baby face simply needs no description!','nft_images/The_cutest_baby_face27.jpg','',2,2),(28,'Little forest ghost',145,0.00,'It was a cloudy sunset in spring, just a week after this first calf of the season was born. After dinner I had some time to visit the Teddycows and I was hoping to find the the blond calf. I found him with his family at the edge of the forest and I could see it was already bigger than the first time I saw it. Because it was cloudy there was little light, but just enough to highlight his blond fur and create this incredible mysterious contrast with the dark surroundings. It was the first time that I was able to capture a Teddycow in a dark setting like this and that I got this opportunity with a little blond calf makes this moment even more special. The little forest ghost was born.\r\n\r\nArtist: Nick Bng  \r\nLocation: Posbank, The Netherlands  \r\nEdition Size: 50','nft_images/Little_forest_ghost28.jpg','',2,2),(29,'Cuteness in the rain',202,0.00,'Together with a friend of mine I visited the Teddycows on a moody evening during Spring. It was during the first weeks of the period that the new Teddycows are getting born. This is always an exciting time for us because you can have such lovely surprises when you visit the Teddycows. On this specific evening this few days old was the surprise for us. It was drizzling a bit, which gave a very moody and dramatic atmosphere. It was quite a challenge to get a decent shot of this new born because it was constantly hiding behind his mother. After a while it gave us a good opportunity to make a few shots of some cuteness in the rain.  \r\nArtist: Nick Bng  \r\n Edition Size: 50','nft_images/Cuteness_in_the_rain29.jpg','',2,2),(30,'Meebug #642',120,5.00,'Meebugs are unique 3D voxel characters, created by a custom generative algorithm, then registered on the Ethereum blockchain. The collection plays with the Meebits iconography and is a continuation of the Larva Lads universe.','nft_images/Meebug_64230.jpg','',8,4),(31,'Meebug #647',111,5.00,'Meebugs are unique 3D voxel characters, created by a custom generative algorithm, then registered on the Ethereum blockchain. The collection plays with the Meebits iconography and is a continuation of the Larva Lads universe.','nft_images/Meebug_64731.jpg','',8,4),(32,'Meebug #648',123,0.00,'Meebugs are unique 3D voxel characters, created by a custom generative algorithm, then registered on the Ethereum blockchain. The collection plays with the Meebits iconography and is a continuation of the Larva Lads universe.','nft_images/Meebug_64832.jpg','',8,8),(33,'Meebug #606',122,5.00,'Meebugs are unique 3D voxel characters, created by a custom generative algorithm, then registered on the Ethereum blockchain. The collection plays with the Meebits iconography and is a continuation of the Larva Lads universe.','nft_images/Meebug_60633.jpg','',8,4),(34,'Meebug #569',576,0.00,'Meebugs are unique 3D voxel characters, created by a custom generative algorithm, then registered on the Ethereum blockchain. The collection plays with the Meebits iconography and is a continuation of the Larva Lads universe.','nft_images/Meebug_56934_6WAdXhu.jpg','',8,8),(35,'Meebug #1',12,5.00,'Meebugs are unique 3D voxel characters, created by a custom generative algorithm, then registered on the Ethereum blockchain. The collection plays with the Meebits iconography and is a continuation of the Larva Lads universe.','nft_images/Meebug_135.jpg','',8,4),(36,'Meebug #12',120,0.00,'Meebugs are unique 3D voxel characters, created by a custom generative algorithm, then registered on the Ethereum blockchain. The collection plays with the Meebits iconography and is a continuation of the Larva Lads universe.','nft_images/Meebug_1236.jpg','',8,8),(37,'Meebug #5',50,0.00,'Meebugs are unique 3D voxel characters, created by a custom generative algorithm, then registered on the Ethereum blockchain. The collection plays with the Meebits iconography and is a continuation of the Larva Lads universe.','nft_images/Meebug_537.jpg','',8,8),(38,'Meebug #20',210,0.00,'Meebugs are unique 3D voxel characters, created by a custom generative algorithm, then registered on the Ethereum blockchain. The collection plays with the Meebits iconography and is a continuation of the Larva Lads universe.','nft_images/Meebug_2038.jpg','',8,8),(39,'Meebug #23',120,0.00,'Meebugs are unique 3D voxel characters, created by a custom generative algorithm, then registered on the Ethereum blockchain. The collection plays with the Meebits iconography and is a continuation of the Larva Lads universe.','nft_images/Meebug_2339.jpg','',8,8),(40,'Meebug #30',125,0.00,'Meebugs are unique 3D voxel characters, created by a custom generative algorithm, then registered on the Ethereum blockchain. The collection plays with the Meebits iconography and is a continuation of the Larva Lads universe.','nft_images/Meebug_3040.jpg','',8,8),(41,'mfer #5106',123,0.00,'mfers by sartoshi','nft_images/mfer_510641.jpg','',8,8),(42,'mfer #51',123,0.00,'mfers by sartoshi','nft_images/mfer_5142.jpg','',8,8),(43,'mfer #1',213,0.00,'mfers by sartoshi','nft_images/mfer_143.jpg','',8,8),(44,'mfer #30',120,0.00,'mfers by sartoshi','nft_images/mfer_3044.jpg','',8,8),(45,'mfer #13',123,0.00,'mfers by sartoshi','nft_images/mfer_1345.jpg','',8,8),(46,'mfer #69',160,0.00,'mfers by sartoshi','nft_images/mfer_6946.jpg','',8,8),(47,'CryptoPunk #1',123,0.00,'Punk','nft_images/CryptoPunk_147.jpg','',8,8),(48,'CryptoPunk #2',140,0.00,'punk','nft_images/CryptoPunk_248.jpg','',8,8),(49,'CryptoPunk #130',130,0.00,'punk','nft_images/CryptoPunk_13049.jpg','',8,8),(50,'CryptoPunk #111',123,0.00,'punk','nft_images/CryptoPunk_11150.jpg','',8,8),(51,'CryptoPunk #69',123,0.00,'punk','nft_images/CryptoPunk_6951.jpg','',8,2),(52,'CryptoPunk #32',233,0.00,'punk','nft_images/CryptoPunk_3252.jpg','',8,NULL),(53,'Travel Tiger #676',120,0.00,'Travel Tiger Club NFTs unlock access to the Smart Diamond membership on Travala.com','nft_images/Travel_Tiger_67653.jpg','',3,3),(54,'Travel Tiger #67',123,0.00,'Travel Tiger Club NFTs unlock access to the Smart Diamond membership on Travala.com','nft_images/Travel_Tiger_6754.jpg','',3,3),(55,'Travel Tiger #13',123,0.00,'Travel Tiger Club NFTs unlock access to the Smart Diamond membership on Travala.com','nft_images/Travel_Tiger_1355.jpg','',3,3),(56,'Travel Tiger #6',789,0.00,'Travel Tiger Club NFTs unlock access to the Smart Diamond membership on Travala.com','nft_images/Travel_Tiger_656.jpg','',3,3),(57,'Travel Tiger #12',123,0.00,'Travel Tiger Club NFTs unlock access to the Smart Diamond membership on Travala.com','nft_images/Travel_Tiger_1257.jpg','',3,3),(58,'Travel Tiger #134',133,0.00,'Travel Tiger Club NFTs unlock access to the Smart Diamond membership on Travala.com','nft_images/Travel_Tiger_13458.jpg','',3,3),(59,'Travel Tiger #134',133,0.00,'Travel Tiger Club NFTs unlock access to the Smart Diamond membership on Travala.com','nft_images/Travel_Tiger_13459.jpg','',3,3),(60,'Travel Tiger #32',322,0.00,'Travel Tiger Club NFTs unlock access to the Smart Diamond membership on Travala.com','nft_images/Travel_Tiger_3260.jpg','',3,3),(61,'Kong #8178',12,0.00,'Rumble Kong League is a competitive 3 vs 3 basketball experience, combining play-to-earn functionality with NFT Collection mechanics, enabling users to compete in engaging ways through NFTs.','nft_images/Kong_817861.jpg','',3,3),(62,'Kong #81',123,0.00,'Rumble Kong League is a competitive 3 vs 3 basketball experience, combining play-to-earn functionality with NFT Collection mechanics, enabling users to compete in engaging ways through NFTs.','nft_images/Kong_8162.jpg','',3,3),(63,'Kong #12',12,0.00,'Rumble Kong League is a competitive 3 vs 3 basketball experience, combining play-to-earn functionality with NFT Collection mechanics, enabling users to compete in engaging ways through NFTs.','nft_images/Kong_1263.jpg','',3,4),(64,'Kong #13',13,0.00,'Rumble Kong League is a competitive 3 vs 3 basketball experience, combining play-to-earn functionality with NFT Collection mechanics, enabling users to compete in engaging ways through NFTs.','nft_images/Kong_1364.jpg','',3,3),(65,'Kong #69',123,0.00,'Rumble Kong League is a competitive 3 vs 3 basketball experience, combining play-to-earn functionality with NFT Collection mechanics, enabling users to compete in engaging ways through NFTs.','nft_images/Kong_6965.jpg','',3,3),(66,'Kong #43',11,0.00,'Rumble Kong League is a competitive 3 vs 3 basketball experience, combining play-to-earn functionality with NFT Collection mechanics, enabling users to compete in engaging ways through NFTs.','nft_images/Kong_4366.jpg','',3,3),(67,'Kong #1000',122,0.00,'Rumble Kong League is a competitive 3 vs 3 basketball experience, combining play-to-earn functionality with NFT Collection mechanics, enabling users to compete in engaging ways through NFTs.','nft_images/Kong_100067.jpg','',3,3),(68,'Kong #1500',123,0.00,'Rumble Kong League is a competitive 3 vs 3 basketball experience, combining play-to-earn functionality with NFT Collection mechanics, enabling users to compete in engaging ways through NFTs.','nft_images/Kong_150068.jpg','',3,3),(69,'Kong #1300',12,0.00,'Rumble Kong League is a competitive 3 vs 3 basketball experience, combining play-to-earn functionality with NFT Collection mechanics, enabling users to compete in engaging ways through NFTs.','nft_images/Kong_130069.jpg','',3,3),(70,'Sugartown #3681',1234,0.00,'Oras are a collection of 9,999 unique beings from another dimension. They entered Sugartown through a rift in the space-time continuum that was accidentally created when the trio of farm friends were developing games.','nft_images/Sugartown_368170.jpg','',2,2),(71,'Sugartown #1',12,0.00,'Oras are a collection of 9,999 unique beings from another dimension. They entered Sugartown through a rift in the space-time continuum that was accidentally created when the trio of farm friends were developing games.','nft_images/Sugartown_171.jpg','',2,2),(72,'Sugartown#12',123,0.00,'Oras are a collection of 9,999 unique beings from another dimension. They entered Sugartown through a rift in the space-time continuum that was accidentally created when the trio of farm friends were developing games.','nft_images/Sugartown1272.jpg','',2,2),(73,'Sugartown #16',122,0.00,'Oras are a collection of 9,999 unique beings from another dimension. They entered Sugartown through a rift in the space-time continuum that was accidentally created when the trio of farm friends were developing games.','nft_images/Sugartown_1673.jpg','',2,2),(74,'Sugartown #34',111,0.00,'Oras are a collection of 9,999 unique beings from another dimension. They entered Sugartown through a rift in the space-time continuum that was accidentally created when the trio of farm friends were developing games.','nft_images/Sugartown_3474.jpg','',2,2),(75,'Sugartown #69',111,0.00,'Oras are a collection of 9,999 unique beings from another dimension. They entered Sugartown through a rift in the space-time continuum that was accidentally created when the trio of farm friends were developing games.','nft_images/Sugartown_6975.jpg','',2,2),(76,'Sugartown#90',123,0.00,'Oras are a collection of 9,999 unique beings from another dimension. They entered Sugartown through a rift in the space-time continuum that was accidentally created when the trio of farm friends were developing games.','nft_images/Sugartown9076.jpg','',2,2),(77,'Sugartown #100',122,0.00,'Oras are a collection of 9,999 unique beings from another dimension. They entered Sugartown through a rift in the space-time continuum that was accidentally created when the trio of farm friends were developing games.','nft_images/Sugartown_10077.jpg','',2,2),(78,'Sugartown #35',132,0.00,'Oras are a collection of 9,999 unique beings from another dimension. They entered Sugartown through a rift in the space-time continuum that was accidentally created when the trio of farm friends were developing games.','nft_images/Sugartown_3578.jpg','',2,2),(79,'Sugartown #201',122,0.00,'Oras are a collection of 9,999 unique beings from another dimension. They entered Sugartown through a rift in the space-time continuum that was accidentally created when the trio of farm friends were developing games.','nft_images/Sugartown_20179.jpg','',2,2),(80,'Sugartown  #78',12,0.00,'Oras are a collection of 9,999 unique beings from another dimension. They entered Sugartown through a rift in the space-time continuum that was accidentally created when the trio of farm friends were developing games.','nft_images/Sugartown__7880.jpg','',2,2),(81,'Lil Pudgy #21921',123,0.00,'Lil Pudgys are a collection of 22,222 randomly generated NFTs minted on Ethereum.','nft_images/Lil_Pudgy_2192181.jpg','',2,2),(82,'Lil Pudgy #21921',123,0.00,'Lil Pudgys are a collection of 22,222 randomly generated NFTs minted on Ethereum.','nft_images/Lil_Pudgy_2192182.jpg','',2,6),(83,'Lil Pudgy #21',123,0.00,'Lil Pudgys are a collection of 22,222 randomly generated NFTs minted on Ethereum.','nft_images/Lil_Pudgy_2183.jpg','',2,2),(84,'Lil Pudgy #1',123,0.00,'Lil Pudgys are a collection of 22,222 randomly generated NFTs minted on Ethereum.','nft_images/Lil_Pudgy_184.jpg','',2,2),(85,'Lil Pudgy #200',213,0.00,'Lil Pudgys are a collection of 22,222 randomly generated NFTs minted on Ethereum.','nft_images/Lil_Pudgy_20085.jpg','',2,2),(86,'Lil Pudgy #300',321,0.00,'Lil Pudgys are a collection of 22,222 randomly generated NFTs minted on Ethereum.','nft_images/Lil_Pudgy_30086.jpg','',2,2),(87,'Lil Pudgy #13110',123,5.00,'Lil Pudgys are a collection of 22,222 randomly generated NFTs minted on Ethereum.','nft_images/Lil_Pudgy_1311087.jpg','',2,NULL),(88,'Super#4524',13,0.00,'Super Cool World is a generative PFP-based project created as an alternative way to interact with fans and collectors. Nina Chanel Abney has completely embraced NFT as a new medium and is interested in the endless potential and capabilities of NFTs that allow for a much deeper engagement with one\'s community.','nft_images/Super452488.jpg','',3,4),(89,'Super #1',13,5.00,'Super Cool World is a generative PFP-based project created as an alternative way to interact with fans and collectors. Nina Chanel Abney has completely embraced NFT as a new medium and is interested in the endless potential and capabilities of NFTs that allow for a much deeper engagement with one\'s community.','nft_images/Super_189.jpg','',3,4),(90,'Super #44',12,3.00,'Super Cool World is a generative PFP-based project created as an alternative way to interact with fans and collectors. Nina Chanel Abney has completely embraced NFT as a new medium and is interested in the endless potential and capabilities of NFTs that allow for a much deeper engagement with one\'s community.','nft_images/Super_4490.jpg','',3,4),(91,'Super  #12',12,3.00,'Super Cool World is a generative PFP-based project created as an alternative way to interact with fans and collectors. Nina Chanel Abney has completely embraced NFT as a new medium and is interested in the endless potential and capabilities of NFTs that allow for a much deeper engagement with one\'s community.','nft_images/Super__1291.jpg','',3,4),(92,'Super  #60',43,4.00,'Super Cool World is a generative PFP-based project created as an alternative way to interact with fans and collectors. Nina Chanel Abney has completely embraced NFT as a new medium and is interested in the endless potential and capabilities of NFTs that allow for a much deeper engagement with one\'s community.','nft_images/Super__6092.jpg','',3,4),(93,'Super  #4',13,4.00,'Super Cool World is a generative PFP-based project created as an alternative way to interact with fans and collectors. Nina Chanel Abney has completely embraced NFT as a new medium and is interested in the endless potential and capabilities of NFTs that allow for a much deeper engagement with one\'s community.','nft_images/Super__493.jpg','',3,4);
/*!40000 ALTER TABLE `nft` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ocena`
--

DROP TABLE IF EXISTS `ocena`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ocena` (
  `IdOce` int NOT NULL AUTO_INCREMENT,
  `Ocena` int NOT NULL,
  `IdKor` int DEFAULT NULL,
  `IdNFT` int NOT NULL,
  PRIMARY KEY (`IdOce`),
  KEY `ocena_IdNFT_b0e8ed17_fk_nft_IdNFT` (`IdNFT`),
  KEY `ocena_IdKor_bc4585c5_fk_registrovanikorisnik_IdKor` (`IdKor`),
  CONSTRAINT `ocena_IdKor_bc4585c5_fk_registrovanikorisnik_IdKor` FOREIGN KEY (`IdKor`) REFERENCES `registrovanikorisnik` (`IdKor`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `ocena_IdNFT_b0e8ed17_fk_nft_IdNFT` FOREIGN KEY (`IdNFT`) REFERENCES `nft` (`IdNFT`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ocena`
--

LOCK TABLES `ocena` WRITE;
/*!40000 ALTER TABLE `ocena` DISABLE KEYS */;
INSERT INTO `ocena` VALUES (1,4,8,16),(2,5,8,11),(3,5,3,16),(4,5,3,17),(5,4,3,18),(6,5,3,19),(7,5,4,89),(8,3,4,90),(9,4,4,92),(10,4,4,93),(11,3,4,91),(12,5,4,30),(13,5,4,31),(14,5,4,33),(15,5,4,35),(16,5,NULL,87);
/*!40000 ALTER TABLE `ocena` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portfolio`
--

DROP TABLE IF EXISTS `portfolio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `portfolio` (
  `IdLis` int NOT NULL,
  PRIMARY KEY (`IdLis`),
  CONSTRAINT `portfolio_IdLis_5d02d2a1_fk_listanft_IdLis` FOREIGN KEY (`IdLis`) REFERENCES `listanft` (`IdLis`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portfolio`
--

LOCK TABLES `portfolio` WRITE;
/*!40000 ALTER TABLE `portfolio` DISABLE KEYS */;
INSERT INTO `portfolio` VALUES (2),(4),(15);
/*!40000 ALTER TABLE `portfolio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pripada`
--

DROP TABLE IF EXISTS `pripada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pripada` (
  `IdPri` int NOT NULL AUTO_INCREMENT,
  `IdLis` int NOT NULL,
  `IdNFT` int NOT NULL,
  PRIMARY KEY (`IdPri`),
  KEY `pripada_IdLis_3fa60898_fk_listanft_IdLis` (`IdLis`),
  KEY `pripada_IdNFT_6ba746bf_fk_nft_IdNFT` (`IdNFT`),
  CONSTRAINT `pripada_IdLis_3fa60898_fk_listanft_IdLis` FOREIGN KEY (`IdLis`) REFERENCES `listanft` (`IdLis`),
  CONSTRAINT `pripada_IdNFT_6ba746bf_fk_nft_IdNFT` FOREIGN KEY (`IdNFT`) REFERENCES `nft` (`IdNFT`)
) ENGINE=InnoDB AUTO_INCREMENT=321 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pripada`
--

LOCK TABLES `pripada` WRITE;
/*!40000 ALTER TABLE `pripada` DISABLE KEYS */;
INSERT INTO `pripada` VALUES (1,3,1),(2,4,1),(3,3,2),(4,4,2),(5,3,3),(6,4,3),(7,3,4),(8,4,4),(9,3,5),(10,4,5),(11,3,6),(12,4,6),(13,3,7),(14,4,7),(15,9,1),(16,9,2),(17,9,5),(18,9,6),(19,9,7),(20,3,8),(21,4,8),(22,3,9),(23,4,9),(25,4,10),(26,10,3),(27,10,4),(28,10,8),(29,10,9),(31,1,11),(32,2,11),(33,1,12),(34,2,12),(35,1,13),(36,2,13),(37,1,14),(38,2,14),(39,1,15),(40,2,15),(41,11,11),(42,11,12),(43,11,13),(44,11,14),(45,11,15),(46,1,16),(47,2,16),(48,1,17),(49,2,17),(50,1,18),(51,2,18),(52,1,19),(53,2,19),(55,2,20),(56,12,16),(57,12,17),(58,12,18),(59,12,19),(62,2,21),(64,2,22),(66,2,23),(67,1,24),(68,2,24),(70,2,25),(72,2,26),(73,1,27),(74,2,27),(75,1,28),(76,2,28),(77,1,29),(78,2,29),(85,6,21),(86,6,23),(87,6,26),(88,3,22),(89,3,25),(91,15,30),(93,15,31),(94,14,32),(95,15,32),(97,15,33),(98,14,34),(99,15,34),(101,15,35),(102,14,36),(103,15,36),(104,14,37),(105,15,37),(106,14,38),(107,15,38),(108,14,39),(109,15,39),(110,14,40),(111,15,40),(112,14,41),(113,15,41),(114,14,42),(115,15,42),(116,14,43),(117,15,43),(118,14,44),(119,15,44),(120,14,45),(121,15,45),(122,14,46),(123,15,46),(124,14,47),(125,15,47),(126,14,48),(127,15,48),(128,14,49),(129,15,49),(130,14,50),(131,15,50),(133,15,51),(135,15,52),(136,14,20),(137,14,10),(140,17,32),(142,17,34),(144,17,36),(145,17,37),(146,17,38),(147,17,39),(148,17,40),(149,18,41),(150,18,42),(151,18,43),(152,18,44),(153,18,45),(154,18,46),(155,19,47),(156,19,48),(157,19,49),(158,19,50),(161,3,53),(162,4,53),(163,3,54),(164,4,54),(165,3,55),(166,4,55),(167,3,56),(168,4,56),(169,3,57),(170,4,57),(171,3,58),(172,4,58),(173,3,59),(174,4,59),(175,3,60),(176,4,60),(177,20,53),(178,20,54),(179,20,55),(180,20,56),(181,20,57),(182,20,58),(183,20,59),(184,20,60),(185,3,61),(186,4,61),(187,3,62),(188,4,62),(190,4,63),(191,3,64),(192,4,64),(193,3,65),(194,4,65),(195,3,66),(196,4,66),(197,3,67),(198,4,67),(199,3,68),(200,4,68),(201,3,69),(202,4,69),(203,21,61),(204,21,62),(206,21,64),(207,21,65),(208,21,66),(209,21,67),(210,21,68),(211,21,69),(212,1,70),(213,2,70),(214,1,71),(215,2,71),(216,1,72),(217,2,72),(218,1,73),(219,2,73),(220,1,74),(221,2,74),(222,1,75),(223,2,75),(224,1,76),(225,2,76),(226,1,77),(227,2,77),(228,1,78),(229,2,78),(230,1,79),(231,2,79),(232,1,80),(233,2,80),(234,22,70),(235,22,71),(236,22,72),(237,22,73),(238,22,74),(239,22,75),(240,22,76),(241,22,77),(242,22,78),(243,22,79),(244,22,80),(245,1,81),(246,2,81),(248,2,82),(249,1,83),(250,2,83),(251,1,84),(252,2,84),(253,1,85),(254,2,85),(255,1,86),(256,2,86),(258,2,87),(259,23,81),(261,23,83),(262,23,84),(263,23,85),(264,23,86),(267,4,88),(269,4,89),(271,4,90),(273,4,91),(275,4,92),(277,4,93),(284,5,88),(285,5,89),(286,5,90),(287,5,92),(288,5,93),(289,5,91),(290,26,88),(291,26,89),(292,26,90),(293,26,91),(294,26,92),(295,26,93),(296,5,30),(297,5,31),(298,5,33),(299,5,35),(300,5,63),(301,27,30),(302,27,31),(303,27,33),(304,27,35),(305,28,30),(306,28,31),(307,28,33),(308,28,35),(309,28,63),(310,28,88),(311,28,89),(312,28,90),(313,28,91),(314,28,92),(315,28,93),(319,1,51),(320,7,82);
/*!40000 ALTER TABLE `pripada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registrovanikorisnik`
--

DROP TABLE IF EXISTS `registrovanikorisnik`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registrovanikorisnik` (
  `IdKor` int NOT NULL,
  `Ime` varchar(20) NOT NULL,
  `Prezime` varchar(20) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `BrojTelefona` varchar(20) NOT NULL,
  `DatumRodjenja` datetime(6) NOT NULL,
  `MestoRodjenja` varchar(20) NOT NULL,
  `BrojKartice` varchar(16) NOT NULL,
  `Slika` varchar(100) NOT NULL,
  `prodatihNft` int NOT NULL,
  `kupljenihNft` int NOT NULL,
  `DatumKreiranja` date DEFAULT NULL,
  PRIMARY KEY (`IdKor`),
  CONSTRAINT `registrovanikorisnik_IdKor_4599b5ed_fk_accounts_korisnik_idkor` FOREIGN KEY (`IdKor`) REFERENCES `accounts_korisnik` (`idkor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registrovanikorisnik`
--

LOCK TABLES `registrovanikorisnik` WRITE;
/*!40000 ALTER TABLE `registrovanikorisnik` DISABLE KEYS */;
INSERT INTO `registrovanikorisnik` VALUES (2,'Zeljko','Pantic','a@gmail.com','0643330022','2000-05-22 00:00:00.000000','Beograd','5435345','profile_images/WhatsApp_Image_2024-04-05_at_16.19.43_d4a822c4.jpg',8,1,'2024-05-30'),(3,'Bogdan','Bogdanovic','bogi@gmail.com','06465476','1992-05-05 00:00:00.000000','Beograd','132432','profile_images/Capture.PNG',8,2,'2024-05-30'),(4,'Margot','Robbie','margo@gmail.com','764634224','1990-05-06 00:00:00.000000','Sidnej','3241665','profile_images/def_profile_MqUzqOM.jpg',0,11,'2024-05-30'),(5,'Vojin','Radosavljevic','voks@gmail.com','0645550022','2002-07-21 00:00:00.000000','Uzice','878568','profile_images/def_profile_4L5lXvw.jpg',0,3,'2024-05-30'),(6,'Danil','Medvedev','medwed@gmail.com','86345234','1996-05-31 00:00:00.000000','Moskva','6578734','profile_images/def_profile_keNZopm.jpg',0,1,'2024-05-30'),(7,'Maria','Sharapova','mara@gmail.com','432764','1988-04-04 00:00:00.000000','Moskva','8543252','profile_images/def_profile_EfKz1Aa.jpg',0,0,'2024-05-30'),(8,'Nale','Gvozdenovic','ngvozdenovic16@gmail.com','0617647777','2002-02-10 00:00:00.000000','Beograd','16137868','profile_images/def_profile_v8BAx0e.jpg',6,2,'2024-05-31');
/*!40000 ALTER TABLE `registrovanikorisnik` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zahtevzaregistraciju`
--

DROP TABLE IF EXISTS `zahtevzaregistraciju`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zahtevzaregistraciju` (
  `IdZah` int NOT NULL AUTO_INCREMENT,
  `KorIme` varchar(32) NOT NULL,
  `Sifra` varchar(128) DEFAULT NULL,
  `Ime` varchar(20) NOT NULL,
  `Prezime` varchar(20) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `BrojTelefona` varchar(20) NOT NULL,
  `DatumRodjenja` date NOT NULL,
  `MestoRodjenja` varchar(20) NOT NULL,
  `BrojKartice` varchar(16) NOT NULL,
  `Uloga` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`IdZah`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zahtevzaregistraciju`
--

LOCK TABLES `zahtevzaregistraciju` WRITE;
/*!40000 ALTER TABLE `zahtevzaregistraciju` DISABLE KEYS */;
INSERT INTO `zahtevzaregistraciju` VALUES (4,'stefi123','12345678','Stefan','Radun','stef6@gmail.com','0617649999','2000-02-10','Beograd','16137868212','kolekcionar'),(5,'kupac','12345678','Kupac','Kupac','kupac6@gmail.com','0617640000','1992-02-12','Nis','6675678792','kupac'),(6,'kolekcionar','12345678','Kolekcionar','Kolekc','kolekc16@gmail.com','0617640001','2000-02-10','Beograd','9712987983','kolekcionar'),(7,'kreator','12345678','Kreator','Kreator','vic16@gmail.com','0909098','2000-02-10','Zlatibor','21333213','kreator');
/*!40000 ALTER TABLE `zahtevzaregistraciju` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-31 23:48:32
