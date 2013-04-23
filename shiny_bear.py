from flask import Flask
import os

app = Flask(__name__)
app.debug = True


class Movie(object):
    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return "<Movie ({})>".format(self.path)

    def get_name(self):
        # only works for UNIX systems, Windows uses \ as a path seperator
        return self.path.split("/")[-1]


def li_decorator(string):
    return decorate("li", string)


def decorate(element, string):
    return "<{el}>{value}</{el}>".format(el=element,
                                         value=string)


def list_movie_paths(path):
    def fn(x):
        return os.path.join(path, "01", x)

    dirs = map(fn, os.listdir(os.path.join(path, "01")))
    return filter(os.path.isdir, dirs)


# ./static/moves/{}/movi1 -> <move name>, <movie video file path>
# ./static/moves/{}/movi2

@app.route("/")
def index():
    index_file = open("index.html", "r")
    index_content = index_file.read()

    #list_movie_paths("./static/movies")
    movies = map(Movie, list_movie_paths("./static/movies"))
    movie_names = map(Movie.get_name, movies)
    movies_html = decorate("ul",
                           "\n".join(map(li_decorator, movie_names)))

    return index_content.format(movies=movies_html)


if __name__ == "__main__":
    app.run()
