import htmlParsers.filmParser as fp
import re
import requests

URL = "https://letterboxd.com/lifeasfiction/list/letterboxd-100-animation/"


def get_top_100_animated_films():
    """
    Collects information and ranking of films on Letterboxd's Top 100 Animated Films List.
    General information regarding the film is stored in a sepearate dictionary, "info"

    :return: a list of films on Letterboxd's Top 100 Animated Films List
    """
    html = requests.get(URL).text

    list_of_films = []
    ranking = 1

    # Since this list is only 100, we only have to deal with one page

    for film in re.finditer("filmListEntry", html):
        # name
        start = film.start() + html[film.start():].find("alt=\"") + 5
        end = start + html[start:].find("\"")
        name = html[start:end]

        area_to_look = html[:html.find("alt=\"" + name + "\"")]
        area_to_look = area_to_look[area_to_look.rfind("data-film-slug") + 16:]
        film_part = area_to_look[:area_to_look.find("\"")]
        url = "film/" + film_part + "/"

        film = {
            "ranking": ranking,
            "name": name,
            "info": fp.get_film_info(url)
        }
        ranking += 1
        list_of_films.append(film)

    return list_of_films
