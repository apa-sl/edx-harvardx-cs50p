# CS50p Problem Set 7: Watch on YouTube
# https://cs50.harvard.edu/python/2022/psets/7/watch/
#
# Goal: convert provided HTML embedded code for YT video & generate YT shortlink to the video from the embedded code
# Author: Adam Labedzki 2023-01-18

import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    """ takes in HTML iframe code and looks for youtube video link in it and returns short YT link """
    # search for src param and extract url from it
    if url := re.search(r"src=[\"']([\w:\/\.]+)[\"']", s):
        url = url.group(1)

        # check if it is an youtube link
        if yt_link := re.search(r"youtube", url):
            # extract video ID (alwyays 11 alfanum chars)
            yt_id = re.search(r"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]{11})", url)
            yt_id = yt_id.group(1)
            return "https://youtu.be/" + yt_id
        else:
            return None

    else:
        return None


if __name__ == "__main__":
    main()