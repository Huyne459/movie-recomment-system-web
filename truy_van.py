import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
    database = "movielens"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM genres")
category = []
for x in mycursor:
    str = ''.join(x)
    category.append(str)

# print(category)

# Tìm phim theo từ khóa tên
def find_movide_by_name(name):
    text = "SELECT * FROM movies WHERE movies.title LIKE '%" + name + "%'"
    mycursor.execute(text)

    result = []
    for x in mycursor:
        result.append(x)
        print(x)

    return result



# Tìm phim theo thể loại
def find_film_by_category(category_name):
    if category_name in category:
        text = "SELECT movies.title FROM movies, genres_movies, genres WHERE  genres_movies.genre_id = (SELECT genres.id FROM genres WHERE genres.name = '" + category_name +"') AND genres_movies.movie_id = movies.id ;"
        mycursor.execute(text)
        result = []
        for x in mycursor:
            str = ''.join(x)
            if result == []:
                result.append(str)
            else:
                if str != result[-1]:
                    result.append(str)

        print(len(result))
    else:
        print(0)


# Săp xếp theo ngày
def sort_movies_by_day(status):
    # Mới -> cũ
    if status == "newer":
        text = "SELECT title FROM movies ORDER BY movies.release_date DESC;"
        mycursor.execute(text)
        result = []
        for x in mycursor:
            str = ''.join(x)
            result.append(str)
    # Cũ -> mới
    else:
        text = "SELECT * FROM movies ORDER BY movies.release_date ASC;"
        mycursor.execute(text)
        result = []
        for x in mycursor:
            str = ''.join(x)
            result.append(str)

    print(result)
    # return result


# Sắp xếp theo rating TB
def sort_movie_by_rating(status="decrease"):
    # Cao -> Thap
    if status == "decrease":
        text = "SELECT * FROM ( SELECT title, AVG(rating) AS avgRating FROM movies INNER JOIN ratings ON ratings.movie_id = movies.id GROUP BY title ) AS ratings ORDER BY avgRating DESC"
        mycursor.execute(text)
        result = []
        for x in mycursor:
            # str1 = ''.join(x)
            result.append(x)
            # print(x)
    # Thap -> cao
    else:
        text = "SELECT * FROM ( SELECT title, AVG(rating) AS avgRating FROM movies INNER JOIN ratings ON ratings.movie_id = movies.id GROUP BY title ) AS ratings ORDER BY avgRating ASC"
        mycursor.execute(text)
        result = []
        for x in mycursor:
            # str1 = ''.join(x)
            result.append(x)
            # print(x)

    print(result)
    # print(type(result[0]))
    # return result

def show_databases():
    mycursor.execute("select * from users")

    for x in mycursor:
      print(x)

