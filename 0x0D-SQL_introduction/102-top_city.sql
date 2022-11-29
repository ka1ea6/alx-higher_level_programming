-- SQL script to display the the 3 cities with the highest temperature in the months
-- July and August
SELECT `city`, SUM(`value`)/COUNT(*) AS `avg_temp`
    FROM `temperatures`
    WHERE `month`=7 OR `month`=8
    GROUP BY `city`
    ORDER BY `avg_temp` 
    desc LIMIT 3;