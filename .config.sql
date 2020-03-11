CREATE DATABASE sensordb;
USE sensordb;
CREATE TABLE readings(id int NOT NULL AUTO_INCREMENT, temperature float, time float,PRIMARY KEY(id));
CREATE USER 'user_sensor'@'localhost' IDENTIFIED BY 'pass_sensor';
GRANT ALL PRIVILEGES ON sensordb.* TO 'user_sensor'@'localhost';
