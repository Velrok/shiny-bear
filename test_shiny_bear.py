from nose.tools import *
from shiny_bear import *


def test_remove_year():
    eq_(remove_year("Movie Name (2012)"),
        "Movie Name")


def test_generate_drive_path():
    eq_(generate_drive_path("drive_name"),
        "/Volumes/media/drive_name/movies/")


def test_movie_names_list():
    eq_(movie_names_list("./testumgebung/movies/"),
        ["Movie 1 (2009)", "Movie 2 (2011)"])


def test_movies_html():
    eq_(movies_html(["Movie"]),
        ["<li>Movie</li>"])


def test_find_video_file():
    eq_(find_video_file("./testumgebung/movies/Movie 1 (2009)/"),
        "M1.mkv")


def test_create_path_to_video_file():
    eq_(create_path_to_video_file("./testumgebung/movies/Movie 1 (2009)/"),
        "./testumgebung/movies/Movie 1 (2009)/M1.mkv")


def test_create_video_file_list():
    eq_(create_video_file_list("./testumgebung/movies/"),
        ["./testumgebung/movies/Movie 1 (2009)/M1.mkv",
        "./testumgebung/movies/Movie 2 (2011)/M2.avi"])


def test_create_movie_path_list():
    eq_(create_movie_path_list("./testumgebung/movies/"),
        ["./testumgebung/movies/Movie 1 (2009)/",
        "./testumgebung/movies/Movie 2 (2011)/"])


def test_html_download_link():
    eq_(html_download_link("./testumgebung/movies/"),
        ['<a href="./testumgebung/movies/Movie 1 (2009)/M1.mkv">Download</a>',
        '<a href="./testumgebung/movies/Movie 2 (2011)/M2.avi">Download</a>'])


# def test_combine_movie_names_and_dl_list():
#     eq_()
