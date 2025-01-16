from flask import Flask, jsonify
from htmlParsers.filmParser import DataType
import htmlParsers.userScraper as us
import json
import requests

app = Flask(__name__)

allowedTypes = ["films", "likes", "watchlist"]

@app.route("/<username>/<type>")
def getUserInfoByType(username, type):
    if type not in allowedTypes:
        return "This is not an allowed type, type=" + type
    films = us.get_page_type_information(username, type, DataType.NODA)
    nodaResponse = requests.post("http://localhost:8080/input/asJSON", params={"films": json.dumps(films)})

    response = jsonify({"nodaResponse": nodaResponse.status_code})
    return response

@app.route("/ping")
def ping():
    return "alive"
