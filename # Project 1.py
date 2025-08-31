# Project 1 
from tkinter import *
from pytube import YouTube # type: ignore
# Example code snippet
url = input("Enter the YouTube video URL: ")
yt = YouTube(url)
audio_stream = yt.streams.filter(only_audio=True).first()
output_path = "/path/to/output/folder"
filename = "audio.mp3"
audio_stream.download(output_path=output_path, filename=filename)
print(f"Audio downloaded to {output_path}/{filename}")
