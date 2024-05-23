from datetime import date
import sys

sys.dont_write_bytecode = True


def writeToTXT(user, films, content):
    """
    Writes the known info regarding the films that user has seen to a txt file

    :param user: the letterboxd user
    :param films: a list of films the user has watched, and info relating to each film (director, year, etc.)
    :param content: string identifier of contents we are saving to file
    """

    filename = str(date.today()) + "-" + user + "-" + content + ".txt"

    print("Writing data to " + filename + "\n")

    with open(filename, "w", encoding="utf-8") as txtfile:
        for film in films:
            txtfile.write(str(film) + "\n")
