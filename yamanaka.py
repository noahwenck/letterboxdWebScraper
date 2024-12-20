from flask import Flask, request
from htmlParsers import userScraper, listScraper
import json
import urllib

app = Flask(__name__)

if __name__ == "__main__":
    print("""
        Invalid startup, please use the following command to start yamanaka up:
        
        python -m flask --app yamanaka run
        """)


@app.route("/user/<username>")
def getUserInfoByType(username):
    films = userScraper.get_page_type_information(username, "films", False)
    return json.dumps(films)


@app.route("/list")
def getListInfo():
    # Parse the list url from the request
    parsed_url = urllib.parse.urlparse(request.args.get('list_url'))
    list_url = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path

    films = listScraper.collect_films_from_list(list_url, False)
    return json.dumps(films)


@app.route("/ping")
def ping():
    return "alive"
