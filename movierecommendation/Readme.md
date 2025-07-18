# Movie Recommender System

This is a content-based movie recommendation system built with Python and Streamlit. You pick a movie, and it shows you five similar ones along with their posters. The recommendations are based on movie similarity.It is a content based recommendation system.


## Features

- Interactive web interface with Streamlit.
- Content-based filtering using cosine similarity.
- It shows you 5 similar movies.
- Real-time poster fetching via TMDB API.
- Easy to use and extend.
- Runs entirely on your local machine using Streamlit.

## Dataset Used

The project uses data from TMDB Movie Metadata on Kaggle:  
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

The data was preprocessed and used to create:

- `movies_dict.pkl` — contains movie info like titles and IDs.
- `similarity.pkl` — contains precomputed similarity scores between movies.

Note: These `.pkl` files are already created and loaded in the app.


### Prerequisites

Make sure you have Python 3.7+ installed. Install the required Python packages using pip:

```bash
pip install streamlit pandas requests
