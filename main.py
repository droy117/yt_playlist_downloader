import tkinter
import customtkinter
from pytube import YouTube
import moviepy.editor as mpe
import os

vname = "clip.mp4"
aname = "audio.mp3"

def startDownload():
    try:
        yt_url = link.get()
        video = YouTube(yt_url).streams.filter(subtype='mp4', res="1080p").first().download()
        os.rename(video, vname)

        audio = YouTube(yt_url).streams.filter(only_audio=True).first().download()
        os.rename(audio, aname)

        video = mpe.VideoFileClip(vname)
        audio = mpe.AudioFileClip(aname)
        final = video.set_audio(audio)

        final.write_videofile("video.mp4")

        os.remove(vname)
        os.remove(aname)

        finishLabel.configure(text="Donwload Complete!")
    except:
        finishLabel.configure(text="Whoops Error! Make sure the link is correct.")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Playlist Downloader")

title = customtkinter.CTkLabel(app, text="Paste the playlist here...")
title.pack(padx=10, pady=10)

url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url)
link.pack()

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

app.mainloop()