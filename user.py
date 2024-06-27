import sys

sys.dont_write_bytecode = True

import argparse
from htmlParsers.diaryScraper import get_list_of_diary_entries
from htmlParsers.filmsScraper import get_films_page_information
from fileWriters.csvWriter import write_to_csv
from fileWriters.txtWriter import write_to_txt

desc_message = "Collect info from Letterboxd regarding films a user has interacted with to a .csv to .txt file.\n"\
               "Note: this can only access non-private information."

parser = argparse.ArgumentParser(description=desc_message, formatter_class=argparse.RawTextHelpFormatter)

# REQUIRED
#todo: add check for if user actually exists
parser.add_argument("user", help="Letterboxd username")
parser.add_argument("section",
                    help="the section of a user's profile to look at.",
                    choices=["films", "diary"])

# Utility Actions
parser.add_argument("-p", "--print", help="print data to console", action="store_true")
parser.add_argument("-c", "--csv", help="write data to a .csv file", action="store_true")
parser.add_argument("-t", "--txt", help="write data to a .txt file", action="store_true")
args = parser.parse_args()

print("\nGathering letterboxd data, this may take a while. (up to several minutes)\n")

match args.section:
    case "films":
        info = get_films_page_information(args.user)
        content = args.user + "-Films"
    case "diary":
        info = get_list_of_diary_entries(args.user)
        content = args.user + "-Diary"

if args.print:
    print("Printing: " + content + "\n")
    print(*info, sep="\n")
    print("\n")

if args.csv:
    write_to_csv(info, content)

if args.txt:
    write_to_txt(info, content)
