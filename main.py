import responses
import pandas as pd

import pickle

import requests
import streamlit as st

def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=254201f403c9e88bdcf59b935657b586&language=en-US'.format(movie_id)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/original" + poster_path
        else:
            return "No poster available for this movie."
    else:
        return "Failed to fetch data. Status code: {}".format(response.status_code)




def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_posters
movies_dict = pickle.load(open('D:\moviereccomendation\movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('D:\moviereccomendation\similarity.pkl','rb'))
#title
st.markdown(
    """
    <style>
    /* CSS to change font color, size, and make text bold */
    .title-text {
        color: #000000; /* Change the color code to the desired color */
        font-size: 45px; /* Change the font size to the desired value */
        font-weight: bold; /* Make the text bold */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the title using the custom styling
st.markdown('<p class="title-text">Movie Recommender System</p>', unsafe_allow_html=True)

#movie title
selected_movie_name = st.selectbox(' ',
movies['title'].values)

#button
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0c0c0c;
    color:#FFFFFF;
}
div.stButton > button:hover {
    background-color: #333333;
    color:#FFFFFF;
    }
</style>""", unsafe_allow_html=True)

b = st.button('Recommend')


#column for posters
if b:
    names,posters = recommend(selected_movie_name)
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.markdown(
            f"""
            <p style='font-family:"Bold", Gadget, sans-serif; font-size: 14px; color: Black;font-weight:Bold'>{names[0]}</p>
            """,
            unsafe_allow_html=True)
        st.image(posters[0])

    with col2:
        st.markdown(
            f"""
                    <p style='font-family:"Bold", Gadget, sans-serif; font-size: 14px; color: Black;font-weight:Bold'>{names[1]}</p>
                    """,
            unsafe_allow_html=True)
        st.image(posters[1])

    with col3:
        st.markdown(
            f"""
                    <p style='font-family:"Bold", Gadget, sans-serif; font-size: 14px; color: Black;font-weight:Bold'>{names[2]}</p>
                    """,
            unsafe_allow_html=True)
        st.image(posters[2])
    with col4:
        st.markdown(
            f"""
                    <p style='font-family:"Bold", Gadget, sans-serif; font-size: 14px; color: Black;font-weight:Bold'>{names[3]}</p>
                    """,
            unsafe_allow_html=True)
        st.image(posters[3])
    with col5:
        st.markdown(
            f"""
                    <p style='font-family:"Bold", Gadget, sans-serif; font-size: 14px; color: Black;font-weight:Bold'>{names[3]}</p>
                    """,
            unsafe_allow_html=True)
        st.image(posters[4])
#https://api.themoviedb.org/3/movie/{}?api_key=254201f403c9e88bdcf59b935657b586&language=en-US



def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://th.bing.com/th/id/OIP.5aiL2lxIDIUtpdOIWnyAeAHaEy?rs=1&pid=ImgDetMain");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
set_bg_hack_url()