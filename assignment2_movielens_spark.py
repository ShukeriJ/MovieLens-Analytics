from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window

# ============================================================
# STQD6324 Data Management - Assignment 2
# MovieLens 100K Analytics using Apache Spark and Cassandra
# Author: Shukeri
# ============================================================

spark = SparkSession.builder \
    .appName("MovieLens Spark Cassandra Assignment") \
    .getOrCreate()

# ============================================================
# 1. Load MovieLens files from HDFS
# ============================================================
ratings_rdd = spark.sparkContext.textFile("hdfs:///user/maria_dev/ml-100k/u.data")
movies_rdd = spark.sparkContext.textFile("hdfs:///user/maria_dev/ml-100k/u.item")
users_rdd = spark.sparkContext.textFile("hdfs:///user/maria_dev/ml-100k/u.user")

print("Ratings:", ratings_rdd.count())
print("Movies:", movies_rdd.count())
print("Users:", users_rdd.count())

# ============================================================
# 2. Convert RDDs into DataFrames
# ============================================================
ratings_df = ratings_rdd.map(lambda x: x.split("\t")).toDF(
    ["user_id", "movie_id", "rating", "timestamp"]
)

users_df = users_rdd.map(lambda x: x.split("|")).toDF(
    ["user_id", "age", "gender", "occupation", "zip_code"]
)

movies_df = movies_rdd.map(lambda x: x.split("|")) \
    .map(lambda x: (x[0], x[1])) \
    .toDF(["movie_id", "movie_title"])

# ============================================================
# 3. Data cleaning and type conversion
# ============================================================
ratings_df = ratings_df \
    .withColumn("user_id", col("user_id").cast("int")) \
    .withColumn("movie_id", col("movie_id").cast("int")) \
    .withColumn("rating", col("rating").cast("int")) \
    .withColumn("timestamp", col("timestamp").cast("long"))

users_df = users_df \
    .withColumn("user_id", col("user_id").cast("int")) \
    .withColumn("age", col("age").cast("int"))

movies_df = movies_df.withColumn("movie_id", col("movie_id").cast("int"))

# ============================================================
# Task 1: Calculate average rating for each movie
# ============================================================
avg_rating_df = ratings_df.groupBy("movie_id") \
    .agg(avg("rating").alias("average_rating"))

avg_rating_movie_df = avg_rating_df.join(movies_df, "movie_id")

print("\nTask 1: Average rating for each movie")
avg_rating_movie_df.select(
    "movie_title", "average_rating"
).show(10, False)

# ============================================================
# Task 2: Top ten movies with highest average ratings
# Improved by filtering movies with at least 50 ratings
# ============================================================
movie_stats_df = ratings_df.groupBy("movie_id") \
    .agg(
        avg("rating").alias("average_rating"),
        count("rating").alias("rating_count")
    ).join(movies_df, "movie_id")

top10_reliable_movies = movie_stats_df.filter(
    col("rating_count") >= 50
).orderBy(
    col("average_rating").desc()
)

print("\nTask 2: Top 10 movies with highest average ratings (minimum 50 ratings)")
top10_reliable_movies.select(
    "movie_title", "average_rating", "rating_count"
).show(10, False)

# ============================================================
# Task 3: Users with at least 50 ratings and favourite genre
# ============================================================
movie_cols = [
    "movie_id", "movie_title", "release_date", "video_release_date",
    "imdb_url", "unknown", "Action", "Adventure", "Animation",
    "Children", "Comedy", "Crime", "Documentary", "Drama", "Fantasy",
    "FilmNoir", "Horror", "Musical", "Mystery", "Romance", "SciFi",
    "Thriller", "War", "Western"
]

movies_genre_df = movies_rdd.map(lambda x: x.split("|")).toDF(movie_cols)

for c in movie_cols[5:]:
    movies_genre_df = movies_genre_df.withColumn(c, col(c).cast("int"))

