import streamlit as st
import pandas as pd
import pickle

# Page Configuration
st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="wide"
)

st.write("Welcome to my Book Recommendation System!")

# Load models

popular_books = pd.read_csv("models/popular_books.csv")
book_pivot = pd.read_pickle("models/book_pivot.pkl")
books = pd.read_pickle("models/books.pkl")
        
with open("models/similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

st.success("Models loaded successfully!")

st.write(popular_books.head())