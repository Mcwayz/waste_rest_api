-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 04, 2024 at 07:55 AM
-- Server version: 11.3.2-MariaDB
-- PHP Version: 8.3.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `waste_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'Super Group');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),
(6, 1, 6),
(7, 1, 7),
(8, 1, 8),
(9, 1, 9),
(10, 1, 10),
(11, 1, 11),
(12, 1, 12),
(13, 1, 13),
(14, 1, 14),
(15, 1, 15),
(16, 1, 16),
(17, 1, 17),
(18, 1, 18),
(19, 1, 19),
(20, 1, 20),
(21, 1, 21),
(22, 1, 22),
(23, 1, 23),
(24, 1, 24),
(25, 1, 25),
(26, 1, 26),
(27, 1, 27),
(28, 1, 28),
(29, 1, 29),
(30, 1, 30),
(31, 1, 31),
(32, 1, 32),
(33, 1, 33),
(34, 1, 34),
(35, 1, 35),
(36, 1, 36),
(37, 1, 37),
(38, 1, 38),
(39, 1, 39),
(40, 1, 40),
(41, 1, 41),
(42, 1, 42),
(43, 1, 43),
(44, 1, 44),
(45, 1, 45),
(46, 1, 46),
(47, 1, 47),
(48, 1, 48),
(49, 1, 49),
(50, 1, 50),
(51, 1, 51),
(52, 1, 52),
(53, 1, 53),
(54, 1, 54),
(55, 1, 55),
(56, 1, 56),
(57, 1, 57),
(58, 1, 58),
(59, 1, 59),
(60, 1, 60),
(61, 1, 61),
(62, 1, 62),
(63, 1, 63),
(64, 1, 64),
(65, 1, 65),
(66, 1, 66),
(67, 1, 67),
(68, 1, 68);

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add collection', 7, 'add_collection'),
(26, 'Can change collection', 7, 'change_collection'),
(27, 'Can delete collection', 7, 'delete_collection'),
(28, 'Can view collection', 7, 'view_collection'),
(29, 'Can add collector profile', 8, 'add_collectorprofile'),
(30, 'Can change collector profile', 8, 'change_collectorprofile'),
(31, 'Can delete collector profile', 8, 'delete_collectorprofile'),
(32, 'Can view collector profile', 8, 'view_collectorprofile'),
(33, 'Can add customer profile', 9, 'add_customerprofile'),
(34, 'Can change customer profile', 9, 'change_customerprofile'),
(35, 'Can delete customer profile', 9, 'delete_customerprofile'),
(36, 'Can view customer profile', 9, 'view_customerprofile'),
(37, 'Can add wallet', 10, 'add_wallet'),
(38, 'Can change wallet', 10, 'change_wallet'),
(39, 'Can delete wallet', 10, 'delete_wallet'),
(40, 'Can view wallet', 10, 'view_wallet'),
(41, 'Can add waste', 11, 'add_waste'),
(42, 'Can change waste', 11, 'change_waste'),
(43, 'Can delete waste', 11, 'delete_waste'),
(44, 'Can view waste', 11, 'view_waste'),
(45, 'Can add wallet history', 12, 'add_wallethistory'),
(46, 'Can change wallet history', 12, 'change_wallethistory'),
(47, 'Can delete wallet history', 12, 'delete_wallethistory'),
(48, 'Can view wallet history', 12, 'view_wallethistory'),
(49, 'Can add requests', 13, 'add_requests'),
(50, 'Can change requests', 13, 'change_requests'),
(51, 'Can delete requests', 13, 'delete_requests'),
(52, 'Can view requests', 13, 'view_requests'),
(53, 'Can add ratings', 14, 'add_ratings'),
(54, 'Can change ratings', 14, 'change_ratings'),
(55, 'Can delete ratings', 14, 'delete_ratings'),
(56, 'Can view ratings', 14, 'view_ratings'),
(57, 'Can add commission collector', 15, 'add_commissioncollector'),
(58, 'Can change commission collector', 15, 'change_commissioncollector'),
(59, 'Can delete commission collector', 15, 'delete_commissioncollector'),
(60, 'Can view commission collector', 15, 'view_commissioncollector'),
(61, 'Can add waste gl', 16, 'add_wastegl'),
(62, 'Can change waste gl', 16, 'change_wastegl'),
(63, 'Can delete waste gl', 16, 'delete_wastegl'),
(64, 'Can view waste gl', 16, 'view_wastegl'),
(65, 'Can add collector commission', 15, 'add_collectorcommission'),
(66, 'Can change collector commission', 15, 'change_collectorcommission'),
(67, 'Can delete collector commission', 15, 'delete_collectorcommission'),
(68, 'Can view collector commission', 15, 'view_collectorcommission'),
(69, 'Can add service charge', 17, 'add_servicecharge'),
(70, 'Can change service charge', 17, 'change_servicecharge'),
(71, 'Can delete service charge', 17, 'delete_servicecharge'),
(72, 'Can view service charge', 17, 'view_servicecharge');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$8Rw7x8evRATBUzXHAZPqqZ$yWIB7PReQ2k64pumSDuMZKRRtAA+Pi/XuJUWPoJ6IGg=', NULL, 0, 'Mcwayz', 'Jack', 'Mcwayz', 'jack@email.com', 0, 1, '2024-02-27 07:16:57.411215'),
(2, 'pbkdf2_sha256$600000$RabIqOwJ5NXVlAfO2h9QEy$wK0MeCSyZTtgLM5gMlbPGuy9Iot194mR1FPdHYG9wxw=', NULL, 0, 'Babayega', 'John', 'Wick', 'jonathan@email.com', 0, 1, '2024-02-27 07:17:57.615818'),
(3, 'pbkdf2_sha256$600000$eponTootO9WorecrGxq6er$ZPdqNyX4+qdq2lOw2HmL4ujQX4euVLtQhUhfy78Yyq8=', NULL, 0, 'Nabster', 'John', 'Snow', 'nabster@email.com', 0, 1, '2024-02-27 14:04:48.700934'),
(4, 'pbkdf2_sha256$600000$PnCgf8rbdGC9KMC3mqe5Az$GhAUPbRIHy5M/bwE94+55nxaSUdOZwzq752Mep5zVhs=', '2024-05-29 13:15:09.548883', 1, 'Madara', 'Madara', 'Uchiha', 'mcwayzj@gmail.com', 1, 1, '2024-03-22 13:07:28.505301');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `base_collection`
--

CREATE TABLE `base_collection` (
  `collection_id` int(11) NOT NULL,
  `collection_date` datetime(6) NOT NULL,
  `collector_id` int(11) NOT NULL,
  `request_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `base_collection`
