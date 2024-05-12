
CREATE OR REPLACE VIEW FiveLargestRevenueOnCodemyTitles AS 
SELECT m.name, release_detail, rating , CONCAT("$",sum(COALESCE(revenue,0)),"M") as revenue
from Movies m 
	inner join MoviesGenre mg on mg.id_movies = m.id 
	inner join Genre g on mg.id_genre = g.id 
WHERE g.name = 'Comedy'
GROUP BY 1,2,3
ORDER BY sum(COALESCE(revenue,0)) DESC
LIMIT 5;


SELECT * from FiveLargestRevenueOnCodemyTitles;

