# CS50p Problem Set 7: Working 9 to 5
# https://cs50.harvard.edu/python/2022/psets/7/working/
#
# Goal: program converts inputed 12-hours format (e.g. 9 AM - 5 PM, 9:00 AM - 5 PM) working time to 24-hours format (9:00 - 17:00)
# Author: Adam Labedzki 2023-01-18

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # check if input is valid using regex
    try:
        if matches := re.search(r"^((?:[1-9]|1[0-2])(?::[0-5]?[0-9]?)?) ([AP]M) to ((?:[1-9]|1[0-2])(?::[0-5]?[0-9]?)?) ([AP]M)$",s):
            pass
        else:
            raise ValueError
    except ValueError:
        raise ValueError
        #sys.exit("Wrong input (expected: HH(:MM) A/PM to HH(:MM) A/PM)")
    # continue with valid input
    else:
        # store input working hours in a dict
        input_time = {}
        input_time["start_h"] = matches.group(1)
        input_time["start_tag"] = matches.group(2)
        input_time["end_h"] = matches.group(3)
        input_time["end_tag"] = matches.group(4)
        # check if minutes have been provided and create minutes values for output time format
        # for starting time
        if matches := re.search(r"^([0-9]{1,2}):([0-5][0-9])$", input_time["start_h"]):
            input_time["start_h"] = matches.group(1)
            input_time["start_m"] = matches.group(2)
        else:
            input_time["start_m"] = "00"
        # for ending time
        if matches := re.search(r"^([0-9]{1,2}):([0-5][0-9])$", input_time["end_h"]):
            input_time["end_h"] = matches.group(1)
            input_time["end_m"] = matches.group(2)
        else:
            input_time["end_m"] = "00"

        # construct output time in 24h format
        output_time = {}
        # construct starting hour
        if input_time["start_tag"] == "AM":
            if input_time["start_h"] == "12":
                output_time["start_h"] = "00"
            else:
                output_time["start_h"] = f"{int(input_time['start_h']):02}"
        else:
            if input_time["start_h"] == "12":
                output_time["start_h"] = str(input_time["start_h"])
            else:
                output_time["start_h"] = str(int(input_time['start_h'])+12)
        output_time["start_m"] = input_time["start_m"]

        # construct end hour
        if input_time["end_tag"] == "AM":
            if input_time["end_h"] == "12":
                output_time["start_h"] = "00"
            else:
                output_time["end_h"] = f"{int(input_time['end_h']):02}"
        else:
            if input_time["end_h"] == "12":
                output_time["end_h"] = str(input_time["end_h"])
            else:
                output_time["end_h"] = str(int(input_time['end_h'])+12)
        output_time["end_m"] = input_time["end_m"]

        return f"{output_time['start_h']}:{output_time['start_m']} to {output_time['end_h']}:{output_time['end_m']}"


if __name__ == "__main__":
    main()