-- SQL script to list all genres in the db hbtn_0d_tvshows_rate by rating
SELECT name, SUM(tv_show_ratings.rate) AS rating
    FROM tv_genres
    INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
    INNER JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
    GROUP BY name
    ORDER BY rating DESC;
