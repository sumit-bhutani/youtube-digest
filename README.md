# YouTube Research Digest

A fully automated pipeline that monitors 28 curated YouTube channels daily, fetches transcripts for new videos, generates deep research briefs using Claude, and emails a digest to your inbox.

## What It Does

1. **Scans 28 YouTube channels** via RSS feeds (no YouTube API key required)
2. **Finds videos published in the last 48 hours** across all channels
3. **Fetches transcripts** using `youtube-transcript-api` (skips videos under 15 minutes)
4. **Analyzes each transcript** with Claude Sonnet using a structured 5-step research prompt covering executive summary, key insights, time-coded breakdown, structured tables, critical thinking, and strategic reflection
5. **Saves each analysis** as a Markdown file in the `analyses/` directory
6. **Emails a full digest** to your Gmail address
7. **Deduplicates** via `processed_videos.json` — videos are never emailed twice

## Channels Monitored

Covers a curated mix of AI/ML, product, VC/startup, and podcast channels:

20VC, a16z, Acquired, All-In, AI Explained, Andrej Karpathy, BeABetterDev, Bg2Pod, BigThinkPlus, ByteByteGo, Code Emporium, David Senra, Dwarkesh Patel, Grow Product, How I AI, Invest Like the Best, Lenny's Podcast, Lex Fridman, Matthew Berman, No Priors, Peter Yang, Product Thinking, Sourcery VC, Stanford Engineering, TBPN, The Diary of a CEO, This Week in Startups, YC Root Access

See `channels.txt` for the full list of handles.

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure secrets

Create a `.env` file in the project root:

```
ANTHROPIC_API_KEY=your_key_here
GMAIL_ADDRESS=your@gmail.com
GMAIL_APP_PASSWORD=your_app_password
```

To generate a Gmail App Password: Google Account → Security → 2-Step Verification → App Passwords

### 3. Run manually

```bash
python analyze_channels.py
```

### 4. Automate with launchd (macOS)

To run daily at 9pm, create `~/Library/LaunchAgents/com.youtube.digest.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.youtube.digest</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/path/to/youtube-digest/analyze_channels.py</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>21</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/path/to/youtube-digest/digest.log</string>
    <key>StandardErrorPath</key>
    <string>/path/to/youtube-digest/digest.log</string>
    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
```

Then load it:

```bash
launchctl load ~/Library/LaunchAgents/com.youtube.digest.plist
```

## Output

- **Markdown files** saved to `analyses/YYYY-MM-DD_channel_title.md`
- **Email digest** sent to the configured Gmail address with all analyses

## File Structure

```
youtube-digest/
├── analyze_channels.py      # Main script
├── channels.txt             # 28 channel handles
├── channel_ids.json         # Pre-resolved channel IDs
├── processed_videos.json    # Tracks analyzed video IDs (dedup)
├── requirements.txt         # Python dependencies
├── .env                     # Secrets (never committed)
├── .gitignore
└── analyses/                # Generated markdown analyses
```

## Notes

- Videos without available transcripts are skipped (auto-generated captions can take hours after publish — the 48h window ensures they're retried)
- Runs locally via launchd; does not require cloud infrastructure
- RSS feeds are used as primary source; yt-dlp is the fallback
