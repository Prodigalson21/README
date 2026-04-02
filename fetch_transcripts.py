#!/usr/bin/env python3
"""
Free YouTube transcript fetcher using yt-dlp (no API keys required)
Run this script to download transcripts from your experts' recent videos.
"""

import subprocess
import os
import sys
import time
from datetime import datetime

# ===== CONFIGURATION =====
# Each expert: (name, channel_url, max_videos)
EXPERTS = [
    ("Kevin_Indig", "https://www.youtube.com/@kevinindig", 3),
    ("Kyle_Roof", "https://www.youtube.com/@KyleRoof", 5),
    ("Aleyda_Solis", "https://www.youtube.com/@aleydasolis", 3),
    ("Nathan_Gotch", "https://www.youtube.com/@NathanGotch", 5),
    ("Surfer_SEO", "https://www.youtube.com/@SurferSEO", 3),
    ("Clearscope", "https://www.youtube.com/@clearscope", 3),
    ("Lily_Ray", "https://www.youtube.com/@lilyraynyc", 2),  # if available
    ("Ross_Hudgens", "https://www.youtube.com/@SiegeMedia", 2),
]

OUTPUT_DIR = "research/youtube-transcripts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ===== FUNCTION: Get video URLs from channel using yt-dlp =====
def get_channel_videos(channel_url, max_videos):
    """Extract video URLs from a YouTube channel using yt-dlp."""
    cmd = [
        "yt-dlp",
        "--flat-playlist",
        "--print", "url",
        "--max-downloads", str(max_videos),
        channel_url
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error fetching videos from {channel_url}: {result.stderr}")
        return []
    urls = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return urls[:max_videos]

# ===== FUNCTION: Download transcript for a video =====
def download_transcript(video_url, expert_name, output_dir):
    """Download transcript as .txt file using yt-dlp."""
    cmd = [
        "yt-dlp",
        "--write-subs",
        "--sub-lang", "en",
        "--skip-download",
        "--convert-subs", "txt",
        "--output", f"{output_dir}/{expert_name}_%(title).50s_%(id)s.%(ext)s",
        video_url
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to download transcript for {video_url}: {e.stderr}")
        return False

# ===== MAIN =====
def main():
    print(f"Starting transcript fetch at {datetime.now()}")
    print(f"Output directory: {OUTPUT_DIR}")
    
    for expert_name, channel_url, max_videos in EXPERTS:
        print(f"\n--- Processing {expert_name} ---")
        video_urls = get_channel_videos(channel_url, max_videos)
        print(f"Found {len(video_urls)} videos")
        
        for idx, url in enumerate(video_urls, 1):
            print(f"  [{idx}/{len(video_urls)}] Downloading transcript from {url}")
            success = download_transcript(url, expert_name, OUTPUT_DIR)
            if success:
                print("    ✓ Done")
            else:
                print("    ✗ Failed")
            time.sleep(1)  # Be polite to YouTube
    
    print(f"\nAll done. Transcripts saved in {OUTPUT_DIR}")

if __name__ == "__main__":
    # Check if yt-dlp is installed
    try:
        subprocess.run(["yt-dlp", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: yt-dlp is not installed. Run: pip install yt-dlp")
        sys.exit(1)
    
    main()
