-- SQL script that lists all the cities of California found in the db hbtn_0d_usa
SELECT id, name FROM cities
    WHERE cities.state_id = 
        (SELECT id FROM states 
        WHERE name = "California");