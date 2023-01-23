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
        table = []
        with open(sys.argv[1], "r") as input_file:
            reader = csv.reader(input_file)
            # remove header row in the reader and park it in separate variable
            _ = next(reader)
            with open(sys.argv[2], "w") as output_file:
                # add header to the output file
                writer_header = ["first", "last", "house"]
                writer = csv.writer(output_file)
                writer.writerow(writer_header)
                # construct rows with separated columns and put them into output file
                for row in reader:
                    final_row = row[0].split(", ")
                    # switch row list index 0 value with index 1 value to stick to the proper columns order (first, last)
                    _ = final_row[0]
                    __ = final_row[1]
                    final_row[0] = __
                    final_row[1] = _
                    final_row.append(row[1])

                    writer.writerow(final_row)

    except FileNotFoundError:
        sys.exit("File does not exits")


if __name__ == "__main__":
    main()