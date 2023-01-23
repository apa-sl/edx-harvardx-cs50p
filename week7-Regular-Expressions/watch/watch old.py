# CS50p Problem Set 7: Watch on YouTube
# https://cs50.harvard.edu/python/2022/psets/7/watch/
#
# Goal: convert provided HTML embedded code for YT video & generate YT shortlink to the video from the embedded code
# Author: Adam Labedzki 2023-01-18

import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # remove iframe tags
    s = s[8:]
    s = s[:-10]
    # split params into list
    params = s.split()

    # look for parameter with the video link & extract video ID (always 11 alfanum chars)
    for i in range(len(params)):
        if re.search(r"^src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]{11})\"$", params[i]):
            video_url = params[i][-12:-1]
            # return string with short video url
            return "https://youtu.be/" + video_url
        else:
            return None


if __name__ == "__main__":
    main()