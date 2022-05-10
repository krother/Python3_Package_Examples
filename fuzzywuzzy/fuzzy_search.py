
from fuzzywuzzy import process

movie_titles = ['Titanic', 'Star Wars', 'Breakfast at Tiffanys']

# find the most similar match and a quality score
print(process.extractOne('Star Wors', movie_titles))
print(process.extractOne('Star', movie_titles))
print(process.extractOne('Tutunuc', movie_titles))
