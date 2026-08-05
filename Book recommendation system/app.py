import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Page Configuration
st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="wide"
)

st.write("Welcome to my Book Recommendation System!")

# Load models
def load_data():
    popular_books = pd.read_csv("models/popular_books.csv")
    books = pd.read_pickle("models/books.pkl")
    book_pivot = pd.read_pickle("models/book_pivot.pkl")

    with open("models/similarity.pkl", "rb") as f:
        similarity = pickle.load(f)

    return popular_books, books, book_pivot, similarity


popular_books, books, book_pivot, similarity = load_data()


# Add sidebar for navigation
st.sidebar.title("📚 Navigation")

option = st.sidebar.radio(
    "Choose Recommendation Type",
    [
        "Popular Books",
        "Recommend Books"
    ]
)

# Popular Books Page


if option == "Popular Books":

    st.header("🔥 Most Popular Books")

    cols = st.columns(5)

    for i in range(min(20, len(popular_books))):

        with cols[i % 5]:

            st.image(
                popular_books.iloc[i]["Image_URL_L"],
                use_container_width=True
            )

            st.markdown(
                f"**{popular_books.iloc[i]['Book_Title']}**"
            )

            st.caption(
                popular_books.iloc[i]["Book_Author"]
            )

            st.write(
                f"⭐ Rating: {round(popular_books.iloc[i]['avg_rating'],2)}"
            )

            st.write(
                f"👥 {popular_books.iloc[i]['num_ratings']} Ratings"
            )