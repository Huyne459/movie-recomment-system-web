from truy_van import *
import pickle

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
# from tensorflow.keras import layers

from keras.models import load_model


model = keras.models.load_model('/home/huy/Desktop/BTL_Phenikaa/Big_data/recomment-system/03-20220428T074146Z-001/03/recomment_model')

with open('user2user_encoded.pkl', 'rb') as f:
    user2user_encoded = pickle.load(f)

with open('movie2movie_encoded.pkl', 'rb') as f:
    movie2movie_encoded = pickle.load(f)

with open('movie_encoded2movie.pkl', 'rb') as f:
    movie_encoded2movie = pickle.load(f)


allMovies = all_movies()
movies_watched_by_user = find_movies_watched_by_userId('001')

user_id = 1
user_encoder = user2user_encoded.get(user_id)

movies_not_watched = allMovies[
    ~allMovies["movieId"].isin(movies_watched_by_user.movieId.values)
]["movieId"]
movies_not_watched = [[movie2movie_encoded.get(x)] for x in movies_not_watched]

user_movie_array = np.hstack(
    ([[user_encoder]] * len(movies_not_watched), movies_not_watched))

ratings = model.predict(user_movie_array).flatten()
top_ratings_indices = ratings.argsort()[-5:][::-1]
recommended_movie_ids = [
    movie_encoded2movie.get(movies_not_watched[x][0]) for x in top_ratings_indices
]

print("Showing recommendations for user: {}".format(user_id))
print("====" * 9)
# Top 5 movie vote by user
print("Movies with high ratings from user")
print("----" * 8)

top_movies_user = (
    movies_watched_by_user.sort_values(by="rating", ascending=False)
    .head(5)
    .movieId.values
)
movie_df_rows = allMovies[allMovies["movieId"].isin(top_movies_user)]
for row in movie_df_rows.itertuples():
    print(row.title)

print("----" * 8)
print("Top 5 movie recommendations")
print("----" * 8)
for id in recommended_movie_ids:
    find_movie_in4_by_movieId(id)
    # print(a)