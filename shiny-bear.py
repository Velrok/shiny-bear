from flask import Flask
from os import listdir
app = Flask(__name__)
app.debug = True

movies_dir = "/Volumes/media/kenobi/movies"
movies_list = listdir(movies_dir)

movies_list_html = []

for movie in movies_list:
    movie_html = "<li>" + movie + "</li>"
    movies_list_html.append(movie_html)


@app.route("/")
def index():
    index = open("index.html", "r")
    index_str = index.read()
    return index_str.format(li_movies=" ".join(movies_list_html))


if __name__ == "__main__":
    app.run()
