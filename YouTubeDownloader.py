from pytube import YouTube

link = input("Enter the link (Paste it from the clipboard): ")
yt = YouTube(link)

# Description of the video request:-
print("Title of the request: ",yt.title)
print("Number of views on the video is: ",yt.views)
print("Length of video is: ",yt.length,"seconds")
print("Video Description: ",yt.description)
print("Ratings: ",yt.rating)

# printing all the available streams...
print(yt.streams)
print(yt.streams.filter(progressive=True))

ys = yt.streams.get_highest_resolution()


# Uncomment any one...according to your preference.
# 
# 1.The code below will download our preferred stream and save it in the current working directory.
ys.download()
# 
# 2.The code below helps you to download in your preferred location.
# ys.download('location')

#....Downloading....
print("Download completed!!")
