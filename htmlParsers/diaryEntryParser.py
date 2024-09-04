import ast
import htmlParsers.filmParser as fp
import requests

BASE_URL = "https://letterboxd.com/"

def get_diary_entry(html, film, user, url):
    """
    Returns a dict of info regarding a diary entry (excluding its name)

    :param html: html contents of the overall diary page
    :param film: re iter of each film entry on a page
    :param user: the letterboxd user
    :param url: url extension to ping the film's distinct page
    :return: dict of diary entry info
    """
    return {
            "Viewing Date": get_viewing_date(html, film),
            "Review": get_review(user, url),
            "Rating": get_rating(html, film),
            "Tags": get_tags(html, film),
            "Rewatch": get_rewatch(html, film),
        }


def get_viewing_date(html, film):
    entry_start = film.start() + html[film.start():].find("data-viewing-date=\"") + 19
    entry_end = html[entry_start:].find("\"")
    return html[entry_start:entry_start + entry_end]


def get_review(user, url):
    # todo: <p> as newline in the review
    # todo: is there a way to not call another get request or need user + url?
    film_html = requests.get(BASE_URL + user + "/" + url).text
    # review_lit = "<meta name=\"description\" content=\""
    review_lit = "<div><p>"
    if film_html.find(review_lit) > 0:
        film_html = film_html[len(review_lit) + film_html.find(review_lit):]
        review = film_html[:film_html.find("</p></div>")]
        return fp.fix_html_characters(review)
    else:
        return ""


def get_rating(html, film):
    # 0 indicates no rating
    entry_start = film.start() + html[film.start():].find("data-rating=\"") + 13
    entry_end = html[entry_start:].find("\"")
    return html[entry_start:entry_start + entry_end]


def get_tags(html, film):
    entry_start = film.start() + html[film.start():].find("data-tags=\'") + 11
    entry_end = html[entry_start:].find("\'")
    tags = html[entry_start:entry_start + entry_end]
    tags = ast.literal_eval(tags)
    return [tag.strip() for tag in tags]

def get_rewatch(html, film):
    entry_start = film.start() + html[film.start():].find("data-rewatch=\"") + 14
    entry_end = entry_start + html[entry_start:].find("\"")
    rewatch = html[entry_start:entry_end]
    # todo: gotta be a better way for this
    if rewatch == "true":
        return True
    else:
        return False