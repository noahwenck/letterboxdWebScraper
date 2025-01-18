from flask import Flask, Response
from flask_cors import CORS
from htmlParsers.filmParser import DataType
import htmlParsers.userScraper as us
import json
import requests

app = Flask(__name__)
CORS(app)

allowedTypes = ["films", "likes", "watchlist"]


@app.route("/<username>/<type>")
def getUserInfoByType(username, type):
    if type not in allowedTypes:
        return "This is not an allowed type, type=" + type
    films = us.get_page_type_information(username, type, DataType.NODA)

    # todo: add catch for failure to post/connect
    requests.post("http://localhost:8080/input/films", params={"films": json.dumps(films)})

    return Response(status=204)


@app.route("/health/check")
def healthCheck():
    return Response(status=200)


@app.route("/ping")
def ping():
    return "alive"
