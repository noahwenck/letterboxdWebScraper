import ast
import re
import requests

BASE_URL = "https://letterboxd.com/"
DIARY_PAGE = "/films/diary"

def getListOfDiaryEntries(user):
    """
    Collects information on entries in a user's diary

    :param user: the letterboxd user
    :return: a list of diary entries
    """

    html = requests.get(BASE_URL + user + DIARY_PAGE).text

    list_of_entries = []
    for page in range(1, getNumDiaryPages(html) + 1):

        # Get new page since each only shows 50 entries
        if page != 1:
            html = requests.get(BASE_URL + user + DIARY_PAGE + "/page/" + str(page)).text

        # Iterate over diary entries on this page
        for entry in re.finditer("<tr class=\"diary-entry-row", html):

            # name
            entry_start = entry.start() + html[entry.start():].find("data-film-name=\"") + 16
            entry_end = html[entry_start:].find("\"")
            name = html[entry_start:entry_start+entry_end]

            # viewing date
            entry_start = entry.start() + html[entry.start():].find("data-viewing-date=\"") + 19
            entry_end = html[entry_start:].find("\"")
            viewing_date = html[entry_start:entry_start + entry_end]

            # review
            review_lit = "data-review-text=\"" #todo do this for all for readability? or not idc
            entry_start = entry.start() + html[entry.start():].find(review_lit) + len(review_lit)
            entry_end = html[entry_start:].find("d")-3 # note that this does not really care for special characters
            review = html[entry_start:entry_start + entry_end]

            # rating
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

            diary_entry = {
                "name": name,
                "viewing_date": viewing_date,
                "review": review,
                "rating": rating,
                "tags": tags,
                "rewatch": rewatch
            }
            list_of_entries.append(diary_entry)

    return list_of_entries


def getNumDiaryPages(html):
    """
    Finds the number of diary pages we need to iterate through (each has 50 entries)

    :param html: html contents of diary page
    :return: number of diary pages a user has
    """

    num_start = html.rfind("diary/page/") + 11
    num_end = num_start + html[num_start:].find("/")
    return int(html[num_start:num_end])
