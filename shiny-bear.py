from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    index = open("index.html", "r")
    return index.read()


if __name__ == "__main__":
    app.run()
