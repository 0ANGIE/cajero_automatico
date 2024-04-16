-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.30 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para cajero_automatico
CREATE DATABASE IF NOT EXISTS `cajero_automatico` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cajero_automatico`;

-- Volcando estructura para tabla cajero_automatico.cuentas
CREATE TABLE IF NOT EXISTS `cuentas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero_cuenta` int NOT NULL,
  `nombre` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `numero_telefono` int NOT NULL,
  `pin` int NOT NULL,
  `saldo` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_cuenta` (`numero_cuenta`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla cajero_automatico.cuentas: ~2 rows (aproximadamente)
INSERT IGNORE INTO `cuentas` (`id`, `numero_cuenta`, `nombre`, `numero_telefono`, `pin`, `saldo`) VALUES
	(1, 12345, 'juan', 6789, 12345, 349800),
	(2, 67890, 'ana', 1234, 67890, 850000);

-- Volcando estructura para tabla cajero_automatico.servicios_publicos
CREATE TABLE IF NOT EXISTS `servicios_publicos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla cajero_automatico.servicios_publicos: ~4 rows (aproximadamente)
INSERT IGNORE INTO `servicios_publicos` (`id`, `nombre`) VALUES
	(1, 'agua'),
	(2, 'luz'),
	(3, 'gas'),
	(4, 'internet');

-- Volcando estructura para tabla cajero_automatico.tipo_cuentas
CREATE TABLE IF NOT EXISTS `tipo_cuentas` (
  `id` int NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla cajero_automatico.tipo_cuentas: ~4 rows (aproximadamente)
INSERT IGNORE INTO `tipo_cuentas` (`id`, `nombre`) VALUES
	(1, 'ahorro'),
	(2, 'corriente'),
	(3, 'nequi'),
	(4, 'bancolombia_mano');

-- Volcando estructura para tabla cajero_automatico.transacciones
CREATE TABLE IF NOT EXISTS `transacciones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cuenta_destino` int NOT NULL,
  `cuenta_id` int NOT NULL,
  `tipo` int NOT NULL,
  `cantidad` int NOT NULL DEFAULT '0',
  `servicio_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `servicios_FK` (`servicio_id`),
  KEY `cuentas_FK` (`cuenta_id`),
  KEY `tipo_cuentas_FK` (`tipo`),
  CONSTRAINT `cuentas_FK` FOREIGN KEY (`cuenta_id`) REFERENCES `cuentas` (`id`),
  CONSTRAINT `servicios_FK` FOREIGN KEY (`servicio_id`) REFERENCES `servicios_publicos` (`id`),
  CONSTRAINT `tipo_cuentas_FK` FOREIGN KEY (`tipo`) REFERENCES `tipo_cuentas` (`id`),
  CONSTRAINT `transacciones_FK` FOREIGN KEY (`cuenta_id`) REFERENCES `cuentas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla cajero_automatico.transacciones: ~0 rows (aproximadamente)

-- Volcando estructura para tabla cajero_automatico.transferencias
CREATE TABLE IF NOT EXISTS `transferencias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cuenta_origen_id` int NOT NULL,
  `cuenta_destino_id` int NOT NULL,
  `cantidad` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cuenta_origen_id` (`cuenta_origen_id`),
  KEY `cuenta_destino_id` (`cuenta_destino_id`),
  CONSTRAINT `transferencias_ibfk_1` FOREIGN KEY (`cuenta_origen_id`) REFERENCES `cuentas` (`id`),
  CONSTRAINT `transferencias_ibfk_2` FOREIGN KEY (`cuenta_destino_id`) REFERENCES `cuentas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla cajero_automatico.transferencias: ~0 rows (aproximadamente)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
