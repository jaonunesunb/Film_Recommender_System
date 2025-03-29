# Import Pandas
import pandas as pd

# Function that computes the weighted rating of each movie
def weighted_rating(x, m, c):
    v_movie_vote_count = x['vote_count']
    R_vote_average_mean = x['vote_average']
    # Calculation based on the IMDB formula
    return (v_movie_vote_count/(v_movie_vote_count+m) * R_vote_average_mean) + (m/(m+v_movie_vote_count) * c)


"""
Nota Ponderada (Weighted Rating - WR)

Fórmula:
WR = (v / (v + m) * R) + (m / (v + m) * C)

Onde:
- WR: Nota ponderada do item
- R: Nota média do item (ex: nota média de um filme)
- v: Número de votos recebidos pelo item
- m: Número mínimo de votos exigido para considerar o item na classificação - fica a critério do freguês
- C: Média de todas as notas de todos os itens
"""


# Load Movies Metadata
metadata = pd.read_csv('src/data/movies_metadata.csv', low_memory=False)

# Print the first three rows
print(metadata.head(3))

C = metadata['vote_average'].mean()

# Calculate the minimum number of votes required to be in the chart, m
M = metadata['vote_count'].quantile(0.90)
print(M)

# Filter out all qualified movies into a new DataFrame
qualified_movies = metadata.copy().loc[metadata['vote_count'] >= M]
print(qualified_movies.shape)

# Define a new feature 'score' and calculate its value with `weighted_rating()`
qualified_movies['score'] = qualified_movies.apply(lambda x: weighted_rating(x, M, C), axis=1)

#Sort movies based on score calculated above
q_qualified_movies = qualified_movies.sort_values('score', ascending=False)

#Print the top 15 movies
print(qualified_movies[['title', 'vote_count', 'vote_average', 'score']].head(20))

