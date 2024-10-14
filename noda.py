from flask import Flask
import htmlParsers.userScraper as us
import json
import requests

app = Flask(__name__)

@app.route("/<username>/<type>")
def getUserInfoByType(username, type):
    if type != "films" and type != "likes":
        return "Only allowing films or likes as input for now"
    films = us.get_page_type_information(username, type, False)
    response = requests.post("http://localhost:8080/input/asJSON", params={"films": json.dumps(films)})
    return json.dumps(response.status_code)

@app.route("/ping")
def ping():
    return "alive"
