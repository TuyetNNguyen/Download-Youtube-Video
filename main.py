import sys
from sys import argv
from pytube import YouTube

def download(cla):
    #print command-line argument
    print(cla)
    url = cla[1]

    # Create a YouTube object
    yt = YouTube(url)

    # Access properties of the YouTube object
    print("Video Title:", yt.title)
    print("Video Duration:", yt.length)

    # Download the video
    yt.streams.get_highest_resolution().download()
    print("Downloaded successfully")
if __name__ == "__main__":
    download(argv)
