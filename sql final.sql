/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - cosmetic_shopmes
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`cosmetic_shopmes` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `cosmetic_shopmes`;

/*Table structure for table `brand` */

DROP TABLE IF EXISTS `brand`;

CREATE TABLE `brand` (
  `brand_id` int(11) NOT NULL AUTO_INCREMENT,
  `brand_name` varchar(100) DEFAULT NULL,
  `brand_desc` varchar(100) DEFAULT NULL,
  `brand_status` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`brand_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `brand` */

insert  into `brand`(`brand_id`,`brand_name`,`brand_desc`,`brand_status`) values 
(1,'MAC',' SHOP With high-performance products ranging from the all-inclusive Studio Fix  Fluid SPF 15 to the ','1'),
(2,'Lakme ','Lakme maintains its quality and sufficiency. Their selection ranges from reasonably priced items to ','1'),
(3,'Maybelline','Maybelline was born in New York and is one of the highly-loved cosmetic brands in India.','1'),
(4,'Colorbar','Colorbar has carved out a place in the international beauty industry. Its items, which fall under th','1'),
(5,'Revlon','Revlon offers an extraordinary range of goods, including cosmetics, hair dyes, hair care, skincare, ','1'),
(6,'Minimalist','Find Right Products & Routines for Your Skin Needs. No Hidden Ingredients, No Opacity.','0');

/*Table structure for table `card` */

DROP TABLE IF EXISTS `card`;

CREATE TABLE `card` (
  `card_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `card_no` varchar(100) DEFAULT NULL,
  `card_name` varchar(100) DEFAULT NULL,
  `expiry_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`card_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `card` */

insert  into `card`(`card_id`,`customer_id`,`card_no`,`card_name`,`expiry_date`) values 
(1,1,'2345678900987656','annu','2026-07'),
(2,6,'2345678987654567','nivya','2023-03'),
(3,8,'1234567876545666','treesa','2026-02'),
(4,5,'1234567845673456','neha','2026-02'),
(5,9,'3432425435454432','213','2023-12');

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) DEFAULT NULL,
  `category_description` varchar(100) DEFAULT NULL,
  `status` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category_name`,`category_description`,`status`) values 
(1,'EYE','Variety of products under the category  of eye ranging from eyeshadow to eye liners','1'),
(3,'LIPS','Lips are one of the most attractive features of your face.Balms, liners, glosses - each of them make','1'),
(4,'FACE','Facial Makeup Products are products that are used to color and highlight facial features. They can e','1'),
(5,'NAILS','Nail cosmetics include a broad range of beauty products that promote the appearance and durability o','1'),
(6,'SKIN','Products that enrich your skin to glow and keep it healthy','1');

/*Table structure for table `color` */

DROP TABLE IF EXISTS `color`;

CREATE TABLE `color` (
  `color_id` int(11) NOT NULL AUTO_INCREMENT,
  `color_name` varchar(100) DEFAULT NULL,
  `color_desc` varchar(100) DEFAULT NULL,
  `color_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`color_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `color` */

insert  into `color`(`color_id`,`color_name`,`color_desc`,`color_status`) values 
(1,'red','range of red shades','1'),
(2,'Green','variety of Green shades','1'),
(3,'Yellow','mixed varieties of yellow shades','1'),
(4,'Black','Black gives you stunning looks','1'),
(5,'Orange','varieties of orange shades','1'),
(6,'Pink','Cute shades of Pink','1'),
(7,'Blue','look stunningwith the range of blue colours','1'),
(8,'Peach','range of Peach shades','1'),
(9,'Natural','natural tone for skin','1');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

/*Table structure for table `courier` */

DROP TABLE IF EXISTS `courier`;

CREATE TABLE `courier` (
  `courier_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `courier_name` varchar(100) DEFAULT NULL,
  `courier_street` varchar(100) DEFAULT NULL,
  `courier_dist` varchar(100) DEFAULT NULL,
  `courier_state` varchar(100) DEFAULT NULL,
  `courier_pincode` varchar(100) DEFAULT NULL,
  `courier_phone` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`courier_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `courier` */

insert  into `courier`(`courier_id`,`staff_id`,`username`,`courier_name`,`courier_street`,`courier_dist`,`courier_state`,`courier_pincode`,`courier_phone`) values 
(7,0,'dtdc@gmail.com','DTDC Courier','Rajagiri valley','Ernakulam','kerala','682017','9876567899'),
(8,0,'instakart@gmail.com','Instakart services','kairali','Ernakulam','kerala','682023','9876567890'),
(9,0,'bluedart@gmail.com','Blue dart couriers',' Pullepady','Ernakulam','kerala','890989','7809453422');

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `customer_fname` varchar(100) DEFAULT NULL,
  `customer_lname` varchar(100) DEFAULT NULL,
  `customer_houser_name` varchar(100) DEFAULT NULL,
  `customer_street` varchar(100) DEFAULT NULL,
  `customer_dist` varchar(100) DEFAULT NULL,
  `customer_state` varchar(100) DEFAULT NULL,
  `customer_pincode` varchar(100) DEFAULT NULL,
  `customer_dob` varchar(100) DEFAULT NULL,
  `customer_gender` varchar(100) DEFAULT NULL,
  `customer_phone` varchar(100) DEFAULT NULL,
  `customer_status` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `customer` */

insert  into `customer`(`customer_id`,`username`,`customer_fname`,`customer_lname`,`customer_houser_name`,`customer_street`,`customer_dist`,`customer_state`,`customer_pincode`,`customer_dob`,`customer_gender`,`customer_phone`,`customer_status`) values 
(8,'treesa@gmail.com','Treesa','Jenny','treesahouse','treestreet','Thrissur','Kerala','987865','2002-07-10','female','8976345690',1),
(6,'nivya@gmail.com','nivya','elizabeth','nivyahouse','church road','Ernakulam','Kerala','682017','1999-07-08','female','7896547896',1),
(5,'neha@gmail.com','neha','niya','house','church road','ernakulam','kerala','682017','2000-01-13','female','8909876547',1),
(9,'jeena@gmail.com','jeenas','hs','houses','streets','Ernakulams','keralas','682024','2000-03-13','female','8976564323',1);

/*Table structure for table `delivery` */

DROP TABLE IF EXISTS `delivery`;

CREATE TABLE `delivery` (
  `delivery_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_master_id` int(11) DEFAULT NULL,
  `courier_id` int(11) DEFAULT NULL,
  `delivery_date` varchar(100) DEFAULT NULL,
  `status` varchar(41) DEFAULT NULL,
  PRIMARY KEY (`delivery_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `delivery` */

