# CS50p Problem Set 0: Making Faces
# https://cs50.harvard.edu/python/2022/psets/0/faces/
#
# Goal: program asks for some input text and coverts all :) and :( to slightly smilling 🙂/frowning 🙁 faces
# Author: Adam Labedzki 2023-01-04

def main():
    text = convert(input("Write something with :) and/or :( : "))
    print(text)

def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text

main()