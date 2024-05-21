import csv
from datetime import date
import sys

sys.dont_write_bytecode = True


def filmsToCSV(user, films):
    """
    Writes the known info regarding the films that user has seen to a csv file

    :param user: the letterboxd user
    :param films: a list of films the user has watched, and info relating to each film (director, year, etc.)
    """

    headers = films[0].keys()

    filename = str(date.today()) + "-" + user + "-Films.csv"

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(films)
