-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for biztrack
DROP DATABASE IF EXISTS `biztrack`;
CREATE DATABASE IF NOT EXISTS `biztrack` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `biztrack`;

-- Dumping structure for table biztrack.products
DROP TABLE IF EXISTS `products`;
CREATE TABLE IF NOT EXISTS `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table biztrack.products: ~1 rows (approximately)
INSERT INTO `products` (`id`, `name`, `price`, `quantity`) VALUES
	(1, 'Laptop', 1000.00, 40),
	(2, 'Smartphone', 700.50, 100),
	(3, 'Tablet', 400.75, 75),
	(4, 'Smartwatch', 200.20, 150),
	(5, 'Wireless Earbuds', 130.30, 200),
	(6, 'Gaming Console', 500.40, 30),
	(7, '4K Monitor', 300.60, 40),
	(8, 'Mechanical Keyboard', 90.10, 120),
	(9, 'Gaming Mouse', 60.25, 180),
	(10, 'External Hard Drive', 80.35, 90),
	(11, 'USB-C Hub', 50.45, 110),
	(12, 'Bluetooth Speaker', 100.55, 140),
	(13, 'VR Headset', 400.65, 25),
	(14, 'Drone', 500.75, 20),
	(15, 'Smart Home Hub', 150.85, 60),
	(16, 'Action Camera', 300.95, 35),
	(17, 'Wireless Charger', 40.05, 130),
	(18, 'Portable SSD', 130.15, 80),
	(19, 'Smart Light Bulb', 20.25, 250),
	(20, 'Fitness Tracker', 80.35, 170),
	(21, 'E-Reader', 130.45, 60),
	(22, 'Noise Cancelling Headphones', 200.55, 70),
	(23, 'Smart Thermostat', 250.65, 40),
	(24, 'Robot Vacuum', 300.75, 30),
	(25, 'Streaming Device', 50.85, 150),
	(26, 'Smart Doorbell', 200.95, 50),
	(27, 'Wi-Fi Router', 130.05, 90),
	(28, '3D Printer', 500.15, 15),
	(29, 'Graphics Tablet', 200.25, 25),
	(30, 'Smart Lock', 150.35, 60),
	(31, 'Electric Scooter', 400.45, 20),
	(32, 'Portable Projector', 300.55, 30),
	(33, 'Gaming Chair', 200.65, 40),
	(34, 'Smart Glasses', 300.75, 10),
	(35, 'Digital Photo Frame', 100.85, 80),
	(36, 'Smart Scale', 50.95, 100),
	(37, 'Smart Plug', 30.05, 200),
	(38, 'Security Camera', 100.15, 70),
	(39, 'Smart Mirror', 400.25, 15),
	(40, 'Smart Refrigerator', 2000.35, 5),
	(41, 'Electric Toothbrush', 50.45, 150),
	(42, 'Smart Coffee Maker', 150.55, 40),
	(43, 'Smart Oven', 500.65, 10),
	(44, 'Smart Washing Machine', 1000.75, 8),
	(45, 'Smart Air Purifier', 200.85, 30),
	(46, 'Smart Water Bottle', 50.95, 120),
	(47, 'Smart Backpack', 100.05, 50),
	(48, 'Smart Ring', 200.15, 20),
	(49, 'Smart Bike', 1000.25, 10),
	(50, 'Smart Speaker', 150.35, 100);

-- Dumping structure for table biztrack.sales
DROP TABLE IF EXISTS `sales`;
CREATE TABLE IF NOT EXISTS `sales` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(255) NOT NULL,
  `quantity` int DEFAULT NULL,
  `total_price` decimal(10,2) DEFAULT NULL,
  `sales_date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table biztrack.sales: ~1 rows (approximately)
INSERT INTO `sales` (`id`, `product_name`, `quantity`, `total_price`, `sales_date`) VALUES
	(1, 'Laptop', 1, 1000.00, '2023-01-01'),
	(2, 'Smartphone', 2, 1401.00, '2023-01-02'),
	(3, 'Tablet', 1, 400.75, '2023-01-03'),
	(4, 'Smartwatch', 3, 600.60, '2023-01-04'),
	(5, 'Wireless Earbuds', 2, 260.60, '2023-01-05'),
	(6, 'Gaming Console', 1, 500.40, '2023-01-06'),
	(7, '4K Monitor', 1, 300.60, '2023-01-07'),
	(8, 'Mechanical Keyboard', 2, 180.20, '2023-01-08'),
	(9, 'Gaming Mouse', 3, 180.75, '2023-01-09'),
	(10, 'External Hard Drive', 1, 80.35, '2023-01-10'),
	(11, 'Laptop', 1, 1000.00, '2023-01-11'),
	(12, 'Smartphone', 2, 1401.00, '2023-01-12'),
	(13, 'Tablet', 1, 400.75, '2023-01-13'),
	(14, 'Smartwatch', 3, 600.60, '2023-01-14'),
	(15, 'Wireless Earbuds', 2, 260.60, '2023-01-15'),
	(16, 'Gaming Console', 1, 500.40, '2023-01-16'),
	(17, '4K Monitor', 1, 300.60, '2023-01-17'),
	(18, 'Mechanical Keyboard', 2, 180.20, '2023-01-18'),
	(19, 'Gaming Mouse', 3, 180.75, '2023-01-19'),
	(20, 'External Hard Drive', 1, 80.35, '2023-01-20'),
	(21, 'Laptop', 1, 1000.00, '2023-01-21'),
	(22, 'Smartphone', 2, 1401.00, '2023-01-22'),
	(23, 'Tablet', 1, 400.75, '2023-01-23'),
	(24, 'Smartwatch', 3, 600.60, '2023-01-24'),
	(25, 'Wireless Earbuds', 2, 260.60, '2023-01-25'),
	(26, 'Gaming Console', 1, 500.40, '2023-01-26'),
	(27, '4K Monitor', 1, 300.60, '2023-01-27'),
	(28, 'Mechanical Keyboard', 2, 180.20, '2023-01-28'),
	(29, 'Gaming Mouse', 3, 180.75, '2023-01-29'),
	(30, 'External Hard Drive', 1, 80.35, '2023-01-30'),
	(51, 'Laptop', 25, 25000.00, '2024-09-19');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
