from flask import Flask
import htmlParsers.userScraper as us
import json

app = Flask(__name__)

@app.route("/<username>")
def getUserInfoByType(username):
    films = us.get_page_type_information(username, "films", False)
    return json.dumps(films)

@app.route("/ping")
def ping():
    return "alive"