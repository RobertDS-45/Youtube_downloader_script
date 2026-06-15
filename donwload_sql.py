import os
from typing import Any, cast
from yt_dlp import YoutubeDL

# 1. Place your target YouTube video or playlist link inside these quotes
video_url = "insertyour_url here" 

usb_output_path = "E:/msql totorial"

if not os.path.exists(usb_output_path):
    os.makedirs(usb_output_path)

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': os.path.join(usb_output_path, '%(playlist_index)s - %(title)s.%(ext)s'),
    'noplaylist': False,
    # Fixed typo here: added the 's' to progress_hooks
    'progress_hooks': [], 
    'ignoreerrors': True,
}

print(f"Starting download directly to USB path: {usb_output_path}...")
try:
    with YoutubeDL(cast(Any,ydl_opts)) as ydl:
        ydl.download([video_url])
    print("\n🎉 Success! The playlist has been safely downloaded to your USB.")
except Exception as e:
    print(f"\n❌ An error occurred: {e}")