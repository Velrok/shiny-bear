from flask import Flask
import os

app = Flask(__name__)
app.debug = True


def generate_drive_path(drive_name):
    """
    Describe what this does. aka doc string
    """
    movies_path = "/Volumes/media/" + drive_name + "/movies/"
    return movies_path


def remove_year(movie_name):
    movie_name_without_year = movie_name[:-7]
    return movie_name_without_year


def movie_names_list(movies_path):
    """
    safe movienames (if folder) from one drive to list
    """
    movie_names = []
    movie_names_temp = list(os.listdir(movies_path))

    for movie in movie_names_temp:
        if os.path.isdir(movies_path + movie):
            movie_names.append(movie)
    return movie_names


def movies_html(movie_names_list):
    """
    add <li> for html
    """
    movies_list_html = []

    for movie in movie_names_list:
        movies_list_html.append("<li>" + movie + "</li>")

    return movies_list_html


def find_video_file(movie_path_for_single_movie):
    for file_item in os.listdir(movie_path_for_single_movie):
        if ".mkv" or ".avi" in file_item:
            return file_item


def create_path_to_video_file(movie_path_for_single_movie):
    return movie_path_for_single_movie + find_video_file(movie_path_for_single_movie)


def create_movie_path_list(movies_path):
    movie_path_list = []
    for movie in movie_names_list(movies_path):
        movie_path_list.append(movies_path + movie + "/")
    return movie_path_list


def create_video_file_list(movies_path):
    video_file_list = []
    for movie in create_movie_path_list(movies_path):
        video_file_list.append(create_path_to_video_file(movie))
    return video_file_list


def html_download_link(movies_path):
    html_download_link_list = []
    for link in create_video_file_list(movies_path):
        html_download_link_list.append('<a href="' + link + '">Download</a>')
    return html_download_link_list

@app.route("/")
def index():
    index = open("index.html", "r")
    index_str = index.read()
    return index_str.format(li_movies=" ".join(movies_list_html))


if __name__ == "__main__":
    app.run()
