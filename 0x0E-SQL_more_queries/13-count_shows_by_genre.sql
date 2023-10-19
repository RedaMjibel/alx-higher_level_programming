-- 13-count_shows_by_genre.sql
-- Lists genres and the number of shows linked to each

SELECT tg.name AS genre, COUNT(tsg.show_id) AS number_of_shows
FROM tv_genres tg
LEFT JOIN tv_showgenres tsg ON tg.id = tsg.genre_id
GROUP BY tg.name
HAVING COUNT(tsg.show_id) > 0
ORDER BY number_of_shows DESC;

