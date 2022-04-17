-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: iitgn_hostel
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `furniture`
--

DROP TABLE IF EXISTS `furniture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `furniture` (
  `furniture_id` int NOT NULL,
  `type` varchar(45) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `block_name` varchar(20) DEFAULT NULL,
  `room_no` int DEFAULT NULL,
  PRIMARY KEY (`furniture_id`),
  KEY `block_name` (`block_name`,`room_no`),
  CONSTRAINT `furniture_ibfk_1` FOREIGN KEY (`block_name`, `room_no`) REFERENCES `hostel_rooms` (`block_name`, `room_no`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `furniture`
--

LOCK TABLES `furniture` WRITE;
/*!40000 ALTER TABLE `furniture` DISABLE KEYS */;
INSERT INTO `furniture` VALUES (1,'CHAIR',500,'Aibaan',109),(2,'TABLE',750,'Aibaan',109),(3,'CHAIR',750,'Beauki',220);
/*!40000 ALTER TABLE `furniture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hostel`
--

DROP TABLE IF EXISTS `hostel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hostel` (
  `block_name` varchar(20) NOT NULL,
  `occupancy` int DEFAULT NULL,
  `capacity` int DEFAULT NULL,
  `laundry_days` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`block_name`),
  CONSTRAINT `hostel_chk_1` CHECK ((`occupancy` <= `capacity`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hostel`
--