insert  into `delivery`(`delivery_id`,`order_master_id`,`courier_id`,`delivery_date`,`status`) values 
(1,1,7,'2023-03-14','Delivered'),
(2,2,7,'2023-03-15','Delivered'),
(3,4,7,'2023-03-15','Delivered'),
(4,17,7,'2023-03-20','Delivered');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL,
  `status` varchar(4) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`username`,`password`,`user_type`,`status`) values 
('admin@gmail.com','admin','admin','1'),
('treesa@gmail.com','treesa','customer','1'),
('ajay@gmail.com','ajay','staff','1'),
('dtdc@gmail.com','dtdc','courier','1'),
('reena@gmail.com','reena','staff','1'),
('neha@gmail.com','neha','customer','1'),
('devana@gmail.com','devana','staff','1'),
('bluedart@gmail.com','blue','courier','0'),
('jay@gmail.com','jay','staff','0'),
('nivya@gmail.com','nivya','customer','1'),
('sreya@gmail.com','sreya','staff','1'),
('instakart@gmail.com','instakart','courier','1'),
('jeena@gmail.com','jeena','customer','1'),
('hai@gmail.com','hello','vendor','1'),
('hai11@gmail.com','hai','vendor','1'),
('glowel@gmail.com','hello','vendor','1');

/*Table structure for table `order_details` */

DROP TABLE IF EXISTS `order_details`;

