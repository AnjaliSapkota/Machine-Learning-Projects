import streamlit as st
import pandas as pd
import numpy as np
import pickle
from pathlib import Path

# Page Configuration
st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"

st.write("Discover popular books and get personalized recommendations.")

# Load models
@st.cache_data
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

# Recommendation Function

def recommend(book_name, n=5):

    if book_name not in book_pivot.index:
        return []

    index = np.where(book_pivot.index == book_name)[0][0]

    similar_items = sorted(
        list(enumerate(similarity[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:n+1]

    recommendations = []

    for item in similar_items:

        title = book_pivot.index[item[0]]

        temp = books[
            books["Book_Title"] == title
        ].drop_duplicates("Book_Title")

        recommendations.append({
            "title": temp["Book_Title"].values[0],
            "author": temp["Book_Author"].values[0],
            "image": temp["Image_URL_L"].values[0]
        })

    return recommendations

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


# Collaborative Filtering

else:

    st.header("📖 Find Similar Books")

    selected_book = st.selectbox(
        "Select a Book",
        sorted(book_pivot.index.tolist())
    )

    if st.button("Recommend"):
        with st.spinner("Finding similar books..."):

            recommendations = recommend(selected_book)

        if len(recommendations) == 0:

            st.warning("Book not found.")

        else:

            cols = st.columns(5)

            for idx, book in enumerate(recommendations):

                with cols[idx]:

                    st.image(book["image"],use_container_width=True)
                    st.markdown(f"### {book['title']}")
                    st.caption(f"✍️ {book['author']}")