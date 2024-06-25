import argparse
from htmlParsers.filmsScraper import get_films_page_information
from fileWriters.csvWriter import write_to_csv
from fileWriters.txtWriter import write_to_txt

desc_message = "Collect info from letterboxd regarding films a user has watched to a .csv to .txt file " \
               "(note: this can only access non-private information)"

parser = argparse.ArgumentParser(description=desc_message)

# REQUIRED
parser.add_argument("user", help="letterboxd username")

# Utility Actions
parser.add_argument("--print", "-p", help="print data to console", action="store_true")
parser.add_argument("--csv", "-c", help="write data to a .csv file", action="store_true")
parser.add_argument("--txt", "-t", help="write data to a .txt file", action="store_true")
args = parser.parse_args()

print("\nGathering letterboxd data, this may take a while (up to several minutes)\n")

info = get_films_page_information(args.user)
content = args.user + "-Films"

if args.print:
    print("Printing: " + content + "\n")
    print(*info, sep="\n")
    print("\n")

if args.csv:
    write_to_csv(info, content)

if args.txt:
    write_to_txt(info, content)
