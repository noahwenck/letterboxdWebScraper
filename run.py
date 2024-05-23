import argparse
from htmlParsers.diaryScraper import getListOfDiaryEntries
from htmlParsers.filmsScraper import getFilmsPageInformation
from fileWriters.csvWriter import writeToCSV
from fileWriters.txtWriter import writeToTXT

desc_message = "letterboxd stats courtesy of me"

parser = argparse.ArgumentParser(description=desc_message)

# REQUIRED
parser.add_argument("--user", "-u", help="letterboxd username")

# Films or Diary
parser.add_argument("-f", help="collect data regarding distinct films logged", action="store_true")
parser.add_argument("-d", help="collect data regarding diary entries cataloged", action="store_true")

# Utility
parser.add_argument("-p", help="print all film data to console", action="store_true")
parser.add_argument("-c", help="write data to a .csv file", action="store_true")
parser.add_argument("-t", help="write data to a .txt file", action="store_true")
args = parser.parse_args()

print("\nGathering letterboxd data, this may take a while (up to several minutes)\n")

if args.f:
    info = getFilmsPageInformation(args.user)

    if args.p:
        for i in range(len(info)):
            print(info[i])

    if args.c:
        writeToCSV(args.user, info, "Films")

    if args.t:
        writeToTXT(args.user, info, "Films")

if args.d:
    info = getListOfDiaryEntries(args.user)

    if args.p:
        for i in range(len(info)):
            print(info[i])

    if args.c:
        writeToCSV(args.user, info, "Diary")

    if args.t:
        writeToTXT(args.user, info, "Diary")


