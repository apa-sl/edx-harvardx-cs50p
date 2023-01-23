# CS50p Problem Set 6: CS50 P-Shirt
# https://cs50.harvard.edu/python/2022/psets/6/shirt/
#
# Goal: create image with overlay cs50 t-shirt on top of person photo using Pillow (PIL) module
# Author: Adam Labedzki 2023-01-16

import sys
import os
from PIL import Image, ImageOps


def main():

    suffixes = ".png", ".jpg", "jpeg"
    # for refference how to get file extension with os.path.splitext:
    # _ = os.path.splitext(sys.argv[1])
    # input_file_ext = _[1]
    # check if there are 2 arguments provided
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # check if img files have been passed as args
    elif not sys.argv[1].endswith(suffixes) or not sys.argv[2].endswith(suffixes):
        sys.exit("Not an image file")
    # check if input & ouput file formats are the same
    elif sys.argv[1][-4:] != sys.argv[2][-4:]:
        sys.exit("Input and output have different extensions")

    # check if file exists
    try:
        with open(sys.argv[1]) as input_file:
            pass
    except FileNotFoundError:
        sys.exit("File does not exits")
    else:
        # create final image with t-shirt overlayed on the photo
        add_shirt(sys.argv[1], sys.argv[2])


def add_shirt(input_image, output_image):
    # open needed image files
    shirt = Image.open("shirt.png")
    photo = Image.open(input_image)

    # resize input image to fit overlay image
    x, y = shirt.size
    photo = ImageOps.fit(photo, (x, y))

    # place shirt on top of the photo
    photo.paste(shirt, shirt) # 1st param: shirt as overlay image, 2nd param: shirt as mask
    shirt.close() # not needed anymore, free memory
    photo.save(output_image)
    photo.close() # not needed anymore, free memory
    return 1


if __name__ == "__main__":
    main()