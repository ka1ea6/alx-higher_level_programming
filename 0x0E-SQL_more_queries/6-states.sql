-- SQL script to create a database hbtn_0d_usa and a table states
-- create a database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- creates a table states with the specified constraints
CREATE TABLE IF NOT EXISTS states(
    id INT UNIQUE NOT NULL AUTO GENERATED PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);