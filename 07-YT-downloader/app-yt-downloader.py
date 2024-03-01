# 1 installations of modules 
# 2 import libraries for the project 
from tkinter import *
from pytube import YouTube
# 3 create the API window 

root = Tk()
root.geometry("600x320")
root.resizable(0, 0)
root.config(bg="lightblue")
root.title("Youtube Video Downloader App")

# 4 create the link to entry widget
Label(root, text="Download YT video for free", font="Roboto  14 bold").place(x=100, y=20)
Label(root, text="Insert your link here", font="Roboto  14 bold", bg="blue", fg="white").place(x=126, y=50)
# entry widget 
videoLink = StringVar()
Entry(root, width=80, textvariable=videoLink).place(x=35, y=85)
# 5 create download function
def downloadVideo():
    yt = YouTube(videoLink.get())
    videoStream = yt.streams.first()
    videoStream.download("c:\\Users\\maki\\Desktop\\YT videos")
    Label(root, text="Download Completed", font="Roboto  14 bold", bg="green", fg="white").place(x=120, y=180)
# 6 create download button 
Button(root, text="Click to download", font="Roboto 16 bold", bg="red", padx=2, command=downloadVideo).place(x=180, y=120)

root.mainloop()
