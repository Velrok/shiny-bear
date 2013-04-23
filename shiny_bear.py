from flask import Flask
import os

app = Flask(__name__)
app.debug = True





@app.route("/")
def index():
    index = open("index.html", "r")
    index_str = index.read()
    return index_str.format(li_movies=" ".join(html_download_links))


if __name__ == "__main__":
    app.run()
