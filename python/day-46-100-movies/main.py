import requests
from bs4 import BeautifulSoup

URL = ("https://web.archive.org/web/20200518073855/https://www.empireonline.com/"
       "movies/features/best-movies-2/")

# Write your code below this line 👇

url = requests.get(URL)
website = url.text
soup = BeautifulSoup(website, "html.parser")
movies = soup.find_all(name = "h3", class_ = "title")

# all_movies = []
# for movie in movies:
#     all_movies.append(movie.getText())
# LINES 12 - 14, SHOULD'VE DONE LIST COMPREHENSION:
# DID LIST COMPREHENSION AFTER WATCHING THE SOLUTION (DIDN'T COPY THOUGH, REALISED I
# COULD USE IT SO THEN WENT TO DO IT MYSELF

all_movies = [movie.getText() for movie in movies]
all_movies = all_movies[::-1] # Reverse the order so number 1 shows at the top of the list -
# slice operator [start:stop:step] so starts at beginning of all_movies list(:), stops
# at end of all_movies list (:) but goes in reverse order (-1).

movies = ""
for item in all_movies:
    movies += item + "\n"

with open("movies.txt", mode="w") as file:
    file.write(movies)
