import tkinter
import customtkinter
from pytube import YouTube, Playlist
import moviepy.editor as mpe
import os

vname = "clip.mp4"
aname = "audio.mp3"

def checkDownload():
    yt_url = link.get()
    if "list" in yt_url:
        playlistDownload()
    else:
        singleDownload()

def playlistDownload():
    print("Playlist Video Link")
    try:
        playlist_url = link.get()
        playlist = Playlist(playlist_url)
        for video in playlist.videos:
            title = video.title
            print(title)
            finishLabel.configure(text=f'Downloding {title}')
            video.streams.filter(subtype='mp4', res="720p").first().download()
            os.rename(video, vname)
            audio = video.streams.filter(only_audio=True).first().download()
            os.rename(audio, aname)

            video = mpe.VideoFileClip(vname)
            audio = mpe.AudioFileClip(aname)
            final = video.set_audio(audio)

            final.write_videofile(f'{title}.mp4')

            os.remove(vname)
            os.remove(aname)

            finishLabel.configure(text="Download Complete!")
    except:
        finishLabel.configure(text="Whoops Error! Make sure the link is correct.")
    print("I am done")


def singleDownload():
    print("Single Video Link")
    try:
        vi_url = link.get()
        video = YouTube(vi_url).streams.filter(subtype='mp4', res="720p").first().download()
        title = YouTube(vi_url).title
        finishLabel.configure(text=f'Downloding {title}')
        os.rename(video, vname)

        audio = YouTube(vi_url).streams.filter(only_audio=True).first().download()
        os.rename(audio, aname)

        video = mpe.VideoFileClip(vname)
        audio = mpe.AudioFileClip(aname)
        final = video.set_audio(audio)

        final.write_videofile(f'{title}.mp4')

        os.remove(vname)
        os.remove(aname)

        finishLabel.configure(text="Download Complete!")
    except:
        finishLabel.configure(text="Whoops Error! Make sure the link is correct.")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Playlist Downloader")

title = customtkinter.CTkLabel(app, text="Paste the playlist or video link below...")
title.pack(padx=10, pady=10)

url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url)
link.pack()

download = customtkinter.CTkButton(app, text="Download", command=checkDownload)
download.pack(padx=10, pady=10)

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

app.mainloop()