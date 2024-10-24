import streamlit as st

st.image("deadpool.png")
st.title("Welcome to the Movie App! :movie_camera:")
st.markdown("Discover your next movie adventure.")

import duckdb

# creating an in memory database from the csv files
db = duckdb.connect(":memory:")
cursor = db.cursor()
cursor.execute("CREATE TABLE movie AS (SELECT * FROM 'tmdb/movies.csv')")
cursor.execute("CREATE TABLE person AS (SELECT * FROM 'tmdb/people.csv')")
cursor.execute("CREATE TABLE genres AS (SELECT * FROM 'tmdb/genres.csv')")
cursor.execute("CREATE TABLE keywords AS (SELECT * FROM 'tmdb/keywords.csv')")


# Display all genres sorted by the number of movies

sql = """
SELECT genre, count(movie_id) AS n_movies
    FROM genres
    GROUP BY genre
    ORDER BY 2 DESC
"""
genres = cursor.execute(sql).fetch_df()
selected_genre = st.selectbox(label="What is your vibe today?", options = genres["genre"])


# Display the 10 most popular movies in the selected genre

sql = """
    SELECT title, popularity, vote_average
    FROM movie INNER JOIN genres ON movie.id = genres.movie_id
    WHERE genre = ?
    ORDER BY popularity DESC
"""
movies_in_genre = cursor.execute(sql, [selected_genre]).fetch_df()
st.table(movies_in_genre[:10])


# Make the user pick the title and display the info for the selected title

selected_title = st.selectbox(label="Pick a title", options = movies_in_genre["title"])

sql = """
    SELECT id, title, tagline, overview, image_url
    FROM movie
    WHERE title = ?
"""
movie_info = cursor.execute(sql, [selected_title]).fetchone()
movie_id = movie_info[0]
movie_tagline = movie_info[2]
movie_overview = movie_info[3]
image_url = movie_info[4]

poster_col, info_col = st.columns([0.3, 0.7])

poster_col.image(image_url)
info_col.markdown(selected_title)
info_col.markdown(f"*{movie_tagline}*")
info_col.markdown(f"*{movie_overview}*")


# Display top 5 billed cast fot the selected movie

sql = """
    SELECT person_id, name, character, image_url
    FROM person
    WHERE movie_id = ?
    LIMIT 5
"""
movie_cast = cursor.execute(sql, [movie_id]).fetchall()
for i, col in enumerate(st.columns(5)):
    person_id, name, character, image_url = movie_cast[i]
    col.image(image_url, caption=name)
    col.markdown(character)


# Recommend movies based on the selected title

if st.button("Recommend movies!"):

    from recommender import recommend
    n_movies_to_recommend = 3
    recommended_ids = recommend(db, movie_id, n=n_movies_to_recommend)

    st.markdown(f"If you liked *{selected_title}*, check out these:")
    for i, col in enumerate(st.columns(n_movies_to_recommend)):
        sql = """
            SELECT title, image_url
            FROM movie
            WHERE id = ?
        """
        similar_movie_id = recommended_ids[i]
        title, poster = cursor.execute(sql, [similar_movie_id]).fetchone()
        col.image(poster, caption=title)
