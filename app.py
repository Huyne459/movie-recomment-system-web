from flask import Flask, redirect, url_for

from truy_van import find_movide_by_name, show_databases, find_film_by_category, sort_movies_by_day, sort_movie_by_rating

# find_film_by_category("Action")
# sort_movies_by_day("newer")
sort_movie_by_rating()

# app = Flask(__name__)
#
#
# @app.route("/")
# def home_page():
#     show_databases()
#     # query = find_movide_by_name()
#     # return query
#
#
# if __name__ == "__main__":
#     app.run(debug=True)