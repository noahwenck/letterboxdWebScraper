import htmlParsers.filmParser as fp
import re
import requests


def collect_films_from_list(list_url):

    html = requests.get(list_url).text

    if "<p class=\"list-number\">" in html:
        rank = True
        ranking = 1
    else:
        rank = False

    films = [find_list_name(html)]
    for page in range(1, fp.get_num_pages(html) + 1):
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

            film = {}
            if rank:
                film.update({"ranking": ranking})
            film.update({"name": name})
            film.update(info)
            films.append(film)

            if rank:
                ranking += 1

    return films


def find_list_name(html):
    """
    Finds the name of the list

    :param html: html contents of the first (or only) page of the list
    :return: name of the list
    """

    name_marker = "<meta property=\"og:title\" content=\""
    mod_html = html[html.find(name_marker) + len(name_marker):]
    name = mod_html[:mod_html.find("\" />")]
    name = fp.fix_html_characters(name)
    return name.replace(" ", "-")
