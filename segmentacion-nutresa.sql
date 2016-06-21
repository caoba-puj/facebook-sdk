CREATE DATABASE `segmentacion-nutresa` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci */;

CREATE TABLE `marca` (
  `idmarca` int(11) NOT NULL AUTO_INCREMENT,
  `marca` varchar(45) CHARACTER SET utf8 DEFAULT NULL,
  `atributos` varchar(1000) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`idmarca`)
) ENGINE=InnoDB AUTO_INCREMENT=341 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;


SELECT * FROM `segmentacion-nutresa`.marca order by marca;
