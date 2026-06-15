# YouTube Video & Playlist Downloader to USB 🚀

A lightweight, automated Python script built to download high-quality YouTube videos or entire playlists directly to an external drive (like a USB flash drive). It is perfect for archiving educational courses, tutorials, or music for seamless offline viewing.

## Features
- **High Quality (1080p/HD):** Automatically fetches and merges the best video and audio streams using FFmpeg.
- **Playlist Sequencing:** Automatically numbers playlist videos (`1 - Title`, `2 - Title`) to maintain their chronological order on your USB.
- **Error Resilience:** Skips deleted or restricted videos automatically without crashing the entire download queue.
- **Smart Skip:** Skips already-downloaded files automatically to save time and bandwidth.

## Requirements

Before running the script, make sure you have the following installed:
- **Python 3.7+**
- **FFmpeg** (Required to merge high-quality video and audio formats into `.mp4`)

### 1. Installing FFmpeg (Windows)
The fastest way to install FFmpeg on Windows is via Windows Package Manager (`winget`). Open your PowerShell as Administrator and run:

```powershell
winget install Gyan.FFmpeg