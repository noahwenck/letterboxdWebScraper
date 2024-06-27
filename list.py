import sys

sys.dont_write_bytecode = True

import argparse
from htmlParsers.listScraper import collect_films_from_list
from fileWriters.csvWriter import write_to_csv
from fileWriters.txtWriter import write_to_txt

desc_message = "Collect info from various notable Letterboxd lists to a .csv to .txt file."

parser = argparse.ArgumentParser(description=desc_message, formatter_class=argparse.RawTextHelpFormatter)

# REQUIRED
parser.add_argument("list",
                    help="The list to look at. Possible options:\n"
                         "Top 250 Narrative Features - narrative\n"
                         "Roger Ebert's Great Movies - ebert\n"
                         "Top 100 Animation - animation",
                    choices=["narrative", "ebert", "animation"])

# Utility Actions
parser.add_argument("-p", "--print", help="print data to console", action="store_true")
parser.add_argument("-c", "--csv", help="write data to a .csv file", action="store_true")
parser.add_argument("-t", "--txt", help="write data to a .txt file", action="store_true")
args = parser.parse_args()

print("\nGathering Letterboxd data, this may take a while (up to several minutes)\n")

# Collect List Info
info = collect_films_from_list(args.list)
match args.list:
    case "narrative":
        content = "Top-250-Narrative"
    case "ebert":
        content = "Roger-Ebert-Great-Movies"
    case "animation":
        content = "Top-100-Animation"

# Utility
if args.print:
    print("Printing: " + content + "\n")
    print(*info, sep="\n")
    print("\n")

if args.csv:
    write_to_csv(info, content)

if args.txt:
    write_to_txt(info, content)
