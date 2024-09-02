import htmlParsers.filmParser as fp
import re
import requests

BASE_URL = "https://letterboxd.com/"
FILMS_PAGE = "/films/page/"


def get_page_type_information(user, page_type):
    """
    Collects a list of the films present on a specific type of user page

    :param user: the letterboxd user
    :param page_type: films, watchlist, likes, etc.
    :return: a list of films found on the page
    """

    page_type = "/" + page_type
    html = requests.get(BASE_URL + user + page_type).text

    film_list = []
    for page in range(1, fp.get_num_pages(html) + 1):

        if page != 1:
            html = requests.get(BASE_URL + user + page_type + "/page/" + str(page)).text

        for entry in re.finditer("<li class=\"poster-container\"", html):
            film = {
                "Name": fp.get_film_name_from_list_page(html, entry)
            }
            film.update(fp.get_film_info(fp.get_film_url_from_list_page(html, entry), False))
            film_list.append(film)

    return film_list