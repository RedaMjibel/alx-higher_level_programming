-- 8-cities_of_california_subquery.sql
-- lists all the cities of California

SELECT id, name
FROM cities
WHERE cities.state_id = (SELECT s.id FROM states s WHERE s.name = 'California');
