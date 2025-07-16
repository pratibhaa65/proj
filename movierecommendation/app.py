import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=9550aa0755e3dccf1e20d2245e90d52d'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']


movies_dict=pickle.load(open('movierecommendation/movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

def recommend(movie):
    movies_index=movies[movies['title']==movie].index[0]
    dist=similarity[movies_index]
    movies_list=[(idx, float(score)) for idx, score in sorted(list(enumerate(dist)),reverse=True,key=lambda x:x[1])[1:6]]

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies ,  recommended_movies_poster          

similarity=pickle.load(open('movierecommendation/similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie = st.selectbox(
    "Select the movie you like!!!",
    movies['title'].values
)

if st.button('Recommend'):
    names,posters=recommend(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.subheader(names[i])
            st.image(posters[i])