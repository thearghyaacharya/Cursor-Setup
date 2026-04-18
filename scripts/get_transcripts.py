"""
YouTube Transcript Collector
Usage: python get_transcripts.py
Saves transcripts as .md files organized by expert folder.
Requires: pip install yt-dlp
"""

import subprocess
import os
import json
import re

# ── TARGET VIDEOS ──────────────────────────────────────────────────────────────
# Add or remove videos here. Format: ("expert-folder-name", "YouTube URL", "Short title")

VIDEOS = [
    # Jack Reamer
    ("jack-reamer", "https://www.youtube.com/watch?v=8tNM1CsmDWo", "best-linkedin-cold-dm-strategy-2025"),
    ("jack-reamer", "https://www.youtube.com/watch?v=4kdPAhSNkUQ", "linkedin-outreach-strategy-hormozi"),

    # Alex Hormozi
    ("alex-hormozi", "https://www.youtube.com/watch?v=cU7nYFnQNSA", "100m-cold-outreach-masterclass"),
    ("alex-hormozi", "https://www.youtube.com/watch?v=bako2wHj5Bo", "how-cold-email-saved-my-business"),

    # Jay Feldman
    ("jay-feldman", "https://www.youtube.com/watch?v=ILK_opONAUg", "cold-email-mastery-next-level-tactics"),

    # Jeremy Chatelaine / QuickMail
    ("jeremy-chatelaine", "https://www.youtube.com/watch?v=8gBcbQcNvJo", "cold-email-outreach-masterclass"),
]

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "research", "youtube-transcripts")


def sanitize(text):
    """Remove timestamps and clean up raw subtitle text."""
    # Remove VTT/SRT timestamp lines
    text = re.sub(r'\d{2}:\d{2}:\d{2}[.,]\d{3} --> \d{2}:\d{2}:\d{2}[.,]\d{3}', '', text)
    text = re.sub(r'^\d+$', '', text, flags=re.MULTILINE)
    # Remove WEBVTT header
    text = re.sub(r'WEBVTT.*?\n', '', text)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Collapse multiple blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def get_video_info(url):
    """Fetch video title and channel name."""
    try:
        result = subprocess.run(
            ["yt-dlp", "--dump-json", "--no-playlist", url],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            return data.get("title", "Unknown Title"), data.get("uploader", "Unknown Channel")
    except Exception:
        pass
    return "Unknown Title", "Unknown Channel"


def download_transcript(url):
    """Download auto-generated subtitles using yt-dlp."""
    try:
        result = subprocess.run(
            [
                "yt-dlp",
                "--write-auto-sub",
                "--sub-lang", "en",
                "--sub-format", "vtt",
                "--skip-download",
                "--output", "/tmp/yt_transcript_%(id)s.%(ext)s",
                url
            ],
            capture_output=True, text=True, timeout=60
        )
        # Find the downloaded file
        import glob
        files = glob.glob("/tmp/yt_transcript_*.vtt")
        if files:
            with open(files[0], "r", encoding="utf-8") as f:
                raw = f.read()
            os.remove(files[0])
            return sanitize(raw)
    except Exception as e:
        print(f"  yt-dlp error: {e}")
    return None


def save_transcript(expert_folder, filename, url, title, channel, transcript):
    """Save transcript as a clean markdown file."""
    folder = os.path.join(BASE_DIR, expert_folder)
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, f"{filename}.md")

    content = f"""# {title}

**Channel:** {channel}  
**URL:** {url}  
**Collected:** April 2026  

---

## Transcript

{transcript}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Saved: {filepath}")


def main():
    # Check yt-dlp is installed
    check = subprocess.run(["yt-dlp", "--version"], capture_output=True, text=True)
    if check.returncode != 0:
        print("yt-dlp not found. Run: pip install yt-dlp")
        return

    print(f"yt-dlp version: {check.stdout.strip()}\n")
    print(f"Processing {len(VIDEOS)} videos...\n")

    success, failed = 0, []

    for expert, url, filename in VIDEOS:
        print(f"[{expert}] {filename}")
        print(f"  URL: {url}")

        title, channel = get_video_info(url)
        print(f"  Title: {title}")

        transcript = download_transcript(url)

        if transcript and len(transcript) > 200:
            save_transcript(expert, filename, url, title, channel, transcript)
            success += 1
        else:
            print(f"  FAILED — no transcript available (video may have no captions)")
            failed.append((expert, url, filename))

        print()

    print("─" * 50)
    print(f"Done. {success}/{len(VIDEOS)} transcripts collected.")
    if failed:
        print(f"\nFailed ({len(failed)}):")
        for expert, url, fname in failed:
            print(f"  [{expert}] {fname} — {url}")


if __name__ == "__main__":
    main()
