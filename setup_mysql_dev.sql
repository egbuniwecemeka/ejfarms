-- MySQL script that pepares my projects server
-- Creates a database, then a user and grants necessary permissions

CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
USE `hbnb_dev_db`;
-- Create the user if it doesn't exist and set it's password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON 'hbnb_dev_db'.* TO 'hbnb_dev'@'localhost';
-- Grant SELECT privileges on performance_schema to hbnb_user
GRANT SELECT ON 'performance_schema'.* TO 'hbnb_dev'@'localhost';
-- Apply changes
FLUSH PRIVILEGES;