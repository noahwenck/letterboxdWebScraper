import htmlParsers.filmParser as fp
import re
import requests

NARRATIVE_URL = "https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/"
EBERT_URL = "https://letterboxd.com/dvideostor/list/roger-eberts-great-movies/"
ANIMATED_URL = "https://letterboxd.com/lifeasfiction/list/letterboxd-100-animation/"


def collect_films_from_list(selected_list):
    rank = True
    # todo: break into helper method for readability
    if selected_list == "narrative":
        list_url = NARRATIVE_URL
        pages = 3
    elif selected_list == "ebert":
        list_url = EBERT_URL
        pages = 3
        rank = False
    elif selected_list == "animation":
        list_url = ANIMATED_URL
        pages = 1

    html = requests.get(list_url).text

    if rank:
        ranking = 1

    films = []
    for page in range(1, pages + 1): # todo make get_num_pages instead of hardcoding
        if page != 1:
            html = requests.get(list_url + "/page/" + str(page)).text

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

            # todo: better way to do rank?
            if rank:
                film = {
                    "ranking": ranking,
                    "name": name
                }
            else:
                film = {
                    "name": name
                }

            film.update(info)
            films.append(film)

            if rank:
                ranking += 1

    return films
