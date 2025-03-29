# 🎬 Movie Recommendation System (Content-Based)

This is a simple content-based movie recommender system built using Python and the scikit-learn library.  
It was developed as a **learning activity** to explore how recommendation algorithms work, especially using metadata features such as cast, director, screenwriter, genres, and keywords.

## 📚 About the Project

The recommender suggests movies that are similar in content to a given title, based on the following features extracted from the movie metadata:
- Cast (top 3 actors)
- Director
- Screenwriter
- Genres
- Keywords

These features are processed into a unified text field ("soup"), vectorized using **CountVectorizer**, and then compared using **Cosine Similarity**.

This project uses datasets from the [Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download) and TMDB databases.

## 🧠 Technologies Used

- Python 3
- Pandas
- NumPy
- scikit-learn (`CountVectorizer`, `cosine_similarity`)
- Jupyter / VSCode (optional)

## 🛠️ How It Works

1. Load movie metadata, keywords, and credits from CSV files.
2. Clean and extract relevant features (cast, crew, etc.).
3. Build a 'soup' string combining all text-based features.
4. Convert the soup into vectors.
5. Compute the cosine similarity between all movies.
6. Recommend the top 10 most similar movies to a given title.

## ▶️ Examples

### If you liked **Inception**:

- Looper
- Evil Behind You
- Reflection
- UFO - Distruggete base Luna!
- Premium Rush
- Trancers II: The Return of Jack Deth
- The Anomaly
- Half-Life
- Recon 2020: The Caprini Massacre
- Dark Island

### If you liked **Saving Private Ryan**:

- Hatred
- Schindler's List
- Breaker Morant
- Empire of the Sun
- Come and See
- The Bridge
- Why We Fight
- Taking Chance
- City of Life and Death
- Tubelight

> These results may vary slightly depending on data preprocessing and filtering settings.
