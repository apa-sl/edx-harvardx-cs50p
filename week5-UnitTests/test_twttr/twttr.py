# CS50p Problem Set 2: Just setting up my twttr
# https://cs50.harvard.edu/python/2022/psets/2/twttr/
#
# Goal: prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted
# Author: Adam Labedzki 2023-01-08


def main():
    # ask user for the text
    text = input("Input: ")
    output_text = shorten(text)
    return print(f"Output: {output_text}")


def shorten(word):
    output_string = ""
    # iterate through all chars in the provided string
    for i in range(len(word)):
        # if char is not a vowel, add it to the output string
        if word[i].lower() not in ["a", "e", "i", "o", "u"]:
            output_string += word[i]
    return output_string


if __name__ == "__main__":
    main()