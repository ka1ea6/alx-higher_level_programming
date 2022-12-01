-- SQL script to ilst all genres of the show Dexter
-- using sub queries
SELECt tv_genres.name AS name
    FROM tv_show_genres
    LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
    LEFT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = "DEXTER"
    ORDER BY tv_genres.name;
