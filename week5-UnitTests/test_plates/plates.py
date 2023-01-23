# CS50p Problem Set 2: Vanity Plates
# https://cs50.harvard.edu/python/2022/psets/2/plates/
#
# Goal: prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not.
# Author: Adam Labedzki 2023-01-08


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(str):
    # min 2 max 6 chars
    if not proper_length(str):
        return False

    # 2 letters at start
    if not proper_start(str):
        return False

    # no periods, spaces, punctuation marks
    if not is_alphanumeric(str):
        return False

    # number only at the end, cannot start with 0 (eg. AA2222)
    if not digits_at_end(str):
        return False

    return True


def is_alphanumeric(str):
    # check if there is any non-letter/non-numeric char in the string
    if str.isalnum():
        return True
    return False


def proper_length(str):
    # check if string has length in range 2-6 chars
    if len(str) in range(2, 7):
        return True
    else:
        return False


def proper_start(str):
    # check if there are only letters as 2 first chars of the string
    if str[0:2].isalpha():
        return True
    else:
        return False


def digits_at_end(str):
    ending = None

    # iterate through string to find digit, if found copy ending of the string
    for i in range(len(str)):
        if (str[i].isnumeric()):
            ending = str[i:]
            break

    # if there is ending with digits
    if ending is not None:
        # check if ending starts with 0
        if ending[0] == "0":
            return False

        # iterate through ending and check are there only digits
        for _ in ending:
            if _.isnumeric() == False:
                return False
    return True


if __name__ == "__main__":
    main()