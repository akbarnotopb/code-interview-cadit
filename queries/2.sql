
CREATE OR REPLACE VIEW MovieStarringLenaHeadey AS 
select m.name, release_detail 
from Movies m
	inner join Roles r on m.id = r.id_movies 
	inner join Stars s on s.id = r.id_roles AND r.sebagai = 'Star'
WHERE s.name = 'Lena Headey'
ORDER BY release_detail ;

select * from MovieStarringLenaHeadey;

