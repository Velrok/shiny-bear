import os


def create_movie_path_list(movies_path):
    movie_path_list = []
    for movie in movie_names_list(movies_path):
        movie_path_list.append(movies_path + movie + "/")
    return movie_path_list


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


print movie_names_list("./testumgebung/movies/")
print create_movie_path_list("./testumgebung/movies/")