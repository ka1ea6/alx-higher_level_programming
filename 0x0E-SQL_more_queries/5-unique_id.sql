-- SQL Script to create a table unique_id
-- creates a table unique id 
CREATE TABLE IF NOT EXISTS unique_id(
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256) 
);