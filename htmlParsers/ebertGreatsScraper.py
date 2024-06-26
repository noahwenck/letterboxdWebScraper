import htmlParsers.filmParser as fp
import re
import requests

URL = "https://letterboxd.com/dvideostor/list/roger-eberts-great-movies/"


# todo: this, and the other list functions are very similar, may be able to combine them
def get_roger_ebert_great_movies():
    """
    Collects information and ranking of films on Roger Ebert's Great Movies List.
    General information regarding the film is stored in a sepearate dictionary, "info"

    :return: a list of films on Roger Ebert's Great Movies List
    """

    html = requests.get(URL).text

    list_of_films = []
    for page in range(1, 5):  # List is 4 pages long
        if page != 1:
            html = requests.get(URL + "/page/" + str(page)).text

        for film in re.finditer("filmListEntry", html):
            # name
            start = film.start() + html[film.start():].find("alt=\"") + 5
            end = start + html[start:].find("\"")
            name = html[start:end]

            area_to_look = html[:html.find("alt=\"" + name + "\"")]
            area_to_look = area_to_look[area_to_look.rfind("data-film-slug") + 16:]
            film_part = area_to_look[:area_to_look.find("\"")]
            url = "film/" + film_part + "/"

            info = fp.get_film_info(url)

            film = {
                "name": name,
            }
            film.update(info)
            list_of_films.append(film)

    return list_of_films
