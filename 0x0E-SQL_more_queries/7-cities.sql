-- SQL script to create a database hbtn_0d_usa and the table cities.
-- Creates a database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- uses the created database
USE hbtn_0d_usa;
-- creates a table cities in the database
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id)
        REFERENCES states(id)
);
