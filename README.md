<img width="701" height="270" alt="image" src="https://github.com/user-attachments/assets/59b6c16b-da5c-484e-949d-02d59b4e6eb8" />


# 🎬 Movie Recommendation System

A **content-based recommendation system** that suggests movies based on their similarity to a movie you like. It uses the **TMDB 5000 dataset** and applies **Natural Language Processing (NLP)** to analyze plots, genres, cast, crew, and keywords for generating recommendations.

<!--
TIP: Add a GIF or screenshot here showing recommendations being generated for a sample movie.
-->

**Caption:** Example — recommendations for *The Dark Knight*.

---

## 📋 Table of Contents

* [Features](#-features)
* [How It Works](#-how-it-works)
* [Tech Stack](#-tech-stack)
* [Dataset](#-dataset)
* [Getting Started](#-getting-started)
* [How to Use](#-how-to-use)
* [Future Improvements](#-future-improvements)

---

## ✨ Features

* **Content-Based Filtering**: Recommends movies using item attributes (genres, keywords, cast, crew).
* **Vector-Based Similarity**: Implements TF-IDF & Cosine Similarity to compute similarity scores.
* **Interactive**: Input a movie title to receive top 10 similar recommendations.
* **Data-Driven**: Built on a dataset containing thousands of movies.

---

## 🧠 How It Works

1. **Data Preprocessing**

   * Cleans and merges features (genres, keywords, overview, cast, crew).
   * Combines them into a single **tags** field per movie.

2. **Vectorization**

   * Applies **TF-IDF** to convert text into numerical vectors.
   * Creates a high-dimensional matrix representing all movies.

3. **Similarity Calculation**

   * Computes **Cosine Similarity** between vectors.
   * Higher scores indicate greater similarity.

4. **Recommendation**

   * User inputs a movie title.
   * System retrieves the vector and returns the top 10 most similar movies.

---

## 🛠️ Tech Stack

* **Python** (core language)
* **Pandas** (data processing)
* **Scikit-learn** (TF-IDF, similarity calculations)
* **Jupyter Notebook / Python Script** (development & testing)

---

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset** from Kaggle:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

📌 [Dataset Link on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

## 🚀 Getting Started

### Prerequisites

* Python 3.6+ installed
* Download TMDB 5000 dataset & place CSVs in the project directory

### Installation

Clone the repo:

```bash
git clone https://github.com/amanchauhan786/moviere.git
cd moviere
```

Create a virtual environment:

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install pandas scikit-learn
```

---

## ✍️ How to Use

Run the script:

```bash
python movie_recommender.py
```

When prompted:

* Enter a movie title (e.g., *Avatar*).
* Get **top 10 recommendations** instantly.

---

## 🔮 Future Improvements

* [ ] **Web App Deployment**: Build with Flask or Streamlit.
* [ ] **Hybrid Approach**: Add user ratings (collaborative + content-based).
* [ ] **Better NLP**: Integrate embeddings (Word2Vec, GloVe, BERT).
* [ ] **Optimization**: Save model & similarity matrix with Pickle for faster runs.

---


