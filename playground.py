class Movie(object):
    def __init__(self, path):
        self.path = path

    def get_name(self):
        return self.path.split("/")[-1]


def find_movies():
    dirs = ["./static/movies/01/Batman (2008)",
            "./static/movies/01/Superman (2013)"]
    return map(Movie, dirs)


print map(Movie.get_name, find_movies())
