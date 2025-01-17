import ast
import base64
from enum import Enum
from functools import lru_cache
import re
import requests
import unicodedata

BASE_URL = "https://letterboxd.com/"


class DataType(Enum):
    BARE = 0  # Basic data
    NODA = 1  # Data for Noda - includes poster
    FULL = 2  # All data I can grab for now - includes cast and crew


@lru_cache(maxsize=None)
def get_film_info(url, datatype):
    """
    Returns a dict of info regarding a film (excluding its name)

    :param datatype: Type of data to collect (and for what purpose)
    :param url: url extension to ping the film's distinct page
    :return: dict of film information
    """

    html = requests.get(BASE_URL + url).text

    info = {
        "Director": get_director(html),
        "Year": get_year(html),
        "Primary Language": get_primary_language(html),
        "Spoken Language": get_spoken_languages(html),
        "Country": get_country(html),
        "Runtime": get_runtime(html),
        "Average Rating": get_average_rating(html),
        "Genre": get_genre(html),
        "Studio": get_studio(html)
    }
    if datatype == DataType.NODA:
        info.update({
            "Base64 Poster": get_base64_poster(html)
        })
    elif datatype == DataType.FULL:
        info.update({
            "Cast": get_cast(html),
            "Crew": get_crew(html)
        })
    return info


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
    try:
        return int(mod_html[mod_html.find(">") + 1:mod_html.find("<")])
    except:
        # Film has not been released yet, or for whatever reason there is no year listed.
        return None


def get_primary_language(html):
    """
    Finds the primary language of a film

    :param html: html of a films homepage
    :return: primary language
    """

    mod_html = html[html.find("/films/language/"):]
    primary_language = mod_html[mod_html.find(">") + 1:mod_html.find("<")]
    primary_language = unicodedata.normalize('NFKD', primary_language)
    return primary_language


def get_spoken_languages(html):
    """
    Finds the spoken language(s) of a film

    :param html: html of a films homepage
    :return: list of spoken languages
    """
    mod_html = html
    spoken_languages = []
    for i in range(html.count("/films/language/")):
        cry = mod_html[mod_html.find("/films/language/"):]
        mod_html = cry[21:2000]
        new_language = cry[cry.find(">") + 1:cry.find("<")]
        new_language = unicodedata.normalize('NFKD', new_language)

        # prevent overlap of Primary and Spoken languages (Primary isn't appended twice)
        if new_language not in spoken_languages:
            spoken_languages.append(new_language)

    return spoken_languages


def get_country(html):
    """
    Finds the country/countries of a film

    :param html: html of a films homepage
    :return: list of country or countries
    """

    mod_html = html
    country = []
    for _ in range(html.count("/films/country/")):
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
    new_runtime_lit = "text-link text-footer\">\n\t\t\t\t\t\n\t\t\t\t\t"

    mod_html = html[html.find(new_runtime_lit):]
    try:
        return int(mod_html[len(new_runtime_lit):mod_html.find("&nbsp;min"):].replace(',', ''))
    except ValueError:
        return None  # In case no runtime is listed (ref. Black '67)


def get_average_rating(html):
    """
    Finds the average rating of a film

    :param html: html of a films homepage
    :return: average rating of a film (float)
    """

    rating_literal = "\"Average rating\" /><meta name=\"twitter:data2\" content=\""
    mod_html = html[html.find(rating_literal):]
    rating = mod_html[len(rating_literal):mod_html.find(" out of 5")]
    if rating == "":
        return float(-1)
    else:
        return float(rating)


def get_genre(html):
    """
    Finds the genre(s) of a film

    :param html: html of a films homepage
    :return: list of genre(s)
    """

    if html.find("genre\":") == -1:
        return None

    mod_html = html[html.find("genre\":") + 7:]
    if mod_html.find(",\"dateModified\":") != -1:
        genre = mod_html[:mod_html.find(",\"dateModified\":")]
        return ast.literal_eval(genre)
    else:
        genre = mod_html[:mod_html.find(",\"@")]
        return ast.literal_eval(genre)


def get_studio(html):
    """
    Finds the studio(s) of a film

    :param html: html of a films homepage
    :return: list of studio(s)
    """

    studio_lit = "text-slug\">"

    mod_html = html[html.find("Studio"):]
    mod_html = mod_html[:mod_html.find("</div>")]  # section off from rest of lists
    studios = []
    for studio_entry in re.finditer(studio_lit, mod_html):
        studio = mod_html[studio_entry.start() + len(studio_lit):]
        studio = studio[:studio.find("</a>")]
        if studio not in studios:   # prevent duplicates of studios (ref. Senna)
            studios.append(fix_html_characters(studio))
    return studios


def get_cast(html):
    """
    Finds the cast of a film

    :param html: html of a films homepage
    :return: dict of cast, and their roles
    """

    mod_html = html
    cast = {}
    for i in range(html.count("a title=\"")):
        crew_member_start = mod_html[mod_html.find("a title=\"") + 9:]
        role = crew_member_start[:crew_member_start.find("\"")]
        person = crew_member_start[crew_member_start.find(">") + 1:crew_member_start.find("<")]
        mod_html = crew_member_start[10:]
        cast[fix_html_characters(person)] = fix_html_characters(role)
    return cast


def get_crew(html):
    """
    Finds the crew (excluding the director) of a film

    :param html: html of a films homepage
    :return: dict of crew, and their role
    """

    role_lit = "crewrole -full\">"
    member_lit = "text-slug\">"

    crew = {}
    # Iterate over crew members
    for role in re.finditer(role_lit, html):
        mod_html = html[role.start() + len(role_lit):]
        mod_html = mod_html[:mod_html.find("</div")]  # section off html so that we don't grab everyone below
        crew_role = mod_html[:mod_html.find("</")]
        if crew_role == "Director":
            continue  # ugly but works

        member_list = []
        for member in re.finditer(member_lit, mod_html):
            crew_member = mod_html[member.start() + len(member_lit):]
            crew_member = crew_member[:crew_member.find("</a>")]
            member_list.append(fix_html_characters(crew_member))

        crew[crew_role] = member_list
    return crew


def get_base64_poster(html):
    """
    Finds the base64 encoded poster of a film

    :param html: html of a films homepage
    :return: base64 encoded poster
    """
    start_of_link = "{\"image\":\""
    end_of_link = "\",\"@type\":\""
    poster_link = html[html.find(start_of_link) + len(start_of_link):html.find(end_of_link)]

    poster_data = requests.get(poster_link).content
    base64_poster = base64.b64encode(poster_data).decode('utf-8')
    return base64_poster


# todo: for maximum data can grab alt titles + nanogenres, but I'm not really interested in any of that for time being


def fix_html_characters(string):
    return string \
        .replace("&#039;", "\'") \
        .replace("&quot;", "\"") \
        .replace("&amp;", "&")
