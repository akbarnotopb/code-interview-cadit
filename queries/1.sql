CREATE OR REPLACE VIEW NumberOfUniqueTitles AS
SELECT COUNT(DISTINCT name) as no_of_unique_titles  from Movies;

select * from NumberOfUniqueTitles;
