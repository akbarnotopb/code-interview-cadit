# Answers
1. Techdoc of CDM, Logical Model, & PDM are on `techdoc` folder
2. Database schema is on `DDL/mysql-schema-only.sql`
3. Pipeline is on `pipeline.py` or `pipeline.ipynb`
4. Queries are on `queries` folder


# Important Notes
## Assumption
1. Genre is not static, new Genre could be added along new Movies Title
2. So do with director & stars

*Therefore, we check if to be added movie has new genre(s) / star(s) or not before inserting to database.*


## Techstack
- Database : MySQL 5.7, should be compatible with Version 8.*
- Language : Python, MySQL
### Library
Already stated on `requirements.txt`


# How to Run
1. `pip install -r requirements.txt`
2. Init `.env`
3. `python pipeline.py`

## PS 
- Running `python pipeline.py` will seed the database by inserting movies, genre, actor dynamically. This may take a while since we check if the movie has new genre/star/director or not on each row.
- Run `DDL/dump.sql` to create the schema and its data
- Call `insertMovie` to insert new movie