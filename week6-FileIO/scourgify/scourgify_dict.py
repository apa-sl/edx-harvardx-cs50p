# CS50p Problem Set 6: Scourgify
# https://cs50.harvard.edu/python/2022/psets/6/scourgify/
#
# Goal: data cleaning by splitting 2 values from 1 column in csv into separate columns
# Author: Adam Labedzki 2023-01-15

import sys
import csv


def main():
    # check if there are 2 arguments provided
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # check if there are csv input & output file names as arguments
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")
    # check if file exists

    try:
        # open csv & save all lines as a table list
        with open(sys.argv[1], "r") as input_file:
            reader = csv.DictReader(input_file)
            # create output csv file
            with open(sys.argv[2], "w") as output_file:
                # construct & write header for the output file
                writer_header = ["first", "last", "house"]
                writer = csv.DictWriter(output_file, writer_header)
                writer.writeheader()
                # construct rows with separated columns and put them into output file
                person = {}
                for row in reader:
                    last, first = row["name"].split(", ")
                    person["first"] = first
                    person["last"] = last
                    person["house"] = row["house"]

                    writer.writerow(person)

    except FileNotFoundError:
        sys.exit("File does not exits")


if __name__ == "__main__":
    main()