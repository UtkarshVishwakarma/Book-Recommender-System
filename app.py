import streamlit as st
import pickle
import pandas as pd
from recommend import recommend
import sklearn

pt = pickle.load(open('models/pt.pkl', 'rb'))

pt = pd.DataFrame(pt)

st.title("Book Recommender System")

book = st.selectbox("Select A Book Below" ,pt.index.tolist())

if st.button("Recommend"):
    recommendations = recommend(book)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(recommendations[0][2])
        st.write(recommendations[0][0])
        st.write(recommendations[0][1])

    with col2:
        st.image(recommendations[1][2])
        st.write(recommendations[1][0])
        st.write(recommendations[1][1])

    with col3:
        st.image(recommendations[2][2])
        st.write(recommendations[2][0])
        st.write(recommendations[2][1])

    with col4:
        st.image(recommendations[3][2])
        st.write(recommendations[3][0])
        st.write(recommendations[3][1])

    with col5:
        st.image(recommendations[4][2])
        st.write(recommendations[4][0])
        st.write(recommendations[4][1])



