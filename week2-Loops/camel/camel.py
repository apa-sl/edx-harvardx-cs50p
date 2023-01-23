# CS50p Problem Set 2: camelCase
# https://cs50.harvard.edu/python/2022/psets/2/camel/
#
# Goal: prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
# Author: Adam Labedzki 2023-01-08

def main():
    cameltext = input("Please enter a camelCase name: ")
    snaketext = camel_to_snake(cameltext)
    return print(snaketext)


def camel_to_snake(string):
    # let's iterate through the provided camelCase string
    for i in range(len(string)):
        # if there is an upper char
        if string[i].isupper():
            # let's overwrite the string while adding "_" char and lower case char in place of detected upper case char
            string = string[:i] + "_" + string[i].lower() + string[i+1:]
    return string


main()