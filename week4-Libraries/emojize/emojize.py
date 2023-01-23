# CS50p Problem Set 4: Emojize
# https://cs50.harvard.edu/python/2022/psets/4/emojize/
#
# Goal: Emojize inputed string converting :emojicode: into an actual emoji
# Author: Adam Labedzki 2023-01-11

from emoji import emojize

text = input("Input: ").strip()
print("Output:" + emojize(text))