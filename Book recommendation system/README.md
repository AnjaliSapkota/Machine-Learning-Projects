# 📚 Book Recommendation System

A machine learning-based **Book Recommendation System** built with **Python**, **Scikit-learn**, and **Streamlit**. The project recommends books using **Collaborative Filtering** and also displays the most popular books based on user ratings.

## 🚀 Live Demo

🔗 **Streamlit App:**  https://machine-learning-projects-bww28p6qf9xprvtcuszzpq.streamlit.app/

## 📌 Features

- 📖 Popular Books Recommendation
- 🤝 Collaborative Filtering Recommendation
- 🔍 Search books by title
- 🖼️ Displays book cover images
- ⭐ Shows average rating and total ratings
- 🎨 Interactive Streamlit interface

---

## 📂 Project Structure

```
Book recommendation system/
│
├── app.py
├── requirements.txt
│
├── data/
│   ├── BX-Books.csv
│   ├── BX-Users.csv
│   └── BX-Book-Ratings.csv
│
├── models/
│   ├── popular_books.csv
│   ├── books.pkl
│   ├── book_pivot.pkl
│   └── similarity.pkl
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── Data Cleaning.ipynb
│   ├── Popularity Based Recommendation.ipynb
│   └── Collaborative Filtering.ipynb
│
└── README.md
```

---

## 📊 Dataset

This project uses the **Book Recommendation Dataset** from Kaggle.

- **Books:** 271,360
- **Users:** 278,858
- **Ratings:** 1,031,136

Dataset:
https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle
- Jupyter Notebook

---

## 📈 Project Workflow

### 1. Exploratory Data Analysis (EDA)

- Dataset overview
- Missing value analysis
- Distribution of ratings
- User activity analysis
- Publication year analysis

---

### 2. Data Cleaning

- Renamed columns
- Removed invalid publication years
- Cleaned missing authors and publishers
- Handled invalid user ages
- Separated explicit and implicit ratings

---

### 3. Popularity-Based Recommendation

Books are ranked using:

- Average Rating
- Number of Ratings

Only books with a sufficient number of ratings are considered to avoid bias.

---

### 4. Collaborative Filtering

User-based filtering was performed by:

- Selecting active users
- Filtering frequently rated books
- Creating a User-Book Pivot Table
- Computing Cosine Similarity

The model recommends books similar to the selected title.

---

## 📷 Application Preview

### Popular Books

Displays the highest-rated books along with:

- Cover Image
- Book Title
- Author
- Average Rating
- Total Ratings

### Recommend Books

Users can:

- Search for a book
- Receive similar book recommendations
- View book covers and authors
---

## 📚 Recommendation Method

The recommendation engine uses **Collaborative Filtering** with **Cosine Similarity**.

Steps:

1. Remove inactive users.
2. Keep frequently rated books.
3. Create a User × Book rating matrix.
4. Compute cosine similarity between books.
5. Recommend the most similar books.

---

## 📌 Future Improvements

- Content-Based Recommendation
- Hybrid Recommendation System
- Filter by Genre and Author
- Personalized User Recommendations
- Better UI/UX
- Docker Deployment
- Cloud Database Integration

---

Please consider giving it a ⭐ on GitHub.
