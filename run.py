import argparse
from htmlParsers.filmsScraper import getFilmsPageInformation
from fileWriters.csvWriter import filmsToCSV

desc_message = "letterboxd stats courtesy of me"

parser = argparse.ArgumentParser(description=desc_message)

# REQUIRED
parser.add_argument("--user", "-u", help="letterboxd username")

# Films or Diary
parser.add_argument("-f", help="collect data regarding distinct films logged", action="store_true")
parser.add_argument("-d", help="collect data regarding diary entries cataloged", action="store_true")

# Utility
parser.add_argument("-p", help="print all film data", action="store_true")
parser.add_argument("-c", help="write data to a .csv file", action="store_true")
parser.add_argument("-t", help="write data to a .txt file", action="store_true")
args = parser.parse_args()

if not (args.f and args.d):
    print("\nGathering letterboxd data, this may take a while (may take several minutes)\n")

    if args.f:
        info = getFilmsPageInformation(args.user)

    if args.d:
        print("placeholder")
        # info = getDiaryPageInformation(args.user)

    if args.p:
        for i in range(len(info)):
            print(info[i])

    if args.c:
        filmsToCSV(args.user, info)

    if args.t:
        print("placeholder")
        # filmstoTXT(args.user, info)
else:
    print("\nPlease don't request both film and diary data at once, it makes me sad\n")
