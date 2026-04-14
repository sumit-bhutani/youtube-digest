#!/usr/bin/env python3
"""
YouTube Channel Monitor & Analyzer
Scans 25 channels, fetches latest video transcripts, analyzes with Claude, emails results.
"""

import os
import re
import sys
import json
import smtplib
import subprocess
import anthropic
import feedparser
import requests
from datetime import datetime, timezone, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi

# Load env vars from .env file manually
def load_env():
    env_path = Path(__file__).parent / '.env'
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, val = line.split('=', 1)
                    os.environ[key.strip()] = val.strip()

load_env()

ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
GMAIL_ADDRESS = os.environ.get('GMAIL_ADDRESS')
GMAIL_APP_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD')

CHANNELS_FILE = Path(__file__).parent / 'channels.txt'
CHANNEL_IDS_FILE = Path(__file__).parent / 'channel_ids.json'
ANALYSES_DIR = Path(__file__).parent / 'analyses'
PROCESSED_FILE = Path(__file__).parent / 'processed_videos.json'
ANALYSES_DIR.mkdir(exist_ok=True)

# Load pre-resolved channel IDs
with open(CHANNEL_IDS_FILE) as f:
    CHANNEL_IDS = json.load(f)

ANALYSIS_PROMPT = """You are a high-rigor YouTube research analyst.

Your task is to convert the YouTube video I provide into a structured, deeply analyzed research brief suitable for product leaders, AI builders, founders, and strategic operators.
Be analytical. Be structured. Avoid fluff. Distinguish facts from inference, and no hallucination.

STEP 1 — Transcript Handling
Retrieve and clean the transcript.
Organize content into logical 8–12 minute clusters.
Preserve timestamps.
Detect topic transitions.
Identify speakers where possible.
Note if transcript quality is weak or incomplete.

STEP 2 — Strategic Synthesis
A. Executive Summary (500–700 words)

Must include:
Core thesis
3–5 primary arguments
Quantitative insights (if present)
Key examples
Strategic implications
What changed vs conventional wisdom

Explicit separation of:
Facts stated
Speaker opinion
Your interpretation

B. Key Insights Expansion (10–15 Bullets)
Each bullet must:

Be insight-level (not descriptive recap)
Include timestamp reference
Explain why it matters
Include 1 implication
C. Deep Time-Coded Breakdown
For each major section:

Section Title
Timestamp Range
Include:

3–7 detailed statements explaining content
Important quotes (verbatim)
Examples discussed
Hidden assumptions (based on industry and market research)
Why this matters for product/strategy leaders (based on industry and market trends)
1 risk or limitation per section

STEP 3 — Structured Extraction Tables

1. Claims Table
| Claim | Evidence Presented | Evidence Type (Data / Anecdote / Opinion) | Strength | Commentary |

2. Metrics & Numbers Table
| Metric | Value | Context | Implication | Reliability |
3. Frameworks / Mental Models
| Framework | Explanation | Origin (if known, based on industry research) | Where It Applies | Limits |

4. Entities Mentioned
| Person / Company | Why Mentioned | Strategic Relevance | Competitive Angle |

STEP 4 — Critical Thinking Layer (based on industry and market research)
Gaps, Assumptions, or Weaknesses

Identify:

Overgeneralizations
Missing data
Logical leaps
Survivorship bias
Incentive misalignment
Unstated trade-offs
Contrarian or Non-Obvious Insights (3–5)
Must challenge surface interpretation.
Practitioner Playbook (5–10 Actions)

Concrete, execution-ready actions for:

PMs
Founders
AI builders
Strategy leaders
No vague advice.

STEP 5 — Strategic Reflection
"If I Were Building in This Space Today"
Provide:

5 execution-level moves
2 structural risks
1 asymmetric long-term bet
1 metric I would obsess over

OUTPUT REQUIREMENTS
Clean markdown
Clear section headers
Timestamp references
Tables formatted cleanly
Analytical tone
No filler language

Separate:
What was said
What is inferred
What is speculative
If uncertain → state uncertainty explicitly

Add a final section:

"Where This Video Is Directionally Wrong (If It Is)" (based on industry and market research)

Repeat STEP 2 through STEP 5 for every 30 minutes of video content.

Here is the transcript:

{transcript}

Video Title: {title}
Channel: {channel}
Video URL: {url}
Published: {published}
"""


HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}


def fetch_via_ytdlp(handle, cutoff_dt):
    """Fallback: fetch recent videos using yt-dlp when RSS is unavailable."""
    try:
        result = subprocess.run(
            [
                sys.executable, '-m', 'yt_dlp',
                '--playlist-end', '10', '--skip-download',
                '--print', '%(id)s|%(title)s|%(upload_date)s',
                f'https://www.youtube.com/@{handle}/videos',
            ],
            capture_output=True, text=True, timeout=60
        )
        cutoff_date = cutoff_dt.strftime('%Y%m%d')
        new_videos = []
        for line in result.stdout.strip().splitlines():
            parts = line.split('|', 2)
            if len(parts) != 3:
                continue
            video_id, title, upload_date = parts
            if not upload_date or upload_date == 'NA' or upload_date < cutoff_date:
                continue
            new_videos.append({
                'title': title,
                'url': f'https://www.youtube.com/watch?v={video_id}',
                'video_id': video_id,
                'published': f'{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}',
            })
        return new_videos
    except Exception as e:
        print(f"  yt-dlp error for {handle}: {e}")
        return []


def fetch_channel_latest_videos(channel_handle, cutoff_dt):
    """Fetch videos published after cutoff using YouTube RSS feeds, with yt-dlp fallback."""
    handle = channel_handle.lstrip('@')

    channel_id = CHANNEL_IDS.get(handle)
    if not channel_id:
        print(f"  No channel ID found for {handle}")
        return []

    rss_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    try:
        resp = requests.get(rss_url, headers=HEADERS, timeout=10)
        if resp.status_code != 200:
            print(f"  RSS feed returned {resp.status_code} for {handle}, trying yt-dlp...")
            return fetch_via_ytdlp(handle, cutoff_dt)

        feed = feedparser.parse(resp.content)
        new_videos = []
        for entry in feed.entries[:10]:
            published = entry.get('published_parsed')
            if not published:
                continue
            pub_dt = datetime(*published[:6], tzinfo=timezone.utc)
            if pub_dt > cutoff_dt:
                video_id = entry.get('yt_videoid', '')
                new_videos.append({
                    'title': entry.get('title', 'Unknown'),
                    'url': entry.get('link', ''),
                    'video_id': video_id,
                    'published': pub_dt.strftime('%Y-%m-%d'),
                })
        return new_videos
    except Exception as e:
        print(f"  Error fetching RSS for {handle}: {e}")
        print(f"  Trying yt-dlp...")
        return fetch_via_ytdlp(handle, cutoff_dt)


def load_processed_videos():
    """Load set of already-processed video IDs."""
    if PROCESSED_FILE.exists():
        with open(PROCESSED_FILE) as f:
            return set(json.load(f))
    return set()


def save_processed_video(video_id, processed_set):
    """Add video ID to processed set and persist."""
    processed_set.add(video_id)
    with open(PROCESSED_FILE, 'w') as f:
        json.dump(list(processed_set), f)


