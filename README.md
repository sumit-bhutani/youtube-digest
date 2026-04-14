# YouTube Research Digest

A self-hosted pipeline that monitors YouTube channels daily, fetches transcripts for new long-form videos, generates deep research briefs using Claude AI, and emails you a digest — no YouTube API key required.

## How It Works

1. **Scans your channels** via YouTube RSS feeds
2. **Finds videos published in the last 48 hours** and skips anything under 15 minutes
3. **Fetches transcripts** using `youtube-transcript-api` (falls back to yt-dlp if RSS is unavailable)
4. **Analyzes each transcript** with Claude Sonnet using a structured 5-step research prompt:
   - Executive summary
   - Key insights and takeaways
   - Time-coded breakdown
   - Structured tables (people, companies, concepts mentioned)
   - Critical analysis and strategic reflection
5. **Saves each analysis** as a Markdown file in `analyses/`
6. **Emails a full digest** to your inbox
7. **Deduplicates** via `processed_videos.json` — videos are never emailed twice even with the 48h window

## Prerequisites

- Python 3.9+
- An [Anthropic API key](https://console.anthropic.com/)
- A Gmail account with [App Passwords](https://support.google.com/accounts/answer/185833) enabled
- `yt-dlp` available (installed automatically via requirements)

## Setup

### 1. Clone and install dependencies

```bash
git clone https://github.com/sumit-bhutani/youtube-digest.git
cd youtube-digest
pip install -r requirements.txt
```

### 2. Configure secrets

Create a `.env` file in the project root:

```
ANTHROPIC_API_KEY=your_anthropic_key
GMAIL_ADDRESS=your@gmail.com
GMAIL_APP_PASSWORD=your_gmail_app_password
```

To generate a Gmail App Password: Google Account → Security → 2-Step Verification → App Passwords

### 3. Customize your channels

Edit `channels.txt` — one YouTube handle per line:

```
@lexfridman
@a16z
@LennysPodcast
```

Then update `channel_ids.json` with the corresponding YouTube channel IDs (needed for RSS feeds). You can find a channel's ID by visiting their YouTube page and checking the URL or using a tool like [Comment Picker](https://commentpicker.com/youtube-channel-id.php).

### 4. Run manually

```bash
python analyze_channels.py
```

### 5. Automate with launchd (macOS)

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

Load it:

```bash
launchctl load ~/Library/LaunchAgents/com.youtube.digest.plist
```

For Linux, use a cron job instead:

```bash
0 21 * * * /usr/bin/python3 /path/to/youtube-digest/analyze_channels.py >> /path/to/digest.log 2>&1
```

## Output

Each analysis is saved as a Markdown file:

```
analyses/2026-04-13_LennysPodcast_An_AI_state_of_the_union.md
```

And emailed as a digest with all analyses for the day concatenated.

## File Structure

```
youtube-digest/
├── analyze_channels.py      # Main script
├── channels.txt             # YouTube handles to monitor
├── channel_ids.json         # Pre-resolved channel IDs (for RSS)
├── processed_videos.json    # Tracks analyzed video IDs (dedup)
├── requirements.txt         # Python dependencies
├── .env                     # Secrets (never committed)
├── .gitignore
└── analyses/                # Generated markdown analyses
```

## Customization

- **Change channels** — edit `channels.txt` and `channel_ids.json`
- **Change the analysis prompt** — edit `ANALYSIS_PROMPT` in `analyze_channels.py`
- **Change the minimum video length** — edit the `< 900` threshold in `fetch_transcript()` (900 seconds = 15 minutes)
- **Change the lookback window** — edit `timedelta(hours=48)` in `main()`

## Notes

- No YouTube Data API key required — uses public RSS feeds
- Auto-generated captions can take hours after a video is published; the 48h window ensures nothing is missed
- Runs entirely locally — no cloud infrastructure needed
- RSS feeds work best from residential IPs; cloud servers may be blocked by YouTube
