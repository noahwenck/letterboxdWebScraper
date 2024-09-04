import htmlParsers.filmParser as fp
import htmlParsers.pageParser as pp
import re
import requests


def collect_films_from_list(list_url, everything):

    html = requests.get(list_url).text

    if "<p class=\"list-number\">" in html:
        rank = True
        ranking = 1
    else:
        rank = False

    films = [find_list_name(html)]
    for page in range(1, pp.get_num_pages(html) + 1):
        if page != 1:
            html = requests.get(list_url + "/page/" + str(page)).text

        for entry in re.finditer("filmListEntry", html):
            info = fp.get_film_info(pp.get_film_url_from_list_page(html, entry), everything)

            film = {}
            if rank:
                film.update({"Ranking": ranking})
            film.update({"Name": pp.get_film_name_from_list_page(html, entry)})
            film.update(info)
            films.append(film)

            if rank:
                ranking += 1

    return films


def find_list_name(html): # todo remove windows reserved chars
    """
    Finds the name of the list

    :param html: html contents of the first (or only) page of the list
    :return: name of the list
    """

    name_marker = "<meta property=\"og:title\" content=\""
    mod_html = html[html.find(name_marker) + len(name_marker):]
    name = mod_html[:mod_html.find("\" />")]
    name = fp.fix_html_characters(name)
    name = name.replace(":", "")
    return name.replace(" ", "-")