--

INSERT INTO `base_collection` (`collection_id`, `collection_date`, `collector_id`, `request_id`) VALUES
(1, '2024-04-15 13:08:59.757795', 1, 1),
(2, '2024-05-21 20:09:49.004476', 1, 2),
(3, '2024-05-31 07:00:00.167487', 1, 3),
(4, '2024-05-31 07:07:27.379212', 1, 4),
(5, '2024-05-31 07:11:06.480701', 1, 5),
(6, '2024-06-03 14:04:51.869809', 1, 6),
(7, '2024-06-03 14:27:52.967500', 1, 7);

-- --------------------------------------------------------

--
-- Table structure for table `base_collectorcommission`
--

CREATE TABLE `base_collectorcommission` (
  `txn_id` int(11) NOT NULL,
  `comission_settlement_date` datetime(6) NOT NULL,
  `comission` decimal(65,2) NOT NULL,
  `collector_id` int(11) NOT NULL,
  `extras` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `base_collectorprofile`
--

CREATE TABLE `base_collectorprofile` (
  `collector_id` int(11) NOT NULL,
  `vehicle` varchar(200) NOT NULL,
  `work_area` varchar(200) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `auth_id` int(11) NOT NULL,
  `waste_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `base_collectorprofile`
--

INSERT INTO `base_collectorprofile` (`collector_id`, `vehicle`, `work_area`, `timestamp`, `auth_id`, `waste_id`) VALUES
(1, 'Fuso : BBC 5673', 'Kabwata - Libala', '2024-02-27 07:17:57.814728', 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `base_customerprofile`
--

CREATE TABLE `base_customerprofile` (
  `customer_id` int(11) NOT NULL,
  `address` longtext NOT NULL,
  `auth_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `base_customerprofile`
--

INSERT INTO `base_customerprofile` (`customer_id`, `address`, `auth_id`) VALUES
(1, '60/263 Kabulonga Kudu St, Lusaka', 1),
(3, 'G124 Off Bulanda Rd, Chililabombwe', 3);

-- --------------------------------------------------------

--
-- Table structure for table `base_ratings`
--

CREATE TABLE `base_ratings` (
  `rating_id` int(11) NOT NULL,
  `rating_score` int(10) UNSIGNED NOT NULL CHECK (`rating_score` >= 0),
  `collection_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `base_requests`
--

CREATE TABLE `base_requests` (
  `request_id` int(11) NOT NULL,
  `location` longtext NOT NULL,
  `number_of_bags` int(10) UNSIGNED NOT NULL CHECK (`number_of_bags` >= 0),
  `request_status` varchar(100) NOT NULL,
  `request_date` datetime(6) NOT NULL,
  `collection_price` decimal(10,2) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `waste_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `base_requests`
--

INSERT INTO `base_requests` (`request_id`, `location`, `number_of_bags`, `request_status`, `request_date`, `collection_price`, `customer_id`, `waste_id`) VALUES
(1, '123 Main St, City', 2, 'Complete', '2024-04-15 12:11:24.700349', 100.00, 1, 1),
(2, '123 Main St, City', 1, 'Complete', '2024-05-21 20:07:08.079778', 40.00, 1, 1),
(3, '123 Main St, City', 1, 'Complete', '2024-05-30 15:08:45.300714', 55.00, 1, 1),
(4, '14 Main St, Lusaka', 1, 'Complete', '2024-05-31 07:04:44.405289', 40.00, 3, 1),
(5, '14 Main St, Lusaka', 2, 'Complete', '2024-05-31 07:09:33.566015', 80.00, 3, 1),
(6, '14 Main St, Lusaka', 3, 'Complete', '2024-06-03 13:59:34.453963', 120.00, 3, 1),
(7, '14 Main St, Lusaka', 4, 'Complete', '2024-06-03 14:20:03.058019', 160.00, 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `base_servicecharge`
--

CREATE TABLE `base_servicecharge` (
  `service_id` int(11) NOT NULL,
  `service_type` varchar(100) NOT NULL,
  `service_charge` decimal(65,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `base_servicecharge`
--

INSERT INTO `base_servicecharge` (`service_id`, `service_type`, `service_charge`) VALUES
(1, 'Collection', 3.00),
(2, 'Commission', 0.03);

-- --------------------------------------------------------

--
-- Table structure for table `base_wallet`
--

CREATE TABLE `base_wallet` (
  `wallet_id` int(11) NOT NULL,
  `balance` decimal(65,2) NOT NULL,
  `collector_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `base_wallet`
--

INSERT INTO `base_wallet` (`wallet_id`, `balance`, `collector_id`) VALUES
(1, 255.00, 1);

-- --------------------------------------------------------

--
-- Table structure for table `base_wallethistory`
--

CREATE TABLE `base_wallethistory` (
  `history_id` int(11) NOT NULL,
  `transaction_type` varchar(100) NOT NULL,
  `transaction_date` datetime(6) NOT NULL,
  `old_wallet_balance` decimal(65,2) NOT NULL,
  `new_wallet_balance` decimal(65,2) NOT NULL,
  `transaction_amount` decimal(65,2) NOT NULL,
  `wallet_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `base_wallethistory`
--

INSERT INTO `base_wallethistory` (`history_id`, `transaction_type`, `transaction_date`, `old_wallet_balance`, `new_wallet_balance`, `transaction_amount`, `wallet_id`) VALUES
(1, 'Debit', '2024-04-15 13:08:59.789326', 850.00, 750.00, 100.00, 1),
(2, 'Debit', '2024-05-21 20:09:49.020341', 750.00, 710.00, 40.00, 1),
(3, 'Debit', '2024-05-31 07:00:00.175469', 710.00, 655.00, 55.00, 1),
(4, 'Debit', '2024-05-31 07:07:27.393983', 655.00, 615.00, 40.00, 1),
(5, 'Debit', '2024-05-31 07:11:06.485742', 615.00, 535.00, 80.00, 1),
(6, 'Debit', '2024-06-03 14:04:51.876848', 535.00, 415.00, 120.00, 1),
(7, 'Debit', '2024-06-03 14:27:52.982449', 415.00, 255.00, 160.00, 1);

-- --------------------------------------------------------

--
-- Table structure for table `base_waste`
--

CREATE TABLE `base_waste` (
  `waste_id` int(11) NOT NULL,
  `waste_type` varchar(100) NOT NULL,
  `waste_desc` varchar(500) NOT NULL,
  `collection_price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `base_waste`
--

INSERT INTO `base_waste` (`waste_id`, `waste_type`, `waste_desc`, `collection_price`) VALUES
(1, 'Domestic Waste', 'Waste generated from households and residential areas. This includes materials such as food scraps, paper, cardboard, plastics, and other general household items.', 40.00),
(2, 'Construction Waste', 'Waste generated from construction, renovation, demolition, or deconstruction activities. This includes materials such as concrete, wood, and other building materials.', 200.00),
(3, 'Septic Waste', 'Waste from septic systems, including human waste, wastewater, and organic matter. Proper disposal of septic waste is essential to prevent contamination of water sources and the spread of diseases.', 300.00),
(4, 'Organic Waste', 'Biodegradable waste from plant or animal sources. This includes food scraps, yard waste, and other organic materials. Organic waste can be composted to produce nutrient-rich soil.', 50.00);

-- --------------------------------------------------------

--
-- Table structure for table `base_wastegl`
--

CREATE TABLE `base_wastegl` (
  `gl_id` int(11) NOT NULL,
  `transaction_type` varchar(100) NOT NULL,
  `transaction_date` datetime(6) NOT NULL,
  `service_charge` decimal(65,2) NOT NULL,
  `old_GL_balance` decimal(65,2) NOT NULL,
  `new_GL_balance` decimal(65,2) NOT NULL,
  `extras` varchar(100) NOT NULL,
  `collection_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `base_wastegl`
--

INSERT INTO `base_wastegl` (`gl_id`, `transaction_type`, `transaction_date`, `service_charge`, `old_GL_balance`, `new_GL_balance`, `extras`, `collection_id`) VALUES
(1, 'DEPOSIT', '2024-04-15 13:08:59.785505', 2.00, 0.00, 95.00, 'Funded By Completed Collection', 1),
(2, 'DEPOSIT', '2024-05-21 20:09:49.016946', 2.00, 95.00, 131.80, 'Funded By Completed Collection', 2),
(3, 'DEPOSIT', '2024-05-31 07:00:00.174967', 3.00, 131.80, 183.78, 'Funded By Completed Collection', 3),
(4, 'DEPOSIT', '2024-05-31 07:07:27.393287', 3.00, 183.78, 220.77, 'Funded By Completed Collection', 4),
(5, 'DEPOSIT', '2024-05-31 07:11:06.485290', 3.00, 220.77, 297.75, 'Funded By Completed Collection', 5),
(6, 'DEPOSIT', '2024-06-03 14:04:51.876091', 3.00, 297.75, 414.71, 'Funded By Completed Collection', 6),
(7, 'DEPOSIT', '2024-06-03 14:27:52.981842', 3.00, 414.71, 571.66, 'Funded By Completed Collection', 7);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-03-22 13:10:20.341861', '1', 'Super Users', 1, '[{\"added\": {}}]', 3, 4),
(2, '2024-03-22 13:10:38.094709', '1', 'SuperGroup', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 3, 4),
(3, '2024-03-22 13:10:48.595610', '1', 'Super Group', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 3, 4);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(7, 'base', 'collection'),
(15, 'base', 'collectorcommission'),
(8, 'base', 'collectorprofile'),
(9, 'base', 'customerprofile'),
(14, 'base', 'ratings'),
(13, 'base', 'requests'),
(17, 'base', 'servicecharge'),
(10, 'base', 'wallet'),
(12, 'base', 'wallethistory'),
(11, 'base', 'waste'),
(16, 'base', 'wastegl'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-02-27 06:50:44.551508'),
(2, 'auth', '0001_initial', '2024-02-27 06:50:45.768226'),
(3, 'admin', '0001_initial', '2024-02-27 06:50:46.010168'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-02-27 06:50:46.019070'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-02-27 06:50:46.027318'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-02-27 06:50:46.178074'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-02-27 06:50:46.279554'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-02-27 06:50:46.332643'),
(9, 'auth', '0004_alter_user_username_opts', '2024-02-27 06:50:46.342579'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-02-27 06:50:46.436641'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-02-27 06:50:46.441102'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-02-27 06:50:46.450884'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-02-27 06:50:46.516204'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-02-27 06:50:46.570480'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-02-27 06:50:46.630097'),
(16, 'auth', '0011_update_proxy_permissions', '2024-02-27 06:50:46.639518'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-02-27 06:50:46.693341'),
(18, 'base', '0001_initial', '2024-02-27 06:50:47.997366'),
(19, 'sessions', '0001_initial', '2024-02-27 06:50:48.100338'),
(20, 'base', '0002_alter_wallet_collector', '2024-02-27 08:11:43.909135'),
(21, 'base', '0002_wastegl_commissioncollector', '2024-03-15 14:11:40.953648'),
(22, 'base', '0003_rename_commissioncollector_collectorcommission', '2024-03-15 14:21:38.445309'),
(23, 'base', '0002_collectorcommission_extras', '2024-03-15 14:57:22.433605'),
(24, 'base', '0002_servicecharge', '2024-05-29 15:23:02.233456');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('3n0788h5h0va80rz4nw7ndhzczmhgbtc', '.eJxVjMsOwiAUBf-FtSGA9CIu3fsNzX2AVA0kpV0Z_12bdKHbMzPnpUZclzKuPc3jJOqsvDr8boT8SHUDcsd6a5pbXeaJ9KbonXZ9bZKel939OyjYy7c-xlP2kNliNoyGvKQhWKForHMsMREgiCCzcQAClrOVMASIBJEF1fsDB0I47g:1sCJ93:wrogXwVw86Z8AS6sqCONObxbPY_UbPDTgqvl5BHXhZw', '2024-06-12 13:15:09.561883'),
('6ltzr294lspqzf3vy6mhkz6u37dh5g9k', '.eJxVjMsOwiAUBf-FtSGA9CIu3fsNzX2AVA0kpV0Z_12bdKHbMzPnpUZclzKuPc3jJOqsvDr8boT8SHUDcsd6a5pbXeaJ9KbonXZ9bZKel939OyjYy7c-xlP2kNliNoyGvKQhWKForHMsMREgiCCzcQAClrOVMASIBJEF1fsDB0I47g:1rnecg:KhPtQQwFCLHnyDNRHZHxtnUdeZb2FssgcE2K7mL7bFY', '2024-04-05 13:07:50.860868'),
('8t14dn1d31uvodgwgppk52itx6pwgbuz', '.eJxVjMsOwiAUBf-FtSGA9CIu3fsNzX2AVA0kpV0Z_12bdKHbMzPnpUZclzKuPc3jJOqsvDr8boT8SHUDcsd6a5pbXeaJ9KbonXZ9bZKel939OyjYy7c-xlP2kNliNoyGvKQhWKForHMsMREgiCCzcQAClrOVMASIBJEF1fsDB0I47g:1rrfgU:2MLFY2uGbtFNS3n4K0cKBuQxhxrOsu1adf6rY4L6fc0', '2024-04-16 15:04:22.127349'),
('ndafkafyzlhco58htkct17x3prgss9vi', '.eJxVjMsOwiAUBf-FtSGA9CIu3fsNzX2AVA0kpV0Z_12bdKHbMzPnpUZclzKuPc3jJOqsvDr8boT8SHUDcsd6a5pbXeaJ9KbonXZ9bZKel939OyjYy7c-xlP2kNliNoyGvKQhWKForHMsMREgiCCzcQAClrOVMASIBJEF1fsDB0I47g:1rwFqZ:qhtWaPEAsZPoTyC7ZvlsMYNsaq83czhIKAulFsSSEhg', '2024-04-29 06:29:43.084929');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `base_collection`
--
ALTER TABLE `base_collection`
  ADD PRIMARY KEY (`collection_id`),
  ADD KEY `base_collection_collector_id_fbfa8dff_fk_base_coll` (`collector_id`),
  ADD KEY `base_collection_request_id_e243d9e8_fk_base_requests_request_id` (`request_id`);

--
-- Indexes for table `base_collectorcommission`
--
ALTER TABLE `base_collectorcommission`
  ADD PRIMARY KEY (`txn_id`),
  ADD UNIQUE KEY `collector_id` (`collector_id`);

--
-- Indexes for table `base_collectorprofile`
--
ALTER TABLE `base_collectorprofile`
  ADD PRIMARY KEY (`collector_id`),
  ADD KEY `base_collectorprofile_waste_id_37207778_fk_base_waste_waste_id` (`waste_id`),
  ADD KEY `base_collectorprofile_auth_id_dd860a91_fk_auth_user_id` (`auth_id`);

--
-- Indexes for table `base_customerprofile`
--
ALTER TABLE `base_customerprofile`
  ADD PRIMARY KEY (`customer_id`),
  ADD KEY `base_customerprofile_auth_id_0ec65cc5_fk_auth_user_id` (`auth_id`);

--
-- Indexes for table `base_ratings`
--
ALTER TABLE `base_ratings`
  ADD PRIMARY KEY (`rating_id`),
  ADD KEY `base_ratings_collection_id_b7157d0e_fk_base_coll` (`collection_id`);

--
-- Indexes for table `base_requests`
--
ALTER TABLE `base_requests`
  ADD PRIMARY KEY (`request_id`),
  ADD KEY `base_requests_customer_id_0623f509_fk_base_cust` (`customer_id`),
  ADD KEY `base_requests_waste_id_5daaacdc_fk_base_waste_waste_id` (`waste_id`);

--
-- Indexes for table `base_servicecharge`
--
ALTER TABLE `base_servicecharge`
  ADD PRIMARY KEY (`service_id`);

--
-- Indexes for table `base_wallet`
--
ALTER TABLE `base_wallet`
  ADD PRIMARY KEY (`wallet_id`),
  ADD UNIQUE KEY `base_wallet_collector_id_ca33e49e_uniq` (`collector_id`);

--
-- Indexes for table `base_wallethistory`
--
ALTER TABLE `base_wallethistory`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `base_wallethistory_wallet_id_fe1174bc_fk_base_wallet_wallet_id` (`wallet_id`);

--
-- Indexes for table `base_waste`
--
ALTER TABLE `base_waste`
  ADD PRIMARY KEY (`waste_id`);

--
-- Indexes for table `base_wastegl`
--
ALTER TABLE `base_wastegl`
  ADD PRIMARY KEY (`gl_id`),
  ADD KEY `base_wastegl_collection_id_401eddeb_fk_base_coll` (`collection_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `base_collection`
--
ALTER TABLE `base_collection`
  MODIFY `collection_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `base_collectorcommission`
--
ALTER TABLE `base_collectorcommission`
  MODIFY `txn_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `base_collectorprofile`
--
ALTER TABLE `base_collectorprofile`
  MODIFY `collector_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `base_customerprofile`
--
ALTER TABLE `base_customerprofile`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `base_ratings`
--
ALTER TABLE `base_ratings`
  MODIFY `rating_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `base_requests`
--
ALTER TABLE `base_requests`
  MODIFY `request_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `base_servicecharge`
--
ALTER TABLE `base_servicecharge`
  MODIFY `service_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `base_wallet`
--
ALTER TABLE `base_wallet`
  MODIFY `wallet_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `base_wallethistory`
--
ALTER TABLE `base_wallethistory`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `base_waste`
--
ALTER TABLE `base_waste`
  MODIFY `waste_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `base_wastegl`
--
ALTER TABLE `base_wastegl`
  MODIFY `gl_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `base_collection`
--
ALTER TABLE `base_collection`
  ADD CONSTRAINT `base_collection_collector_id_fbfa8dff_fk_base_coll` FOREIGN KEY (`collector_id`) REFERENCES `base_collectorprofile` (`collector_id`),
  ADD CONSTRAINT `base_collection_request_id_e243d9e8_fk_base_requests_request_id` FOREIGN KEY (`request_id`) REFERENCES `base_requests` (`request_id`);

--
-- Constraints for table `base_collectorcommission`
--
ALTER TABLE `base_collectorcommission`
  ADD CONSTRAINT `base_commissioncolle_collector_id_0505fecd_fk_base_coll` FOREIGN KEY (`collector_id`) REFERENCES `base_collectorprofile` (`collector_id`);

--
-- Constraints for table `base_collectorprofile`
--
ALTER TABLE `base_collectorprofile`
  ADD CONSTRAINT `base_collectorprofile_auth_id_dd860a91_fk_auth_user_id` FOREIGN KEY (`auth_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `base_collectorprofile_waste_id_37207778_fk_base_waste_waste_id` FOREIGN KEY (`waste_id`) REFERENCES `base_waste` (`waste_id`);

--
-- Constraints for table `base_customerprofile`
--
ALTER TABLE `base_customerprofile`
  ADD CONSTRAINT `base_customerprofile_auth_id_0ec65cc5_fk_auth_user_id` FOREIGN KEY (`auth_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `base_ratings`
--
ALTER TABLE `base_ratings`
  ADD CONSTRAINT `base_ratings_collection_id_b7157d0e_fk_base_coll` FOREIGN KEY (`collection_id`) REFERENCES `base_collection` (`collection_id`);

--
-- Constraints for table `base_requests`
--
ALTER TABLE `base_requests`
  ADD CONSTRAINT `base_requests_customer_id_0623f509_fk_base_cust` FOREIGN KEY (`customer_id`) REFERENCES `base_customerprofile` (`customer_id`),
  ADD CONSTRAINT `base_requests_waste_id_5daaacdc_fk_base_waste_waste_id` FOREIGN KEY (`waste_id`) REFERENCES `base_waste` (`waste_id`);

--
-- Constraints for table `base_wallet`
--
ALTER TABLE `base_wallet`
  ADD CONSTRAINT `base_wallet_collector_id_ca33e49e_fk_base_coll` FOREIGN KEY (`collector_id`) REFERENCES `base_collectorprofile` (`collector_id`);

--
-- Constraints for table `base_wallethistory`
--
ALTER TABLE `base_wallethistory`
  ADD CONSTRAINT `base_wallethistory_wallet_id_fe1174bc_fk_base_wallet_wallet_id` FOREIGN KEY (`wallet_id`) REFERENCES `base_wallet` (`wallet_id`);

--
-- Constraints for table `base_wastegl`
--
ALTER TABLE `base_wastegl`
  ADD CONSTRAINT `base_wastegl_collection_id_401eddeb_fk_base_coll` FOREIGN KEY (`collection_id`) REFERENCES `base_collection` (`collection_id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
