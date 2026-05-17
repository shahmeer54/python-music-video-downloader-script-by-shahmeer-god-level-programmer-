import os
import tkinter as tk
from tkinter import ttk, messagebox

def download_song():
    song_name = entry.get()

    if not song_name:
        messagebox.showerror("Error", "Enter a song name")
        return

    download_folder = "songs"
    os.makedirs(download_folder, exist_ok=True)

    status_label.config(text=f"Downloading: {song_name}")
    progress.start()

    root.update()

    command = f'yt-dlp "ytsearch1:{song_name}" -x --audio-format mp3 -o "{download_folder}/%(title)s.%(ext)s"'
    
    os.system(command)

    progress.stop()
    status_label.config(text="Done!")

# bhen ki chot window setup
root = tk.Tk()
root.title("Song Downloader")
root.geometry("400x250")

# appp ka titleeeee ye bc 
title = tk.Label(root, text="YT Song Downloader", font=("Arial", 18))
title.pack(pady=10)

# data entry ka systemm yyyoooo
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# bharwa bhen ka lora download button 
download_btn = tk.Button(root, text="Download", command=download_song)
download_btn.pack(pady=10)




# ghatiya gando status 
status_label = tk.Label(root, text="")
status_label.pack(pady=10)
teee = tk.Label(root , text="check the download  folder  after the download :").pack()



root.mainloop()
