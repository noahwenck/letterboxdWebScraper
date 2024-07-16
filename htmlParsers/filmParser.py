import ast
import re
import requests
import unicodedata

BASE_URL = "https://letterboxd.com/"


def get_num_pages(html):
    """
    Finds the number of pages that must be iterated over

    :param html: html contents of the page
    :return: number of pages
    """

    num_start = html.rfind("/page/") + 6
    num_end = num_start + html[num_start:].find("/")
    try:
        return int(html[num_start:num_end])
    except ValueError:
        return 1


def get_film_info(url, everything):
    """
    Returns a dict of info regarding a film (excluding its name)

    :param everything:
    :param url: url extension to ping the film's distinct page
    :return: dict of film information
    """

    html = requests.get(BASE_URL + url).text

    info = {
        "director": get_director(html),
        "year": get_year(html),
        "primary_language": get_primary_language(html),
        "spoken_language": get_spoken_languages(html),
        "country": get_country(html),
        "runtime": get_runtime(html),
        "avg_rating": get_average_rating(html),
        "genre": get_genre(html)
    }
    if everything:
        everything_info = {
            "cast": get_cast(html),
            "crew": get_crew(html)
        }
        info.update(everything_info)
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
    return int(mod_html[mod_html.find(">") + 1:mod_html.find("<")])


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
    rating = mod_html[len(rating_literal):mod_html.find(" out of 5")]
    if rating == "":
        return float(-1)
    else:
        return float(rating)


def get_studio(html):
    """
    Finds the studio(s) of a film

    :param html: html of a films homepage
    :return: list of studio(s)
    """

    studio_lit = "text-slug\">"

    mod_html = html[html.find("Studios"):]
    mod_html = mod_html[:mod_html.find("</div>")] # section off from rest of lists
    studios = []
    for studio_entry in re.finditer(studio_lit, mod_html):
        studio = mod_html[studio_entry.start() + len(studio_lit):]
        studio = studio[:studio.find("</a>")]
        studios.append(studio)
    return studios


def get_genre(html):
    """
    Finds the genre(s) of a film

    :param html: html of a films homepage
    :return: list of genre(s)
    """

    mod_html = html[html.find("genre\":")+7:]
    genre = mod_html[:mod_html.find(",\"@")]
    genre = ast.literal_eval(genre)
    return genre


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
        mod_html = mod_html[:mod_html.find("</div")] # section off html so that we don't grab everyone below
        crew_role = mod_html[:mod_html.find("</")]
        if crew_role == "Director":
            continue # ugly but works

        member_list = []
        for member in re.finditer(member_lit, mod_html):
            crew_member = mod_html[member.start() + len(member_lit):]
            crew_member = crew_member[:crew_member.find("</a>")]
            member_list.append(fix_html_characters(crew_member))

        crew[crew_role] = member_list
    return crew


#todo: for maximum data can grab alt titles + nanogenres, but I'm not really interested in any of that for time being


def fix_html_characters(string):
    return string\
        .replace("&#039;", "\'")\
        .replace("&quot;", "\"")\
        .replace("&amp;", "&")