CREATE TABLE `order_details` (
  `order_details_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_master_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `total_price` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`order_details_id`)
) ENGINE=MyISAM AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;

/*Data for the table `order_details` */

insert  into `order_details`(`order_details_id`,`order_master_id`,`product_id`,`quantity`,`total_price`) values 
(1,1,7,'1','133'),
(2,2,2,'2','264'),
(14,13,8,'3','540'),
(4,4,8,'2','360'),
(7,7,11,'3','396'),
(9,9,11,'1','132'),
(20,18,3,'1','3'),
(11,8,12,'3','223'),
(16,15,8,'4','720'),
(19,17,1,'2','121'),
(21,19,13,'1','132'),
(22,20,1,'2','121'),
(23,21,1,'1','121'),
(24,22,5,'1','110'),
(25,23,5,'1','220'),
(26,24,5,'1','165'),
(29,27,4,'2','330'),
(28,26,4,'3','495'),
(30,28,4,'2','440'),
(31,14,7,'2','264');

/*Table structure for table `order_master` */

DROP TABLE IF EXISTS `order_master`;

CREATE TABLE `order_master` (
  `order_master_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `total_amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `order_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`order_master_id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

/*Data for the table `order_master` */

insert  into `order_master`(`order_master_id`,`customer_id`,`total_amount`,`date`,`order_status`) values 
(1,8,'132','2023-03-14','Delivered'),
(2,5,'264','2023-03-15','Delivered'),
(4,8,'360','2023-03-15','Delivered'),
(8,5,'396','2023-03-15','Paid'),
(7,8,'396','2023-03-15','Paid'),
(9,8,'132','2023-03-15','Paid'),
(17,8,'240','2023-03-18','Delivered'),
(13,5,'540','2023-03-15','Paid'),
(14,9,'264','2023-03-15','Paid'),
(15,6,'720','2023-03-15','Paid'),
(18,6,'132','2023-03-18','Paid'),
(19,8,'132','2023-03-18','Paid'),
(20,8,'240','2023-03-20','Paid'),
(21,8,'120','2023-03-20','Paid'),
(22,8,'110','2023-03-20','Paid'),
(23,8,'220','2023-03-20','Paid'),
(24,8,'165','2023-03-20','Paid'),
(27,8,'330','2023-03-20','Paid'),
(26,6,'495','2023-03-20','Paid'),
(28,8,'440','2023-03-20','pending');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `card_id` int(11) DEFAULT NULL,
  `order_master_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`card_id`,`order_master_id`,`amount`,`date`) values 
(1,3,1,'132','2023-03-14'),
(2,4,2,'264','2023-03-15'),
(3,3,4,'360','2023-03-15'),
(4,3,7,'396','2023-03-15'),
(5,3,9,'132','2023-03-15'),
(6,4,8,'396','2023-03-15'),
(7,4,13,'540','2023-03-15'),
(8,2,15,'720','2023-03-15'),
(9,3,17,'240','2023-03-18'),
(10,2,18,'132','2023-03-18'),
(11,3,19,'132','2023-03-18'),
(12,3,20,'240','2023-03-20'),
(13,3,21,'120','2023-03-20'),
(14,3,21,'120','2023-03-20'),
(15,3,22,'110','2023-03-20'),
(16,3,23,'220','2023-03-20'),
(17,3,24,'165','2023-03-20'),
(18,2,26,'495','2023-03-20'),
(19,3,27,'330','2023-03-20'),
(20,5,14,'264','2023-03-31');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `subcategory_id` int(11) DEFAULT NULL,
  `color_id` int(11) DEFAULT NULL,
  `brand_id` int(11) DEFAULT NULL,
  `product_name` varchar(100) DEFAULT NULL,
  `product_description` varchar(100) DEFAULT NULL,
  `product_image` varchar(1000) DEFAULT NULL,
  `pro_per` varchar(10) NOT NULL,
  `product_exp` date DEFAULT NULL,
  `stock` varchar(100) DEFAULT NULL,
  `product_status` varchar(1) DEFAULT NULL,
  `rate` int(10) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`subcategory_id`,`color_id`,`brand_id`,`product_name`,`product_description`,`product_image`,`pro_per`,`product_exp`,`stock`,`product_status`,`rate`) values 
