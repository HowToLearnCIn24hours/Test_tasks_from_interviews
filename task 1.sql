/*There is a table City_Population with a population of cities: CITY (city name), Population (population).
Write an SQL query that displays a city with a minimum population.*/
SELECT city, population 
FROM city_population
WHERE population = (
SELECT MIN(population)
FROM city_population);