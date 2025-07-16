import streamlit as st
import pickle
import pandas as pd

st.title('Movie Recommender System')

movies_dict=pickle.load(open('movierecommendation/movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

selecte_movie = st.selectbox(
    "Select the movie you like!!!",
    movies['title'].values
)

st.write("You selected:", selecte_movie)

if st.button('say'):
    

# import streamlit as st
# import pickle
# import pandas as pd

# # Set title
# st.title('🎬 Movie Recommender System')

# # Load the pickle file 
# with open('movierecommendation/movies_dict.pkl', 'rb') as f:
#     movies_dict = pickle.load(f)

# # Convert to DataFrame
# movies = pd.DataFrame(movies_dict)

# # Selectbox to choose a movie
# option = st.selectbox(
#     "Select a movie to get recommendations:",
#     movies['title'].values
# )

# # Show selected movie
# st.write("🎥 You selected:", option)