(1,2,1,1,'Vivid bright bluish-red','A creamy Lipstick formula with a soft cushiony feel, medium-to-full buildable coverage and a satin f','static/images21395b94-4d5c-45ab-b19d-4faefd34f3e2lipstick.jpeg','20','2027-07-25','4','1',120),
(2,4,4,3,'Maybelline New York Mascara','urls Lashes, Highly Pigmented Colour, Long-lasting, Waterproof, Hypercurl , Black, 9.2ml','static/images624ed374-96c2-44c1-8126-91f56cd5a572mascara.jpeg','10','2026-05-14','0','1',0),
(3,3,4,2,'LAKMÉ EYECONIC LIQUID EYELINER','Smudge proof bold and beautiful eyes\r\ngives your eyes a stylish look','static/imagesbefdbd3b-ae09-42be-a084-d10d28b1bce1eyeliner.png','20','2023-02-17','4','1',2),
(4,7,8,4,'Colorbar Radiant White UV Compact Powder','Protects from skin darkening/pigmentation and premature ageing; SPF 18 for sun protection\r\nVisible f','static/imagesaea7dd8f-27de-407b-acf7-cb340984a539contour.jpeg','10','2026-08-04','2','1',220),
(5,6,6,5,'Pinkish Lip Gloss','This lip gloss gives you shiny and smooth lips','static/images586672c5-ecaf-4da2-97eb-bd60855aec1elipgloss.jpeg','10','2026-07-15','0','1',165),
(7,5,1,3,'Red Lip Liner','Maybelline New York Makeup Color Sensational Shaping Lip Liner, Brick Red, Red Lip Liner, 0.01 Oz ','static/images169b756a-60f8-4262-85fb-4c1c417704a9lipliner.jpg','10','2025-02-08','3','1',132),
(8,8,9,2,'LAKMÉ PERFECTING LIQUID FOUNDATION','foundation that match your skin tone','static/images5d51ea62-40b5-4a5e-99a9-9a7156aba0fbfoundation.jpeg','10','2024-03-12','0','1',0),
(12,1,1,1,'mac eye shadow','hbn','static/imagesb2eecfbb-65ba-4ad1-a821-0d609d91f204serum.jpeg','10','2023-12-12','2','1',220),
(13,1,2,1,'MAC GREEN EYE-SHADOW','green eye shadow','static/images0dc209a1-8b08-4034-a9ee-637b55a0f487green.png','10','2025-10-10','0','1',0);

/*Table structure for table `purchase_child` */

DROP TABLE IF EXISTS `purchase_child`;

