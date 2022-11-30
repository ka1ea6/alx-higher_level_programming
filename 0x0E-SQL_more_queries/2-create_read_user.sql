-- SQL script to create a database hbtn_0d_2 and the ser user_0d_2
-- creates a database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates a user if it doesn't exist
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- grants permission to user user_0d_2
GRANT SELECT ON 'hbtn_0d_2'.* TO user_0d_2@localhost;