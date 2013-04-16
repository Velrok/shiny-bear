from nose.tools import *
from shiny_bear import *


def test_remove_year_removes_the_year():
    eq_(remove_year("Movie Name (2012)"),
        "Movie Name")


def test_generate_drive_path():
    eq_(generate_drive_path("drive_name"),
        "/Volumes/media/drive_name/movies/")


def test_movie_names_list():
    eq_(movie_names_list("/Volumes/media/yoda/movies/"),
        ["Eagle Eye (2008)"])