LOCK TABLES `hostel` WRITE;
/*!40000 ALTER TABLE `hostel` DISABLE KEYS */;
INSERT INTO `hostel` VALUES ('Aibaan',124,200,'Monday'),('Beauki',120,250,'Thursday'),('Duven',140,180,'Tuesday');
/*!40000 ALTER TABLE `hostel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hostel_rooms`
--

DROP TABLE IF EXISTS `hostel_rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hostel_rooms` (
  `block_name` varchar(20) NOT NULL,
  `room_no` int NOT NULL,
  `sharing_type` varchar(20) DEFAULT NULL,
  `floor` int DEFAULT NULL,
  PRIMARY KEY (`room_no`,`block_name`),
  KEY `block_name` (`block_name`),
  CONSTRAINT `hostel_rooms_ibfk_1` FOREIGN KEY (`block_name`) REFERENCES `hostel` (`block_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `hostel_rooms_chk_1` CHECK (((`sharing_type` = _utf8mb4'single') or (`sharing_type` = _utf8mb4'double') or (`sharing_type` = _utf8mb4'triple')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hostel_rooms`
--

LOCK TABLES `hostel_rooms` WRITE;
/*!40000 ALTER TABLE `hostel_rooms` DISABLE KEYS */;
INSERT INTO `hostel_rooms` VALUES ('Aibaan',109,'Double',1),('Beauki',220,'Triple',2),('Duven',301,'Single',3);
/*!40000 ALTER TABLE `hostel_rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leave_rec`
--

DROP TABLE IF EXISTS `leave_rec`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leave_rec` (
  `record_no` int NOT NULL,
  `out_time` datetime DEFAULT NULL,
  `in_time` datetime DEFAULT NULL,
  `roll_no` int DEFAULT NULL,
  PRIMARY KEY (`record_no`),
  KEY `roll_no_idx` (`roll_no`),
  CONSTRAINT `leave_rec_ibfk_1` FOREIGN KEY (`roll_no`) REFERENCES `student` (`roll_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leave_rec`
--

LOCK TABLES `leave_rec` WRITE;
/*!40000 ALTER TABLE `leave_rec` DISABLE KEYS */;
INSERT INTO `leave_rec` VALUES (1,'2022-02-12 17:09:00','2022-02-10 09:00:00',21120016),(2,'2022-03-14 08:22:00','2022-03-17 23:50:00',19221109),(3,'2022-03-23 11:50:00','2022-03-20 06:08:00',21120016),(4,'2022-03-21 22:08:00','2022-03-20 07:10:00',21120006);
/*!40000 ALTER TABLE `leave_rec` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postgrad`
--

DROP TABLE IF EXISTS `postgrad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `postgrad` (
  `roll_no` int NOT NULL,
  `supervisior` varchar(45) DEFAULT NULL,
  `block_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`roll_no`),
  KEY `block_name_idx` (`block_name`),
  CONSTRAINT `postgrad_ibfk_1` FOREIGN KEY (`block_name`) REFERENCES `hostel` (`block_name`),
  CONSTRAINT `postgrad_ibfk_2` FOREIGN KEY (`roll_no`) REFERENCES `student` (`roll_no`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postgrad`
--

LOCK TABLES `postgrad` WRITE;
/*!40000 ALTER TABLE `postgrad` DISABLE KEYS */;
INSERT INTO `postgrad` VALUES (19110072,'Anirban Das Gupta','Duven'),(19221109,'Mayank Singh','Aibaan');
/*!40000 ALTER TABLE `postgrad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `staff_id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `service` varchar(45) NOT NULL,
  `salary` int DEFAULT NULL,
  PRIMARY KEY (`staff_id`),
  CONSTRAINT `staff_chk_1` CHECK ((`salary` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (101,'Ramesh','Sweeper',3000),(108,'Chetan','Plumber',3500),(201,'Sita','Cleaner',3000);
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_works_for`
--

DROP TABLE IF EXISTS `staff_works_for`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff_works_for` (
  `block_name` varchar(20) NOT NULL,
  `staff_id` int NOT NULL,
  `working_days` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`block_name`,`staff_id`),
  KEY `staff_id_idx` (`staff_id`),
  CONSTRAINT `staff_works_for_ibfk_1` FOREIGN KEY (`block_name`) REFERENCES `hostel` (`block_name`) ON DELETE CASCADE,
  CONSTRAINT `staff_works_for_ibfk_2` FOREIGN KEY (`staff_id`) REFERENCES `staff` (`staff_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_works_for`
--

LOCK TABLES `staff_works_for` WRITE;
/*!40000 ALTER TABLE `staff_works_for` DISABLE KEYS */;
INSERT INTO `staff_works_for` VALUES ('Aibaan',101,'Tuesday'),('Aibaan',108,'Sunday'),('Duven',108,'Friday');
/*!40000 ALTER TABLE `staff_works_for` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `roll_no` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `branch` varchar(45) NOT NULL,
  `street` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `email_id` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`roll_no`),
  UNIQUE KEY `email_id_UNIQUE` (`email_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (19110072,'Pranav Ninawe','CSE','Itwari Street','Pune','Maharashtra','2001-10-07','prni@gmail.com'),(19221109,'Iram Nawab','Biotechnology','Dal Lake Street','Srinagar','Kashmir','1998-06-13','iranaw@gmail.com'),(21120006,'Darshan Patil','Civil ','AB 3, Civil Lane','Nandurbar','Maharashtra','2001-09-05','patdar@gmail.com'),(21120016,'Rovin Singh','CSE','Shadawal Park A/4 2 ','Boisar','Maharashtra','2002-11-20','rs206987@gmail.com');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_contact`
--

DROP TABLE IF EXISTS `student_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_contact` (
  `roll_no` int NOT NULL,
  `contact` bigint NOT NULL,
  PRIMARY KEY (`roll_no`,`contact`),
  CONSTRAINT `student_contact_ibfk_1` FOREIGN KEY (`roll_no`) REFERENCES `student` (`roll_no`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_contact`
--

LOCK TABLES `student_contact` WRITE;
/*!40000 ALTER TABLE `student_contact` DISABLE KEYS */;
INSERT INTO `student_contact` VALUES (19110072,9473517890),(19221109,8463720473),(21120006,7482940371),(21120016,8379047632),(21120016,9876543210);
/*!40000 ALTER TABLE `student_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_hostel_payment`
--

DROP TABLE IF EXISTS `student_hostel_payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_hostel_payment` (
  `transaction_id` int NOT NULL,
  `roll_no` int NOT NULL,
  `block_name` varchar(20) NOT NULL,
  PRIMARY KEY (`transaction_id`,`roll_no`,`block_name`),
  KEY `roll_no_idx` (`roll_no`),
  KEY `block_name_idx` (`block_name`),
  CONSTRAINT `student_hostel_payment_ibfk_1` FOREIGN KEY (`transaction_id`) REFERENCES `transaction` (`transaction_id`),
  CONSTRAINT `student_hostel_payment_ibfk_2` FOREIGN KEY (`roll_no`) REFERENCES `student` (`roll_no`),
  CONSTRAINT `student_hostel_payment_ibfk_3` FOREIGN KEY (`block_name`) REFERENCES `hostel` (`block_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_hostel_payment`
--

LOCK TABLES `student_hostel_payment` WRITE;
/*!40000 ALTER TABLE `student_hostel_payment` DISABLE KEYS */;
INSERT INTO `student_hostel_payment` VALUES (3,19110072,'Duven'),(4,19221109,'Aibaan'),(2,21120006,'Beauki'),(1,21120016,'Duven');
/*!40000 ALTER TABLE `student_hostel_payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction` (
  `transaction_id` int NOT NULL,
  `amount` int DEFAULT NULL,
  `mode_of_payment` varchar(45) NOT NULL,
  PRIMARY KEY (`transaction_id`),
  CONSTRAINT `transaction_chk_1` CHECK ((`amount` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
INSERT INTO `transaction` VALUES (1,50000,'Online'),(2,50000,'Cash'),(3,45000,'Cheque'),(4,45000,'Card');
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `undergrad`
--

DROP TABLE IF EXISTS `undergrad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `undergrad` (
  `roll_no` int NOT NULL,
  `JEE_score` float DEFAULT NULL,
  `block_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`roll_no`),
  KEY `block_name_idx` (`block_name`),
  CONSTRAINT `undergrad_ibfk_1` FOREIGN KEY (`roll_no`) REFERENCES `student` (`roll_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `undergrad_ibfk_2` FOREIGN KEY (`block_name`) REFERENCES `hostel` (`block_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `undergrad`
--

LOCK TABLES `undergrad` WRITE;
/*!40000 ALTER TABLE `undergrad` DISABLE KEYS */;
INSERT INTO `undergrad` VALUES (21120006,94.9,'Beauki'),(21120016,99,'Duven');
/*!40000 ALTER TABLE `undergrad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `warden`
--

DROP TABLE IF EXISTS `warden`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `warden` (
  `warden_id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `salary` int DEFAULT NULL,
  `block_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`warden_id`),
  KEY `block_name_idx` (`block_name`),
  CONSTRAINT `` FOREIGN KEY (`block_name`) REFERENCES `hostel` (`block_name`) ON DELETE SET NULL,
  CONSTRAINT `warden_chk_1` CHECK ((`salary` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warden`
--

LOCK TABLES `warden` WRITE;
/*!40000 ALTER TABLE `warden` DISABLE KEYS */;
INSERT INTO `warden` VALUES (901,'Ankita Deshmukh',20000,'Aibaan'),(902,'Bharat Bhai',20000,'Duven'),(903,'Vishwajeet Mishra',20000,'Beauki');
/*!40000 ALTER TABLE `warden` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `warden_contact`
--

DROP TABLE IF EXISTS `warden_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `warden_contact` (
  `warden_id` int NOT NULL,
  `contact` bigint NOT NULL,
  PRIMARY KEY (`warden_id`,`contact`),
  CONSTRAINT `warden_contact_ibfk_1` FOREIGN KEY (`warden_id`) REFERENCES `warden` (`warden_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warden_contact`
--

LOCK TABLES `warden_contact` WRITE;
/*!40000 ALTER TABLE `warden_contact` DISABLE KEYS */;
INSERT INTO `warden_contact` VALUES (902,7890356271),(902,9822738632),(903,7893163777);
/*!40000 ALTER TABLE `warden_contact` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-31  4:57:08
