import pickle
import streamlit as st
import requests

#Method to fetch poster of a movie
def fetch_poster(movie_id):
    #API call to TMDB
    url = "https://api.themoviedb.org/3/movie/{}?api_key=d15120b5f2fc373b1c88ad5c97384251&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

#Method to recommend a set of movies based on user selected movie
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda x:x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name, recommended_movies_poster
        

st.header("Movie Recommendation System")
#Load movies
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))

#Load Similarity scores
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

#Selection section
movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Select a movie that you like',
    movie_list
)

#button to show recommendations
if st.button('Show Recommendations'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    mov1, mov2, mov3, mov4, mov5 = st.columns(5)
    with mov1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0])

    with mov2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1])

    with mov3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2])

    with mov4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3])
        
    with mov5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4])    