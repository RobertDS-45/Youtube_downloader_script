import os
from typing import Any, cast

from yt_dlp import YoutubeDL

VIDEO_URL = "https://www.youtube.com/watch?v=CXq0CB47nkY"
USB_OUTPUT_PATH = "E:/youtube"


def build_ydl_opts(output_dir: str) -> dict[str, Any]:
    """Use a cookie file when available and keep the request realistic for YouTube."""
    cookie_file = os.environ.get("YOUTUBE_COOKIE_FILE")

    opts: dict[str, Any] = {
        "format": "bv*+ba/b",
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "noplaylist": True,
        "progress_hooks": [],
        "retries": 10,
        "fragment_retries": 10,
        "extractor_args": {"youtube": ["player_client=android"]},
        "http_headers": {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/126.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        },
        "nocheckcertificate": True,
        "ignoreerrors": False,
    }

    if cookie_file and os.path.exists(cookie_file):
        opts["cookies"] = cookie_file

    return opts


def download_video(video_url: str, output_dir: str = USB_OUTPUT_PATH) -> None:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    ydl_opts = build_ydl_opts(output_dir)

    print(f"Starting download directly to USB path: {output_dir}...")
    if not ydl_opts.get("cookies"):
        print("No cookie file was provided. YouTube is likely rate-limiting the request.")
        print("Export a valid YouTube cookie file from your browser and set YOUTUBE_COOKIE_FILE before rerunning.")

    try:
        with YoutubeDL(cast(Any, ydl_opts)) as ydl:
            ydl.download([video_url])
        print("\n🎉 Success! The video was safely downloaded to your USB.")
    except Exception as exc:  # pragma: no cover - runtime branch
        message = str(exc)
        lower_message = message.lower()
        if (
            "sign in to confirm you’re not a bot" in lower_message
            or "sign in to confirm you're not a bot" in lower_message
            or "429" in lower_message
            or "too many requests" in lower_message
        ):
            print("\n⚠️ YouTube is blocking the request as a bot-check or rate-limit response.")
            print("Fix: export your browser cookies to a file and set YOUTUBE_COOKIE_FILE to that path before running the script.")
            print("Example: set YOUTUBE_COOKIE_FILE=C:/path/to/youtube_cookies.txt")
        else:
            print(f"\n❌ An error occurred: {exc}")
        raise


if __name__ == "__main__":
    download_video(VIDEO_URL)
