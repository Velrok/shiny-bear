from nose.tools import *
from shiny_bear import *


def test_list_movie_paths():
    result = list_movie_paths("./static/movies")
    expected = ["./static/movies/01/Movie 1 (2009)", "./static/movies/01/Movie 2 (2011)"]
    eq_(result, expected)


def test_movie_get_name():
    movie = Movie("./some/path/Batman (2013)")
    eq_(movie.get_name(),
        "Batman (2013)")
