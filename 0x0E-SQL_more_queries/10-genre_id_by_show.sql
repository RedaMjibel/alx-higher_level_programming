-- 10-genre_id_by_show.sql
-- Lists shows with at least one linked genre

SELECT DISTINCT ts.title, tsg.genre_id
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg ON ts.id = tsg.show_id
WHERE tsg.genre_id IS NOT NULL
ORDER BY ts.title ASC, tsg.genre_id ASC;
