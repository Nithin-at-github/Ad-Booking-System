/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 8.0.18 : Database - multi_tier_ad_booking
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`multi_tier_ad_booking` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `multi_tier_ad_booking`;

/*Table structure for table `adcontent` */

DROP TABLE IF EXISTS `adcontent`;

CREATE TABLE `adcontent` (
  `content_id` int(11) NOT NULL AUTO_INCREMENT,
  `ad_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `ad_type` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `file_path` varchar(500) DEFAULT NULL,
  `message` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`content_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `adcontent` */

insert  into `adcontent`(`content_id`,`ad_id`,`user_id`,`ad_type`,`date`,`file_path`,`message`,`status`) values (1,1,1,'space','12/131/1/21','static/images/bd5c7e2b-31e4-430e-8d6e-06423bc0c2a9abc.jpeg','aaa','Approved'),(2,1,1,'custom','123221423','static/images/8e520a69-45ba-4266-9cc8-218587eb3822abc.jpeg','aa','Approved'),(8,1,2,'space','2020-02-18','static/images/764d337b-dd74-4a3a-89ab-237a7ac0998dabc.jpeg','noo','Approved'),(9,1,3,'space','2020-02-18','static/images/09f404ac-fc95-45e9-8964-b101910b72dcabc.jpeg','need the plot','Approved'),(10,2,4,'space','2020-02-18','static/images/3210d943-b5ef-4c2e-9d04-b728ddb8feb3abc.jpeg','hi','Approved'),(11,2,2,'custom','2020-02-19','static/images/a092273b-e8a9-4b54-847f-d83363ba95caabc.jpeg','new','Booked');

/*Table structure for table `adspaces` */

DROP TABLE IF EXISTS `adspaces`;

CREATE TABLE `adspaces` (
  `ad_space_id` int(11) NOT NULL AUTO_INCREMENT,
  `media_id` int(11) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ad_space_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `adspaces` */

insert  into `adspaces`(`ad_space_id`,`media_id`,`description`,`amount`,`status`) values (1,2,'husxbjhvgsa','2000','Approved'),(2,2,'q','5000','Approved');

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category_name`,`description`) values (2,'Electronics','Electrinic items');

/*Table structure for table `commission` */

DROP TABLE IF EXISTS `commission`;

CREATE TABLE `commission` (
  `commission_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT NULL,
  `percentage` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`commission_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `commission` */

insert  into `commission`(`commission_id`,`category_id`,`percentage`,`type`) values (2,2,'10','space');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `complaint_description` varchar(50) DEFAULT NULL,
  `solution_description` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`user_id`,`complaint_description`,`solution_description`,`date`) values (1,1,'not interesting','We\'ll make it better','12/2/4'),(2,2,'not interesting','pending','2021-07-09'),(3,2,'not interesting','pending','2021-07-09');

/*Table structure for table `customrequest` */

DROP TABLE IF EXISTS `customrequest`;

CREATE TABLE `customrequest` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `request_description` varchar(50) DEFAULT NULL,
  `request_status` varchar(50) DEFAULT NULL,
  `date_requested` varchar(50) DEFAULT NULL,
  `media_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `customrequest` */

insert  into `customrequest`(`request_id`,`user_id`,`category_id`,`request_description`,`request_status`,`date_requested`,`media_id`) values (1,1,2,'need a big space','Accepted by Admin','12/2/2020',0),(2,2,2,'gggg','Waiting for Approval','2020-02-19',0),(3,2,2,'hii need high','pending','2020-02-19',0);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`log_id`,`username`,`password`,`user_type`) values (1,'admin','admin','admin'),(3,'surya@gmail.com','surya','media'),(7,'vishnu','vishnu','user');

/*Table structure for table `medias` */

DROP TABLE IF EXISTS `medias`;

CREATE TABLE `medias` (
  `media_id` int(11) NOT NULL AUTO_INCREMENT,
  `log_id` int(11) DEFAULT NULL,
  `media_name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`media_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `medias` */

insert  into `medias`(`media_id`,`log_id`,`media_name`,`email`,`phone`,`category_id`,`description`) values (2,3,'surya','surya@gmail.com','9048174031',2,'qqqqq');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `pay_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `ad_id` int(11) DEFAULT NULL,
  `ad_type` varchar(50) DEFAULT NULL,
  `ad_amount` varchar(50) DEFAULT NULL,
  `net_amount` varchar(50) DEFAULT NULL,
  `payment_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`pay_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`pay_id`,`user_id`,`date`,`ad_id`,`ad_type`,`ad_amount`,`net_amount`,`payment_type`) values (1,1,'12/2/3',1,'space','1000','1250','cash'),(2,1,'2020-02-15',2,'custom','1300','2500','paid'),(3,2,'2020-02-18',1,'space','2000','2200.0','cash'),(4,2,'2020-02-18',2,'space','5000','5500.0','cash');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `log_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `middle_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `house_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`user_id`,`log_id`,`first_name`,`middle_name`,`last_name`,`dob`,`phone`,`email`,`house_name`,`place`,`district`,`pincode`) values (1,NULL,'Roshin','','Shibu','03/11/2000','3232323232','roshin@gmail.com','parackal','manarcad','kottayam','686019'),(2,7,'vishnu ','vinod','p','26/07/1998','9048174031','vishnu.vinod.1004@gmail.com','pulickakuzhikarottu ','karimkunnam ','idukki','685586'),(3,8,'vishnu ','vinod','p','26/07/1998','9048174031','vishnu.vinod.1004@gmail.com','pulickakuzhikarottu ','karimkunnam ','idukki','685586'),(4,9,'vishnu ','vinod','p','26/07/1998','9048174031','vishnu.vinod.1004@gmail.com','pulickakuzhikarottu ','karimkunnam ','idukki','685586');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
