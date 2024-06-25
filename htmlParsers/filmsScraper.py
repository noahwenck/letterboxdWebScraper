import htmlParsers.filmParser as fp
import re
import requests

BASE_URL = "https://letterboxd.com/"
FILMS_PAGE = "/films/page/"


def get_films_page_information(user):
    """
    Collects information regarding a users /films/ page to collect all the distinct films that a user has seen,
    compiles each film, with information (director, year, etc.) regarding each film into a single list

    :param user: the letterboxd user
    :return: a list of films the user has watched, and info relating to each film (director, year, etc.)
    """

    # find list of films names and list of urls to ping
    # todo make this cleaner
    # todo consider breaking logic into separate method
    films_html = requests.get(BASE_URL + user + "/films/").text
    numFilmsPages = get_num_films_pages(films_html)
    film_list = get_films_names(films_html)
    url_list = get_films_urls(films_html, film_list)
    for page in range(2, numFilmsPages + 1):
        films_html = requests.get(BASE_URL + user + FILMS_PAGE + str(page)).text
        new_films = get_films_names(films_html)
        film_list += new_films
        url_list += get_films_urls(films_html, new_films)

    film_info = []
    for num in range(len(film_list)):
        # get film html
        html = requests.get(BASE_URL + url_list[num]).text

        film = {
            "name": film_list[num],
            "director": fp.get_director(html),
            "year": fp.get_year(html),
            "language": fp.get_language(html),
            "country": fp.get_country(html),
            "runtime": fp.get_runtime(html),
            "avg_rating": fp.get_average_rating(html)
        }
        film_info.append(film)

    return film_info


def get_num_films_pages(html):
    """
    Returns the number of /films pages a user has
    \nSince every page can only hold 72 films,
    if the user has seen more than that we need to know how many other pages we need to go through

    :param html: html contents of $USER$/films page
    :return: number of /films pages a user has
    """

    num_start = html.rfind(FILMS_PAGE) + len(FILMS_PAGE)
    num_end = num_start + html[num_start:].find("/")
    try:
        return int(html[num_start:num_end])
    except ValueError:
        return 1


def get_films_names(html):
    """
    Returns a chronological array of the names of films listed on the given /films page

    :param html: html contents of $USER$/films page to yoink list of films from
    :return: chronological array of film names present on this page
    """

    # Separate the list of films from the rest of the garbo
    start = "<ul class=\"poster-list -p70 -grid film-list clear\">"
    end = "<div class=\"clear\"></div>"
    htmlListOfPosters = html[html.find(start):]
    htmlListOfPosters = htmlListOfPosters[:htmlListOfPosters.find(end)]

    start_of_item = "<li class=\"poster-container\">"
    list_of_films = []

    # Finds each distinct film in the list, parses for the name
    for film in re.finditer(start_of_item, htmlListOfPosters):
        film_start = film.start() + htmlListOfPosters[film.start():].find("alt=\"") + 5
        film_end = film_start + htmlListOfPosters[film_start:].find("\"")
        list_of_films.append(htmlListOfPosters[film_start:film_end])

    return list_of_films


def get_films_urls(html, list_of_films):
    """
    Returns the extension of a url needed to ping the actual page of an individual film

    :param html: html contents of $USER$/films
    :param list_of_films: literally in the name
    :return: list of url endings to ping film pages
    """

    # note to self: Dune/Godzilla issue should be solved, but keep eye out for any edge-cases
    url_list = []
    for film in list_of_films:
        area_to_look = html[:html.find("alt=\"" + film + "\"")]
        area_to_look = area_to_look[area_to_look.rfind("data-film-slug") + 16:]
        film_part = area_to_look[:area_to_look.find("\"")]
        url_list.append("film/" + film_part + "/")

    return url_list