movies_genre_df = movies_genre_df.withColumn(
    "movie_id", col("movie_id").cast("int")
)

active_users_df = ratings_df.groupBy("user_id") \
    .agg(count("movie_id").alias("movies_rated")) \
    .filter(col("movies_rated") >= 50)

active_ratings_df = ratings_df.join(active_users_df, "user_id")
active_movies_df = active_ratings_df.join(movies_genre_df, "movie_id")

genre_cols = movie_cols[5:]

genre_count_df = active_movies_df.groupBy("user_id").agg(
    *[sum(col(g)).alias(g) for g in genre_cols]
)

genre_stack_expr = """
stack(19,
'unknown', unknown,
'Action', Action,
'Adventure', Adventure,
'Animation', Animation,
'Children', Children,
'Comedy', Comedy,
'Crime', Crime,
'Documentary', Documentary,
'Drama', Drama,
'Fantasy', Fantasy,
'FilmNoir', FilmNoir,
'Horror', Horror,
'Musical', Musical,
'Mystery', Mystery,
'Romance', Romance,
'SciFi', SciFi,
'Thriller', Thriller,
'War', War,
'Western', Western
) as (genre, genre_count)
"""

genre_long_df = genre_count_df.select(
    "user_id",
    expr(genre_stack_expr)
)

window_spec = Window.partitionBy("user_id").orderBy(col("genre_count").desc())

favorite_genre_df = genre_long_df.withColumn(
    "rank",
    row_number().over(window_spec)
).filter(
    col("rank") == 1
).drop("rank")

task3_result_df = favorite_genre_df.join(
    active_users_df,
    "user_id"
).select(
    "user_id",
    "movies_rated",
    col("genre").alias("favourite_genre"),
    "genre_count"
)

print("\nTask 3: Users with at least 50 ratings and favourite genre")
task3_result_df.orderBy(
    col("movies_rated").desc()
).show(20, False)

# ============================================================
# Task 4: Users less than 20 years old
# ============================================================
users_under_20_df = users_df.filter(col("age") < 20)

print("\nTask 4: Users less than 20 years old")
users_under_20_df.show(20, False)
print("Users under 20:", users_under_20_df.count())

# ============================================================
# Task 5: Scientists aged between 30 and 40
# ============================================================
scientist_users_df = users_df.filter(
    (col("occupation") == "scientist") &
    (col("age") >= 30) &
    (col("age") <= 40)
)

print("\nTask 5: Users whose occupation is scientist and age is between 30 and 40")
scientist_users_df.show(20, False)
print("Scientists aged 30 to 40:", scientist_users_df.count())

# ============================================================
# Cassandra Integration Template
# ============================================================
# The following code can be used when Cassandra and the Spark-Cassandra connector
# are available in the execution environment.
#
# Example spark-submit:
# spark-submit --packages com.datastax.spark:spark-cassandra-connector_2.11:2.3.0 assignment2_movielens_spark.py
#
# Example writes:
# avg_rating_movie_df.write.format("org.apache.spark.sql.cassandra") \
#     .mode("append") \
#     .options(table="average_movie_ratings", keyspace="movielens") \
#     .save()
#
# top10_reliable_movies.write.format("org.apache.spark.sql.cassandra") \
#     .mode("append") \
#     .options(table="top10_movies", keyspace="movielens") \
#     .save()
#
# task3_result_df.write.format("org.apache.spark.sql.cassandra") \
#     .mode("append") \
#     .options(table="user_favourite_genres", keyspace="movielens") \
#     .save()
#
# users_under_20_df.write.format("org.apache.spark.sql.cassandra") \
#     .mode("append") \
#     .options(table="users_under_20", keyspace="movielens") \
#     .save()
#
# scientist_users_df.write.format("org.apache.spark.sql.cassandra") \
#     .mode("append") \
#     .options(table="scientist_users_30_40", keyspace="movielens") \
#     .save()

spark.stop()
