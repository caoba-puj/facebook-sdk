-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema parametrization
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `parametrization` ;

-- -----------------------------------------------------
-- Schema parametrization
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `parametrization` DEFAULT CHARACTER SET utf8 ;
USE `parametrization` ;

-- -----------------------------------------------------
-- Table `parametrization`.`Credential`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `parametrization`.`Credential` (
  `idCredential` INT NOT NULL AUTO_INCREMENT,
  `consumerKey` VARCHAR(45) NOT NULL,
  `consumerSecret` VARCHAR(45) NOT NULL,
  `accessToken` VARCHAR(45) NOT NULL,
  `accessTokenSecret` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCredential`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parametrization`.`WhoToFollow`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `parametrization`.`WhoToFollow` (
  `idWhoToFollow` INT NOT NULL AUTO_INCREMENT,
  `twiterAccount` VARCHAR(45) NOT NULL,
  `brand` VARCHAR(45) NULL,
  `brandAttributes` VARCHAR(1000) NULL,
  PRIMARY KEY (`idWhoToFollow`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parametrization`.`keyword`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `parametrization`.`keyword` (
  `idkeyword` INT NOT NULL AUTO_INCREMENT,
  `keyword` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idkeyword`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parametrization`.`Hashtag`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `parametrization`.`Hashtag` (
  `idHashtag` INT NOT NULL AUTO_INCREMENT,
  `hashtag` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idHashtag`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parametrization`.`Process`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `parametrization`.`Process` (
  `idProcess` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `outputDirectory` VARCHAR(45) NOT NULL,
  `streamType` VARCHAR(45) NOT NULL,
  `logFile` VARCHAR(45) NOT NULL,
  `streamFilename` VARCHAR(45) NOT NULL,
  `start` DATETIME NOT NULL,
  `end` DATETIME NOT NULL,
  `processType` VARCHAR(45) CHARACTER SET 'dec8' NOT NULL DEFAULT 'Stream, Rest',
  `inputDirRest` VARCHAR(45) NULL,
  `regexRest` VARCHAR(45) NULL,
  `idProcessStream` INT NULL,
  PRIMARY KEY (`idProcess`),
  INDEX `fk_Process_Process1_idx` (`idProcessStream` ASC),
  CONSTRAINT `fk_Process_Process1`
    FOREIGN KEY (`idProcessStream`)
    REFERENCES `parametrization`.`Process` (`idProcess`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parametrization`.`Coordinates`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `parametrization`.`Coordinates` (
  `idCoordinate` INT NOT NULL AUTO_INCREMENT,
  `coordinates` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCoordinate`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parametrization`.`Process_has_WhoToFollow`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `parametrization`.`Process_has_WhoToFollow` (
  `Process_idProcess` INT NOT NULL,
  `WhoToFollow_idWhoToFollow` INT NOT NULL,
  PRIMARY KEY (`Process_idProcess`, `WhoToFollow_idWhoToFollow`),
  INDEX `fk_Process_has_WhoToFollow_WhoToFollow1_idx` (`WhoToFollow_idWhoToFollow` ASC),
  INDEX `fk_Process_has_WhoToFollow_Process1_idx` (`Process_idProcess` ASC),
  CONSTRAINT `fk_Process_has_WhoToFollow_Process1`
    FOREIGN KEY (`Process_idProcess`)
    REFERENCES `parametrization`.`Process` (`idProcess`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Process_has_WhoToFollow_WhoToFollow1`
    FOREIGN KEY (`WhoToFollow_idWhoToFollow`)
    REFERENCES `parametrization`.`WhoToFollow` (`idWhoToFollow`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parametrization`.`Process_has_keyword`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `parametrization`.`Process_has_keyword` (
  `Process_idProcess` INT NOT NULL,
  `keyword_idkeyword` INT NOT NULL,
  PRIMARY KEY (`Process_idProcess`, `keyword_idkeyword`),
  INDEX `fk_Process_has_keyword_keyword1_idx` (`keyword_idkeyword` ASC),
  INDEX `fk_Process_has_keyword_Process1_idx` (`Process_idProcess` ASC),
  CONSTRAINT `fk_Process_has_keyword_Process1`
    FOREIGN KEY (`Process_idProcess`)
    REFERENCES `parametrization`.`Process` (`idProcess`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Process_has_keyword_keyword1`
    FOREIGN KEY (`keyword_idkeyword`)
    REFERENCES `parametrization`.`keyword` (`idkeyword`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parametrization`.`Process_has_Coordinate`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `parametrization`.`Process_has_Coordinate` (
  `Process_idProcess` INT NOT NULL,
  `Coordinate_idCoordinate` INT NOT NULL,
  PRIMARY KEY (`Process_idProcess`, `Coordinate_idCoordinate`),
  INDEX `fk_Process_has_Coordinate_Coordinate1_idx` (`Coordinate_idCoordinate` ASC),
  INDEX `fk_Process_has_Coordinate_Process1_idx` (`Process_idProcess` ASC),
  CONSTRAINT `fk_Process_has_Coordinate_Process1`
    FOREIGN KEY (`Process_idProcess`)
    REFERENCES `parametrization`.`Process` (`idProcess`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Process_has_Coordinate_Coordinate1`
    FOREIGN KEY (`Coordinate_idCoordinate`)
    REFERENCES `parametrization`.`Coordinates` (`idCoordinate`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parametrization`.`Process_has_Hashtag`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `parametrization`.`Process_has_Hashtag` (
  `Process_idProcess` INT NOT NULL,
  `Hashtag_idHashtag` INT NOT NULL,
  PRIMARY KEY (`Process_idProcess`, `Hashtag_idHashtag`),
  INDEX `fk_Process_has_Hashtag_Hashtag1_idx` (`Hashtag_idHashtag` ASC),
  INDEX `fk_Process_has_Hashtag_Process1_idx` (`Process_idProcess` ASC),
  CONSTRAINT `fk_Process_has_Hashtag_Process1`
    FOREIGN KEY (`Process_idProcess`)
    REFERENCES `parametrization`.`Process` (`idProcess`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Process_has_Hashtag_Hashtag1`
    FOREIGN KEY (`Hashtag_idHashtag`)
    REFERENCES `parametrization`.`Hashtag` (`idHashtag`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parametrization`.`Process_has_Credential`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `parametrization`.`Process_has_Credential` (
  `Process_idProcess` INT NOT NULL,
  `Credential_idCredential` INT NOT NULL,
  PRIMARY KEY (`Process_idProcess`, `Credential_idCredential`),
  INDEX `fk_Process_has_Credential_Credential1_idx` (`Credential_idCredential` ASC),
  INDEX `fk_Process_has_Credential_Process1_idx` (`Process_idProcess` ASC),
  CONSTRAINT `fk_Process_has_Credential_Process1`
    FOREIGN KEY (`Process_idProcess`)
    REFERENCES `parametrization`.`Process` (`idProcess`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Process_has_Credential_Credential1`
    FOREIGN KEY (`Credential_idCredential`)
    REFERENCES `parametrization`.`Credential` (`idCredential`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
