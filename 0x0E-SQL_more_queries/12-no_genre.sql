-- 12-no_genre.sql
-- lists all shows contained in the database

SELECT ts.title, tsg.genre_id
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg ON ts.id = tsg.show_id
WHERE tsg.genre_id IS NULL
ORDER BY ts.title ASC, tsg.genre_id ASC;
