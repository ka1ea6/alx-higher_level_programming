-- SQL script to list all records of the table second_table of hbtn_0c_0 database
SELECT score, name FROM second_table WHERE name != "" ORDER BY score DESC,  name DESC;