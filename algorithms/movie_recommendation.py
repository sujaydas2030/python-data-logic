"""
Movie recommendation using dot product similarity.
"""

# Import literal_eval to safely evaluate string input
from ast import literal_eval

# Taking the input
user_vector = literal_eval(input())
movie_vectors = literal_eval(input())

def recommend_movie(user_vector, movie_vectors):
    # Write your code here
  dot_products=[]
  for movie_vector in movie_vectors:
    if len(movie_vector)!=len(user_vector):
      return 'Invalid movie vector(s)'
    dot_product=0
    for i in range(len(movie_vector)):
      dot_product+=user_vector[i]*movie_vector[i]
    dot_products.append(dot_product)
  max_movie= max(dot_products)

  index=dot_products.index(max_movie)

  return f'Movie {index+1} is highly likely to be enjoyed by the user.'

# Print the output
print(recommend_movie(user_vector, movie_vectors))