CREATE TABLE `purchase_child` (
  `purchase_child_id` int(11) NOT NULL AUTO_INCREMENT,
  `purchase_master_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `cost_price` varchar(100) DEFAULT NULL,
  `selling_price` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `pc_status` varchar(20) NOT NULL,
  PRIMARY KEY (`purchase_child_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `purchase_child` */

insert  into `purchase_child`(`purchase_child_id`,`purchase_master_id`,`product_id`,`cost_price`,`selling_price`,`quantity`,`pc_status`) values 
(1,1,1,'500','120','4','stock added'),
(2,2,3,'2','2','4','stock added'),
(3,3,5,'100','110','1','stock added'),
(4,3,5,'150','165','1','stock added'),
(5,4,5,'200','220','1','stock added'),
(6,5,7,'120','132','5','stock added'),
(7,6,7,'150','165','1','available'),
(8,7,4,'150','165','5','stock added'),
(9,7,4,'200','220','2','stock added'),
(10,8,12,'200','220','2','stock added');

/*Table structure for table `purchase_master` */

DROP TABLE IF EXISTS `purchase_master`;

CREATE TABLE `purchase_master` (
  `purchase_master_id` int(11) NOT NULL AUTO_INCREMENT,
  `vendor_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `total` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`purchase_master_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `purchase_master` */

insert  into `purchase_master`(`purchase_master_id`,`vendor_id`,`staff_id`,`total`,`status`) values 
(1,1,0,'1000','paid'),
(3,1,0,'250','paid'),
(2,3,0,'8','paid'),
(4,2,0,'200','paid'),
(5,1,0,'600','paid'),
(6,2,0,'150','paid'),
(7,1,0,'1150','paid'),
(8,7,0,'400','paid');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `staff_fname` varchar(100) DEFAULT NULL,
  `staff_lname` varchar(100) DEFAULT NULL,
  `staff_gender` varchar(100) DEFAULT NULL,
  `staff_dob` varchar(100) DEFAULT NULL,
  `staff_house_name` varchar(100) DEFAULT NULL,
  `staff_street` varchar(100) DEFAULT NULL,
  `staff_dist` varchar(100) DEFAULT NULL,
  `staff_state` varchar(100) DEFAULT NULL,
  `staff_pincode` varchar(100) DEFAULT NULL,
  `staff_phone` varchar(100) DEFAULT NULL,
  `staff_status` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`username`,`staff_fname`,`staff_lname`,`staff_gender`,`staff_dob`,`staff_house_name`,`staff_street`,`staff_dist`,`staff_state`,`staff_pincode`,`staff_phone`,`staff_status`) values 
(7,'sreya@gmail.com','sreya','jayeesh','female','1989-12-13','sreyahouse','sree nagar','malappuram','Kerala','680976','5678945678',1),
(5,'devana@gmail.com','devana','rose','female','2002-08-05','house','KV house','ernakulam','kerala','682018','9876567890',1),
(6,'reena@gmail.com','reena','joy','female','1999-03-24','green villas','burger street','Ernakulam','Kerala','908767','9087256378',1),
(4,'jay@gmail.com','jay','kumar','male','2000-02-01','sarra','church road','ernakulam','kerala','682017','9809876567',0),
(9,'ajay@gmail.com','Ajay','V','male','2000-12-10','ajayhouse','street','Kayamkulam','Kerala','896957','8092345604',1);

/*Table structure for table `subcategory` */

DROP TABLE IF EXISTS `subcategory`;

CREATE TABLE `subcategory` (
  `subcategory_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) NOT NULL,
  `subcategory_name` varchar(100) DEFAULT NULL,
  `subcategory_description` varchar(100) DEFAULT NULL,
  `sub_status` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`subcategory_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `subcategory` */

insert  into `subcategory`(`subcategory_id`,`category_id`,`subcategory_name`,`subcategory_description`,`sub_status`) values 
(1,1,'eyeshadow','dfcghj ','1'),
(2,3,'LIP STICK','make your lips attractive','1'),
(3,1,'Eye liners','Eyeliner is a special kind of pencil that is used on the edges of the eyelids to make the eyes look ','1'),
(4,1,'Mascara','Mascara is makeup that makes your eyelashes look longer and thicker. ','1'),
(5,3,'Lip Liners','Lip liner, also known as a lip pencil, is a cosmetic product. It is intended to fill in uneven areas','1'),
(6,3,'Lip Gloss','Lip gloss is a cosmetic used primarily to give lips a glossy luster, and sometimes to add a subtle c','1'),
(7,4,'Contour','Contouring is all about adding dimension to the face by sculpting the features and enhancing your fa','1'),
(8,4,'Foundation','Foundation is a liquid, cream, or powder makeup applied to the face and neck to create an even, unif','1'),
(9,4,'Compact','A compact (also powder box, powder case and flapjack) is a cosmetic product.','1'),
(10,5,'Nail polish remover','removes nail polish ','1');

/*Table structure for table `vendor` */

DROP TABLE IF EXISTS `vendor`;

CREATE TABLE `vendor` (
  `vendor_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `vendor_name` varchar(100) DEFAULT NULL,
  `vendor_phone` varchar(100) DEFAULT NULL,
  `vendor_email` varchar(100) DEFAULT NULL,
  `vendor_hno` varchar(100) DEFAULT NULL,
  `vendor_street` varchar(100) DEFAULT NULL,
  `vendor_dist` varchar(100) DEFAULT NULL,
  `vendor_pin` varchar(100) DEFAULT NULL,
  `vendor_date` varchar(100) DEFAULT NULL,
  `vendor_status` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`vendor_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `vendor` */

insert  into `vendor`(`vendor_id`,`username`,`staff_id`,`vendor_name`,`vendor_phone`,`vendor_email`,`vendor_hno`,`vendor_street`,`vendor_dist`,`vendor_pin`,`vendor_date`,`vendor_status`) values 
(1,'glowel@gmail.com',0,'GLOWEL COSMETICS','9876235644','glowel@gmail.com','glowel pvt','seoul','malappuram','789026','2023-02-24','1'),
(2,'kbeauty@gmail.com',0,'K.BEAUTY GLOBAL','7823567890','kbeauty@gmail.com','kb pvt','mareena nagar','kollam','809761','2023-02-22','1'),
(3,'kj@gmail.com',0,'KJ cosmetics','6789027364','kj@gmail.com','kjhouse','kairali','Ernakulam','789876','2023-12-12','1'),
(5,'merin@gmail.com',0,'merin','4567879878','merin@gmail.com','house','kairali','Ernakulam','682019','2023-03-13','1'),
(6,'sugar@gmail.com',0,'Sugar Cosmetics','7898672312','sugar@gmail.com','sugar pvt','Rajaji Junction','kollam','789026','2023-03-14','1'),
(7,'hai11@gmail.com',0,'user qwerty','2345678907','student@gmail.com','xfdsgdsg','gsdgdsg','Ernakulam1','123456','2023-04-08','1');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
