
CREATE OR REPLACE VIEW MoviesFeaturingDeNiroAndScorsese AS
SELECT m.name, release_detail, rating 
FROM Movies m 
	inner join Roles r on r.id_movies = m.id AND r.sebagai = 'Star'
	inner join Stars s on r.id_roles = s.id 
	inner join Roles r2 on r2.id_movies  = m.id AND r2.sebagai = 'Director' 
	inner join Stars s2 on r2.id_roles = s2.id 
WHERE s.name = 'Robert De Niro' AND s2.name = 'Martin Scorsese';

SELECT * FROM MoviesFeaturingDeNiroAndScorsese;

