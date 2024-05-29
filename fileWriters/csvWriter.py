import csv
from datetime import date
import sys

sys.dont_write_bytecode = True


def write_to_csv(films, content):
    """
    Writes the known info regarding the films that user has seen to a csv file

    :param films: a list of films the user has watched, and info relating to each film (director, year, etc.)
    :param content: string identifier of contents we are saving to file
    """

    headers = films[0].keys()

    filename = str(date.today()) + "-" + content + ".csv"

    print("Writing data to " + filename + "\n")

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(films)
