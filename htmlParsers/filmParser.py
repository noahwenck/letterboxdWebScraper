import requests

BASE_URL = "https://letterboxd.com/"


def get_film_info(url):
    """
    Returns a dict of info regarding a film (excluding its name)
    :param url: url extension to ping the film's distinct page
    :return: dict of film information
    """
    html = requests.get(BASE_URL + url).text

    return {
        "director": get_director(html),
        "year": get_year(html),
        "language": get_language(html),
        "country": get_country(html),
        "runtime": get_runtime(html),
        "avg_rating": get_average_rating(html)
    }

def get_director(html):
    """
    Finds the director(s) of a film
    :param html: html of a films homepage
    :return: list of director(s)
    """

    dir_literal = "a href=\"/director/"
    mod_html = html[html.find(dir_literal):]
    director = []
    for i in range(html.count(dir_literal)):
        chunk_to_check = mod_html[mod_html.find(dir_literal):]
        mod_html = chunk_to_check[21:2000]
        director.append(chunk_to_check[chunk_to_check.find(">") + 1:chunk_to_check.find("<")])
    return director


def get_year(html):
    """
    Finds the release year of a film
    :param html: html of a films homepage
    :return: year (int)
    """

    mod_html = html[html.find("/films/year/"):]
    return int(mod_html[mod_html.find(">") + 1:mod_html.find("<")])


def get_language(html):
    """
    Finds the language(s) of a film
    :param html: html of a films homepage
    :return: list of language(s)
    """

    mod_html = html
    language = []
    for i in range(html.count("/films/language/")):
        cry = mod_html[mod_html.find("/films/language/"):]
        mod_html = cry[21:2000]
        new_language = cry[cry.find(">") + 1:cry.find("<")]

        # prevent overlap of Primary and Spoken languages
        if new_language not in language:
            language.append(cry[cry.find(">") + 1:cry.find("<")])

    return language


def get_country(html):
    """
    Finds the country of countries of a film
    :param html: html of a films homepage
    :return: list of country or countries
    """

    mod_html = html
    country = []
    for i in range(html.count("/films/country/")):
        cry = mod_html[mod_html.find("/films/country/"):]
        mod_html = cry[21:2000]
        country.append(cry[cry.find(">") + 1:cry.find("<")])

    return country


def get_runtime(html):
    """
    Finds the runtime of a film
    :param html: html of a films homepage
    :return: runtime of a film (int)
    """

    mod_html = html[html.find("runTime: "):]
    return int(mod_html[9:mod_html.find(" }"):])


def get_average_rating(html):
    """
    Finds the average rating of a film
    :param html: html of a films homepage
    :return: average rating of a film (float)
    """

    rating_literal = "\"Average rating\" /><meta name=\"twitter:data2\" content=\""
    mod_html = html[html.find(rating_literal):]
    return float(mod_html[len(rating_literal):mod_html.find(" out of 5")])