import ast
import htmlParsers.filmParser as fp
import re
import requests

BASE_URL = "https://letterboxd.com/"
DIARY_PAGE = "/films/diary"


def get_list_of_diary_entries(user, everything):
    """
    Collects information on entries in a user's diary

    :param user: the letterboxd user
    :return: a list of diary entries
    """

    html = requests.get(BASE_URL + user + DIARY_PAGE).text

    list_of_entries = []
    for page in range(1, fp.get_num_pages(html) + 1):

        # Get new page since each only shows 50 entries
        if page != 1:
            html = requests.get(BASE_URL + user + DIARY_PAGE + "/page/" + str(page)).text

        # Iterate over diary entries on this page
        for entry in re.finditer("<tr class=\"diary-entry-row", html):

            # name
            entry_start = entry.start() + html[entry.start():].find("data-film-name=\"") + 16
            entry_end = html[entry_start:].find("\"")
            name = html[entry_start:entry_start + entry_end]

            # url
            area_to_look = html[:html.find("alt=\"" + name + "\"")]
            area_to_look = area_to_look[area_to_look.rfind("data-film-slug") + 16:]
            film_part = area_to_look[:area_to_look.find("\"")]
            url = "film/" + film_part + "/"

            # viewing date
            entry_start = entry.start() + html[entry.start():].find("data-viewing-date=\"") + 19
            entry_end = html[entry_start:].find("\"")
            viewing_date = html[entry_start:entry_start + entry_end]

            # review
            # todo: <p> as newline in the review
            film_html = requests.get(BASE_URL + user + "/" + url).text
            # review_lit = "<meta name=\"description\" content=\""
            review_lit = "<div><p>"
            if film_html.find(review_lit) > 0:
                film_html = film_html[len(review_lit) + film_html.find(review_lit):]
                review = film_html[:film_html.find("</p></div>")]
                review = fp.fix_html_characters(review)
            else:
                review = ""

            # rating
            # 0 indicates no rating
            entry_start = entry.start() + html[entry.start():].find("data-rating=\"") + 13
            entry_end = html[entry_start:].find("\"")
            rating = html[entry_start:entry_start + entry_end]

            # tags
            entry_start = entry.start() + html[entry.start():].find("data-tags=\'") + 11
            entry_end = html[entry_start:].find("\'")
            tags = html[entry_start:entry_start + entry_end]
            tags = ast.literal_eval(tags)
            tags = [tag.strip() for tag in tags]

            # rewatch
            entry_start = entry.start() + html[entry.start():].find("data-rewatch=\"") + 14
            entry_end = entry_start + html[entry_start:].find("\"")
            rewatch = html[entry_start:entry_end]
            # why is python like this, so sad
            if rewatch == "true":
                rewatch = True
            else:
                rewatch = False

            info = fp.get_film_info(url, everything)

            diary_entry = {
                "name": name,
                "viewing_date": viewing_date,
                "review": review,
                "rating": rating,
                "tags": tags,
                "rewatch": rewatch,
            }
            diary_entry.update(info)
            list_of_entries.append(diary_entry)

    return list_of_entries
