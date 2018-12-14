
from fuzzywuzzy import process

movie_titles = ['Titanic', 'Star Wars', 'Breakfast at Tiffanys']

process.extractOne('Star Wors', movie_titles)
process.extractOne('Star', movie_titles)
process.extractOne('Tutu', movie_titles)
