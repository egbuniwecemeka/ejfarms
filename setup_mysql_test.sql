-- MySQL script that pepares my projects server
-- Creates a database, then a user and grants necessary permissions

CREATE DATABASE IF NOT EXISTS `ejfarms_test_db`;
USE `ejfarms_test_db`;
-- Create the user if it doesn't exist and set it's password
CREATE USER IF NOT EXISTS 'ej_test'@'localhost' IDENTIFIED BY '$Fake_dev_password123';
-- Grant all privileges on hbnb_dev_db to hbnb_dev
-- 'WITH GRANRT OPTION' allows user to grant any inherited permission to other users
GRANT ALL PRIVILEGES ON ejfarms_test_db.* TO 'ej_test'@'localhost';
-- Grant SELECT privileges on performance_schema to hbnb_user
GRANT SELECT ON performance_schema.* TO 'ej_test'@'localhost';
-- Apply changes
FLUSH PRIVILEGES;