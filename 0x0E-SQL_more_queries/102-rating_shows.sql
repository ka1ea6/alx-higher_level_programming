-- SQL script that lists all shows by their rating
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
    FROM tv_shows
    LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
    GROUP BY tv_show_ratings.show_id
    ORDER BY rating DESC;