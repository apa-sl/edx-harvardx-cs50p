# CS50p Problem Set 1: File Extensions
# https://cs50.harvard.edu/python/2022/psets/1/extensions/
#
# Goal: prompt the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes from the list, in other case optup common default.
# Author: Adam Labedzki 2023-01-06

# dict with known file types
filetypes = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}


def main():
    # get the filename from the user, remove all left/right leading spaces and convert to lowercase
    filename = input("What is the file name? ").strip().lower()

    # call function checking the filetype and print the result
    print(check_filetype(filename))

def check_filetype(filename):
    # get the file type by splitting filename from the right by "." separator only once. We will get a list of strings
    filetype = filename.rsplit(".", 1)

    # check if provided filename has an extension:
    if "." in filename:
        # check if extracted filetype is in the dict or not:
        if filetype[1] not in filetypes:
            return "application/octet-stream"
        else:
            return filetypes[filetype[1]]
    else:
        return "application/octet-stream"


main()