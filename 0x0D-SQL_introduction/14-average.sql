-- SQL script to compute the average score of all records in the table second_table
SELECT SUM(`score`)/COUNT(*) AS `average` FROM  `second_table`;