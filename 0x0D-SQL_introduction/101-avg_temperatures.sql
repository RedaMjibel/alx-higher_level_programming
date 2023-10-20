-- 101-avg_temperatures.sql
-- displays the average temperature

SELECT city, ROUND(AVG(value), 2) AS average_temperature_fahrenheit
FROM temperatures
GROUP BY city
ORDER BY average_temperature_fahrenheit DESC;
