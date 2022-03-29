from email import charset
import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='admin', host='127.0.0.1', port=3306, charset='utf8')

criar_tabelas = '''-- MySQL Script generated by MySQL Workbench
-- Tue Mar 29 13:37:14 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema eng2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema eng2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `eng2` DEFAULT CHARACTER SET utf8 ;
USE `eng2` ;

-- -----------------------------------------------------
-- Table `eng2`.`TAREFA`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eng2`.`TAREFA` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `NOME` VARCHAR(45) NOT NULL,
  `DESCRICAO` VARCHAR(90) NULL,
  `TIPO` VARCHAR(45) NOT NULL,
  `STATUS` VARCHAR(30) NULL,
  `PRIORIDADE` VARCHAR(15) NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `eng2`.`USUARIO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eng2`.`USUARIO` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `USERNAME` VARCHAR(45) NOT NULL,
  `EMAIL` VARCHAR(45) NOT NULL,
  `SENHA` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
'''

conn.commit()