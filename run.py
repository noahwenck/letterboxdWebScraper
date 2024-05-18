import argparse
from htmlParser import getFilmInformation

desc_message = "letterboxd stats courtesy of me"

parser = argparse.ArgumentParser(description=desc_message)
parser.add_argument("--user", "-u", help="letterboxd username")
parser.add_argument("--print", "-p", help="print all film data", action="store_true")
args = parser.parse_args()

film_info = getFilmInformation(args.user)

if args.print:
    for i in range(len(film_info)):
        print(film_info[i])
