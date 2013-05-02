from nose.tools import *
from shiny_bear import *


def test_list_movie_paths():
    result = list_movie_paths("./static/movies")
    expected = ["./static/movies/01/Movie 1 (2009)", "./static/movies/01/Movie 2 (2011)"]
    eq_(result, expected)


def test_movie_get_name():
    batman_movie = Movie("./some/path/Batman (2013)")
    eq_(batman_movie.get_name(),
        "Batman (2013)")


def test_get_video_file():
    movie_1 = Movie("./testumgebung/movies/Movie 1 (2009)")
    eq_(movie_1.get_video_file(), "./testumgebung/movies/Movie 1 (2009)/M1.mkv")


def test_get_video_file_avi():
    movie_1 = Movie("./testumgebung/movies/Movie 2 (2011)")
    eq_(movie_1.get_video_file(), "./testumgebung/movies/Movie 2 (2011)/M2.avi")
