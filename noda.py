from flask import Flask, Response
from flask_cors import CORS
from htmlParsers.filmParser import DataType
from htmlParsers import userScraper, listScraper
import json
import requests

app = Flask(__name__)
CORS(app)

allowedTypes = ["films", "likes", "watchlist"]


@app.route("/<username>/<letterboxdType>")
def getUserInfoByType(username, letterboxdType):
    if letterboxdType not in allowedTypes:
        return "This is not an allowed type, type=" + letterboxdType
    films = userScraper.get_page_type_information(username, letterboxdType, DataType.NODA)

    # todo: add catch for failure to post/connect
    requests.post("http://localhost:8080/input/films", params={"films": json.dumps(films)})

    return Response(status=204)


@app.route("/list/<username>/<list_path>")
def getListInfo(username, list_path):
    list_url = "https://letterboxd.com/" + username + "/list/" + list_path
    listData = listScraper.collect_films_from_list(list_url, DataType.NODA)

    # todo: add catch for failure to post/connect
    requests.post("http://localhost:8080/input/list", params={"list": json.dumps(listData)})

    return Response(status=200)


@app.route("/health/check")
def healthCheck():
    return Response(status=200)


@app.route("/ping")
def ping():
    return "alive"