def fetch_transcript(video_id):
    """Fetch transcript for a YouTube video. Returns None if under 15 minutes."""
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)

        # Check duration — skip videos under 15 minutes
        if transcript and transcript[-1].start < 900:
            print(f"  Skipping — video is under 15 minutes")
            return None

        formatted = []
        for entry in transcript:
            minutes = int(entry.start // 60)
            seconds = int(entry.start % 60)
            timestamp = f"[{minutes:02d}:{seconds:02d}]"
            formatted.append(f"{timestamp} {entry.text}")

        return "\n".join(formatted)
    except Exception as e:
        print(f"  Transcript error: {type(e).__name__}: {e}")
        return None


def analyze_with_claude(transcript, title, channel, url, published):
    """Analyze transcript using Claude API."""
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    prompt = ANALYSIS_PROMPT.format(
        transcript=transcript,
        title=title,
        channel=channel,
        url=url,
        published=published
    )

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text


def save_analysis(channel, title, analysis, video_url, published_date):
    """Save analysis to markdown file."""
    safe_channel = re.sub(r'[^a-zA-Z0-9_-]', '_', channel)
    safe_title = re.sub(r'[^a-zA-Z0-9_-]', '_', title[:50])
    date_str = datetime.now().strftime('%Y-%m-%d')

    filename = f"{date_str}_{safe_channel}_{safe_title}.md"
    filepath = ANALYSES_DIR / filename

    header = f"""# {title}

**Channel:** {channel}
**URL:** {video_url}
**Published:** {published_date}
**Analyzed:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

"""

    with open(filepath, 'w') as f:
        f.write(header + analysis)

    return filepath


def send_email(analyses_results):
    """Send email digest with all analyses."""
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"YouTube Research Digest — {datetime.now().strftime('%B %d, %Y')}"
    msg['From'] = GMAIL_ADDRESS
    msg['To'] = GMAIL_ADDRESS

    body = f"# YouTube Research Digest\n\n"
    body += f"**Date:** {datetime.now().strftime('%B %d, %Y')}\n"
    body += f"**Videos analyzed:** {len(analyses_results)}\n\n"
    body += "---\n\n"

    for result in analyses_results:
        body += f"## [{result['channel']}] {result['title']}\n"
        body += f"**URL:** {result['url']}\n\n"
        body += result['analysis']
        body += "\n\n---\n\n"

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
            server.sendmail(GMAIL_ADDRESS, GMAIL_ADDRESS, msg.as_string())
        print(f"  Email sent to {GMAIL_ADDRESS}")
    except Exception as e:
        print(f"  Email error: {e}")


def main():
    print(f"\n{'='*60}")
    print(f"YouTube Channel Monitor — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*60}\n")

    with open(CHANNELS_FILE) as f:
        channels = [line.strip() for line in f if line.strip()]

    print(f"Scanning {len(channels)} channels...\n")

    cutoff = datetime.now(timezone.utc) - timedelta(hours=48)
    processed_videos = load_processed_videos()
    analyses_results = []

    for channel_handle in channels:
        print(f"Checking {channel_handle}...")

        new_videos = fetch_channel_latest_videos(channel_handle, cutoff)

        if not new_videos:
            print(f"  No new videos in last 48h")
            continue

        print(f"  Found {len(new_videos)} new video(s)!")

        for video in new_videos:
            title = video['title']
            video_url = video['url']
            video_id = video['video_id']
            published = video['published']
            handle = channel_handle.lstrip('@')

            if video_id in processed_videos:
                print(f"  Already processed, skipping: {title[:50]}")
                continue

            print(f"  Processing: {title[:60]}...")

            print(f"  Fetching transcript...")
            transcript = fetch_transcript(video_id)

            if not transcript:
                print(f"  No transcript available, skipping")
                continue

            print(f"  Analyzing with Claude...")
            try:
                analysis = analyze_with_claude(transcript, title, handle, video_url, published)
            except Exception as e:
                print(f"  Analysis error: {e}")
                continue

            filepath = save_analysis(handle, title, analysis, video_url, published)
            print(f"  Saved: {filepath.name}")
            save_processed_video(video_id, processed_videos)

            analyses_results.append({
                'channel': handle,
                'title': title,
                'url': video_url,
                'analysis': analysis,
                'filepath': str(filepath)
            })

    print(f"\n{'='*60}")
    print(f"Processed {len(analyses_results)} videos")
    print(f"{'='*60}\n")

    if analyses_results:
        print("Sending email digest...")
        send_email(analyses_results)
    else:
        print("No new videos today — no email sent.")


if __name__ == '__main__':
    main()
