
CREATE OR REPLACE VIEW RevenuePerDirector AS
SELECT s.name, CONCAT("$",sum(COALESCE(revenue,0)),"M") as revenue from Movies m 
	inner join Roles r on r.id_movies = m.id
	inner join Stars s on r.id_roles = s.id  and r.sebagai  = 'Director'
GROUP BY s.name;


SELECT * from RevenuePerDirector;
