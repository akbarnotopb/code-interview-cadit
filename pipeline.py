import mysql.connector, pandas as pd
from dotenv import dotenv_values


print("""
Assumption
1. Genre is not static, new Genre could be added along new Movies Title
2. So do with director & stars.

Notes:
If new movies is added, then just call insertMovie on that new DataFrame   
""")

CONFIG = dotenv_values(".env") 

if not CONFIG.keys():
    raise Exception(".env is not set yet!")

def selectIfNotExistThenInsert(cursor, table, data):
    cursor.execute(f"SELECT id FROM {table} WHERE name = %s", (data,))
    result = cursor.fetchone()

    if result:
        return result[0]
    else:
        cursor.execute(f"INSERT INTO {table}(name) VALUES (%s)", (data,))
        return cursor.lastrowid


def extractGenres(genre) -> list:
    return genre.strip().replace("\n","").replace(" ","").split(",") if not pd.isna(genre) else []


def extractRevenue(revenue) -> float:
    if pd.isna(revenue): 
        return None
    else:
        return revenue.replace("$","").replace("M","")

def extractPlot(plot) -> str:
    plot =  plot.replace("\n","").replace("Add a Plot","").strip()
    return plot if plot != "" else None


def extractStars(stars) -> dict:
    res = {
        "Director": [],
        "Stars": []
    }

    def _extract(val , key):
        val = val.replace(f"{key}:","").replace(f"{key}:","")
        return [x.strip() for x in val.split(",")]

    parts = stars.replace("\n","").split("|")

    for _ in parts:
        if "Director" in _ or "Directors" in _:
            res['Director'] = _extract(_, "Director")

        elif "Stars" in _ or "Stars" in _:
            res['Stars'] = _extract(_, "Stars")

    return res

def sanitize(data):
    return None if pd.isna(data) else data


def insertMovieDetail(data, cursor, connection):
    genres = [selectIfNotExistThenInsert(cursor,'Genre',_) for _ in data['genre']]
    sqls = []
    directors = [selectIfNotExistThenInsert(cursor,'Stars',_) for _ in data['stars']['Director']]

    stars = [selectIfNotExistThenInsert(cursor,'Stars',_) for _ in data['stars']['Stars']]

    sql = f"""INSERT INTO Movies(name, plot, rating, duration, votes, release_detail, revenue) VALUES (%s, %s, %s, %s,%s, %s ,%s)"""
    cursor.execute(sql, (data['name'], data['plot'], data['rating'],data['duration'],data['votes'],data['year'],data['revenue']))
    id_movies = cursor.lastrowid

    if genres:
        moviesgenre = [ (id_movies, _) for _ in genres]
        sql = f"INSERT INTO MoviesGenre(id_movies, id_genre) VALUES {','.join([repr(_) for _ in moviesgenre])}"
        sqls.append(sql)
        cursor.execute(sql)

    if directors:
        moviedirectors = [(id_movies, _, 'Director') for _ in directors]
        sql = f"INSERT INTO Roles(id_movies, id_roles, sebagai) VALUES {','.join([repr(_) for _ in moviedirectors])}"
        sqls.append(sql)
        cursor.execute(sql)

    if stars:
        moviestars = [(id_movies, _, 'Star') for _ in stars]
        sql = f"INSERT INTO Roles(id_movies, id_roles, sebagai) VALUES { ','.join([repr(_) for _ in moviestars])}"
        sqls.append(sql)
        cursor.execute(sql)

    return sqls

    # 1. Genre is not static, new Genre could be added along new Movies Title
# 2. So do with director & stars.

# Notes:
# If new movies is added, then just call insertMove on that new DataFrame
def insertMovie(data:dict):
    detail = {
            "name": sanitize(data.MOVIES).strip(),
            "genre":extractGenres(data.GENRE),
            "year" : sanitize(data.YEAR),
            "rating": float(sanitize(data.RATING)) if sanitize(data.RATING) else None,
            "plot": extractPlot(data.PLOT),
            "stars" : extractStars(data.STARS),
            "votes" : int(sanitize(data.VOTES)) if sanitize(data.VOTES) else None,
            "duration" : float(sanitize(data.RunTime)) if sanitize(data.RunTime) else None,
            "revenue": extractRevenue(data.Gross),
        }
    insertMovieDetail(detail, cursor, mydb)

if __name__ == "__main__":
    mydb = mysql.connector.connect(
    host=CONFIG['HOST'],
    user=CONFIG['USER'],
    password=CONFIG['PASSWORD'],
    database=CONFIG['DATABASE'],
    port=CONFIG['PORT']
    )

    df = pd.read_csv("movies.csv")
    df.rename(columns={"ONE-LINE":"PLOT"},inplace=True)
    df['VOTES'] = df['VOTES'].replace(",","", regex=True)

    cursor = mydb.cursor()
    mydb.start_transaction() 

    for _, data in df.iterrows():
        try:
            detail = {
                "name": sanitize(data.MOVIES).strip(),
                "genre":extractGenres(data.GENRE),
                "year" : sanitize(data.YEAR),
                "rating": float(sanitize(data.RATING)) if sanitize(data.RATING) else None,
                "plot": extractPlot(data.PLOT),
                "stars" : extractStars(data.STARS),
                "votes" : int(sanitize(data.VOTES)) if sanitize(data.VOTES) else None,
                "duration" : float(sanitize(data.RunTime)) if sanitize(data.RunTime) else None,
                "revenue": extractRevenue(data.Gross),
            }
            sqls = insertMovieDetail(detail, cursor, mydb)
            mydb.commit()
        except Exception as e:
            mydb.rollback()
            print(sqls)
            print(data)
            print(detail)
            print(e)
            break

