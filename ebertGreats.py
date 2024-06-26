import argparse
from htmlParsers.ebertGreatsScraper import get_roger_ebert_great_movies
from fileWriters.csvWriter import write_to_csv
from fileWriters.txtWriter import write_to_txt

desc_message = "Collect info from Roger Ebert's Great Movies list to a .csv to .txt file " \
               "(note: this can only access non-private information)"

parser = argparse.ArgumentParser(description=desc_message)

# Utility Actions
parser.add_argument("--print", "-p", help="print data to console", action="store_true")
parser.add_argument("--csv", "-c", help="write data to a .csv file", action="store_true")
parser.add_argument("--txt", "-t", help="write data to a .txt file", action="store_true")
args = parser.parse_args()

print("\nGathering letterboxd data, this may take a while (up to several minutes)\n")

info = get_roger_ebert_great_movies()
content = "RogerEbertGreatMovies"

if args.print:
    print("Printing: " + content + "\n")
    print(*info, sep="\n")
    print("\n")

if args.csv:
    write_to_csv(info, content) #todo: add bool for date (this list won't ever change), is this worth for all of 2 lists that won't change?

if args.txt:
    write_to_txt(info, content)
