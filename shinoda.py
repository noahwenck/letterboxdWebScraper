from flask import Flask, Response, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from htmlParsers.filmParser import DataType
from htmlParsers import userScraper, listScraper

app = Flask(__name__)
CORS(app)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Shinoda API (Letterboxd Web Scraper)"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

allowedTypes = ["films", "likes", "watchlist"]


# todo: Add <dataType> to the route?
@app.route("/<username>/<letterboxdType>")
def getUserInfoByType(username, letterboxdType):
    if letterboxdType not in allowedTypes:
        print("This is not an allowed type, type=" + letterboxdType)
        return Response(status=400)
    films = userScraper.get_page_type_information(username, letterboxdType, DataType.NODA)

    # todo: add catch for failure to post/connect
    return jsonify(films), 200


@app.route("/list/<username>/<list_path>")
def getListInfo(username, list_path):
    list_url = "https://letterboxd.com/" + username + "/list/" + list_path
    listData = listScraper.collect_films_from_list(list_url, DataType.NODA)

    # todo: add catch for failure to post/connect
    return jsonify(listData), 200


@app.route("/health/check")
def healthCheck():
    return Response(status=200)


@app.route("/ping")
def ping():
    return "alive"


if __name__ == "__main__":
    app.run()
