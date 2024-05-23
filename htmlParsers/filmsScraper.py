import re
import requests

BASE_URL = "https://letterboxd.com/"
FILMS_PAGE = "/films/page/"


def getNumberOfFilmsPages(html):
    """
    Returns the number of /films pages a user has
    \nSince every page can only hold 72 films,
    if the user has seen more than that we need to know how many other pages we need to go through

    :param html: html contents of $USER$/films page
    :return: number of /films pages a user has
    """

    spot_to_look = html.rindex(FILMS_PAGE)
    start = html[spot_to_look + len(FILMS_PAGE):].find(">")
    # lmao good luck
    num = html[spot_to_look + len(FILMS_PAGE) + start + 1:
               spot_to_look + len(FILMS_PAGE) + html[spot_to_look + len(FILMS_PAGE):].find("<")]
    return int(num)


def getListOfFilmNames(html):
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
    # todo: rename item to film ig? idk dont really care too much
    for item in re.finditer(start_of_item, htmlListOfPosters):
        item_start = item.start() + htmlListOfPosters[item.start():].find("alt=\"") + 5
        item_end = htmlListOfPosters[item_start:].find("\"")
        list_of_films.append(htmlListOfPosters[item_start:item_start + item_end])

    return list_of_films


def getUrlsForFilms(html, list_of_films):
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


def getFilmsPageInformation(user):
    """
    Collects information regarding a users /films/ page to collect all the distinct films that a user has seen,
    compiles each film, with information (director, year, etc.) regarding each film into a single list

    :param user: the letterboxd user
    :return: a list of films the user has watched, and info relating to each film (director, year, etc.)
    """

    # oh noah theres a better way to parse this html ooohohsushs
    # yeah of course there is shut up idk what im doing let me be
    # - the voices

    # find list of films names and list of urls to ping
    # todo make this cleaner
    # todo consider breaking logic into separate method
    films_html = requests.get(BASE_URL + user + "/films/").text
    numFilmsPages = getNumberOfFilmsPages(films_html)
    film_list = getListOfFilmNames(films_html)
    url_list = getUrlsForFilms(films_html, film_list)
    for page in range(2, numFilmsPages + 1):
        films_html = requests.get(BASE_URL + user + FILMS_PAGE + str(page)).text
        new_films = getListOfFilmNames(films_html)
        film_list += new_films
        url_list += getUrlsForFilms(films_html, new_films)

    film_info = []
    for num in range(len(film_list)):
        # get film html
        html = requests.get(BASE_URL + url_list[num]).text

        # director
        dir_literal = "<a href=\"/director/"
        mod_html = html[html.find(dir_literal):]
        director = []
        for i in range(html.count(dir_literal)):
            cry = mod_html[mod_html.find(dir_literal)+1:] # 1 to offset the < in dir_literal
            mod_html = cry[21:2000]
            director.append(cry[cry.find(">") + 1:cry.find("<")])

        # year
        mod_html = html
        cry = mod_html[mod_html.find("/films/year/"):]
        year = cry[cry.find(">") + 1:cry.find("<")]

        # language
        mod_html = html
        language = []
        for i in range(html.count("/films/language/")):
            cry = mod_html[mod_html.find("/films/language/"):]
            mod_html = cry[21:2000]
            new_language = cry[cry.find(">") + 1:cry.find("<")]

            # prevent overlap of Primary and Spoken languages
            if new_language not in language:
                language.append(cry[cry.find(">") + 1:cry.find("<")])

        # country
        mod_html = html
        country = []
        for i in range(html.count("/films/country/")):
            cry = mod_html[mod_html.find("/films/country/"):]
            mod_html = cry[21:2000]
            country.append(cry[cry.find(">") + 1:cry.find("<")])

        # runtime
        mod_html = html[html.find("runTime: "):]
        runtime = mod_html[9:mod_html.find(" }"):]

        # average rating
        rating_literal = "\"Average rating\" /><meta name=\"twitter:data2\" content=\""
        mod_html = html[html.find(rating_literal):]
        avg_rating = mod_html[len(rating_literal):mod_html.find(" out of 5")]

        # create dict and return it
        # todo: put each chunk into indiv helper method, call when creating this map
        # todo: switch to appending individual items if we only want some? dont know if thats good or bad tho, just thot
        film = {
            "name": film_list[num],
            "director": director,
            "year": year, #todo make int? or leave as string
            "language": language,
            "country": country,
            "runtime": int(runtime),
            "avg_rating": float(avg_rating)
        }
        film_info.append(film)

    return film_info
