import ssl
from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)

# Title of video
print("Title: ", yt.title)
# Number of views of video 
print("Number of views: ", yt.views)
# Length of video 
print("Length of video: ", yt.length, "seconds")
# Discription of video 
print("Discription:", yt.description)
# Rating
print("Ratings: ", yt.rating)
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!") 